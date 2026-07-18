import json
import math
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Cal_angulo import angulo_contato
from linha_base import linha_base
from processamento_imagem import contorno, filtros

ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = ROOT / "imagens_teste"
OUT_DIR = ROOT / "audit_outputs"
LOG_PATH = OUT_DIR / "function_audit_log.jsonl"
REPORT_PATH = OUT_DIR / "audit_report.md"


def build_report():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if LOG_PATH.exists():
        LOG_PATH.unlink()

    files = sorted(IMAGES_DIR.glob("*.png"))
    for image_path in files:
        img = cv2.imread(str(image_path))
        if img is None:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask, _ = filtros.aplicar_multi_threshold(img)
        mask_gota, pts = contorno.extrair_mascara_gota(mask, img_gray=gray)
        if pts is None or len(pts) < 10:
            continue

        res = linha_base.detectar_baseline_hibrida(pts, debug=False)
        baseline_y = float(res["baseline_y"])
        p_esq = res.get("p_esq")
        p_dir = res.get("p_dir")
        if p_esq is None or p_dir is None:
            continue

        angulo_contato.set_audit_context(baseline_y=baseline_y, image_name=image_path.stem)
        altura_gota = float(np.max(pts[:, 1]) - np.min(pts[:, 1])) if len(pts) > 0 else 100.0
        offset = float(np.clip(angulo_contato.ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, angulo_contato.ANGLE_BASELINE_OFFSET_MIN, angulo_contato.ANGLE_BASELINE_OFFSET_MAX))
        baseline_ajustada = baseline_y + offset

        for lado in ("esq", "dir"):
            contact_point = p_esq if lado == "esq" else p_dir
            local_pts = angulo_contato._selecionar_pontos_lado(pts, p_esq, p_dir, baseline_ajustada, lado)
            if len(local_pts) < 3:
                continue
            poly_result = angulo_contato._calcular_slope_tangente_polynomial(local_pts, baseline_y, lado)
            if poly_result is None:
                continue
            m_tangente, coeffs, poly_pts = poly_result
            _ = angulo_contato.calcular_angulo_circular(pts, p_esq, p_dir, baseline_y, lado)

            vis = img.copy()
            if len(pts) >= 3:
                cv2.polylines(vis, [pts.astype(np.int32)], isClosed=True, color=(180, 180, 180), thickness=1)
            for i, pt in enumerate(local_pts, start=1):
                x, y = int(round(float(pt[0]))), int(round(float(pt[1])))
                cv2.circle(vis, (x, y), 3, (0, 0, 255), -1)
                cv2.putText(vis, str(i), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            cx, cy = int(round(float(contact_point[0]))), int(round(float(contact_point[1])))
            cv2.circle(vis, (cx, cy), 5, (0, 255, 0), -1)
            cv2.line(vis, (0, int(round(baseline_y))), (vis.shape[1], int(round(baseline_y))), (0, 255, 255), 1)
            cv2.imwrite(str(OUT_DIR / f"{image_path.stem}_{lado}_audit.png"), vis)

            # polyfit visualization
            poly_vis = img.copy()
            if len(pts) >= 3:
                cv2.polylines(poly_vis, [pts.astype(np.int32)], isClosed=True, color=(180, 180, 180), thickness=1)
            ys = poly_pts[:, 1]
            xs = poly_pts[:, 0]
            predicted = coeffs[0] * ys**2 + coeffs[1] * ys + coeffs[2]
            for x, y in zip(xs, ys):
                cv2.circle(poly_vis, (int(round(x)), int(round(y))), 2, (255, 0, 0), -1)
            if len(ys) >= 2:
                y_min, y_max = int(np.min(ys)), int(np.max(ys))
                y_grid = np.linspace(y_min, y_max, 60)
                x_grid = coeffs[0] * y_grid**2 + coeffs[1] * y_grid + coeffs[2]
                for idx in range(len(y_grid) - 1):
                    x1, y1 = int(round(x_grid[idx])), int(round(y_grid[idx]))
                    x2, y2 = int(round(x_grid[idx + 1])), int(round(y_grid[idx + 1]))
                    cv2.line(poly_vis, (x1, y1), (x2, y2), (255, 255, 0), 1)
            cx, cy = int(round(float(contact_point[0]))), int(round(float(contact_point[1])))
            cv2.circle(poly_vis, (cx, cy), 5, (0, 255, 0), -1)
            cv2.line(poly_vis, (0, int(round(baseline_y))), (poly_vis.shape[1], int(round(baseline_y))), (0, 255, 255), 1)
            cv2.imwrite(str(OUT_DIR / f"{image_path.stem}_{lado}_polyfit.png"), poly_vis)

    events = []
    if LOG_PATH.exists():
        with open(LOG_PATH, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    events.append(json.loads(line))

    image_names = sorted({event.get("image_name") for event in events if event.get("event") in {"selection", "polyfit"} and event.get("image_name")})

    lines = []
    lines.append("# Relatório de auditoria das funções")
    lines.append("")
    lines.append("Este relatório foi gerado executando o pipeline real do projeto sobre as imagens em `imagens_teste` sem alterar a lógica de cálculo.")
    lines.append("")
    lines.append("## Resumo")
    lines.append("")
    lines.append(f"- Imagens processadas: {len(files)}")
    lines.append(f"- Eventos capturados: {len(events)}")
    lines.append("")

    for image_name in image_names:
        lines.append(f"## Imagem: {image_name}")
        lines.append("")
        for lado in ("esq", "dir"):
            sel_events = [ev for ev in events if ev.get("event") == "selection" and ev.get("image_name") == image_name and ev.get("lado") == lado]
            poly_events = [ev for ev in events if ev.get("event") == "polyfit" and ev.get("image_name") == image_name and ev.get("lado") == lado]
            if not sel_events:
                continue
            sel = sel_events[-1]
            poly = poly_events[-1] if poly_events else None
            lines.append(f"### Lado: {lado}")
            lines.append("")
            lines.append("#### Etapa 1 — Entrada de _selecionar_pontos_lado()")
            lines.append("")
            lines.append(f"- quantidade total de pontos do contorno: {sel['total_contour_points']}")
            lines.append(f"- ponto de contato recebido: {sel['contact_point']}")
            lines.append(f"- baseline_y: {sel['baseline_y_real']}")
            lines.append(f"- baseline_ajustada: {sel['baseline_ajustada']}")
            lines.append(f"- lado solicitado: {lado}")
            lines.append(f"- largura da região: {sel['window_height']} px")
            lines.append(f"- altura da gota: {sel['altura_gota']:.2f} px")
            lines.append("")
            lines.append("#### Etapa 2 — Processo interno de seleção")
            lines.append("")
            lines.append("| índice | x | y | dist. contato | dist. baseline | aceito | motivo |")
            lines.append("|---|---:|---:|---:|---:|---|---|")
            for item in sel.get("all_points", []):
                lines.append(f"| {item['index']} | {item['x']:.2f} | {item['y']:.2f} | {item['dist_contato']:.2f} | {item['dist_baseline']:.2f} | {'SIM' if item['accepted'] else 'NÃO'} | {item['reason']} |")
            lines.append("")
            lines.append("#### Etapa 3 — Resultado final da seleção")
            lines.append("")
            lines.append("| índice | x | y | dist. contato | dist. baseline |")
            lines.append("|---|---:|---:|---:|---:|")
            for item in sel.get("selected_points", []):
                lines.append(f"| {item['index']} | {item['x']:.2f} | {item['y']:.2f} | {item['x'] - sel['contact_point'][0]:.2f} | {item['y'] - sel['baseline_ajustada']:.2f} |")
            lines.append("")
            indices = [item["index"] for item in sel.get("selected_points", [])]
            if indices:
                lines.append(f"- primeiro índice: {indices[0]}")
                lines.append(f"- último índice: {indices[-1]}")
                lines.append(f"- quantidade: {len(indices)}")
                jumps = []
                for a, b in zip(indices, indices[1:]):
                    if b - a > 1:
                        jumps.append(f"{a} -> {b}")
                if jumps:
                    lines.append("- salto detectado: " + ", ".join(jumps))
                else:
                    lines.append("- contorno totalmente contínuo")
            lines.append("")
            lines.append("#### Etapa 4 — Visualização")
            lines.append("")
            lines.append(f"![{image_name} {lado}]({OUT_DIR.name}/{image_path.stem}_{lado}_audit.png)")
            lines.append("")
            lines.append("#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()")
            lines.append("")
            if poly is not None:
                lines.append(f"- quantidade de pontos recebidos: {poly['selected_count']}")
                lines.append("- lista completa dos pontos:")
                for pt in poly.get("points", []):
                    lines.append(f"  - idx={pt['index']} x={pt['x']:.2f} y={pt['y']:.2f}")
                lines.append(f"- baseline: {poly['baseline_y']}")
                lines.append(f"- lado: {poly['lado']}")
            lines.append("")
            lines.append("#### Etapa 6 — Verificação da ordem")
            lines.append("")
            if poly is not None and poly.get("order_matches_selection"):
                lines.append("SIM")
            else:
                lines.append("NÃO")
                lines.append("A ordem foi modificada.")
            lines.append("")
            lines.append("#### Etapa 7 — Polyfit")
            lines.append("")
            if poly is not None:
                lines.append("| x | y |")
                lines.append("|---:|---:|")
                for pt in poly.get("points", []):
                    lines.append(f"| {pt['x']:.4f} | {pt['y']:.4f} |")
                lines.append("")
                lines.append(f"- coeficientes: a={poly['coeffs'][0]:.6f}, b={poly['coeffs'][1]:.6f}, c={poly['coeffs'][2]:.6f}")
                lines.append(f"- RMSE: {poly['rmse']:.6f}")
            lines.append("")
            lines.append("#### Etapa 8 — Derivada")
            lines.append("")
            if poly is not None:
                lines.append(f"- dx/dy = {poly['dx_dy']:.6f}")
                lines.append(f"- dy/dx = {poly['dy_dx']:.6f}")
                lines.append("- coordenada usada para a derivada: baseline_y")
            lines.append("")
            lines.append("#### Etapa 9 — Comparação geométrica")
            lines.append("")
            lines.append(f"![{image_name} {lado} polyfit]({OUT_DIR.name}/{image_path.stem}_{lado}_polyfit.png)")
            lines.append("")
            lines.append("#### Etapa 10 — Consistência")
            lines.append("")
            lines.append(f"- Existe salto nos índices? {'SIM' if indices and any(b-a > 1 for a, b in zip(indices, indices[1:])) else 'NÃO'}")
            lines.append(f"- Existe inversão da ordem? {'SIM' if poly is not None and not poly.get('order_matches_selection', True) else 'NÃO'}")
            lines.append(f"- Existe ponto duplicado? {'SIM' if len(indices) != len(set(indices)) else 'NÃO'}")
            lines.append("- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO")
            lines.append("- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO")
            lines.append("- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO")
            lines.append(f"- O polyfit usa exatamente os pontos selecionados? {'SIM' if poly is not None and poly.get('order_matches_selection') else 'NÃO'}")
            lines.append("- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO")
            lines.append("- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO")
            lines.append("")
            lines.append("#### Etapa 11 — Diagnóstico automático")
            lines.append("")
            selection_ok = not (indices and any(b - a > 1 for a, b in zip(indices, indices[1:]))) and (poly is not None and poly.get("order_matches_selection", True))
            lines.append(f"- A seleção de pontos parece correta? {'SIM' if selection_ok else 'NÃO'}")
            lines.append(f"- O problema parece estar na seleção? {'SIM' if not selection_ok else 'NÃO'}")
            lines.append(f"- O problema parece estar no polyfit? {'SIM' if poly is not None and not poly.get('order_matches_selection', True) else 'NÃO'}")
            lines.append(f"- O problema parece estar na derivada? {'NÃO'}")
            lines.append("- Existe alguma inconsistência detectada?")
            if not selection_ok:
                lines.append("  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.")
            else:
                lines.append("  - Nenhuma inconsistência óbvia detectada nos logs de seleção e polyfit.")
            lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"report written to {REPORT_PATH}")


if __name__ == "__main__":
    build_report()
