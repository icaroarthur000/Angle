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
    
    # 1. Centraliza os dados para garantir estabilidade da matriz
    xm = np.mean(x)
    ym = np.mean(y)
    u = x - xm
    v = y - ym
    
    # 2. Monta o sistema linear algébrico de Kåsa
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
    
    # 3. Resolve a matriz
    try:
        uc, vc = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        # Se os pontos formarem uma linha reta perfeita e paralela
        return 0.0, 0.0, 0.0
        
    # 4. Retorna o centro para as coordenadas reais
    xc = xm + uc
    yc = ym + vc
    
    # 5. O Pulo do Gato: Calcula o raio pela média das distâncias físicas
    distancias = np.sqrt((x - xc)**2 + (y - yc)**2)
    R = np.mean(distancias)
    
    return float(xc), float(yc), float(R)

def _calcular_angulo_polynomial_fallback(local_pts: np.ndarray, baseline_y: float, lado: str) -> float:
    """Fallback polinomial (baseado no código anterior)."""
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


def _selecionar_pontos_lado(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_ajustada: float,
    lado: str,
) -> np.ndarray:
    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    window_height = int(np.clip(ANGLE_WINDOW_HEIGHT_FACTOR * altura_gota, ANGLE_WINDOW_HEIGHT_MIN, ANGLE_WINDOW_HEIGHT_MAX))
    mask = (gota_pts[:, 1] < baseline_ajustada - 3) & (gota_pts[:, 1] > baseline_ajustada - window_height)
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
    """Calcula qualidade [0,1] baseada no RMSE do ajuste circular para ambos os lados."""
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
    # Mapeamento exponencial: rmse baixo -> score alto
    score = float(np.exp(-rmse_medio / max(1e-6, QUALITY_RMSE_REF_PX)))
    score = float(np.clip(score, QUALITY_MIN_SCORE, QUALITY_MAX_SCORE))
    return {"score": score, "rmse_px": rmse_medio, "n_pts": float(total_pts)}


def calcular_angulo_circular(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
    lado: str
) -> Optional[float]:
    """Calcula o ângulo de contato via Goniometria Diferencial (Ajuste Circular + Derivada)."""
    if gota_pts is None or len(gota_pts) < 5:
        return None
    if p_esq is None or p_dir is None:
        return None
    if lado not in ("esq", "dir"):
        return None
    
    # --- CALIBRAÇÃO ADAPTATIVA DE BASELINE ---
    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    offset_calibracao = float(np.clip(ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, ANGLE_BASELINE_OFFSET_MIN, ANGLE_BASELINE_OFFSET_MAX))
    baseline_ajustada = baseline_y + offset_calibracao

    # Janela de análise com base na linha ajustada
    local_pts = _selecionar_pontos_lado(gota_pts, p_esq, p_dir, baseline_ajustada, lado)

    if len(local_pts) < 3:
        return None

    # Normalização de coordenadas (centering)
    mean_xy = np.mean(local_pts, axis=0)
    local_pts_centered = local_pts.astype(np.float64) - mean_xy

    # Ajuste inicial do círculo para remoção de outliers (Filtro Sigma)
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

    # Ajuste Circular final usando pontos limpos
    try:
        xc, yc, R = ajustar_circulo_algebrico(local_pts_filtered)
    except (np.linalg.LinAlgError, ValueError):
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_ajustada, lado)

    # Reajusta para coordenada global
    yc += mean_xy[1]
    xc += mean_xy[0]

    try:
        # 1. Validação de Raio
        if R is None or R <= 0:
            logger.warning("Ajuste circular falhou: raio inválido.")
            return _calcular_angulo_polynomial_fallback(local_pts, baseline_ajustada, lado)

        # 2. Ponto de Contato de Sub-pixel (Interseção Círculo-Reta)
        dy = baseline_ajustada - yc
        
        # Verificação se a baseline está fora do círculo
        if abs(dy) >= R:
            logger.warning("Baseline fora do círculo.")
            return _calcular_angulo_polynomial_fallback(local_pts, baseline_ajustada, lado)
        
        dx = math.sqrt(max(0.0, R**2 - dy**2))
        x_contato = xc - dx if lado == "esq" else xc + dx

        # 3. Derivada Implícita (Inclinação da Tangente)
        numerador = x_contato - xc
        denominador = baseline_ajustada - yc
        
        if denominador == 0:
            theta_deg = 90.0
        else:
            m_tangente = -numerador / denominador
            theta_rad = math.atan(abs(m_tangente))
            theta_deg = math.degrees(theta_rad)

        # 4. Ajuste de Quadrante (Hidrofóbico vs Hidrofílico)
        if yc > baseline_ajustada:
            theta_deg = 180.0 - theta_deg
            
        # --- DEBUG ---
        logger.debug(
            "[GONIOMETRIA %s] R=%.2f xc=%.2f yc=%.2f baseline_adj=%.2f angulo=%.2f°",
            lado, R, xc, yc, baseline_ajustada, theta_deg
        )
        
        return float(np.clip(theta_deg, 0.0, 180.0))

    except Exception as e:
        logger.error("Erro no cálculo diferencial: %s", e)
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_ajustada, lado)


# Manter compatibilidade: alias depreciado
def calcular_angulo_polinomial(*args, **kwargs):
    warnings.warn(
        "calcular_angulo_polinomial está depreciado. Use calcular_angulo_circular.",
        DeprecationWarning,
        stacklevel=2,
    )
    return calcular_angulo_circular(*args, **kwargs)