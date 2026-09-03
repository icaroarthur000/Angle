import math
import warnings
from pathlib import Path
from typing import List, Tuple

import cv2
import numpy as np

from Cal_angulo import angulo_contato as ac
from linha_base import linha_base as lb
from processamento_imagem import contorno

IMAGE_CASES = [
    ("30_geo", "imagens_teste/30_geo.png"),
    ("50_geo", "imagens_teste/50_geo.png"),
    ("75_geo", "imagens_teste/75_geo.png"),
    ("100_geo", "imagens_teste/100_geo.png"),
    ("130_geo", "imagens_teste/130_geo.png"),
]
WINDOW_SIZES = [7, 9, 11, 13, 15, 17, 21, 25, 31]
DIRECTIONS = ["forward", "backward"]
OUTPUT_DIR = Path("audit_outputs/window_audit_temp")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def _as_int(pt):
    return (int(round(float(pt[0]))), int(round(float(pt[1]))))


def _draw_points(img, pts, color, radius=1, thickness=-1):
    if pts is None or len(pts) == 0:
        return
    for pt in np.asarray(pts, dtype=np.int32):
        cv2.circle(img, (int(pt[0]), int(pt[1])), radius, color, thickness, lineType=cv2.LINE_AA)


def _build_window_indices(contour_pts: np.ndarray, contact_idx: int, n: int, direction: str) -> List[int]:
    if len(contour_pts) == 0:
        return []
    if contact_idx < 0 or contact_idx >= len(contour_pts):
        raise ValueError("contact_idx fora do contorno")
    if n <= 0:
        return []
    if direction not in {"forward", "backward"}:
        raise ValueError("direção inválida")

    indices = []
    if direction == "forward":
        for step in range(n):
            idx = (contact_idx + step) % len(contour_pts)
            indices.append(idx)
    else:
        for step in range(n):
            idx = (contact_idx - step) % len(contour_pts)
            indices.append(idx)
    return indices


def _build_window_indices_centered(contour_pts: np.ndarray, contact_idx: int, n: int, direction: str) -> List[int]:
    if len(contour_pts) == 0:
        return []
    if n <= 0:
        return []
    if direction not in {"forward", "backward"}:
        raise ValueError("direção inválida")
    half = n // 2
    if direction == "forward":
        start = contact_idx - half
        indices = [(start + step) % len(contour_pts) for step in range(n)]
    else:
        start = contact_idx + half
        indices = [(start - step) % len(contour_pts) for step in range(n)]
    return indices


def _polyfit_metrics(window_pts: np.ndarray, contact_pt: np.ndarray):
    if len(window_pts) < 3:
        return None
    ys = window_pts[:, 1]
    xs = window_pts[:, 0]
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        coeffs = np.polyfit(ys, xs, 2)
    a, b, c = coeffs
    y_contact = float(contact_pt[1])
    dx_dy = 2.0 * a * y_contact + b
    dy_dx = None if abs(dx_dy) < 1e-12 else 1.0 / dx_dy
    if dy_dx is None:
        theta_tan = float("nan")
    else:
        vx, vy = ac._normalizar_vetor_tangente(dy_dx)
        theta_tan = math.degrees(math.atan2(vy, vx))

    # Ajuste residuals
    fitted = a * ys**2 + b * ys + c
    residuals = xs - fitted
    rmse = float(np.sqrt(np.mean(residuals**2)))
    ss_res = float(np.sum(residuals**2))
    ss_tot = float(np.sum((xs - np.mean(xs))**2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")

    # Conditioning proxy
    cond = None
    try:
        x = np.vstack([ys**2, ys, np.ones_like(ys)]).T
        cond = float(np.linalg.cond(x))
    except Exception:
        cond = float("nan")

    return {
        "coeffs": coeffs,
        "dx_dy": dx_dy,
        "dy_dx": dy_dx,
        "theta_tan": theta_tan,
        "rmse": rmse,
        "r2": r2,
        "cond": cond,
        "warnings": [str(item.message) for item in w],
    }


def _window_span(contour_pts: np.ndarray, idxs: List[int]):
    if not idxs:
        return None
    return int(min(idxs)), int(max(idxs))


def _max_distance_to_contact(contour_pts: np.ndarray, idxs: List[int], contact_idx: int):
    if not idxs:
        return float("nan")
    contact_pt = contour_pts[contact_idx]
    dists = [np.linalg.norm(contour_pts[idx] - contact_pt) for idx in idxs]
    return float(max(dists))


def _angular_variation(window_pts: np.ndarray):
    if len(window_pts) < 2:
        return float("nan")
    xs = window_pts[:, 0]
    ys = window_pts[:, 1]
    angles = []
    for i in range(1, len(window_pts)):
        dx = xs[i] - xs[i - 1]
        dy = ys[i] - ys[i - 1]
        if abs(dx) < 1e-9 and abs(dy) < 1e-9:
            continue
        angle = math.degrees(math.atan2(dy, dx))
        angles.append(angle)
    if len(angles) < 2:
        return float("nan")
    return float(np.max(angles) - np.min(angles))


def _all_lateral(window_pts: np.ndarray, contact_pt: np.ndarray, baseline_y: float):
    if len(window_pts) == 0:
        return False
    # Heurística simples: todos os pontos devem estar acima da baseline e próximos ao contato
    y_vals = window_pts[:, 1]
    y_contact = float(contact_pt[1])
    return bool(np.all(y_vals <= max(y_contact, baseline_y) + 5.0) and np.all(y_vals >= baseline_y - 40.0))


def audit_case(name: str, image_path: str):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    _, contour_pts = contorno.extrair_mascara_gota(bin_img, img_gray=gray)

    baseline = lb.detectar_baseline_hibrida(contour_pts, debug=False)
    baseline_y = float(baseline["baseline_y"])
    p_esq = baseline["p_esq"]
    p_dir = baseline["p_dir"]

    # localizar contato no contorno real
    def contact_idx_for(pt):
        pt_arr = np.asarray(pt, dtype=float)
        dists = np.linalg.norm(contour_pts - pt_arr, axis=1)
        return int(np.argmin(dists))

    contact_infos = [
        ("esq", p_esq),
        ("dir", p_dir),
    ]

    results = []
    for lado, contato in contact_infos:
        contact_idx = contact_idx_for(contato)
        for n in WINDOW_SIZES:
            for direction in DIRECTIONS:
                # janela centrada em torno do contato
                idxs_centered = _build_window_indices_centered(contour_pts, contact_idx, n, direction)
                # janela não centralizada, a partir do contato em direção escolhida
                idxs_direct = _build_window_indices(contour_pts, contact_idx, n, direction)
                for label, idxs in [("centered", idxs_centered), ("direct", idxs_direct)]:
                    if len(idxs) == 0:
                        continue
                    window_pts = contour_pts[idxs]
                    metrics = _polyfit_metrics(window_pts, contour_pts[contact_idx])
                    if metrics is None:
                        continue
                    results.append({
                        "image": name,
                        "lado": lado,
                        "n": n,
                        "direction": direction,
                        "mode": label,
                        "idx_start": int(idxs[0]),
                        "idx_contact": int(contact_idx),
                        "idx_end": int(idxs[-1]),
                        "n_real": int(len(idxs)),
                        "coeffs": metrics["coeffs"],
                        "dx_dy": metrics["dx_dy"],
                        "dy_dx": metrics["dy_dx"],
                        "theta_tan": metrics["theta_tan"],
                        "rmse": metrics["rmse"],
                        "r2": metrics["r2"],
                        "cond": metrics["cond"],
                        "warning": bool(metrics["warnings"]),
                        "max_dist": _max_distance_to_contact(contour_pts, idxs, contact_idx),
                        "angular_var": _angular_variation(window_pts),
                        "lateral": _all_lateral(window_pts, contour_pts[contact_idx], baseline_y),
                    })

    # salvar tabela CSV resumida
    out_csv = OUTPUT_DIR / f"{name}_window_audit.csv"
    import csv
    with out_csv.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=[
            "image", "lado", "n", "direction", "mode", "idx_start", "idx_contact", "idx_end", "n_real",
            "dx_dy", "dy_dx", "theta_tan", "rmse", "r2", "cond", "warning", "max_dist", "angular_var", "lateral"
        ])
        writer.writeheader()
        for row in results:
            clean_row = {}
            for k, v in row.items():
                if k == "coeffs":
                    continue
                if isinstance(v, list):
                    clean_row[k] = ";".join(map(str, v))
                elif isinstance(v, np.ndarray):
                    clean_row[k] = ",".join(map(str, v.tolist()))
                else:
                    clean_row[k] = v
            writer.writerow(clean_row)

    # salvar visualização
    vis = img.copy()
    h, w = vis.shape[:2]
    if len(contour_pts) >= 2:
        cv2.polylines(vis, [contour_pts.astype(np.int32)], False, (160, 160, 160), 1, lineType=cv2.LINE_AA)
    cv2.circle(vis, _as_int(contour_pts[contact_idx_for(p_esq)]), 6, (0, 255, 0), 2, lineType=cv2.LINE_AA)
    cv2.circle(vis, _as_int(contour_pts[contact_idx_for(p_dir)]), 6, (0, 255, 0), 2, lineType=cv2.LINE_AA)

    # escolher alguns tamanhos para desenhar
    selected_sizes = [7, 11, 17, 25, 31]
    colors = [(255, 0, 0), (0, 180, 255), (0, 255, 0), (255, 0, 255), (0, 0, 255)]
    for (lado, contato), color, n in zip(contact_infos, [(255, 0, 0), (0, 0, 255)], [0, 0]):
        pass

    # desenhar para os dois lados e os tamanhos escolhidos
    for idx, (lado, contato) in enumerate(contact_infos):
        color = (255, 0, 0) if lado == "esq" else (0, 0, 255)
        contact_idx = contact_idx_for(contato)
        for size, c in zip(selected_sizes, [(255, 0, 0), (0, 180, 255), (0, 255, 0), (255, 0, 255), (0, 0, 255)]):
            idxs = _build_window_indices_centered(contour_pts, contact_idx, size, "forward")
            window_pts = contour_pts[idxs]
            if len(window_pts) >= 3:
                # desenhar a janela
                for pt in window_pts:
                    cv2.circle(vis, _as_int(pt), 1, c, -1, lineType=cv2.LINE_AA)
                # desenhar curva do polyfit
                ys = window_pts[:, 1]
                xs = window_pts[:, 0]
                coeffs = np.polyfit(ys, xs, 2)
                a, b, c_poly = coeffs
                y_min, y_max = int(np.min(ys)), int(np.max(ys))
                ys_plot = np.linspace(y_min, y_max, 50)
                xs_plot = a * ys_plot**2 + b * ys_plot + c_poly
                pts_plot = np.column_stack([xs_plot, ys_plot]).astype(np.int32)
                cv2.polylines(vis, [pts_plot], False, c, 1, lineType=cv2.LINE_AA)
        cv2.circle(vis, _as_int(contour_pts[contact_idx]), 5, color, 2, lineType=cv2.LINE_AA)

    out_img = OUTPUT_DIR / f"{name}_window_audit.png"
    cv2.imwrite(str(out_img), vis)


for name, path in IMAGE_CASES:
    audit_case(name, path)

print(f"Saved temporary audit files to {OUTPUT_DIR}")
