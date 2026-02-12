import math


def desenhar_baseline(canvas, baseline_y, ratio, offset_x, offset_y, 
                     image_width=None, line_params=None):
    """
    Desenha a linha base (vermelha).
    Garante que a linha acompanhe a gota milimetricamente no zoom.
    """
    if baseline_y is None:
        return

    # 1. Definir a extensão da linha (do início ao fim da largura da imagem)
    # Se image_width não for passado, tentamos pegar do canvas, mas o ideal é vir do main
    w_img = image_width if image_width else 1000

    # CORREÇÃO: Ignorar line_params temporariamente
    # Sempre usar a linha horizontal até corrigir o cálculo de line_params
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
    except Exception:
        pass


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
            except Exception:
                pass


def desenhar_tangentes(canvas, p_esq, p_dir, ae, ad, zoom_scale, to_scr):
    """
    Desenha as linhas de tangente nos pontos de contato.
    
    Args:
        canvas: Canvas do Tkinter
        p_esq: Ponto de contato esquerdo [x, y]
        p_dir: Ponto de contato direito [x, y]
        ae: Ângulo esquerdo em graus
        ad: Ângulo direito em graus
        zoom_scale: Escala de zoom
        to_scr: Função para converter de coordenadas de imagem para tela
    """
    try:
        import math
        
        # Comprimento da linha tangente (em pixels de imagem)
        length = 40 / zoom_scale
        
        if p_esq is not None and len(p_esq) == 2:
            x, y = p_esq
            # Converter ângulo para radianos
            angle_rad = math.radians(ae)
            dx = length * math.cos(angle_rad)
            dy = length * math.sin(angle_rad)
            
            x1, y1 = to_scr(x - dx, y - dy)
            x2, y2 = to_scr(x + dx, y + dy)
            canvas.create_line(x1, y1, x2, y2, fill="green", width=2, tags="tangent")
        
        if p_dir is not None and len(p_dir) == 2:
            x, y = p_dir
            # Converter ângulo para radianos
            angle_rad = math.radians(ad)
            dx = length * math.cos(angle_rad)
            dy = length * math.sin(angle_rad)
            
            x1, y1 = to_scr(x - dx, y - dy)
            x2, y2 = to_scr(x + dx, y + dy)
            canvas.create_line(x1, y1, x2, y2, fill="green", width=2, tags="tangent")
    except Exception as e:
        print(f"Erro ao desenhar tangentes: {e}")