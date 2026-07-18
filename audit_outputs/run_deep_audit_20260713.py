import csv
import inspect
import math
import os
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Cal_angulo import angulo_contato
from linha_base import linha_base
from processamento_imagem import contorno, filtros


IMG_DIR = ROOT / "imagens_teste"
OUT_DIR = ROOT / "audit_outputs" / "deep_audit_20260713"
IMG_OUT = OUT_DIR / "visualizacoes"
CSV_OUT = OUT_DIR / "csv"

NAMES = ["30_geo.png", "50_geo.png", "75_geo.png", "100_geo.png", "130_geo.png"]
SIDES = ["esq", "dir"]


def fnum(v, nd=6):
    if v is None:
        return "None"
    try:
        vf = float(v)
    except Exception:
        return str(v)
    if math.isinf(vf):
        return "inf" if vf > 0 else "-inf"
    if math.isnan(vf):
        return "nan"
    return f"{vf:.{nd}f}"


def source_line(fn):
    try:
        return inspect.getsourcelines(fn)[1]
    except Exception:
        return None


SRC_LINES = {
    "_selecionar_pontos_lado": source_line(angulo_contato._selecionar_pontos_lado),
    "_selecionar_pontos_tangente": source_line(angulo_contato._selecionar_pontos_tangente),
    "_calcular_slope_tangente_polynomial": source_line(angulo_contato._calcular_slope_tangente_polynomial),
    "calcular_angulo_circular": source_line(angulo_contato.calcular_angulo_circular),
    "detect_baseline_tls": source_line(linha_base.detect_baseline_tls),
    "detectar_baseline_hibrida": source_line(linha_base.detectar_baseline_hibrida),
    "find_contact_points_by_extrapolation": source_line(linha_base.find_contact_points_by_extrapolation),
    "encontrar_contorno_gota_robusto": source_line(contorno.encontrar_contorno_gota_robusto),
}


def gerar_binario_analise(roi):
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    bin_mask, metodo = filtros.aplicar_multi_threshold(roi)
    mask_gota, pts = contorno.extrair_mascara_gota(bin_mask, img_gray=gray)
    q = contorno.avaliar_qualidade_contorno(pts, bin_mask.shape)
    return mask_gota, {
        "mask_source": metodo,
        "quality_score": float(q.get("score", 0.0)),
        "risk_flags": q.get("risk_flags", []),
    }


def run_initial_pipeline(raw_image):
    bin_img, analysis_meta = gerar_binario_analise(raw_image)
    gota_pts = contorno.encontrar_contorno_gota_robusto(bin_img)
    if gota_pts is None:
        gota_pts = contorno.encontrar_contorno_gota(bin_img)
    if gota_pts is None:
        raise RuntimeError("contorno nao detectado")

    res = linha_base.detectar_baseline_hibrida(gota_pts, debug=False)
    baseline_y = res["baseline_y"]
    baseline_line_params = res.get("line_params")
    p_esq = res.get("p_esq")
    p_dir = res.get("p_dir")

    try:
        baseline_ok = baseline_y is not None and np.isfinite(baseline_y)
    except Exception:
        baseline_ok = False

    if not baseline_ok or p_esq is None or p_dir is None:
        base_y, base_p_esq, base_p_dir = linha_base.encontrar_pontos_contato_base(gota_pts)
        if not baseline_ok:
            baseline_y = base_y
        if p_esq is None and base_p_esq is not None:
            p_esq = [float(base_p_esq[0]), float(base_p_esq[1])]
        if p_dir is None and base_p_dir is not None:
            p_dir = [float(base_p_dir[0]), float(base_p_dir[1])]

    if p_esq is None or p_dir is None:
        p_esq_fb, p_dir_fb = linha_base.encontrar_pontos_contato(gota_pts, baseline_y)
        if p_esq is None and p_esq_fb is not None:
            p_esq = [float(p_esq_fb[0]), float(p_esq_fb[1])]
        if p_dir is None and p_dir_fb is not None:
            p_dir = [float(p_dir_fb[0]), float(p_dir_fb[1])]

    if p_esq is not None:
        p_esq = [float(p_esq[0]), float(p_esq[1])]
    if p_dir is not None:
        p_dir = [float(p_dir[0]), float(p_dir[1])]

    floor_info = {}
    if gota_pts is not None:
        gray_raw = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
        _, thresh_bg = cv2.threshold(gray_raw, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        x_esq = max(0, int(np.min(gota_pts[:, 0])) - 5)
        x_dir = min(gray_raw.shape[1] - 1, int(np.max(gota_pts[:, 0])) + 5)
        meio_y = gray_raw.shape[0] // 2
        transicoes_esq = np.where(thresh_bg[meio_y:, x_esq] == 0)[0]
        transicoes_dir = np.where(thresh_bg[meio_y:, x_dir] == 0)[0]
        y_esq = (transicoes_esq[0] + meio_y) if len(transicoes_esq) > 0 else baseline_y
        y_dir = (transicoes_dir[0] + meio_y) if len(transicoes_dir) > 0 else baseline_y
        chao_real = float(max(y_esq, y_dir))
        floor_info = {
            "x_esq": int(x_esq),
            "x_dir": int(x_dir),
            "meio_y": int(meio_y),
            "y_esq": float(y_esq),
            "y_dir": float(y_dir),
            "chao_real": float(chao_real),
            "baseline_before_floor_lock": float(baseline_y),
            "changed": bool(chao_real > baseline_y),
        }
        if chao_real > baseline_y:
            baseline_y = chao_real

    anchor_info = {}
    if gota_pts is not None and baseline_y is not None:
        meio_x = float(np.mean(gota_pts[:, 0]))
        h_gota = float(np.max(gota_pts[:, 1]) - np.min(gota_pts[:, 1]))
        y_max_contorno = float(np.max(gota_pts[:, 1]))
        y_limite_inf = y_max_contorno - (0.03 * h_gota)
        y_limite_sup = y_max_contorno - (0.30 * h_gota)

        lado_esq_completo = gota_pts[gota_pts[:, 0] < meio_x]
        lado_dir_completo = gota_pts[gota_pts[:, 0] >= meio_x]
        pts_esq_saudavel = gota_pts[
            (gota_pts[:, 0] < meio_x)
            & (gota_pts[:, 1] >= y_limite_sup)
            & (gota_pts[:, 1] <= y_limite_inf)
        ]
        pts_dir_saudavel = gota_pts[
            (gota_pts[:, 0] >= meio_x)
            & (gota_pts[:, 1] >= y_limite_sup)
            & (gota_pts[:, 1] <= y_limite_inf)
        ]

        def ancorar(pts_parede, pts_completo, y_chao):
            if len(pts_parede) < 5:
                idx_local = int(np.argmax(pts_completo[:, 1]))
                return pts_completo[idx_local], None, None
            poly = np.polyfit(pts_parede[:, 1], pts_parede[:, 0], 2)
            x_teorico = float(np.polyval(poly, y_chao))
            distancias = np.hypot(pts_completo[:, 0] - x_teorico, pts_completo[:, 1] - y_chao)
            idx_local = int(np.argmin(distancias))
            return pts_completo[idx_local], poly, x_teorico

        anchor_info = {
            "meio_x": meio_x,
            "h_gota": h_gota,
            "y_max_contorno": y_max_contorno,
            "y_limite_inf": float(y_limite_inf),
            "y_limite_sup": float(y_limite_sup),
            "n_esq_completo": int(len(lado_esq_completo)),
            "n_dir_completo": int(len(lado_dir_completo)),
            "n_esq_saudavel": int(len(pts_esq_saudavel)),
            "n_dir_saudavel": int(len(pts_dir_saudavel)),
            "p_before_anchor_esq": p_esq,
            "p_before_anchor_dir": p_dir,
        }

        if len(lado_esq_completo) > 0:
            p_ideal_esq, poly_esq, x_teorico_esq = ancorar(pts_esq_saudavel, lado_esq_completo, baseline_y)
            p_esq = [float(p_ideal_esq[0]), float(p_ideal_esq[1])]
            anchor_info["x_teorico_esq"] = x_teorico_esq
            anchor_info["poly_esq"] = None if poly_esq is None else [float(x) for x in poly_esq]
        if len(lado_dir_completo) > 0:
            p_ideal_dir, poly_dir, x_teorico_dir = ancorar(pts_dir_saudavel, lado_dir_completo, baseline_y)
            p_dir = [float(p_ideal_dir[0]), float(p_ideal_dir[1])]
            anchor_info["x_teorico_dir"] = x_teorico_dir
            anchor_info["poly_dir"] = None if poly_dir is None else [float(x) for x in poly_dir]

    if baseline_line_params is not None:
        vx, vy, x0, _ = baseline_line_params
        baseline_line_params = (vx, vy, x0, baseline_y)

    return {
        "raw_image": raw_image,
        "bin_img": bin_img,
        "analysis_meta": analysis_meta,
        "gota_pts": gota_pts,
        "baseline_y": float(baseline_y),
        "baseline_line_params": baseline_line_params,
        "p_esq": p_esq,
        "p_dir": p_dir,
        "baseline_method": res.get("method"),
        "contact_method": res.get("contact_method"),
        "floor_info": floor_info,
        "anchor_info": anchor_info,
    }


def point_indices_for_point(pts, p):
    if p is None or pts is None or len(pts) == 0:
        return None, None
    d = np.hypot(pts[:, 0] - float(p[0]), pts[:, 1] - float(p[1]))
    idx = int(np.argmin(d))
    return idx, float(d[idx])


def selecionar_lado_audit(pts, p_esq, p_dir, baseline_y, lado):
    altura_gota = float(np.max(pts[:, 1]) - np.min(pts[:, 1])) if len(pts) > 0 else 100.0
    offset_calibracao = float(
        np.clip(
            angulo_contato.ANGLE_BASELINE_OFFSET_FACTOR * altura_gota,
            angulo_contato.ANGLE_BASELINE_OFFSET_MIN,
            angulo_contato.ANGLE_BASELINE_OFFSET_MAX,
        )
    )
    baseline_ajustada = baseline_y + offset_calibracao
    window_height = int(
        np.clip(
            angulo_contato.ANGLE_WINDOW_HEIGHT_FACTOR * altura_gota,
            angulo_contato.ANGLE_WINDOW_HEIGHT_MIN,
            angulo_contato.ANGLE_WINDOW_HEIGHT_MAX,
        )
    )
    center_x_approx = float((p_esq[0] + p_dir[0]) / 2.0)
    contact = p_esq if lado == "esq" else p_dir
    contact_idx, contact_dist = point_indices_for_point(pts, contact)

    vertical_mask = (pts[:, 1] <= baseline_ajustada) & (pts[:, 1] > baseline_ajustada - window_height)
    if lado == "esq":
        side_mask = pts[:, 0] < center_x_approx
    else:
        side_mask = pts[:, 0] > center_x_approx
    final_mask = vertical_mask & side_mask
    final_indices = np.where(final_mask)[0]
    local_pts = pts[final_indices]

    actual = angulo_contato._selecionar_pontos_lado(pts, p_esq, p_dir, baseline_ajustada, lado)
    actual_matches = len(actual) == len(local_pts) and (len(actual) == 0 or np.allclose(actual, local_pts))

    rows = []
    for i, (x, y) in enumerate(pts):
        in_vertical = bool(vertical_mask[i])
        in_side = bool(side_mask[i])
        kept = bool(final_mask[i])
        reasons = []
        if not in_vertical:
            if y > baseline_ajustada:
                reasons.append("abaixo_baseline_ajustada")
            if y <= baseline_ajustada - window_height:
                reasons.append("acima_janela_permitida")
        if not in_side:
            reasons.append("lado_errado")
        rows.append({
            "indice": int(i),
            "x": float(x),
            "y": float(y),
            "dist_baseline": float(baseline_y - y),
            "dist_baseline_ajustada": float(baseline_ajustada - y),
            "dist_ponto_contato": float(math.hypot(float(x) - contact[0], float(y) - contact[1])),
            "lado_correto": in_side,
            "candidato_janela": in_vertical,
            "permaneceu": kept,
            "descartado": not kept,
            "motivo_descarte": "mantido" if kept else ";".join(reasons),
        })

    diffs = np.diff(final_indices).astype(int).tolist() if len(final_indices) >= 2 else []
    breaks = []
    for pos, diff in enumerate(diffs):
        if diff != 1:
            breaks.append({
                "ordem": int(pos),
                "indice_anterior": int(final_indices[pos]),
                "indice_seguinte": int(final_indices[pos + 1]),
                "diferenca": int(diff),
            })

    return {
        "lado": lado,
        "altura_gota": altura_gota,
        "offset_calibracao": offset_calibracao,
        "baseline_y": baseline_y,
        "baseline_ajustada": baseline_ajustada,
        "window_height": window_height,
        "center_x_approx": center_x_approx,
        "contact_point": contact,
        "contact_idx": contact_idx,
        "contact_dist": contact_dist,
        "rows": rows,
        "final_indices": final_indices.astype(int).tolist(),
        "local_pts": local_pts,
        "actual_matches": actual_matches,
        "diffs": diffs,
        "breaks": breaks,
        "consecutive": len(breaks) == 0,
    }


def slope_audit(sel):
    local_pts = sel["local_pts"]
    baseline_y = sel["baseline_y"]
    lado = sel["lado"]
    local_indices = np.array(sel["final_indices"], dtype=int)
    if local_pts is None or len(local_pts) < 3:
        return {"status": "sem_pontos_suficientes", "poly_indices": [], "poly_pts": np.empty((0, 2))}

    dist = baseline_y - local_pts[:, 1]
    tangent_mask = (dist >= 0.0) & (dist <= 30.0)
    tangent_pts_initial = local_pts[tangent_mask]
    tangent_indices_initial = local_indices[tangent_mask]
    tangent_order_initial = np.where(tangent_mask)[0]

    used_fallback_to_local = False
    if len(tangent_pts_initial) == 0:
        selected_pts = np.empty((0, 2), dtype=float)
        selected_indices = np.array([], dtype=int)
        selected_local_order = np.array([], dtype=int)
    else:
        sort = np.argsort(dist[tangent_mask])
        sort = sort[:min(12, len(sort))]
        selected_pts = tangent_pts_initial[sort]
        selected_indices = tangent_indices_initial[sort]
        selected_local_order = tangent_order_initial[sort]

    if len(selected_pts) < 4:
        selected_pts = local_pts
        selected_indices = local_indices
        selected_local_order = np.arange(len(local_pts))
        used_fallback_to_local = True

    if len(selected_pts) < 3:
        return {
            "status": "sem_pontos_suficientes_para_polyfit",
            "used_fallback_to_local": used_fallback_to_local,
            "poly_indices": selected_indices.astype(int).tolist(),
            "poly_pts": selected_pts,
        }

    ys = selected_pts[:, 1]
    xs = selected_pts[:, 0]
    if np.std(ys) < 1e-6 or np.std(xs) < 1e-6:
        return {
            "status": "std_zero",
            "used_fallback_to_local": used_fallback_to_local,
            "std_x": float(np.std(xs)),
            "std_y": float(np.std(ys)),
            "poly_indices": selected_indices.astype(int).tolist(),
            "poly_pts": selected_pts,
            "poly_order": selected_local_order.astype(int).tolist(),
        }

    coeffs = np.polyfit(ys, xs, 2)
    pred = np.polyval(coeffs, ys)
    residuals = xs - pred
    abs_err = np.abs(residuals)
    rmse = float(np.sqrt(np.mean(residuals ** 2)))
    sse = float(np.sum(residuals ** 2))
    sst = float(np.sum((xs - np.mean(xs)) ** 2))
    r2 = float(1.0 - sse / sst) if sst > 1e-12 else float("nan")
    max_err = float(np.max(abs_err)) if len(abs_err) else 0.0
    mean_err = float(np.mean(abs_err)) if len(abs_err) else 0.0
    a, b, c = [float(v) for v in coeffs]
    dx_dy = float(2.0 * a * baseline_y + b)
    if not np.isfinite(dx_dy):
        m_tangente = float("nan")
    elif abs(dx_dy) < 1e-9:
        m_tangente = float("inf")
    else:
        m_tangente = float(1.0 / dx_dy)
    dy_dx = m_tangente
    angulo_bruto = float(math.degrees(math.atan(abs(m_tangente)))) if np.isfinite(m_tangente) else 90.0
    angulo_normalizado = float(np.clip(angulo_bruto, 0.0, 180.0))
    angulo_externo = 180.0 - angulo_normalizado
    angulo_interno = angulo_normalizado

    return {
        "status": "ok",
        "used_fallback_to_local": used_fallback_to_local,
        "tangent_initial_indices": tangent_indices_initial.astype(int).tolist(),
        "poly_indices": selected_indices.astype(int).tolist(),
        "poly_order": selected_local_order.astype(int).tolist(),
        "poly_pts": selected_pts,
        "coeffs": [a, b, c],
        "rmse": rmse,
        "r2": r2,
        "max_err": max_err,
        "mean_err": mean_err,
        "errors": [
            {
                "ordem": int(k),
                "indice": int(selected_indices[k]),
                "x": float(selected_pts[k, 0]),
                "y": float(selected_pts[k, 1]),
                "x_pred": float(pred[k]),
                "erro": float(residuals[k]),
                "erro_abs": float(abs_err[k]),
            }
            for k in range(len(selected_pts))
        ],
        "dx_dy": dx_dy,
        "dy_dx": dy_dx,
        "m_tangente": m_tangente,
        "angulo_bruto": angulo_bruto,
        "angulo_normalizado": angulo_normalizado,
        "angulo_externo": angulo_externo,
        "angulo_interno": angulo_interno,
    }


def circular_context(pts, sel, slope):
    local_pts = sel["local_pts"]
    if len(local_pts) < 3:
        return {"status": "sem_pontos"}
    mean_xy = np.mean(local_pts, axis=0)
    centered = local_pts.astype(np.float64) - mean_xy
    try:
        xc0, yc0, r0 = angulo_contato.ajustar_circulo_algebrico(centered)
    except Exception as e:
        return {"status": f"erro_circular_inicial:{e}"}
    dists = np.hypot(centered[:, 0] - xc0, centered[:, 1] - yc0)
    residuals = np.abs(dists - r0)
    sigma = float(np.std(residuals))
    if sigma > 0:
        inliers = residuals <= (angulo_contato.ANGLE_OUTLIER_SIGMA_SCALE * sigma)
        filtered = centered[inliers]
    else:
        inliers = np.ones(len(centered), dtype=bool)
        filtered = centered
    if len(filtered) < 3:
        return {"status": "menos_de_3_inliers", "sigma": sigma}
    try:
        xc, yc, r = angulo_contato.ajustar_circulo_algebrico(filtered)
    except Exception as e:
        return {"status": f"erro_circular_final:{e}", "sigma": sigma}
    xc += mean_xy[0]
    yc += mean_xy[1]
    baseline_y = sel["baseline_y"]
    dy = baseline_y - yc
    circle_baseline_outside = bool(abs(dy) >= r)
    x_contact = float(sel["contact_point"][0])
    y_line_at_xc = None
    theta_adjusted = None
    if slope.get("status") == "ok":
        m = slope["m_tangente"]
        y_line_at_xc = float(baseline_y + m * (xc - x_contact)) if np.isfinite(m) else float("inf")
        theta_adjusted = float(slope["angulo_bruto"])
        if yc > y_line_at_xc:
            theta_adjusted = 180.0 - theta_adjusted
    return {
        "status": "ok",
        "mean_x": float(mean_xy[0]),
        "mean_y": float(mean_xy[1]),
        "xc": float(xc),
        "yc": float(yc),
        "R": float(r),
        "dy_baseline": float(dy),
        "circle_baseline_outside": circle_baseline_outside,
        "sigma": sigma,
        "n_inliers": int(np.count_nonzero(inliers)),
        "y_line_at_xc": y_line_at_xc,
        "theta_after_circle_internal_rule": theta_adjusted,
    }


def verificacoes(pts, sel, slope):
    problems = []
    rows = sel["rows"]
    final_idx = sel["final_indices"]
    poly_idx = slope.get("poly_indices", [])
    baseline_y = sel["baseline_y"]
    baseline_adj = sel["baseline_ajustada"]
    window_height = sel["window_height"]
    center = sel["center_x_approx"]
    lado = sel["lado"]

    seen = {}
    for i, p in enumerate(pts):
        key = (float(p[0]), float(p[1]))
        if key in seen:
            problems.append({
                "tipo": "ponto_repetido",
                "indice": int(i),
                "ponto": key,
                "onde": f"tambem aparece no indice {seen[key]}",
                "porque": "mesmas coordenadas x,y no contorno",
            })
        else:
            seen[key] = i

    for b in sel["breaks"]:
        problems.append({
            "tipo": "indices_nao_consecutivos",
            "indice": b["indice_seguinte"],
            "ponto": tuple(map(float, pts[b["indice_seguinte"]])),
            "onde": f"entre {b['indice_anterior']} e {b['indice_seguinte']}",
            "porque": f"diferenca de indice = {b['diferenca']}",
        })

    if len(final_idx) < 3:
        problems.append({
            "tipo": "poucos_pontos",
            "indice": None,
            "ponto": None,
            "onde": "_selecionar_pontos_lado",
            "porque": f"numero final de pontos = {len(final_idx)}",
        })

    if len(poly_idx) < 4:
        problems.append({
            "tipo": "poucos_pontos_polyfit",
            "indice": None,
            "ponto": None,
            "onde": "_calcular_slope_tangente_polynomial",
            "porque": f"numero de pontos no polyfit = {len(poly_idx)}",
        })

    for i in final_idx:
        x, y = pts[i]
        if lado == "esq" and not (x < center):
            problems.append({"tipo": "ponto_lado_errado", "indice": int(i), "ponto": (float(x), float(y)), "onde": "_selecionar_pontos_lado", "porque": "x nao e menor que center_x_approx"})
        if lado == "dir" and not (x > center):
            problems.append({"tipo": "ponto_lado_errado", "indice": int(i), "ponto": (float(x), float(y)), "onde": "_selecionar_pontos_lado", "porque": "x nao e maior que center_x_approx"})
        if y <= baseline_adj - window_height:
            problems.append({"tipo": "ponto_acima_regiao_permitida", "indice": int(i), "ponto": (float(x), float(y)), "onde": "_selecionar_pontos_lado", "porque": "y <= baseline_ajustada - window_height"})
        if y > baseline_adj:
            problems.append({"tipo": "ponto_abaixo_baseline_ajustada", "indice": int(i), "ponto": (float(x), float(y)), "onde": "_selecionar_pontos_lado", "porque": "y > baseline_ajustada"})
        if y > baseline_y:
            problems.append({"tipo": "ponto_abaixo_baseline_fisica", "indice": int(i), "ponto": (float(x), float(y)), "onde": "_calcular_slope_tangente_polynomial/entrada", "porque": "y > baseline_y"})
        if abs(baseline_y - y) > 30 and i in poly_idx:
            problems.append({"tipo": "ponto_polyfit_distante_baseline", "indice": int(i), "ponto": (float(x), float(y)), "onde": "_calcular_slope_tangente_polynomial", "porque": f"distancia baseline = {baseline_y - y:.3f}"})

    if len(final_idx) >= 3:
        idx_arr = np.array(final_idx, dtype=int)
        diffs = np.diff(idx_arr)
        signs = np.sign(diffs[diffs != 0])
        if len(signs) and np.any(signs != signs[0]):
            problems.append({
                "tipo": "ordem_incorreta_ou_invertida",
                "indice": int(idx_arr[0]),
                "ponto": tuple(map(float, pts[idx_arr[0]])),
                "onde": "_selecionar_pontos_lado",
                "porque": "diferencas de indices mudam de sinal",
            })
        jumps = np.where(np.abs(diffs) > 1)[0]
        if len(jumps) > 0:
            problems.append({
                "tipo": "saltos_no_trecho",
                "indice": int(idx_arr[jumps[0] + 1]),
                "ponto": tuple(map(float, pts[idx_arr[jumps[0] + 1]])),
                "onde": "continuidade_do_contorno",
                "porque": f"primeiro salto {int(idx_arr[jumps[0]])}->{int(idx_arr[jumps[0]+1])}",
            })

    selected_rows = [rows[i] for i in range(len(rows)) if rows[i]["permaneceu"]]
    for r in selected_rows:
        if r["dist_ponto_contato"] > max(60.0, 0.35 * (np.max(pts[:, 0]) - np.min(pts[:, 0]))):
            problems.append({
                "tipo": "ponto_muito_afastado_do_ponto_de_contato",
                "indice": r["indice"],
                "ponto": (r["x"], r["y"]),
                "onde": "_selecionar_pontos_lado",
                "porque": f"distancia ao contato = {r['dist_ponto_contato']:.3f}",
            })

    return problems


def write_csv(path, fieldnames, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def draw_audit_image(base_img, pts, sel, slope, out_path):
    img = base_img.copy()
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    overlay = img.copy()

    all_pts = pts.astype(np.int32).reshape(-1, 1, 2)
    cv2.polylines(overlay, [all_pts], True, (150, 150, 150), 1)
    h, w = img.shape[:2]
    yb = int(round(sel["baseline_y"]))
    yba = int(round(sel["baseline_ajustada"]))
    cv2.line(overlay, (0, yb), (w - 1, yb), (0, 255, 255), 1)
    cv2.line(overlay, (0, yba), (w - 1, yba), (255, 255, 0), 1)

    final_set = set(sel["final_indices"])
    poly_set = set(slope.get("poly_indices", []))
    vertical_set = {r["indice"] for r in sel["rows"] if r["candidato_janela"]}

    for i in vertical_set:
        x, y = pts[i]
        cv2.circle(overlay, (int(x), int(y)), 2, (0, 0, 255), -1)
    for i in vertical_set - final_set:
        x, y = pts[i]
        cv2.circle(overlay, (int(x), int(y)), 3, (0, 165, 255), -1)
    for i in final_set:
        x, y = pts[i]
        cv2.circle(overlay, (int(x), int(y)), 2, (0, 0, 255), -1)
    for order, i in enumerate(slope.get("poly_indices", [])):
        x, y = pts[i]
        cv2.circle(overlay, (int(x), int(y)), 4, (255, 0, 0), -1)
        cv2.putText(overlay, str(order), (int(x) + 3, int(y) - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1, cv2.LINE_AA)

    cp = sel["contact_point"]
    cv2.circle(overlay, (int(round(cp[0])), int(round(cp[1]))), 6, (0, 255, 0), -1)

    # Number contour indices sparsely plus all selected/polyfit indices.
    label_indices = set(range(0, len(pts), max(1, len(pts) // 80))) | final_set | poly_set
    for i in sorted(label_indices):
        x, y = pts[i]
        cv2.putText(overlay, str(i), (int(x) + 2, int(y) + 2), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (220, 220, 220), 1, cv2.LINE_AA)

    if slope.get("status") == "ok":
        a, b, c = slope["coeffs"]
        ys = np.linspace(min(pts[:, 1]), max(pts[:, 1]), 240)
        curve = []
        for y in ys:
            x = a * y * y + b * y + c
            if -w <= x <= 2 * w and -h <= y <= 2 * h:
                curve.append([int(round(x)), int(round(y))])
        if len(curve) >= 2:
            cv2.polylines(overlay, [np.array(curve, dtype=np.int32).reshape(-1, 1, 2)], False, (255, 0, 255), 1)

        m = slope["m_tangente"]
        x0, y0 = cp
        length = max(40.0, 0.15 * w)
        if np.isfinite(m):
            dx = length / math.sqrt(1 + m * m)
            dy = m * dx
        else:
            dx, dy = 0.0, length
        cv2.line(
            overlay,
            (int(round(x0 - dx)), int(round(y0 - dy))),
            (int(round(x0 + dx)), int(round(y0 + dy))),
            (0, 255, 0),
            2,
        )

    cv2.putText(overlay, "contorno cinza | contato verde | baseline amarelo | baseline ajustada ciano", (8, 16), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(overlay, "candidatos vermelho | descartados laranja | polyfit azul | curva magenta", (8, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imwrite(str(out_path), overlay)


def audit_image(name):
    path = IMG_DIR / name
    img = cv2.imread(str(path))
    if img is None:
        raise RuntimeError(f"falha ao abrir {path}")
    state = run_initial_pipeline(img)
    pts = state["gota_pts"]
    result = {"name": name, "state": state, "sides": {}}
    for lado in SIDES:
        sel = selecionar_lado_audit(pts, state["p_esq"], state["p_dir"], state["baseline_y"], lado)
        slope = slope_audit(sel)
        circ = circular_context(pts, sel, slope)
        probs = verificacoes(pts, sel, slope)
        result["sides"][lado] = {"sel": sel, "slope": slope, "circ": circ, "problems": probs}

        stem = Path(name).stem
        write_csv(
            CSV_OUT / f"{stem}_{lado}_todos_pontos.csv",
            ["indice", "x", "y", "dist_baseline", "dist_baseline_ajustada", "dist_ponto_contato", "lado_correto", "candidato_janela", "permaneceu", "descartado", "motivo_descarte"],
            sel["rows"],
        )
        if slope.get("errors"):
            write_csv(
                CSV_OUT / f"{stem}_{lado}_polyfit_erros.csv",
                ["ordem", "indice", "x", "y", "x_pred", "erro", "erro_abs"],
                slope["errors"],
            )
        else:
            write_csv(CSV_OUT / f"{stem}_{lado}_polyfit_erros.csv", ["ordem", "indice", "x", "y", "x_pred", "erro", "erro_abs"], [])
        draw_audit_image(img, pts, sel, slope, IMG_OUT / f"{stem}_{lado}_audit.png")
    return result


def md_table_points(rows):
    lines = ["| indice | x | y | dist baseline | dist contato | lado correto | descartado | motivo |",
             "|---:|---:|---:|---:|---:|:---:|:---:|---|"]
    for r in rows:
        lines.append(
            f"| {r['indice']} | {fnum(r['x'],3)} | {fnum(r['y'],3)} | {fnum(r['dist_baseline'],3)} | {fnum(r['dist_ponto_contato'],3)} | {r['lado_correto']} | {r['descartado']} | {r['motivo_descarte']} |"
        )
    return "\n".join(lines)


def build_report(results):
    lines = []
    lines.append("# Auditoria detalhada das funcoes de selecao e tangente")
    lines.append("")
    lines.append("Escopo: pipeline atual do programa, sem alteracao de algoritmo.")
    lines.append("")
    lines.append("## Linhas de codigo observadas")
    for k, v in SRC_LINES.items():
        lines.append(f"- `{k}` inicia na linha `{v}`.")
    lines.append("")
    lines.append("## Formulas registradas")
    lines.append("- `altura_gota = max(y) - min(y)`")
    lines.append("- `offset_calibracao = clip(ANGLE_BASELINE_OFFSET_FACTOR * altura_gota, ANGLE_BASELINE_OFFSET_MIN, ANGLE_BASELINE_OFFSET_MAX)`")
    lines.append("- `baseline_ajustada = baseline_y + offset_calibracao`")
    lines.append("- `window_height = int(clip(ANGLE_WINDOW_HEIGHT_FACTOR * altura_gota, ANGLE_WINDOW_HEIGHT_MIN, ANGLE_WINDOW_HEIGHT_MAX))`")
    lines.append("- `_selecionar_pontos_lado`: `mask = (y <= baseline_ajustada) & (y > baseline_ajustada - window_height)`")
    lines.append("- lado esquerdo: `x < center_x_approx`; lado direito: `x > center_x_approx`")
    lines.append("- `_selecionar_pontos_tangente`: `distance_from_baseline = baseline_y - y`; `0 <= distance <= 30`; ordena por menor distancia e usa ate 12 pontos")
    lines.append("- `_calcular_slope_tangente_polynomial`: `x = a*y^2 + b*y + c`; `dx/dy = 2*a*baseline_y + b`; `dy/dx = 1/(dx/dy)`")
    lines.append("- angulo bruto: `degrees(atan(abs(dy/dx)))`; angulo externo tabulado: `180 - angulo_bruto`; angulo interno tabulado: `angulo_bruto`")
    lines.append("")

    conclusions = []
    for res in results:
        name = res["name"]
        st = res["state"]
        pts = st["gota_pts"]
        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"- Dimensao imagem: `{st['raw_image'].shape[1]} x {st['raw_image'].shape[0]}`")
        lines.append(f"- Mascara: `{st['analysis_meta'].get('mask_source')}`; qualidade: `{fnum(st['analysis_meta'].get('quality_score'),4)}`; flags: `{st['analysis_meta'].get('risk_flags')}`")
        lines.append(f"- Numero de pontos no contorno: `{len(pts)}`")
        lines.append(f"- Baseline final: `{fnum(st['baseline_y'],6)}`")
        lines.append(f"- Ponto contato esquerdo: `{st['p_esq']}`")
        lines.append(f"- Ponto contato direito: `{st['p_dir']}`")
        lines.append(f"- Metodo baseline: `{st['baseline_method']}`; metodo contato: `{st['contact_method']}`")
        lines.append(f"- Trava absoluta no chao: `{st['floor_info']}`")
        lines.append(f"- Ancora matematica: `{st['anchor_info']}`")
        lines.append("")

        image_has_selection_issue = False
        image_has_poly_issue = False
        math_issue = False
        geom_issue = False
        first_origin = None

        for lado in SIDES:
            side = res["sides"][lado]
            sel = side["sel"]
            slope = side["slope"]
            circ = side["circ"]
            probs = side["problems"]
            side_name = "esquerdo" if lado == "esq" else "direito"
            lines.append(f"### Lado {side_name}")
            lines.append("")
            lines.append("#### PARTE 1 - _selecionar_pontos_lado()")
            lines.append(f"- Indice do ponto de contato: `{sel['contact_idx']}`; distancia ate ponto real: `{fnum(sel['contact_dist'],6)}`")
            lines.append(f"- baseline_y: `{fnum(sel['baseline_y'],6)}`")
            lines.append(f"- baseline_ajustada: `{fnum(sel['baseline_ajustada'],6)}`")
            lines.append(f"- Parametros: altura_gota=`{fnum(sel['altura_gota'],6)}`, offset_calibracao=`{fnum(sel['offset_calibracao'],6)}`, window_height=`{sel['window_height']}`, center_x_approx=`{fnum(sel['center_x_approx'],6)}`, lado=`{lado}`")
            lines.append(f"- Saida igual a funcao real importada: `{sel['actual_matches']}`")
            lines.append("")
            lines.append("Todos os pontos candidatos antes dos filtros, com decisao final:")
            lines.append(md_table_points(sel["rows"]))
            lines.append("")
            lines.append("Pontos que permaneceram:")
            lines.append(", ".join(map(str, sel["final_indices"])) if sel["final_indices"] else "nenhum")
            lines.append("")
            lines.append(f"- Numero final de pontos: `{len(sel['final_indices'])}`")
            lines.append(f"- Primeiro indice: `{sel['final_indices'][0] if sel['final_indices'] else None}`")
            lines.append(f"- Ultimo indice: `{sel['final_indices'][-1] if sel['final_indices'] else None}`")
            lines.append(f"- Indices consecutivos: `{'SIM' if sel['consecutive'] else 'NAO'}`")
            if sel["breaks"]:
                lines.append("- Quebras:")
                for b in sel["breaks"]:
                    lines.append(f"  - entre `{b['indice_anterior']}` e `{b['indice_seguinte']}`; diferenca `{b['diferenca']}`")
            lines.append("")

            lines.append("#### PARTE 2 - continuidade do contorno")
            lines.append(f"- Diferencas entre indices consecutivos: `{sel['diffs']}`")
            jumps = [d for d in sel["diffs"] if d != 1]
            lines.append(f"- Existencia de saltos: `{'SIM' if jumps else 'NAO'}`")
            lines.append(f"- Existencia de wrap-around: `{'SIM' if any(d < 0 for d in sel['diffs']) else 'NAO'}`")
            y_vals = [sel["rows"][i]["y"] for i in range(len(sel["rows"])) if sel["rows"][i]["permaneceu"]]
            mix_top_base = bool(y_vals and (max(y_vals) - min(y_vals) > 0.60 * sel["altura_gota"]))
            lines.append(f"- Existencia de mistura entre topo e base da gota: `{'SIM' if mix_top_base else 'NAO'}`")
            lines.append("")

            lines.append("#### PARTE 3 - _calcular_slope_tangente_polynomial()")
            lines.append(f"- Status: `{slope.get('status')}`")
            lines.append(f"- Usou fallback para todos os local_pts: `{slope.get('used_fallback_to_local')}`")
            lines.append("Pontos que entram no polyfit:")
            lines.append("| ordem | indice | x | y |")
            lines.append("|---:|---:|---:|---:|")
            poly_pts = slope.get("poly_pts", np.empty((0, 2)))
            poly_indices = slope.get("poly_indices", [])
            for k, idx in enumerate(poly_indices):
                x, y = poly_pts[k]
                lines.append(f"| {k} | {idx} | {fnum(x,3)} | {fnum(y,3)} |")
            if slope.get("status") == "ok":
                lines.append(f"- Coeficientes `[a,b,c]`: `{[fnum(v,12) for v in slope['coeffs']]}`")
                lines.append(f"- RMSE: `{fnum(slope['rmse'],9)}`")
                lines.append(f"- R2: `{fnum(slope['r2'],9)}`")
                lines.append(f"- Erro maximo: `{fnum(slope['max_err'],9)}`")
                lines.append(f"- Erro medio absoluto: `{fnum(slope['mean_err'],9)}`")
                lines.append("Erro em cada ponto:")
                lines.append("| ordem | indice | x | y | x_pred | erro | erro_abs |")
                lines.append("|---:|---:|---:|---:|---:|---:|---:|")
                for e in slope["errors"]:
                    lines.append(f"| {e['ordem']} | {e['indice']} | {fnum(e['x'],3)} | {fnum(e['y'],3)} | {fnum(e['x_pred'],6)} | {fnum(e['erro'],6)} | {fnum(e['erro_abs'],6)} |")
            lines.append("")

            lines.append("#### PARTE 4 - derivada")
            if slope.get("status") == "ok":
                lines.append(f"- dx/dy: `{fnum(slope['dx_dy'],12)}`")
                lines.append(f"- dy/dx: `{fnum(slope['dy_dx'],12)}`")
                lines.append(f"- inclinacao da tangente: `{fnum(slope['m_tangente'],12)}`")
                lines.append(f"- angulo bruto: `{fnum(slope['angulo_bruto'],9)}`")
                lines.append(f"- angulo apos normalizacao: `{fnum(slope['angulo_normalizado'],9)}`")
                lines.append(f"- angulo externo: `{fnum(slope['angulo_externo'],9)}`")
                lines.append(f"- angulo interno: `{fnum(slope['angulo_interno'],9)}`")
            else:
                lines.append("- Derivada nao calculada pela funcao: slope_result = None.")
            lines.append(f"- Contexto circular usado por `calcular_angulo_circular`: `{circ}`")
            lines.append("")

            lines.append("#### PARTE 5 - visualizacao")
            stem = Path(name).stem
            lines.append(f"- Imagem anotada: `audit_outputs/deep_audit_20260713/visualizacoes/{stem}_{lado}_audit.png`")
            lines.append(f"- CSV todos os pontos: `audit_outputs/deep_audit_20260713/csv/{stem}_{lado}_todos_pontos.csv`")
            lines.append(f"- CSV erros polyfit: `audit_outputs/deep_audit_20260713/csv/{stem}_{lado}_polyfit_erros.csv`")
            lines.append("")

            lines.append("#### PARTE 6 - verificacoes")
            if probs:
                for p in probs:
                    lines.append(f"- `{p['tipo']}` | onde: `{p['onde']}` | indice: `{p['indice']}` | ponto: `{p['ponto']}` | porque: `{p['porque']}`")
            else:
                lines.append("- Nenhum problema automatico registrado.")
            lines.append("")

            if sel["breaks"] or len(sel["final_indices"]) < 3:
                image_has_selection_issue = True
                geom_issue = True
                first_origin = first_origin or "Cal_angulo/angulo_contato.py:231"
            if slope.get("status") != "ok" or len(poly_indices) < 4:
                image_has_poly_issue = True
                math_issue = True
                first_origin = first_origin or "Cal_angulo/angulo_contato.py:95"
            if any(p["tipo"] in {"ponto_abaixo_baseline_fisica", "ponto_polyfit_distante_baseline"} for p in probs):
                image_has_poly_issue = True
                geom_issue = True
                first_origin = first_origin or "Cal_angulo/angulo_contato.py:78"

        conclusions.append({
            "name": name,
            "selection_ok": not image_has_selection_issue,
            "poly_ok": not image_has_poly_issue,
            "erro_selecionar": image_has_selection_issue,
            "erro_slope": image_has_poly_issue,
            "math_issue": math_issue,
            "geom_issue": geom_issue,
            "first_origin": first_origin or "sem comportamento anomalo detectado nas duas funcoes auditadas",
        })

    lines.append("## PARTE 7 - Conclusao factual")
    lines.append("")
    lines.append("| imagem | selecao correta | polyfit correto | erro nasce em _selecionar_pontos_lado | erro nasce em _calcular_slope_tangente_polynomial | inconsistencia matematica | inconsistencia geometrica | primeira linha observada |")
    lines.append("|---|:---:|:---:|:---:|:---:|:---:|:---:|---|")
    for c in conclusions:
        lines.append(
            f"| {c['name']} | {'SIM' if c['selection_ok'] else 'NAO'} | {'SIM' if c['poly_ok'] else 'NAO'} | {'SIM' if c['erro_selecionar'] else 'NAO'} | {'SIM' if c['erro_slope'] else 'NAO'} | {'SIM' if c['math_issue'] else 'NAO'} | {'SIM' if c['geom_issue'] else 'NAO'} | `{c['first_origin']}` |"
        )

    return "\n".join(lines)


def main():
    IMG_OUT.mkdir(parents=True, exist_ok=True)
    CSV_OUT.mkdir(parents=True, exist_ok=True)
    results = [audit_image(name) for name in NAMES]
    report = build_report(results)
    (OUT_DIR / "relatorio_auditoria_completo.md").write_text(report, encoding="utf-8")
    print(str(OUT_DIR / "relatorio_auditoria_completo.md"))


if __name__ == "__main__":
    main()
