import cv2
import numpy as np

def aplicar_pre_processamento(imagem):
    """Aplica escala de cinza, blur e threshold."""
    # Converte para tons de cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Aplica um leve desfoque para reduzir ruído
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Aplica limiarização (Threshold) de Otsu invertido
    _, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Limpeza morfológica para remover pontos brancos pequenos (ruído)
    bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    
    return gray, bin_img