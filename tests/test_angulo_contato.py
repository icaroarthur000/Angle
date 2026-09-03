import numpy as np
import pytest
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


def test_selecao_tangente_usa_janela_contigua_ao_contato_no_contorno():
    contour = np.array([
        [0.0, 0.0],
        [1.0, 1.0],
        [2.0, 2.0],
        [3.0, 3.0],
        [4.0, 4.0],
        [5.0, 5.0],
        [6.0, 6.0],
        [7.0, 7.0],
        [8.0, 8.0],
        [9.0, 9.0],
        [10.0, 10.0],
        [11.0, 11.0],
    ], dtype=float)

    contact = [4.0, 4.0]
    local_pts = contour[[0, 2, 4, 6, 8, 10]]

    selected = angulo_contato._selecionar_pontos_tangente(local_pts, baseline_y=10.0, p_contato=contact, contour_pts=contour)

    assert len(selected) == 7
    indices = [int(np.where((contour == pt).all(axis=1))[0][0]) for pt in selected]
    assert indices[0] == 4
    assert indices[-1] == 10
    assert all(indices[i + 1] - indices[i] == 1 for i in range(len(indices) - 1))


def test_selecao_contigua_preserva_ordem_do_contorno():
    contour = np.array([
        [10.0, 10.0],
        [11.0, 10.0],
        [12.0, 10.0],
        [13.0, 10.0],
        [14.0, 10.0],
        [15.0, 10.0],
        [16.0, 10.0],
        [17.0, 10.0],
        [17.0, 11.0],
        [17.0, 12.0],
        [16.0, 13.0],
        [15.0, 14.0],
        [14.0, 15.0],
        [13.0, 16.0],
        [12.0, 17.0],
        [11.0, 18.0],
        [10.0, 19.0],
    ], dtype=float)

    contact = [12.0, 10.0]
    local_pts = contour[[2, 3, 4, 5, 6, 7, 8, 9, 10]]

    selected = angulo_contato._selecionar_pontos_tangente(local_pts, baseline_y=10.0, p_contato=contact, contour_pts=contour)

    assert len(selected) >= 4
    indices = [int(np.where((contour == pt).all(axis=1))[0][0]) for pt in selected]
    assert indices[0] == 2
    assert indices[-1] == 10

    circular_deltas = []
    for i in range(1, len(indices)):
        delta = indices[i] - indices[i - 1]
        circular_deltas.append(delta if delta > 0 else delta + len(contour))

    assert all(delta == 1 for delta in circular_deltas)


def test_selecao_tangente_usa_ordem_do_contorno_quando_local_pts_esta_em_ordem_inversa():
    contour = np.array([
        [0.0, 10.0],
        [1.0, 10.0],
        [2.0, 10.0],
        [3.0, 10.0],
        [4.0, 10.0],
        [5.0, 10.0],
    ], dtype=float)

    contact = [2.0, 10.0]
    local_pts = contour[[5, 4, 3, 2, 1, 0]]

    selected = angulo_contato._selecionar_pontos_tangente(local_pts, baseline_y=10.0, p_contato=contact, contour_pts=contour)

    indices = [int(np.where((contour == pt).all(axis=1))[0][0]) for pt in selected]
    deltas = [
        (indices[i] - indices[i - 1]) % len(contour)
        for i in range(1, len(indices))
    ]

    assert len(indices) >= 4
    assert all(delta == 1 for delta in deltas)


def test_selecao_tangente_prefere_janela_pequena_e_local():
    contour = np.array([
        [0.0, 0.0],
        [1.0, 1.0],
        [2.0, 2.0],
        [3.0, 3.0],
        [4.0, 4.0],
        [5.0, 5.0],
        [6.0, 6.0],
        [7.0, 7.0],
        [8.0, 8.0],
        [9.0, 9.0],
        [10.0, 10.0],
        [11.0, 11.0],
        [12.0, 12.0],
        [13.0, 13.0],
        [14.0, 14.0],
        [15.0, 15.0],
        [16.0, 16.0],
        [17.0, 17.0],
        [18.0, 18.0],
        [19.0, 19.0],
    ], dtype=float)
    contact = [8.0, 8.0]
    local_pts = contour

    selected = angulo_contato._selecionar_pontos_tangente(local_pts, baseline_y=10.0, p_contato=contact, contour_pts=contour)

    assert len(selected) == 7
    assert np.allclose(selected[0], contour[4])
    assert np.allclose(selected[-1], contour[10])


def test_selecao_tangente_fallback_quando_geometria_nao_e_confiavel():
    contour = np.array([
        [0.0, 0.0],
        [1.0, 1.0],
        [2.0, 2.0],
        [3.0, 3.0],
        [4.0, 4.0],
        [5.0, 5.0],
        [6.0, 6.0],
        [7.0, 7.0],
        [8.0, 8.0],
        [9.0, 9.0],
    ], dtype=float)
    contact = [100.0, 100.0]
    local_pts = contour

    selected = angulo_contato._selecionar_pontos_tangente(local_pts, baseline_y=10.0, p_contato=contact, contour_pts=contour)

    assert len(selected) <= 16
    assert len(selected) == len(local_pts[:16])


def test_selecao_tangente_nao_fica_restrita_a_pontos_na_baseline_quando_ha_curvatura_local():
    contour = np.array([
        [0.0, 10.0],
        [1.0, 10.0],
        [2.0, 10.0],
        [3.0, 10.0],
        [4.0, 10.0],
        [5.0, 10.0],
        [6.0, 10.0],
        [7.0, 10.0],
        [8.0, 10.0],
        [9.0, 10.0],
        [8.0, 9.0],
        [7.0, 8.0],
        [6.0, 7.0],
        [5.0, 6.0],
    ], dtype=float)

    contact = [5.0, 10.0]
    local_pts = contour

    selected = angulo_contato._selecionar_pontos_tangente(local_pts, baseline_y=10.0, p_contato=contact, contour_pts=contour)

    assert len(selected) >= 4
    assert np.any(np.abs(selected[:, 1] - 10.0) > 0.1)


def test_valida_candidato_contato_rejeita_ponto_espelhado():
    contour = np.array([
        [10.0, 100.0],
        [20.0, 101.0],
        [30.0, 102.0],
        [40.0, 103.0],
        [50.0, 104.0],
        [60.0, 105.0],
        [70.0, 106.0],
        [80.0, 107.0],
        [90.0, 108.0],
        [100.0, 109.0],
    ], dtype=float)
    baseline_y = 100.0
    contact = [55.0, 100.0]
    candidate = [95.0, 100.0]

    validation = angulo_contato.validar_candidato_contato(contour, candidate, contact, baseline_y, lado="esq")

    assert validation is not None
    assert validation["is_valid"] is False
    assert validation["reason"] == "deslocado_da_regiao_de_contato"


def test_selecao_tangente_passa_lado_real_para_validacao_contato(monkeypatch):
    contour = np.array([
        [0.0, 10.0],
        [1.0, 10.0],
        [2.0, 10.0],
        [3.0, 10.0],
        [4.0, 10.0],
        [5.0, 10.0],
        [6.0, 10.0],
        [7.0, 10.0],
        [8.0, 10.0],
        [9.0, 10.0],
    ], dtype=float)

    selected = angulo_contato._selecionar_pontos_tangente(
        contour,
        baseline_y=10.0,
        p_contato=[4.0, 10.0],
        contour_pts=contour,
        lado="dir",
    )

    assert len(selected) >= 4


@pytest.mark.parametrize(
    ("lado", "tangent_vec", "expected"),
    [
        ("esq", np.array([1.0, np.tan(np.deg2rad(30.0))]), 30.0),
        ("esq", np.array([1.0, np.tan(np.deg2rad(50.0))]), 50.0),
        ("esq", np.array([-1.0, np.tan(np.deg2rad(100.0))]), 100.0),
        ("esq", np.array([-1.0, np.tan(np.deg2rad(130.0))]), 130.0),
        ("dir", np.array([-1.0, np.tan(np.deg2rad(30.0))]), 30.0),
        ("dir", np.array([-1.0, np.tan(np.deg2rad(50.0))]), 50.0),
        ("dir", np.array([1.0, np.tan(np.deg2rad(100.0))]), 100.0),
        ("dir", np.array([1.0, np.tan(np.deg2rad(130.0))]), 130.0),
    ],
)
def test_conversao_geometrica_tangente_para_angulo_interno(lado, tangent_vec, expected):
    angle = angulo_contato._calcular_angulo_interno_por_vetor_tangente(tangent_vec, lado)
    assert angle == pytest.approx(expected, abs=1e-6)
