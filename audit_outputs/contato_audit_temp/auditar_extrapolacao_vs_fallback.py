import json
import math
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from processamento_imagem import contorno, filtros
from linha_base import linha_base

OUT_ROOT = ROOT / "audit_outputs" / "contato_audit_temp"
JSON_DIR = OUT_ROOT / "extrapolation_vs_fallback"
VIS_DIR = OUT_ROOT / "visualizacoes_extrapolacao_vs_fallback"
JSON_DIR.mkdir(parents=True, exist_ok=True)
VIS_DIR.mkdir(parents=True, exist_ok=True)

IMAGES = [
    ("30_geo", ROOT / "imagens_teste" / "30_geo.png"),
    ("50_geo", ROOT / "imagens_teste" / "50_geo.png"),
    ("75_geo", ROOT / "imagens_teste" / "75_geo.png"),
    ("100_geo", ROOT / "imagens_teste" / "100_geo.png"),
    ("130_geo", ROOT / "imagens_teste" / "130_geo.png"),
]


def _as_int(pt):
    return (int(round(float(pt[0]))), int(round(float(pt[1]))))


def _nearest_idx(points, target):
    if points is None or len(points) == 0:
        return None
    target = np.asarray(target, dtype=float)
    dist = np.linalg.norm(points - target, axis=1)
    return int(np.argmin(dist))


def _classify(dist_extrap_to_contour, dist_returned_to_contour, dx):
    if dist_extrap_to_contour <= 2.0 and abs(dx) <= 2.0:
        return "A"
    if dist_extrap_to_contour <= 6.0 and abs(dx) <= 6.0:
        return "B"
    if dist_extrap_to_contour <= 12.0 and abs(dx) <= 12.0:
        return "C"
    return "D"


def _window_indices(n_points, center_idx, radius=30):
    if n_points <= 0:
        return []
    return [(center_idx + step) % n_points for step in range(-radius, radius + 1)]


def _draw(img, contour_pts, baseline_y, extrap_pt, returned_pt, nearest_idx, window_indices, side, label):
    vis = img.copy()
    cv2.polylines(vis, [contour_pts.astype(np.int32)], False, (180, 180, 180), 1, lineType=cv2.LINE_AA)
    cv2.line(vis, (0, int(round(baseline_y))), (vis.shape[1], int(round(baseline_y))), (0, 255, 255), 2)

    for idx in window_indices:
        pt = contour_pts[idx]
        cv2.circle(vis, _as_int(pt), 1, (0, 165, 255), -1, lineType=cv2.LINE_AA)

    if extrap_pt is not None:
        cv2.circle(vis, _as_int(extrap_pt), 6, (0, 255, 0), 2, lineType=cv2.LINE_AA)
        cv2.putText(vis, "extrap", (_as_int(extrap_pt)[0] + 7, _as_int(extrap_pt)[1] - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)
    if returned_pt is not None:
        cv2.circle(vis, _as_int(returned_pt), 6, (255, 0, 0), 2, lineType=cv2.LINE_AA)
        cv2.putText(vis, "retorno", (_as_int(returned_pt)[0] + 7, _as_int(returned_pt)[1] + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 0, 0), 1)
    if nearest_idx is not None:
        nearest_pt = contour_pts[nearest_idx]
        cv2.circle(vis, _as_int(nearest_pt), 6, (255, 0, 255), 2, lineType=cv2.LINE_AA)
        cv2.putText(vis, f"idx {nearest_idx}", (_as_int(nearest_pt)[0] + 7, _as_int(nearest_pt)[1] - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1)

    cv2.putText(vis, label, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    return vis


for name, path in IMAGES:
    img = cv2.imread(str(path))
    if img is None:
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask, _ = filtros.aplicar_multi_threshold(img)
    _, pts = contorno.extrair_mascara_gota(mask, img_gray=gray)
    if pts is None or len(pts) < 10:
        continue

    res = linha_base.detectar_baseline_hibrida(pts, debug=False)
    baseline_y = float(res.get("baseline_y", 0.0))
    p_esq = res.get("p_esq")
    p_dir = res.get("p_dir")

    y_vals = pts[:, 1]
    y_min, y_max = float(np.min(y_vals)), float(np.max(y_vals))
    height = y_max - y_min
    y_roi_bottom = y_max - 0.02 * height
    y_roi_top = y_min + 0.20 * height
    margem_base = max(6.0, 0.06 * height)
    y_roi_bottom = min(y_roi_bottom, baseline_y - margem_base)
    if y_roi_bottom <= y_roi_top:
        y_roi_bottom = baseline_y - 2.0

    roi_mask = (y_vals >= y_roi_top) & (y_vals <= y_roi_bottom)
    roi_pts = pts[roi_mask]
    x_center = float(np.mean(pts[:, 0]))

    rows = []
    for side_name, side_pts in (("esq", roi_pts[roi_pts[:, 0] < x_center]), ("dir", roi_pts[roi_pts[:, 0] >= x_center])):
        if len(side_pts) < 8:
            continue
        coeffs = np.polyfit(side_pts[:, 1], side_pts[:, 0], 2)
        poly = np.poly1d(coeffs)
        x_contact = float(poly(baseline_y))
        extrap_pt = np.array([x_contact, baseline_y], dtype=float)
        returned_pt = np.array(p_esq if side_name == "esq" else p_dir, dtype=float)

        nearest_idx = _nearest_idx(pts, extrap_pt)
        nearest_pt = pts[nearest_idx] if nearest_idx is not None else None
        dist_extrap_to_contour = float(np.linalg.norm(extrap_pt - nearest_pt)) if nearest_pt is not None else float("nan")
        dist_returned_to_contour = float(np.linalg.norm(returned_pt - nearest_pt)) if nearest_pt is not None else float("nan")
        dx = float(extrap_pt[0] - returned_pt[0])
        classification = _classify(dist_extrap_to_contour, dist_returned_to_contour, dx)

        window_indices = _window_indices(len(pts), nearest_idx, radius=30)
        vis = _draw(img, pts, baseline_y, extrap_pt, returned_pt, nearest_idx, window_indices, side_name, f"{name} {side_name} class={classification}")
        cv2.imwrite(str(VIS_DIR / f"{name}_{side_name}_compare.png"), vis)

        rows.append({
            "image": name,
            "side": side_name,
            "baseline_y": baseline_y,
            "coeffs": [float(c) for c in coeffs],
            "x_contact": x_contact,
            "extrap_pt": [float(extrap_pt[0]), float(extrap_pt[1])],
            "returned_pt": [float(returned_pt[0]), float(returned_pt[1])],
            "nearest_idx": nearest_idx,
            "dist_extrap_to_contour": dist_extrap_to_contour,
            "dist_returned_to_contour": dist_returned_to_contour,
            "dx": dx,
            "classification": classification,
        })

    with (JSON_DIR / f"{name}_compare.json").open("w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2)

report_lines = []
report_lines.append("# Comparação extrapolação x ponto retornado")
report_lines.append("")
for name, _ in IMAGES:
    path = JSON_DIR / f"{name}_compare.json"
    if path.exists():
        with path.open("r", encoding="utf-8") as fh:
            rows = json.load(fh)
        report_lines.append(f"## {name}")
        report_lines.append("")
        for row in rows:
            report_lines.append(
                f"- {row['side']}: coeffs={row['coeffs']} | x_contact={row['x_contact']:.2f} | extrap={row['extrap_pt']} | returned={row['returned_pt']} | nearest_idx={row['nearest_idx']} | dist_extrap={row['dist_extrap_to_contour']:.2f} | dist_returned={row['dist_returned_to_contour']:.2f} | dx={row['dx']:.2f} | cls={row['classification']}"
            )
        report_lines.append("")
(OUT_ROOT / "relatorio_extrapolacao_vs_fallback.md").write_text("\n".join(report_lines), encoding="utf-8")
print(f"Relatório salvo em {OUT_ROOT / 'relatorio_extrapolacao_vs_fallback.md'}")
