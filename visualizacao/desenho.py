"""desenho.py

Funções de renderização para o sistema de medição de ângulo de contato.

Suporta:
- Contornos da gota
- Linha base (baseline) inclinada via regressão
- Pontos de contato
- Tangentes para visualização dos ângulos

Todas as funções recebem uma função to_scr(x, y) que converte
coordenadas de imagem para tela, garantindo coerência de zoom/pan.
"""

import cv2
import numpy as np
import math


def desenhar_contorno(canvas, gota_pts: np.ndarray, to_scr):
    """Desenha o contorno da gota no canvas com uma única chamada (OTIMIZADO).
    
    Parâmetros:
    - canvas: canvas Tkinter
    - gota_pts: array Nx2 com pontos (x, y) do contorno em coordenadas de imagem
    - to_scr: função callback to_scr(x, y) → (x_tela, y_tela)
    
    OTIMIZAÇÃO CRÍTICA: Constrói uma lista plana [x1, y1, x2, y2, ...] e faz uma única
    chamada ao canvas.create_line(). Isso elimina o "piscar" causado por milhares de
    chamadas individuais e acelera a renderização ~10x.
    """
    if gota_pts is None or len(gota_pts) < 3:
        return
    
    # Converter todos os pontos para coordenadas de tela em uma passagem
    pts_tela = []
    for pt in gota_pts:
        x_scr, y_scr = to_scr(pt[0], pt[1])
        pts_tela.append(int(round(x_scr)))
        pts_tela.append(int(round(y_scr)))
    
    # Fechar o polígono: adicionar o primeiro ponto ao final para formar loop fechado
    if len(pts_tela) >= 6:  # pelo menos 3 pontos (6 coordenadas)
        pts_tela.append(pts_tela[0])
        pts_tela.append(pts_tela[1])
    
    # UMA ÚNICA CHAMADA ao canvas para desenhar todo o contorno (não múltiplas)
    if len(pts_tela) >= 4:
        canvas.create_line(*pts_tela, fill="cyan", width=1)


def desenhar_pontos_contato(canvas, p_esq, p_dir, to_scr):
    """Desenha os pontos de contato (esquerdo e direito) no canvas.
    
    Parâmetros:
    - canvas: canvas Tkinter
    - p_esq: [x, y] ponto de contato esquerdo em coordenadas de imagem
    - p_dir: [x, y] ponto de contato direito em coordenadas de imagem
    - to_scr: função callback to_scr(x, y) → (x_tela, y_tela)
    """
    if p_esq is None or p_dir is None:
        return
    
    radius = 5
    
    # ponto esquerdo
    x_esq, y_esq = to_scr(p_esq[0], p_esq[1])
    x_esq, y_esq = int(round(x_esq)), int(round(y_esq))
    canvas.create_oval(
        x_esq - radius, y_esq - radius,
        x_esq + radius, y_esq + radius,
        fill="yellow",
        outline="yellow"
    )
    
    # ponto direito
    x_dir, y_dir = to_scr(p_dir[0], p_dir[1])
    x_dir, y_dir = int(round(x_dir)), int(round(y_dir))
    canvas.create_oval(
        x_dir - radius, y_dir - radius,
        x_dir + radius, y_dir + radius,
        fill="yellow",
        outline="yellow"
    )


def desenhar_tangentes(canvas, p_esq, p_dir, angle_esq, angle_dir, 
                       zoom_scale, to_scr, tangent_length: int = 50):
    """Desenha as tangentes aos ângulos de contato no canvas.
    
    Parâmetros:
    - canvas: canvas Tkinter
    - p_esq: [x, y] ponto de contato esquerdo
    - p_dir: [x, y] ponto de contato direito
    - angle_esq: ângulo de contato esquerdo (graus)
    - angle_dir: ângulo de contato direito (graus)
    - zoom_scale: fator de zoom (para escalar comprimento das tangentes)
    - to_scr: função callback to_scr(x, y) → (x_tela, y_tela)
    - tangent_length: comprimento base da tangente em pixels
    """
    if p_esq is None or p_dir is None or angle_esq is None or angle_dir is None:
        return
    
    # escalar comprimento conforme zoom
    length = int(tangent_length * zoom_scale)
    
    # tangente esquerda
    angle_esq_rad = math.radians(angle_esq)
    dx_esq = length * math.cos(angle_esq_rad)
    dy_esq = -length * math.sin(angle_esq_rad)  # inverter Y (canvas)
    
    x_esq_1, y_esq_1 = to_scr(p_esq[0], p_esq[1])
    x_esq_2, y_esq_2 = to_scr(p_esq[0] + dx_esq, p_esq[1] + dy_esq)
    
    canvas.create_line(
        int(round(x_esq_1)), int(round(y_esq_1)),
        int(round(x_esq_2)), int(round(y_esq_2)),
        fill="lime",
        width=2
    )
    
    # tangente direita
    angle_dir_rad = math.radians(angle_dir)
    dx_dir = length * math.cos(angle_dir_rad)
    dy_dir = -length * math.sin(angle_dir_rad)
    
    x_dir_1, y_dir_1 = to_scr(p_dir[0], p_dir[1])
    x_dir_2, y_dir_2 = to_scr(p_dir[0] + dx_dir, p_dir[1] + dy_dir)
    
    canvas.create_line(
        int(round(x_dir_1)), int(round(y_dir_1)),
        int(round(x_dir_2)), int(round(y_dir_2)),
        fill="lime",
        width=2
    )


def desenhar_baseline(canvas, baseline_y, ratio, offset_x, offset_y, 
                      image_width: int = None, line_params=None):
    """Desenha a linha base (baseline) no canvas, suportando inclinação.
    
    Parâmetros:
    - canvas: canvas Tkinter
    - baseline_y: coordenada Y da baseline na imagem (para compatibilidade)
    - ratio: fator de zoom aplicado
    - offset_x: deslocamento horizontal (ox em main.py)
    - offset_y: deslocamento vertical (oy em main.py)
    - image_width: largura da imagem escalada (nw em main.py); se None, usa canvas.winfo_width()
    - line_params: (vx, vy, x0, y0) da regressão; se None, assume horizontal
    
    Se line_params for fornecido, desenha a linha base inclinada.
    Caso contrário, desenha uma linha horizontal simples (fallback).
    """
    # defina largura padrão se não informado
    if image_width is None:
        image_width = canvas.winfo_width()
    
    # conversão Y para screen
    y_base_scr = int(round(baseline_y * ratio + offset_y))
    
    # se há parâmetros de regressão, usar linha inclinada
    if line_params is not None:
        vx, vy, x0, y0 = line_params
        # normalizar direção
        norm = np.sqrt(vx**2 + vy**2)
        if norm > 1e-6:
            vx, vy = vx / norm, vy / norm
        
        # encontrar pontos de início e fim da linha base dentro da imagem
        # parametrização: (x, y) = (x0, y0) + t * (vx, vy)
        # queremos que x varie de 0 a image_width
        
        if abs(vx) > 1e-6:
            # solucionar para t: x = x0 + t*vx; t = (x - x0) / vx
            t_start = (0 - x0) / vx
            t_end = (image_width - x0) / vx
        else:
            # linha vertical, não pode ser baseline principal
            t_start = 0
            t_end = 1
        
        # calcular pontos nos limites horizontais
        x_start = int(round(offset_x))
        y_start = int(round(y0 + t_start * vy))
        x_start_scr = x_start
        y_start_scr = int(round(y_start * ratio + offset_y))
        
        x_end = int(round(offset_x + image_width))
        y_end = int(round(y0 + t_end * vy))
        x_end_scr = x_end
        y_end_scr = int(round(y_end * ratio + offset_y))
        
        # desenhar linha inclinada
        canvas.create_line(
            x_start_scr, y_start_scr,
            x_end_scr, y_end_scr,
            fill="red",
            width=2
        )
    else:
        # fallback: linha horizontal simples
        x_start_scr = int(round(offset_x))
        x_end_scr = int(round(offset_x + image_width))
        
        canvas.create_line(
            x_start_scr, y_base_scr,
            x_end_scr, y_base_scr,
            fill="red",
            width=2
        )
