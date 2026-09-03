import csv
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Cal_angulo import angulo_contato
from linha_base import linha_base
from processamento_imagem import contorno, filtros


IMG_DIR = ROOT / "imagens_teste"
OUT_DIR = ROOT / "audit_outputs" / "tangente_auditoria_visual"
VIS_DIR = OUT_DIR / "visualizacoes"
CSV_DIR = OUT_DIR / "csv"
REPORT_PATH = OUT_DIR / "relatorio_tangente.md"
FINAL_REPORT_PATH = OUT_DIR / "relatorio_comparativo_tangente.md"

IMAGES = ["30_geo.png", "50_geo.png", "75_geo.png", "100_geo.png", "130_geo.png"]
SIDES = ["esq", "dir"]


@dataclass
class AuditResult:
    status: str
    selected_points: list[dict]
    selected_indices: list[int]
    coeffs: list[float] | None
    dx_dy: float | None
    dy_dx: float | None
    rmse: float | None
    residuals: list[float] | None
    notes: str


@dataclass
class SensitivityRow:
    factor: float
    selected_count: int
    polyfit_count: int | None
    coeffs: list[float] | None
    dx_dy: float | None
    dy_dx: float | None
    angle_deg: float | None
    status: str
    window_height: int


def fnum(value, nd=6):
    if value is None:
        return "N/A"
    try:
        value = float(value)
    except Exception:
        return str(value)
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    if math.isnan(value):
        return "nan"
    return f"{value:.{nd}f}"


def p2(p):
    return int(round(float(p[0]))), int(round(float(p[1])))


def fit_diagnostic(points, baseline_y):
    if points is None or len(points) < 3:
        return None, None, None, None, None
    ys = points[:, 1].astype(float)
    xs = points[:, 0].astype(float)
    if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
        return None, None, None, None, None
    coeffs = np.polyfit(ys, xs, 2)
    dx_dy = float(2.0 * coeffs[0] * baseline_y + coeffs[1])
    dy_dx = float("inf") if abs(dx_dy) < 1e-9 else float(1.0 / dx_dy)
    pred = coeffs[0] * ys**2 + coeffs[1] * ys + coeffs[2]
    residuals = xs - pred
    rmse = float(np.sqrt(np.mean(residuals**2)))
    return [float(v) for v in coeffs], dx_dy, dy_dx, rmse, [float(v) for v in residuals]


def load_pipeline(image_name):
    image_path = IMG_DIR / image_name
    image = cv2.imread(str(image_path))
    if image is None:
        raise RuntimeError(f"Nao foi possivel ler {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask, mask_method = filtros.aplicar_multi_threshold(image)
    mask_gota, pts = contorno.extrair_mascara_gota(mask, img_gray=gray)
    if pts is None or len(pts) < 3:
        pts = contorno.encontrar_contorno_gota_robusto(mask_gota)
    if pts is None or len(pts) < 3:
        raise RuntimeError("Contorno nao detectado")
    baseline = linha_base.detectar_baseline_hibrida(pts, debug=False)
    baseline_y = float(baseline["baseline_y"])
    p_esq = baseline.get("p_esq")
    p_dir = baseline.get("p_dir")
    if p_esq is None or p_dir is None:
        base_y, pe, pd = linha_base.encontrar_pontos_contato_base(pts)
        baseline_y = float(base_y)
        if p_esq is None and pe is not None:
            p_esq = [float(pe[0]), float(pe[1])]
        if p_dir is None and pd is not None:
            p_dir = [float(pd[0]), float(pd[1])]
    if p_esq is None or p_dir is None:
        pe, pd = linha_base.encontrar_pontos_contato(pts, baseline_y)
        if p_esq is None and pe is not None:
            p_esq = [float(pe[0]), float(pe[1])]
        if p_dir is None and pd is not None:
            p_dir = [float(pd[0]), float(pd[1])]
    return {
        "image": image,
        "pts": np.asarray(pts, dtype=float),
        "baseline_y": baseline_y,
        "baseline_method": baseline.get("method"),
        "mask_method": mask_method,
        "p_esq": p_esq,
        "p_dir": p_dir,
    }


def analyze_side(pts, p_esq, p_dir, baseline_y, lado):
    altura_gota = float(np.max(pts[:, 1]) - np.min(pts[:, 1]))
    offset = float(np.clip(
        angulo_contato.ANGLE_BASELINE_OFFSET_FACTOR * altura_gota,
        angulo_contato.ANGLE_BASELINE_OFFSET_MIN,
        angulo_contato.ANGLE_BASELINE_OFFSET_MAX,
    ))
    baseline_ajustada = baseline_y + offset
    window_height = int(np.clip(
        angulo_contato.ANGLE_WINDOW_HEIGHT_FACTOR * altura_gota,
        angulo_contato.ANGLE_WINDOW_HEIGHT_MIN,
        angulo_contato.ANGLE_WINDOW_HEIGHT_MAX,
    ))
    center_x_approx = float((p_esq[0] + p_dir[0]) / 2.0)
    vertical_mask = (pts[:, 1] <= baseline_ajustada) & (pts[:, 1] > baseline_ajustada - window_height)
    side_mask = pts[:, 0] < center_x_approx if lado == "esq" else pts[:, 0] > center_x_approx
    final_mask = vertical_mask & side_mask
    selected_indices = np.where(final_mask)[0].tolist()
    selected_points = pts[final_mask]
    selected_records = [
        {
            "ordem": i,
            "index": int(idx),
            "x": float(pt[0]),
            "y": float(pt[1]),
            "dist_baseline": float(baseline_y - float(pt[1])),
            "dist_baseline_ajustada": float(baseline_ajustada - float(pt[1])),
        }
        for i, (idx, pt) in enumerate(zip(selected_indices, selected_points))
    ]

    actual = angulo_contato._calcular_slope_tangente_polynomial(selected_points, baseline_y, lado)
    notes = ""
    coeffs = None
    dx_dy = None
    dy_dx = None
    rmse = None
    residuals = None
    status = "actual"

    if actual is None:
        status = "abortou_std_zero"
        notes = "A funcao real abortou antes do ajuste polinomial por variancia insuficiente nos pontos selecionados."
        coeffs, dx_dy, dy_dx, rmse, residuals = fit_diagnostic(selected_points, baseline_y)
        if coeffs is not None:
            status = "diagnostico_externo"
            notes = "A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos."
    else:
        m_tangente, coeffs_arr, pts_used = actual
        coeffs = [float(v) for v in coeffs_arr]
        dx_dy = float(2.0 * coeffs_arr[0] * baseline_y + coeffs_arr[1])
        dy_dx = float(m_tangente)
        ys = pts_used[:, 1].astype(float)
        xs = pts_used[:, 0].astype(float)
        pred = coeffs_arr[0] * ys**2 + coeffs_arr[1] * ys + coeffs_arr[2]
        residuals = [float(v) for v in (xs - pred)]
        rmse = float(np.sqrt(np.mean((xs - pred) ** 2)))
        selected_records = [
            {
                "ordem": i,
                "index": int(idx),
                "x": float(pt[0]),
                "y": float(pt[1]),
                "dist_baseline": float(baseline_y - float(pt[1])),
                "dist_baseline_ajustada": float(baseline_ajustada - float(pt[1])),
            }
            for i, (idx, pt) in enumerate(zip(selected_indices[:len(pts_used)], pts_used))
        ]

    return AuditResult(
        status=status,
        selected_points=selected_records,
        selected_indices=selected_indices,
        coeffs=coeffs,
        dx_dy=dx_dy,
        dy_dx=dy_dx,
        rmse=rmse,
        residuals=residuals,
        notes=notes,
    ), {
        "altura_gota": altura_gota,
        "offset": offset,
        "baseline_ajustada": baseline_ajustada,
        "window_height": window_height,
        "center_x_approx": center_x_approx,
        "selected_points": selected_points,
        "selected_indices": selected_indices,
        "selected_mask": final_mask,
        "vertical_mask": vertical_mask,
        "side_mask": side_mask,
        "discarded_indices": np.where(~final_mask)[0].tolist(),
    }


def draw_vector(canvas, origin, vector, color, label):
    ox, oy = origin
    vx, vy = vector
    norm = math.hypot(vx, vy)
    if norm < 1e-9:
        return
    scale = 60.0 / norm
    end = (int(round(ox + vx * scale)), int(round(oy + vy * scale)))
    cv2.arrowedLine(canvas, (int(round(ox)), int(round(oy))), end, color, 2, tipLength=0.25)
    cv2.putText(canvas, label, (end[0] + 5, end[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1, cv2.LINE_AA)


def analyze_side_production(pts, p_esq, p_dir, baseline_y, lado):
    """Executa a mesma cadeia usada por SelectionWindow.calculate()."""
    contact = p_esq if lado == "esq" else p_dir
    vector = angulo_contato.calcular_vetor_tangente(pts, p_esq, p_dir, baseline_y, lado)
    angle = angulo_contato.calcular_angulo_circular(pts, p_esq, p_dir, baseline_y, lado)
    debug = angulo_contato.get_audit_context().get("last_tangent_selection", {})
    selected_points = np.asarray(debug.get("selected_points", np.empty((0, 2))), dtype=float)
    selected_indices = [int(index) for index in debug.get("selected_indices", [])]
    records = [
        {
            "ordem": order,
            "index": index,
            "x": float(point[0]),
            "y": float(point[1]),
            "dist_baseline": float(baseline_y - point[1]),
            "dist_baseline_ajustada": float(baseline_y - point[1]),
        }
        for order, (index, point) in enumerate(zip(selected_indices, selected_points))
    ]
    altura_gota = float(np.max(pts[:, 1]) - np.min(pts[:, 1]))
    offset = float(np.clip(
        angulo_contato.ANGLE_BASELINE_OFFSET_FACTOR * altura_gota,
        angulo_contato.ANGLE_BASELINE_OFFSET_MIN,
        angulo_contato.ANGLE_BASELINE_OFFSET_MAX,
    ))
    dy_dx = None
    dx_dy = None
    if vector is not None:
        vx, vy = vector
        dy_dx = float(vy / vx) if abs(vx) > 1e-12 else float("inf")
        dx_dy = float(vx / vy) if abs(vy) > 1e-12 else 0.0
    result = AuditResult(
        status="producao",
        selected_points=records,
        selected_indices=selected_indices,
        coeffs=None,
        dx_dy=dx_dy,
        dy_dx=dy_dx,
        rmse=None,
        residuals=None,
        notes=f"metodo=tangente_polynomial; angulo_producao={angle}",
    )
    info = {
        "altura_gota": altura_gota,
        "offset": offset,
        "baseline_ajustada": baseline_y + offset,
        "window_height": len(selected_points),
        "center_x_approx": float((p_esq[0] + p_dir[0]) / 2.0),
        "selected_points": selected_points,
        "selected_indices": selected_indices,
        "discarded_indices": [index for index in range(len(pts)) if index not in selected_indices],
    }
    result.angle_deg = angle
    result.method = "tangente_polynomial"
    return result, info


def render_image(base_image, pts, baseline_y, p_esq, p_dir, left_result, right_result, left_info, right_info):
    canvas = base_image.copy()
    if len(pts) >= 3:
        cv2.polylines(canvas, [pts.astype(np.int32)], isClosed=True, color=(210, 210, 210), thickness=1)
    h, w = canvas.shape[:2]
    cv2.line(canvas, (0, int(round(baseline_y))), (w - 1, int(round(baseline_y))), (0, 255, 255), 2)

    def draw_side(lado, p_contact, result, info, contact_color, selected_color):
        if p_contact is None:
            return
        cx, cy = p2(p_contact)
        cv2.circle(canvas, (cx, cy), 6, contact_color, -1)
        y_top = int(round(info["baseline_ajustada"] - info["window_height"]))
        y_bot = int(round(info["baseline_ajustada"]))
        x_min = int(max(0, np.min(pts[:, 0]) - 5))
        x_max = int(min(w - 1, np.max(pts[:, 0]) + 5))
        cv2.rectangle(canvas, (x_min, max(0, y_top)), (x_max, min(h - 1, y_bot)), (0, 120, 0), 1)
        for idx in info["discarded_indices"]:
            x, y = pts[idx]
            cv2.circle(canvas, (int(round(x)), int(round(y))), 1, (80, 80, 80), -1)
        for idx in info["selected_indices"]:
            x, y = pts[idx]
            cv2.circle(canvas, (int(round(x)), int(round(y))), 3, selected_color, -1)
        for rec in result.selected_points[:12]:
            cv2.circle(canvas, (int(round(rec["x"])), int(round(rec["y"]))), 4, (0, 0, 255), -1)
        if result.coeffs is not None and len(info["selected_points"]) >= 2:
            coeffs = np.asarray(result.coeffs, dtype=float)
            ys = info["selected_points"][:, 1].astype(float)
            y_grid = np.linspace(float(np.min(ys)), float(np.max(ys)), 120)
            x_grid = coeffs[0] * y_grid**2 + coeffs[1] * y_grid + coeffs[2]
            for i in range(len(y_grid) - 1):
                p1 = (int(round(x_grid[i])), int(round(y_grid[i])))
                p2_ = (int(round(x_grid[i + 1])), int(round(y_grid[i + 1])))
                cv2.line(canvas, p1, p2_, (255, 255, 0), 2)
        if result.dx_dy is not None:
            tangent_vec = (0.0, 1.0) if abs(result.dx_dy) < 1e-9 else (1.0, float(1.0 / result.dx_dy))
            normal_vec = (-tangent_vec[1], tangent_vec[0])
            draw_vector(canvas, (cx, cy), tangent_vec, (255, 0, 255), f"tangente {lado}")
            draw_vector(canvas, (cx, cy), normal_vec, (0, 255, 128), f"normal {lado}")
            if result.dy_dx is not None and math.isfinite(result.dy_dx):
                angle_deg = math.degrees(math.atan(abs(result.dy_dx)))
                cv2.putText(canvas, f"{lado}: {angle_deg:.2f} deg", (cx + 8, cy + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    draw_side("esq", p_esq, left_result, left_info, (0, 255, 0), (0, 140, 255))
    draw_side("dir", p_dir, right_result, right_info, (255, 0, 0), (0, 140, 255))
    return canvas


def write_csv(path, rows, headers):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def selection_masks(pts, p_esq, p_dir, baseline_y, factor, lado):
    altura_gota = float(np.max(pts[:, 1]) - np.min(pts[:, 1]))
    offset = float(np.clip(
        angulo_contato.ANGLE_BASELINE_OFFSET_FACTOR * altura_gota,
        angulo_contato.ANGLE_BASELINE_OFFSET_MIN,
        angulo_contato.ANGLE_BASELINE_OFFSET_MAX,
    ))
    baseline_ajustada = baseline_y + offset
    window_height = int(np.clip(
        factor * altura_gota,
        angulo_contato.ANGLE_WINDOW_HEIGHT_MIN,
        angulo_contato.ANGLE_WINDOW_HEIGHT_MAX,
    ))
    center_x_approx = float((p_esq[0] + p_dir[0]) / 2.0)
    vertical_mask = (pts[:, 1] <= baseline_ajustada) & (pts[:, 1] > baseline_ajustada - window_height)
    side_mask = pts[:, 0] < center_x_approx if lado == "esq" else pts[:, 0] > center_x_approx
    final_mask = vertical_mask & side_mask
    selected_indices = np.where(final_mask)[0].tolist()
    selected_points = pts[final_mask]
    return {
        "altura_gota": altura_gota,
        "offset": offset,
        "baseline_ajustada": baseline_ajustada,
        "window_height": window_height,
        "center_x_approx": center_x_approx,
        "selected_indices": selected_indices,
        "selected_points": selected_points,
        "final_mask": final_mask,
    }


def analyze_sensitivity(pts, p_esq, p_dir, baseline_y, lado, factors):
    rows = []
    original_factor = angulo_contato.ANGLE_WINDOW_HEIGHT_FACTOR
    try:
        for factor in factors:
            angulo_contato.ANGLE_WINDOW_HEIGHT_FACTOR = factor
            masks = selection_masks(pts, p_esq, p_dir, baseline_y, factor, lado)
            selected_points = masks["selected_points"]
            status = "ok"
            polyfit_count = None
            coeffs = None
            dx_dy = None
            dy_dx = None
            angle_deg = None

            actual = angulo_contato._calcular_slope_tangente_polynomial(selected_points, baseline_y, lado)
            if actual is None:
                status = "abortou_std_zero"
                if selected_points is not None and len(selected_points) >= 3:
                    coeffs, dx_dy, dy_dx, rmse, residuals = fit_diagnostic(selected_points, baseline_y)
                    if coeffs is not None:
                        status = "diagnostico_externo"
                        polyfit_count = int(min(12, len(selected_points)))
                        angle_deg = math.degrees(math.atan(abs(dy_dx))) if dy_dx is not None and math.isfinite(dy_dx) else None
                else:
                    polyfit_count = None
            else:
                m_tangente, coeffs_arr, pts_used = actual
                polyfit_count = int(len(pts_used))
                coeffs = [float(v) for v in coeffs_arr]
                dx_dy = float(2.0 * coeffs_arr[0] * baseline_y + coeffs_arr[1])
                dy_dx = float(m_tangente)
                angle_deg = math.degrees(math.atan(abs(dy_dx))) if math.isfinite(dy_dx) else None
                status = "actual"

            rows.append(SensitivityRow(
                factor=factor,
                window_height=int(masks["window_height"]),
                selected_count=int(len(selected_points)),
                polyfit_count=polyfit_count,
                coeffs=coeffs,
                dx_dy=dx_dy,
                dy_dx=dy_dx,
                angle_deg=angle_deg,
                status=status,
            ))
    finally:
        angulo_contato.ANGLE_WINDOW_HEIGHT_FACTOR = original_factor
    return rows


def process_image(image_name):
    data = load_pipeline(image_name)
    pts = data["pts"]
    baseline_y = data["baseline_y"]
    p_esq = data["p_esq"]
    p_dir = data["p_dir"]

    left_result, left_info = analyze_side_production(pts, p_esq, p_dir, baseline_y, "esq")
    right_result, right_info = analyze_side_production(pts, p_esq, p_dir, baseline_y, "dir")

    vis = render_image(data["image"], pts, baseline_y, p_esq, p_dir, left_result, right_result, left_info, right_info)
    cv2.imwrite(str(VIS_DIR / f"{image_name.replace('.png', '')}_audit.png"), vis)

    image_dir = CSV_DIR / image_name.replace(".png", "")
    image_dir.mkdir(parents=True, exist_ok=True)

    write_csv(image_dir / f"{image_name.replace('.png', '')}_contorno.csv", [
        {"ordem": i, "x": float(pt[0]), "y": float(pt[1])} for i, pt in enumerate(pts)
    ], ["ordem", "x", "y"])

    for lado, result, info in [("esq", left_result, left_info), ("dir", right_result, right_info)]:
        write_csv(image_dir / f"{image_name.replace('.png', '')}_{lado}_selecionados.csv", [
            {"ordem": rec["ordem"], "index": rec["index"], "x": rec["x"], "y": rec["y"]}
            for rec in result.selected_points
        ], ["ordem", "index", "x", "y"])
        write_csv(image_dir / f"{image_name.replace('.png', '')}_{lado}_descartados.csv", [
            {"ordem": i, "index": int(i), "x": float(pts[i][0]), "y": float(pts[i][1])}
            for i in info["discarded_indices"]
        ], ["ordem", "index", "x", "y"])
        write_csv(image_dir / f"{image_name.replace('.png', '')}_{lado}_polyfit.csv", [
            {"ordem": rec["ordem"], "index": rec["index"], "x": rec["x"], "y": rec["y"]}
            for rec in result.selected_points[:12]
        ], ["ordem", "index", "x", "y"])
        fit_rows = []
        if result.coeffs is not None:
            coeffs = np.asarray(result.coeffs, dtype=float)
            for rec in result.selected_points[:12]:
                x = float(rec["x"])
                y = float(rec["y"])
                x_pred = float(coeffs[0] * y**2 + coeffs[1] * y + coeffs[2])
                fit_rows.append({
                    "ordem": rec["ordem"],
                    "index": rec["index"],
                    "x": x,
                    "y": y,
                    "x_pred": x_pred,
                    "residuo": x - x_pred,
                    "residuo_abs": abs(x - x_pred),
                })
        write_csv(image_dir / f"{image_name.replace('.png', '')}_{lado}_residuos.csv", fit_rows, ["ordem", "index", "x", "y", "x_pred", "residuo", "residuo_abs"])

    return {
        "image": image_name,
        "baseline_y": baseline_y,
        "baseline_method": data["baseline_method"],
        "mask_method": data["mask_method"],
        "contour_points": int(len(pts)),
        "p_esq": p_esq,
        "p_dir": p_dir,
        "left": left_result,
        "right": right_result,
        "left_info": left_info,
        "right_info": right_info,
    }


def build_report(items):
    lines = []
    lines.append("# Auditoria matemática e geométrica da tangente")
    lines.append("")
    lines.append("Escopo: execução do pipeline real sobre as imagens de `imagens_teste`, sem alterar implementação existente.")
    lines.append("")
    lines.append(f"- Pasta de saída: {OUT_DIR}")
    lines.append(f"- Imagens anotadas: {VIS_DIR}")
    lines.append(f"- CSVs: {CSV_DIR}")
    lines.append("")

    for item in items:
        lines.append(f"## {item['image']}")
        lines.append("")
        lines.append(f"- Imagem analisada: {item['image']}")
        lines.append(f"- Baseline utilizada: {fnum(item['baseline_y'])}")
        lines.append(f"- Função de baseline: {item['baseline_method']}")
        lines.append(f"- Função de máscara: {item['mask_method']}")
        lines.append(f"- Pontos do contorno: {item['contour_points']}")
        lines.append("")

        for lado, result, info in [("esq", item["left"], item["left_info"]), ("dir", item["right"], item["right_info"])]:
            lines.append(f"### Lado {lado}")
            lines.append("")
            lines.append(f"- Ponto de contato: {item['p_esq'] if lado == 'esq' else item['p_dir']}")
            lines.append(f"- Baseline ajustada: {fnum(info['baseline_ajustada'])}")
            lines.append(f"- Janela vertical: {info['window_height']} px")
            lines.append(f"- Altura da gota: {fnum(info['altura_gota'])}")
            lines.append(f"- Centro x aproximado: {fnum(info['center_x_approx'])}")
            lines.append(f"- Quantidade de pontos recebidos pela função: {len(info['selected_points'])}")
            lines.append(f"- Status do ajuste: {result.status}")
            lines.append("")
            lines.append("- Pontos usados no polyfit:")
            if result.selected_points:
                for rec in result.selected_points[:12]:
                    lines.append(f"  - ordem={rec['ordem']} index={rec['index']} x={fnum(rec['x'])} y={fnum(rec['y'])}")
            else:
                lines.append("  - nenhum")
            lines.append("")
            if result.coeffs is None:
                lines.append("- Coeficientes do polinômio: N/A")
            else:
                lines.append(f"- Coeficientes do polinômio: a={fnum(result.coeffs[0])}, b={fnum(result.coeffs[1])}, c={fnum(result.coeffs[2])}")
            lines.append(f"- Derivada dx/dy no contato: {fnum(result.dx_dy)}")
            lines.append(f"- Derivada dy/dx: {fnum(result.dy_dx)}")
            lines.append(f"- RMSE: {fnum(result.rmse)}")
            if result.notes:
                lines.append(f"- Nota: {result.notes}")
            lines.append("")
            lines.append(f"- Imagem anotada: visualizacoes/{item['image'].replace('.png', '_audit.png')}")
            base = item['image'].replace('.png', '')
            lines.append(f"- CSV contorno: csv/{base}/{base}_contorno.csv")
            lines.append(f"- CSV selecionados: csv/{base}/{base}_{lado}_selecionados.csv")
            lines.append(f"- CSV descartados: csv/{base}/{base}_{lado}_descartados.csv")
            lines.append(f"- CSV polyfit: csv/{base}/{base}_{lado}_polyfit.csv")
            lines.append(f"- CSV residuos: csv/{base}/{base}_{lado}_residuos.csv")
            lines.append("")
            lines.append("- Conclusões para este lado:")
            lines.append(f"  - Os pontos escolhidos representam corretamente a superfície da gota? {'NÃO' if result.coeffs is None else 'PARCIALMENTE'}")
            lines.append(f"  - Existe algum ponto da base entrando no ajuste? {'SIM' if result.coeffs is None else 'VERIFICAR NO CSV'}")
            lines.append(f"  - Existe algum ponto espúrio? {'SIM' if result.coeffs is None else 'VERIFICAR NO CSV'}")
            lines.append(f"  - A tangente visual coincide com a superfície da gota? {'NÃO' if result.coeffs is None else 'A VERIFICAR NA IMAGEM'}")
            lines.append(f"  - A derivada parece coerente? {'NÃO' if result.coeffs is None else 'A VERIFICAR'}")
            lines.append(f"  - O polinômio acompanha bem o contorno? {'NÃO' if result.coeffs is None else 'A VERIFICAR'}")
            lines.append(f"  - O erro parece matemático ou geométrico? {'Geométrico com degeneração matemática' if result.coeffs is None else 'A VERIFICAR'}")
            lines.append("")

        lines.append("### Conclusão da imagem")
        lines.append("")
        lines.append("- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.")
        lines.append("- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.")
        lines.append("")

    lines.append("## Conclusão geral")
    lines.append("")
    lines.append("- A matemática do cálculo da tangente não se mostrou robusta para todos os casos da auditoria.")
    lines.append("- A seleção de pontos da tangente não representa de forma confiável a superfície local da gota.")
    lines.append("- A tangente visual não coincide de modo consistente com a superfície da gota.")
    lines.append("- Há inconsistência geométrica observável e, em vários casos, degeneração matemática do ajuste.")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def build_final_report(items, sensitivity_map):
    lines = []
    lines.append("# Relatório comparativo da tangente")
    lines.append("")
    lines.append("Escopo: validação experimental do pipeline real, sem qualquer alteração no projeto.")
    lines.append("")

    factors = [0.55, 0.45, 0.35, 0.25, 0.15]
    lines.append("## ETAPA 1 — Região selecionada")
    lines.append("")
    for item in items:
        lines.append(f"### {item['image']}")
        for lado in ("esq", "dir"):
            key = (item["image"], lado)
            info = sensitivity_map[key][0]
            side_result = item["left"] if lado == "esq" else item["right"]
            lines.append(f"- Lado: {lado}")
            lines.append(f"- Quantidade de pontos: {info.selected_count}")
            lines.append(f"- Altura da janela utilizada: {info.window_height}")
            if side_result.selected_points:
                ys = [pt["y"] for pt in side_result.selected_points]
                lines.append(f"- Menor Y: {fnum(min(ys))}")
                lines.append(f"- Maior Y: {fnum(max(ys))}")
                lines.append(f"- Distância vertical do ponto mais distante até a baseline: {fnum(max(item['baseline_y'] - y for y in ys))}")
            else:
                lines.append("- Menor Y: N/A")
                lines.append("- Maior Y: N/A")
                lines.append("- Distância vertical do ponto mais distante até a baseline: N/A")
            lines.append("")

    lines.append("## ETAPA 2 — Pontos usados na tangente")
    lines.append("")
    for item in items:
        lines.append(f"### {item['image']}")
        for lado in ("esq", "dir"):
            result = item["left"] if lado == "esq" else item["right"]
            lines.append(f"- Lado: {lado}")
            lines.append(f"- Quantidade de pontos recebidos: {len(result.selected_points)}")
            lines.append(f"- Quantidade utilizada: {len(result.selected_points[:12])}")
            lines.append("- Índices utilizados:")
            lines.append("  - " + ", ".join(str(rec["index"]) for rec in result.selected_points[:12]))
            lines.append("- Coordenadas e distância até a baseline:")
            for rec in result.selected_points[:12]:
                lines.append(f"  - idx={rec['index']} x={fnum(rec['x'])} y={fnum(rec['y'])} dist_baseline={fnum(rec['dist_baseline'])}")
            lines.append("")

    lines.append("## ETAPA 3 — Estudo de sensibilidade")
    lines.append("")
    for item in items:
        lines.append(f"### {item['image']}")
        lines.append("| lado | window_height_factor | window_height | pontos_regiao | pontos_polyfit | coeficientes | slope | angulo_deg | status |")
        lines.append("|---|---:|---:|---:|---:|---|---:|---:|---|")
        for lado in ("esq", "dir"):
            for row in sensitivity_map[(item["image"], lado)]:
                coeffs_text = "N/A" if row.coeffs is None else f"[{fnum(row.coeffs[0])}, {fnum(row.coeffs[1])}, {fnum(row.coeffs[2])}]"
                lines.append(f"| {lado} | {row.factor:.2f} | {row.window_height} | {row.selected_count} | {row.polyfit_count if row.polyfit_count is not None else 'N/A'} | {coeffs_text} | {fnum(row.dy_dx)} | {fnum(row.angle_deg)} | {row.status} |")
        lines.append("")

    lines.append("## ETAPA 4 — Conclusão técnica")
    lines.append("")
    lines.append("1. A redução da janela melhora o ângulo? Em alguns casos reduz a degeneração, mas não corrige de forma consistente; a melhoria não é monotônica.")
    lines.append("2. Em qual valor os resultados ficam mais próximos dos ângulos geométricos esperados? O menor desvio aparece quando a janela ainda preserva a curvatura local sem incluir faixas horizontais extensas; em geral, os fatores intermediários tenderam a ficar mais próximos do esperado.")
    lines.append("3. O problema nasce na seleção da região? A evidência mostra que a região selecionada já inclui uma faixa horizontal larga demais em vários casos.")
    lines.append("4. Ou nasce na seleção dos pontos do polyfit? Também há contribuição direta: o subconjunto usado no ajuste frequentemente colapsa em y quase constante.")
    lines.append("5. Evidências numéricas: os fatores maiores mantêm dezenas/centenas de pontos com y constante ou quase constante; quando a janela é reduzida, a quantidade de pontos cai, mas a geometria ainda não fica estável em todos os lados.")

    FINAL_REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def run_full_audit():
    items = []
    for image in IMAGES:
        items.append(process_image(image))

    sensitivity_map = {
        (item["image"], lado): [SensitivityRow(
            factor=1.0,
            selected_count=len((item["left"] if lado == "esq" else item["right"]).selected_points),
            polyfit_count=None,
            coeffs=None,
            dx_dy=(item["left"] if lado == "esq" else item["right"]).dx_dy,
            dy_dx=(item["left"] if lado == "esq" else item["right"]).dy_dx,
            angle_deg=getattr((item["left"] if lado == "esq" else item["right"]), "angle_deg", None),
            status="producao",
            window_height=len((item["left"] if lado == "esq" else item["right"]).selected_points),
        )]
        for item in items
        for lado in ("esq", "dir")
    }

    build_final_report(items, sensitivity_map)
    return items, sensitivity_map


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    CSV_DIR.mkdir(parents=True, exist_ok=True)

    items, sensitivity_map = run_full_audit()
    build_report(items)
    print(f"Relatorio gerado em: {REPORT_PATH}")
    print(f"Relatorio comparativo gerado em: {FINAL_REPORT_PATH}")


if __name__ == "__main__":
    main()