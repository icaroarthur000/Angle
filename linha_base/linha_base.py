
import cv2
import numpy as np
import warnings
from typing import Tuple, Optional, Dict, List

# Defaults and tunable constants
DEFAULT_WINDOW = 9
DEFAULT_ERR_THRESH = 1.2
DEFAULT_Y_FRAC = 0.4
MIN_VALID_IDXS = 20
EPS_NORMALIZE = 1e-8

def safe_normalize(dx: float, dy: float, eps: float = EPS_NORMALIZE) -> Tuple[float, float]:
    """Normalize vector (dx,dy) safely, avoiding division by zero."""
    dist = np.hypot(dx, dy)
    if dist < eps:
        return 1.0, 0.0
    return dx / dist, dy / dist

def ensure_ordered_contour(gota_pts: np.ndarray, shape: Optional[Tuple[int, int]] = None) -> np.ndarray:
    """
    Robust reconstruction of an ordered external contour.
    - Infers a padded mask if `shape` is None, shifting negative coords into positive space.
    - Clips points to mask bounds to avoid fillPoly errors on edge cases.
    - Returns a contour (N,2) as floats and undoes any applied shift.
    If contour extraction fails, returns the original `gota_pts` (unchanged).
    """
    # Defensive checks
    if gota_pts is None or len(gota_pts) == 0:
        return gota_pts

    if shape is None:
        min_x = int(np.floor(np.min(gota_pts[:, 0])))
        min_y = int(np.floor(np.min(gota_pts[:, 1])))
        max_x = int(np.ceil(np.max(gota_pts[:, 0])))
        max_y = int(np.ceil(np.max(gota_pts[:, 1])))
        pad = 8
        origin_x = min_x - pad
        origin_y = min_y - pad
        w = max_x - min_x + 1 + 2 * pad
        h = max_y - min_y + 1 + 2 * pad
        shape = (max(10, h), max(10, w))
        # Translate points so that mask origin corresponds to (origin_x, origin_y)
        pts_shifted = (gota_pts - np.array([origin_x, origin_y])).astype(np.int32)
        origin = np.array([origin_x, origin_y], dtype=float)
    else:
        pts_shifted = gota_pts.astype(np.int32)
        origin = np.array([0.0, 0.0], dtype=float)

    mask = np.zeros(shape, dtype=np.uint8)

    # Clip to bounds to avoid fillPoly errors if points fell outside mask
    pts_shifted[:, 0] = np.clip(pts_shifted[:, 0], 0, shape[1] - 1)
    pts_shifted[:, 1] = np.clip(pts_shifted[:, 1], 0, shape[0] - 1)

    try:
        cv2.fillPoly(mask, [pts_shifted], 255)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    except Exception:
        return gota_pts

    if not contours:
        return gota_pts

    c = max(contours, key=cv2.contourArea).squeeze()
    if c.ndim == 1:
        c = c.reshape(1, -1)
    c = c.reshape(-1, 2).astype(float)

    # Map contour coordinates back to original image coordinates
    c = c + origin

    return c

def _compute_curvature_at_point(pts: np.ndarray, idx: int, window: int = 3) -> float:
    n = len(pts)
    if idx < window or idx >= n - window:
        return np.nan
    p_prev = pts[idx - window].astype(float)
    p_curr = pts[idx].astype(float)
    p_next = pts[idx + window].astype(float)
    v1 = p_curr - p_prev
    v2 = p_next - p_curr
    denom = (np.linalg.norm(v1) + 1e-8)
    return np.linalg.norm(v2 - v1) / denom

# Duplicate older implementation removed - use the single general version below.
# (The earlier simplistic variant was removed to avoid ambiguity and to centralize
#  contact detection in the general implementation.)

# Removed shorter duplicate implementation of `detectar_baseline_hibrida` to avoid ambiguity
# and keep only the central maestro implementation further below.
# =================================================================
# BLOCO 3: IDENTIFICAÇÃO DE CONTATO (O "Joelho" da Gota)
# ESTE É O PONTO MAIS IMPORTANTE DA SUA METODOLOGIA.


def find_contact_points_by_transition(
    gota_pts: np.ndarray,
    line_params: Optional[Tuple[float, float, float, float]] = None,
    window: int = DEFAULT_WINDOW,
    err_thresh: float = DEFAULT_ERR_THRESH,
    y_frac: float = DEFAULT_Y_FRAC,
    min_valid_idxs: int = MIN_VALID_IDXS,
) -> Tuple[Optional[List[float]], Optional[List[float]]]:
    """
    Robust contact detection that scans contiguously along the ordered contour.
    Parameters exposed for tuning: `window`, `err_thresh`, `y_frac`, `min_valid_idxs`.
    Uses `line_params` (if provided) to pick a stable center near the fitted line.
    Returns (p_esq, p_dir) where each is None or [float(x), float(y)].
    """
    def _as_point(p):
        return None if p is None else [float(p[0]), float(p[1])]

    def _norm_pt(p):
        """Ensure a point is a float list or None for stable downstream usage."""
        if p is None:
            return None
        return [float(p[0]), float(p[1])]

    # 3.1 Ensure contour ordered and float
    contour = ensure_ordered_contour(gota_pts).astype(float)

    # 3.2 Define lower region by Y (keep indices to preserve contour sequence)
    y_min, y_max = np.min(contour[:, 1]), np.max(contour[:, 1])
    y_lim = y_min + y_frac * (y_max - y_min)
    valid_idxs = np.where(contour[:, 1] >= y_lim)[0]
    # Defensive: ignore only a few bottom-most image rows to avoid discarding
    # valid base if the crop is tight against the droplet edge.
    bottom_ignore_px = 1
    if len(valid_idxs) > 0:
        keep_mask = contour[valid_idxs, 1] <= (y_max - bottom_ignore_px)
        valid_idxs = valid_idxs[keep_mask]
    if len(valid_idxs) < min_valid_idxs:
        warnings.warn(f"find_contact_points_by_transition: too few valid bottom points ({len(valid_idxs)}); returning (None, None)")
        return None, None

    # 3.3 Find a stable center index
    if line_params is not None:
        vx, vy, x0, y0 = line_params
        pts_valid = contour[valid_idxs]
        normal = np.array([-vy, vx])
        nnorm = np.linalg.norm(normal)
        if nnorm < 1e-12:
            normal = np.array([0.0, 1.0])
        dists = np.abs((pts_valid - np.array([x0, y0])) @ normal)
        center_pos = int(np.argmin(dists))
    else:
        xs = contour[valid_idxs, 0]
        x_mean = float(np.mean(xs))
        # center_pos is an index within valid_idxs (position), not a global contour index
        center_pos = int(np.argmin(np.abs(xs - x_mean)))

    # 3.4 Local detector: scans along valid_idxs towards left/right
    def detect_contact_by_local_line(contour, valid_idxs, center_pos, is_left=True, window=window, err_thresh=err_thresh):
        """Deterministic contact selection using a global per-point score.

        For every index in `valid_idxs` we compute three geometric quantities:
         - mean orthogonal error to the local best-fit line (SVD)
         - normal verticality term (|normal_y|)
         - local curvature (via `_compute_curvature_at_point`)

        A single scalar score is formed per candidate:
            score = w_err * err + w_vert * (1 - |normal_y|) + w_curv * curv
        Lower scores are better (more substrate-like: low error, normal near vertical, low curvature).

        Selection rule (deterministic): choose the index with the minimum score on the
        left side (indices < center_pos) and the index with the minimum score on the
        right side (indices > center_pos). No early returns, no scan-order dependence.
        """
        n_valid = len(valid_idxs)
        if n_valid == 0:
            return None

        # Weights for the scalar score (choose deterministic, tunable constants)
        w_err = 1.0
        w_vert = 1.0
        # Prioritize curvature to prefer the last curved point before flat substrate
        w_curv = 3.0

        min_points_in_window = 5
        very_large_score = 1e6

        # First pass: compute raw terms for each valid position and store in arrays.
        n_valid = len(valid_idxs)
        err_arr = np.full((n_valid,), very_large_score, dtype=float)
        vert_arr = np.full((n_valid,), very_large_score, dtype=float)  # stores (1 - |normal_y|)
        curv_arr = np.full((n_valid,), very_large_score, dtype=float)

        half = max(1, window // 2)
        for i_pos in range(n_valid):
            global_idx = int(valid_idxs[i_pos])
            win_start = max(0, i_pos - half)
            win_end = min(n_valid, i_pos + half + 1)
            win_idx = valid_idxs[win_start:win_end]

            if len(win_idx) < min_points_in_window:
                # too small window -> leave large sentinel values
                continue

            pts = contour[win_idx]
            centroid = pts.mean(axis=0)

            try:
                U, s, Vt = np.linalg.svd(pts - centroid)
            except np.linalg.LinAlgError:
                continue

            # principal normal (unit length)
            normal = Vt[1] if Vt.shape[0] > 1 else Vt[0]
            n_norm = np.linalg.norm(normal)
            if n_norm < 1e-12:
                continue
            normal = normal / n_norm

            # error: mean orthogonal distance to the local line
            distances = np.abs((pts - centroid) @ normal)
            err = float(np.mean(distances))

            # verticality term stored as (1 - |normal_y|)
            normal_y = abs(normal[1])
            vert_term = 1.0 - normal_y

            # curvature computed only on the local valid window (local angular variation)
            try:
                local_center_pos = int(np.where(win_idx == global_idx)[0][0])
            except Exception:
                curv = float(1e3)
            else:
                k_candidate = min(local_center_pos, len(win_idx) - 1 - local_center_pos, max(1, window // 2))
                if k_candidate < 1:
                    curv = float(1e3)
                else:
                    k = int(k_candidate)
                    if (local_center_pos - k) < 0 or (local_center_pos + k) >= len(pts):
                        curv = float(1e3)
                    else:
                        p_prev = pts[local_center_pos - k].astype(float)
                        p_curr = pts[local_center_pos].astype(float)
                        p_next = pts[local_center_pos + k].astype(float)
                        v1 = p_curr - p_prev
                        v2 = p_next - p_curr
                        n1 = np.linalg.norm(v1)
                        n2 = np.linalg.norm(v2)
                        if n1 < 1e-8 or n2 < 1e-8:
                            curv = float(1e3)
                        else:
                            cosang = np.clip(np.dot(v1, v2) / (n1 * n2), -1.0, 1.0)
                            angle = float(np.arccos(cosang))
                            curv = angle

            err_arr[i_pos] = err
            vert_arr[i_pos] = vert_term
            curv_arr[i_pos] = float(curv)

        # Normalize each term using the P95 percentile over VALID entries to avoid dominance
        eps = 1e-8
        valid_mask = (err_arr < very_large_score / 2) & (curv_arr < very_large_score / 2)

        if np.any(valid_mask):
            p95_err = float(np.percentile(err_arr[valid_mask], 95))
            p95_vert = float(np.percentile(vert_arr[valid_mask], 95))
            p95_curv = float(np.percentile(curv_arr[valid_mask], 95))

            denom_err = max(p95_err, eps)
            denom_vert = max(p95_vert, eps)
            denom_curv = max(p95_curv, eps)

            norm_err = err_arr / denom_err
            norm_vert = vert_arr / denom_vert
            norm_curv = curv_arr / denom_curv
        else:
            # No valid windows: keep large normalized values so they won't be chosen
            norm_err = np.full_like(err_arr, very_large_score)
            norm_vert = np.full_like(vert_arr, very_large_score)
            norm_curv = np.full_like(curv_arr, very_large_score)

        # Final deterministic score (lower is better)
        scores = (w_err * norm_err) + (w_vert * norm_vert) + (w_curv * norm_curv)

        # Now pick the CONTACT by detecting a CURVE->FLAT transition (deterministic)
        # We define a "flat" threshold from the scores distribution (P25). Then,
        # starting from the center we scan outward to find the first contiguous
        # flat run; the contact is the index immediately before this run.
        left_candidate = None
        right_candidate = None

        valid_score_mask = scores < (very_large_score / 2)
        if np.any(valid_score_mask):
            plane_thresh = float(np.percentile(scores[valid_score_mask], 25))
        else:
            plane_thresh = float(np.percentile(scores, 25))

        # Minimum length of a flat run to be considered a valid substrate region
        # Require at least 3 consecutive flat windows to reduce sensitivity to noise
        min_flat_len = max(3, window // 3)


        # left side: scan from center_pos-1 down to 0
        for pos in range(int(center_pos) - 1, -1, -1):
            if scores[pos] <= plane_thresh:
                # found start of a flat run (closest to center)
                run_start = pos
                run_end = pos
                # extend the flat run outward (decreasing indices)
                while run_start - 1 >= 0 and scores[run_start - 1] <= plane_thresh:
                    run_start -= 1
                run_len = run_end - run_start + 1
                if run_len >= min_flat_len:
                    contact_pos = run_end + 1  # index immediately before flat run (towards center)
                    if contact_pos <= int(center_pos) - 1 and contact_pos >= 0:
                        global_idx = int(valid_idxs[contact_pos])
                        left_candidate = [float(contour[global_idx, 0]), float(contour[global_idx, 1])]
                        break
                # otherwise treat this small flat as noise and continue searching

        # fallback for left if no transition found: pick minimal score on left (deterministic)
        if left_candidate is None:
            left_mask = np.arange(n_valid) < int(center_pos)
            if np.any(left_mask):
                left_idx = int(np.argmin(scores[left_mask]))
                left_positions = np.where(left_mask)[0]
                chosen_pos = left_positions[left_idx]
                global_idx = int(valid_idxs[chosen_pos])
                left_candidate = [float(contour[global_idx, 0]), float(contour[global_idx, 1])]

        # right side: scan from center_pos+1 up to n_valid-1
        for pos in range(int(center_pos) + 1, n_valid):
            if scores[pos] <= plane_thresh:
                run_start = pos
                run_end = pos
                # extend the flat run outward (increasing indices)
                while run_end + 1 < n_valid and scores[run_end + 1] <= plane_thresh:
                    run_end += 1
                run_len = run_end - run_start + 1
                if run_len >= min_flat_len:
                    contact_pos = run_start - 1  # index immediately before flat run (towards center)
                    if contact_pos >= int(center_pos) + 1 and contact_pos < n_valid:
                        global_idx = int(valid_idxs[contact_pos])
                        right_candidate = [float(contour[global_idx, 0]), float(contour[global_idx, 1])]
                        break
                # else small flat = noise; continue

        # fallback for right if no transition found: pick minimal score on right (deterministic)
        if right_candidate is None:
            right_mask = np.arange(n_valid) > int(center_pos)
            if np.any(right_mask):
                right_idx = int(np.argmin(scores[right_mask]))
                right_positions = np.where(right_mask)[0]
                chosen_pos = right_positions[right_idx]
                global_idx = int(valid_idxs[chosen_pos])
                right_candidate = [float(contour[global_idx, 0]), float(contour[global_idx, 1])]

        return left_candidate if is_left else right_candidate

    p_esq = detect_contact_by_local_line(contour, valid_idxs, center_pos, is_left=True, window=window, err_thresh=err_thresh)
    p_dir = detect_contact_by_local_line(contour, valid_idxs, center_pos, is_left=False, window=window, err_thresh=err_thresh)

    # Sanity check: left and right contact heights should be similar (avoid bad detections)
    if p_esq is not None and p_dir is not None:
        if abs(p_esq[1] - p_dir[1]) > 5:
            warnings.warn("find_contact_points_by_transition: left/right contact heights differ by >5 px")

    return _as_point(p_esq), _as_point(p_dir)

# =================================================================
# BLOCO 4: O MAESTRO (Função Híbrida)
# Aqui o software decide qual estratégia usar.
# =================================================================

def detectar_baseline_hibrida(gota_pts: np.ndarray) -> Dict:
    """
    Orquestra o pipeline:
    1. Acha a inclinação do chão (TLS).
    2. Acha os pontos de contato reais (Transição).
    3. Redefine a altura da linha base para os contatos reais (Precisão Científica).
    """
    def _norm_pt(p):
        """Ensure a point is a float list or None."""
        if p is None:
            return None
        return [float(p[0]), float(p[1])]

    if len(gota_pts) < 10: return {'method': 'error', 'p_esq': None, 'p_dir': None}

    # NOTE: avoid double-ordering: `find_contact_points_by_transition` will
    # call `ensure_ordered_contour` internally for safety when needed.

    # Primeiro tente uma estratégia determinística baseada apenas nos contatos
    p_esq, p_dir = find_contact_points_by_transition(gota_pts)
    if p_esq and p_dir:
        dx = p_dir[0] - p_esq[0]
        dy = p_dir[1] - p_esq[1]
        vx, vy = safe_normalize(dx, dy)
        x0, y0 = (p_esq[0] + p_dir[0]) / 2.0, (p_esq[1] + p_dir[1]) / 2.0
        return {
            'line_params': (float(vx), float(vy), float(x0), float(y0)),
            'baseline_y': y0,
            'method': 'deterministic_transition',
            'contact_method': 'geometric_transition',
            'p_esq': _norm_pt(p_esq), 'p_dir': _norm_pt(p_dir),
            'r_squared': 1.0
        }

    # Tenta o método principal (Científico)
    try:
        candidates = select_baseline_candidates(gota_pts)
        line_params, r_squared = fit_baseline_tls_explicit(candidates)
    except Exception:
        # Any failure here (missing helper or bad data) causes graceful fallback
        line_params, r_squared = None, 0.0

    if line_params is not None and r_squared >= 0.6:
        p_esq, p_dir = find_contact_points_by_transition(gota_pts, line_params)
        
        if p_esq and p_dir:
            # Enforce contract: when contacts are available, the final baseline
            # position and line parameters must be derived from the contacts
            dx = p_dir[0] - p_esq[0]
            dy = p_dir[1] - p_esq[1]
            vx, vy = safe_normalize(dx, dy)
            x0, y0 = (p_esq[0] + p_dir[0]) / 2.0, (p_esq[1] + p_dir[1]) / 2.0
            baseline_y = y0
            return {
                'line_params': (float(vx), float(vy), float(x0), float(y0)),
                'baseline_y': baseline_y,
                'method': 'tls_transition',
                'contact_method': 'geometric_transition',
                'p_esq': _norm_pt(p_esq), 'p_dir': _norm_pt(p_dir),
                'r_squared': r_squared
            }

    # Se tudo falhar, usa o Fallback (Segurança)
    y_fallback = detectar_baseline_cintura(gota_pts)
    p_esq, p_dir = encontrar_pontos_contato(gota_pts, y_fallback)
    # If we have both contacts from the fallback, synthesize a line_params
    if p_esq is not None and p_dir is not None:
        dx = p_dir[0] - p_esq[0]
        dy = p_dir[1] - p_esq[1]
        vx, vy = safe_normalize(dx, dy)
        # Use o centro horizontal da gota (mais estável que a média dos contatos)
        try:
            x0 = float(np.mean(gota_pts[:, 0]))
        except Exception:
            x0 = (p_esq[0] + p_dir[0]) / 2.0
        y0 = (p_esq[1] + p_dir[1]) / 2.0
        lp = (float(vx), float(vy), float(x0), float(y0))
    else:
        lp = None
    return {
        'line_params': lp, 'baseline_y': y_fallback,
        'method': 'fallback_cintura', 'contact_method': 'cintura_fallback',
        'p_esq': _norm_pt(p_esq), 'p_dir': _norm_pt(p_dir)
    }

def detectar_baseline_cintura(gota_pts: np.ndarray) -> float:
    """Procura a menor largura na base. Útil quando o substrato está invisível."""
    # OpenCV expects CV_32F or CV_32S for point sets; cast to int32 for robustness
    pts = gota_pts.astype(np.int32)
    x, y, w, h = cv2.boundingRect(pts)
    min_width = float('inf')
    # Start at 85% of height to stay well away from noisy bottom
    y_res = float(y + h * 0.85)
    # Search for the droplet "neck" (minimum width region) between 70-85% of height
    # This region typically marks the transition from curved body to substrate
    row_start = int(y + h * 0.70)
    row_end = int(y + h * 0.85)
    step = max(1, h // 100)
    for row in range(row_start, row_end, step):
        row_pts = gota_pts[np.abs(gota_pts[:, 1] - row) < 2]
        if len(row_pts) >= 2:
            width = np.max(row_pts[:, 0]) - np.min(row_pts[:, 0])
            if width < min_width:
                min_width = width
                y_res = float(row)

    # If our found baseline is too close to the image bottom, recompute using
    # the lowest contour points while explicitly excluding the last few rows
    # which often belong to the background/frame.
    bottom_ignore_px = 1
    y_bottom = float(y + h)
    if y_res >= (y_bottom - bottom_ignore_px):
        # select candidate points that are below the bulk but above the ignored rows
        candidates = gota_pts[gota_pts[:, 1] <= (y_bottom - bottom_ignore_px)]
        if len(candidates) >= 2:
            # take a high percentile of these to approximate the lowest meaningful row
            y_res = float(np.percentile(candidates[:, 1], 95))
        else:
            # fallback: use 85% height, not the extreme bottom pixel
            y_res = float(y + h * 0.85)

    return y_res

def encontrar_pontos_contato(gota_pts: np.ndarray, baseline_y: float) -> Tuple:
    """Apenas localiza os extremos horizontais em uma altura Y fixa."""
    base_pts = gota_pts[np.abs(gota_pts[:, 1] - baseline_y) < 5]
    if len(base_pts) > 0:
        return [float(np.min(base_pts[:, 0])), baseline_y], [float(np.max(base_pts[:, 0])), baseline_y]
    pts = gota_pts.astype(np.int32)
    x, y, w, h = cv2.boundingRect(pts)
    return [float(x), baseline_y], [float(x + w), baseline_y]


def debug_plot_contact(contour, p_esq, p_dir):
    """Minimal debug plot for quick visual inspection of detected contacts."""
    try:
        import matplotlib.pyplot as plt
    except Exception:
        warnings.warn('debug_plot_contact: matplotlib not available')
        return
    plt.figure(figsize=(5, 5))
    plt.plot(contour[:, 0], contour[:, 1], '-k', linewidth=1)
    if p_esq:
        plt.scatter(p_esq[0], p_esq[1], c='r', s=50)
    if p_dir:
        plt.scatter(p_dir[0], p_dir[1], c='b', s=50)
    plt.gca().invert_yaxis()
    plt.axis('equal')
    plt.show()