from typing import Union, Tuple
import numpy as np
import math


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


def calcular_angulo_circular(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
    lado: str
) -> float:
    """Calcula o ângulo de contato via Goniometria Diferencial (Ajuste Circular + Derivada)."""
    if gota_pts is None or len(gota_pts) < 5:
        return 0.0
    if p_esq is None or p_dir is None:
        return 0.0
    if lado not in ("esq", "dir"):
        return 0.0
    
    # --- PULO DO GATO: CALIBRAÇÃO DE BASELINE ---
    # Compensa a espessura da linha preta da imagem (+3 pixels para baixo)
    offset_calibracao = 3.0
    baseline_ajustada = baseline_y + offset_calibracao

    # Janela de análise com base na linha ajustada
    window_height = 150
    mask = (gota_pts[:, 1] < baseline_ajustada - 3) & \
           (gota_pts[:, 1] > baseline_ajustada - window_height)

    local_pts = gota_pts[mask]

    # Refinar para borda externa (lado)
    center_x_approx = (p_esq[0] + p_dir[0]) / 2
    if lado == "esq":
        local_pts = local_pts[local_pts[:, 0] < center_x_approx]
    else:
        local_pts = local_pts[local_pts[:, 0] > center_x_approx]

    if len(local_pts) < 3:
        return 0.0

    # Normalização de coordenadas (centering)
    mean_xy = np.mean(local_pts, axis=0)
    local_pts_centered = local_pts.astype(np.float64) - mean_xy

    # Ajuste inicial do círculo para remoção de outliers (Filtro Sigma)
    try:
        xc0, yc0, R0 = ajustar_circulo_algebrico(local_pts_centered)
    except Exception:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

    dists = np.hypot(local_pts_centered[:, 0] - xc0, local_pts_centered[:, 1] - yc0)
    residuals = np.abs(dists - R0)
    sigma = np.std(residuals)

    if sigma > 0:
        inliers = residuals <= (2.0 * sigma)
        local_pts_filtered = local_pts_centered[inliers]
    else:
        local_pts_filtered = local_pts_centered

    if len(local_pts_filtered) < 3:
        return 0.0

    # Ajuste Circular final usando pontos limpos
    try:
        xc, yc, R = ajustar_circulo_algebrico(local_pts_filtered)
    except Exception:
        return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

    # Reajusta para coordenada global
    yc += mean_xy[1]
    xc += mean_xy[0]

    try:
        # 1. Validação de Raio
        if R is None or R <= 0:
            print("Ajuste circular falhou: raio inválido.")
            return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)

        # 2. Ponto de Contato de Sub-pixel (Interseção Círculo-Reta)
        dy = baseline_ajustada - yc
        
        # Verificação se a baseline está fora do círculo
        if abs(dy) >= R:
            print("Baseline fora do círculo.")
            return _calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)
        
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