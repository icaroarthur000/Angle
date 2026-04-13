import cv2
import numpy as np

# Modos de qualidade (espelha quality_analyzer para evitar import circular)
_HIGH_QUALITY = "HIGH_QUALITY"
_BALANCED     = "BALANCED"
_ROBUST       = "ROBUST"


def _ensure_odd(value: int) -> int:
    """Garante que o valor seja ímpar (necessário para blocksize do adaptiveThreshold)."""
    return value if value % 2 == 1 else value + 1


def preprocessar_imagem_robusto(imagem, quality_mode=None):
    """Melhora contraste local e reduz sensibilidade a iluminação irregular.

    Parâmetro quality_mode (opcional):
      - HIGH_QUALITY : CLAHE clipLimit=1.0, tileGridSize=(4,4), blur 3×3
      - BALANCED     : CLAHE clipLimit=1.5, tileGridSize=(4,4), blur 3×3 (padrão)
      - ROBUST       : CLAHE clipLimit=2.0, tileGridSize=(8,8), blur 3×3
    """
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    if quality_mode == _HIGH_QUALITY:
        clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(4, 4))
    elif quality_mode == _ROBUST:
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    else:  # BALANCED ou None → comportamento padrão anterior (compatibilidade)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray_clahe = clahe.apply(gray)
    return cv2.GaussianBlur(gray_clahe, (3, 3), 0)


def _fechar_mascara(bin_img, kernel_size=(5, 5), iterations=1):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    return cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel, iterations=iterations)


def aplicar_filtro_binary_otsu(imagem, quality_mode=None):
    """Binarização OTSU com fechamento morfológico.

    Parâmetro quality_mode (opcional):
      - HIGH_QUALITY : GaussianBlur 3×3, kernel de fechamento 3×3
      - BALANCED     : GaussianBlur 3×3, kernel de fechamento 5×5 (padrão)
      - ROBUST       : GaussianBlur 5×5, kernel de fechamento 5×5
    """
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    if quality_mode == _HIGH_QUALITY:
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        close_k = (3, 3)
    elif quality_mode == _ROBUST:
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        close_k = (5, 5)
    else:  # BALANCED ou None → comportamento padrão anterior
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        close_k = (5, 5)
    _, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    bin_img = _fechar_mascara(bin_img, close_k, iterations=1)
    return gray, bin_img


def aplicar_filtro_edges_canny(imagem, quality_mode=None):
    """Detecção de bordas por Canny.

    Parâmetro quality_mode (opcional):
      - HIGH_QUALITY : GaussianBlur 3×3
      - BALANCED/ROBUST: GaussianBlur 5×5 (comportamento padrão anterior)
    """
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    if quality_mode == _HIGH_QUALITY:
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
    else:
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 30, 100)
    return gray, edges


def aplicar_filtro_binary_adaptive(imagem, quality_mode=None):
    """Binarização adaptativa gaussiana com limpeza morfológica.

    Parâmetro quality_mode (opcional):
      - HIGH_QUALITY : GaussianBlur 3×3, blocksize mínimo 11
      - BALANCED     : GaussianBlur 3×3, blocksize mínimo 21
      - ROBUST       : GaussianBlur 5×5, blocksize mínimo 31 (comportamento anterior)
    """
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    if quality_mode == _HIGH_QUALITY:
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        blocksize = _ensure_odd(max(11, (min(h, w) // 50) | 1))
    elif quality_mode == _BALANCED:
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        blocksize = _ensure_odd(max(21, (min(h, w) // 40) | 1))
    else:  # ROBUST ou None → comportamento padrão anterior
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        blocksize = _ensure_odd(max(31, (min(h, w) // 30) | 1))
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


def aplicar_preprocessamento_clahe(imagem, quality_mode=None):
    gray_clahe = preprocessar_imagem_robusto(imagem, quality_mode=quality_mode)
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


def aplicar_multi_threshold(imagem, quality_mode=None):
    """Testa OTSU, ADAPTIVE e CANNY e retorna a máscara mais promissora.

    Parâmetro quality_mode (opcional): propagado para cada filtro individual.
    """
    _, bin_otsu = aplicar_filtro_binary_otsu(imagem, quality_mode=quality_mode)
    _, bin_adaptive = aplicar_filtro_binary_adaptive(imagem, quality_mode=quality_mode)
    _, edges = aplicar_filtro_edges_canny(imagem, quality_mode=quality_mode)
    bin_canny = _fechar_mascara(edges, (3, 3), iterations=2)

    candidatos = {
        "OTSU": (bin_otsu, _score_mascara(bin_otsu)),
        "ADAPTIVE": (bin_adaptive, _score_mascara(bin_adaptive)),
        "CANNY": (bin_canny, _score_mascara(bin_canny)),
    }

    metodo, (mask, _) = max(candidatos.items(), key=lambda item: item[1][1])
    return mask, metodo


def aplicar_pre_processamento(imagem, quality_mode=None):
    """Compatibilidade: mantém OTSU como pipeline padrão simples."""
    return aplicar_filtro_binary_otsu(imagem, quality_mode=quality_mode)
