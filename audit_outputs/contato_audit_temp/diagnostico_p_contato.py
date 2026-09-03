import json
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from processamento_imagem import contorno, filtros
from linha_base import linha_base

OUTPUT_DIR = ROOT / "audit_outputs" / "contato_audit_temp"
VIS_DIR = OUTPUT_DIR / "visualizacoes"
VIS_DIR.mkdir(parents=True, exist_ok=True)

IMAGES = [
    ("30_geo", ROOT / "imagens_teste" / "30_geo.png"),
    ("50_geo", ROOT / "imagens_teste" / "50_geo.png"),
    ("75_geo", ROOT / "imagens_teste" / "75_geo.png"),
    ("100_geo", ROOT / "imagens_teste" / "100_geo.png"),
    ("130_geo", ROOT / "imagens_teste" / "130_geo.png"),
]
WINDOW_RADIUS = 20


def _as_int(pt):
    return (int(round(float(pt[0]))), int(round(float(pt[1]))))


def _nearest_idx(points, target):
    if points is None or len(points) == 0:
        return None
    target = np.asarray(target, dtype=float)
    dist = np.linalg.norm(points - target, axis=1)
    return int(np.argmin(dist))


def _window_indices(n_points, center_idx, radius):
    if n_points <= 0:
        return []
    half = max(1, radius)
    return [(center_idx + step) % n_points for step in range(-half, half + 1)]


def _classify_case(dist_to_contour, dist_to_baseline, local_span, baseline_y, y_contact):
    if dist_to_contour <= 2.0 and abs(dist_to_baseline) <= 2.0:
        return "A"
    if dist_to_contour <= 5.0 and abs(dist_to_baseline) <= 4.0:
        return "B"
    if dist_to_contour <= 10.0 and abs(dist_to_baseline) <= 8.0:
        return "C"
    return "D"


def _draw_case(img, contour_pts, baseline_y, p_contact, side, nearest_idx, window_indices, dist_to_contour, dist_to_baseline):
    vis = img.copy()
    cv2.polylines(vis, [contour_pts.astype(np.int32)], False, (180, 180, 180), 1, lineType=cv2.LINE_AA)
    cv2.line(vis, (0, int(round(baseline_y))), (vis.shape[1], int(round(baseline_y))), (0, 255, 255), 1)

    if p_contact is not None:
        cv2.circle(vis, _as_int(p_contact), 6, (0, 255, 0), 2, lineType=cv2.LINE_AA)
        cv2.putText(vis, f"p_{side}", _as_int(p_contact), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    if nearest_idx is not None:
        nearest_pt = contour_pts[nearest_idx]
        cv2.circle(vis, _as_int(nearest_pt), 6, (255, 0, 255), 2, lineType=cv2.LINE_AA)
        cv2.putText(vis, f"idx {nearest_idx}", (_as_int(nearest_pt)[0] + 7, _as_int(nearest_pt)[1] - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1)

    if window_indices:
        for idx in window_indices:
            pt = contour_pts[idx]
            cv2.circle(vis, _as_int(pt), 2, (0, 165, 255), -1, lineType=cv2.LINE_AA)

    cv2.putText(vis, f"dist_contour={dist_to_contour:.2f}px", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(vis, f"dist_baseline={dist_to_baseline:.2f}px", (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    return vis


for name, path in IMAGES:
    img = cv2.imread(str(path))
    if img is None:
        print(f"[WARN] imagem não encontrada: {path}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask, _ = filtros.aplicar_multi_threshold(img)
    _, pts = contorno.extrair_mascara_gota(mask, img_gray=gray)
    if pts is None or len(pts) < 10:
        print(f"[WARN] contorno insuficiente para {name}")
        continue

    res = linha_base.detectar_baseline_hibrida(pts, debug=False)
    baseline_y = float(res.get("baseline_y", 0.0))
    p_esq = res.get("p_esq")
    p_dir = res.get("p_dir")

    results = []
    for side, p_contact in (("esq", p_esq), ("dir", p_dir)):
        if p_contact is None:
            continue

        contact_pt = np.asarray(p_contact, dtype=float)
        nearest_idx = _nearest_idx(pts, contact_pt)
        nearest_pt = pts[nearest_idx] if nearest_idx is not None else None

        if nearest_idx is None:
            dist_to_contour = float("nan")
            dist_to_baseline = float("nan")
            classification = "D"
            window_indices = []
        else:
            dist_to_contour = float(np.linalg.norm(contact_pt - nearest_pt))
            dist_to_baseline = float(abs(float(nearest_pt[1]) - baseline_y))
            window_indices = _window_indices(len(pts), nearest_idx, WINDOW_RADIUS)
            classification = _classify_case(dist_to_contour, dist_to_baseline, len(window_indices), baseline_y, float(contact_pt[1]))

        vis = _draw_case(img, pts, baseline_y, contact_pt, side, nearest_idx, window_indices, dist_to_contour, dist_to_baseline)
        out_path = VIS_DIR / f"{name}_{side}_contato_context.png"
        cv2.imwrite(str(out_path), vis)

        results.append({
            "image": name,
            "side": side,
            "baseline_y": baseline_y,
            "p_contact": [float(contact_pt[0]), float(contact_pt[1])],
            "nearest_idx": nearest_idx,
            "nearest_pt": [float(nearest_pt[0]), float(nearest_pt[1])] if nearest_pt is not None else None,
            "dist_to_contour": dist_to_contour,
            "dist_to_baseline": dist_to_baseline,
            "classification": classification,
            "window_indices": window_indices,
        })

    summary_path = OUTPUT_DIR / f"{name}_summary.json"
    with summary_path.open("w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)

    print(f"[{name}] salvo: {summary_path}")

print(f"Resultados salvos em {OUTPUT_DIR}")
