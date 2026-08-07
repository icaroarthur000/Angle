import cv2
import numpy as np
import logging
from typing import Tuple, Optional, Dict, List
from parametros import obter

logger = logging.getLogger(__name__)

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


def _selecionar_canto_contato(
    candidatos: np.ndarray,
    lado: str,
    baseline_y: float,
    x_center_ref: float,
) -> List[float]:
    """Escolhe o ponto de contato que mais parece uma quina física da gota.

    A regra favorece o ponto mais baixo do lado, mas também exige que ele seja
    uma extremidade lateral do ramo inferior, e não apenas um ponto qualquer da
    faixa de base.
    """
    if candidatos is None or len(candidatos) == 0:
        return [float(x_center_ref), float(baseline_y)]

    pts = np.asarray(candidatos, dtype=np.float64).reshape(-1, 2)
    y_max = float(np.max(pts[:, 1]))
    y_min = float(np.min(pts[:, 1]))
    altura = max(1.0, y_max - y_min)

    # O ponto de contato deve sair do extremo real do ramo inferior.
    # Primeiro limitamos ao último trecho vertical da gota e depois pegamos
    # a borda lateral mais externa desse trecho.
    banda_inferior = max(2.0, 0.06 * altura)
    faixa = pts[pts[:, 1] >= (y_max - banda_inferior)]
    if len(faixa) < 2:
        faixa = pts

    if lado == "esq":
        idx = int(np.lexsort((faixa[:, 1], faixa[:, 0]))[0])
    else:
        idx = int(np.lexsort((faixa[:, 1], -faixa[:, 0]))[0])

    melhor = faixa[idx]
    return [float(melhor[0]), float(baseline_y)]

# =================================================================
# BLOCO 1: DETECÇÃO DA BASELINE - FLOOR-SEEKER (NOVO)
# =================================================================

def detect_baseline_tls(gota_pts: np.ndarray, bottom_fraction: float = 0.30, debug: bool = False) -> Tuple[float, Optional[Tuple]]:
    
    if gota_pts is None or len(gota_pts) < 5:
        return 0.0, None

    y_vals = gota_pts[:, 1].astype(np.float64)
    y_max = float(np.max(y_vals))
    q = float(np.clip(1.0 - max(0.02, min(0.5, bottom_fraction)), 0.0, 1.0))
    y_cut = float(np.quantile(y_vals, q))
    floor_pts = gota_pts[y_vals >= y_cut]

    baseline_y, line_params, n_inliers = _fit_line_robusta(floor_pts, debug=debug)
    if line_params is not None and np.isfinite(baseline_y):
        vx, vy, x0, _ = line_params
        return baseline_y, (float(vx), float(vy), float(x0), float(baseline_y))

    # Fallback conservador para não quebrar fluxo legado
    tolerance = 5.0
    near_floor = gota_pts[np.abs(gota_pts[:, 1] - y_max) <= tolerance]
    if len(near_floor) < 2:
        x0 = float(np.mean(gota_pts[:, 0]))
        if debug:
            print("[BASELINE ROBUSTA] fallback extremo acionado")
        return y_max, (1.0, 0.0, x0, y_max)

    x0 = float(np.mean(near_floor[:, 0]))
    if debug:
        print(f"[BASELINE ROBUSTA] fallback simples: y={y_max:.2f}, inliers={n_inliers}")
    return float(y_max), (1.0, 0.0, x0, y_max)


def fallback_geometric(gota_pts: np.ndarray, baseline_y: float, debug: bool = False) -> Tuple[Optional[List[float]], Optional[List[float]]]:
    """Fallback geométrico compatível para os dois pontos de contato."""
    if gota_pts is None or len(gota_pts) < 2:
        return None, None

    pts = np.asarray(gota_pts, dtype=np.float64).reshape(-1, 2)
    x_center = float(np.mean(pts[:, 0]))
    y_max = float(np.max(pts[:, 1]))
    altura = max(1.0, y_max - float(np.min(pts[:, 1])))
    banda = max(2.0, 0.12 * altura)
    candidatos = pts[pts[:, 1] >= (y_max - banda)]
    if len(candidatos) < 2:
        candidatos = pts

    p_esq = _selecionar_canto_contato(candidatos[candidatos[:, 0] <= x_center], "esq", baseline_y, x_center)
    p_dir = _selecionar_canto_contato(candidatos[candidatos[:, 0] >= x_center], "dir", baseline_y, x_center)

    if debug:
        print(f"[FALLBACK GEOM] esq={p_esq} dir={p_dir}")

    return p_esq, p_dir


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
    def _ancorar_no_extremo_lado(lado: str, baseline_ref: float, x_center_ref: float) -> List[float]:
        pts = np.asarray(gota_pts, dtype=np.float64).reshape(-1, 2)
        y_max_ref = float(np.max(pts[:, 1]))
        y_min_ref = float(np.min(pts[:, 1]))
        altura_ref = max(1.0, y_max_ref - y_min_ref)
        banda = max(2.0, 0.06 * altura_ref)
        mask = pts[:, 1] >= (y_max_ref - banda)
        indices = np.flatnonzero(mask)

        if len(indices) >= 2:
            cortes = np.where(np.diff(indices) > 1)[0]
            inicio = 0
            melhor_run = indices
            melhor_len = 0
            melhor_media_y = -1.0
            for corte in np.append(cortes, len(indices) - 1):
                fim = corte + 1
                run = indices[inicio:fim]
                inicio = fim
                if len(run) == 0:
                    continue
                media_y = float(np.mean(pts[run, 1]))
                if len(run) > melhor_len or (len(run) == melhor_len and media_y > melhor_media_y):
                    melhor_run = run
                    melhor_len = len(run)
                    melhor_media_y = media_y

            run_pts = pts[melhor_run]
            if len(run_pts) >= 2:
                extremos = np.array([run_pts[0], run_pts[-1]], dtype=np.float64)
                if lado == "esq":
                    melhor = extremos[np.argmin(extremos[:, 0])]
                else:
                    melhor = extremos[np.argmax(extremos[:, 0])]
                return [float(melhor[0]), float(baseline_ref)]

        faixa = pts[mask] if np.any(mask) else pts
        if len(faixa) < 2:
            faixa = pts

        if lado == "esq":
            melhor = faixa[np.argmin(faixa[:, 0])]
        else:
            melhor = faixa[np.argmax(faixa[:, 0])]
        return [float(melhor[0]), float(baseline_ref)]

    def _ponto_valido_no_contorno(ponto: Optional[List[float]], lado: str) -> bool:
        if ponto is None or gota_pts is None or len(gota_pts) < 3:
            return False

        contorno = np.asarray(gota_pts, dtype=np.float32).reshape(-1, 1, 2)
        px, py = float(ponto[0]), float(ponto[1])
        return cv2.pointPolygonTest(contorno, (px, py), True) >= 0.0

    def _fallback_lado(
        lado: str,
        baseline_ref: float,
        y_max_ref: float,
        height_ref: float,
        x_center_ref: float,
    ) -> List[float]:
        adaptive_tol = max(5.0, 0.15 * height_ref)
        near_baseline = gota_pts[gota_pts[:, 1] >= (y_max_ref - adaptive_tol)]

        if len(near_baseline) >= 2:
            if lado == "esq":
                candidatos = near_baseline[near_baseline[:, 0] <= x_center_ref]
            else:
                candidatos = near_baseline[near_baseline[:, 0] >= x_center_ref]
            if len(candidatos) < 2:
                candidatos = near_baseline
            return _selecionar_canto_contato(candidatos, lado, baseline_ref, x_center_ref)

        y_terco = y_max_ref - 0.33 * height_ref
        terco_inf = gota_pts[gota_pts[:, 1] >= y_terco]
        if len(terco_inf) >= 2:
            if lado == "esq":
                candidatos = terco_inf[terco_inf[:, 0] <= x_center_ref]
            else:
                candidatos = terco_inf[terco_inf[:, 0] >= x_center_ref]
            if len(candidatos) < 2:
                candidatos = terco_inf
            return _selecionar_canto_contato(candidatos, lado, baseline_ref, x_center_ref)

        if lado == "esq":
            return [float(np.min(gota_pts[:, 0])), baseline_ref]
        return [float(np.max(gota_pts[:, 0])), baseline_ref]

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

    # Guarda: evitar ROI vazia (pode ocorrer em gotas muito pequenas)
    if y_roi_bottom <= y_roi_top:
        logger.warning("ROI vazia após margem_base=%.1fpx. Usando margem mínima.", margem_base)
        y_roi_bottom = float(baseline_y) - 2.0
    
    roi_mask = (y_vals >= y_roi_top) & (y_vals <= y_roi_bottom)
    roi_pts = gota_pts[roi_mask]
    
    if len(roi_pts) < MIN_POINTS_FOR_FIT:
        return None, None
    
    x_center = float(np.mean(gota_pts[:, 0]))
    
    if debug:
        logger.debug("[EXTRAPOLAÇÃO] ROI: %d pontos entre Y=%.1f e Y=%.1f",
                     len(roi_pts), y_roi_top, y_roi_bottom)
    
    # Separa em esquerda e direita
    left_pts = roi_pts[roi_pts[:, 0] < x_center]
    right_pts = roi_pts[roi_pts[:, 0] >= x_center]
    
    def extrapolate_side(pts, side_name):
        if len(pts) < MIN_POINTS_FOR_FIT:
            return None, None
        
        try:
            # Polyfit: Y como função de X
            coeffs = np.polyfit(pts[:, 1], pts[:, 0], degree)
            poly = np.poly1d(coeffs)
            
            # Extrapola para baseline_y
            x_contact = poly(baseline_y)
            
            if not np.isfinite(x_contact):
                return None, None
            
            if debug:
                print(f"[{side_name}] Ponto de contato extrapolado: ({x_contact:.2f}, {baseline_y:.2f}) coeffs={coeffs}")
            return [float(x_contact), float(baseline_y)], coeffs
        
        except Exception as e:
            if debug:
                print(f"[{side_name}] Erro no polyfit: {e}")
            return None, None
    
    p_esq, coeffs_esq = extrapolate_side(left_pts, "ESQUERDA")
    p_dir, coeffs_dir = extrapolate_side(right_pts, "DIREITA")
    
    y_max = float(np.max(gota_pts[:, 1]))
    y_min = float(np.min(gota_pts[:, 1]))
    height = y_max - y_min

    if p_esq is None and p_dir is None:
        if debug:
            print("[EXTRAPOLAÇÃO] Ambos os lados falharam, usando fallback geométrico")
        return fallback_geometric(gota_pts, baseline_y, debug=debug)

    p_esq_final = _ancorar_no_extremo_lado("esq", baseline_y, x_center)
    p_dir_final = _ancorar_no_extremo_lado("dir", baseline_y, x_center)

    return p_esq_final, p_dir_final


# =================================================================
# BLOCO 3: PIPELINE MAESTRO (Orquestração)
# =================================================================

def detectar_baseline_hibrida(gota_pts: np.ndarray, debug: bool = False) -> Dict:
    
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
    
    # 1. Detectar baseline com FLOOR-SEEKER (Y máximo)
    baseline_y, line_params = detect_baseline_tls(gota_pts, debug=debug)
    
    if debug:
        y_max = float(np.max(gota_pts[:, 1]))
        print(f"\n[BASELINE] Y_max do contorno: {y_max:.2f}")
        print(f"[BASELINE] Baseline Y: {baseline_y:.2f}")
        print(f"[CONTORNO] Pontos totais: {len(gota_pts)}, Y_min={np.min(gota_pts[:, 1]):.1f}, Y_max={np.max(gota_pts[:, 1]):.1f}")
    
    # 2. Encontrar pontos de contato via extrapolação polinomial
    p_esq, p_dir = find_contact_points_by_extrapolation(gota_pts, baseline_y, debug=debug)
    
    if debug:
        print("\n✓ RESULTADO FINAL:")
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
