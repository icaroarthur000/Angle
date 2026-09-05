from typing import Union, Tuple, Dict, Optional
import math
import logging
import warnings

import numpy as np
from parametros import obter

logger = logging.getLogger(__name__)

_AUDIT_CONTEXT: Dict[str, object] = {}


def set_audit_context(**kwargs) -> Dict[str, object]:
    """Armazena contexto de auditoria para inspeÃ§Ã£o externa sem alterar o fluxo principal."""
    global _AUDIT_CONTEXT
    _AUDIT_CONTEXT.update(kwargs)
    return dict(_AUDIT_CONTEXT)


def get_audit_context() -> Dict[str, object]:
    """Retorna o contexto de auditoria atual."""
    return dict(_AUDIT_CONTEXT)

ANGLE_BASELINE_OFFSET_FACTOR = float(obter("angle_baseline_offset_factor", 0.01))
ANGLE_CONTACT_CANDIDATE_MAX_DIST = float(obter("angle_contact_candidate_max_dist", 25.0))
ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL = float(obter("angle_contact_candidate_max_vertical", 12.0))
ANGLE_CONTACT_LOCAL_WINDOW_SIZES = tuple(int(v) for v in obter("angle_contact_local_window_sizes", "7,9,11,13,15,17").split(",") if str(v).strip())
ANGLE_CONTACT_MIN_WINDOW_POINTS = int(obter("angle_contact_min_window_points", 4))
ANGLE_CONTACT_MIN_R2 = float(obter("angle_contact_min_r2", 0.70))
ANGLE_CONTACT_MAX_RMSE = float(obter("angle_contact_max_rmse", 3.0))
ANGLE_CONTACT_MAX_COND = float(obter("angle_contact_max_cond", 1e8))
ANGLE_BASELINE_OFFSET_MIN = float(obter("angle_baseline_offset_min", 1.5))
ANGLE_BASELINE_OFFSET_MAX = float(obter("angle_baseline_offset_max", 4.0))
ANGLE_WINDOW_HEIGHT_FACTOR = float(obter("angle_window_height_factor", 0.55))
ANGLE_WINDOW_HEIGHT_MIN = int(obter("angle_window_height_min", 70))
ANGLE_WINDOW_HEIGHT_MAX = int(obter("angle_window_height_max", 220))
ANGLE_OUTLIER_SIGMA_SCALE = float(obter("angle_outlier_sigma_scale", 2.0))
QUALITY_RMSE_REF_PX = float(obter("quality_rmse_ref_px", 3.0))
QUALITY_MIN_SCORE = float(obter("quality_min_score", 0.0))
QUALITY_MAX_SCORE = float(obter("quality_max_score", 1.0))


def validar_candidato_contato(
    contour_pts: np.ndarray,
    candidate: Union[list, tuple, np.ndarray],
    reference_contact: Union[list, tuple, np.ndarray],
    baseline_y: float,
    lado: str,
) -> Optional[Dict[str, object]]:
    if contour_pts is None or len(contour_pts) < 4:
        return None
    if candidate is None or len(candidate) < 2:
        return None
    if reference_contact is None or len(reference_contact) < 2:
        return None

    contour_arr = np.asarray(contour_pts, dtype=float)
    candidate_pt = np.asarray(candidate, dtype=float).reshape(1, 2)
    ref_pt = np.asarray(reference_contact, dtype=float).reshape(1, 2)

    dist_to_ref = float(np.linalg.norm(candidate_pt[0] - ref_pt[0]))
    dist_to_contour = float(np.min(np.linalg.norm(contour_arr - candidate_pt[0], axis=1)))
    vertical_to_baseline = float(abs(candidate_pt[0, 1] - baseline_y))

    if not np.isfinite(dist_to_ref) or not np.isfinite(dist_to_contour):
        return {"is_valid": False, "reason": "invalido", "dist_to_ref": dist_to_ref, "dist_to_contour": dist_to_contour, "vertical_to_baseline": vertical_to_baseline}
    if vertical_to_baseline > ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL:
        return {"is_valid": False, "reason": "deslocado_da_regiao_de_contato", "dist_to_ref": dist_to_ref, "dist_to_contour": dist_to_contour, "vertical_to_baseline": vertical_to_baseline}
    if dist_to_ref > ANGLE_CONTACT_CANDIDATE_MAX_DIST:
        return {"is_valid": False, "reason": "deslocado_da_regiao_de_contato", "dist_to_ref": dist_to_ref, "dist_to_contour": dist_to_contour, "vertical_to_baseline": vertical_to_baseline}
    if dist_to_contour > ANGLE_CONTACT_CANDIDATE_MAX_DIST:
        return {"is_valid": False, "reason": "distante_do_contorno", "dist_to_ref": dist_to_ref, "dist_to_contour": dist_to_contour, "vertical_to_baseline": vertical_to_baseline}

    x_center = float(np.mean(contour_arr[:, 0]))
    if lado == "esq" and candidate_pt[0, 0] > x_center:
        return {"is_valid": False, "reason": "deslocado_da_regiao_de_contato", "dist_to_ref": dist_to_ref, "dist_to_contour": dist_to_contour, "vertical_to_baseline": vertical_to_baseline}
    if lado == "dir" and candidate_pt[0, 0] < x_center:
        return {"is_valid": False, "reason": "deslocado_da_regiao_de_contato", "dist_to_ref": dist_to_ref, "dist_to_contour": dist_to_contour, "vertical_to_baseline": vertical_to_baseline}

    return {"is_valid": True, "reason": "ok", "dist_to_ref": dist_to_ref, "dist_to_contour": dist_to_contour, "vertical_to_baseline": vertical_to_baseline}


def _selecionar_janela_local(contour_pts: np.ndarray, p_contato: Union[list, tuple], baseline_y: float, lado: str) -> Tuple[np.ndarray, Dict[str, object]]:
    if contour_pts is None or len(contour_pts) < 4:
        return np.empty((0, 2), dtype=float), {"window_size": 0, "reason": "sem_contorno"}
    contour_arr = np.asarray(contour_pts, dtype=float)
    contato = np.asarray(p_contato[:2], dtype=float)
    distances = np.hypot(contour_arr[:, 0] - contato[0], contour_arr[:, 1] - contato[1])
    anchor_idx = int(np.argmin(distances))

    for window_size in ANGLE_CONTACT_LOCAL_WINDOW_SIZES:
        if window_size < ANGLE_CONTACT_MIN_WINDOW_POINTS:
            continue
        half = window_size // 2
        indices = [(anchor_idx + offset) % len(contour_arr) for offset in range(-half, half + 1)]
        selected = contour_arr[indices]
        ys = selected[:, 1]
        xs = selected[:, 0]
        if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
            continue
        try:
            coeffs = np.polyfit(ys, xs, 2)
        except (np.linalg.LinAlgError, ValueError):
            continue
        x_fit = np.polyval(coeffs, ys)
        resid = x_fit - xs
        rmse = float(np.sqrt(np.mean(resid ** 2)))
        ss_res = float(np.sum(resid ** 2))
        ss_tot = float(np.sum((xs - np.mean(xs)) ** 2))
        r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 0 else float("nan")
        X = np.column_stack([ys ** 2, ys, np.ones_like(ys)])
        try:
            cond = float(np.linalg.cond(X))
        except np.linalg.LinAlgError:
            cond = float("inf")
        if not np.isfinite(r2) or r2 < ANGLE_CONTACT_MIN_R2:
            continue
        if rmse > ANGLE_CONTACT_MAX_RMSE:
            continue
        if not np.isfinite(cond) or cond > ANGLE_CONTACT_MAX_COND:
            continue
        return selected, {"window_size": window_size, "reason": "ok", "rmse": rmse, "r2": r2, "cond": cond}

    return contour_arr[[anchor_idx]], {"window_size": 1, "reason": "fallback_ancora"}


def ajustar_circulo_algebrico(pontos: np.ndarray) -> Tuple[float, float, float]:
    if len(pontos) < 3:
        raise ValueError("Poucos pontos para ajuste circular.")

    x = pontos[:, 0]
    y = pontos[:, 1]
    xm = np.mean(x)
    ym = np.mean(y)
    u = x - xm
    v = y - ym
    Suu = np.sum(u**2)
    Svv = np.sum(v**2)
    Suv = np.sum(u * v)
    Suuu = np.sum(u**3)
    Svvv = np.sum(v**3)
    Suvv = np.sum(u * v**2)
    Suuv = np.sum(u**2 * v)
    A = np.array([[Suu, Suv], [Suv, Svv]])
    B = np.array([Suuu + Suvv, Svvv + Suuv]) / 2.0
    try:
        uc, vc = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        return 0.0, 0.0, 0.0
    xc = xm + uc
    yc = ym + vc
    dist = np.sqrt((x - xc) ** 2 + (y - yc) ** 2)
    R = np.mean(dist)
    return float(xc), float(yc), float(R)


def _selecionar_ponto_contato_robusto(
    contour_pts: np.ndarray,
    p_contato: Optional[Union[list, tuple]] = None,
    baseline_y: float = 0.0,
    lado: str = "esq",
) -> np.ndarray:
    if contour_pts is None or len(contour_pts) < 4:
        return np.empty((0, 2), dtype=float)
    if p_contato is None or len(p_contato) < 2:
        return np.empty((0, 2), dtype=float)

    contour_arr = np.asarray(contour_pts, dtype=float)
    contato_ref = np.asarray(p_contato[:2], dtype=float)
    pool = [contato_ref]
    nearby_mask = np.linalg.norm(contour_arr - contato_ref, axis=1) <= ANGLE_CONTACT_CANDIDATE_MAX_DIST
    pool.extend(contour_arr[nearby_mask])

    if lado == "esq":
        near_baseline = contour_arr[np.abs(contour_arr[:, 1] - baseline_y) <= ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL]
        pool.extend(near_baseline[near_baseline[:, 0] <= contato_ref[0]])
    else:
        near_baseline = contour_arr[np.abs(contour_arr[:, 1] - baseline_y) <= ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL]
        pool.extend(near_baseline[near_baseline[:, 0] >= contato_ref[0]])

    best_point = contato_ref
    best_score = None
    for candidate in pool:
        validation = validar_candidato_contato(contour_arr, candidate, contato_ref, baseline_y, lado)
        if validation is None or not validation.get("is_valid", False):
            continue
        score = float(validation.get("dist_to_ref", 0.0)) + 0.5 * float(validation.get("dist_to_contour", 0.0)) + 0.25 * float(validation.get("vertical_to_baseline", 0.0))
        if best_score is None or score < best_score:
            best_score = score
            best_point = np.asarray(candidate, dtype=float)
    return best_point.astype(float)


def _selecionar_pontos_tangente(
    local_pts: np.ndarray,
    baseline_y: float,
    p_contato: Optional[Union[list, tuple]] = None,
    contour_pts: Optional[np.ndarray] = None,
    lado: str = "esq",
    profile_open: bool = False,
) -> np.ndarray:
    """Seleciona uma janela contínua e local do contorno ao redor do ponto de contato para o polyfit."""
    if local_pts is None or len(local_pts) < 3:
        return np.empty((0, 2), dtype=float)

    points = np.asarray(local_pts, dtype=float)
    parent = np.asarray(contour_pts if contour_pts is not None else local_pts, dtype=float)
    if len(parent) == 0 or len(points) == 0:
        return np.empty((0, 2), dtype=float)

    # Um perfil extraído já está ordenado e aberto; não o reinterprete como
    # contorno cíclico nem procure um ramo alternativo no fechamento.
    if profile_open:
        if p_contato is None or len(p_contato) < 2:
            selected_points = points[: min(7, len(points))]
        else:
            contact_local_idx = int(np.argmin(np.linalg.norm(points - np.asarray(p_contato[:2], dtype=float), axis=1)))
            window_size = min(7, len(points))
            start_idx = max(0, min(contact_local_idx - window_size // 2, len(points) - window_size))
            selected_points = points[start_idx:start_idx + window_size]
        if len(selected_points) >= 4:
            set_audit_context(last_tangent_selection={
                "contact_idx": contact_local_idx if p_contato is not None and len(p_contato) >= 2 else 0,
                "selected_indices": list(range(start_idx, start_idx + len(selected_points))) if p_contato is not None and len(p_contato) >= 2 else list(range(len(selected_points))),
                "selected_count": int(len(selected_points)),
                "contiguous": True,
                "profile_open": True,
                "selected_points": selected_points.astype(float),
            })
        return selected_points

    if p_contato is None or len(p_contato) < 2:
        return points[: min(16, len(points))]

    contato = np.asarray(p_contato[:2], dtype=float)
    if not np.isfinite(contato).all():
        return points[: min(16, len(points))]

    contact_idx = int(np.argmin(np.hypot(parent[:, 0] - contato[0], parent[:, 1] - contato[1])))
    dist_to_contact = float(np.min(np.hypot(parent[:, 0] - contato[0], parent[:, 1] - contato[1])))
    if not np.isfinite(contact_idx) or dist_to_contact > 12.0:
        return points[: min(16, len(points))]

    lookup = {tuple(np.round(point, 6)) for point in points}
    candidate_indices = [idx for idx in range(len(parent)) if tuple(np.round(parent[idx], 6)) in lookup]
    if candidate_indices:
        candidate_indices = sorted(candidate_indices)
        candidate_runs = []
        current_run = [candidate_indices[0]]
        for idx in candidate_indices[1:]:
            if idx == current_run[-1] + 1:
                current_run.append(idx)
            else:
                candidate_runs.append(current_run)
                current_run = [idx]
        candidate_runs.append(current_run)

        selected_run = None
        for run in candidate_runs:
            if contact_idx in run and 4 <= len(run) <= 12:
                selected_run = run
                break

        if selected_run is not None:
            selected_indices = list(selected_run)
            selected_points = parent[selected_indices]
        else:
            window_size = min(7, len(parent))
            start_idx = contact_idx if contact_idx <= 6 else max(0, contact_idx - 4)
            end_idx = min(len(parent), start_idx + window_size)
            if end_idx - start_idx < 4:
                start_idx = max(0, len(parent) - window_size)
                end_idx = len(parent)
            selected_indices = list(range(start_idx, end_idx))
            selected_points = parent[selected_indices]
    else:
        window_size = min(7, len(parent))
        if contact_idx <= 6:
            start_idx = contact_idx
        else:
            start_idx = max(0, contact_idx - 4)
        end_idx = min(len(parent), start_idx + window_size)
        if end_idx - start_idx < 4:
            start_idx = max(0, len(parent) - window_size)
            end_idx = len(parent)
        selected_indices = list(range(start_idx, end_idx))
        selected_points = parent[selected_indices]

    if len(selected_points) < 4:
        window_size = min(7, len(parent))
        selected_indices = list(range(min(len(parent), window_size)))
        selected_points = parent[selected_indices]

    selection_debug = {
        "contact_idx": int(np.argmin(np.hypot(parent[:, 0] - contato[0], parent[:, 1] - contato[1]))),
        "selected_indices": [int(idx) for idx in selected_indices],
        "selected_count": int(len(selected_indices)),
        "mean_dist_to_contact": float(np.mean(np.hypot(selected_points[:, 0] - contato[0], selected_points[:, 1] - contato[1]))) if len(selected_points) else 0.0,
        "max_dist_to_contact": float(np.max(np.hypot(selected_points[:, 0] - contato[0], selected_points[:, 1] - contato[1]))) if len(selected_points) else 0.0,
        "contiguous": len(selected_indices) <= 1 or all((selected_indices[i] + 1) % len(parent) == selected_indices[i + 1] for i in range(len(selected_indices) - 1)),
        "selected_points": selected_points.astype(float),
    }
    set_audit_context(last_tangent_selection=selection_debug)

    return selected_points


def _calcular_slope_tangente_polynomial(
    local_pts: np.ndarray,
    baseline_y: float,
    lado: str,
    p_contato: Optional[Union[list, tuple]] = None,
    contour_pts: Optional[np.ndarray] = None,
    profile_open: bool = False,
) -> Optional[Tuple[float, np.ndarray, np.ndarray]]:
    """Calcula a inclinaï¿½ï¿½o da tangente usando ajuste x = f(y) na regiï¿½o de contato."""
    if local_pts is None or len(local_pts) < 3:
        return None

    pts = _selecionar_pontos_tangente(
        local_pts, baseline_y, p_contato, contour_pts,
        lado=lado, profile_open=profile_open
    )
    if len(pts) < 4:
        pts = np.asarray(local_pts, dtype=float)

    ys = pts[:, 1]
    xs = pts[:, 0]
    if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
        return None

    try:
        coeffs = np.polyfit(ys, xs, 2)
    except (np.linalg.LinAlgError, ValueError):
        return None

    a, b = coeffs[0], coeffs[1]
    y_derivada = float(p_contato[1]) if p_contato is not None and len(p_contato) >= 2 else float(baseline_y)
    dx_dy = 2.0 * a * y_derivada + b

    if not np.isfinite(dx_dy):
        return None
    if abs(dx_dy) < 1e-9:
        m_tangente = float("inf")
    else:
        m_tangente = 1.0 / dx_dy

    logger.debug(
        "[TANGENTE] lado=%s pts=%d coeffs=%s dx_dy=%.6f m_tangente=%.6f",
        lado, len(pts), np.array2string(coeffs, precision=4), dx_dy, m_tangente
    )

    return m_tangente, coeffs, pts


def _calcular_angulo_polynomial_fallback(local_pts: np.ndarray, baseline_y: float, lado: str) -> float:
    if local_pts is None or len(local_pts) < 3:
        return 0.0
    ys = local_pts[:, 1]
    xs = local_pts[:, 0]
    if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
        return 0.0
    try:
        coeffs = np.polyfit(ys, xs, 2)
    except (np.linalg.LinAlgError, ValueError):
        return 0.0
    a, b = coeffs[0], coeffs[1]
    dx_dy = 2.0 * a * baseline_y + b
    if abs(dx_dy) < 1e-9:
        theta = 90.0
    else:
        theta = math.degrees(math.atan(1.0 / dx_dy))
    if theta < 0:
        theta = abs(theta)
    return float(np.clip(theta, 0.0, 180.0))


def _normalizar_vetor_tangente(m_tangente: float) -> Tuple[float, float]:
    if not np.isfinite(m_tangente):
        return 0.0, 1.0
    vx = 1.0
    vy = float(m_tangente)
    norm = math.hypot(vx, vy)
    if norm < 1e-9:
        return 1.0, 0.0
    return vx / norm, vy / norm


def _calcular_angulo_interno_por_vetor_tangente(tangent_vec: np.ndarray, lado: str) -> float:
    tangent_vec = np.asarray(tangent_vec, dtype=float).reshape(-1)
    if tangent_vec.size != 2:
        return 0.0

    vx, vy = float(tangent_vec[0]), float(tangent_vec[1])
    if abs(vx) < 1e-12 and abs(vy) < 1e-12:
        return 90.0

    angle = math.degrees(math.atan2(vy, vx))
    if angle < 0.0:
        angle += 180.0

    if vx < 0.0:
        angle = 180.0 - angle

    return float(np.clip(angle, 0.0, 180.0))


def _angulo_interno_pelo_centro(theta_deg: float, yc: float, y_contato: float) -> float:
    theta_deg = float(np.clip(theta_deg, 0.0, 180.0))
    if yc < y_contato - 1.0:
        theta_deg = 180.0 - theta_deg
    return float(np.clip(theta_deg, 0.0, 180.0))


def _selecionar_pontos_lado(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_ajustada: float,
    lado: str,
) -> np.ndarray:
    if gota_pts is None or len(gota_pts) < 1:
        return np.empty((0, 2), dtype=float)
    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    window_height = int(np.clip(ANGLE_WINDOW_HEIGHT_FACTOR * altura_gota, ANGLE_WINDOW_HEIGHT_MIN, ANGLE_WINDOW_HEIGHT_MAX))
    mask = (gota_pts[:, 1] <= baseline_ajustada) & (gota_pts[:, 1] > baseline_ajustada - window_height)
    local_pts = gota_pts[mask]
    center_x_approx = (p_esq[0] + p_dir[0]) / 2
    if lado == "esq":
        return local_pts[local_pts[:, 0] < center_x_approx]
    return local_pts[local_pts[:, 0] > center_x_approx]


def obter_pontos_para_tangente(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
    lado: str,
) -> np.ndarray:
    if gota_pts is None or p_esq is None or p_dir is None or lado not in ("esq", "dir"):
        return np.empty((0, 2), dtype=float)
    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    offset_calibracao = float(np.clip(ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, ANGLE_BASELINE_OFFSET_MIN, ANGLE_BASELINE_OFFSET_MAX))
    baseline_ajustada = baseline_y + offset_calibracao
    return _selecionar_pontos_lado(gota_pts, p_esq, p_dir, baseline_ajustada, lado)


def calcular_vetor_tangente(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
    lado: str,
) -> Optional[Tuple[float, float]]:
    if gota_pts is None or len(gota_pts) < 5:
        return None
    if p_esq is None or p_dir is None:
        return None
    if lado not in ("esq", "dir"):
        return None
    slope_result = _calcular_slope_tangente_polynomial(
        gota_pts, baseline_y, lado,
        p_contato=(p_esq if lado == "esq" else p_dir),
        contour_pts=gota_pts,
        profile_open=True,
    )
    if slope_result is None:
        return None
    m_tangente, _, _ = slope_result
    return _normalizar_vetor_tangente(m_tangente)


def calcular_angulo_circular(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
    lado: str,
) -> Optional[float]:
    if gota_pts is None or len(gota_pts) < 5:
        return None
    if p_esq is None or p_dir is None:
        return None
    if lado not in ("esq", "dir"):
        return None

    offset_calibracao = 3.0
    baseline_ajustada = float(baseline_y) + offset_calibracao
    pts = np.asarray(gota_pts, dtype=float)
    mask = (pts[:, 1] < baseline_ajustada - 3.0) & (pts[:, 1] > baseline_ajustada - 150.0)
    local_pts = pts[mask]
    center_x = (float(p_esq[0]) + float(p_dir[0])) / 2.0
    if lado == "esq":
        local_pts = local_pts[local_pts[:, 0] < center_x]
    else:
        local_pts = local_pts[local_pts[:, 0] > center_x]

    if len(local_pts) < 3:
        return None

    mean_xy = np.mean(local_pts, axis=0)
    local_pts_centered = local_pts.astype(np.float64) - mean_xy
    try:
        xc0, yc0, R0 = ajustar_circulo_algebrico(local_pts_centered)
    except Exception:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

    dists = np.hypot(local_pts_centered[:, 0] - xc0, local_pts_centered[:, 1] - yc0)
    residuals = np.abs(dists - R0)
    sigma = np.std(residuals)
    if sigma > 0:
        local_pts_filtered = local_pts_centered[residuals <= 2.0 * sigma]
    else:
        local_pts_filtered = local_pts_centered

    if len(local_pts_filtered) < 3:
        return None

    try:
        xc, yc, R = ajustar_circulo_algebrico(local_pts_filtered)
    except Exception:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

    yc += mean_xy[1]
    xc += mean_xy[0]
    if R is None or R <= 0:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

    dy = baseline_ajustada - yc
    if abs(dy) >= R:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

    dx = math.sqrt(max(0.0, R ** 2 - dy ** 2))
    x_contato = xc - dx if lado == "esq" else xc + dx
    denominador = baseline_ajustada - yc
    if abs(denominador) < 1e-12:
        theta_deg = 90.0
    else:
        m_tangente = -(x_contato - xc) / denominador
        theta_deg = math.degrees(math.atan(abs(m_tangente)))

    if yc > baseline_ajustada:
        theta_deg = 180.0 - theta_deg

    return float(np.clip(theta_deg, 0.0, 180.0))


def calcular_qualidade_dinamica(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
) -> Dict[str, float]:
    if gota_pts is None or len(gota_pts) < 8 or p_esq is None or p_dir is None:
        return {"score": 0.0, "rmse_px": 999.0, "n_pts": 0.0}

    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    offset = float(np.clip(ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, ANGLE_BASELINE_OFFSET_MIN, ANGLE_BASELINE_OFFSET_MAX))
    baseline_ajustada = baseline_y + offset
    rmses = []
    total_pts = 0
    for lado in ("esq", "dir"):
        local_pts = _selecionar_pontos_lado(gota_pts, p_esq, p_dir, baseline_ajustada, lado)
        if len(local_pts) < 4:
            continue
        total_pts += int(len(local_pts))
        try:
            xc, yc, R = ajustar_circulo_algebrico(local_pts)
            if not np.isfinite(R) or R <= 0:
                continue
            d = np.hypot(local_pts[:, 0] - xc, local_pts[:, 1] - yc)
            rmse = float(np.sqrt(np.mean((d - R) ** 2)))
            if np.isfinite(rmse):
                rmses.append(rmse)
        except Exception:
            continue

    if not rmses:
        return {"score": 0.0, "rmse_px": 999.0, "n_pts": float(total_pts)}

    rmse_medio = float(np.mean(rmses))
    score = float(np.exp(-rmse_medio / max(1e-6, QUALITY_RMSE_REF_PX)))
    score = float(np.clip(score, QUALITY_MIN_SCORE, QUALITY_MAX_SCORE))
    return {"score": score, "rmse_px": rmse_medio, "n_pts": float(total_pts)}


# Backward-compatible alias

def calcular_angulo_polinomial(*args, **kwargs):
    warnings.warn("calcular_angulo_polinomial estï¿½ depreciado. Use calcular_angulo_circular.", DeprecationWarning, stacklevel=2)
    return calcular_angulo_circular(*args, **kwargs)




