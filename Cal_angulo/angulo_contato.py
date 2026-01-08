import numpy as np
import math

def calcular_angulo_polinomial(gota_pts, p_esq, p_dir, baseline_y, lado):
    """
    Calcula o ângulo de contato usando ajuste polinomial de 2ª ordem.
    lado: "esq" ou "dir"
    """
    # Janela de análise (pontos acima da baseline)
    window_height = 50
    mask = (gota_pts[:, 1] < baseline_y) & \
           (gota_pts[:, 1] > baseline_y - window_height)

    local_pts = gota_pts[mask]
    
    if len(local_pts) < 5: return 0.0

    center_x = (p_esq[0] + p_dir[0]) / 2
    
    # Filtrar lado
    if lado == "esq":
        local_pts = local_pts[local_pts[:, 0] < center_x]
    else:
        local_pts = local_pts[local_pts[:, 0] > center_x]

    if len(local_pts) < 5: return 0.0

    try:
        # Ajuste Polinomial: x = ay^2 + by + c (invertido para melhor ajuste vertical)
        ys = local_pts[:, 1]
        xs = local_pts[:, 0]
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