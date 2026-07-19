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
OUT_DIR = ROOT / "audit_outputs" / "selecionar_pontos_tangente_focada"
VIS_DIR = OUT_DIR / "visualizacoes"
CSV_DIR = OUT_DIR / "csv"
REPORT_PATH = OUT_DIR / "relatorio_auditoria_selecao_tangente.md"

IMAGES = ["30_geo.png", "50_geo.png", "75_geo.png", "100_geo.png", "130_geo.png"]


@dataclass
class SelectionAudit:
    image_name: str
    lado: str
    baseline_y: float
    baseline_adjusted: float
    window_height: int
    height: float
    center_x: float
    contact_point: list[float] | None
    received_rows: list[dict]
    discarded_rows: list[dict]
    kept_rows: list[dict]
    coeffs: list[float] | None
    dx_dy: float | None
    dy_dx: float | None
    eval_point: tuple[float, float] | None
    selected_count: int
    status: str
    notes: str


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


def selection_region(pts, p_esq, p_dir, baseline_y, lado, factor=None):
    altura_gota = float(np.max(pts[:, 1]) - np.min(pts[:, 1]))
    offset = float(np.clip(
        angulo_contato.ANGLE_BASELINE_OFFSET_FACTOR * altura_gota,
        angulo_contato.ANGLE_BASELINE_OFFSET_MIN,
        angulo_contato.ANGLE_BASELINE_OFFSET_MAX,
    ))
    baseline_adjusted = baseline_y + offset
    if factor is None:
        factor = angulo_contato.ANGLE_WINDOW_HEIGHT_FACTOR
    window_height = int(np.clip(
        factor * altura_gota,
        angulo_contato.ANGLE_WINDOW_HEIGHT_MIN,
        angulo_contato.ANGLE_WINDOW_HEIGHT_MAX,
    ))
    center_x = float((p_esq[0] + p_dir[0]) / 2.0)
    vertical_mask = (pts[:, 1] <= baseline_adjusted) & (pts[:, 1] > baseline_adjusted - window_height)
    side_mask = pts[:, 0] < center_x if lado == "esq" else pts[:, 0] > center_x
    final_mask = vertical_mask & side_mask
    selected_contour_indices = np.where(final_mask)[0].tolist()
    selected_points = pts[final_mask]
    return {
        "altura_gota": altura_gota,
        "offset": offset,
        "baseline_adjusted": baseline_adjusted,
        "window_height": window_height,
        "center_x": center_x,
        "selected_contour_indices": selected_contour_indices,
        "selected_points": selected_points,
    }


def fit_polynomial(points, baseline_y):
    if points is None or len(points) < 3:
        return None, None, None, None, None

    ys = points[:, 1].astype(float)
    xs = points[:, 0].astype(float)
    if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
        return None, None, None, None, None

    coeffs = np.polyfit(ys, xs, 2)
    dx_dy = float(2.0 * coeffs[0] * baseline_y + coeffs[1])
    dy_dx = float("inf") if abs(dx_dy) < 1e-9 else float(1.0 / dx_dy)
    x_eval = float(coeffs[0] * baseline_y**2 + coeffs[1] * baseline_y + coeffs[2])
    residuals = xs - (coeffs[0] * ys**2 + coeffs[1] * ys + coeffs[2])
    rmse = float(np.sqrt(np.mean(residuals**2)))
    return [float(v) for v in coeffs], dx_dy, dy_dx, (x_eval, float(baseline_y)), rmse


def build_rows(local_pts, contour_indices, kept_local_indices, baseline_y, baseline_adjusted):
    selected_set = set(int(i) for i in kept_local_indices)
    received_rows = []
    discarded_rows = []

    for order_in, pt in enumerate(local_pts):
        dist = float(baseline_y - float(pt[1]))
        dist_adj = float(baseline_adjusted - float(pt[1]))
        row = {
            "ordem_entrada": order_in,
            "indice_local": order_in,
            "indice_contorno": int(contour_indices[order_in]),
            "x": float(pt[0]),
            "y": float(pt[1]),
            "dist_baseline": dist,
            "dist_baseline_ajustada": dist_adj,
        }
        received_rows.append(row)

        if order_in not in selected_set:
            row_discard = dict(row)
            row_discard["motivo"] = "fora_da_janela" if not (0.0 <= dist <= 30.0) else "fora_do_top12"
            discarded_rows.append(row_discard)

    kept_rows = []
    for order_out, idx in enumerate(kept_local_indices):
        pt = local_pts[idx]
        kept_rows.append({
            "ordem_mantida": order_out,
            "ordem_entrada": int(idx),
            "indice_local": int(idx),
            "indice_contorno": int(contour_indices[idx]),
            "x": float(pt[0]),
            "y": float(pt[1]),
            "dist_baseline": float(baseline_y - float(pt[1])),
            "dist_baseline_ajustada": float(baseline_adjusted - float(pt[1])),
        })

    return received_rows, discarded_rows, kept_rows


def write_csv(path, rows, headers):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def render_selection_image(base_image, received_rows, kept_rows, discarded_rows, coeffs, baseline_y, eval_point, out_path):
    pts = np.asarray([[row["x"], row["y"]] for row in received_rows], dtype=float)
    points_for_crop = [pts[:, 0], pts[:, 1]]
    if coeffs is not None and len(kept_rows) >= 2:
        ys = np.array([row["y"] for row in kept_rows], dtype=float)
        y_grid = np.linspace(float(np.min(ys)), float(np.max(ys)), 180)
        x_grid = coeffs[0] * y_grid**2 + coeffs[1] * y_grid + coeffs[2]
        points_for_crop.extend([x_grid, y_grid])
        if eval_point is not None:
            points_for_crop[0] = np.append(points_for_crop[0], eval_point[0])
            points_for_crop[1] = np.append(points_for_crop[1], eval_point[1])

    min_x = max(0, int(math.floor(float(np.min(points_for_crop[0])))) - 15)
    max_x = min(base_image.shape[1] - 1, int(math.ceil(float(np.max(points_for_crop[0])))) + 15)
    min_y = max(0, int(math.floor(float(np.min(points_for_crop[1])))) - 15)
    max_y = min(base_image.shape[0] - 1, int(math.ceil(float(np.max(points_for_crop[1])))) + 15)

    width = max(1, max_x - min_x + 1)
    height = max(1, max_y - min_y + 1)
    canvas = np.full((height, width, 3), 245, dtype=np.uint8)

    def shift(point):
        return int(round(float(point[0]) - min_x)), int(round(float(point[1]) - min_y))

    for pt in pts:
        x, y = shift(pt)
        cv2.circle(canvas, (x, y), 2, (165, 165, 165), -1)

    discard_set = {int(row["ordem_entrada"]) for row in discarded_rows}
    keep_set = {int(row["ordem_entrada"]) for row in kept_rows}

    for idx, pt in enumerate(pts):
        x, y = shift(pt)
        if idx in discard_set:
            cv2.circle(canvas, (x, y), 3, (70, 70, 220), -1)
        if idx in keep_set:
            cv2.circle(canvas, (x, y), 4, (40, 170, 40), -1)

    for row in kept_rows:
        x, y = shift((row["x"], row["y"]))
        cv2.putText(canvas, str(row["ordem_mantida"] + 1), (x + 4, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (20, 20, 20), 1, cv2.LINE_AA)

    if coeffs is not None and len(kept_rows) >= 2:
        ys = np.array([row["y"] for row in kept_rows], dtype=float)
        y_grid = np.linspace(float(np.min(ys)), float(np.max(ys)), 220)
        x_grid = coeffs[0] * y_grid**2 + coeffs[1] * y_grid + coeffs[2]
        for i in range(len(y_grid) - 1):
            p1 = shift((x_grid[i], y_grid[i]))
            p2 = shift((x_grid[i + 1], y_grid[i + 1]))
            cv2.line(canvas, p1, p2, (220, 120, 0), 2)

    if eval_point is not None:
        ex, ey = shift(eval_point)
        cv2.circle(canvas, (ex, ey), 5, (0, 220, 220), -1)
        cv2.circle(canvas, (ex, ey), 8, (0, 120, 120), 1)

    cv2.rectangle(canvas, (8, 8), (220, 86), (255, 255, 255), -1)
    cv2.rectangle(canvas, (8, 8), (220, 86), (210, 210, 210), 1)
    cv2.circle(canvas, (22, 24), 3, (165, 165, 165), -1)
    cv2.putText(canvas, "recebidos", (34, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (30, 30, 30), 1, cv2.LINE_AA)
    cv2.circle(canvas, (22, 42), 4, (40, 170, 40), -1)
    cv2.putText(canvas, "mantidos", (34, 46), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (30, 30, 30), 1, cv2.LINE_AA)
    cv2.circle(canvas, (22, 60), 4, (70, 70, 220), -1)
    cv2.putText(canvas, "descartados", (34, 64), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (30, 30, 30), 1, cv2.LINE_AA)
    cv2.circle(canvas, (22, 78), 4, (0, 220, 220), -1)
    cv2.putText(canvas, "derivada", (34, 82), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (30, 30, 30), 1, cv2.LINE_AA)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out_path), canvas)


def analyze_side(image_name, pts, p_esq, p_dir, baseline_y, lado):
    local_selection = selection_region(pts, p_esq, p_dir, baseline_y, lado)
    local_pts = np.asarray(local_selection["selected_points"], dtype=float)
    contour_indices = local_selection["selected_contour_indices"]
    distance_from_baseline = baseline_y - local_pts[:, 1]
    valid_mask = (distance_from_baseline >= 0.0) & (distance_from_baseline <= 30.0)
    candidate_indices = np.where(valid_mask)[0]
    sorted_candidates = candidate_indices[np.argsort(distance_from_baseline[valid_mask])]
    kept_local_indices = sorted_candidates[: min(12, len(sorted_candidates))].tolist()

    received_rows, discarded_rows, kept_rows = build_rows(
        local_pts,
        contour_indices,
        kept_local_indices,
        baseline_y,
        local_selection["baseline_adjusted"],
    )

    coeffs = None
    dx_dy = None
    dy_dx = None
    eval_point = None
    status = "abortou_std_zero"
    notes = "A funcao real nao conseguiu completar o ajuste com a amostra recebida."

    selected_points = local_pts[kept_local_indices]
    if len(selected_points) >= 3:
        coeffs_diag, dx_dy_diag, dy_dx_diag, eval_point_diag, _ = fit_polynomial(selected_points, baseline_y)
        if coeffs_diag is not None:
            coeffs = coeffs_diag
            dx_dy = dx_dy_diag
            dy_dx = dy_dx_diag
            eval_point = eval_point_diag
            status = "diagnostico_externo"
            notes = "A parabola e a derivada sao calculadas sobre o subconjunto retornado pela selecao local da funcao."

    return SelectionAudit(
        image_name=image_name,
        lado=lado,
        baseline_y=float(baseline_y),
        baseline_adjusted=float(local_selection["baseline_adjusted"]),
        window_height=int(local_selection["window_height"]),
        height=float(local_selection["altura_gota"]),
        center_x=float(local_selection["center_x"]),
        contact_point=p_esq if lado == "esq" else p_dir,
        received_rows=received_rows,
        discarded_rows=discarded_rows,
        kept_rows=kept_rows,
        coeffs=coeffs,
        dx_dy=dx_dy,
        dy_dx=dy_dx,
        eval_point=eval_point,
        selected_count=int(len(local_pts)),
        status=status,
        notes=notes,
    )


def write_side_outputs(image_name, image, audit):
    base = image_name.replace(".png", "")
    side_dir = CSV_DIR / base / audit.lado
    side_dir.mkdir(parents=True, exist_ok=True)

    write_csv(
        side_dir / "recebidos.csv",
        audit.received_rows,
        ["ordem_entrada", "indice_local", "indice_contorno", "x", "y", "dist_baseline", "dist_baseline_ajustada"],
    )
    write_csv(
        side_dir / "descartados.csv",
        audit.discarded_rows,
        ["ordem_entrada", "indice_local", "indice_contorno", "x", "y", "dist_baseline", "dist_baseline_ajustada", "motivo"],
    )
    write_csv(
        side_dir / "mantidos.csv",
        audit.kept_rows,
        ["ordem_mantida", "ordem_entrada", "indice_local", "indice_contorno", "x", "y", "dist_baseline", "dist_baseline_ajustada"],
    )

    poly_rows = []
    if audit.coeffs is not None and audit.kept_rows:
        coeffs = np.asarray(audit.coeffs, dtype=float)
        for row in audit.kept_rows:
            x = float(row["x"])
            y = float(row["y"])
            x_pred = float(coeffs[0] * y**2 + coeffs[1] * y + coeffs[2])
            poly_rows.append({
                "ordem_mantida": row["ordem_mantida"],
                "ordem_entrada": row["ordem_entrada"],
                "indice_local": row["indice_local"],
                "indice_contorno": row["indice_contorno"],
                "x": x,
                "y": y,
                "x_pred": x_pred,
                "residuo": x - x_pred,
                "residuo_abs": abs(x - x_pred),
            })
    write_csv(
        side_dir / "parabola.csv",
        poly_rows,
        ["ordem_mantida", "ordem_entrada", "indice_local", "indice_contorno", "x", "y", "x_pred", "residuo", "residuo_abs"],
    )

    render_selection_image(
        image,
        audit.received_rows,
        audit.kept_rows,
        audit.discarded_rows,
        np.asarray(audit.coeffs, dtype=float) if audit.coeffs is not None else None,
        audit.baseline_y,
        audit.eval_point,
        VIS_DIR / f"{base}_{audit.lado}_foco.png",
    )


def build_report(items):
    lines = []
    lines.append("# Auditoria focada da selecao de pontos da tangente")
    lines.append("")
    lines.append("Escopo: apenas a funcao `_selecionar_pontos_tangente()` e a parabola derivada dos pontos que ela manteve.")
    lines.append("")
    lines.append(f"- Pasta de saida: {OUT_DIR}")
    lines.append(f"- Imagens focadas: {VIS_DIR}")
    lines.append(f"- CSVs: {CSV_DIR}")
    lines.append("")

    for item in items:
        lines.append(f"## {item['image']}")
        lines.append("")
        lines.append(f"- Baseline utilizada: {fnum(item['baseline_y'])}")
        lines.append(f"- Funcao de baseline: {item['baseline_method']}")
        lines.append(f"- Funcao de mascara: {item['mask_method']}")
        lines.append(f"- Pontos do contorno: {item['contour_points']}")
        lines.append("")

        for audit in item["sides"]:
            lines.append(f"### Lado {audit.lado}")
            lines.append("")
            lines.append(f"- Ponto de contato: {audit.contact_point}")
            lines.append(f"- Baseline ajustada: {fnum(audit.baseline_adjusted)}")
            lines.append(f"- Janela vertical usada pela selecao: {audit.window_height} px")
            lines.append(f"- Altura da gota: {fnum(audit.height)}")
            lines.append(f"- Centro x aproximado: {fnum(audit.center_x)}")
            lines.append(f"- Quantidade de pontos recebidos pela funcao: {len(audit.received_rows)}")
            lines.append(f"- Quantidade de pontos mantidos pela funcao: {len(audit.kept_rows)}")
            lines.append(f"- Quantidade de pontos descartados pela funcao: {len(audit.discarded_rows)}")
            lines.append(f"- Status: {audit.status}")
            lines.append("")
            lines.append("- Todos os pontos recebidos: CSV `recebidos.csv`")
            lines.append("- Todos os pontos descartados: CSV `descartados.csv`")
            lines.append("- Ordem final dos pontos mantidos: CSV `mantidos.csv`")
            lines.append("")
            lines.append("- Pontos mantidos na ordem retornada pela funcao:")
            if audit.kept_rows:
                for row in audit.kept_rows:
                    lines.append(
                        f"  - ordem={row['ordem_mantida']} entrada={row['ordem_entrada']} indice_local={row['indice_local']} x={fnum(row['x'])} y={fnum(row['y'])} dist_baseline={fnum(row['dist_baseline'])}"
                    )
            else:
                lines.append("  - nenhum")
            lines.append("")
            if audit.coeffs is not None:
                lines.append(f"- Parabola ajustada: a={fnum(audit.coeffs[0])}, b={fnum(audit.coeffs[1])}, c={fnum(audit.coeffs[2])}")
                lines.append(f"- Derivada dx/dy no ponto de contato do ajuste: {fnum(audit.dx_dy)}")
                lines.append(f"- Derivada dy/dx: {fnum(audit.dy_dx)}")
                lines.append(f"- Ponto exato onde a derivada foi calculada: x={fnum(audit.eval_point[0])}, y={fnum(audit.eval_point[1])}")
            else:
                lines.append("- Parabola ajustada: N/A")
                lines.append("- Derivada dx/dy no ponto de contato do ajuste: N/A")
                lines.append("- Derivada dy/dx: N/A")
                lines.append("- Ponto exato onde a derivada foi calculada: N/A")
            lines.append(f"- Nota: {audit.notes}")
            lines.append("")
            lines.append(f"- Imagem focada: visualizacoes/{item['image'].replace('.png', '')}_{audit.lado}_foco.png")
            lines.append(f"- CSV recebidos: csv/{item['image'].replace('.png', '')}/{audit.lado}/recebidos.csv")
            lines.append(f"- CSV descartados: csv/{item['image'].replace('.png', '')}/{audit.lado}/descartados.csv")
            lines.append(f"- CSV mantidos: csv/{item['image'].replace('.png', '')}/{audit.lado}/mantidos.csv")
            lines.append(f"- CSV parabola: csv/{item['image'].replace('.png', '')}/{audit.lado}/parabola.csv")
            lines.append("")

    lines.append("## Conclusao objetiva")
    lines.append("")
    lines.append("- A funcao recebe a regiao local calculada antes dela e, dentro dessa regiao, seleciona apenas os pontos com distancia de 0 a 30 px acima da baseline ajustada.")
    lines.append("- Desses pontos, ela retira no maximo 12, em ordem de proximidade crescente com a baseline.")
    lines.append("- Quando os pontos remanescentes ficam quase colineares ou com y quase constante, a parabola de apoio deixa de existir no caminho real e o ajuste aborta.")
    lines.append("- A imagem focada mostra apenas recebidos, descartados, mantidos, a parabola ajustada quando existe e o ponto exato de avaliacao da derivada.")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def process_image(image_name):
    data = load_pipeline(image_name)
    pts = data["pts"]

    left = analyze_side(image_name, pts, data["p_esq"], data["p_dir"], data["baseline_y"], "esq")
    right = analyze_side(image_name, pts, data["p_esq"], data["p_dir"], data["baseline_y"], "dir")

    for audit in [left, right]:
        write_side_outputs(image_name, data["image"], audit)

    return {
        "image": image_name,
        "baseline_y": data["baseline_y"],
        "baseline_method": data["baseline_method"],
        "mask_method": data["mask_method"],
        "contour_points": int(len(pts)),
        "sides": [left, right],
    }


def run():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    CSV_DIR.mkdir(parents=True, exist_ok=True)
    items = [process_image(image_name) for image_name in IMAGES]
    build_report(items)
    print(f"Relatorio gerado em: {REPORT_PATH}")
    print(f"Imagens geradas em: {VIS_DIR}")
    print(f"CSVs gerados em: {CSV_DIR}")


if __name__ == "__main__":
    run()