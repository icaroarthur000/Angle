import numpy as np
import cv2

from linha_base import linha_base
from Cal_angulo import angulo_contato
from processamento_imagem import filtros


def _contorno_sintetico_circular(cx=120.0, cy=120.0, r=55.0, n=260):
    t = np.linspace(0.08 * np.pi, 0.92 * np.pi, n)
    x = cx + r * np.cos(t)
    y = cy + r * np.sin(t)
    return np.stack([x, y], axis=1).astype(np.float64)


def test_baseline_robusta_reduz_outlier():
    pts = _contorno_sintetico_circular()
    # outlier abaixo do piso real
    outlier = np.array([[120.0, 220.0]], dtype=np.float64)
    pts_ruidoso = np.vstack([pts, outlier])

    baseline_y, line = linha_base.detect_baseline_tls(pts_ruidoso)

    assert line is not None
    # baseline deve ficar próxima do piso real da gota, e não no outlier extremo
    y_real = float(np.max(pts[:, 1]))
    assert abs(baseline_y - y_real) < 8.0


def test_qualidade_dinamica_em_faixa_valida():
    pts = _contorno_sintetico_circular()
    y_base = float(np.max(pts[:, 1]))
    p_esq = [float(np.min(pts[:, 0])), y_base]
    p_dir = [float(np.max(pts[:, 0])), y_base]

    q = angulo_contato.calcular_qualidade_dinamica(pts, p_esq, p_dir, y_base)

    assert 0.0 <= float(q["score"]) <= 1.0
    assert float(q["rmse_px"]) >= 0.0


def test_multi_threshold_retorna_mascara_e_metodo():
    img = np.zeros((180, 220, 3), dtype=np.uint8)
    # elipse clara em fundo escuro
    rr, cc = np.ogrid[:180, :220]
    mask = (((cc - 110) / 50.0) ** 2 + ((rr - 100) / 35.0) ** 2) <= 1.0
    img[mask] = (220, 220, 220)

    bin_img, metodo = filtros.aplicar_multi_threshold(img)

    assert bin_img.shape == img.shape[:2]
    assert metodo in {"OTSU", "ADAPTIVE", "CANNY"}


def test_contorno_achatado_de_30_graus_nao_e_rejeitado():
    img = np.zeros((220, 260), dtype=np.uint8)
    cv2.ellipse(img, (130, 140), (80, 30), 0, 0, 180, 255, -1)

    pts = contorno.encontrar_contorno_gota_robusto(img, substrate_removed=True)

    assert pts is not None
    assert len(pts) > 100
    assert int(np.max(pts[:, 1])) >= 168


# =========================================================
# Teste de ROI-invariância + cascata tripla
# =========================================================
from processamento_imagem import contorno
from Cal_angulo import angulo_contato as ac


def _criar_imagem_gota_com_substrato(h_roi, w=250, h_gota=80, w_gota=100):
    """Cria imagem sintética BGR de gota escura sobre fundo claro + substrato escuro no fundo.
    O substrato sempre fica nas últimas 30 linhas do ROI.
    h_roi controla quanto 'espaço abaixo' da gota existe.
    """
    img = np.full((h_roi, w, 3), 200, dtype=np.uint8)  # fundo claro

    # Gota: semi-elipse escura centrada horizontalmente, apoiada em y_base_gota
    y_base_gota = h_roi - 40  # gota termina ~40px acima do fundo
    cx, cy = w // 2, y_base_gota - h_gota // 2
    rr, cc = np.ogrid[:h_roi, :w]
    mask_gota = (((cc - cx) / (w_gota / 2.0)) ** 2 + ((rr - cy) / (h_gota / 2.0)) ** 2) <= 1.0
    mask_gota = mask_gota & (rr <= y_base_gota)
    img[mask_gota] = (30, 30, 30)  # escuro

    # Substrato escuro no fundo inteiro (últimas 25 linhas)
    img[h_roi - 25:, :] = (20, 20, 20)

    return img, y_base_gota


def test_isolar_gota_substrato_separa_gota_de_substrato():
    """A cascata tripla deve separar a gota do substrato colado pelo Otsu."""
    img_bgr, _ = _criar_imagem_gota_com_substrato(h_roi=220)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    _, bin_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Sem separação, Otsu cola gota + substrato numa massa gigante
    bin_limpa, _ = contorno.isolar_gota_substrato(gray, bin_otsu)

    # O substrato (últimas 25 linhas) deve ter sido cortado: quase zero foreground lá
    fg_fundo = int(np.count_nonzero(bin_limpa[-25:, :]))
    assert fg_fundo < 50, f"Substrato não foi removido: {fg_fundo} pixels restantes"

    # A gota em si deve continuar com foreground significativo
    fg_gota = int(np.count_nonzero(bin_limpa[:180, :]))
    assert fg_gota > 500, f"Gota foi amputada: apenas {fg_gota} pixels restantes"


def test_roi_invariancia_angulo():
    """O ângulo calculado deve variar <= 2° entre ROIs com alturas diferentes."""
    angulos = []
    for h_extra in [0, 50, 100]:
        h_roi = 220 + h_extra
        img_bgr, _ = _criar_imagem_gota_com_substrato(h_roi=h_roi)
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        _, bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        mask, pts = contorno.extrair_mascara_gota(bin_img, img_gray=gray)
        if pts is None or len(pts) < 10:
            continue

        from linha_base import linha_base as lb
        res = lb.detectar_baseline_hibrida(pts)
        if res["p_esq"] is None or res["p_dir"] is None:
            continue

        ae = ac.calcular_angulo_circular(pts, res["p_esq"], res["p_dir"], res["baseline_y"], "esq")
        ad = ac.calcular_angulo_circular(pts, res["p_esq"], res["p_dir"], res["baseline_y"], "dir")
        media = (ae + ad) / 2.0
        if media > 1.0:
            angulos.append(media)

    assert len(angulos) >= 2, f"Apenas {len(angulos)} ROIs produziram ângulo válido"
    variacao = max(angulos) - min(angulos)
    assert variacao <= 2.0, f"Variação de ângulo entre ROIs = {variacao:.2f}° (máx permitido: 2°)"


def test_ponto_fora_do_contorno_e_corrigido():
    """Ponto fora do contorno deve ser projetado para a faixa de contato."""
    t = np.linspace(0, np.pi, 220)
    cx, cy, r = 100.0, 80.0, 60.0
    contorno_pts = np.stack([cx + r * np.cos(t), cy + r * np.sin(t)], axis=1)
    baseline_y = float(np.max(contorno_pts[:, 1]))

    ponto_fora = [100.0, baseline_y + 20.0]
    ponto_corrigido, foi_corrigido = contorno.projetar_ponto_no_contorno(
        ponto_fora, contorno_pts, baseline_y, tolerancia_px=2.0, faixa_baseline_px=30.0
    )

    assert foi_corrigido is True
    dists = np.hypot(contorno_pts[:, 0] - ponto_corrigido[0], contorno_pts[:, 1] - ponto_corrigido[1])
    assert float(np.min(dists)) <= 2.0
    assert ponto_corrigido[1] >= (baseline_y - 30.0)


def test_ponto_dentro_da_tolerancia_nao_e_alterado():
    """Ponto já válido próximo do contorno não deve ser alterado."""
    t = np.linspace(0, np.pi, 220)
    cx, cy, r = 100.0, 80.0, 60.0
    contorno_pts = np.stack([cx + r * np.cos(t), cy + r * np.sin(t)], axis=1)
    baseline_y = float(np.max(contorno_pts[:, 1]))

    idx = int(np.argmax(contorno_pts[:, 1]))
    ponto_valido = [float(contorno_pts[idx, 0]), float(contorno_pts[idx, 1])]
    ponto_final, foi_corrigido = contorno.projetar_ponto_no_contorno(
        ponto_valido, contorno_pts, baseline_y, tolerancia_px=2.0, faixa_baseline_px=30.0
    )

    assert foi_corrigido is False
    assert np.allclose(ponto_final, ponto_valido)
