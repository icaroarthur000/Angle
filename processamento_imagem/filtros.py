import cv2
import numpy as np


def preprocessar_imagem_robusto(imagem):
    """Melhora contraste local e reduz sensibilidade a iluminação irregular."""
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray_clahe = clahe.apply(gray)
    return cv2.GaussianBlur(gray_clahe, (3, 3), 0)


def _fechar_mascara(bin_img, kernel_size=(5, 5), iterations=1):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    return cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel, iterations=iterations)


def aplicar_filtro_binary_otsu(imagem):
    """Binarização OTSU com fechamento morfológico."""
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    bin_img = _fechar_mascara(bin_img, (5, 5), iterations=1)
    return gray, bin_img


def aplicar_filtro_edges_canny(imagem):
    """Detecção de bordas por Canny."""
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 30, 100)
    return gray, edges


def aplicar_filtro_binary_adaptive(imagem):
    """Binarização adaptativa gaussiana com limpeza morfológica."""
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    h, w = blur.shape[:2]
    blocksize = max(31, (min(h, w) // 30) | 1)
    binary = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        blocksize,
        2,
    )
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)
    return gray, binary


def aplicar_preprocessamento_clahe(imagem):
    gray_clahe = preprocessar_imagem_robusto(imagem)
    return gray_clahe, gray_clahe


def _score_mascara(bin_img):
    total_pixels = float(bin_img.shape[0] * bin_img.shape[1])
    white_pixels = float(np.count_nonzero(bin_img == 255))
    fill_ratio = white_pixels / total_pixels if total_pixels else 0.0
    if fill_ratio < 0.03 or fill_ratio > 0.92:
        return -999.0

    unique, counts = np.unique(bin_img, return_counts=True)
    probs = counts / total_pixels if total_pixels else np.array([1.0])
    entropy = -np.sum(probs * np.log2(probs + 1e-10))
    return (0.7 * fill_ratio) - (0.3 * entropy / 8.0)


def aplicar_multi_threshold(imagem):
    """Testa OTSU, ADAPTIVE e CANNY e retorna a máscara mais promissora."""
    _, bin_otsu = aplicar_filtro_binary_otsu(imagem)
    _, bin_adaptive = aplicar_filtro_binary_adaptive(imagem)
    _, edges = aplicar_filtro_edges_canny(imagem)
    bin_canny = _fechar_mascara(edges, (3, 3), iterations=2)

    candidatos = {
        "OTSU": (bin_otsu, _score_mascara(bin_otsu)),
        "ADAPTIVE": (bin_adaptive, _score_mascara(bin_adaptive)),
        "CANNY": (bin_canny, _score_mascara(bin_canny)),
    }

    metodo, (mask, _) = max(candidatos.items(), key=lambda item: item[1][1])
    return mask, metodo


def aplicar_pre_processamento(imagem):
    """Compatibilidade: mantém OTSU como pipeline padrão simples."""
    return aplicar_filtro_binary_otsu(imagem)
