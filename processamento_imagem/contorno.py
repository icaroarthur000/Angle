import cv2
import numpy as np

def encontrar_contorno_gota(imagem_binaria):
    """
    Encontra o maior contorno da gota com máscara de segurança nas bordas.
    
    A máscara de 5px força fisicamente a separação da gota do frame da imagem,
    garantindo que nenhum contorno toque nas bordas (especialmente o fundo).
    """
    # Garante que a imagem seja 8-bit single channel
    if len(imagem_binaria.shape) == 3:
        img = cv2.cvtColor(imagem_binaria, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem_binaria.copy()

    # Passo 1: Fechamento morfológico LEVE.
    kernel = np.ones((3, 3), np.uint8)
    processed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)

    # CORREÇÃO CRÍTICA: Máscara de segurança - Borda preta de 10px
    # Isto garante de forma ROBUSTA que nenhum pixel branco toque nas bordas da imagem,
    # especialmente no fundo (y = h). Força a gota a "flutuar" bem longe do frame.
    # Espessura aumentada para 10px (de 5px) para garantir separação total.
    h, w = processed.shape[:2]
    cv2.rectangle(processed, (0, 0), (w - 1, h - 1), 0, thickness=10)

    # Passo 2: Encontrar contornos
    conts, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Fallback se a binarização falhou mas há bordas visíveis
    if not conts:
        edges = cv2.Canny(img, 30, 100)
        # Aplicar a máscara também no Canny para consistência (mesma 10px de espessura)
        cv2.rectangle(edges, (0, 0), (w - 1, h - 1), 0, thickness=10)
        conts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if not conts:
        return None

    # NOVO: Filtrar contornos que tocam as bordas da imagem
    h, w = img.shape[:2]
    margin = 5  # pixels de margem para considerar "tocando a borda"
    MAX_BORDER_TOUCHES = 3  # Contornos que tocam 3+ bordas são considerados borda da imagem
    valid_contours = []

    for c in conts:
        pts = c.reshape(-1, 2)
        
        # Verificar se o contorno toca as bordas
        touches_left = np.any(pts[:, 0] <= margin)
        touches_right = np.any(pts[:, 0] >= w - margin)
        touches_top = np.any(pts[:, 1] <= margin)
        touches_bottom = np.any(pts[:, 1] >= h - margin)
        
        # Se tocar 3 ou mais bordas, provavelmente é a borda da imagem (não a gota)
        border_count = sum([touches_left, touches_right, touches_top, touches_bottom])
        
        if border_count < MAX_BORDER_TOUCHES:  # Aceitar apenas se tocar menos de 3 bordas
            valid_contours.append(c)

    if not valid_contours:
        return None

    # Passo 3: Selecionar o maior contorno válido
    c = max(valid_contours, key=cv2.contourArea)

    # Passo 4: Filtrar ruído - contornos muito pequenos são desprezados
    if cv2.contourArea(c) < 100:
        return None

    # Retorna os pontos do contorno como array Nx2
    pts = c.reshape(-1, 2)
    
    # VALIDAÇÃO EXTRA: Garantir que nenhum ponto está pegando nas bordas
    # Remove pontos que estão muito perto das extremidades (10px de margem)
    margin = 10
    valid_mask = (
        (pts[:, 0] > margin) & (pts[:, 0] < w - margin) &  # Esquerda e direita
        (pts[:, 1] > margin) & (pts[:, 1] < h - margin)     # Topo e fundo
    )
    
    if np.sum(valid_mask) < 10:  # Se remover muito, não vale a pena
        return pts  # Retorna o original
    
    pts_filtered = pts[valid_mask]
    return pts_filtered if len(pts_filtered) > 0 else pts