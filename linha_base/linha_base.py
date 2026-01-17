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


def _validate_baseline_sanity(line_params: Tuple,
                               gota_pts: np.ndarray,
                               max_acceptable_angle: float = 45.0) -> bool:
    """Valida se a baseline estimada é fisicamente razoável.
    
    Critérios de sanidade:
    1. Inclinação não deve exceder ~45° (gotas não descaem de substratos de pé)
    2. Linha deve passar perto do centróide inferior da gota
    3. Direção (vx, vy) deve estar normalizada
    
    Retorna True se baseline é aceitável, False caso contrário.
    """
    if line_params is None:
        return False
    
    vx, vy, x0, y0 = line_params
    
    # Verificar normalização
    norm = np.sqrt(vx**2 + vy**2)
    if norm < 0.95 or norm > 1.05:
        return False
    
    # Verificar inclinação
    angle_rad = np.arctan2(abs(vy), abs(vx))
    angle_deg = np.degrees(angle_rad)
    if angle_deg > max_acceptable_angle:
        return False
    
    # A linha base deve estar perto do fundo da gota
    x_min = np.min(gota_pts[:, 0])
    x_max = np.max(gota_pts[:, 0])
    y_min = np.min(gota_pts[:, 1])
    y_max = np.max(gota_pts[:, 1])
    
    # y0 deve estar entre 70%-95% da altura (região inferior)
    expected_y_min = y_min + 0.7 * (y_max - y_min)
    expected_y_max = y_max + 0.1 * (y_max - y_min)  # um pouco abaixo do máximo
    
    if y0 < expected_y_min or y0 > expected_y_max:
        return False
    
    # x0 deve estar dentro ou perto dos limites horizontais
    if x0 < x_min - 10 or x0 > x_max + 10:
        return False
    
    return True


def select_baseline_candidates(gota_pts: np.ndarray,
                                curvature_threshold: float = 0.15,
                                y_variance_threshold: float = 8.0,
                                slope_threshold: float = 0.15,
                                lateral_margin_percent: float = 0.12) -> np.ndarray:
    """Seleciona pontos candidatos à superfície sólida (baseline).
    
    Critérios PRINCIPAIS (filtram superfície sólida):
    1. Curvatura local ≈ 0 (superfície plana)
    2. Variação Y pequena (não sobe/desce bruscamente)
    3. Inclinação local (slope) ≈ 0 [NOVO] (tangente quase horizontal)
    4. Zona de exclusão lateral [NOVO] (não está perto dos pés da gota)
    5. Na região inferior da gota (50%-95% da altura)
    
    Esses filtros juntos eliminam pontos do pé da gota, que possuem:
    - Curvatura baixa (após suavização)
    - Mas inclinação crescente (slope alto)
    - E localização nas extremidades
    
    Parâmetros:
    - slope_threshold: inclinação máxima aceita (~0.15 = ~8.5°)
    - lateral_margin_percent: fração horizontal para excluir (0.12 = 12% de cada lado)
    
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
    
    # FILTRO LATERAL: Excluir pontos perto das extremidades X
    # O pé da gota está nas extremidades; superfície sólida é central
    margin = lateral_margin_percent * w_rect
    x_min_valid = x_rect + margin
    x_max_valid = x_rect + w_rect - margin
    
    x_margin_mask = (pts_in_region[:, 0] >= x_min_valid) & (pts_in_region[:, 0] <= x_max_valid)
    pts_center = pts_in_region[x_margin_mask]
    
    if len(pts_center) < 5:
        # Relaxar margem se muito restritivo
        margin = lateral_margin_percent * 0.5 * w_rect
        x_min_valid = x_rect + margin
        x_max_valid = x_rect + w_rect - margin
        x_margin_mask = (pts_in_region[:, 0] >= x_min_valid) & (pts_in_region[:, 0] <= x_max_valid)
        pts_center = pts_in_region[x_margin_mask]
    
    if len(pts_center) < 5:
        pts_center = pts_in_region  # fallback: usar todos se margem muito restritiva
    
    # suavizar contorno para cálculo de curvatura mais robusto
    if len(pts_center) > 5:
        kernel_size = 5
        pts_smooth = cv2.blur(pts_center.astype(np.float32), (kernel_size, 1))
    else:
        pts_smooth = pts_center.astype(np.float32)
    
    # calcular curvatura em cada ponto suavizado
    curvatures = []
    for i in range(len(pts_smooth)):
        curv = _compute_curvature_at_point(pts_smooth, i, window=2)
        curvatures.append(curv)
    
    curvatures = np.array(curvatures)
    
    # FILTRO SLOPE: Inclinação local (dy/dx) deve ser ~0 para superfície
    # Pé da gota tem slope crescente; superfície tem slope ≈ 0
    slopes = []
    window = min(3, len(pts_smooth) // 5)  # janela para estimar inclinação
    
    for i in range(len(pts_smooth)):
        start_idx = max(0, i - window)
        end_idx = min(len(pts_smooth), i + window + 1)
        
        if start_idx < end_idx - 1:
            dy = pts_smooth[end_idx - 1, 1] - pts_smooth[start_idx, 1]
            dx = pts_smooth[end_idx - 1, 0] - pts_smooth[start_idx, 0]
            
            # slope = |dy| / |dx|, com proteção contra divisão por zero
            slope = abs(dy) / (abs(dx) + 1e-6)
        else:
            slope = float('inf')
        
        slopes.append(slope)
    
    slopes = np.array(slopes)
    
    # filtro: curvatura baixa AND inclinação baixa AND Y-variação pequena
    candidates_mask = (curvatures < curvature_threshold) & (slopes < slope_threshold)
    
    # verificar variação Y em janela local (elimina ruído vertical)
    window_size = max(3, len(pts_center) // 10)  # 10% do comprimento
    for i in range(len(candidates_mask)):
        if candidates_mask[i]:
            start_idx = max(0, i - window_size // 2)
            end_idx = min(len(pts_smooth), i + window_size // 2 + 1)
            y_var = np.max(pts_smooth[start_idx:end_idx, 1]) - np.min(pts_smooth[start_idx:end_idx, 1])
            if y_var > y_variance_threshold:
                candidates_mask[i] = False
    
    candidates = pts_center[candidates_mask]
    
    # se nenhum candidato passou nos filtros rígidos, relaxar critérios (fallback)
    if len(candidates) < 5:
        # fallback 1: relaxar slope, manter curvatura
        relaxed_mask = (curvatures < curvature_threshold * 2.0) & (slopes < slope_threshold * 1.5)
        candidates = pts_center[relaxed_mask]
        
        if len(candidates) < 5:
            # fallback 2: pegar os 20% mais planos (menor curvatura)
            sorted_indices = np.argsort(curvatures)
            n_to_select = max(5, len(curvatures) // 5)
            candidates = pts_center[sorted_indices[:n_to_select]]
    
    return candidates.astype(np.float32)


def fit_baseline_with_line(candidates: np.ndarray,
                            gota_pts: np.ndarray = None,
                            method: str = 'tls') -> Tuple[Optional[Tuple], float]:
    """Regressão robusta da linha base com suporte a TLS e cv2.fitLine.
    
    Parâmetros:
    - candidates: pontos candidatos à superfície
    - gota_pts: contorno completo da gota (para validação de sanidade)
    - method: 'tls' (recomendado) ou 'ransac' (cv2.fitLine)
    
    Retorna:
    - (vx, vy, x0, y0): parâmetros da linha (direção + ponto)
    - r_squared: qualidade do ajuste (0-1, maior é melhor)
    
    Se houver poucos candidatos, fit falhar ou baseline ser não-física,
    retorna (None, 0.0).
    
    NOVO: TLS (Total Least Squares) é o método padrão por ser mais preciso
    para minimizar distância perpendicular.
    """
    if candidates is None or len(candidates) < 5:
        return None, 0.0
    
    # Tentar TLS primeiro (mais preciso)
    if method == 'tls':
        line_params, r_squared = fit_baseline_tls_explicit(candidates)
    else:
        # Fallback para cv2.fitLine RANSAC
        try:
            line_params_raw = cv2.fitLine(candidates, cv2.DIST_L2, 0, 0.01, 0.01)
            vx, vy, x0, y0 = float(line_params_raw[0]), float(line_params_raw[1]), \
                              float(line_params_raw[2]), float(line_params_raw[3])
            
            norm = np.sqrt(vx**2 + vy**2)
            if norm < 0.9:
                return None, 0.0
            
            # Calcular R² para cv2.fitLine
            residuals = []
            for pt in candidates:
                dx = pt[0] - x0
                dy = pt[1] - y0
                dist = abs(-vy * dx + vx * dy)
                residuals.append(dist)
            
            residuals = np.array(residuals)
            ss_res = np.sum(residuals ** 2)
            
            y_spread = np.max(candidates[:, 1]) - np.min(candidates[:, 1])
            x_spread = np.max(candidates[:, 0]) - np.min(candidates[:, 0])
            
            if y_spread > x_spread:
                y_mean = np.mean(candidates[:, 1])
                ss_tot = np.sum((candidates[:, 1] - y_mean) ** 2)
            else:
                x_mean = np.mean(candidates[:, 0])
                ss_tot = np.sum((candidates[:, 0] - x_mean) ** 2)
            
            r_squared = 1.0 - (ss_res / (ss_tot + 1e-6)) if ss_tot > 1e-6 else 0.0
            r_squared = max(0.0, min(1.0, r_squared))
            
            line_params = (vx, vy, x0, y0)
        except Exception:
            return None, 0.0
    
    # Validar sanidade física se contorno está disponível
    if line_params is not None and gota_pts is not None:
        if not _validate_baseline_sanity(line_params, gota_pts):
            return None, 0.0
    
    return line_params, r_squared if line_params is not None else (None, 0.0)


def fit_baseline_tls_explicit(candidates: np.ndarray) -> Tuple[Optional[Tuple], float]:
    """Regressão Linear Ortogonal (TLS - Total Least Squares) com SVD.
    
    Minimiza a distância PERPENDICULAR de TODOS os pontos à reta.
    Mais preciso que L2 para detecção de baseline.
    
    Parâmetros:
    - candidates: array Nx2 com pontos candidatos
    
    Retorna:
    - (vx, vy, x0, y0): linha em forma paramétrica
    - r_squared: qualidade do fit baseado em variância explicada
    """
    if candidates is None or len(candidates) < 5:
        return None, 0.0
    
    try:
        # Centralizar pontos (crucial para TLS)
        center = np.mean(candidates, axis=0)
        centered = candidates - center
        
        # SVD da matriz de covariância
        # H = centered^T @ centered
        # O autovetor com maior autovalor = direção da reta
        U, S, Vt = np.linalg.svd(centered.T @ centered)
        
        # Primeiro vetor = maior autovalor = direção da reta
        direction = Vt[0, :]
        
        # Normalizar
        norm = np.linalg.norm(direction)
        if norm < 1e-6:
            return None, 0.0
        
        vx, vy = direction / norm
        x0, y0 = center
        
        # R² = variância_explicada / variância_total
        var_total = np.sum(S)
        var_explained = S[0] if len(S) > 0 else 0
        
        r_squared = float(var_explained / var_total) if var_total > 1e-6 else 0.0
        r_squared = np.clip(r_squared, 0.0, 1.0)
        
        return (vx, vy, x0, y0), r_squared
        
    except Exception as e:
        print(f"[TLS] Erro: {e}")
        return None, 0.0


def find_contact_points_by_perpendicular_distance(gota_pts: np.ndarray,
                                                    line_params: Tuple,
                                                    distance_threshold: float = 2.0) -> Tuple[List, List]:
    """Encontra pontos de contato usando distância perpendicular MÍNIMA.
    
    Metodologia (do seu pseudocódigo refatorado):
    1. Calcular distância perpendicular de TODOS os pontos à linha
    2. Filtrar pontos próximos à linha (distância < threshold)
    3. Filtrar por região Y (parte inferior da gota)
    4. Separar por X do centróide
    5. Escolher O PONTO com MENOR distância perpendicular por lado
    
    Esse método é mais robusto que extremos de t porque:
    - Prioriza proximidade física real
    - Menos sensível a ruído nas extremidades
    - Melhor para superfícies irregulares
    
    Parâmetros:
    - gota_pts: contorno completo da gota
    - line_params: (vx, vy, x0, y0) da regressão
    - distance_threshold: máxima distância perpendicular aceita (pixels)
    
    Retorna:
    - p_esq: [x, y] ponto de contato esquerdo (menor distância, lado esquerdo)
    - p_dir: [x, y] ponto de contato direito (menor distância, lado direito)
    """
    vx, vy, x0, y0 = line_params
    
    # Normalizar direção
    norm = np.sqrt(vx**2 + vy**2)
    if norm < 1e-6:
        return None, None
    vx, vy = vx / norm, vy / norm
    
    # ETAPA A: Calcular distância perpendicular de TODOS os pontos
    perp_distances = []
    for pt in gota_pts:
        dx = pt[0] - x0
        dy = pt[1] - y0
        # Distância perpendicular = |(-vy, vx) · (pt - x0, y0)|
        dist = abs(-vy * dx + vx * dy)
        perp_distances.append(dist)
    
    perp_distances = np.array(perp_distances)
    
    # ETAPA B: Filtrar por distância (proximidade à linha)
    close_mask = perp_distances < distance_threshold
    close_indices = np.where(close_mask)[0]
    
    if len(close_indices) < 2:
        # Fallback: usar os 2 pontos mais próximos
        close_indices = np.argsort(perp_distances)[:max(2, len(gota_pts)//10)]
    
    close_pts = gota_pts[close_indices]
    
    # ETAPA C: Filtrar por região Y (inferior da gota)
    x_rect, y_rect, w_rect, h_rect = cv2.boundingRect(gota_pts)
    y_threshold = y_rect + int(h_rect * 0.6)  # Região inferior
    
    y_mask = close_pts[:, 1] >= y_threshold
    region_pts_indices = close_indices[y_mask]
    
    if len(region_pts_indices) < 2:
        # Fallback: usar todos os próximos
        region_pts_indices = close_indices
    
    region_pts = gota_pts[region_pts_indices]
    region_distances = perp_distances[region_pts_indices]
    
    # ETAPA D: Separar por X do centróide
    center_x = np.mean(gota_pts[:, 0])
    
    esq_mask = region_pts[:, 0] < center_x
    dir_mask = region_pts[:, 0] > center_x
    
    esq_pts_indices = np.where(esq_mask)[0]
    dir_pts_indices = np.where(dir_mask)[0]
    
    # ETAPA E: Escolher ponto com MENOR distância perpendicular por lado
    if len(esq_pts_indices) > 0:
        esq_dists = region_distances[esq_pts_indices]
        min_esq_idx = esq_pts_indices[np.argmin(esq_dists)]
        p_esq = [float(region_pts[esq_pts_indices[np.argmin(esq_dists)], 0]),
                 float(region_pts[esq_pts_indices[np.argmin(esq_dists)], 1])]
    else:
        p_esq = [float(np.min(region_pts[:, 0])), float(np.mean(region_pts[:, 1]))]
    
    if len(dir_pts_indices) > 0:
        dir_dists = region_distances[dir_pts_indices]
        min_dir_idx = dir_pts_indices[np.argmin(dir_dists)]
        p_dir = [float(region_pts[dir_pts_indices[np.argmin(dir_dists)], 0]),
                 float(region_pts[dir_pts_indices[np.argmin(dir_dists)], 1])]
    else:
        p_dir = [float(np.max(region_pts[:, 0])), float(np.mean(region_pts[:, 1]))]
    
    # Garantir esquerdo < direito
    if p_esq[0] > p_dir[0]:
        p_esq, p_dir = p_dir, p_esq
    
    return p_esq, p_dir


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
    
    Método heurístico robusto para casos onde a regressão falha.
    
    Física: O ponto de contato é onde a gota tem menor largura (máxima curvatura,
    transição entre superfície e gota inclinada).
    
    Otimização: Usa stride adaptativo para não processar pixel-por-pixel em imagens grandes.
    """
    x, y, w, h = cv2.boundingRect(gota_pts)
    
    baseline_y = float(y + h) - 2.0
    search_start = int(y + h * 0.5)
    search_end = int(y + h * 0.95)
    
    # Stride adaptativo: reduz loop em imagens grandes
    # Para imagens com altura > 200 pixels, processar a cada 2-3 pixels
    stride = max(1, h // 100)  # ~1% da altura, mínimo 1
    
    min_width = float('inf')
    neck_candidate = -1
    
    if search_end > search_start:
        for row in range(search_start, search_end, stride):
            pts_in_row = gota_pts[np.abs(gota_pts[:, 1] - row) < 2]
            if len(pts_in_row) >= 2:
                w_row = np.max(pts_in_row[:, 0]) - np.min(pts_in_row[:, 0])
                if w_row < min_width:
                    min_width = w_row
                    neck_candidate = row
    
    # Refinar: se encontrou candidato, procurar mais precisamente na vizinhança
    if neck_candidate != -1 and neck_candidate > search_start:
        search_refined_start = max(search_start, neck_candidate - stride)
        search_refined_end = min(search_end, neck_candidate + stride)
        
        for row in range(search_refined_start, search_refined_end):
            pts_in_row = gota_pts[np.abs(gota_pts[:, 1] - row) < 2]
            if len(pts_in_row) >= 2:
                w_row = np.max(pts_in_row[:, 0]) - np.min(pts_in_row[:, 0])
                if w_row < min_width:
                    min_width = w_row
                    neck_candidate = row
        
        baseline_y = float(neck_candidate)
    
    return baseline_y


def detectar_baseline_hibrida(gota_pts: np.ndarray,
                               min_candidates: int = 5,
                               min_r_squared: float = 0.6,
                               use_perpendicular_distance: bool = True) -> Dict:
    """Pipeline híbrido melhorado: regressão TLS + detecção por distância perpendicular.
    
    Esta é a função principal para detecção de baseline.
    
    NOVO: Usa detecção de pontos baseada em DISTÂNCIA PERPENDICULAR MÍNIMA
    (mais robusto que extremos de t).
    
    Fluxo:
    1. Selecionar pontos com curvatura baixa (superfície)
    2. Aplicar regressão TLS (Total Least Squares) - mais precisa
    3. Validar qualidade (R² ≥ 0.6) e sanidade física (ângulo, posição)
    4. Se bem-sucedido: encontrar pontos por distância perpendicular mínima
    5. Se falhar: usar fallback geométrico (cintura)
    
    A baseline pode estar inclinada e funciona com câmeras inclinadas.
    
    Parâmetros:
    - gota_pts: contorno da gota
    - min_candidates: mínimo de candidatos para regressão
    - min_r_squared: mínimo R² aceito (0.6 = bom compromisso)
    - use_perpendicular_distance: usar método de distância perpendicular (recomendado)
    
    Retorna dict:
    {
        'line_params': (vx, vy, x0, y0) ou None,
        'baseline_y': float,
        'r_squared': float (qualidade do fit, 0-1),
        'method': str ('tls' ou 'fallback'),
        'p_esq': [x, y],
        'p_dir': [x, y],
        'contact_method': str ('perpendicular' ou 'projection')
    }
    """
    if len(gota_pts) < 5:
        return {'line_params': None, 'baseline_y': 0.0, 'r_squared': 0.0,
                'method': 'error', 'p_esq': None, 'p_dir': None, 'contact_method': None}
    
    # ETAPA 1: Selecionar candidatos à superfície
    candidates = select_baseline_candidates(gota_pts)
    
    # ETAPA 2: Tentar regressão TLS (nova função)
    line_params, r_squared = fit_baseline_with_line(candidates, gota_pts, method='tls')
    
    if line_params is not None and r_squared >= min_r_squared and len(candidates) >= min_candidates:
        # Regressão TLS bem-sucedida!
        
        # ETAPA 3: Encontrar pontos de contato
        if use_perpendicular_distance:
            # NOVO: Usar método de distância perpendicular mínima (seu pseudocódigo)
            p_esq, p_dir = find_contact_points_by_perpendicular_distance(
                gota_pts, line_params, distance_threshold=2.5
            )
            contact_method = 'perpendicular'
        else:
            # Alternativa: Usar projeção paramétrica (método anterior)
            p_esq, p_dir = project_contour_onto_baseline(gota_pts, line_params)
            contact_method = 'projection'
        
        baseline_y = line_params[3]  # y0 da linha
        
        return {
            'line_params': line_params,
            'baseline_y': baseline_y,
            'r_squared': r_squared,
            'method': 'tls',
            'p_esq': p_esq,
            'p_dir': p_dir,
            'contact_method': contact_method
        }
    else:
        # ETAPA 4: Fallback — usar cintura
        baseline_y = detectar_baseline_cintura(gota_pts)
        p_esq, p_dir = encontrar_pontos_contato(gota_pts, baseline_y)
        
        return {
            'line_params': None,
            'baseline_y': baseline_y,
            'r_squared': 0.0,
            'method': 'fallback',
            'p_esq': p_esq,
            'p_dir': p_dir,
            'contact_method': None
        }


def encontrar_pontos_contato(gota_pts: np.ndarray, baseline_y: float) -> Tuple:
    """Encontra pontos de contato na altura da baseline (para compatibilidade).
    
    Este é um wrapper do método anterior, mantido para compatibilidade com main.py.
    Usado quando a regressão falha (fallback cintura).
    """
    threshold_y = 5
    base_pts = gota_pts[np.abs(gota_pts[:, 1] - baseline_y) < threshold_y]
    
    if len(base_pts) > 0:
        p_esq = [float(np.min(base_pts[:, 0])), baseline_y]
        p_dir = [float(np.max(base_pts[:, 0])), baseline_y]
        return p_esq, p_dir
    else:
        # Fallback: usar bounding box
        x, y, w, h = cv2.boundingRect(gota_pts)
        p_esq = [float(x), baseline_y]
        p_dir = [float(x + w), baseline_y]
        return p_esq, p_dir


def diagnosticar_baseline(gota_pts: np.ndarray,
                          baseline_result: Dict) -> Dict:
    """Função de diagnóstico para verificar qualidade da baseline.
    
    Retorna métricas de qualidade e recomendações para debugging.
    Útil para validação e troubleshooting em sistemas multi-usuário.
    
    Retorna dict com:
    - method: 'regression' ou 'fallback'
    - r_squared: qualidade do fit
    - num_candidatos: quantos pontos passaram no filtro de curvatura
    - angulo_baseline: inclinação estimada em graus
    - status: 'OK', 'MARGINAL' ou 'FALLBACK'
    - msg: string com diagnóstico
    """
    if baseline_result['method'] == 'error':
        return {
            'method': 'error',
            'status': 'ERRO',
            'msg': 'Contorno muito pequeno ou inválido'
        }
    
    candidates = select_baseline_candidates(gota_pts)
    num_cand = len(candidates)
    
    result_info = {
        'method': baseline_result['method'],
        'r_squared': baseline_result['r_squared'],
        'num_candidatos': num_cand,
        'baseline_y': baseline_result['baseline_y']
    }
    
    if baseline_result['method'] == 'regression':
        line_params = baseline_result['line_params']
        vx, vy, x0, y0 = line_params
        angle_rad = np.arctan2(abs(vy), abs(vx))
        angle_deg = np.degrees(angle_rad)
        
        result_info['angulo_baseline'] = angle_deg
        
        if baseline_result['r_squared'] >= 0.8 and num_cand >= 10:
            result_info['status'] = 'OK'
            result_info['msg'] = f'Regressão excelente: R²={baseline_result["r_squared"]:.3f}, ' \
                                  f'ângulo={angle_deg:.1f}°, {num_cand} candidatos'
        elif baseline_result['r_squared'] >= 0.7 and num_cand >= 5:
            result_info['status'] = 'OK'
            result_info['msg'] = f'Regressão aceitável: R²={baseline_result["r_squared"]:.3f}, ' \
                                  f'ângulo={angle_deg:.1f}°, {num_cand} candidatos'
        else:
            result_info['status'] = 'MARGINAL'
            result_info['msg'] = f'Regressão marginal: R²={baseline_result["r_squared"]:.3f}'
    else:
        result_info['angulo_baseline'] = 0.0
        result_info['status'] = 'FALLBACK'
        result_info['msg'] = f'Fallback cintura usado ({num_cand} candidatos disponíveis)'
    
    return result_info