import cv2
import numpy as np
from parametros import obter

# Limiar mínimo de circularidade para validar contorno de gota.
# O valor 0.35 aceita gotas hidrofílicas muito achatadas (Anglo < 30°) sem rejeitar ruído.
MIN_CIRCULARITY: float = float(obter("min_circularity", 0.35))


# =================================================================
# PIPELINE DE SEPARAÇÃO GOTA-SUBSTRATO (Cascata Tripla)
# Técnica A: Necking (perfil de largura)
# Técnica B: Sobel Y (gradiente direcional)
# Técnica C: Abertura Anisotrópica (quebra de pontes morfológicas)
# =================================================================

def _necking_detection(img_bin):
    """Técnica A: Detecta o 'pescoço' da gota pelo perfil de largura por linha.
    Retorna (y_neck, confianca) ou (-1, 0.0) se não encontrar."""
    h, w = img_bin.shape[:2]
    if h < 30 or w < 30:
        return -1, 0.0

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
    """Técnica B: Detecta a superfície física por gradiente Sobel na direção Y.
    Opera na imagem cinza ORIGINAL (independente do Otsu).
    Retorna (y_sobel, confianca) ou (-1, 0.0)."""
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

    # Projeção horizontal: soma dos gradientes por linha
    projecao = np.sum(sobel_abs, axis=1)

    if len(projecao) < 5:
        return -1, 0.0

    # Suaviza para reduzir ruído
    k = np.array([1, 2, 3, 2, 1], dtype=np.float64)
    projecao = np.convolve(projecao, k / k.sum(), mode="same")

    media_geral = float(np.mean(projecao))
    if media_geral < 1e-6:
        return -1, 0.0

    # Busca o pico mais forte na metade inferior da projeção
    # (a superfície é tipicamente a borda horizontal mais intensa na parte baixa)
    meio_proj = len(projecao) // 2
    subproj = projecao[meio_proj:]
    if len(subproj) < 3:
        return -1, 0.0

    idx_pico = meio_proj + int(np.argmax(subproj))
    pico_val = float(projecao[idx_pico])

    y_sobel = y_start + idx_pico

    # Confiança = proeminência do pico sobre a média
    confianca = float(np.clip((pico_val / media_geral - 1.0) / 3.0, 0.0, 1.0))

    return y_sobel, confianca


def _abertura_anisotropica(img_bin, kernel_size=(9, 3)):
    """Técnica C: Abertura morfológica com kernel largo e curto para
    quebrar pontes horizontais entre gota e substrato.
    Retorna (img_limpa, y_base_contorno, confianca)."""
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
    """Pipeline de separação Gota-Substrato por cascata tripla.

    Combina Necking + Sobel Y + Abertura Anisotrópica com decisor
    por confiança para encontrar a linha de corte real.

    Args:
        img_gray: imagem em escala de cinza (original, pré-binarização)
        img_bin: imagem binária (ex: Otsu) possivelmente com gota+substrato colados

    Returns:
        Máscara binária com substrato removido abaixo da linha de corte.
    """
    if img_bin is None:
        return img_bin
    h, w = img_bin.shape[:2]
    if h < 30 or w < 30:
        return img_bin

    # --- Técnica C: Abertura anisotrópica (dá estimativa de contorno limpo) ---
    bin_morf, y_base_morf, conf_morf = _abertura_anisotropica(img_bin)

    # --- Técnica A: Necking (perfil de largura na imagem pós-morfologia) ---
    y_neck, conf_neck = _necking_detection(bin_morf)

    # --- Técnica B: Sobel Y (gradiente na imagem cinza original) ---
    y_sobel, conf_sobel = -1, 0.0
    if img_gray is not None and img_gray.shape[:2] == img_bin.shape[:2]:
        y_sobel, conf_sobel = _sobel_y_surface(img_gray)

    # --- Decisor por confiança ---
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
    bin_limpa[y_corte + 1:, :] = 0

    # Se restar menos de 300 pixels acima do corte, provavelmente amputou a gota
    if fg_acima < 300:
        return bin_morf

    return bin_limpa


def remover_substrato_abaixo_superficie(imagem_binaria, img_gray=None):
    """Zera conteúdo abaixo da superfície usando o pipeline de cascata tripla.

    Mantém interface retrocompatível: aceita img_gray opcional.
    Se img_gray não for fornecido, usa apenas técnicas que operam na binária.
    """
    if imagem_binaria is None:
        return imagem_binaria, None

    if len(imagem_binaria.shape) == 3:
        base = cv2.cvtColor(imagem_binaria, cv2.COLOR_BGR2GRAY)
    else:
        base = imagem_binaria.copy()

    resultado = isolar_gota_substrato(img_gray, base)

    # Estima y_surface para retrocompatibilidade (onde o corte foi feito)
    diff = (base > 0).astype(np.int16) - (resultado > 0).astype(np.int16)
    linhas_cortadas = np.where(np.any(diff > 0, axis=1))[0]
    y_surface = int(linhas_cortadas[0]) if len(linhas_cortadas) > 0 else None

    return resultado, y_surface


def extrair_mascara_gota(imagem_binaria, img_gray=None):
    """Retorna máscara sólida apenas da gota e os pontos de contorno usados.

    Args:
        imagem_binaria: máscara binária (pode conter gota+substrato colados)
        img_gray: imagem cinza original (opcional, melhora a separação via Sobel)
    """
    if imagem_binaria is None:
        return None, None

    if len(imagem_binaria.shape) == 3:
        base = cv2.cvtColor(imagem_binaria, cv2.COLOR_BGR2GRAY)
    else:
        base = imagem_binaria.copy()

    # Aplica pipeline de separação tripla
    base_clean = isolar_gota_substrato(img_gray, base)

    pts = encontrar_contorno_gota_robusto(base_clean)
    if pts is None:
        pts = encontrar_contorno_gota(base_clean)

    if pts is None or len(pts) < 10:
        return base_clean, None

    mask = np.zeros(base_clean.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [pts.astype(np.int32)], 255)
    return mask, pts


# =================================================================
# NOVA FUNÇÃO: Busca Robusta de Contorno (com Validação)
# =================================================================
def encontrar_contorno_gota_robusto(imagem_binaria):
    """
    Versão ROBUSTA de detecção de contorno.
    - Usa validação rigorosa de contorno
    - Filtra contornos inválidos (pequenos, não-circulares)
    - Melhor para gotas de tamanhos variados
    
    Retorna: Array de pontos ou None se falhar
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
    #processed[max(0, h - bottom_margin):, :] = 0
    processed[:, :side_margin] = 0
    processed[:, max(0, w - side_margin):] = 0
    
    # Busca contornos
    conts, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if not conts:
        edges = cv2.Canny(img, 30, 100)
        edges[:top_margin, :] = 0
        #edges[max(0, h - bottom_margin):, :] = 0
        edges[:, :side_margin] = 0
        edges[:, max(0, w - side_margin):] = 0
        conts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if not conts:
        return None
    
    # FILTRO NOVO: Validar contornos
    valid_contours = []
    for c in conts:
        # Rejeita contornos que não parecem gotas
        if _validar_contorno(c, h, w):
            pts = c.reshape(-1, 2)
            
            # Verifica apenas topo e laterais; o fundo pode tocar a base da gota.
            margin = max(4, int(0.01 * min(h, w)))
            touches = (np.any(pts[:, 0] <= margin) or np.any(pts[:, 0] >= w - margin) or
                      np.any(pts[:, 1] <= margin))
            touches_bottom = np.any(pts[:, 1] >= h - margin)
            
            x, y, bw, bh = cv2.boundingRect(c)
            faixa_superficie = (bw > 0.70 * w) and (bh < 0.30 * h) and (y > 0.35 * h)
            ancora_no_fundo = touches_bottom and (bw > 0.60 * w)
            
            if not touches and not faixa_superficie:
                valid_contours.append(c)
    
    if not valid_contours:
        return None
    
    # Seleciona melhor contorno válido por score geométrico (evita pegar superfície/chão).
    c = max(valid_contours, key=lambda cc: _pontuacao_contorno(cc, h, w))
    pts = c.reshape(-1, 2)
    
    # Limpa pontos nas bordas
    margin = max(6, int(0.02 * min(h, w)))
    valid_mask = (
        (pts[:, 0] > margin) & (pts[:, 0] < w - margin) &
        (pts[:, 1] > top_margin) & (pts[:, 1] < h)
    )
    
    if np.sum(valid_mask) < 10:
        pts_final = pts
    else:
        pts_final = pts[valid_mask]
    
    #pts_final = _remover_faixa_horizontal_vazada(pts_final, h, w)#
    return pts_final if len(pts_final) > 0 else None

def _validar_contorno(c, h: int, w: int) -> bool:
    """
    Verifica se um contorno é válido para ser uma gota.
    Retorna True se válido, False caso contrário.
    """
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
    if circularidade < MIN_CIRCULARITY:  # Muito irregular = não é gota
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
        if y_max > 0.92 * h and span_ratio > 0.75 and fundo_ratio > 0.12 and bh < 0.30 * h:
            return False
    
    return True


def _margens_adaptativas(h: int, w: int):
    """Define margens de proteção proporcionais ao tamanho da ROI."""
    base = min(h, w)
    side = max(6, int(0.02 * base))
    bottom = max(2, int(0.005 * h))
    top = max(1, int(0.004 * h))
    return top, side, bottom


def _pontuacao_contorno(c, h: int, w: int) -> float:
    """Score geométrico para escolher contorno de gota (evita faixa de chão)."""
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
    """Retorna score [0,1] e sinais de risco do contorno detectado."""
    if pts is None or len(pts) < 20:
        return {"score": 0.0, "risk_flags": ["contorno_insuficiente"]}

    h, w = int(img_shape[0]), int(img_shape[1])
    pts = np.asarray(pts)
    x_min, y_min = np.min(pts[:, 0]), np.min(pts[:, 1])
    x_max, y_max = np.max(pts[:, 0]), np.max(pts[:, 1])
    bw = max(1.0, x_max - x_min)
    bh = max(1.0, y_max - y_min)

    area_est = float(cv2.contourArea(pts.astype(np.float32).reshape(-1, 1, 2)))
    if area_est == 0.0:
        area_est = float(len(pts))  # fallback seguro se contorArea retornar 0
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
    """Remove apenas vazamento horizontal no fundo, sem cortar o corpo da gota."""
    if pts is None or len(pts) < 20:
        return pts

    y_max = float(np.max(pts[:, 1]))
    banda = max(2.0, 0.01 * h)
    fundo = pts[pts[:, 1] >= (y_max - banda)]
    if len(fundo) < 12:
        return pts

    x_span = float(np.max(fundo[:, 0]) - np.min(fundo[:, 0]))
    vazou_superficie = x_span > 0.78 * w
    if not vazou_superficie:
        return pts

    # Remove só a faixa horizontal central; preserva regiões laterais de contato.
    y_cut = y_max - banda
    x_q10 = float(np.quantile(fundo[:, 0], 0.10))
    x_q90 = float(np.quantile(fundo[:, 0], 0.90))
    margem_lateral = max(4.0, 0.03 * w)
    x_left_keep = x_q10 + margem_lateral
    x_right_keep = x_q90 - margem_lateral

    faixa_inferior = pts[:, 1] >= y_cut
    miolo_horizontal = (pts[:, 0] >= x_left_keep) & (pts[:, 0] <= x_right_keep)
    remover = faixa_inferior & miolo_horizontal
    keep = ~remover
    pts2 = pts[keep]
    return pts2 if len(pts2) >= 20 else pts


def encontrar_contorno_gota(imagem_binaria):
    """
    Encontra o maior contorno da gota com máscara de segurança nas bordas.
    
    A máscara de 5px força fisicamente a separação da gota do frame da imagem,
    garantindo que nenhum contorno toque nas bordas (especialmente o fundo).
    """
    # Garante que a imagem seja 8-bit single channel
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
    processed[:, :side_margin] = 0
    processed[:, max(0, w - side_margin):] = 0

    # Passo 2: Encontrar contornos
    conts, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Fallback se a binarização falhou mas há bordas visíveis
    if not conts:
        edges = cv2.Canny(img, 30, 100)
        edges[:top_margin, :] = 0
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
        
        # Verificar se o contorno toca as bordas laterais ou o topo.
        touches_left = np.any(pts[:, 0] <= margin)
        touches_right = np.any(pts[:, 0] >= w - margin)
        touches_top = np.any(pts[:, 1] <= margin)
        
        # Se tocar 3 ou mais dessas bordas, provavelmente é a borda da imagem (não a gota)
        border_count = sum([touches_left, touches_right, touches_top])
        
        # Rejeita faixa de superfície: muito larga, baixa e achatada.
        x, y, bw, bh = cv2.boundingRect(c)
        faixa_superficie = (bw > 0.70 * w) and (bh < 0.30 * h) and (y > 0.35 * h)
        if border_count < MAX_BORDER_TOUCHES and not faixa_superficie:
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
        (pts[:, 1] > top_margin) & (pts[:, 1] < h)     # Topo e fundo
    )
    
    if np.sum(valid_mask) < 10:  # Se remover muito, não vale a pena
        pts_final = pts
    else:
        pts_final = pts[valid_mask]

    # Remove apenas vazamento horizontal de superfície (quando existir)
    pts_final = _remover_faixa_horizontal_vazada(pts_final, h, w)
    return pts_final if len(pts_final) > 0 else pts


def avaliar_transicao_contato(ponto, gota_pts, baseline_y, indice=None):
    """Avalia se um ponto pertence à transição gota-substrato, não ao piso horizontal."""
    if gota_pts is None or len(gota_pts) < 3 or ponto is None:
        return {"valida": False, "qualidade": 0.0, "motivo": "dados_ausentes"}

    pontos = np.asarray(gota_pts, dtype=float)
    alvo = np.asarray(ponto[:2], dtype=float)
    if indice is None:
        indice = int(np.argmin(np.linalg.norm(pontos - alvo, axis=1)))

    anterior = pontos[(indice - 1) % len(pontos)]
    seguinte = pontos[(indice + 1) % len(pontos)]
    raio_transicao = min(5, max(1, len(pontos) // 20))
    vizinhanca = [
        pontos[(indice - deslocamento) % len(pontos)]
        for deslocamento in range(1, raio_transicao + 1)
    ] + [
        pontos[(indice + deslocamento) % len(pontos)]
        for deslocamento in range(1, raio_transicao + 1)
    ]
    horizontais = int(abs(anterior[1] - alvo[1]) <= 1.0) + int(abs(seguinte[1] - alvo[1]) <= 1.0)
    ascendente = any(abs(float(alvo[1] - vizinho[1])) > 1.0 for vizinho in vizinhanca)
    distancia_baseline = abs(float(alvo[1]) - float(baseline_y))
    qualidade = 1.0
    qualidade -= 0.35 * horizontais
    qualidade += 0.15 if ascendente else -0.15
    qualidade -= min(0.5, distancia_baseline / 20.0)
    qualidade = float(np.clip(qualidade, 0.0, 1.0))
    transicao_valida = ascendente and distancia_baseline <= 12.0
    return {
        "valida": bool(transicao_valida),
        "qualidade": qualidade,
        "motivo": "ok" if transicao_valida else "fechamento_horizontal",
        "indice": int(indice),
        "vizinhos_horizontais": horizontais,
        "ascendente": bool(ascendente),
        "distancia_baseline": float(distancia_baseline),
    }


def projetar_ponto_no_contorno(ponto, gota_pts, baseline_y,
                               tolerancia_px=2.0, faixa_baseline_px=30.0):
    """Valida se ponto está dentro da tolerância do contorno.
    Se não estiver, projeta para o ponto válido mais próximo na faixa inferior.

    Retorna (ponto_final, corrigido_bool).
    """
    if gota_pts is None or len(gota_pts) == 0:
        return ponto, False

    px, py = float(ponto[0]), float(ponto[1])
    mask = gota_pts[:, 1] >= (baseline_y - faixa_baseline_px)
    candidatos_faixa = gota_pts[mask] if np.any(mask) else gota_pts
    candidatos = candidatos_faixa if len(candidatos_faixa) >= 3 else gota_pts
    indices_candidatos = np.flatnonzero(mask) if np.any(mask) and len(candidatos_faixa) >= 3 else np.arange(len(gota_pts))
    centro_x = float(np.mean(gota_pts[:, 0]))

    # Mantém o ponto no mesmo lado e força o encaixe na transicao inferior do contorno.
    if px < centro_x:
        lado_mask = candidatos[:, 0] <= centro_x
    else:
        lado_mask = candidatos[:, 0] >= centro_x

    if np.count_nonzero(lado_mask) >= 3:
        candidatos = candidatos[lado_mask]
        indices_candidatos = indices_candidatos[lado_mask]

    baseline_dist = np.abs(candidatos[:, 1] - float(baseline_y))
    scores = baseline_dist + 0.5 * np.hypot(candidatos[:, 0] - px, candidatos[:, 1] - py)
    for local_idx, point in enumerate(candidatos):
        original_idx = int(indices_candidatos[local_idx]) if local_idx < len(indices_candidatos) else None
        if original_idx is None:
            continue
        previous = gota_pts[(original_idx - 1) % len(gota_pts)]
        following = gota_pts[(original_idx + 1) % len(gota_pts)]
        transition_neighbors = [
            gota_pts[(original_idx - offset) % len(gota_pts)]
            for offset in range(1, min(5, max(1, len(gota_pts) // 20)) + 1)
        ] + [
            gota_pts[(original_idx + offset) % len(gota_pts)]
            for offset in range(1, min(5, max(1, len(gota_pts) // 20)) + 1)
        ]
        horizontal_neighbors = int(abs(previous[1] - point[1]) <= 1.0) + int(abs(following[1] - point[1]) <= 1.0)
        rising_neighbor = any(abs(float(point[1] - neighbor[1])) > 1.0 for neighbor in transition_neighbors)
        scores[local_idx] += 12.0 * horizontal_neighbors
        if rising_neighbor:
            scores[local_idx] -= 4.0

    idx = int(np.argmin(scores))
    ponto_final = [float(candidatos[idx, 0]), float(candidatos[idx, 1])]

    indice_original = int(np.argmin(np.linalg.norm(gota_pts - np.asarray([px, py]), axis=1)))
    qualidade_original = avaliar_transicao_contato(
        [px, py], gota_pts, baseline_y, indice=indice_original
    )
    dentro_tolerancia = (
        abs(ponto_final[0] - px) <= tolerancia_px
        and abs(ponto_final[1] - py) <= tolerancia_px
    )
    if dentro_tolerancia and qualidade_original["valida"]:
        return ponto_final, False

    return ponto_final, True


def extrair_perfil_liquido_ar(gota_pts, p_esq, p_dir, baseline_y, margem_px=2.0,
                               indice_esq=None, indice_dir=None):
    """Retorna o caminho do contorno que representa o arco liquido-ar.

    O contorno bruto pode ser fechado pela mascara Binary. Entre os indices
    mais proximos dos contatos, escolhe-se o caminho que contem a elevacao da
    gota acima da baseline e rejeita-se o fechamento inferior sobre o substrato.

    Se `indice_esq`/`indice_dir` forem informados (ancora ja validada), sao
    usados diretamente; a busca por distancia so ocorre como fallback.
    """
    resultado_invalido = {"valida": False, "motivo": "geometria_invalida", "indices": []}
    if gota_pts is None or len(gota_pts) < 5 or p_esq is None or p_dir is None:
        resultado_invalido["motivo"] = "dados_ausentes"
        return np.empty((0, 2), dtype=float), resultado_invalido

    pontos = np.asarray(gota_pts, dtype=float)
    contato_esq = np.asarray(p_esq[:2], dtype=float)
    contato_dir = np.asarray(p_dir[:2], dtype=float)
    baseline = float(baseline_y)
    if not np.isfinite(pontos).all() or not np.isfinite(contato_esq).all() or not np.isfinite(contato_dir).all() or not np.isfinite(baseline):
        resultado_invalido["motivo"] = "valores_nao_finitos"
        return np.empty((0, 2), dtype=float), resultado_invalido
    if contato_esq[0] >= contato_dir[0]:
        resultado_invalido["motivo"] = "contatos_fora_de_ordem"
        return np.empty((0, 2), dtype=float), resultado_invalido

    if indice_esq is not None and 0 <= int(indice_esq) < len(pontos):
        idx_esq = int(indice_esq)
    else:
        idx_esq = int(np.argmin(np.linalg.norm(pontos - contato_esq, axis=1)))
    if indice_dir is not None and 0 <= int(indice_dir) < len(pontos):
        idx_dir = int(indice_dir)
    else:
        idx_dir = int(np.argmin(np.linalg.norm(pontos - contato_dir, axis=1)))
    if idx_esq <= idx_dir:
        caminhos = (
            list(range(idx_esq, idx_dir + 1)),
            list(range(idx_dir, len(pontos))) + list(range(0, idx_esq + 1)),
        )
    else:
        caminhos = (
            list(range(idx_esq, len(pontos))) + list(range(0, idx_dir + 1)),
            list(range(idx_dir, idx_esq + 1)),
        )

    candidatos = []
    for caminho in caminhos:
        trecho = pontos[caminho]
        acima = trecho[:, 1] < baseline - margem_px
        abaixo = trecho[:, 1] > baseline + margem_px
        if len(trecho) < 5 or int(np.count_nonzero(acima)) < 5:
            continue
        # Penaliza o fechamento inferior e privilegia o ramo elevado da gota.
        score = int(np.count_nonzero(acima)) - 2 * int(np.count_nonzero(abaixo))
        candidatos.append((score, caminho))

    if not candidatos:
        resultado_invalido["motivo"] = "perfil_superior_ausente"
        return np.empty((0, 2), dtype=float), resultado_invalido

    candidatos.sort(key=lambda item: item[0], reverse=True)
    if len(candidatos) > 1 and candidatos[0][0] <= candidatos[1][0]:
        resultado_invalido["motivo"] = "perfil_ambiguo"
        return np.empty((0, 2), dtype=float), resultado_invalido

    indices = candidatos[0][1]
    # Normaliza para que o perfil sempre comece na ancora esquerda e termine na direita.
    if indices[0] == idx_dir and indices[-1] == idx_esq:
        indices = list(reversed(indices))
    perfil = pontos[indices]
    resultado = {
        "valida": True,
        "motivo": "ok",
        "indices": indices,
        "pontos": int(len(perfil)),
        "contato_esq_idx": idx_esq,
        "contato_dir_idx": idx_dir,
        "indice_perfil_esq": 0,
        "indice_perfil_dir": int(len(perfil) - 1),
        "contato_esq_fisico": bool(np.linalg.norm(pontos[idx_esq] - contato_esq) <= 2.0),
        "contato_dir_fisico": bool(np.linalg.norm(pontos[idx_dir] - contato_dir) <= 2.0),
    }
    return perfil, resultado