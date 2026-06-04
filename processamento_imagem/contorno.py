import cv2
import numpy as np

# =================================================================
# MÓDULO: processamento_imagem/contorno.py
# Responsável por:
#   1. Separar gota do substrato (cascata tripla: Necking + Sobel Y + morfologia)
#   2. Extrair contorno da gota e avaliar sua qualidade
#   3. Projetar pontos de contato de volta ao contorno quando arrastados
# =================================================================


# =================================================================
# BLOCO 1 — SEPARADORES (funções privadas da cascata tripla)
# =================================================================

def _necking_detection(img_bin):
    """Detecta estreitamento (pescoço) entre gota e substrato pelo perfil de largura."""
    h, w = img_bin.shape[:2]
    if h < 30 or w < 30:
        return -1, 0.0

    # Perfil de largura: número de pixels brancos por linha
    larguras = np.sum(img_bin > 0, axis=1).astype(np.float64)

    # Suaviza o perfil para evitar ruído pontual
    if len(larguras) >= 7:
        k = np.array([1, 2, 3, 4, 3, 2, 1], dtype=np.float64)
        larguras = np.convolve(larguras, k / k.sum(), mode="same")

    # Encontra a região da gota (onde há pixels brancos)
    linhas_ativas = np.where(larguras > 0)[0]
    if len(linhas_ativas) < 10:
        return -1, 0.0

    y_topo = int(linhas_ativas[0])
    y_base_fg = int(linhas_ativas[-1])
    h_gota = y_base_fg - y_topo
    if h_gota < 15:
        return -1, 0.0

    # Procura vale entre 55% e 95% da altura da gota (zona de contato)
    y_ini = y_topo + int(h_gota * 0.55)
    y_fim = min(h, y_topo + int(h_gota * 0.95))
    if y_fim <= y_ini + 3:
        return -1, 0.0

    perfil = larguras[y_ini:y_fim]
    if len(perfil) < 3:
        return -1, 0.0

    # O máximo do perfil nessa faixa (largura do corpo da gota)
    larg_max = float(np.max(perfil))
    if larg_max < 5:
        return -1, 0.0

    idx_min = int(np.argmin(perfil))
    larg_min = float(perfil[idx_min])
    y_neck = y_ini + idx_min

    # Confiança = profundidade relativa do vale
    profundidade = (larg_max - larg_min) / larg_max
    # Exige estreitamento mínimo de 15% para ser considerado necking real
    if profundidade < 0.15:
        return -1, 0.0

    return y_neck, float(np.clip(profundidade, 0.0, 1.0))


def _sobel_y_surface(img_gray):
    """Detecta a linha da superfície sólida pelo gradiente Sobel vertical na imagem original."""
    h, w = img_gray.shape[:2]
    if h < 30 or w < 30:
        return -1, 0.0

    # Analisa apenas a metade inferior (evita confundir com topo da gota)
    y_start = int(h * 0.45)
    roi = img_gray[y_start:, :]
    if roi.shape[0] < 10:
        return -1, 0.0

    sobel_y = cv2.Sobel(roi, cv2.CV_64F, 0, 1, ksize=3)
    sobel_abs = np.abs(sobel_y)

    # Contagem de colunas ativas por linha (em vez de soma de magnitudes).
    # Princípio: a superfície do substrato é a ÚNICA borda horizontal que
    # percorre toda a largura da imagem — ativa muito mais colunas do que
    # qualquer borda parcial da curvatura lateral da gota.
    # argmax na contagem localiza corretamente o substrato.
    mean_abs = float(np.mean(sobel_abs))
    if mean_abs < 1e-6:
        return -1, 0.0

    col_threshold = mean_abs * 2.0
    projecao = np.sum(sobel_abs > col_threshold, axis=1).astype(np.float64)

    if len(projecao) < 5:
        return -1, 0.0

    # Suaviza para reduzir ruído
    k = np.array([1, 2, 3, 2, 1], dtype=np.float64)
    projecao = np.convolve(projecao, k / k.sum(), mode="same")

    # Projeção de soma mantida apenas para calcular confiança
    projecao_sum = np.sum(sobel_abs, axis=1)
    projecao_sum = np.convolve(projecao_sum, k / k.sum(), mode="same")
    media_geral = float(np.mean(projecao_sum))
    if media_geral < 1e-6:
        return -1, 0.0

    # argmax na contagem de colunas — bloco inferior do ROI
    meio_proj = len(projecao) // 2
    subproj = projecao[meio_proj:]
    if len(subproj) < 3:
        return -1, 0.0

    idx_pico = meio_proj + int(np.argmax(subproj))
    pico_val = float(projecao_sum[idx_pico])

    y_sobel = y_start + idx_pico

    # Confiança = proeminência do pico sobre a média
    confianca = float(np.clip((pico_val / media_geral - 1.0) / 3.0, 0.0, 1.0))

    return y_sobel, confianca


def _abertura_anisotropica(img_bin, kernel_size=(9, 3)):
    """Quebra pontes horizontais entre gota e substrato com kernel largo e curto."""
    h, w = img_bin.shape[:2]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    bin_morf = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)

    conts, _ = cv2.findContours(bin_morf, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not conts:
        return bin_morf, h, 0.0

    maior = max(conts, key=cv2.contourArea)
    x, y, bw, bh = cv2.boundingRect(maior)
    y_base = y + bh

    # Confiança: quanto de foreground foi removido (indica separação efetiva)
    fg_antes = float(np.count_nonzero(img_bin))
    fg_depois = float(np.count_nonzero(bin_morf))
    if fg_antes > 0:
        removido = (fg_antes - fg_depois) / fg_antes
        confianca = float(np.clip(removido * 5.0, 0.0, 1.0))  # escala 0-1
    else:
        confianca = 0.0

    return bin_morf, y_base, confianca


def isolar_gota_substrato(img_gray, img_bin):
    """Combina Necking + Sobel Y + abertura morfológica para encontrar y_corte.

    Retorna (bin_limpa, y_corte) onde y_corte é a posição física exata da
    superfície, calculada ANTES de qualquer erosão.
    """
    if img_bin is None:
        return img_bin
    h, w = img_bin.shape[:2]
    if h < 30 or w < 30:
        return img_bin

    # --- Técnica C: base morfológica como fallback seguro ---
    bin_morf, y_base_morf, conf_morf = _abertura_anisotropica(img_bin)

    # --- Técnica A: pescoço na imagem pós-abertura ---
    y_neck, conf_neck = _necking_detection(bin_morf)

    # --- Técnica B: borda Sobel na imagem cinza original ---
    y_sobel, conf_sobel = -1, 0.0
    if img_gray is not None and img_gray.shape[:2] == img_bin.shape[:2]:
        y_sobel, conf_sobel = _sobel_y_surface(img_gray)

    # --- Decisor: consenso por confiança ---
    candidatos = []
    if y_neck > 0 and conf_neck > 0.0:
        candidatos.append((y_neck, conf_neck, "necking"))
    if y_sobel > 0 and conf_sobel > 0.0:
        candidatos.append((y_sobel, conf_sobel, "sobel_y"))

    # Fallback seguro: base do contorno morfológico
    y_corte = y_base_morf

    if len(candidatos) >= 2:
        # Dois métodos concordam?  (tolerância de 8px)
        y_a, c_a, _ = candidatos[0]
        y_b, c_b, _ = candidatos[1]
        if abs(y_a - y_b) <= 8:
            # Consenso: média ponderada pela confiança
            peso_total = c_a + c_b
            y_corte = int((y_a * c_a + y_b * c_b) / max(1e-9, peso_total))
        else:
            # Divergência: usa o de maior confiança
            melhor = max(candidatos, key=lambda t: t[1])
            y_corte = melhor[0]
    elif len(candidatos) == 1:
        y_corte = candidatos[0][0]

    # --- Proteção anti-amputação ---
    # Detecta topo real do foreground para calcular altura da gota
    linhas_fg = np.where(np.any(img_bin > 0, axis=1))[0]
    if len(linhas_fg) > 5:
        y_topo_fg = int(linhas_fg[0])
        h_gota = y_corte - y_topo_fg
        # O corte não pode ficar acima de 70% da altura da gota (preserva pelo menos 70%)
        y_minimo_corte = y_topo_fg + int(h_gota * 0.70) if h_gota > 0 else y_corte
        y_corte = max(y_corte, y_minimo_corte)

    # Segurança final: verifica se a gota ACIMA do corte mantém massa suficiente.
    # Diferente de checar "% total removida", verificamos se o foreground
    # restante (a gota) é significativo — isso evita abortar quando o substrato
    # é grande mas o corte é correto.
    bin_limpa = img_bin.copy()
    fg_acima = int(np.count_nonzero(bin_limpa[:y_corte, :]))
    bin_limpa[y_corte:, :] = 0

    # Se restar menos de 300 pixels acima do corte, provavelmente amputou a gota
    if fg_acima < 300:
        return bin_morf, y_base_morf

    return bin_limpa, y_corte


# =================================================================
# BLOCO 2 — INTERFACE PÚBALICA DE REMOÇÃO DE SUBSTRATO
# =================================================================


def remover_substrato_abaixo_superficie(imagem_binaria, img_gray=None):
    """Ponto de entrada pública da cascata. Retorna (bin_limpa, y_surface)."""
    if imagem_binaria is None:
        return imagem_binaria, None

    if len(imagem_binaria.shape) == 3:
        base = cv2.cvtColor(imagem_binaria, cv2.COLOR_BGR2GRAY)
    else:
        base = imagem_binaria.copy()

    resultado, y_corte = isolar_gota_substrato(img_gray, base)

    # y_corte é calculado ANTES da erosão morfológica — é a posição física
    # exata da superfície do substrato. Propagar direto como y_surface.
    y_surface = int(y_corte) if y_corte is not None else None

    return resultado, y_surface


# =================================================================
# BLOCO 3 — EXTRAÇÃO DE MÁSCARA E PROJEÇÃO DE PONTOS
# =================================================================


def extrair_mascara_gota(imagem_binaria, img_gray=None):
    """Separa o substrato, extrai o contorno e retorna a máscara sólida da gota."""
    if imagem_binaria is None:
        return None, None

    if len(imagem_binaria.shape) == 3:
        base = cv2.cvtColor(imagem_binaria, cv2.COLOR_BGR2GRAY)
    else:
        base = imagem_binaria.copy()

    # Aplica pipeline de separação tripla
    base_clean, _ = isolar_gota_substrato(img_gray, base)

    pts = encontrar_contorno_gota_robusto(base_clean, substrate_removed=True)
    if pts is None:
        pts = encontrar_contorno_gota(base_clean)

    if pts is None or len(pts) < 10:
        return base_clean, None

    mask = np.zeros(base_clean.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [pts.astype(np.int32)], 255)
    return mask, pts


def projetar_ponto_no_contorno(
    ponto,
    gota_pts: np.ndarray,
    baseline_y: float,
    tolerancia_px: float = 2.0,
    faixa_baseline_px: float = 30.0,
):
    """Projeta um ponto (contato manual) para o ponto mais próximo do contorno.

    Restringe a busca à faixa inferior (próxima à baseline) para não saltar
    para o topo da gota.

    Retorna (ponto_final, foi_corrigido).
    """
    if ponto is None:
        return ponto, False

    try:
        px, py = float(ponto[0]), float(ponto[1])
    except Exception:
        return ponto, False

    if gota_pts is None:
        return [px, py], False

    pts = np.asarray(gota_pts, dtype=np.float64)
    if pts.ndim != 2 or pts.shape[0] == 0 or pts.shape[1] < 2:
        return [px, py], False

    tol = max(0.0, float(tolerancia_px))
    faixa = max(1.0, float(faixa_baseline_px))

    if baseline_y is None or not np.isfinite(float(baseline_y)):
        baseline_ref = float(np.max(pts[:, 1]))
    else:
        baseline_ref = float(baseline_y)

    mask = pts[:, 1] >= (baseline_ref - faixa)
    candidatos = pts[mask] if np.any(mask) else pts

    # Restringe ao lado correto (esq/dir) para evitar salto entre joelhos
    center_x = float(np.mean(pts[:, 0]))
    if px <= center_x:
        candidatos_lado = candidatos[candidatos[:, 0] <= center_x]
    else:
        candidatos_lado = candidatos[candidatos[:, 0] > center_x]
    if len(candidatos_lado) > 0:
        candidatos = candidatos_lado

    dists = np.hypot(candidatos[:, 0] - px, candidatos[:, 1] - py)
    idx_min = int(np.argmin(dists))
    min_dist = float(dists[idx_min])

    if min_dist <= tol:
        return [px, py], False

    ponto_corrigido = [float(candidatos[idx_min, 0]), float(candidatos[idx_min, 1])]
    return ponto_corrigido, True


# =================================================================
# BLOCO 4 — DETECÇÃO DE CONTORNO
# =================================================================


# =================================================================
# NOVA FUNÇÃO: Busca Robusta de Contorno (com Validação)
# =================================================================
def encontrar_contorno_gota_robusto(imagem_binaria, substrate_removed: bool = False):
    """Versão principal de extração de contorno com validação geométrica.

    substrate_removed=True: desativa filtros de fundo (bottom_margin, ancora_no_fundo)
    para que o contorno alcance a linha de contato real.
    """
    if len(imagem_binaria.shape) == 3:
        img = cv2.cvtColor(imagem_binaria, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem_binaria.copy()
    
    h, w = img.shape[:2]
    
    # Morphological closing
    kernel = np.ones((3, 3), np.uint8)
    processed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    # Margens de segurança
    top_margin, side_margin, bottom_margin = _margens_adaptativas(h, w)
    processed[:top_margin, :] = 0
    # Proteção inferior: só aplica quando o substrato NÃO foi removido ainda,
    # evitando cortar a linha de contato real da gota limpa.
    if not substrate_removed:
        processed[max(0, h - bottom_margin):, :] = 0
    processed[:, :side_margin] = 0
    processed[:, max(0, w - side_margin):] = 0
    
    # Busca contornos
    conts, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if not conts:
        edges = cv2.Canny(img, 30, 100)
        edges[:top_margin, :] = 0
        if not substrate_removed:
            edges[max(0, h - bottom_margin):, :] = 0
        edges[:, :side_margin] = 0
        edges[:, max(0, w - side_margin):] = 0
        conts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if not conts:
        return None
    
    # FILTRO: Validar contornos
    valid_contours = []
    for c in conts:
        if _validar_contorno(c, h, w):
            pts = c.reshape(-1, 2)
            
            margin = max(4, int(0.01 * min(h, w)))
            touches_sides = (np.any(pts[:, 0] <= margin) or np.any(pts[:, 0] >= w - margin) or
                             np.any(pts[:, 1] <= margin))
            touches_bottom = np.any(pts[:, 1] >= h - margin)
            
            x, y, bw, bh = cv2.boundingRect(c)
            faixa_superficie = (bw > 0.70 * w) and (bh < 0.30 * h) and (y > 0.35 * h)

            if substrate_removed:
                # Substrato removido: só rejeita faixa horizontal pura (artefato residual)
                if not faixa_superficie:
                    valid_contours.append(c)
            else:
                ancora_no_fundo = touches_bottom and (bw > 0.60 * w)
                touches = touches_sides or touches_bottom
                if not touches and not faixa_superficie and not ancora_no_fundo:
                    valid_contours.append(c)
    
    if not valid_contours:
        return None
    
    # Seleciona melhor contorno válido por score geométrico.
    c = max(valid_contours, key=lambda cc: _pontuacao_contorno(cc, h, w))
    pts = c.reshape(-1, 2)
    
    # Limpa pontos nas bordas laterais e topo; fundo só clipa quando sem limpeza
    margin = max(6, int(0.02 * min(h, w)))
    if substrate_removed:
        valid_mask = (
            (pts[:, 0] > margin) & (pts[:, 0] < w - margin) &
            (pts[:, 1] > top_margin)
        )
    else:
        valid_mask = (
            (pts[:, 0] > margin) & (pts[:, 0] < w - margin) &
            (pts[:, 1] > top_margin) & (pts[:, 1] < h - bottom_margin)
        )
    
    if np.sum(valid_mask) < 10:
        pts_final = pts
    else:
        pts_final = pts[valid_mask]
    
    if not substrate_removed:
        pts_final = _remover_faixa_horizontal_vazada(pts_final, h, w)
    return pts_final if len(pts_final) > 0 else None

def _validar_contorno(c, h: int, w: int) -> bool:
    """Critérios geométricos para aceitar um contorno como gota (area, circularidade, convexidade)."""
    area = float(cv2.contourArea(c))
    
    # Critério 1: Tamanho mínimo (gota muito pequena é inválida)
    if area < 100:
        return False
    
    # Critério 2: Bounding box válido
    x, y, bw, bh = cv2.boundingRect(c)
    if bw < 20 or bh < 20:
        return False
    
    # Critério 3: Razão altura/largura (gota não pode ser muito achatada)
    aspect_ratio = max(bw, bh) / max(1.0, min(bw, bh))
    if aspect_ratio > 8.0:  # Muito alongada = não é gota
        return False
    
    # Critério 4: Circularidade (4π*Area / Perímetro²)
    perimetro = cv2.arcLength(c, True)
    if perimetro < 20:
        return False
    circularidade = (4 * np.pi * area) / (perimetro ** 2)
    if circularidade < 0.25:  # Gotas hidrofóbicas/achatadas ainda devem passar
        return False
    
    # Critério 5: Convexidade (area real / area hull)
    hull = cv2.convexHull(c)
    hull_area = cv2.contourArea(hull)
    if hull_area > 0:
        convexidade = area / hull_area
        if convexidade < 0.7:  # Muito côncavo = ruído
            return False
    
    # Critério 6: Preenchimento no bounding box
    fill_ratio = area / (bw * bh)
    if fill_ratio < 0.5:  # Contorno oco = inválido
        return False

    # Critério 7: Rejeita contornos com "faixa de chão" no fundo da ROI.
    pts = c.reshape(-1, 2)
    y_max = float(np.max(pts[:, 1]))
    banda = max(2.0, 0.015 * h)
    fundo = pts[pts[:, 1] >= (y_max - banda)]
    if len(fundo) >= 12:
        span_ratio = float((np.max(fundo[:, 0]) - np.min(fundo[:, 0])) / max(1.0, w))
        fundo_ratio = float(len(fundo) / max(1, len(pts)))
        if y_max > 0.92 * h and span_ratio > 0.75 and fundo_ratio > 0.12:
            return False
    
    return True


def _margens_adaptativas(h: int, w: int):
    """Margens de exclusão proporcionais ao tamanho da ROI (topo, laterais, fundo)."""
    base = min(h, w)
    side = max(6, int(0.02 * base))
    bottom = max(2, int(0.005 * h))
    top = max(1, int(0.004 * h))
    return top, side, bottom


def _pontuacao_contorno(c, h: int, w: int) -> float:
    """Score de preferência: favorece maior área, altura e centralidade; penaliza faixa de chão."""
    area = float(cv2.contourArea(c))
    if area <= 0:
        return -1e9

    x, y, bw, bh = cv2.boundingRect(c)
    area_norm = area / float(max(1, h * w))
    altura_norm = bh / float(max(1, h))
    largura_norm = bw / float(max(1, w))
    cx = x + bw / 2.0
    centralidade = 1.0 - abs(cx - (w / 2.0)) / float(max(1, w / 2.0))

    # Penaliza faixa horizontal baixa muito larga (padrão de superfície/chão).
    penaliza_faixa = 1.0 if (largura_norm > 0.72 and altura_norm < 0.30 and y > 0.40 * h) else 0.0

    return (2.0 * area_norm) + (0.9 * altura_norm) + (0.6 * centralidade) - (2.0 * penaliza_faixa)


def avaliar_qualidade_contorno(pts: np.ndarray, img_shape) -> dict:
    """Score [0,1] e sinais de risco do contorno (encosta fundo/topo, faixa horizontal)."""
    if pts is None or len(pts) < 20:
        return {"score": 0.0, "risk_flags": ["contorno_insuficiente"]}

    h, w = int(img_shape[0]), int(img_shape[1])
    pts = np.asarray(pts)
    x_min, y_min = np.min(pts[:, 0]), np.min(pts[:, 1])
    x_max, y_max = np.max(pts[:, 0]), np.max(pts[:, 1])
    bw = max(1.0, x_max - x_min)
    bh = max(1.0, y_max - y_min)

    area_est = float(len(pts))
    fill_ratio = min(1.0, area_est / float(max(1, bw * bh)))
    altura_rel = min(1.0, bh / float(max(1, h)))
    largura_rel = min(1.0, bw / float(max(1, w)))

    risk_flags = []
    if y_max > 0.98 * h:
        risk_flags.append("encosta_fundo")
    if y_min < 0.01 * h:
        risk_flags.append("encosta_topo")
    if largura_rel > 0.90 and altura_rel < 0.35:
        risk_flags.append("faixa_horizontal")

    score = 0.45 * altura_rel + 0.30 * largura_rel + 0.25 * fill_ratio
    score = float(np.clip(score, 0.0, 1.0))
    if len(risk_flags) >= 2:
        score *= 0.75

    return {"score": score, "risk_flags": risk_flags}


def _remover_faixa_horizontal_vazada(pts: np.ndarray, h: int, w: int) -> np.ndarray:
    """Remove apenas vazamento horizontal no fundo, sem cortar o corpo da gota.

    DESATIVADO: o substrato é separado antes da extração do contorno;
    este filtro cortava a base real da gota impedindo contorno e linha vermelha
    de tocarem o chão.
    Para reativar em imagens com rugosidade de substrato: remover o 'return pts'
    abaixo e restaurar o corpo original.
    """
    # -- DESATIVADO -- reativar se necessário para imagens com rugosidade
    return pts


def encontrar_contorno_gota(imagem_binaria):
    """Fallback: maior contorno válido sem validação rigorosa de circularidade."""
    # Garante canal único
    if len(imagem_binaria.shape) == 3:
        img = cv2.cvtColor(imagem_binaria, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem_binaria.copy()

    # Passo 1: Fechamento morfológico LEVE.
    kernel = np.ones((3, 3), np.uint8)
    processed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1)

    # Máscara de segurança adaptativa por escala da ROI.
    h, w = processed.shape[:2]
    top_margin, side_margin, bottom_margin = _margens_adaptativas(h, w)
    processed[:top_margin, :] = 0
    processed[max(0, h - bottom_margin):, :] = 0
    processed[:, :side_margin] = 0
    processed[:, max(0, w - side_margin):] = 0

    # Passo 2: Encontrar contornos
    conts, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Fallback se a binarização falhou mas há bordas visíveis
    if not conts:
        edges = cv2.Canny(img, 30, 100)
        edges[:top_margin, :] = 0
        edges[max(0, h - bottom_margin):, :] = 0
        edges[:, :side_margin] = 0
        edges[:, max(0, w - side_margin):] = 0
        conts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if not conts:
        return None

    # NOVO: Filtrar contornos que tocam as bordas da imagem
    h, w = img.shape[:2]
    margin = max(4, int(0.01 * min(h, w)))
    MAX_BORDER_TOUCHES = 3  # Contornos que tocam 3+ bordas são considerados borda da imagem
    valid_contours = []

    for c in conts:
        pts = c.reshape(-1, 2)
        
        # Verificar se o contorno toca as bordas
        touches_left = np.any(pts[:, 0] <= margin)
        touches_right = np.any(pts[:, 0] >= w - margin)
        touches_top = np.any(pts[:, 1] <= margin)
        touches_bottom = np.any(pts[:, 1] >= h - margin)
        
        # Se tocar 3 ou mais bordas, provavelmente é a borda da imagem (não a gota)
        border_count = sum([touches_left, touches_right, touches_top, touches_bottom])
        
        # Rejeita faixa de superfície: muito larga, baixa e achatada.
        x, y, bw, bh = cv2.boundingRect(c)
        faixa_superficie = (bw > 0.70 * w) and (bh < 0.30 * h) and (y > 0.35 * h)
        ancora_no_fundo = touches_bottom and (bw > 0.60 * w)

        if border_count < MAX_BORDER_TOUCHES and not faixa_superficie and not ancora_no_fundo:
            valid_contours.append(c)

    if not valid_contours:
        return None

    # Passo 3: Selecionar o melhor contorno válido por score geométrico
    c = max(valid_contours, key=lambda cc: _pontuacao_contorno(cc, h, w))

    # Passo 4: Filtrar ruído - contornos muito pequenos são desprezados
    if cv2.contourArea(c) < 100:
        return None

    # Retorna os pontos do contorno como array Nx2
    pts = c.reshape(-1, 2)
    
    # VALIDAÇÃO EXTRA: Garantir que nenhum ponto está pegando nas bordas
    # Remove pontos que estão muito perto das extremidades (10px de margem)
    margin = max(6, int(0.02 * min(h, w)))
    valid_mask = (
        (pts[:, 0] > margin) & (pts[:, 0] < w - margin) &  # Esquerda e direita
        (pts[:, 1] > top_margin)  # bottom_margin desativado: impedia chegar à superfície real
        # & (pts[:, 1] < h - bottom_margin)  -- DESATIVADO
    )
    
    if np.sum(valid_mask) < 10:  # Se remover muito, não vale a pena
        pts_final = pts
    else:
        pts_final = pts[valid_mask]

    # _remover_faixa_horizontal_vazada desativada (veja a função)
    pts_final = _remover_faixa_horizontal_vazada(pts_final, h, w)
    return pts_final if len(pts_final) > 0 else pts