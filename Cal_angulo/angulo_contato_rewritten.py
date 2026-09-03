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
ANGLE_CONTACT_CANDIDATE_MAX_DIST = float(obter("angle_contact_candidate_max_dist", 25.0))
ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL = float(obter("angle_contact_candidate_max_vertical", 12.0))
ANGLE_CONTACT_CANDIDATE_MIN_NEIGHBORS = int(obter("angle_contact_candidate_min_neighbors", 3))
ANGLE_WINDOW_HEIGHT_FACTOR = float(obter("angle_window_height_factor", 0.55))
ANGLE_WINDOW_HEIGHT_MIN = int(obter("angle_window_height_min", 70))
ANGLE_WINDOW_HEIGHT_MAX = int(obter("angle_window_height_max", 220))
ANGLE_OUTLIER_SIGMA_SCALE = float(obter("angle_outlier_sigma_scale", 2.0))
QUALITY_RMSE_REF_PX = float(obter("quality_rmse_ref_px", 3.0))
QUALITY_MIN_SCORE = float(obter("quality_min_score", 0.0))
QUALITY_MAX_SCORE = float(obter("quality_max_score", 1.0))


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
    distancias = np.sqrt((x - xc) ** 2 + (y - yc) ** 2)
    R = np.mean(distancias)
    return float(xc), float(yc), float(R)


def validar_candidato_contato(
    contour_pts: np.ndarray,
    candidate: Union[list, tuple, np.ndarray],
    contact_ref: Union[list, tuple, np.ndarray],
    baseline_y: float,
    lado: str = "esq",
) -> Optional[Dict[str, object]]:
    """Valida se um candidato de contato está alinhado com a região física de contato."""
    if contour_pts is None or len(contour_pts) < 4:
        return None
    if candidate is None or len(candidate) < 2:
        return None

    contour_arr = np.asarray(contour_pts, dtype=float)
    candidate_arr = np.asarray(candidate[:2], dtype=float)
    contact_arr = np.asarray(contact_ref[:2], dtype=float)
    if not np.isfinite(candidate_arr).all() or not np.isfinite(contact_arr).all():
        return None

    dist_to_ref = float(np.linalg.norm(candidate_arr - contact_arr))
    vertical_to_baseline = float(abs(candidate_arr[1] - baseline_y))

    if dist_to_ref > ANGLE_CONTACT_CANDIDATE_MAX_DIST:
        return {"is_valid": False, "reason": "deslocado_da_regiao_de_contato", "dist_to_ref": dist_to_ref, "vertical_to_baseline": vertical_to_baseline}

    if lado == "esq" and float(candidate_arr[0]) > float(contact_arr[0]) + 1e-6:
        return {"is_valid": False, "reason": "deslocado_da_regiao_de_contato", "dist_to_ref": dist_to_ref, "vertical_to_baseline": vertical_to_baseline}

    if lado == "dir" and float(candidate_arr[0]) < float(contact_arr[0]) - 1e-6:
        return {"is_valid": False, "reason": "deslocado_da_regiao_de_contato", "dist_to_ref": dist_to_ref, "vertical_to_baseline": vertical_to_baseline}

    if vertical_to_baseline > ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL:
        return {"is_valid": False, "reason": "deslocado_da_regiao_de_contato", "dist_to_ref": dist_to_ref, "vertical_to_baseline": vertical_to_baseline}

    return {"is_valid": True, "reason": "ok", "dist_to_ref": dist_to_ref, "vertical_to_baseline": vertical_to_baseline}


def _selecionar_ponto_contato_robusto(
    contour_pts: np.ndarray,
    p_contato: Optional[Union[list, tuple]] = None,
    baseline_y: float = 0.0,
    lado: str = "esq",
) -> np.ndarray:
    """Seleciona um ponto de contato mais plausível para a região de contato com base em validação geométrica."""
    if contour_pts is None or len(contour_pts) < 4:
        return np.empty((0, 2), dtype=float)
    if p_contato is None or len(p_contato) < 2:
        return np.empty((0, 2), dtype=float)

    contour_arr = np.asarray(contour_pts, dtype=float)
    contato_ref = np.asarray(p_contato[:2], dtype=float)
    if not np.isfinite(contato_ref).all():
        return np.empty((0, 2), dtype=float)

    pool = [contato_ref]
    nearby_mask = np.linalg.norm(contour_arr - contato_ref, axis=1) <= ANGLE_CONTACT_CANDIDATE_MAX_DIST
    nearby = contour_arr[nearby_mask]
    if len(nearby) > 0:
        pool.extend(nearby)

    if lado == "esq":
        near_baseline = contour_arr[np.abs(contour_arr[:, 1] - baseline_y) <= ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL]
        if len(near_baseline) > 0:
            pool.extend(near_baseline[near_baseline[:, 0] <= contato_ref[0]])
    else:
        near_baseline = contour_arr[np.abs(contour_arr[:, 1] - baseline_y) <= ANGLE_CONTACT_CANDIDATE_MAX_VERTICAL]
        if len(near_baseline) > 0:
            pool.extend(near_baseline[near_baseline[:, 0] >= contato_ref[0]])

    best_point = contato_ref
    best_score = None
    for candidate in pool:
        validation = validar_candidato_contato(contour_arr, candidate, contato_ref, baseline_y, lado)
        if validation is None or not validation.get("is_valid", False):
            continue
        score = float(validation.get("dist_to_ref", 0.0)) + 0.5 * float(validation.get("vertical_to_baseline", 0.0))
        if best_score is None or score < best_score:
            best_score = score
            best_point = np.asarray(candidate, dtype=float)

    return best_point.astype(float)


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
    if len(candidate_indices) <= 12 and np.all(np.diff(candidate_indices) == 1):
        return parent_pts[candidate_indices]

    candidate_pts = parent_pts[candidate_indices]
    contact_distances = np.hypot(candidate_pts[:, 0] - contato[0], candidate_pts[:, 1] - contato[1])
    anchor_pos = int(np.argmin(contact_distances))
    if not np.isfinite(contact_distances[anchor_pos]) or contact_distances[anchor_pos] > 12.0:
        return pts[: min(16, len(pts))]

    candidate_count = len(candidate_indices)
    if candidate_count < 4:
        return pts[: min(16, len(pts))]

    window_size = min(7, candidate_count)
    start = max(0, anchor_pos - window_size // 2 - 1)
    end = min(candidate_count, start + window_size)
    if end - start < 4:
        start = max(0, end - window_size)
    selected_indices = candidate_indices[start:end]

    if len(selected_indices) < 4:
        fallback_indices = candidate_indices[: min(16, len(candidate_indices))]
        if len(fallback_indices) >= 4:
            return parent_pts[fallback_indices]
        fallback = pts[: min(16, len(pts))]
        if len(fallback) >= 4:
            return fallback
        return np.empty((0, 2), dtype=float)

    selected_pts = parent_pts[selected_indices]
    if len(selected_pts) < 4:
        fallback_indices = candidate_indices[: min(16, len(candidate_indices))]
        if len(fallback_indices) >= 4:
            return parent_pts[fallback_indices]
        fallback = pts[: min(16, len(pts))]
        if len(fallback) >= 4:
            return fallback
        return np.empty((0, 2), dtype=float)

    if np.any(np.diff(selected_indices) != 1):
        return parent_pts[selected_indices]

    ys = selected_pts[:, 1]
    xs = selected_pts[:, 0]
    if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
        return parent_pts[selected_indices]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            coeffs = np.polyfit(ys, xs, 2)
        except (np.linalg.LinAlgError, ValueError):
            return parent_pts[selected_indices]

    a, b, c = coeffs
    dx_dy = float(2.0 * a * contato[1] + b)
    if not np.isfinite(dx_dy):
        return parent_pts[selected_indices]

    return parent_pts[selected_indices]


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


def _calcular_angulo_polynomial_fallback(local_pts: np.ndarray, baseline_y: float, lado: str) -> float:
    if local_pts is None or len(local_pts) < 3:
        return 0.0
    ys = local_pts[:, 1]
    xs = local_pts[:, 0]
    if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
        return 0.0
    coeffs = np.polyfit(ys, xs, 2)
    a, b, c = coeffs
    dx_dy = 2 * a * baseline_y + b
    theta_rad = math.atan(1 / dx_dy) if dx_dy != 0 else math.pi / 2
    theta_deg = math.degrees(theta_rad)
    if lado == "esq":
        if theta_deg < 0:
            theta_deg += 180
    else:
        if theta_deg > 0:
            theta_deg = 180 - theta_deg
        else:
            theta_deg = abs(theta_deg)
    return float(np.clip(theta_deg, 0.0, 180.0))


def _normalizar_vetor_tangente(m_tangente: float) -> tuple[float, float]:
    if not np.isfinite(m_tangente):
        return 0.0, 1.0
    vx = 1.0
    vy = float(m_tangente)
    norm = math.hypot(vx, vy)
    if norm < 1e-9:
        return 1.0, 0.0
    return vx / norm, vy / norm


def _calcular_angulo_interno_por_vetor_tangente(tangent_vec: np.ndarray, lado: str) -> float:
    """Converte um vetor tangente local em ângulo interno de contato usando a baseline como referência geométrica."""
    tangent_vec = np.asarray(tangent_vec, dtype=float).reshape(-1)
    if tangent_vec.size != 2:
        return 0.0

    tangent_vec = tangent_vec.astype(float)
    norm = float(np.linalg.norm(tangent_vec))
    if not np.isfinite(norm) or norm < 1e-12:
        return 0.0
    tangent_unit = tangent_vec / norm

    if lado == "esq":
        baseline_vec = np.array([1.0, 0.0], dtype=float)
    else:
        baseline_vec = np.array([-1.0, 0.0], dtype=float)

    baseline_unit = baseline_vec / float(np.linalg.norm(baseline_vec))
    dot = float(np.dot(tangent_unit, baseline_unit))
    cross = float(tangent_unit[0] * baseline_unit[1] - tangent_unit[1] * baseline_unit[0])
    theta = math.degrees(math.atan2(cross, dot))
    theta = (theta + 360.0) % 360.0

    if theta > 180.0:
        theta = 360.0 - theta
    if theta < 0.0:
        theta = abs(theta)

    return float(np.clip(theta, 0.0, 180.0))


def _angulo_interno_pelo_centro(theta_deg: float, yc: float, y_contato: float) -> float:
    """Converte o angulo agudo da tangente no angulo interno do liquido."""
    theta_deg = float(np.clip(theta_deg, 0.0, 180.0))
    if yc < y_contato - 1.0:
        theta_deg = 180.0 - theta_deg
    return float(np.clip(theta_deg, 0.0, 180.0))


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
) -> Optional[tuple[float, float]]:
    if gota_pts is None or len(gota_pts) < 5:
        return None
    if p_esq is None or p_dir is None:
        return None
    if lado not in ("esq", "dir"):
        return None

    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    offset_calibracao = float(np.clip(ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, ANGLE_BASELINE_OFFSET_MIN, ANGLE_BASELINE_OFFSET_MAX))
    baseline_ajustada = baseline_y + offset_calibracao

    local_pts = _selecionar_pontos_lado(gota_pts, p_esq, p_dir, baseline_ajustada, lado)
    if len(local_pts) < 3:
        return None

    contato = p_esq if lado == "esq" else p_dir
    slope_result = _calcular_slope_tangente_polynomial(local_pts, baseline_y, lado, contato, gota_pts)
    if slope_result is None:
        return None

    m_tangente, coeffs, pts = slope_result
    vx, vy = _normalizar_vetor_tangente(m_tangente)
    return vx, vy


def _selecionar_pontos_lado(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_ajustada: float,
    lado: str,
) -> np.ndarray:
    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    window_height = int(np.clip(ANGLE_WINDOW_HEIGHT_FACTOR * altura_gota, ANGLE_WINDOW_HEIGHT_MIN, ANGLE_WINDOW_HEIGHT_MAX))
    mask = (gota_pts[:, 1] <= baseline_ajustada) & (gota_pts[:, 1] > baseline_ajustada - window_height)
    local_pts = gota_pts[mask]
    center_x_approx = (p_esq[0] + p_dir[0]) / 2
    if lado == "esq":
        return local_pts[local_pts[:, 0] < center_x_approx]
    return local_pts[local_pts[:, 0] > center_x_approx]


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


def calcular_angulo_circular(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
    lado: str,
) -> Optional[float]:
    """Calcula o ângulo de contato usando uma estimativa geométrica simples e robusta."""
    if gota_pts is None or len(gota_pts) < 5:
        return None
    if p_esq is None or p_dir is None:
        return None
    if lado not in ("esq", "dir"):
        return None

    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    offset_calibracao = float(np.clip(ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, ANGLE_BASELINE_OFFSET_MIN, ANGLE_BASELINE_OFFSET_MAX))
    baseline_ajustada = baseline_y + offset_calibracao
    local_pts = _selecionar_pontos_lado(gota_pts, p_esq, p_dir, baseline_ajustada, lado)

    if len(local_pts) < 3:
        return None

    mean_xy = np.mean(local_pts, axis=0)
    local_pts_centered = local_pts.astype(np.float64) - mean_xy

    try:
        xc0, yc0, R0 = ajustar_circulo_algebrico(local_pts_centered)
    except (np.linalg.LinAlgError, ValueError):
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_ajustada, lado)

    dists = np.hypot(local_pts_centered[:, 0] - xc0, local_pts_centered[:, 1] - yc0)
    residuals = np.abs(dists - R0)
    sigma = np.std(residuals)
    if sigma > 0:
        inliers = residuals <= (ANGLE_OUTLIER_SIGMA_SCALE * sigma)
        local_pts_filtered = local_pts_centered[inliers]
    else:
        local_pts_filtered = local_pts_centered

    if len(local_pts_filtered) < 3:
        return None

    try:
        xc, yc, R = ajustar_circulo_algebrico(local_pts_filtered)
    except (np.linalg.LinAlgError, ValueError):
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_ajustada, lado)

    yc += mean_xy[1]
    xc += mean_xy[0]

    if R is None or R <= 0:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_ajustada, lado)

    dy = baseline_y - yc
    if abs(dy) >= R:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_ajustada, lado)

    contato = p_esq if lado == "esq" else p_dir
    contato_robusto = _selecionar_ponto_contato_robusto(gota_pts, contato, baseline_y, lado)
    if len(contato_robusto) >= 2:
        contato = contato_robusto

    x_contato = float(contato[0])
    y_contato = float(contato[1])

    tangent_vec = np.array([1.0, 0.0], dtype=float)
    if not np.isclose(float(y_contato - yc), 0.0):
        slope = float((x_contato - xc) / (y_contato - yc))
        tangent_vec = np.array([1.0, slope], dtype=float)
    tangent_vec = tangent_vec / float(np.linalg.norm(tangent_vec))

    theta_deg = _calcular_angulo_interno_por_vetor_tangente(tangent_vec, lado)

    logger.debug(
        "[GONIOMETRIA %s] R=%.2f xc=%.2f yc=%.2f baseline_adj=%.2f angulo=%.2f°",
        lado, R, xc, yc, baseline_ajustada, theta_deg,
    )

    return float(np.clip(theta_deg, 0.0, 180.0))


def calcular_angulo_polinomial(*args, **kwargs):
    warnings.warn(
        "calcular_angulo_polinomial está depreciado. Use calcular_angulo_circular.",
        DeprecationWarning,
        stacklevel=2,
    )
    return calcular_angulo_circular(*args, **kwargs)
