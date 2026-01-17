from typing import Union
import numpy as np
import math

def calcular_angulo_polinomial(
    gota_pts: np.ndarray,
    p_esq: Union[list, tuple],
    p_dir: Union[list, tuple],
    baseline_y: float,
    lado: str
) -> float:
    """
    Calcula o ângulo de contato usando ajuste polinomial de 2ª ordem.
    
    Args:
        gota_pts: Array Nx2 com pontos do contorno (x, y)
        p_esq: Ponto de contato esquerdo [x, y]
        p_dir: Ponto de contato direito [x, y]
        baseline_y: Altura da linha base em pixels
        lado: "esq" para esquerdo, "dir" para direito
    
    Returns:
        Ângulo de contato em graus (0.0-180.0) ou 0.0 se inválido
    """
    # Validar entradas
    if gota_pts is None or len(gota_pts) < 5:
        return 0.0
    if p_esq is None or p_dir is None:
        return 0.0
    if lado not in ("esq", "dir"):
        return 0.0
    # Janela de análise (pontos acima da baseline)
    window_height = 50
    mask = (gota_pts[:, 1] < baseline_y) & \
           (gota_pts[:, 1] > baseline_y - window_height)

    local_pts = gota_pts[mask]
    
    if len(local_pts) < 5:
        return 0.0

    center_x = (p_esq[0] + p_dir[0]) / 2
    
    # Filtrar lado
    if lado == "esq":
        local_pts = local_pts[local_pts[:, 0] < center_x]
    else:
        local_pts = local_pts[local_pts[:, 0] > center_x]

    if len(local_pts) < 3:
        return 0.0

    try:
        # Ajuste Polinomial: x = ay^2 + by + c (invertido para melhor ajuste vertical)
        ys = local_pts[:, 1]
        xs = local_pts[:, 0]
        
        # Verificar se há variação suficiente nos dados
        if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
            return 0.0
        
        coeffs = np.polyfit(ys, xs, 2)
        a, b, c = coeffs

        # Derivada dx/dy na altura da baseline
        dx_dy = 2 * a * baseline_y + b
        
        # Ângulo
        theta_rad = math.atan(1 / dx_dy) if dx_dy != 0 else math.pi / 2
        theta_deg = math.degrees(theta_rad)

        if lado == "esq":
            if theta_deg < 0: theta_deg += 180
            return theta_deg
        else:
            if theta_deg > 0:
                theta_deg = 180 - theta_deg
            else:
                theta_deg = abs(theta_deg)
            return theta_deg

    except Exception as e:
        print(f"Erro no cálculo: {e}")
        return 0.0