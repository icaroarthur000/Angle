import numpy as np
from Cal_angulo import angulo_contato


def test_angulo_interno_semicirculo_horizontal():
    # Contorno aproximado de semicírculo sobre baseline y=100
    # Para ângulo de contato de 90°, o centro do círculo deve estar exatamente
    # sobre a baseline (y_centro == y_baseline) e a gota forma um arco semicircular.
    cx, cy, r = 120.0, 100.0, 40.0
    t = np.linspace(np.pi, 0, 120)
    x = cx + r * np.cos(t)
    y = cy - r * np.sin(t)
    pts = np.stack([x, y], axis=1)

    baseline_y = 100.0
    p_esq = [float(np.min(pts[:, 0])), baseline_y]
    p_dir = [float(np.max(pts[:, 0])), baseline_y]

    ae = angulo_contato.calcular_angulo_circular(pts, p_esq, p_dir, baseline_y, "esq")
    ad = angulo_contato.calcular_angulo_circular(pts, p_esq, p_dir, baseline_y, "dir")

    assert ae is not None
    assert ad is not None
    assert 0.0 <= ae <= 180.0
    assert 0.0 <= ad <= 180.0
    assert abs(ae - ad) < 5.0
    assert 80.0 < ae < 100.0
    assert 80.0 < ad < 100.0
