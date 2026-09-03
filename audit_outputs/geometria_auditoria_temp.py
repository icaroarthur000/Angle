import csv
import math
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Cal_angulo import angulo_contato
from linha_base import linha_base
from processamento_imagem import contorno, filtros

IMG_DIR = ROOT / "imagens_teste"
OUT_DIR = ROOT / "audit_outputs" / "auditoria_geometrica"
VIS_DIR = OUT_DIR / "visualizacoes"
REPORT_PATH = OUT_DIR / "relatorio_geometrico.md"
TABLE_PATH = OUT_DIR / "tabela_geometrica.csv"

IMAGES = ["30_geo.png", "50_geo.png", "75_geo.png", "100_geo.png", "130_geo.png"]
SIDES = ["esq", "dir"]


def fnum(value, nd=6):
    if value is None:
        return "N/A"
    try:
        value = float(value)
    except Exception:
        return str(value)
    if math.isnan(value) or math.isinf(value):
        return "N/A"
    return f"{value:.{nd}f}"


def find_index(contour_pts: np.ndarray, point: np.ndarray) -> Optional[int]:
    if contour_pts is None or len(contour_pts) == 0:
        return None
    point = np.asarray(point, dtype=float).reshape(1, 2)
    matches = np.where(np.all(np.isclose(contour_pts, point[0], atol=1e-6), axis=1))[0]
    if len(matches) == 0:
        return None
    return int(matches[0])


def build_contiguity_summary(indices: List[int], total_points: int) -> Tuple[bool, bool, List[Tuple[int, int]]]:
    if not indices:
        return False, False, []
    sorted_idx = sorted(int(i) for i in indices)
    if len(sorted_idx) <= 1:
        return True, False, []
    gaps = []
    jumps = []
    for a, b in zip(sorted_idx[:-1], sorted_idx[1:]):
        gap = b - a
        if gap > 1:
            jumps.append((a, b))
            gaps.append(gap)
    wrap_around = False
    if len(sorted_idx) >= 2 and sorted_idx[0] == 0 and sorted_idx[-1] == total_points - 1:
        wrap_around = True
    contiguous = len(jumps) == 0 and not wrap_around
    return contiguous, wrap_around, jumps


def load_pipeline(image_name: str) -> Dict[str, object]:
    image_path = IMG_DIR / image_name
    image = cv2.imread(str(image_path))
    if image is None:
        raise RuntimeError(f"Não foi possível ler {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask, mask_method = filtros.aplicar_multi_threshold(image)
    mask_gota, pts = contorno.extrair_mascara_gota(mask, img_gray=gray)
    if pts is None or len(pts) < 3:
        pts = contorno.encontrar_contorno_gota_robusto(mask_gota)
    if pts is None or len(pts) < 3:
        raise RuntimeError("Contorno não detectado")
    baseline = linha_base.detectar_baseline_hibrida(np.asarray(pts, dtype=float), debug=False)
    baseline_y = float(baseline["baseline_y"])
    p_esq = baseline.get("p_esq")
    p_dir = baseline.get("p_dir")
    if p_esq is None or p_dir is None:
        pe, pd = linha_base.encontrar_pontos_contato(np.asarray(pts, dtype=float), baseline_y)
        if p_esq is None and pe is not None:
            p_esq = [float(pe[0]), float(pe[1])]
        if p_dir is None and pd is not None:
            p_dir = [float(pd[0]), float(pd[1])]
    return {
        "image": image,
        "image_name": image_name,
        "pts": np.asarray(pts, dtype=float),
        "baseline_y": baseline_y,
        "mask_method": mask_method,
        "p_esq": p_esq,
        "p_dir": p_dir,
    }


def analyze_side(contour_pts: np.ndarray, p_esq, p_dir, baseline_y: float, lado: str) -> Dict[str, object]:
    contato = p_esq if lado == "esq" else p_dir
    altura_gota = float(np.max(contour_pts[:, 1]) - np.min(contour_pts[:, 1])) if len(contour_pts) > 0 else 0.0
    offset = float(np.clip(angulo_contato.ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, angulo_contato.ANGLE_BASELINE_OFFSET_MIN, angulo_contato.ANGLE_BASELINE_OFFSET_MAX))
    baseline_ajustada = baseline_y + offset
    selected_points = angulo_contato._selecionar_pontos_lado(contour_pts, p_esq, p_dir, baseline_ajustada, lado)
    selected_points = np.asarray(selected_points, dtype=float)

    selected_indices = []
    for pt in selected_points:
        idx = find_index(contour_pts, pt)
        if idx is not None:
            selected_indices.append(int(idx))

    if len(selected_points) >= 2:
        contact_x = float(contato[0])
        contact_y = float(contato[1])
        dists = np.hypot(selected_points[:, 0] - contact_x, selected_points[:, 1] - contact_y)
        avg_dist = float(np.mean(dists)) if len(dists) else None
        max_dist = float(np.max(dists)) if len(dists) else None
    else:
        avg_dist = None
        max_dist = None

    # Use the current tangent slope path as-is.
    slope_result = angulo_contato._calcular_slope_tangente_polynomial(selected_points, baseline_y, lado, contato, contour_pts)
    method = "polyfit"
    slope = None
    coeffs = None
    angle_deg = None
    if slope_result is not None:
        slope, coeffs, pts_used = slope_result
        slope = float(slope)
        coeffs = [float(v) for v in coeffs]
        if math.isfinite(slope):
            angle_deg = float(abs(math.degrees(math.atan(slope))))
        else:
            angle_deg = 90.0
    else:
        # Try the current circular path only as a diagnostic fallback; do not invent a new rule.
        angle_val = angulo_contato.calcular_angulo_circular(contour_pts, p_esq, p_dir, baseline_y, lado)
        if angle_val is not None and math.isfinite(float(angle_val)):
            method = "círculo"
            angle_deg = float(angle_val)
            slope = math.tan(math.radians(angle_deg)) if angle_deg is not None else None
        else:
            method = "fallback"
            slope = None
            angle_deg = None

    first_point = selected_points[0] if len(selected_points) > 0 else None
    last_point = selected_points[-1] if len(selected_points) > 0 else None
    first_idx = int(selected_indices[0]) if len(selected_indices) > 0 else None
    last_idx = int(selected_indices[-1]) if len(selected_indices) > 0 else None
    contig, wrap, jumps = build_contiguity_summary(selected_indices, len(contour_pts))
    y_min = float(np.min(selected_points[:, 1])) if len(selected_points) > 0 else None
    y_max = float(np.max(selected_points[:, 1])) if len(selected_points) > 0 else None
    vertical_distance = float(abs(baseline_y - y_max)) if baseline_y is not None and y_max is not None else None

    return {
        "contact": [float(contato[0]), float(contato[1])],
        "contact_index": find_index(contour_pts, contato),
        "first_point": [float(first_point[0]), float(first_point[1])] if first_point is not None else None,
        "last_point": [float(last_point[0]), float(last_point[1])] if last_point is not None else None,
        "first_index": first_idx,
        "last_index": last_idx,
        "selected_count": int(len(selected_points)),
        "y_min": y_min,
        "y_max": y_max,
        "y_range": [y_min, y_max],
        "baseline_ajustada": baseline_ajustada,
        "distance_to_baseline": vertical_distance,
        "slope": slope,
        "angle_deg": angle_deg,
        "method": method,
        "contiguous": contig,
        "wrap_around": wrap,
        "jumps": jumps,
        "avg_dist_to_contact": avg_dist,
        "max_dist_to_contact": max_dist,
        "selected_indices": selected_indices,
        "selected_points": selected_points,
    }


def draw_tangent_line(canvas, contact, slope, color):
    if contact is None:
        return
    cx, cy = int(round(contact[0])), int(round(contact[1]))
    if slope is None or not math.isfinite(float(slope)):
        return
    length = 80.0
    if abs(slope) < 1e-8:
        dx, dy = length, 0.0
    else:
        dx = length / math.sqrt(1.0 + slope * slope)
        dy = slope * dx
    p1 = (cx, cy)
    p2 = (int(round(cx + dx)), int(round(cy + dy)))
    p3 = (int(round(cx - dx)), int(round(cy - dy)))
    cv2.line(canvas, p1, p2, color, 2)
    cv2.line(canvas, p1, p3, color, 1)


def render_image(base_image, contour_pts, baseline_y, p_esq, p_dir, left_info, right_info):
    canvas = base_image.copy()
    if len(contour_pts) >= 3:
        cv2.polylines(canvas, [np.asarray(contour_pts, dtype=np.int32)], isClosed=True, color=(200, 200, 200), thickness=1)
    h, w = canvas.shape[:2]
    cv2.line(canvas, (0, int(round(baseline_y))), (w - 1, int(round(baseline_y))), (0, 255, 255), 2)

    def draw_contact(contact, color):
        if contact is None:
            return
        x, y = int(round(contact[0])), int(round(contact[1]))
        cv2.circle(canvas, (x, y), 6, color, -1)
        cv2.circle(canvas, (x, y), 3, (255, 255, 255), 2)

    def draw_selected(points, color):
        for x, y in points:
            cv2.circle(canvas, (int(round(x)), int(round(y))), 2, color, -1)

    draw_contact(p_esq, (0, 255, 0))
    draw_contact(p_dir, (255, 0, 0))
    draw_selected(left_info["selected_points"], (0, 140, 255))
    draw_selected(right_info["selected_points"], (255, 140, 0))

    if left_info["slope"] is not None and math.isfinite(float(left_info["slope"])):
        draw_tangent_line(canvas, left_info["contact"], left_info["slope"], (0, 255, 255))
    if right_info["slope"] is not None and math.isfinite(float(right_info["slope"])):
        draw_tangent_line(canvas, right_info["contact"], right_info["slope"], (255, 255, 0))

    return canvas


def write_report(items: List[Dict[str, object]]):
    lines = []
    lines.append("# Auditoria geométrica do pipeline atual")
    lines.append("")
    lines.append("Objetivo: verificar se os pontos usados para cada tangente estão próximos do ponto de contato e formam uma sequência física contínua no contorno.")
    lines.append("")
    for item in items:
        lines.append(f"## {item['image_name']}")
        lines.append("")
        lines.append(f"- Baseline: {fnum(item['baseline_y'])}")
        lines.append(f"- Método de máscara: {item['mask_method']}")
        lines.append(f"- Pontos do contorno: {len(item['pts'])}")
        lines.append("")
        for lado in SIDES:
            info = item[f"{lado}_audit"]
            lines.append(f"### Lado {lado}")
            lines.append("")
            lines.append(f"- Ponto de contato usado: {info['contact']}")
            lines.append(f"- Índice do ponto de contato no contorno: {info['contact_index']}")
            lines.append(f"- Primeiros pontos selecionados: {info['first_point']}")
            lines.append(f"- Últimos pontos selecionados: {info['last_point']}")
            lines.append(f"- Índices primeiro/último: {info['first_index']} / {info['last_index']}")
            lines.append(f"- Quantidade total selecionada: {info['selected_count']}")
            lines.append(f"- Faixa de y usada: [{fnum(info['y_min'])}, {fnum(info['y_max'])}]")
            lines.append(f"- Distância vertical até a baseline: {fnum(info['distance_to_baseline'])}")
            lines.append(f"- Inclinação da tangente: {fnum(info['slope'])}")
            lines.append(f"- Ângulo da tangente em relação à horizontal: {fnum(info['angle_deg'])}")
            lines.append(f"- Método efetivamente usado: {info['method']}")
            lines.append(f"- Sequência contínua no contorno: {'sim' if info['contiguous'] else 'não'}")
            lines.append(f"- Wrap-around: {'sim' if info['wrap_around'] else 'não'}")
            lines.append(f"- Saltos entre índices: {info['jumps']}")
            lines.append(f"- Distância média ao contato: {fnum(info['avg_dist_to_contact'])}")
            lines.append(f"- Distância máxima ao contato: {fnum(info['max_dist_to_contact'])}")
            lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_table(items: List[Dict[str, object]]):
    header = ["imagem", "lado", "contato", "índice contato", "nº pontos", "índices inicial-final", "contíguo?", "y_min-y_max", "método", "fallback?", "slope", "ângulo tangente"]
    rows = []
    for item in items:
        for lado in SIDES:
            info = item[f"{lado}_audit"]
            rows.append([
                item["image_name"],
                lado,
                f"[{fnum(info['contact'][0])}, {fnum(info['contact'][1])}]",
                info["contact_index"],
                info["selected_count"],
                f"{info['first_index']} -> {info['last_index']}",
                "sim" if info["contiguous"] else "não",
                f"[{fnum(info['y_min'])}, {fnum(info['y_max'])}]",
                info["method"],
                "sim" if info["method"] == "fallback" else "não",
                fnum(info["slope"]),
                fnum(info["angle_deg"]),
            ])
    with TABLE_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    items = []
    for image_name in IMAGES:
        data = load_pipeline(image_name)
        left = analyze_side(data["pts"], data["p_esq"], data["p_dir"], data["baseline_y"], "esq")
        right = analyze_side(data["pts"], data["p_esq"], data["p_dir"], data["baseline_y"], "dir")
        data["esq_audit"] = left
        data["dir_audit"] = right
        image_vis = render_image(data["image"], data["pts"], data["baseline_y"], data["p_esq"], data["p_dir"], left, right)
        out_path = VIS_DIR / f"{image_name.replace('.png', '')}_audit.png"
        cv2.imwrite(str(out_path), image_vis)
        items.append(data)
    write_report(items)
    write_table(items)
    print(f"Relatório geométrico salvo em: {REPORT_PATH}")
    print(f"Tabela CSV salva em: {TABLE_PATH}")
    print(f"Imagens salvas em: {VIS_DIR}")


if __name__ == "__main__":
    main()
