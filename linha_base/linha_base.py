"""linha_base.py

Pipeline híbrido para detecção de linha base (baseline) em gotas.

Metodologia:
1. Selecionar pontos candidatos com curvatura baixa (superfície sólida)
2. Aplicar regressão robusta (cv2.fitLine) para estimar orientação da baseline
3. Projetar contorno sobre a baseline para encontrar pontos de contato
4. Fallback automático (método geométrico de cintura) se regressão falhar

A linha base pode estar inclinada e não é assumida como horizontal.
Compatível com multiplos usuários, câmeras inclinadas e substratos variados.
"""

import cv2
import numpy as np
from typing import Tuple, Optional, Dict, List


def _compute_curvature_at_point(pts: np.ndarray, idx: int, window: int = 3) -> float:
    """Estima curvatura local usando segunda derivada discreta.
    
    Usa janela de pontos vizinhos para calcular d²y/dx² (aproximação robusta).
    Retorna magnitude da curvatura normalizada.
    """
    if idx < window or idx >= len(pts) - window:
        return float('inf')  # invalida pontos perto das bordas
    
    p_prev = pts[idx - window].astype(np.float64)
    p_curr = pts[idx].astype(np.float64)
    p_next = pts[idx + window].astype(np.float64)
    
    # primeira derivada (dy/dx aproximado)
    dprev = p_curr - p_prev
    dnext = p_next - p_curr
    
    # segunda derivada
    d2p = dnext - dprev
    
    # magnitude normalizada
    curvature = np.linalg.norm(d2p) / (np.linalg.norm(dprev) + 1e-6)
    return float(curvature)


def select_baseline_candidates(gota_pts: np.ndarray,
                                curvature_threshold: float = 0.15,
                                y_variance_threshold: float = 8.0) -> np.ndarray:
    """Seleciona pontos candidatos à superfície sólida (baseline).
    
    Critérios:
    - Curvatura local próxima de zero (superfície plana)
    - Variação Y pequena (não sobe/desce bruscamente)
    - Na região inferior da gota (50%-95% da altura)
    
    Retorna array Nx2 com pontos candidatos ou array vazio se nenhum encontrado.
    """
    if len(gota_pts) < 10:
        return np.array([], dtype=np.float32)
    
    x_rect, y_rect, w_rect, h_rect = cv2.boundingRect(gota_pts)
    
    # região inferior: 50%-95% da altura
    search_start = y_rect + int(h_rect * 0.5)
    search_end = y_rect + int(h_rect * 0.95)
    
    # filtro Y: apenas pontos na região
    y_mask = (gota_pts[:, 1] >= search_start) & (gota_pts[:, 1] <= search_end)
    pts_in_region = gota_pts[y_mask]
    
    if len(pts_in_region) < 5:
        return np.array([], dtype=np.float32)
    
    # suavizar contorno para cálculo de curvatura mais robusto
    if len(pts_in_region) > 5:
        kernel_size = 5
        pts_smooth = cv2.blur(pts_in_region.astype(np.float32), (kernel_size, 1))
    else:
        pts_smooth = pts_in_region.astype(np.float32)
    
    # calcular curvatura em cada ponto suavizado
    curvatures = []
    for i in range(len(pts_smooth)):
        curv = _compute_curvature_at_point(pts_smooth, i, window=2)
        curvatures.append(curv)
    
    curvatures = np.array(curvatures)
    
    # filtro: curvatura baixa (plano) e Y-variação pequena dentro de janela local
    candidates_mask = curvatures < curvature_threshold
    
    # verificar variação Y em janela local (elimina ruído vertical)
    window_size = max(3, len(pts_in_region) // 10)  # 10% do comprimento
    for i in range(len(candidates_mask)):
        if candidates_mask[i]:
            start_idx = max(0, i - window_size // 2)
            end_idx = min(len(pts_smooth), i + window_size // 2 + 1)
            y_var = np.max(pts_smooth[start_idx:end_idx, 1]) - np.min(pts_smooth[start_idx:end_idx, 1])
            if y_var > y_variance_threshold:
                candidates_mask[i] = False
    
    candidates = pts_in_region[candidates_mask]
    
    # se nenhum candidato passou nos filtros rígidos, relaxar critérios
    if len(candidates) < 5:
        # fallback: pegar os 20% mais planos (menor curvatura)
        sorted_indices = np.argsort(curvatures)
        n_to_select = max(5, len(curvatures) // 5)
        candidates = pts_in_region[sorted_indices[:n_to_select]]
    
    return candidates.astype(np.float32)


def fit_baseline_with_line(candidates: np.ndarray) -> Tuple[Optional[Tuple], float]:
    """Regressão robusta da linha base usando cv2.fitLine (RANSAC).
    
    Retorna:
    - (vx, vy, x0, y0): parâmetros da linha (direção + ponto)
    - r_squared: qualidade do ajuste (0-1, maior é melhor)
    
    Se houver poucos candidatos ou fit falhar, retorna (None, 0.0).
    """
    if candidates is None or len(candidates) < 5:
        return None, 0.0
    
    # cv2.fitLine usa RANSAC e retorna (vx, vy, x, y) — direção normalizada
    try:
        line_params = cv2.fitLine(candidates, cv2.DIST_L2, 0, 0.01, 0.01)
        vx, vy, x0, y0 = float(line_params[0]), float(line_params[1]), \
                          float(line_params[2]), float(line_params[3])
        
        # validar normalização
        norm = np.sqrt(vx**2 + vy**2)
        if norm < 0.9:  # não normalizado corretamente
            return None, 0.0
        
        # calcular R² como validação de qualidade
        # resíduos: distância de cada ponto à linha
        residuals = []
        for pt in candidates:
            dx = pt[0] - x0
            dy = pt[1] - y0
            # perpendicular distance (produto cruzado com direção normalizada)
            dist = abs(-vy * dx + vx * dy)
            residuals.append(dist)
        
        residuals = np.array(residuals)
        
        # R² baseado em variação Y (mais apropriado para linhas não-verticais)
        ss_res = np.sum(residuals ** 2)
        
        # para referência: usar spread de Y ou X (o que for maior)
        y_spread = np.max(candidates[:, 1]) - np.min(candidates[:, 1])
        x_spread = np.max(candidates[:, 0]) - np.min(candidates[:, 0])
        
        # usar a dimensão com maior variação
        if y_spread > x_spread:
            y_mean = np.mean(candidates[:, 1])
            ss_tot = np.sum((candidates[:, 1] - y_mean) ** 2)
        else:
            x_mean = np.mean(candidates[:, 0])
            ss_tot = np.sum((candidates[:, 0] - x_mean) ** 2)
        
        r_squared = 1.0 - (ss_res / (ss_tot + 1e-6)) if ss_tot > 1e-6 else 0.0
        r_squared = max(0.0, min(1.0, r_squared))  # clamp [0,1]
        
        return (vx, vy, x0, y0), float(r_squared)
    except Exception:
        return None, 0.0


def project_contour_onto_baseline(gota_pts: np.ndarray,
                                   line_params: Tuple) -> Tuple[List, List]:
    """Projeta contorno sobre a linha base e encontra pontos de contato.
    
    A projeção ortogonal sobre a linha garante que os pontos de contato
    sejam o "toque" real do líquido na superfície sólida.
    
    Retorna:
    - p_esq: [x, y] ponto de contato esquerdo
    - p_dir: [x, y] ponto de contato direito
    """
    vx, vy, x0, y0 = line_params
    
    # normalizar direção
    norm = np.sqrt(vx**2 + vy**2)
    if norm < 1e-6:
        return None, None
    vx, vy = vx / norm, vy / norm
    
    # para cada ponto do contorno, calcular sua projeção sobre a linha
    # usando parâmetro t: ponto_projetado = (x0, y0) + t * (vx, vy)
    projections = []
    for pt in gota_pts:
        dx = pt[0] - x0
        dy = pt[1] - y0
        t = dx * vx + dy * vy  # parâmetro de projeção
        proj_x = x0 + t * vx
        proj_y = y0 + t * vy
        projections.append((proj_x, proj_y, t))
    
    if not projections:
        return None, None
    
    projections = np.array(projections)
    # pontos extremos: menor e maior t
    t_values = projections[:, 2]
    idx_esq = np.argmin(t_values)
    idx_dir = np.argmax(t_values)
    
    p_esq = [float(projections[idx_esq, 0]), float(projections[idx_esq, 1])]
    p_dir = [float(projections[idx_dir, 0]), float(projections[idx_dir, 1])]
    
    return p_esq, p_dir


def detectar_baseline_cintura(gota_pts: np.ndarray) -> float:
    """Fallback geométrico: detecta altura da baseline pela 'cintura' (menor largura).
    
    Método heurístico robusta para casos onde a regressão falha.
    """
    x, y, w, h = cv2.boundingRect(gota_pts)
    
    baseline_y = float(y + h) - 2.0
    search_start = int(y + h * 0.5)
    search_end = int(y + h * 0.95)
    
    min_width = float('inf')
    neck_candidate = -1
    
    if search_end > search_start:
        for row in range(search_start, search_end):
            pts_in_row = gota_pts[np.abs(gota_pts[:, 1] - row) < 2]
            if len(pts_in_row) >= 2:
                w_row = np.max(pts_in_row[:, 0]) - np.min(pts_in_row[:, 0])
                if w_row < min_width:
                    min_width = w_row
                    neck_candidate = row
    
    if neck_candidate != -1 and neck_candidate > search_start:
        baseline_y = float(neck_candidate)
    
    return baseline_y


def detectar_baseline_hibrida(gota_pts: np.ndarray,
                               min_candidates: int = 5,
                               min_r_squared: float = 0.7) -> Dict:
    """Pipeline híbrido: regressão com fallback automático.
    
    Retorna dict:
    {
        'line_params': (vx, vy, x0, y0) ou None,
        'baseline_y': float,
        'r_squared': float (qualidade do fit),
        'method': str ('regression' ou 'fallback'),
        'p_esq': [x, y],
        'p_dir': [x, y]
    }
    """
    if len(gota_pts) < 5:
        return {'line_params': None, 'baseline_y': 0.0, 'r_squared': 0.0,
                'method': 'error', 'p_esq': None, 'p_dir': None}
    
    # ETAPA 2: Selecionar candidatos
    candidates = select_baseline_candidates(gota_pts)
    
    # ETAPA 3: Tentar regressão
    line_params, r_squared = fit_baseline_with_line(candidates)
    
    if line_params is not None and r_squared >= min_r_squared and len(candidates) >= min_candidates:
        # ETAPA 4: Regressão bem-sucedida — projetar e encontrar contatos
        p_esq, p_dir = project_contour_onto_baseline(gota_pts, line_params)
        baseline_y = line_params[3]  # y0 da linha
        return {
            'line_params': line_params,
            'baseline_y': baseline_y,
            'r_squared': r_squared,
            'method': 'regression',
            'p_esq': p_esq,
            'p_dir': p_dir
        }
    else:
        # ETAPA 5: Fallback — usar cintura
        baseline_y = detectar_baseline_cintura(gota_pts)
        p_esq, p_dir = encontrar_pontos_contato(gota_pts, baseline_y)
        return {
            'line_params': None,
            'baseline_y': baseline_y,
            'r_squared': 0.0,
            'method': 'fallback',
            'p_esq': p_esq,
            'p_dir': p_dir
        }


def encontrar_pontos_contato(gota_pts: np.ndarray, baseline_y: float) -> Tuple:
    """Encontra pontos de contato na altura da baseline (para compatibilidade).
    
    Este é um wrapper do método anterior, mantido para compatibilidade com main.py.
    """
    threshold_y = 5
    base_pts = gota_pts[np.abs(gota_pts[:, 1] - baseline_y) < threshold_y]
    
    if len(base_pts) > 0:
        p_esq = [float(np.min(base_pts[:, 0])), baseline_y]
        p_dir = [float(np.max(base_pts[:, 0])), baseline_y]
        return p_esq, p_dir
    else:
        # Fallback
        x, y, w, h = cv2.boundingRect(gota_pts)
        p_esq = [float(x), baseline_y]
        p_dir = [float(x + w), baseline_y]
        return p_esq, p_dir