import cv2
import numpy as np

def encontrar_contorno_gota(imagem_binaria):
    """Encontra o maior contorno da gota tentando alguns passos
    para preencher possíveis falhas e preservar a borda completa.
    Retorna um array Nx2 com pontos (x,y) ou None.
    """
    img = imagem_binaria.copy()
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Tentativa 1: fechar pequenos buracos para obter contorno contínuo
    kernel = np.ones((5, 5), np.uint8)
    closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=2)

    conts, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Se não encontrou, tentar detecção por bordas (Canny)
    if not conts:
        edges = cv2.Canny(img, 50, 150)
        conts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if not conts:
        return None

    # Seleciona o maior contorno por área
    c = max(conts, key=cv2.contourArea)

    # Retorna os pontos completos do contorno (sem simplificação)
    pts = c.reshape(-1, 2)
    return pts