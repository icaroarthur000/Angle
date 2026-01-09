"""preprocess.py

Funções de pré-processamento robusto para medições de ângulo de contato.

API principal:
    - `preprocess_image_for_contact_angle(img_bgr, ...)` -> dict com chaves
        `enhanced_gray`, `binary`, `corrected_bgr`, `debug_imgs`
    - `save_debug_imgs(debug_dict, out_dir, prefix="dbg")` salva imagens de debug

Principais características:
    - correção de iluminação por divisão usando um background estimado
    - CLAHE com grid que escala com o tamanho da imagem
    - binarização adaptativa (Gaussian) com block size protegido para imagens pequenas
    - limpeza morfológica opcional

Este arquivo fornece validações de entrada e garante que `debug_imgs` contenha
imagens uint8 prontas para salvar/exibição.
"""

import os
from typing import Dict, Any, Optional, Tuple

import cv2
import numpy as np


def estimate_background(img_gray, bg_ksize=None):
    h, w = img_gray.shape[:2]
    if bg_ksize is None:
        k = max(51, (min(h, w) // 6) | 1)  # odd and scale with image
    else:
        k = bg_ksize if bg_ksize % 2 == 1 else bg_ksize + 1
    bg = cv2.GaussianBlur(img_gray, (k, k), 0)
    return bg


def correct_illumination_divide(img_gray, bg):
    img_f = img_gray.astype(np.float32) + 1.0
    bg_f = bg.astype(np.float32) + 1.0
    corrected = (img_f / bg_f) * 128.0
    corrected = np.clip(corrected, 0, 255).astype(np.uint8)
    return corrected


def preprocess_image_for_contact_angle(img_bgr,
                                       nm_gauss=3,
                                       bg_ksize=None,
                                       clahe_clip=2.0,
                                       clahe_grid: Optional[Tuple[int, int]] = None,
                                       adapt_blocksize=None,
                                       adapt_C=2,
                                       do_morph_cleanup=True):
    """
    Recebe imagem BGR (crop) e retorna dict:
      - enhanced_gray: imagem após correção e CLAHE (uint8)
      - binary: imagem binarizada (uint8, 0/255)
      - corrected_bgr: enhanced_gray convertido para BGR (para preview)
      - debug_imgs: dict {gray, bg, corrected, enhanced, binary}
    Parâmetros adaptam-se ao tamanho da imagem quando None.
    """
    # --- Validação de entrada ---
    if not isinstance(img_bgr, np.ndarray):
        raise TypeError("img_bgr deve ser um numpy.ndarray")
    if img_bgr.ndim != 3 or img_bgr.shape[2] not in (3, 4):
        raise ValueError("img_bgr deve ser uma imagem BGR com 3 canais")

    # 1) gray + denoise
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    if nm_gauss and nm_gauss > 0:
        k = nm_gauss if nm_gauss % 2 == 1 else nm_gauss + 1
        gray = cv2.GaussianBlur(gray, (k, k), 0)

    # 2) estimate background and correct illumination
    h, w = gray.shape[:2]
    if bg_ksize is None:
        bg_k = max(51, (min(h, w) // 6) | 1)
    else:
        bg_k = bg_ksize if bg_ksize % 2 == 1 else bg_ksize + 1
    bg = estimate_background(gray, bg_k)
    corrected = correct_illumination_divide(gray, bg)

    # 3) CLAHE (tile grid escala com a imagem quando não informado)
    if clahe_grid is None:
        # heurística: número de tiles proporcional ao menor lado
        tile = max(1, int(min(h, w) / 50))
        tg = (min(8, tile), min(8, tile))
    else:
        tg = (max(1, int(clahe_grid[0])), max(1, int(clahe_grid[1])))
    clahe = cv2.createCLAHE(clipLimit=clahe_clip, tileGridSize=tg)
    enhanced = clahe.apply(corrected)

    # 4) adaptive threshold
    if adapt_blocksize is None:
        # block proportional to image size (odd)
        adapt_blocksize = max(31, (min(h, w) // 30) | 1)
    blockSize = adapt_blocksize if adapt_blocksize % 2 == 1 else adapt_blocksize + 1
    # protege blockSize para não ser maior que a dimensão da imagem
    max_allowed = max(3, min(h, w) - (1 if (min(h, w) % 2 == 0) else 0))
    if blockSize >= min(h, w):
        blockSize = max_allowed if max_allowed % 2 == 1 else max_allowed - 1
    binary = cv2.adaptiveThreshold(enhanced, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV,
                                   blockSize, adapt_C)

    # 5) morphological cleanup (configurável; parâmetros fixos são um bom default)
    if do_morph_cleanup:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
        binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)

    corrected_bgr = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)

    # garante que todas as imagens de debug sejam uint8
    def _to_uint8(img: np.ndarray) -> np.ndarray:
        if img is None:
            return None
        if img.dtype == np.uint8:
            return img
        arr = np.clip(img, 0, 255).astype(np.uint8)
        return arr

    debug = {"gray": _to_uint8(gray), "bg": _to_uint8(bg), "corrected": _to_uint8(corrected),
             "enhanced": _to_uint8(enhanced), "binary": _to_uint8(binary)}

    return {
        "enhanced_gray": enhanced,
        "binary": binary,
        "corrected_bgr": corrected_bgr,
        "debug_imgs": debug
    }


def save_debug_imgs(debug_dict: Dict[str, Any], out_dir: str, prefix: str = "dbg") -> Dict[str, str]:
    """Salva imagens do `debug_dict` em `out_dir` com o `prefix` e retorna um map de caminhos.
    
    Parâmetros:
    - debug_dict: dict de nome->imagem (grayscale ou BGR), preferencialmente uint8
    - out_dir: diretório de saída (será criado se não existir)
    - prefix: prefixo dos nomes de arquivo (default: "dbg")
    
    Retorna:
    - dict {nome: caminho_arquivo} para os itens salvos com sucesso
    - Continua mesmo se algumas imagens falharem (não quebra pipeline)
    """
    os.makedirs(out_dir, exist_ok=True)
    saved: Dict[str, str] = {}
    
    for k, img in (debug_dict or {}).items():
        if img is None:
            continue
        
        # garante uint8
        if isinstance(img, np.ndarray) and img.dtype != np.uint8:
            img_to_save = np.clip(img, 0, 255).astype(np.uint8)
        else:
            img_to_save = img
        
        path = os.path.join(out_dir, f"{prefix}_{k}.png")
        
        try:
            ok = cv2.imwrite(path, img_to_save)
            if ok:
                saved[k] = path
        except Exception:
            # não interrompe; coleta somente o que foi salvo
            continue
    
    return saved
