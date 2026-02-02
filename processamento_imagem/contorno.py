import cv2
import numpy as np

def encontrar_contorno_gota(imagem_binaria):
    """
    Encontra o maior contorno da gota preservando a fidelidade da borda.
    Ajustado para não arredondar excessivamente a zona de contato.
    """
    # Garante que a imagem seja 8-bit single channel
    if len(imagem_binaria.shape) == 3:
        img = cv2.cvtColor(imagem_binaria, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem_binaria.copy()

    # Passo 1: Fechamento morfológico LEVE.
    # Usamos um kernel menor (3x3) ou menos iterações para não deformar a transição gota-substrato.
    kernel = np.ones((3, 3), np.uint8)
    processed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)

    # Passo 2: Encontrar contornos
    conts, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Fallback se a binarização falhou mas há bordas visíveis
    if not conts:
        edges = cv2.Canny(img, 30, 100) # Thresholds mais baixos para capturar transições suaves
        conts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if not conts:
        return None

    # Passo 3: Selecionar o maior contorno (assume-se que a gota é o objeto principal)
    c = max(conts, key=cv2.contourArea)

    # Passo 4: Limpeza de ruído (opcional)
    # Se o contorno for muito pequeno (ex: ruído de poeira), ignora.
    if cv2.contourArea(c) < 100:
        return None

    # Retorna os pontos completos Nx2
    pts = c.reshape(-1, 2)
    
    # IMPORTANTE: Garantir ordem sequencial dos pontos para o cálculo da curvatura
    # O findContours já costuma retornar ordenado, mas reshape garante a estrutura.
    return pts