import json
from pathlib import Path
from typing import Any, Dict

# =================================================================
# MÓDULO: parametros.py
# Gerencia config.json em runtime: leitura, escrita e cache em memória.
# obter(nome, fallback): ponto de acesso único usado por todos os módulos.
# =================================================================

CONFIG_PATH = Path(__file__).resolve().parent / "config.json"

DEFAULTS: Dict[str, Any] = {
    "baseline_bottom_fraction": 0.10,
    "baseline_inlier_min_pixels": 2.0,
    "baseline_inlier_mad_scale": 2.5,
    "baseline_refine_iterations": 2,
    "roi_bottom_exclude": 0.02,
    "roi_top_exclude": 0.20,
    "polyfit_degree": 2,
    "min_points_for_fit": 8,
    "angle_baseline_offset_factor": 0.01,
    "angle_baseline_offset_min": 1.5,
    "angle_baseline_offset_max": 4.0,
    "angle_window_height_factor": 0.55,
    "angle_window_height_min": 70,
    "angle_window_height_max": 220,
    "angle_outlier_sigma_scale": 2.0,
    "quality_rmse_ref_px": 3.0,
    "quality_min_score": 0.0,
    "quality_max_score": 1.0,
    "test_angle_tolerance_deg": 1.0
}

_CACHE: Dict[str, Any] | None = None


def carregar_parametros(force_reload: bool = False) -> Dict[str, Any]:
    global _CACHE
    if _CACHE is not None and not force_reload:
        return _CACHE

    data: Dict[str, Any] = dict(DEFAULTS)
    if CONFIG_PATH.exists():
        try:
            raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                data.update(raw)
        except Exception:
            pass

    _CACHE = data
    return data


def salvar_parametros(parametros: Dict[str, Any]) -> None:
    merged = dict(DEFAULTS)
    merged.update(parametros or {})
    CONFIG_PATH.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
    global _CACHE
    _CACHE = merged


def obter(nome: str, fallback: Any = None) -> Any:
    params = carregar_parametros()
    if nome in params:
        return params[nome]
    return fallback


def atualizar_runtime(updates: Dict[str, Any]) -> Dict[str, Any]:
    params = carregar_parametros().copy()
    params.update(updates or {})
    global _CACHE
    _CACHE = params
    return params
