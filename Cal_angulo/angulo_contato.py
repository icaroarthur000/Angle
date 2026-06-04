from typing import Union, Tuple, Dict
import numpy as np
import math
from parametros import obter

# =================================================================
# MÓDULO: Cal_angulo/angulo_contato.py
# Responsável por:
#   1. Ajuste de círculo pelo método de Kåsa (ajustar_circulo_algebrico)
#   2. Seleção de pontos laterais por janela de altura (_selecionar_pontos_lado)
#   3. Cálculo do ângulo por derivada implícita do círculo (calcular_angulo_circular)
#   4. Qualidade do ajuste via RMSE (calcular_qualidade_dinamica)
# =================================================================

# --- Parâmetros lidos do config.json ---
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


# =================================================================
# BLOCO 1 — AJUSTE DE CÍRCULO (Kåsa algébrico)
# =================================================================


def ajustar_circulo_algebrico(pontos: np.ndarray) -> Tuple[float, float, float]:
    """Ajuste de círculo pelo método de Kåsa. Retorna (xc, yc, R)."""
    if len(pontos) < 3:
        raise ValueError("Poucos pontos para ajuste circular.")
    
    x = pontos[:, 0]
    y = pontos[:, 1]
    
    # Centraliza para estabilidade numérica da matriz
    xm = np.mean(x)
    ym = np.mean(y)
    u = x - xm
    v = y - ym
    
    # Monta o sistema linear de Kåsa
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
    
    # Resolve o sistema 2x2
    try:
        uc, vc = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        # Se os pontos formarem uma linha reta perfeita e paralela
        return 0.0, 0.0, 0.0
        
    # Retorna ao sistema de coordenadas original
    xc = xm + uc
    yc = ym + vc
    
    # Raio = média das distâncias reais (mais estável que formula algébrica)
    distancias = np.sqrt((x - xc)**2 + (y - yc)**2)
    R = np.mean(distancias)
    
    return float(xc), float(yc), float(R)


# =================================================================
# BLOCO 2 — FALLBACK POLINOMIAL
# =================================================================


def _calcular_angulo_polynomial_fallback(local_pts: np.ndarray, baseline_y: float, lado: str) -> float:
    """Fallback: tangente pelo coeficiente do polyfit grau 2."""
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


# =================================================================
# BLOCO 3 — SELEÇÃO DE PONTOS LATERAIS
# =================================================================


def _is_obtuse_by_geometry(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
) -> bool:
    """Retorna True se a geometria do contorno indica ângulo obtuso (> 90°).

    Critério físico: se a largura máxima da gota (equador) for maior que
    a largura da base (distância entre pontos de contato), o ângulo de
    contato é obrigatoriamente > 90°, pois a barriga projeta para fora
    da linha de toque com o substrato.
    """
    if gota_pts is None or len(gota_pts) < 4 or p_esq is None or p_dir is None:
        return False
    base_width = abs(float(p_dir[0]) - float(p_esq[0]))
    if base_width < 1.0:
        return False
    # Largura por linha Y: para cada Y único calcula max_x - min_x
    y_vals = gota_pts[:, 1]
    unique_ys = np.unique(y_vals)
    widths = []
    for y in unique_ys:
        xs = gota_pts[y_vals == y, 0]
        if len(xs) >= 2:
            widths.append(float(np.max(xs) - np.min(xs)))
    if not widths:
        return False
    equator_width = float(np.max(widths))
    return equator_width > base_width * 1.05


def _selecionar_pontos_lado(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_ajustada: float,
    lado: str,
    is_obtuse: bool = False,
) -> np.ndarray:
    """Filtra pontos do contorno na janela de cálculo de ângulo para um lado."""
    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    window_height = int(np.clip(ANGLE_WINDOW_HEIGHT_FACTOR * altura_gota, ANGLE_WINDOW_HEIGHT_MIN, ANGLE_WINDOW_HEIGHT_MAX))
    # Para gotas obtusas a curvatura crítica fica perto da base;
    # a exclusão padrão de 10% jogaria fora exatamente esses pixels.
    if is_obtuse:
        excl_base = max(2.0, 0.02 * altura_gota)
    else:
        # Para gotas agudas a curvatura relevante fica muito próxima da base;
        # exclusão de 10% desperdiçava exatamente os dados mais informativos.
        excl_base = max(3.0, 0.03 * altura_gota)
    mask = (gota_pts[:, 1] < baseline_ajustada - excl_base) & (gota_pts[:, 1] > baseline_ajustada - window_height)
    local_pts = gota_pts[mask]
    center_x_approx = (p_esq[0] + p_dir[0]) / 2
    if lado == "esq":
        return local_pts[local_pts[:, 0] < center_x_approx]
    return local_pts[local_pts[:, 0] > center_x_approx]


# =================================================================
# BLOCO 4 — QUALIDADE E ÂNGULO CIRCULAR
# =================================================================


def calcular_qualidade_dinamica(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
) -> Dict[str, float]:
    """Score [0,1] baseado no RMSE do ajuste de círculo em ambos os lados."""
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
    # Mapeamento RMSE → score: exp decrescente, rápido para RMSE > ref_px
    score = float(np.exp(-rmse_medio / max(1e-6, QUALITY_RMSE_REF_PX)))
    score = float(np.clip(score, QUALITY_MIN_SCORE, QUALITY_MAX_SCORE))
    return {"score": score, "rmse_px": rmse_medio, "n_pts": float(total_pts)}


def calcular_angulo_circular(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
    lado: str
) -> float:
    """Cálculo do ângulo por ajuste círculo Kåsa + derivada implícita na baseline."""
    if gota_pts is None or len(gota_pts) < 5:
        return 0.0
    if p_esq is None or p_dir is None:
        return 0.0
    if lado not in ("esq", "dir"):
        return 0.0
    
    # Offset adaptativo: recua a baseline ~1-4px para evitar o queixo da gota
    altura_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1])) if len(gota_pts) > 0 else 100.0
    offset_calibracao = float(np.clip(ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, ANGLE_BASELINE_OFFSET_MIN, ANGLE_BASELINE_OFFSET_MAX))
    baseline_ajustada = baseline_y + offset_calibracao

    # Detecta geometria obtusa para ajustar a janela de seleção de pontos
    is_obtuse = _is_obtuse_by_geometry(gota_pts, p_esq, p_dir)

    # Janela de análise com base na linha ajustada
    local_pts = _selecionar_pontos_lado(gota_pts, p_esq, p_dir, baseline_ajustada, lado, is_obtuse=is_obtuse)

    if len(local_pts) < 3:
        return 0.0

    # Centra os pontos para estabilidade numérica do Kåsa
    mean_xy = np.mean(local_pts, axis=0)
    local_pts_centered = local_pts.astype(np.float64) - mean_xy

    # Ajuste inicial: detecta e remove outliers (filtro sigma)
    try:
        xc0, yc0, R0 = ajustar_circulo_algebrico(local_pts_centered)
    except Exception:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

    dists = np.hypot(local_pts_centered[:, 0] - xc0, local_pts_centered[:, 1] - yc0)
    residuals = np.abs(dists - R0)
    sigma = np.std(residuals)

    if sigma > 0:
        inliers = residuals <= (ANGLE_OUTLIER_SIGMA_SCALE * sigma)
        local_pts_filtered = local_pts_centered[inliers]
    else:
        local_pts_filtered = local_pts_centered

    if len(local_pts_filtered) < 3:
        return 0.0

    # Ajuste final com pontos limpos
    try:
        xc, yc, R = ajustar_circulo_algebrico(local_pts_filtered)
    except Exception:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

    # Reajusta para coordenada global
    yc += mean_xy[1]
    xc += mean_xy[0]

    try:
        # Validação do raio
        if R is None or R <= 0:
            print("Ajuste circular falhou: raio inválido.")
            return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

        # Intersecção círculo-baseline: dx = sqrt(R² - dy²)
        # A intersecção é calculada em baseline_y (= y_substrate, plano físico real)
        # para que o ângulo e a tangente coincidam exatamente com o ponto amarelo.
        # baseline_ajustada continua sendo usada SOMENTE como filtro de janela
        # de pontos em _selecionar_pontos_lado (afasta o "queixo" da gota).
        dy = baseline_y - yc

        # Verificação se a baseline está fora do círculo
        if abs(dy) >= R:
            print("Baseline fora do círculo.")
            return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

        dx = math.sqrt(max(0.0, R**2 - dy**2))
        x_contato = xc - dx if lado == "esq" else xc + dx

        # Derivada implícita do círculo no ponto de contato: m = -(x-xc)/(y-yc)
        numerador = x_contato - xc
        denominador = baseline_y - yc

        if denominador == 0:
            theta_deg = 90.0
        else:
            m_tangente = -numerador / denominador
            theta_rad = math.atan(abs(m_tangente))
            theta_deg = math.degrees(theta_rad)

        # Ajuste de quadrante: hidrofóbico (centro acima) vs hidrofílico (centro abaixo)
        if yc > baseline_y:
            theta_deg = 180.0 - theta_deg
            
        # --- DEBUG PROFISSIONAL ---
        print(f"\n--- GONIOMETRIA DIFERENCIAL ({lado}) ---")
        print(f"Baseline Original: {baseline_y:.2f} | Baseline Ajustada: {baseline_ajustada:.2f}")
        print(f"Raio (R): {R:.2f} | Centro: ({xc:.2f}, {yc:.2f})")
        print(f"Sub-pixel X contato: {x_contato:.2f}")
        print(f"ÂNGULO FINAL: {theta_deg:.2f}°\n")
        
        return float(np.clip(theta_deg, 0.0, 180.0))

    except Exception as e:
        print(f"Erro no cálculo diferencial: {e}")
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)


# Manter compatibilidade: alias para a nova função
calcular_angulo_polinomial = calcular_angulo_circular