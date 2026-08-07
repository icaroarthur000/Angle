import math
import logging
import numpy as np

logger = logging.getLogger(__name__)


def _segmentos_contorno(gota_pts, to_scr, max_gap_img_px: float = 2.5):
    """Divide o contorno em ramos e remove a faixa inferior de ligação.

    O contorno analisado pode ser fechado, mas para exibição não deve desenhar
    a ligação inferior nem unir os dois lados por baixo da gota.
    """
    if gota_pts is None or len(gota_pts) < 2:
        return []

    pts = np.asarray(gota_pts, dtype=np.float32).reshape(-1, 2)
    y_max = float(np.max(pts[:, 1]))
    y_min = float(np.min(pts[:, 1]))
    altura = max(1.0, y_max - y_min)

    # Remove a última faixa inferior para evitar o arco que encosta na base.
    faixa_inferior = max(3.0, 0.015 * altura)
    pts_visiveis = pts[pts[:, 1] < (y_max - faixa_inferior)]
    if len(pts_visiveis) < 2:
        return []

    segmentos = []
    segmento_atual = []
    ponto_prev = None

    for pt in pts_visiveis:
        x_scr, y_scr = to_scr(pt[0], pt[1])
        ponto_atual = (float(x_scr), float(y_scr))

        if ponto_prev is not None:
            gap_img = float(np.hypot(float(pt[0] - ponto_prev[0]), float(pt[1] - ponto_prev[1])))
            if gap_img > max_gap_img_px and len(segmento_atual) >= 4:
                segmentos.append(segmento_atual)
                segmento_atual = []

        segmento_atual.extend(ponto_atual)
        ponto_prev = pt

    if len(segmento_atual) >= 4:
        segmentos.append(segmento_atual)

    return segmentos


def desenhar_baseline(canvas, baseline_y, ratio, offset_x, offset_y,
                      image_width=None, line_params=None):
    """
    Desenha a linha base (vermelha).
    Suporta baseline inclinada quando line_params=(vx, vy, x0, y0) é fornecido.
    """
    if baseline_y is None:
        return

    # AVISO-04: usa largura real do canvas como fallback em vez de 1000 px fixo
    w_img = image_width if image_width else canvas.winfo_width()

    # CROSS-01: renderiza a inclinação real da baseline quando disponível
    if line_params is not None:
        vx, vy, x0, y0 = line_params
        if abs(vx) > 1e-9:
            t_left  = (0 - x0) / vx
            t_right = (w_img - x0) / vx
            y_left  = y0 + t_left  * vy
            y_right = y0 + t_right * vy
            x1 = offset_x
            y1 = y_left  * ratio + offset_y
            x2 = offset_x + w_img * ratio
            y2 = y_right * ratio + offset_y
            canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags="baseline")
            return

    # Fallback: baseline horizontal
    y_scr = (baseline_y * ratio) + offset_y
    x_start = offset_x
    x_end = offset_x + (w_img * ratio)
    canvas.create_line(x_start, y_scr, x_end, y_scr, fill="red", width=2, tags="baseline")


def desenhar_contorno(canvas, gota_pts, to_scr):
    """
    Desenha o contorno da gota na tela.
    
    Args:
        canvas: Canvas do Tkinter
        gota_pts: Array Nx2 com pontos do contorno
        to_scr: Função para converter de coordenadas de imagem para tela
    """
    if gota_pts is None or len(gota_pts) < 2:
        return
    try:
        for segmento in _segmentos_contorno(gota_pts, to_scr):
            canvas.create_line(*segmento, fill="cyan", width=1, tags="contour")
    except (TypeError, ValueError) as e:
        logger.debug("desenhar_contorno: %s", e)


def desenhar_pontos_contato(canvas, p_esq, p_dir, to_scr):
    """
    Desenha os pontos de contato (amarelo) na tela.
    
    Args:
        canvas: Canvas do Tkinter
        p_esq: Ponto de contato esquerdo [x, y]
        p_dir: Ponto de contato direito [x, y]
        to_scr: Função para converter de coordenadas de imagem para tela
    """
    r = 5
    for p in [p_esq, p_dir]:
        if p is not None:
            try:
                x, y = to_scr(p[0], p[1])
                canvas.create_oval(x-r, y-r, x+r, y+r, fill="yellow", outline="black", tags="contact_point")
            except (TypeError, ValueError) as e:
                logger.debug("desenhar_pontos_contato: %s", e)
def desenhar_tangentes(canvas, p_esq, p_dir, ae, ad, zoom_scale, to_scr):
    """
    Desenha as linhas de tangente nos pontos de contato com proporção visual constante.
    """
    try:
        # Define a escala para evitar distorção visual na aproximação
        escala = zoom_scale if zoom_scale and zoom_scale > 0 else 1.0
        length = 50 / escala 
        
        if p_esq is not None and len(p_esq) == 2:
            x, y = p_esq
            angle_rad = math.radians(ae)
            
            # Vetor esquerdo: Y negativo para projetar a linha para cima
            dx = length * math.cos(angle_rad)
            dy = -length * math.sin(angle_rad)
            
            # Projeção de 20% abaixo da base para facilitar a visualização do vértice
            x1, y1 = to_scr(x - 0.2 * dx, y - 0.2 * dy)
            x2, y2 = to_scr(x + dx, y + dy)
            canvas.create_line(x1, y1, x2, y2, fill="green", width=2, tags="tangent")
        
        if p_dir is not None and len(p_dir) == 2:
            x, y = p_dir
            angle_rad = math.radians(ad)
            
            # Vetor direito: X negativo para espelhar, Y negativo para projetar para cima
            dx = -length * math.cos(angle_rad)
            dy = -length * math.sin(angle_rad)
            
            # Projeção de 20% abaixo da base para facilitar a visualização do vértice
            x1, y1 = to_scr(x - 0.2 * dx, y - 0.2 * dy)
            x2, y2 = to_scr(x + dx, y + dy)
            canvas.create_line(x1, y1, x2, y2, fill="green", width=2, tags="tangent")
            
    except (TypeError, ValueError, AttributeError) as e:
        logger.warning("Erro na renderização das tangentes: %s", e)

def desenhar_tangente_vetor(canvas, p_contato, vetor, zoom_scale, to_scr):
    """Desenha a tangente diretamente a partir do vetor calculado."""
    if p_contato is None or vetor is None or len(p_contato) != 2:
        return
    try:
        escala = zoom_scale if zoom_scale and zoom_scale > 0 else 1.0
        length = 50 / escala
        x, y = p_contato
        vx, vy = vetor
        x1, y1 = to_scr(x - vx * length, y - vy * length)
        x2, y2 = to_scr(x + vx * length, y + vy * length)
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, tags="tangent_vector")
    except (TypeError, ValueError, AttributeError) as e:
        logger.warning("Erro na renderização da tangente vetorial: %s", e)


def desenhar_contorno_destaque(canvas, gota_pts, to_scr, cor="orange", largura=2):
    """Desenha o contorno em destaque quando um ponto é corrigido."""
    if gota_pts is None or len(gota_pts) < 2:
        return
    try:
        for segmento in _segmentos_contorno(gota_pts, to_scr):
            canvas.create_line(*segmento, fill=cor, width=largura, tags="contour_highlight")
    except (TypeError, ValueError):
        pass