"""
adaptive_preprocessing.py
--------------------------
Pré-processamento adaptativo baseado na qualidade da imagem de entrada.

Modos disponíveis (definidos em quality_analyzer):
  - HIGH_QUALITY : kernels pequenos, sem CLAHE, sem morphology pesada
  - BALANCED     : kernels médios, CLAHE leve
  - ROBUST       : filtros agressivos (comportamento original)

Função principal: preprocess_adaptive(img_bgr, quality_mode=None)
  - Se quality_mode for None, detecta automaticamente.
  - Retorna dict compatível com preprocess_image_for_contact_angle.
"""

import cv2
import numpy as np
from typing import Optional, Dict, Any

from processamento_imagem.quality_analyzer import (
    analyze_image_quality,
    HIGH_QUALITY, BALANCED, ROBUST,
)


def _morph_cleanup(binary: np.ndarray, kernel_size: int = 3, iterations: int = 1) -> np.ndarray:
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN,  k, iterations=iterations)
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, k, iterations=iterations)
    return binary


def _preprocess_high_quality(img_bgr: np.ndarray) -> Dict[str, Any]:
    """
    Modo HIGH_QUALITY: imagem já boa → processamento mínimo.
    - GaussianBlur 3×3 apenas para suavizar aliasing
    - Threshold OTSU direto (sem CLAHE, sem correção de iluminação)
    - Morphology leve (kernel 3×3, 1 iteração)
    """
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    binary = _morph_cleanup(binary, kernel_size=3, iterations=1)
    enhanced = blurred
    corrected_bgr = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
    debug = {"gray": gray, "enhanced": enhanced, "binary": binary}
    return {
        "enhanced_gray":  enhanced,
        "binary":         binary,
        "corrected_bgr":  corrected_bgr,
        "debug_imgs":     debug,
        "quality_mode":   HIGH_QUALITY,
    }


def _preprocess_balanced(img_bgr: np.ndarray) -> Dict[str, Any]:
    """
    Modo BALANCED: qualidade média → CLAHE leve + adaptive threshold moderado.
    - GaussianBlur 3×3
    - CLAHE clipLimit=1.5, tileGridSize=(4,4)
    - Adaptive threshold blocksize mínimo 21
    - Morphology 3×3, 1 iteração
    """
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    h, w = blurred.shape[:2]

    # Correção de iluminação leve
    k_bg = max(51, (min(h, w) // 8) | 1)
    bg = cv2.GaussianBlur(blurred.astype(np.float32), (k_bg, k_bg), 0)
    corrected_f = (blurred.astype(np.float32) + 1.0) / (bg + 1.0) * 128.0
    corrected = np.clip(corrected_f, 0, 255).astype(np.uint8)

    # CLAHE leve
    tile = max(1, min(4, int(min(h, w) / 80)))
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(tile, tile))
    enhanced = clahe.apply(corrected)

    # Adaptive threshold moderado
    blocksize = max(21, (min(h, w) // 40) | 1)
    blocksize = blocksize if blocksize % 2 == 1 else blocksize + 1
    binary = cv2.adaptiveThreshold(
        enhanced, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        blocksize, 2,
    )
    binary = _morph_cleanup(binary, kernel_size=3, iterations=1)

    corrected_bgr = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
    debug = {"gray": gray, "corrected": corrected, "enhanced": enhanced, "binary": binary}
    return {
        "enhanced_gray":  enhanced,
        "binary":         binary,
        "corrected_bgr":  corrected_bgr,
        "debug_imgs":     debug,
        "quality_mode":   BALANCED,
    }


def _preprocess_robust(img_bgr: np.ndarray) -> Dict[str, Any]:
    """
    Modo ROBUST: imagem de baixa qualidade → filtros agressivos.
    Equivalente ao comportamento original de preprocess_image_for_contact_angle.
    - GaussianBlur 5×5 (ou 3×3 se imagem pequena)
    - Correção de iluminação completa (divisão pelo fundo)
    - CLAHE clipLimit=2.0, tileGridSize escalado
    - Adaptive threshold blocksize máx 31+
    - Morphology 3×3, 1 iteração
    """
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]

    # GaussianBlur adaptado ao tamanho
    nm = 5 if min(h, w) >= 100 else 3
    blurred = cv2.GaussianBlur(gray, (nm, nm), 0)

    # Correção de iluminação
    k_bg = max(51, (min(h, w) // 6) | 1)
    bg = cv2.GaussianBlur(blurred.astype(np.float32), (k_bg, k_bg), 0)
    corrected_f = (blurred.astype(np.float32) + 1.0) / (bg + 1.0) * 128.0
    corrected = np.clip(corrected_f, 0, 255).astype(np.uint8)

    # CLAHE
    tile = max(1, int(min(h, w) / 50))
    tg = (min(8, tile), min(8, tile))
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=tg)
    enhanced = clahe.apply(corrected)

    # Adaptive threshold
    blocksize = max(31, (min(h, w) // 30)) | 1
    # Ensure blocksize stays strictly below image dimension (OpenCV requirement)
    dim_min = min(h, w)
    if blocksize >= dim_min:
        max_allowed = dim_min - 1 if dim_min % 2 == 0 else dim_min - 2
        blocksize = max(3, max_allowed | 1)
    binary = cv2.adaptiveThreshold(
        enhanced, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        blocksize, 2,
    )
    binary = _morph_cleanup(binary, kernel_size=3, iterations=1)

    corrected_bgr = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
    debug = {"gray": gray, "bg": np.clip(bg, 0, 255).astype(np.uint8),
             "corrected": corrected, "enhanced": enhanced, "binary": binary}
    return {
        "enhanced_gray":  enhanced,
        "binary":         binary,
        "corrected_bgr":  corrected_bgr,
        "debug_imgs":     debug,
        "quality_mode":   ROBUST,
    }


_MODE_FUNCS = {
    HIGH_QUALITY: _preprocess_high_quality,
    BALANCED:     _preprocess_balanced,
    ROBUST:       _preprocess_robust,
}


def preprocess_adaptive(
    img_bgr: np.ndarray,
    quality_mode: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Pré-processamento adaptativo.

    Parâmetros
    ----------
    img_bgr      : np.ndarray  – imagem BGR uint8
    quality_mode : str | None  – HIGH_QUALITY, BALANCED ou ROBUST.
                                 Se None, detecta automaticamente.

    Retorno
    -------
    dict com chaves:
        "enhanced_gray"  : np.ndarray  – imagem processada em escala de cinza
        "binary"         : np.ndarray  – máscara binária uint8
        "corrected_bgr"  : np.ndarray  – versão BGR da imagem melhorada
        "debug_imgs"     : dict
        "quality_mode"   : str         – modo efetivamente usado
        "quality_info"   : dict        – métricas de qualidade (quando auto-detectado)
    """
    if not isinstance(img_bgr, np.ndarray):
        raise TypeError("img_bgr deve ser um numpy.ndarray")
    if img_bgr.ndim != 3 or img_bgr.shape[2] not in (3, 4):
        raise ValueError("img_bgr deve ser uma imagem BGR com 3 canais")

    # Converte BGRA → BGR se necessário
    if img_bgr.shape[2] == 4:
        img_bgr = cv2.cvtColor(img_bgr, cv2.COLOR_BGRA2BGR)

    quality_info: Dict[str, Any] = {}
    if quality_mode is None:
        quality_info = analyze_image_quality(img_bgr)
        quality_mode = quality_info["mode"]

    func = _MODE_FUNCS.get(quality_mode, _preprocess_balanced)
    result = func(img_bgr)
    result["quality_info"] = quality_info
    return result
