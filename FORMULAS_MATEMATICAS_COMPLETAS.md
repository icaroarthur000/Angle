# LISTA COMPLETA DE FORMULAS MATEMATICAS

## 1. PROCESSAMENTO DE IMAGEM - filtros.py

| Formula | Localizacao | Uso |
|---|---|---|
| `Blurred = GaussianBlur(Gray, kernel=5x5, sigma=0)` | `filtros.py` | Suavizacao para reduzir ruido |
| `Binary = OTSU_INV(Blurred)` | `filtros.py` | Binarizacao automatica invertida |
| `Closed = MORPH_CLOSE(Binary, kernel=elipse 5x5, iter=1)` | `filtros.py` | Fechamento para selar a gota |

## 2. PROCESSAMENTO AVANCADO - preprocess.py

| Formula | Localizacao | Uso |
|---|---|---|
| `k_bg = max(51, floor(min(h, w)/6) OR 1)` | `preprocess.py` | Tamanho do kernel de fundo (impar e proporcional) |
| `k_bg = bg_ksize (se impar) senao (bg_ksize + 1)` | `preprocess.py` | Correcao para kernel impar |
| `Bg = GaussianBlur(Gray, kernel=k_bg x k_bg, sigma=0)` | `preprocess.py` | Estimativa do fundo iluminacao |
| `C(x,y) = ((I(x,y) + 1) / (B(x,y) + 1)) * 128` | `preprocess.py` | Correcao de iluminacao por divisao |
| `tile = max(1, floor(min(h, w)/50))` | `preprocess.py` | Escala de grid do CLAHE |
| `tg = (min(8, tile), min(8, tile))` | `preprocess.py` | Limite do grid do CLAHE |
| `k_adapt = max(31, floor(min(h, w)/30) OR 1)` | `preprocess.py` | Janela do limiar adaptativo |
| `blockSize = adapt_blocksize (se impar) senao (adapt_blocksize + 1)` | `preprocess.py` | Garantia de bloco impar |
| `max_allowed = max(3, min(h, w) - (1 se min(h,w) for par senao 0))` | `preprocess.py` | Limite maximo valido do bloco |
| `Binary = AdaptiveThreshold_Gaussian(Enhanced, 255, THRESH_BINARY_INV, blockSize, C=adapt_C)` | `preprocess.py` | Limiar adaptativo |
| `Opened = MORPH_OPEN(Binary, kernel=elipse 3x3, iter=1)` | `preprocess.py` | Limpeza morfologica |
| `Closed = MORPH_CLOSE(Opened, kernel=elipse 3x3, iter=1)` | `preprocess.py` | Selagem final da mascara |

## 3. DETECCAO DE CONTORNO - contorno.py

| Formula | Localizacao | Uso |
|---|---|---|
| `processed = MORPH_CLOSE(img, kernel=ones 3x3, iter=1)` | `contorno.py` | Fechamento leve antes de contornos |
| `processed = rectangle_border_zero(processed, espessura=10)` | `contorno.py` | Mascara de seguranca nas bordas |
| `edges = Canny(img, threshold1=30, threshold2=100)` | `contorno.py` | Fallback por bordas |
| `border_count = [touch_left] + [touch_right] + [touch_top] + [touch_bottom]` | `contorno.py` | Contagem de bordas tocadas |
| `contorno valido se border_count < 3` | `contorno.py` | Remove borda da imagem mascarada como contorno |
| `valid_mask = (10 < x < w-10) AND (10 < y < h-10)` | `contorno.py` | Filtra pontos proximos das extremidades |

## 4. LINHA BASE E CONTATO - linha_base.py

| Formula | Localizacao | Uso |
|---|---|---|
| `dist = hypot(dx, dy)` | `linha_base.py` | Norma do vetor para normalizacao |
| `v_norm = (dx/dist, dy/dist)` se `dist >= eps`, senao `(1, 0)` | `linha_base.py` | Normalizacao segura |
| `Y_baseline = max(Y_i)` | `linha_base.py` | Floor-seeker da baseline |
| `floor_pts: abs(Y_i - Y_baseline) <= 5` | `linha_base.py` | Selecao de pontos proximos ao piso |
| `x0 = mean(X_floor)` | `linha_base.py` | Centro horizontal da faixa de contato |
| `y_roi_bottom = y_max - roi_bottom * altura` | `linha_base.py` | Limite inferior da ROI |
| `y_roi_top = y_min + roi_top * altura` | `linha_base.py` | Limite superior da ROI |
| `x_center = mean(X_contorno)` | `linha_base.py` | Separacao esquerda/direita |
| `X(Y) = a*Y^2 + b*Y + c` (polyfit grau 2) | `linha_base.py` | Extrapolacao de cada lado |
| `X_contato = X(Y_baseline)` | `linha_base.py` | Intersecao extrapolada com baseline |
| `dist = abs(X_lado - x_center)` | `linha_base.py` | Distancia lateral para espelhamento |
| `P_espelhado = [x_center +/- dist, Y_baseline]` | `linha_base.py` | Fallback quando um lado falha |
| `near_baseline: abs(Y - baseline_y) < 5` | `linha_base.py` | Fallback geometrico |
| `band_pts: Y >= (Y_max - band_px)` | `linha_base.py` | Faixa inferior para compatibilidade |

## 5. AJUSTE CIRCULAR E ANGULO - angulo_contato.py

| Formula | Localizacao | Uso |
|---|---|---|
| `u = x - mean(x)` e `v = y - mean(y)` | `angulo_contato.py` | Centralizacao para estabilidade numerica |
| `Suu = sum(u^2), Svv = sum(v^2), Suv = sum(u*v)` | `angulo_contato.py` | Termos da matriz de Kasa |
| `Suuu = sum(u^3), Svvv = sum(v^3), Suvv = sum(u*v^2), Suuv = sum(u^2*v)` | `angulo_contato.py` | Termos do vetor independente |
| `A = [[Suu, Suv], [Suv, Svv]]` | `angulo_contato.py` | Sistema linear do ajuste circular |
| `B = [(Suuu + Suvv), (Svvv + Suuv)] / 2` | `angulo_contato.py` | Lado direito do sistema |
| `[uc, vc] = solve(A, B)` | `angulo_contato.py` | Centro no sistema centralizado |
| `xc = mean(x) + uc`, `yc = mean(y) + vc` | `angulo_contato.py` | Centro no sistema original |
| `R = mean(sqrt((x - xc)^2 + (y - yc)^2))` | `angulo_contato.py` | Raio medio fisico |
| `dx_dy = 2*a*baseline_y + b` | `angulo_contato.py` | Derivada do fallback polinomial |
| `theta = atan(1/dx_dy)` (ou `pi/2` se `dx_dy = 0`) | `angulo_contato.py` | Angulo no fallback |
| `baseline_ajustada = baseline_y + 3` | `angulo_contato.py` | Compensacao de calibracao |
| `mask = (Y < baseline_ajustada - 3) AND (Y > baseline_ajustada - 150)` | `angulo_contato.py` | Janela local de ajuste |
| `center_x_approx = (x_esq + x_dir)/2` | `angulo_contato.py` | Separacao por lado |
| `dist_i = hypot(x_i - xc0, y_i - yc0)` | `angulo_contato.py` | Distancia radial para residuos |
| `residual_i = abs(dist_i - R0)` | `angulo_contato.py` | Erro radial |
| `inlier se residual_i <= 2*sigma` | `angulo_contato.py` | Filtro sigma |
| `dy = baseline_ajustada - yc` | `angulo_contato.py` | Distancia vertical baseline-centro |
| `dx = sqrt(max(0, R^2 - dy^2))` | `angulo_contato.py` | Intersecao circulo-reta |
| `x_contato = xc - dx` (esq) ou `xc + dx` (dir) | `angulo_contato.py` | Contato sub-pixel |
| `m_tangente = -(x_contato - xc)/(baseline_ajustada - yc)` | `angulo_contato.py` | Derivada implicita da tangente |
| `theta = degrees(atan(abs(m_tangente)))` | `angulo_contato.py` | Angulo de contato base |
| `theta = 180 - theta` se `yc > baseline_ajustada` | `angulo_contato.py` | Ajuste de quadrante |
| `theta_final = clip(theta, 0, 180)` | `angulo_contato.py` | Limitacao fisica |

## 6. VISUALIZACAO - desenho.py

| Formula | Localizacao | Uso |
|---|---|---|
| `y_scr = baseline_y * ratio + offset_y` | `desenho.py` | Projecao vertical da baseline |
| `x_end = offset_x + image_width * ratio` | `desenho.py` | Extensao horizontal da baseline |
| `length = 50 / zoom_scale` | `desenho.py` | Comprimento visual da tangente |
| `angle_rad = radians(angulo)` | `desenho.py` | Conversao para trigonometria |
| Lado esquerdo: `dx = length*cos(angle_rad)`, `dy = -length*sin(angle_rad)` | `desenho.py` | Vetor tangente esquerdo |
| Lado direito: `dx = -length*cos(angle_rad)`, `dy = -length*sin(angle_rad)` | `desenho.py` | Vetor tangente direito |
| `P1 = (x - 0.2*dx, y - 0.2*dy)`, `P2 = (x + dx, y + dy)` | `desenho.py` | Segmento desenhado da tangente |

## 7. CONVERSOES E ESCALA DE TELA - main.py

| Formula | Localizacao | Uso |
|---|---|---|
| `ratio = min(canvas_w/img_w, canvas_h/img_h)` | `main.py` | Ajuste de imagem na area util |
| `ratio_zoom = min(canvas_w/img_w, canvas_h/img_h) * zoom_scale` | `main.py` | Escala com zoom |
| `offset_x = (canvas_w - new_w)/2`, `offset_y = (canvas_h - new_h)/2` | `main.py` | Centralizacao da imagem |
| `x_img = (x_canvas - offset_x)/ratio`, `y_img = (y_canvas - offset_y)/ratio` | `main.py` | Conversao Tela -> Imagem |
| `x_img = clip(x_img, 0, w-1)`, `y_img = clip(y_img, 0, h-1)` | `main.py` | Limite da coordenada na imagem |
| `to_scr(x,y) = (x*ratio + ox, y*ratio + oy)` | `main.py` | Conversao Imagem -> Tela |
| `img_radius = screen_radius / ratio_local` | `main.py` | Raio de clique consistente no zoom |
| `dist = hypot(x_img - x_p, y_img - y_p)` | `main.py` | Deteccao de clique proximo ao ponto |
| `baseline_y = (y_esq + y_dir)/2` | `main.py` | Recalculo da baseline no arraste manual |
