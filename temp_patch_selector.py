from pathlib import Path
import re

path = Path(r"c:\Users\Icaro Arthur\Documents\Angle\Cal_angulo\angulo_contato.py")
text = path.read_text(encoding="utf-8")
start = text.index("def _selecionar_pontos_tangente(")
end = text.index("def _calcular_slope_tangente_polynomial(")
new_block = '''def _selecionar_pontos_tangente(
    local_pts: np.ndarray,
    baseline_y: float,
    p_contato: Optional[Union[list, tuple]] = None,
    contour_pts: Optional[np.ndarray] = None,
    lado: str = "esq",
) -> np.ndarray:
    """Seleciona uma janela contínua e local do contorno ao redor do ponto de contato para o polyfit."""
    if local_pts is None or len(local_pts) < 3:
        return np.empty((0, 2), dtype=float)

    points = np.asarray(local_pts, dtype=float)
    parent = np.asarray(contour_pts if contour_pts is not None else local_pts, dtype=float)
    if len(parent) == 0 or len(points) == 0:
        return np.empty((0, 2), dtype=float)

    if p_contato is None or len(p_contato) < 2:
        return points[: min(16, len(points))]

    contato = np.asarray(p_contato[:2], dtype=float)
    if not np.isfinite(contato).all():
        return points[: min(16, len(points))]

    contato_robusto = _selecionar_ponto_contato_robusto(parent, contato, baseline_y, lado=lado)
    if len(contato_robusto) >= 2:
        contato = contato_robusto

    contact_idx = int(np.argmin(np.hypot(parent[:, 0] - contato[0], parent[:, 1] - contato[1])))
    dist_to_contact = float(np.min(np.hypot(parent[:, 0] - contato[0], parent[:, 1] - contato[1])))
    if not np.isfinite(contact_idx) or dist_to_contact > 12.0:
        return points[: min(16, len(points))]

    lookup = {tuple(np.round(point, 6)) for point in points}
    candidate_indices = [idx for idx in range(len(parent)) if tuple(np.round(parent[idx], 6)) in lookup]
    if candidate_indices:
        candidate_indices = sorted(candidate_indices)
        candidate_runs = []
        current_run = [candidate_indices[0]]
        for idx in candidate_indices[1:]:
            if idx == current_run[-1] + 1:
                current_run.append(idx)
            else:
                candidate_runs.append(current_run)
                current_run = [idx]
        candidate_runs.append(current_run)

        selected_run = None
        for run in candidate_runs:
            if contact_idx in run and 4 <= len(run) <= 12:
                selected_run = run
                break

        if selected_run is None and len(candidate_runs) == 1:
            selected_run = candidate_runs[0]

        if selected_run is not None:
            selected_indices = list(selected_run)
            selected_points = parent[selected_indices]
        else:
            window_size = min(7, len(parent))
            if contact_idx <= 6:
                start_idx = contact_idx
            else:
                start_idx = max(0, contact_idx - 4)

            end_idx = min(len(parent), start_idx + window_size)
            if end_idx - start_idx < 4:
                start_idx = max(0, len(parent) - window_size)
                end_idx = len(parent)

            selected_indices = list(range(start_idx, end_idx))
            selected_points = parent[selected_indices]
    else:
        window_size = min(7, len(parent))
        if contact_idx <= 6:
            start_idx = contact_idx
        else:
            start_idx = max(0, contact_idx - 4)

        end_idx = min(len(parent), start_idx + window_size)
        if end_idx - start_idx < 4:
            start_idx = max(0, len(parent) - window_size)
            end_idx = len(parent)

        selected_indices = list(range(start_idx, end_idx))
        selected_points = parent[selected_indices]

    if len(selected_points) < 4:
        window_size = min(7, len(parent))
        selected_indices = list(range(min(len(parent), window_size)))
        selected_points = parent[selected_indices]

    selection_debug = {
        "contact_idx": int(np.argmin(np.hypot(parent[:, 0] - contato[0], parent[:, 1] - contato[1]))),
        "selected_indices": [int(idx) for idx in selected_indices],
        "selected_count": int(len(selected_indices)),
        "mean_dist_to_contact": float(np.mean(np.hypot(selected_points[:, 0] - contato[0], selected_points[:, 1] - contato[1]))) if len(selected_points) else 0.0,
        "max_dist_to_contact": float(np.max(np.hypot(selected_points[:, 0] - contato[0], selected_points[:, 1] - contato[1]))) if len(selected_points) else 0.0,
        "contiguous": len(selected_indices) <= 1 or all((selected_indices[i] + 1) % len(parent) == selected_indices[i + 1] for i in range(len(selected_indices) - 1)),
        "selected_points": selected_points.astype(float),
    }
    set_audit_context(last_tangent_selection=selection_debug)

    return selected_points


'''
path.write_text(text[:start] + new_block + text[end:], encoding="utf-8")
print("patched")
