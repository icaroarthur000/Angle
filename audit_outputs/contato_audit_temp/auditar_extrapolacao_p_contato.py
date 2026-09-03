import json
import math
import sys
import warnings
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from processamento_imagem import contorno, filtros
from linha_base import linha_base

OUT_ROOT = ROOT / "audit_outputs" / "contato_audit_temp"
JSON_DIR = OUT_ROOT / "extrapolation_audit"
VIS_DIR = OUT_ROOT / "visualizacoes_extrapolacao"
JSON_DIR.mkdir(parents=True, exist_ok=True)
VIS_DIR.mkdir(parents=True, exist_ok=True)

IMAGES = [
    ("30_geo", ROOT / "imagens_teste" / "30_geo.png"),
    ("50_geo", ROOT / "imagens_teste" / "50_geo.png"),
    ("75_geo", ROOT / "imagens_teste" / "75_geo.png"),
    ("100_geo", ROOT / "imagens_teste" / "100_geo.png"),
    ("130_geo", ROOT / "imagens_teste" / "130_geo.png"),
]

ROI_BOTTOM_EXCLUDE = 0.02
ROI_TOP_EXCLUDE = 0.20
POLYFIT_DEGREE = 2
MIN_POINTS_FOR_FIT = 8


def _as_int(pt):
    return (int(round(float(pt[0]))), int(round(float(pt[1]))))


def _nearest_idx(points, target):
    if points is None or len(points) == 0:
        return None
    target = np.asarray(target, dtype=float)
    dist = np.linalg.norm(points - target, axis=1)
    return int(np.argmin(dist))


def _baseline_contact_candidate(pts, side_name, baseline_y, x_center):
    if pts is None or len(pts) == 0:
        return None, None
    if side_name == "esq":
        side_mask = pts[:, 0] <= x_center
    else:
        side_mask = pts[:, 0] >= x_center
    side_pts = pts[side_mask]
    if len(side_pts) == 0:
        return None, None
    idx = int(np.argmin(np.abs(side_pts[:, 1] - baseline_y)))
    candidate_pt = side_pts[idx]
    return candidate_pt, idx


def _fit_and_extrapolate(gota_pts, baseline_y):
    y_vals = gota_pts[:, 1]
    y_min, y_max = float(np.min(y_vals)), float(np.max(y_vals))
    height = y_max - y_min

    y_roi_bottom = y_max - ROI_BOTTOM_EXCLUDE * height
    y_roi_top = y_min + ROI_TOP_EXCLUDE * height
    margem_base = max(6.0, 0.06 * height)
    y_roi_bottom = min(y_roi_bottom, float(baseline_y) - margem_base)

    if y_roi_bottom <= y_roi_top:
        y_roi_bottom = float(baseline_y) - 2.0

    roi_mask = (y_vals >= y_roi_top) & (y_vals <= y_roi_bottom)
    roi_pts = gota_pts[roi_mask]
    x_center = float(np.mean(gota_pts[:, 0]))
    result = []

    for side_name, side_pts in (("esq", roi_pts[roi_pts[:, 0] < x_center]), ("dir", roi_pts[roi_pts[:, 0] >= x_center])):
        if len(side_pts) < MIN_POINTS_FOR_FIT:
            result.append({
                "side": side_name,
                "used_points": [],
                "coeffs": None,
                "x_contact": None,
                "reason": "pontos_insuficientes_na_roi",
            })
            continue

        with warnings.catch_warnings(record=True) as warns:
            warnings.simplefilter("always")
            coeffs = np.polyfit(side_pts[:, 1], side_pts[:, 0], POLYFIT_DEGREE)
        poly = np.poly1d(coeffs)
        x_contact = float(poly(baseline_y))
        used_points = []
        for idx, point in enumerate(side_pts):
            used_points.append({
                "index": int(idx),
                "x": float(point[0]),
                "y": float(point[1]),
            })

        result.append({
            "side": side_name,
            "used_points": used_points,
            "coeffs": [float(c) for c in coeffs],
            "x_contact": x_contact,
            "y_eval": float(baseline_y),
            "warning": bool(warns),
            "roi_top": float(y_roi_top),
            "roi_bottom": float(y_roi_bottom),
            "x_center": x_center,
        })

    return {
        "roi_top": float(y_roi_top),
        "roi_bottom": float(y_roi_bottom),
        "x_center": x_center,
        "side_results": result,
    }


def _draw_audit(img, contour_pts, baseline_y, side_result, calc_pt, nearest_idx, nearest_pt, baseline_contact_idx, baseline_contact_pt):
    vis = img.copy()
    cv2.polylines(vis, [contour_pts.astype(np.int32)], False, (180, 180, 180), 1, lineType=cv2.LINE_AA)
    cv2.line(vis, (0, int(round(baseline_y))), (vis.shape[1], int(round(baseline_y))), (0, 255, 255), 2)

    for point in side_result["used_points"]:
        pt = contour_pts[int(point["index"])] if int(point["index"]) < len(contour_pts) else None
        if pt is None:
            continue
        cv2.circle(vis, _as_int(pt), 2, (0, 165, 255), -1, lineType=cv2.LINE_AA)

    if calc_pt is not None:
        cv2.circle(vis, _as_int(calc_pt), 6, (0, 255, 0), 2, lineType=cv2.LINE_AA)
        cv2.putText(vis, f"p_{side_result['side']}", (_as_int(calc_pt)[0] + 7, _as_int(calc_pt)[1] - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)

    if nearest_idx is not None and nearest_pt is not None:
        cv2.circle(vis, _as_int(nearest_pt), 6, (255, 0, 255), 2, lineType=cv2.LINE_AA)
        cv2.putText(vis, f"idx {nearest_idx}", (_as_int(nearest_pt)[0] + 7, _as_int(nearest_pt)[1] - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1)

    if baseline_contact_pt is not None:
        cv2.circle(vis, _as_int(baseline_contact_pt), 6, (255, 255, 0), 2, lineType=cv2.LINE_AA)
        cv2.putText(vis, "baseline-contact", (_as_int(baseline_contact_pt)[0] + 7, _as_int(baseline_contact_pt)[1] + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)

    coeffs = side_result.get("coeffs")
    if coeffs:
        label = f"x = {coeffs[0]:.4f}y^2 + {coeffs[1]:.4f}y + {coeffs[2]:.4f}"
        cv2.putText(vis, label, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        cv2.putText(vis, f"baseline_y = {baseline_y:.1f}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        cv2.putText(vis, f"x_contact = {side_result['x_contact']:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)

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

    audit = _fit_and_extrapolate(pts, baseline_y)
    x_center = audit["x_center"]

    per_side = []
    for side_result in audit["side_results"]:
        side_name = side_result["side"]
        p_calc = [float(side_result["x_contact"]), baseline_y] if side_result["x_contact"] is not None else None
        calc_pt = np.asarray(p_calc, dtype=float) if p_calc is not None else None

        if calc_pt is not None:
            nearest_idx = _nearest_idx(pts, calc_pt)
            nearest_pt = pts[nearest_idx] if nearest_idx is not None else None
            baseline_contact_pt, baseline_contact_idx = _baseline_contact_candidate(pts, side_name, baseline_y, x_center)
            dist_to_contour = float(np.linalg.norm(calc_pt - nearest_pt)) if nearest_pt is not None else float("nan")
            dist_to_baseline = float(abs(calc_pt[1] - baseline_y))
            dist_to_baseline_contact = float(np.linalg.norm(calc_pt - baseline_contact_pt)) if baseline_contact_pt is not None else float("nan")
        else:
            nearest_idx = None
            nearest_pt = None
            baseline_contact_pt = None
            baseline_contact_idx = None
            dist_to_contour = float("nan")
            dist_to_baseline = float("nan")
            dist_to_baseline_contact = float("nan")

        vis = _draw_audit(img, pts, baseline_y, side_result, calc_pt, nearest_idx, nearest_pt, baseline_contact_idx, baseline_contact_pt)
        cv2.imwrite(str(VIS_DIR / f"{name}_{side_name}_extrapolation.png"), vis)

        per_side.append({
            "image": name,
            "side": side_name,
            "baseline_y": baseline_y,
            "p_calc": [float(calc_pt[0]), float(calc_pt[1])] if calc_pt is not None else None,
            "p_production": [float(p_esq[0]), float(p_esq[1])] if side_name == "esq" and p_esq is not None else ([float(p_dir[0]), float(p_dir[1])] if side_name == "dir" and p_dir is not None else None),
            "coeffs": side_result.get("coeffs"),
            "roi_top": side_result.get("roi_top"),
            "roi_bottom": side_result.get("roi_bottom"),
            "x_center": x_center,
            "used_points_count": len(side_result.get("used_points", [])),
            "used_points": side_result.get("used_points", []),
            "nearest_idx": nearest_idx,
            "nearest_pt": [float(nearest_pt[0]), float(nearest_pt[1])] if nearest_pt is not None else None,
            "dist_to_contour": dist_to_contour,
            "dist_to_baseline": dist_to_baseline,
            "dist_to_baseline_contact": dist_to_baseline_contact,
            "warning": side_result.get("warning"),
        })

    with (JSON_DIR / f"{name}_extrapolation.json").open("w", encoding="utf-8") as fh:
        json.dump(per_side, fh, indent=2)

    print(f"[{name}] salvo JSON e visualizações")

report_lines = []
report_lines.append("# Relatório de auditoria da extrapolação de p_esq/p_dir")
report_lines.append("")
report_lines.append("Este relatório usa o fluxo atual de produção sem alterar a implementação.")
report_lines.append("")

for name, _ in IMAGES:
    json_path = JSON_DIR / f"{name}_extrapolation.json"
    if not json_path.exists():
        continue
    with json_path.open("r", encoding="utf-8") as fh:
        rows = json.load(fh)
    report_lines.append(f"## {name}")
    report_lines.append("")
    for row in rows:
        report_lines.append(f"- {row['side']}: coeffs={row['coeffs']} | p_calc={row['p_calc']} | p_production={row['p_production']} | dist_to_contour={row['dist_to_contour']:.2f} | dist_to_baseline={row['dist_to_baseline']:.2f} | dist_to_baseline_contact={row['dist_to_baseline_contact']:.2f}")
    report_lines.append("")

(OUT_ROOT / "relatorio_extrapolacao.md").write_text("\n".join(report_lines), encoding="utf-8")
print(f"Relatório salvo em {OUT_ROOT / 'relatorio_extrapolacao.md'}")
