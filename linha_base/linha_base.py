"""
linha_base.py

Este módulo é o "cérebro" geométrico do software. 
Ele separa o que é a gota (curva) do que é o substrato (reta).
"""

import cv2
import numpy as np
from typing import Tuple, Optional, Dict, List

# =================================================================
# BLOCO 1: NÚCLEO MATEMÁTICO (Geometria Diferencial)
# Foque aqui para entender como o software "enxerga" curvas.
# =================================================================

def _compute_curvature_at_point(pts: np.ndarray, idx: int, window: int = 3) -> float:
    """
    Calcula se um ponto faz parte de uma curva ou de uma reta.
    Raciocínio: Se a direção dos pixels muda muito, a curvatura é alta (gota).
    Se os pixels seguem uma linha, a curvatura é baixa (substrato).
    """
    if idx < window or idx >= len(pts) - window:
        return float('inf')
    
    p_prev = pts[idx - window].astype(np.float64)
    p_curr = pts[idx].astype(np.float64)
    p_next = pts[idx + window].astype(np.float64)
    
    # Derivadas discretas para achar a variação de direção
    dprev = p_curr - p_prev
    dnext = p_next - p_curr
    d2p = dnext - dprev
    
    # Normalização para que o tamanho da gota não mude o resultado
    curvature = np.linalg.norm(d2p) / (np.linalg.norm(dprev) + 1e-6)
    return float(curvature)

def fit_baseline_tls_explicit(candidates: np.ndarray) -> Tuple[Optional[Tuple], float]:
    """
    Desenha a melhor linha possível através dos pontos do substrato.
    Usa TLS (Total Least Squares): minimiza a distância perpendicular,
    sendo muito mais preciso para baselines inclinadas do que uma regressão comum.
    """
    if candidates is None or len(candidates) < 5:
        return None, 0.0
    
    try:
        center = np.mean(candidates, axis=0)
        centered = candidates - center
        # SVD: Decomposição matemática para achar a orientação da linha
        U, S, Vt = np.linalg.svd(centered.T @ centered)
        
        direction = Vt[0, :]
        vx, vy = direction / np.linalg.norm(direction)
        x0, y0 = center
        
        # R_squared indica o quão "reta" é a superfície detectada
        r_squared = float(S[0] / np.sum(S)) if np.sum(S) > 1e-6 else 0.0
        return (vx, vy, x0, y0), r_squared
    except Exception:
        return None, 0.0

# =================================================================
# BLOCO 2: FILTROS DE SELEÇÃO (A "Peneira")
# Aqui você ajusta a sensibilidade para diferentes superfícies.
# =================================================================

def select_baseline_candidates(gota_pts: np.ndarray,
                                curvature_threshold: float = 0.12,
                                slope_threshold: float = 0.12) -> np.ndarray:
    """
    VARREDURA: Procura pontos que pareçam ser o "chão" sólido.
    TRABALHE AQUI: Se o software não achar o substrato em vidros reflexivos,
    tente ajustar o 'curvature_threshold'.
    """
    x_rect, y_rect, w_rect, h_rect = cv2.boundingRect(gota_pts)
    
    # Restringe a busca aos 25% inferiores da imagem (onde o substrato deve estar)
    search_start = y_rect + int(h_rect * 0.75)
    search_end = y_rect + int(h_rect * 0.98)
    
    pts_in_region = gota_pts[(gota_pts[:, 1] >= search_start) & (gota_pts[:, 1] <= search_end)]
    
    if len(pts_in_region) < 5: return np.array([], dtype=np.float32)
    
    # Suaviza para ignorar ruídos de pixelagem da câmera
    pts_smooth = cv2.blur(pts_in_region.astype(np.float32), (5, 1))
    
    candidates_mask = []
    for i in range(len(pts_smooth)):
        curv = _compute_curvature_at_point(pts_smooth, i, window=2)
        # Filtro: Curvatura baixa (plano) e inclinação baixa (horizontal/leve inclinação)
        candidates_mask.append(curv < curvature_threshold)
    
    candidates = pts_in_region[np.array(candidates_mask)]
    return candidates.astype(np.float32)

# =================================================================
# BLOCO 3: IDENTIFICAÇÃO DE CONTATO (O "Joelho" da Gota)
# ESTE É O PONTO MAIS IMPORTANTE DA SUA METODOLOGIA.
# =================================================================

def find_contact_points_by_transition(gota_pts: np.ndarray,
                                      line_params: Tuple,
                                      curvature_threshold: float = 0.20) -> Tuple[List, List]:
    """
    LOCALIZAÇÃO FÍSICA: Procura onde a gota "dobra" para tocar o chão.
    DIFERENCIAL: Não usa a linha base para "puxar" o ponto, mas sim a 
    geometria do contorno para achar a transição real.
    """
    vx, vy, x0, y0 = line_params
    center_x = np.mean(gota_pts[:, 0])
    
    # Pega a parte inferior da gota (60% para baixo)
    y_lim = np.min(gota_pts[:, 1]) + 0.6 * (np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1]))
    pts = gota_pts[gota_pts[:, 1] >= y_lim]
    
    def detect_side(side_pts, is_left=True):
        if len(side_pts) < 10: return None
        # Ordena para percorrer da gota (curva) para o substrato (reta)
        side_pts = side_pts[np.argsort(side_pts[:, 0])]
        if not is_left: side_pts = side_pts[::-1]
        
        for i in range(2, len(side_pts) - 2):
            # Procura o ponto de TRANSIÇÃO (onde a curvatura aumenta bruscamente)
            if _compute_curvature_at_point(side_pts, i, window=2) > curvature_threshold:
                return [float(side_pts[i][0]), float(side_pts[i][1])]
        return [float(side_pts[0][0]), float(side_pts[0][1])]

    p_esq = detect_side(pts[pts[:, 0] < center_x], True)
    p_dir = detect_side(pts[pts[:, 0] > center_x], False)
    
    return p_esq, p_dir

# =================================================================
# BLOCO 4: O MAESTRO (Função Híbrida)
# Aqui o software decide qual estratégia usar.
# =================================================================

def detectar_baseline_hibrida(gota_pts: np.ndarray) -> Dict:
    """
    Orquestra o pipeline:
    1. Acha a inclinação do chão (TLS).
    2. Acha os pontos de contato reais (Transição).
    3. Redefine a altura da linha base para os contatos reais (Precisão Científica).
    """
    if len(gota_pts) < 10: return {'method': 'error', 'p_esq': None, 'p_dir': None}

    # Tenta o método principal (Científico)
    candidates = select_baseline_candidates(gota_pts)
    line_params, r_squared = fit_baseline_tls_explicit(candidates)
    
    if line_params is not None and r_squared >= 0.6:
        p_esq, p_dir = find_contact_points_by_transition(gota_pts, line_params)
        
        if p_esq and p_dir:
            # TRABALHE AQUI: A linha base é movida para a média dos contatos.
            # Isso garante que o ângulo seja medido na interface real líquido-sólido.
            baseline_y = (p_esq[1] + p_dir[1]) / 2.0
            return {
                'line_params': line_params,
                'baseline_y': baseline_y,
                'method': 'tls_transition',
                'contact_method': 'geometric_transition',
                'p_esq': p_esq, 'p_dir': p_dir
            }

    # Se tudo falhar, usa o Fallback (Segurança)
    y_fallback = detectar_baseline_cintura(gota_pts)
    p_esq, p_dir = encontrar_pontos_contato(gota_pts, y_fallback)
    return {
        'line_params': None, 'baseline_y': y_fallback,
        'method': 'fallback_cintura', 'contact_method': 'cintura_fallback',
        'p_esq': p_esq, 'p_dir': p_dir
    }

def detectar_baseline_cintura(gota_pts: np.ndarray) -> float:
    """Procura a menor largura na base. Útil quando o substrato está invisível."""
    x, y, w, h = cv2.boundingRect(gota_pts)
    min_width = float('inf')
    y_res = float(y + h)
    for row in range(int(y + h * 0.6), int(y + h * 0.98), max(1, h//100)):
        row_pts = gota_pts[np.abs(gota_pts[:, 1] - row) < 2]
        if len(row_pts) >= 2:
            width = np.max(row_pts[:, 0]) - np.min(row_pts[:, 0])
            if width < min_width:
                min_width = width
                y_res = float(row)
    return y_res

def encontrar_pontos_contato(gota_pts: np.ndarray, baseline_y: float) -> Tuple:
    """Apenas localiza os extremos horizontais em uma altura Y fixa."""
    base_pts = gota_pts[np.abs(gota_pts[:, 1] - baseline_y) < 5]
    if len(base_pts) > 0:
        return [float(np.min(base_pts[:, 0])), baseline_y], [float(np.max(base_pts[:, 0])), baseline_y]
    x, y, w, h = cv2.boundingRect(gota_pts)
    return [float(x), baseline_y], [float(x + w), baseline_y]