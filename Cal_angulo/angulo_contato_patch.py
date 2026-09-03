def _calcular_angulo_interno_por_vetor_tangente(tangent_vec: np.ndarray, lado: str) -> float:
    """Converte um vetor tangente local em ângulo interno de contato usando uma referência geométrica explícita."""
    tangent_vec = np.asarray(tangent_vec, dtype=float).reshape(-1)
    if tangent_vec.size != 2:
        return 0.0

    tangent_vec = tangent_vec.astype(float)
    norm = float(np.linalg.norm(tangent_vec))
    if not np.isfinite(norm) or norm < 1e-12:
        return 0.0

    tangent_unit = tangent_vec / norm
    if lado == "esq":
        baseline_vec = np.array([1.0, 0.0], dtype=float)
    else:
        baseline_vec = np.array([-1.0, 0.0], dtype=float)

    baseline_unit = baseline_vec / float(np.linalg.norm(baseline_vec))
    dot = float(np.dot(tangent_unit, baseline_unit))
    cross = float(tangent_unit[0] * baseline_unit[1] - tangent_unit[1] * baseline_unit[0])
    theta = math.degrees(math.atan2(cross, dot))
    theta = (theta + 360.0) % 360.0

    if theta > 180.0:
        theta = 360.0 - theta
    if theta < 0.0:
        theta = abs(theta)

    return float(np.clip(theta, 0.0, 180.0))
