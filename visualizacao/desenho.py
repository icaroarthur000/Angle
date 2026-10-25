import math
import logging
import cv2
import numpy as np

logger = logging.getLogger(__name__)


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
        pts_list = []
        for pt in gota_pts:
            pts_list.extend(to_scr(pt[0], pt[1]))
        canvas.create_line(*pts_list, fill="cyan", width=1, tags="contour")
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

def segmento_tangente_exterior(
    p_contato,
    vetor,
    contour_pts,
    baseline_y,
    binary_mask,
    length,
    lado="esq",
):
    """Return the upper-facing tangent ray, clipped before it enters the drop mask."""
    if p_contato is None or vetor is None or contour_pts is None or binary_mask is None:
        return None
    if len(p_contato) != 2 or len(contour_pts) < 3 or length <= 0 or lado not in ("esq", "dir"):
        return None

    contact = tuple(float(value) for value in p_contato)
    direction = np.asarray(vetor, dtype=float).reshape(-1).copy()
    if direction.size != 2 or not np.all(np.isfinite(direction)):
        return None
    norm = float(np.linalg.norm(direction))
    if norm < 1e-9:
        return None
    direction /= norm

    if baseline_y is None:
        return None
    if abs(direction[1]) <= 1e-6:
        if (lado == "esq" and direction[0] > 0) or (lado == "dir" and direction[0] < 0):
            direction *= -1
    elif direction[1] > 0:
        direction *= -1
    upper_ray = direction

    mask = np.asarray(binary_mask)
    if mask.ndim == 3:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    height, width = mask.shape[:2]
    interior_mask = cv2.erode(mask, np.ones((3, 3), dtype=np.uint8), iterations=1)

    end_distance = float(length)
    step = 0.5
    for distance in np.arange(2.0, end_distance + step, step):
        x = int(round(contact[0] + upper_ray[0] * distance))
        y = int(round(contact[1] + upper_ray[1] * distance))
        if x < 0 or x >= width or y < 0 or y >= height:
            end_distance = max(0.0, distance - step)
            break
        if interior_mask[y, x] > 0:
            end_distance = max(0.0, distance - step)
            break

    if end_distance < 2.0:
        logger.debug(
            "Tangente omitida: ajuste entra na máscara antes de formar um segmento visível "
            "(contato=%s, vetor=%s).",
            contact,
            direction.tolist(),
        )
        return None
    end = np.asarray(contact) + upper_ray * end_distance
    return contact, (float(end[0]), float(end[1]))


def desenhar_tangente_vetor(
    canvas,
    p_contato,
    vetor,
    zoom_scale,
    to_scr,
    contour_pts=None,
    baseline_y=None,
    binary_mask=None,
    lado="esq",
):
    """Draw only the outward-facing portion of the fitted tangent."""
    if p_contato is None or vetor is None or len(p_contato) != 2:
        return
    try:
        escala = zoom_scale if zoom_scale and zoom_scale > 0 else 1.0
        length = 50 / escala
        segment = segmento_tangente_exterior(
            p_contato,
            vetor,
            contour_pts,
            baseline_y,
            binary_mask,
            length,
            lado,
        )
        if segment is None:
            return
        x1, y1 = to_scr(*segment[0])
        x2, y2 = to_scr(*segment[1])
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2, tags="tangent_vector")
    except (TypeError, ValueError, AttributeError) as e:
        logger.warning("Erro na renderização da tangente vetorial: %s", e)


def desenhar_contorno_destaque(canvas, gota_pts, to_scr, cor="orange", largura=2):
    """Desenha o contorno em destaque quando um ponto é corrigido."""
    if gota_pts is None or len(gota_pts) < 2:
        return
    try:
        pts_list = []
        for pt in gota_pts:
            pts_list.extend(to_scr(pt[0], pt[1]))
        canvas.create_line(*pts_list, fill=cor, width=largura, tags="contour_highlight")
    except (TypeError, ValueError):
        pass