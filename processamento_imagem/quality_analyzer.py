"""
quality_analyzer.py
-------------------
Detecta a qualidade de uma imagem em escala de cinza e recomenda
um modo de pré-processamento: HIGH_QUALITY, BALANCED ou ROBUST.

Métricas avaliadas:
  - Contraste  : desvio-padrão normalizado do histograma
  - Ruído      : estimado via laplaciano (variância)
  - Iluminação : uniformidade da intensidade média local
"""

import cv2
import numpy as np
from typing import Dict, Any


# Modos de processamento disponíveis
HIGH_QUALITY = "HIGH_QUALITY"
BALANCED = "BALANCED"
ROBUST = "ROBUST"

# Limiares para classificação
_SCORE_HIGH = 0.65   # score >= 0.65 → HIGH_QUALITY
_SCORE_LOW  = 0.35   # score <  0.35 → ROBUST


def _calc_contrast_score(gray: np.ndarray) -> float:
    """Desvio-padrão normalizado [0,1]. Quanto maior, mais contraste."""
    std = float(np.std(gray.astype(np.float32)))
    # std máximo teórico para imagem bimodal (0/255) ≈ 127.5
    return min(std / 127.5, 1.0)


def _calc_noise_score(gray: np.ndarray) -> float:
    """
    Estima nível de ruído pela variância do laplaciano (normalizada).
    Score alto → imagem nítida (pouco ruído).
    """
    lap_var = float(cv2.Laplacian(gray, cv2.CV_64F).var())
    # lap_var > 500 → imagem muito nítida; < 50 → muito ruidosa/desfocada
    score = min(lap_var / 500.0, 1.0)
    return score


def _calc_illumination_score(gray: np.ndarray) -> float:
    """
    Uniformidade de iluminação: compara intensidade média local com global.
    Score alto → iluminação uniforme.
    """
    h, w = gray.shape[:2]
    k = max(51, (min(h, w) // 6) | 1)
    bg = cv2.GaussianBlur(gray.astype(np.float32), (k, k), 0)
    global_mean = float(gray.mean()) + 1e-6
    local_var = float(np.std(bg / global_mean))
    # local_var próximo de 0 → iluminação uniforme
    score = max(0.0, 1.0 - local_var * 5.0)
    return min(score, 1.0)


def analyze_image_quality(img_bgr: np.ndarray) -> Dict[str, Any]:
    """
    Analisa a qualidade de uma imagem BGR e retorna métricas + modo recomendado.

    Parâmetros
    ----------
    img_bgr : np.ndarray
        Imagem BGR uint8.

    Retorno
    -------
    dict com chaves:
        "score"        : float [0,1] – score global de qualidade
        "contrast"     : float [0,1]
        "sharpness"    : float [0,1]  (inverso de ruído)
        "illumination" : float [0,1]
        "mode"         : str  – HIGH_QUALITY | BALANCED | ROBUST
    """
    if not isinstance(img_bgr, np.ndarray) or img_bgr.ndim < 2:
        return {"score": 0.5, "contrast": 0.5, "sharpness": 0.5,
                "illumination": 0.5, "mode": BALANCED}  # graceful fallback for unsupported input

    if img_bgr.ndim == 3:
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    else:
        gray = img_bgr

    contrast     = _calc_contrast_score(gray)
    sharpness    = _calc_noise_score(gray)
    illumination = _calc_illumination_score(gray)

    # Pesos: contraste tem maior impacto na detecção de gota
    score = 0.45 * contrast + 0.35 * sharpness + 0.20 * illumination

    if score >= _SCORE_HIGH:
        mode = HIGH_QUALITY
    elif score < _SCORE_LOW:
        mode = ROBUST
    else:
        mode = BALANCED

    return {
        "score":        round(score, 4),
        "contrast":     round(contrast, 4),
        "sharpness":    round(sharpness, 4),
        "illumination": round(illumination, 4),
        "mode":         mode,
    }
