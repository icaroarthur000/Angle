import csv
import math
import warnings
from pathlib import Path

import cv2
import numpy as np

from processamento_imagem import contorno
from linha_base import linha_base as lb

OUTPUT_DIR = Path("audit_outputs/window_audit_temp/diagnostico_janelas_centrais")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

IMAGES = [
    ("30_geo", "imagens_teste/30_geo.png"),
    ("50_geo", "imagens_teste/50_geo.png"),
    ("75_geo", "imagens_teste/75_geo.png"),
    ("100_geo", "imagens_teste/100_geo.png"),
    ("130_geo", "imagens_teste/130_geo.png"),
]
SIZES = [7, 9, 11, 13, 15, 17]
SIDES = ["esq", "dir"]


def _as_int(pt):
    return (int(round(float(pt[0]))), int(round(float(pt[1]))))


def _build_centered_window(contour_pts, contact_idx, n):
    if len(contour_pts) == 0:
        return []
    if n <= 0:
        return []
    half = n // 2
    start = (contact_idx - half) % len(contour_pts)
    return [(start + step) % len(contour_pts) for step in range(n)]


def _is_consecutive(indices, n_contour):
    if len(indices) < 2:
        return False
    prev = indices[0]
    for idx in indices[1:]:
        diff = (idx - prev) % n_contour
        if diff != 1:
            return False
        prev = idx
    return True


def _fit_metrics(pts, y_contact):
    if len(pts) < 2:
        return None
    ys = pts[:, 1]
    xs = pts[:, 0]

    with warnings.catch_warnings(record=True) as warns:
        warnings.simplefilter("always")
        coeffs_lin = np.polyfit(ys, xs, 1)
    x_fit_lin = np.polyval(coeffs_lin, ys)
    resid_lin = x_fit_lin - xs
    rmse_lin = float(np.sqrt(np.mean(resid_lin**2)))
    ss_res_lin = float(np.sum(resid_lin**2))
    ss_tot_lin = float(np.sum((xs - np.mean(xs))**2))
    r2_lin = float(1.0 - ss_res_lin / ss_tot_lin) if ss_tot_lin > 0 else float("nan")
    X_lin = np.column_stack([ys, np.ones_like(ys)])
    cond_lin = float(np.linalg.cond(X_lin)) if len(X_lin) >= 2 else float("nan")
    slope_dx_dy = float(coeffs_lin[0])
    dy_dx = float(1.0 / slope_dx_dy) if abs(slope_dx_dy) > 1e-12 else float("nan")
    if np.isfinite(dy_dx):
        theta = float(math.degrees(math.atan2(dy_dx, 1.0)))
    else:
        theta = float("nan")

    with warnings.catch_warnings(record=True) as warns_quad:
        warnings.simplefilter("always")
        coeffs_quad = np.polyfit(ys, xs, 2)
    x_fit_quad = np.polyval(coeffs_quad, ys)
    resid_quad = x_fit_quad - xs
    rmse_quad = float(np.sqrt(np.mean(resid_quad**2)))
    ss_res_quad = float(np.sum(resid_quad**2))
    ss_tot_quad = float(np.sum((xs - np.mean(xs))**2))
    r2_quad = float(1.0 - ss_res_quad / ss_tot_quad) if ss_tot_quad > 0 else float("nan")
    X_quad = np.column_stack([ys**2, ys, np.ones_like(ys)])
    cond_quad = float(np.linalg.cond(X_quad)) if len(X_quad) >= 3 else float("nan")
    a, b, c = coeffs_quad
    dx_dy_quad = float(2.0 * a * y_contact + b)
    dy_dx_quad = float(1.0 / dx_dy_quad) if abs(dx_dy_quad) > 1e-12 else float("nan")
    if np.isfinite(dy_dx_quad):
        theta_quad = float(math.degrees(math.atan2(dy_dx_quad, 1.0)))
    else:
        theta_quad = float("nan")

    return {
        "lin_slope": slope_dx_dy,
        "lin_dy_dx": dy_dx,
        "lin_theta": theta,
        "lin_rmse": rmse_lin,
        "lin_r2": r2_lin,
        "lin_cond": cond_lin,
        "quad_coeffs": coeffs_quad,
        "quad_dx_dy": dx_dy_quad,
        "quad_dy_dx": dy_dx_quad,
        "quad_theta": theta_quad,
        "quad_rmse": rmse_quad,
        "quad_r2": r2_quad,
        "quad_cond": cond_quad,
        "warnings": bool(warns or warns_quad),
    }


def _linear_segment(pts, color, img):
    if len(pts) < 2:
        return
    ys = pts[:, 1]
    xs = pts[:, 0]
    coeffs = np.polyfit(ys, xs, 1)
    y_min, y_max = float(np.min(ys)), float(np.max(ys))
    ys_plot = np.linspace(y_min, y_max, 20)
    xs_plot = np.polyval(coeffs, ys_plot)
    pts_plot = np.column_stack([xs_plot, ys_plot]).astype(np.int32)
    cv2.polylines(img, [pts_plot], False, color, 1, lineType=cv2.LINE_AA)


def _quadratic_segment(pts, color, img):
    if len(pts) < 3:
        return
    ys = pts[:, 1]
    xs = pts[:, 0]
    coeffs = np.polyfit(ys, xs, 2)
    y_min, y_max = float(np.min(ys)), float(np.max(ys))
    ys_plot = np.linspace(y_min, y_max, 30)
    xs_plot = np.polyval(coeffs, ys_plot)
    pts_plot = np.column_stack([xs_plot, ys_plot]).astype(np.int32)
    cv2.polylines(img, [pts_plot], False, color, 1, lineType=cv2.LINE_AA)


def _draw_window(img, contour_pts, idxs, color, radius=2):
    if not idxs:
        return
    for idx in idxs:
        pt = contour_pts[idx]
        cv2.circle(img, _as_int(pt), radius, color, -1, lineType=cv2.LINE_AA)


def analyze_case(name, image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, contour_pts = contorno.extrair_mascara_gota(gray, img_gray=gray)
    if contour_pts is None or len(contour_pts) < 10:
        raise RuntimeError(f"contorno insuficiente para {name}")

    baseline = lb.detectar_baseline_hibrida(contour_pts, debug=False)
    baseline_y = float(baseline["baseline_y"])
    p_esq = baseline["p_esq"]
    p_dir = baseline["p_dir"]
    contact_points = {"esq": p_esq, "dir": p_dir}

    rows = []
    for lado in SIDES:
        contato = contact_points[lado]
        if contato is None:
            continue
        contact_idx = int(np.argmin(np.linalg.norm(contour_pts - np.asarray(contato, dtype=float), axis=1)))
        contact_pt = contour_pts[contact_idx]
        prev = None
        for n in SIZES:
            idxs = _build_centered_window(contour_pts, contact_idx, n)
            pts = contour_pts[idxs]
            metrics = _fit_metrics(pts, float(contact_pt[1]))
            first_pt = contour_pts[idxs[0]]
            last_pt = contour_pts[idxs[-1]]
            max_dist = float(np.max(np.linalg.norm(pts - contact_pt, axis=1)))
            consecutive = _is_consecutive(idxs, len(contour_pts))
            row = {
                "image": name,
                "lado": lado,
                "n": n,
                "idx_start": int(idxs[0]),
                "idx_end": int(idxs[-1]),
                "consecutivo": consecutive,
                "first_xy": f"({first_pt[0]:.2f},{first_pt[1]:.2f})",
                "last_xy": f"({last_pt[0]:.2f},{last_pt[1]:.2f})",
                "max_dist": max_dist,
                "lin_slope": metrics["lin_slope"],
                "lin_theta": metrics["lin_theta"],
                "lin_rmse": metrics["lin_rmse"],
                "lin_r2": metrics["lin_r2"],
                "lin_cond": metrics["lin_cond"],
                "quad_dx_dy": metrics["quad_dx_dy"],
                "quad_dy_dx": metrics["quad_dy_dx"],
                "quad_theta": metrics["quad_theta"],
                "quad_rmse": metrics["quad_rmse"],
                "quad_r2": metrics["quad_r2"],
                "quad_cond": metrics["quad_cond"],
                "warning": metrics["warnings"],
            }
            if prev is not None:
                row["d_theta"] = row["quad_theta"] - prev["quad_theta"]
                row["d_slope"] = row["quad_dx_dy"] - prev["quad_dx_dy"]
            else:
                row["d_theta"] = float("nan")
                row["d_slope"] = float("nan")
            prev = row
            rows.append(row)

    csv_path = OUTPUT_DIR / f"{name}_diagnostico.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        fields = [
            "image", "lado", "n", "idx_start", "idx_end", "consecutivo", "first_xy", "last_xy", "max_dist",
            "lin_slope", "lin_theta", "lin_rmse", "lin_r2", "lin_cond",
            "quad_dx_dy", "quad_dy_dx", "quad_theta", "quad_rmse", "quad_r2", "quad_cond", "warning", "d_theta", "d_slope"
        ]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: ("" if v is None else v) for k, v in row.items()})

    # Visualização por imagem
    vis = img.copy()
    cv2.polylines(vis, [contour_pts.astype(np.int32)], False, (180, 180, 180), 1, lineType=cv2.LINE_AA)
    for lado in SIDES:
        contato = contact_points[lado]
        if contato is None:
            continue
        c_idx = int(np.argmin(np.linalg.norm(contour_pts - np.asarray(contato, dtype=float), axis=1)))
        cv2.circle(vis, _as_int(contour_pts[c_idx]), 7, (0, 255, 0), 2, lineType=cv2.LINE_AA)

    colors = {7: (255, 0, 0), 11: (0, 180, 255), 15: (0, 255, 0), 17: (255, 0, 255)}
    for n in [7, 11, 15, 17]:
        for lado in SIDES:
            contato = contact_points[lado]
            if contato is None:
                continue
            c_idx = int(np.argmin(np.linalg.norm(contour_pts - np.asarray(contato, dtype=float), axis=1)))
            idxs = _build_centered_window(contour_pts, c_idx, n)
            _draw_window(vis, contour_pts, idxs, colors[n], radius=2)
            pts = contour_pts[idxs]
            if len(pts) >= 3:
                _quadratic_segment(pts, colors[n], vis)
                _linear_segment(pts, (255, 255, 255), vis)

    cv2.imwrite(str(OUTPUT_DIR / f"{name}_vis.png"), vis)

for name, path in IMAGES:
    analyze_case(name, path)

print(f"Resultados salvos em {OUTPUT_DIR}")
