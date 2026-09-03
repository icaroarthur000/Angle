from typing import Union, Tuple, Dict, Optional
import numpy as np
import math
import logging
import warnings
from parametros import obter

logger = logging.getLogger(__name__)


ANGLE_BASELINE_OFFSET_FACTOR = float(obter("angle_baseline_offset_factor", 0.01))
ANGLE_BASELINE_OFFSET_MIN = float(obter("angle_baseline_offset_min", 1.5))
ANGLE_BASELINE_OFFSET_MAX = float(obter("angle_baseline_offset_max", 4.0))
ANGLE_WINDOW_HEIGHT_FACTOR = float(obter("angle_window_height_factor", 0.55))
ANGLE_WINDOW_HEIGHT_MIN = int(obter("angle_window_height_min", 70))
ANGLE_WINDOW_HEIGHT_MAX = int(obter("angle_window_height_max", 220))
ANGLE_OUTLIER_SIGMA_SCALE = float(obter("angle_outlier_sigma_scale", 2.0))
QUALITY_RMSE_REF_PX = float(obter("quality_rmse_ref_px", 3.0))
QUALITY_MIN_SCORE = float(obter("quality_min_score", 0.0))
QUALITY_MAX_SCORE = float(obter("quality_max_score", 1.0))


def ajustar_circulo_algebrico(pontos: np.ndarray) -> Tuple[float, float, float]:
    """
    Método Kåsa para ajuste de círculo (Alta Robustez).
    Calcula o raio através da média real das distâncias, impedindo R=0.
    """
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
    
    A = np.array([[Suu, Suv], 
                  [Suv, Svv]])
    B = np.array([Suuu + Suvv, Svvv + Suuv]) / 2.0
    
    try:
        uc, vc = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        return 0.0, 0.0, 0.0
    
    xc = xm + uc
    yc = ym + vc
    
    distancias = np.sqrt((x - xc)**2 + (y - yc)**2)
    R = np.mean(distancias)
    
    return float(xc), float(yc), float(R)


def _selecionar_pontos_tangente(
    local_pts: np.ndarray,
    baseline_y: float,
    p_contato: Optional[Union[list, tuple]] = None,
    contour_pts: Optional[np.ndarray] = None,
) -> np.ndarray:
    """Seleciona uma janela contínua e local do contorno ao redor do ponto de contato para o polyfit."""
    if local_pts is None or len(local_pts) < 3:
        return np.empty((0, 2), dtype=float)

    distance_from_baseline = baseline_y - local_pts[:, 1]
    pts = local_pts[(distance_from_baseline >= -5.0) & (distance_from_baseline <= 45.0)]

    if len(pts) == 0:
        return np.empty((0, 2), dtype=float)

    if p_contato is None or len(p_contato) < 2:
        return pts[: min(16, len(pts))]

    contato = np.asarray(p_contato[:2], dtype=float)
    parent_pts = np.asarray(contour_pts if contour_pts is not None else local_pts, dtype=float)
    if len(parent_pts) == 0:
        return pts[: min(16, len(pts))]

    lookup = {tuple(np.round(point, 6)) for point in pts}
    candidate_indices = [idx for idx in range(len(parent_pts)) if tuple(np.round(parent_pts[idx], 6)) in lookup]
    if not candidate_indices:
        return pts[: min(16, len(pts))]

    candidate_indices = sorted(candidate_indices)
    candidate_pts = parent_pts[candidate_indices]
    contact_distances = np.hypot(candidate_pts[:, 0] - contato[0], candidate_pts[:, 1] - contato[1])
    anchor_pos = int(np.argmin(contact_distances))
    if not np.isfinite(contact_distances[anchor_pos]) or contact_distances[anchor_pos] > 12.0:
        return pts[: min(16, len(pts))]

    candidate_count = len(candidate_indices)
    if candidate_count < 4:
        return pts[: min(16, len(pts))]

    window_sizes = [7, 9, 11, 13, 15, 17]
    window_sizes = [n for n in window_sizes if n <= candidate_count]
    if not window_sizes:
        return pts[: min(16, len(pts))]

    prev_metrics = None
    best_selected = None
    best_metrics = None

    for window_size in window_sizes:
        start = max(0, anchor_pos - window_size // 2)
        end = min(candidate_count, start + window_size)
        if end - start < 4:
            start = max(0, end - window_size)
        selected_indices = candidate_indices[start:end]
        if len(selected_indices) < 4:
            continue

        selected_pts = parent_pts[selected_indices]
        if len(selected_pts) < 4:
            continue

        if np.any(np.diff(selected_indices) != 1):
            continue

        max_dist = float(np.max(np.hypot(selected_pts[:, 0] - contato[0], selected_pts[:, 1] - contato[1])))
        if max_dist > 25.0:
            continue

        ys = selected_pts[:, 1]
        xs = selected_pts[:, 0]
        if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
            continue

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                coeffs = np.polyfit(ys, xs, 2)
            except (np.linalg.LinAlgError, ValueError):
                continue

        a, b, c = coeffs
        dx_dy = float(2.0 * a * contato[1] + b)
        if not np.isfinite(dx_dy):
            continue
        if abs(dx_dy) < 1e-9:
            m_tangente = float("inf")
        else:
            m_tangente = 1.0 / dx_dy

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

        if not np.isfinite(r2) or r2 < 0.70:
            continue
        if rmse > 3.0:
            continue
        if not np.isfinite(cond) or cond > 1e8:
            continue

        theta = float(math.degrees(math.atan2(m_tangente, 1.0))) if np.isfinite(m_tangente) else float("nan")

        if prev_metrics is not None:
            delta_theta = abs(theta - prev_metrics["theta"])
            delta_slope = abs(dx_dy - prev_metrics["dx_dy"])
            if delta_theta > 3.0 or delta_slope > 0.15:
                continue

        prev_metrics = {"theta": theta, "dx_dy": dx_dy}
        best_selected = selected_indices
        best_metrics = {
            "size": len(selected_indices),
            "rmse": rmse,
            "r2": r2,
            "cond": cond,
            "theta": theta,
            "dx_dy": dx_dy,
        }
        if len(selected_indices) <= 7:
            break

    if best_selected is not None and best_metrics is not None:
        return parent_pts[best_selected]

    fallback = pts[: min(16, len(pts))]
    if len(fallback) >= 4:
        return fallback
    return np.empty((0, 2), dtype=float)


def _calcular_slope_tangente_polynomial(
    local_pts: np.ndarray,
    baseline_y: float,
    lado: str,
    p_contato: Optional[Union[list, tuple]] = None,
    contour_pts: Optional[np.ndarray] = None,
) -> Optional[tuple[float, np.ndarray, np.ndarray]]:
    if local_pts is None or len(local_pts) < 3:
        return None
    pts = _selecionar_pontos_tangente(local_pts, baseline_y, p_contato, contour_pts)
    if len(pts) < 4:
        pts = local_pts
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
    return m_tangente, coeffs, pts
