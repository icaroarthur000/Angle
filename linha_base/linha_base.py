import cv2
import numpy as np
from typing import Tuple, Optional, Dict, List
from parametros import obter

# =================================================================
# CONFIGURAÇÕES CIENTÍFICAS (baseado em ADSA e DropSnake)
# =================================================================
EPS_NORMALIZE = 1e-8

# Parâmetros para extrapolação polinomial e detecção de baseline
ROI_BOTTOM_EXCLUDE = float(obter("roi_bottom_exclude", 0.02))
ROI_TOP_EXCLUDE = float(obter("roi_top_exclude", 0.20))
POLYFIT_DEGREE = int(obter("polyfit_degree", 2))
MIN_POINTS_FOR_FIT = int(obter("min_points_for_fit", 8))
BASELINE_BOTTOM_FRACTION = float(obter("baseline_bottom_fraction", 0.10))
BASELINE_INLIER_MIN_PIXELS = float(obter("baseline_inlier_min_pixels", 2.0))
BASELINE_INLIER_MAD_SCALE = float(obter("baseline_inlier_mad_scale", 2.5))
BASELINE_REFINE_ITERATIONS = int(obter("baseline_refine_iterations", 2))

def safe_normalize(dx: float, dy: float, eps: float = EPS_NORMALIZE) -> Tuple[float, float]:
    """Normaliza vetor (dx,dy) com segurança contra divisão por zero."""
    dist = np.hypot(dx, dy)
    if dist < eps:
        return 1.0, 0.0
    return dx / dist, dy / dist


def _fit_line_robusta(pontos: np.ndarray, debug: bool = False) -> Tuple[float, Optional[Tuple[float, float, float, float]], int]:
    """Ajusta linha robusta via cv2.fitLine + poda iterativa por MAD (estilo RANSAC)."""
    if pontos is None or len(pontos) < 2:
        return 0.0, None, 0

    pts = np.asarray(pontos, dtype=np.float32).reshape(-1, 1, 2)
    inliers = pts.copy()

    iters = max(1, BASELINE_REFINE_ITERATIONS)
    for _ in range(iters):
        if len(inliers) < 2:
            break

        vx, vy, x0, y0 = cv2.fitLine(inliers, cv2.DIST_L1, 0, 0.01, 0.01)
        vx = float(np.ravel(vx)[0])
        vy = float(np.ravel(vy)[0])
        x0 = float(np.ravel(x0)[0])
        y0 = float(np.ravel(y0)[0])

        # Distância perpendicular de cada ponto à linha ajustada
        pontos_xy = inliers.reshape(-1, 2)
        num = np.abs(vy * (pontos_xy[:, 0] - x0) - vx * (pontos_xy[:, 1] - y0))
        den = max(1e-9, np.hypot(vx, vy))
        dist = num / den

        med = float(np.median(dist))
        mad = float(np.median(np.abs(dist - med)))
        robust_sigma = max(1e-6, 1.4826 * mad)
        limiar = max(BASELINE_INLIER_MIN_PIXELS, BASELINE_INLIER_MAD_SCALE * robust_sigma)

        mask = dist <= limiar
        novos_inliers = inliers.reshape(-1, 2)[mask]
        if len(novos_inliers) < 2:
            break

        if len(novos_inliers) == len(inliers):
            break
        inliers = novos_inliers.reshape(-1, 1, 2).astype(np.float32)

    if len(inliers) < 2:
        return 0.0, None, 0

    vx, vy, x0, y0 = cv2.fitLine(inliers, cv2.DIST_L1, 0, 0.01, 0.01)
    vx = float(np.ravel(vx)[0])
    vy = float(np.ravel(vy)[0])
    x0 = float(np.ravel(x0)[0])
    y0 = float(np.ravel(y0)[0])

    # baseline_y robusta: quantil alto dos inliers (mais próximo do piso físico)
    baseline_y = float(np.quantile(inliers.reshape(-1, 2)[:, 1], 0.90))

    if debug:
        print(f"[BASELINE ROBUSTA] inliers={len(inliers)} vx={vx:.4f} vy={vy:.4f} y={baseline_y:.2f}")

    return baseline_y, (vx, vy, x0, y0), int(len(inliers))

# =================================================================
# BLOCO 1: DETECÇÃO DA BASELINE - FLOOR-SEEKER (NOVO)
# =================================================================

def detect_baseline_tls(
    gota_pts: np.ndarray,
    mascara=None,
    debug: bool = False,
) -> Tuple[float, Optional[Tuple]]:
    """Detecta a baseline pelo perfil inferior da máscara limpa ou do contorno.

    Quando `mascara` (binária, apenas gota) é fornecida:
      - Para cada coluna X com foreground → pixel mais baixo (max Y)
      - baseline_y = mediana do perfil: robusto a spikes isolados, sem limiares fixos
      - slope = np.polyfit de 1° grau: captura inclinação real do substrato
      - line_params usa esse slope → reta vermelha acompanha o substrato

    Fallback (sem máscara): percentil 99.5 dos Y do contorno.
    """
    if gota_pts is None or len(gota_pts) < 5:
        return 0.0, None

    y_vals = gota_pts[:, 1].astype(np.float64)
    x_vals = gota_pts[:, 0].astype(np.float64)

    # ------------------------------------------------------------------
    # Caminho principal: análise por coluna sobre a máscara limpa
    # ------------------------------------------------------------------
    if mascara is not None and mascara.ndim == 2 and np.any(mascara > 0):
        msk = mascara > 0
        col_xs, col_ys = [], []
        for xi in range(msk.shape[1]):
            rows = np.where(msk[:, xi])[0]
            if len(rows) > 0:
                col_xs.append(float(xi))
                col_ys.append(float(rows[-1]))  # pixel mais baixo desta coluna

        if len(col_xs) >= 3:
            bx = np.array(col_xs)
            by = np.array(col_ys)

            # percentile 99.5 do perfil inferior: robusto a poucos outliers,
            # mas captura o ponto mais baixo real (linha de contato) ao contrário
            # de np.median, que daria o centro da curva inferior da gota.
            baseline_y = float(np.percentile(by, 99.5))

            try:
                slope = float(np.polyfit(bx, by, 1)[0])
            except Exception:
                slope = 0.0

            vx, vy = safe_normalize(1.0, slope)
            x0 = float(np.mean(bx))

            if debug:
                print(f"[BASELINE COLUNA] baseline_y={baseline_y:.2f} | "
                      f"slope={slope:.5f} | colunas={len(bx)}")

            return baseline_y, (float(vx), float(vy), float(x0), float(baseline_y))

    # ------------------------------------------------------------------
    # Fallback: percentil 99.5 dos Y do contorno
    # ------------------------------------------------------------------
    baseline_y = float(np.percentile(y_vals, 99.5))

    near = gota_pts[y_vals >= (baseline_y - 2.0)]
    if len(near) < 1:
        near = gota_pts
    x0 = (float(np.min(near[:, 0])) + float(np.max(near[:, 0]))) / 2.0

    if debug:
        print(f"[BASELINE FALLBACK] baseline_y={baseline_y:.2f} | percentil 99.5")

    return baseline_y, (1.0, 0.0, float(x0), float(baseline_y))


# =================================================================
# BLOCO 2: EXTRAPOLAÇÃO POLINOMIAL (Método Científico)
# =================================================================

def find_contact_points_by_extrapolation(
    gota_pts: np.ndarray,
    baseline_y: float,
    roi_bottom: float = ROI_BOTTOM_EXCLUDE,
    roi_top: float = ROI_TOP_EXCLUDE,
    degree: int = POLYFIT_DEGREE,
    debug: bool = False
) -> Tuple[Optional[List[float]], Optional[List[float]]]:
    """
    MÉTODO CIENTÍFICO: Extrapolação Polinomial para precisão sub-pixel.
    """
    if gota_pts is None or len(gota_pts) < MIN_POINTS_FOR_FIT:
        return None, None
    
    y_vals = gota_pts[:, 1]
    y_min, y_max = float(np.min(y_vals)), float(np.max(y_vals))
    height = y_max - y_min
    
    if height < 1:
        return None, None
    
    # Define região de interesse (ROI): exclui extremos e foca na curvatura
    y_roi_bottom = y_max - roi_bottom * height
    y_roi_top = y_min + roi_top * height

    # Corte adicional próximo à baseline para evitar contaminação pela "saia" de contato.
    # Em imagens fáceis, poucos pixels perto do piso podem deslocar muito o ângulo final.
    margem_base = max(6.0, 0.06 * height)
    y_roi_bottom = min(y_roi_bottom, float(baseline_y) - margem_base)
    
    roi_mask = (y_vals >= y_roi_top) & (y_vals <= y_roi_bottom)
    roi_pts = gota_pts[roi_mask]
    
    if len(roi_pts) < MIN_POINTS_FOR_FIT:
        return None, None
    
    x_center = float(np.mean(gota_pts[:, 0]))
    
    if debug:
        print(f"[EXTRAPOLAÇÃO] ROI: {len(roi_pts)} pontos entre Y={y_roi_top:.1f} e Y={y_roi_bottom:.1f}")
    
    # Separa em esquerda e direita
    left_pts = roi_pts[roi_pts[:, 0] < x_center]
    right_pts = roi_pts[roi_pts[:, 0] >= x_center]
    
    def extrapolate_side(pts, side_name):
        if len(pts) < MIN_POINTS_FOR_FIT:
            return None
        
        try:
            # Polyfit: Y como função de X
            coeffs = np.polyfit(pts[:, 1], pts[:, 0], degree)
            poly = np.poly1d(coeffs)
            
            # Extrapola para baseline_y
            x_contact = poly(baseline_y)
            
            if not np.isfinite(x_contact):
                return None
            
            if debug:
                print(f"[{side_name}] Ponto de contato extrapolado: ({x_contact:.2f}, {baseline_y:.2f})")
            return [float(x_contact), float(baseline_y)]
        
        except Exception as e:
            if debug:
                print(f"[{side_name}] Erro no polyfit: {e}")
            return None
    
    p_esq = extrapolate_side(left_pts, "ESQUERDA")
    p_dir = extrapolate_side(right_pts, "DIREITA")
    
    # Se ambos falharam, usar fallback
    if p_esq is None and p_dir is None:
        if debug:
            print("[EXTRAPOLAÇÃO] Ambos os lados falharam, usando fallback geométrico")
        return fallback_geometric(gota_pts, baseline_y, debug=debug)
    
    # Se apenas um lado falhou, espelhar o outro
    if p_esq is None and p_dir is not None:
        dist = abs(p_dir[0] - x_center)
        p_esq = [x_center - dist, baseline_y]
        if debug:
            print(f"[ESQUERDA] Espelhado a partir da direita: ({p_esq[0]:.2f}, {p_esq[1]:.2f})")
    
    if p_dir is None and p_esq is not None:
        dist = abs(p_esq[0] - x_center)
        p_dir = [x_center + dist, baseline_y]
        if debug:
            print(f"[DIREITA] Espelhado a partir da esquerda: ({p_dir[0]:.2f}, {p_dir[1]:.2f})")
    
    return p_esq, p_dir


def fallback_geometric(gota_pts: np.ndarray, baseline_y: float, debug: bool = False) -> Tuple[Optional[List[float]], Optional[List[float]]]:

    if debug:
        print("[FALLBACK] Usando detecção geométrica simples")
    
    y_max = float(np.max(gota_pts[:, 1]))
    y_min = float(np.min(gota_pts[:, 1]))
    height = y_max - y_min

    # Tolerância adaptativa: busca pontos nos 15% inferiores do contorno
    adaptive_tol = max(5.0, 0.15 * height)
    near_baseline = gota_pts[gota_pts[:, 1] >= (y_max - adaptive_tol)]
    
    if len(near_baseline) >= 2:
        x_center = float(np.mean(gota_pts[:, 0]))
        # Ponto esquerdo: extremo esquerdo na faixa inferior
        left_pts = near_baseline[near_baseline[:, 0] <= x_center]
        right_pts = near_baseline[near_baseline[:, 0] > x_center]
        x_esq = float(np.min(left_pts[:, 0])) if len(left_pts) > 0 else float(np.min(near_baseline[:, 0]))
        x_dir = float(np.max(right_pts[:, 0])) if len(right_pts) > 0 else float(np.max(near_baseline[:, 0]))
        return [x_esq, baseline_y], [x_dir, baseline_y]
    
    # Fallback final: extremos horizontais do terço inferior
    y_terco = y_max - 0.33 * height
    terco_inf = gota_pts[gota_pts[:, 1] >= y_terco]
    if len(terco_inf) >= 2:
        x_center = float(np.mean(gota_pts[:, 0]))
        x_min = float(np.min(terco_inf[terco_inf[:, 0] <= x_center][:, 0])) if np.any(terco_inf[:, 0] <= x_center) else float(np.min(terco_inf[:, 0]))
        x_max = float(np.max(terco_inf[terco_inf[:, 0] > x_center][:, 0])) if np.any(terco_inf[:, 0] > x_center) else float(np.max(terco_inf[:, 0]))
        return [x_min, baseline_y], [x_max, baseline_y]

    x_min = float(np.min(gota_pts[:, 0]))
    x_max = float(np.max(gota_pts[:, 0]))
    return [x_min, baseline_y], [x_max, baseline_y]


# =================================================================
# BLOCO 3: PIPELINE MAESTRO (Orquestração)
# =================================================================

def detectar_baseline_hibrida(gota_pts: np.ndarray, mascara=None, debug: bool = False) -> Dict:

    def _norm_pt(p):
        if p is None:
            return None
        return [float(p[0]), float(p[1])]

    if gota_pts is None or len(gota_pts) < 10:
        return {
            'baseline_y': 0.0,
            'line_params': None,
            'p_esq': None,
            'p_dir': None,
            'method': 'failed',
            'contact_method': 'failed'
        }
    
    if debug:
        print("\n" + "="*60)
        print("DETECÇÃO - FLOOR-SEEKER + EXTRAPOLAÇÃO")
        print("="*60)
    
    # 1. Detectar baseline com análise por coluna (ou fallback percentil)
    baseline_y, line_params = detect_baseline_tls(gota_pts, mascara=mascara, debug=debug)
    
    if debug:
        y_max = float(np.max(gota_pts[:, 1]))
        print(f"\n[BASELINE] Y_max do contorno: {y_max:.2f}")
        print(f"[BASELINE] Baseline Y: {baseline_y:.2f}")
        print(f"[CONTORNO] Pontos totais: {len(gota_pts)}, Y_min={np.min(gota_pts[:, 1]):.1f}, Y_max={np.max(gota_pts[:, 1]):.1f}")
    
    # 2. Encontrar pontos de contato via extrapolação polinomial
    p_esq, p_dir = find_contact_points_by_extrapolation(gota_pts, baseline_y, debug=debug)
    
    # 3. Refinar line_params baseado nos pontos finais
    # ⚠️ MAS NÃO SOBRESCREVER baseline_y! Já temos o valor correto (Y_max)
    if p_esq is not None and p_dir is not None:
        dx = p_dir[0] - p_esq[0]
        dy = p_dir[1] - p_esq[1]
        vx, vy = safe_normalize(dx, dy)
        x0 = (p_esq[0] + p_dir[0]) / 2.0
        # Mantém baseline_y original (Y máximo do contorno)
        line_params = (float(vx), float(vy), float(x0), float(baseline_y))
    
    if debug:
        print(f"\n✓ RESULTADO FINAL:")
        print(f"  Baseline Y: {baseline_y:.2f} [Y MÁXIMO DO CONTORNO]")
        print(f"  Ponto Esquerdo: {_norm_pt(p_esq)}")
        print(f"  Ponto Direito: {_norm_pt(p_dir)}")
        if p_esq and p_dir:
            dist_pontos = abs(p_dir[0] - p_esq[0])
            print(f"  Distância X entre pontos: {dist_pontos:.2f} px")
            x_center = float(np.mean(gota_pts[:, 0]))
            print(f"  Centro X do contorno: {x_center:.2f}")
            esq_offset = abs(p_esq[0] - x_center)
            dir_offset = abs(p_dir[0] - x_center)
            print(f"  Offset esq/dir do centro: {esq_offset:.2f} / {dir_offset:.2f}")
        print("="*60 + "\n")
    
    return {
        'baseline_y': baseline_y,
        'line_params': line_params,
        'p_esq': _norm_pt(p_esq),
        'p_dir': _norm_pt(p_dir),
        'method': 'floor_seeker_hybrid',
        'contact_method': 'polynomial_extrapolation',
        'r_squared': 1.0
    }


# =================================================================
# FUNÇÕES AUXILIARES (Compatibilidade)
# =================================================================

def encontrar_pontos_contato_base(gota_pts: np.ndarray, band_px: int = 2) -> Tuple[float, List[float], List[float]]:
    """Compatibilidade: Retorna baseline_y e extremos na faixa inferior."""
    if gota_pts is None or len(gota_pts) == 0:
        return 0.0, [0.0, 0.0], [0.0, 0.0]
    
    y_max = float(np.max(gota_pts[:, 1]))
    band_pts = gota_pts[gota_pts[:, 1] >= (y_max - band_px)]
    
    if len(band_pts) >= 2:
        x_min = float(np.min(band_pts[:, 0]))
        x_max = float(np.max(band_pts[:, 0]))
        return y_max, [x_min, y_max], [x_max, y_max]
    
    x_min = float(np.min(gota_pts[:, 0]))
    x_max = float(np.max(gota_pts[:, 0]))
    return y_max, [x_min, y_max], [x_max, y_max]


def encontrar_pontos_contato(gota_pts: np.ndarray, baseline_y: float) -> Tuple[Optional[List[float]], Optional[List[float]]]:
    """Compatibilidade com chamadas legadas do main: fallback geométrico."""
    return fallback_geometric(gota_pts, baseline_y, debug=False)
