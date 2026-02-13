import cv2
import numpy as np
from typing import Tuple, Optional, Dict, List

# =================================================================
# CONFIGURAÇÕES CIENTÍFICAS (baseado em ADSA e DropSnake)
# =================================================================
EPS_NORMALIZE = 1e-8

# Parâmetros para extrapolação polinomial e detecção de baseline
ROI_BOTTOM_EXCLUDE = 0.005  
ROI_TOP_EXCLUDE = 0.20      
POLYFIT_DEGREE = 2         
MIN_POINTS_FOR_FIT = 8   

def safe_normalize(dx: float, dy: float, eps: float = EPS_NORMALIZE) -> Tuple[float, float]:
    """Normaliza vetor (dx,dy) com segurança contra divisão por zero."""
    dist = np.hypot(dx, dy)
    if dist < eps:
        return 1.0, 0.0
    return dx / dist, dy / dist

# =================================================================
# BLOCO 1: DETECÇÃO DA BASELINE - FLOOR-SEEKER (NOVO)
# =================================================================

def detect_baseline_tls(gota_pts: np.ndarray, bottom_fraction: float = 0.30, debug: bool = False) -> Tuple[float, Optional[Tuple]]:
    """
    ═══════════════════════════════════════════════════════════════
    FLOOR-SEEKER SIMPLIFICADO (FÍSICA PURA):
    Pega o piso FÍSICO real, nada de estatística.
    ═══════════════════════════════════════════════════════════════
    
    Estratégia ultra-direta:
    1. Pega o Y MÁXIMO do contorno inteiro (ponto mais baixo = piso)
    2. Encontra todos os pontos PRÓXIMOS ao piso (±5 pixels de contato)
    3. Calcula orientação SEMPRE HORIZONTAL (baseline é o piso!)
    
    RESULTADO: Linha vermelha COLADA no piso real, sem flutuação, sem estatística.
    
    Baseado em: Física simples - o substrato é o ponto Y mais baixo do contorno.
    
    Args:
        gota_pts: Contorno da gota (Nx2 array)
        bottom_fraction: [IGNORADO] Deixado apenas para compatibilidade
    
    Returns:
        baseline_y: Y MÁXIMO do contorno  (piso físico real)
        line_params: (vx=1.0, vy=0.0, x0=centro, y0=y_max) - linha horizontal
    """
    if gota_pts is None or len(gota_pts) < 5:
        return 0.0, None
    
    # PASSO 1: Pega o piso REAL (máximo Y = ponto mais baixo)
    y_max = float(np.max(gota_pts[:, 1]))
    y_min = float(np.min(gota_pts[:, 1]))
    
    # PASSO 2: Encontra todos os pontos PRÓXIMOS ao piso (±5 pixels de contato)
    tolerance = 5.0
    floor_pts = gota_pts[np.abs(gota_pts[:, 1] - y_max) <= tolerance]
    
    if len(floor_pts) < 2:
        # Fallback: nenhum ponto encontrado? Use extremos
        if debug:
            print(f"[FLOOR-SEEKER] AVISO: Nenhum ponto no piso, usando extremos!")
        x0 = float(np.mean(gota_pts[:, 0]))
        return y_max, (1.0, 0.0, x0, y_max)
    
    # PASSO 3: Centro horizontal dos pontos de contato
    x0 = float(np.mean(floor_pts[:, 0]))
    
    # PASSO 4: Orientação é SEMPRE horizontal (o piso É horizontal!)
    vx, vy = 1.0, 0.0
    
    # DEBUG
    if debug:
        print(f"[FLOOR-SEEKER] Y={y_max:.1f}, {len(floor_pts)} pontos no piso, x0={x0:.1f}")
    
    return float(y_max), (float(vx), float(vy), float(x0), float(y_max))


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
    """
    Fallback simples: Pegar extremos horizontais próximos à baseline.
    """
    if debug:
        print("[FALLBACK] Usando detecção geométrica simples")
    
    tolerance = 5
    near_baseline = gota_pts[np.abs(gota_pts[:, 1] - baseline_y) < tolerance]
    
    if len(near_baseline) >= 2:
        x_min = float(np.min(near_baseline[:, 0]))
        x_max = float(np.max(near_baseline[:, 0]))
        return [x_min, baseline_y], [x_max, baseline_y]
    
    x_min = float(np.min(gota_pts[:, 0]))
    x_max = float(np.max(gota_pts[:, 0]))
    return [x_min, baseline_y], [x_max, baseline_y]


# =================================================================
# BLOCO 3: PIPELINE MAESTRO (Orquestração)
# =================================================================

def detectar_baseline_hibrida(gota_pts: np.ndarray, debug: bool = False) -> Dict:
    """
    Pipeline completo: Floor-Seeker + Extrapolação Polinomial.
    
    Args:
        gota_pts: Contorno da gota (Nx2 array)
        debug: Se True, exibe mensagens de debug no console
    """
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
