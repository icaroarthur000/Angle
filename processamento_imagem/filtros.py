import cv2
import numpy as np

def aplicar_pre_processamento(imagem):
    """Pipeline simplificado e robusto para detecção de gota.
    
    Etapas:
    1. Converte para tons de cinza
    2. Aplica Gaussian Blur (5, 5) para suavização
    3. Binarização com Otsu (invertido) para criar máscara inicial
    4. MORPH_CLOSE (5, 5) para selar a gota como massa sólida única e eliminar buracos
    
    Retorna:
    - gray: imagem em escala de cinza (uint8)
    - bin_img: imagem binarizada (uint8, 0/255) com gota como massa branca sólida
    """
    # 1) Converter para tons de cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # 2) Gaussian Blur (5, 5) para reduzir ruído
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 3) Otsu threshold (invertido para ter a gota em branco)
    _, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 4) MORPH_CLOSE com kernel (5, 5) para garantir gota como massa sólida única, sem buracos
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    return gray, bin_img