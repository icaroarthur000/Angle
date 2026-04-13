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


def _garantir_impar(valor: int, minimo: int = 3) -> int:
    valor = max(int(valor), minimo)
    return valor if valor % 2 == 1 else valor + 1


def aplicar_filtro_binary_otsu(imagem, blur_kernel=(5, 5), morph_kernel=(5, 5), morph_iterations=1):
    """Binarização OTSU com fechamento morfológico."""
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    kx = _garantir_impar(blur_kernel[0])
    ky = _garantir_impar(blur_kernel[1])
    blur = cv2.GaussianBlur(gray, (kx, ky), 0)
    _, bin_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    if morph_iterations > 0:
        bin_img = _fechar_mascara(bin_img, morph_kernel, iterations=morph_iterations)
    return gray, bin_img


def aplicar_filtro_edges_canny(imagem):
    """Detecção de bordas por Canny."""
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 30, 100)
    return gray, edges


def aplicar_filtro_binary_adaptive(
    imagem,
    blur_kernel=(5, 5),
    block_divisor=30,
    block_min=31,
    c_value=2,
    open_kernel=(3, 3),
    close_kernel=(3, 3),
    open_iterations=1,
    close_iterations=1,
):
    """Binarização adaptativa gaussiana com limpeza morfológica."""
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    kx = _garantir_impar(blur_kernel[0])
    ky = _garantir_impar(blur_kernel[1])
    blur = cv2.GaussianBlur(gray, (kx, ky), 0)
    h, w = blur.shape[:2]
    blocksize = _garantir_impar(max(block_min, min(h, w) // max(1, block_divisor)), minimo=3)
    if blocksize >= min(h, w):
        limite = _garantir_impar(max(3, min(h, w) - 1), minimo=3)
        blocksize = min(blocksize, limite)
    binary = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        blocksize,
        c_value,
    )
    if open_iterations > 0:
        kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, open_kernel)
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_open, iterations=open_iterations)
    if close_iterations > 0:
        kernel_close = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, close_kernel)
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_close, iterations=close_iterations)
    return gray, binary


def gerar_candidatos_segmentacao(imagem):
    """Gera máscaras candidatas com agressividades diferentes.

    A ordem vai do mais preservador ao mais robusto. A escolha final deve ser
    guiada pela qualidade da segmentação obtida, não pela aparência da imagem.
    """
    candidatos = {}

    _, candidatos["OTSU_LIGHT"] = aplicar_filtro_binary_otsu(
        imagem,
        blur_kernel=(3, 3),
        morph_kernel=(3, 3),
        morph_iterations=1,
    )
    _, candidatos["OTSU"] = aplicar_filtro_binary_otsu(imagem)

    _, candidatos["ADAPTIVE_LIGHT"] = aplicar_filtro_binary_adaptive(
        imagem,
        blur_kernel=(3, 3),
        block_divisor=60,
        block_min=11,
        c_value=1,
        open_iterations=0,
        close_iterations=0,
    )
    _, candidatos["ADAPTIVE"] = aplicar_filtro_binary_adaptive(imagem)

    _, edges = aplicar_filtro_edges_canny(imagem)
    candidatos["CANNY"] = _fechar_mascara(edges, (3, 3), iterations=2)
    return candidatos


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
    candidatos_segmentacao = gerar_candidatos_segmentacao(imagem)
    candidatos = {
        "OTSU": (candidatos_segmentacao["OTSU"], _score_mascara(candidatos_segmentacao["OTSU"])),
        "ADAPTIVE": (candidatos_segmentacao["ADAPTIVE"], _score_mascara(candidatos_segmentacao["ADAPTIVE"])),
        "CANNY": (candidatos_segmentacao["CANNY"], _score_mascara(candidatos_segmentacao["CANNY"])),
    }

    metodo, (mask, _) = max(candidatos.items(), key=lambda item: item[1][1])
    return mask, metodo


def aplicar_pre_processamento(imagem):
    """Compatibilidade: mantém OTSU como pipeline padrão simples."""
    return aplicar_filtro_binary_otsu(imagem)
