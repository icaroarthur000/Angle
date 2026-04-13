import math

import numpy as np
import cv2

from linha_base import linha_base
from Cal_angulo import angulo_contato
from processamento_imagem import filtros
from parametros import obter

# Tolerância configurável para testes de regressão
TOL = float(obter("test_angle_tolerance_deg", 2.0))


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


def test_candidatos_segmentacao_progressiva_sao_validos():
    img = np.zeros((180, 220, 3), dtype=np.uint8)
    rr, cc = np.ogrid[:180, :220]
    mask = (((cc - 110) / 50.0) ** 2 + ((rr - 100) / 35.0) ** 2) <= 1.0
    img[mask] = (220, 220, 220)

    candidatos = filtros.gerar_candidatos_segmentacao(img)

    assert set(candidatos.keys()) == {"OTSU_LIGHT", "OTSU", "ADAPTIVE_LIGHT", "ADAPTIVE", "CANNY"}
    for mascara in candidatos.values():
        assert mascara.shape == img.shape[:2]
        assert mascara.dtype == np.uint8


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
    bin_limpa = contorno.isolar_gota_substrato(gray, bin_otsu)

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
        if ae is None or ad is None:
            continue
        media = (ae + ad) / 2.0
        if media > 1.0:
            angulos.append(media)

    assert len(angulos) >= 2, f"Apenas {len(angulos)} ROIs produziram ângulo válido"
    variacao = max(angulos) - min(angulos)
    assert variacao <= TOL, f"Variação de ângulo entre ROIs = {variacao:.2f}° (máx permitido: {TOL}°)"


# AVISO-09: teste do fallback polinomial com pontos colineares
def test_fallback_polinomial_com_pontos_colineares():
    """Se o contorno for colinear (sem curvatura), o ajuste polinomial deve
    degenerar e o fallback deve retornar um float válido (0 <= ang <= 180)."""
    # Pontos exatamente colineares na horizontal (nenhuma curvatura)
    xs = np.linspace(50.0, 150.0, 60)
    ys = np.full_like(xs, 80.0)
    pts = np.stack([xs, ys], axis=1)

    baseline_y = 80.0
    p_esq = [50.0, 80.0]
    p_dir = [150.0, 80.0]

    angulo = angulo_contato.calcular_angulo_circular(pts, p_esq, p_dir, baseline_y, "esq")

    # Deve retornar float ou None, não lançar exceção
    if angulo is not None:
        assert isinstance(angulo, float)
        assert 0.0 <= angulo <= 180.0, f"Fallback retornou ângulo fora do domínio: {angulo}°"


# ==========================================================
# Testes de regressão para gotas com ângulos baixos (30°/50°)
# Verifica que o cálculo angular não sofre viés sistemático
# causado pelo offset de calibração na baseline.
# ==========================================================

def _contorno_calota_esferica(theta_deg, R=60, cx=120, n=300):
    """Gera contorno de calota esférica perfeita com ângulo de contato dado.

    Retorna (pts, baseline_y, p_esq, p_dir).
    """
    theta = math.radians(theta_deg)
    baseline_y = 200.0
    yc = baseline_y - R * math.cos(theta)
    alphas = np.linspace(theta, 2 * np.pi - theta, n)
    x = cx + R * np.sin(alphas)
    y = yc + R * np.cos(alphas)
    pts = np.stack([x, y], axis=1).astype(np.float64)
    half_w = R * math.sin(theta)
    p_esq = [cx - half_w, baseline_y]
    p_dir = [cx + half_w, baseline_y]
    return pts, baseline_y, p_esq, p_dir


def test_angulo_circular_30_graus_sem_vies():
    """Ângulo de 30° deve ser medido com erro < 2° para gotas de vários tamanhos."""
    for R in [15, 25, 50]:
        pts, bl, pe, pd = _contorno_calota_esferica(30, R=R)
        ae = angulo_contato.calcular_angulo_circular(pts, pe, pd, bl, "esq")
        ad = angulo_contato.calcular_angulo_circular(pts, pe, pd, bl, "dir")
        assert ae is not None and ad is not None, f"Cálculo retornou None para R={R}"
        media = (ae + ad) / 2.0
        assert abs(media - 30.0) < TOL, (
            f"Ângulo 30° R={R}: medido {media:.2f}° (erro={abs(media-30):.2f}°, tol={TOL}°)"
        )


def test_angulo_circular_50_graus_sem_vies():
    """Ângulo de 50° deve ser medido com erro < 2° para gotas de vários tamanhos."""
    for R in [15, 25, 50]:
        pts, bl, pe, pd = _contorno_calota_esferica(50, R=R)
        ae = angulo_contato.calcular_angulo_circular(pts, pe, pd, bl, "esq")
        ad = angulo_contato.calcular_angulo_circular(pts, pe, pd, bl, "dir")
        assert ae is not None and ad is not None, f"Cálculo retornou None para R={R}"
        media = (ae + ad) / 2.0
        assert abs(media - 50.0) < TOL, (
            f"Ângulo 50° R={R}: medido {media:.2f}° (erro={abs(media-50):.2f}°, tol={TOL}°)"
        )


def test_angulo_independente_do_raio():
    """O ângulo medido não deve depender significativamente do tamanho da gota.

    Para o mesmo ângulo de contato, gotas com R=15 e R=80 devem dar resultados
    semelhantes (variação < 2°).
    """
    for target in [30, 50, 90]:
        medidas = []
        for R in [15, 25, 50, 80]:
            pts, bl, pe, pd = _contorno_calota_esferica(target, R=R)
            ae = angulo_contato.calcular_angulo_circular(pts, pe, pd, bl, "esq")
            ad = angulo_contato.calcular_angulo_circular(pts, pe, pd, bl, "dir")
            if ae is not None and ad is not None:
                medidas.append((ae + ad) / 2.0)
        assert len(medidas) >= 2, f"θ={target}°: insuficientes medições válidas"
        variacao = max(medidas) - min(medidas)
        assert variacao < TOL, (
            f"θ={target}°: variação entre tamanhos = {variacao:.2f}° (tol={TOL}°)"
        )
