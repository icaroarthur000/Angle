# LISTA COMPLETA DE FORMULAS MATEMATICAS 


Fontes: codigo Python atual + config.json

## 1. PROCESSAMENTO DE IMAGEM - filtros.py

| Formula | Localizacao | Uso |
|---|---|---|
| `Gray = cvtColor(BGR, BGR2GRAY)` | `filtros.py` | Conversao para cinza |
| `Blur = GaussianBlur(Gray, kernel=5x5, sigma=0)` | `filtros.py` | Suavizacao de ruido |
| `Binary = OTSU_INV(Blur)` | `filtros.py` | Binarizacao automatica invertida |
| `Closed = MORPH_CLOSE(Binary, kernel=elipse 5x5, iter=1)` | `filtros.py` | Selagem da mascara |
| `Adaptive = AdaptiveThresholdGaussian(Blur, THRESH_BINARY_INV, blockSize, C=2)` | `filtros.py` | Binarizacao adaptativa |
| `Edges = Canny(Blur, 30, 100)` | `filtros.py` | Extracao de bordas |

## 2. SCORE DE MASCARA E SELECAO AUTOMATICA - filtros.py

| Formula | Localizacao | Uso |
|---|---|---|
| `fill = white_pixels / total_pixels` | `filtros.py` | Taxa de preenchimento da mascara |
| `rejeita se fill < 0.03 ou fill > 0.92` | `filtros.py` | Elimina mascaras inviaveis |
| `entropy = -sum(p_i * log2(p_i))` | `filtros.py` | Penalizacao de ruido |
| `score = 0.7*fill - 0.3*(entropy/8)` | `filtros.py` | Ranking das mascaras |
| `mask = argmax(score) em {OTSU, ADAPTIVE, CANNY}` | `filtros.py` | Escolha do melhor metodo |

## 3. PROCESSAMENTO  - preprocess.py

| Formula | Localizacao | Uso |
|---|---|---|
| `k_bg = max(51, floor(min(h, w)/6) OR 1)` | `preprocess.py` | Kernel de estimativa de fundo |
| `Bg = GaussianBlur(Gray, kernel=k_bg x k_bg, sigma=0)` | `preprocess.py` | Fundo de iluminacao |
| `Corrected = ((Gray + 1) / (Bg + 1)) * 128` | `preprocess.py` | Correcao por divisao |
| `tile = max(1, floor(min(h,w)/50))` | `preprocess.py` | Escala do CLAHE |
| `tileGrid = (min(8,tile), min(8,tile))` | `preprocess.py` | Grade do CLAHE |
| `blockSize = max(31, floor(min(h,w)/30) OR 1)` | `preprocess.py` | Janela da limiarizacao adaptativa |
| `Binary = AdaptiveThresholdGaussian(Enhanced, THRESH_BINARY_INV, blockSize, C=adapt_C)` | `preprocess.py` | Limiarizacao final |
| `OPEN(3x3) -> CLOSE(3x3)` | `preprocess.py` | Limpeza morfologica |

## 4. DETECCAO DE CONTORNO - contorno.py

| Formula | Localizacao | Uso |
|---|---|---|
| `processed = MORPH_CLOSE(img, kernel=3x3, iter=1)` | `contorno.py` | Fechamento inicial |
| `top/side/bottom margins = funcao de min(h,w)` | `contorno.py` | Mascara adaptativa de borda |
| `contours = findContours(processed, RETR_EXTERNAL, CHAIN_APPROX_NONE)` | `contorno.py` | Extracao de contornos |
| `fallback: edges = Canny(img, 30, 100)` | `contorno.py` | Recuperacao quando contorno falha |
| `Area >= 100` | `contorno.py` | Filtro de tamanho minimo |
| `bw >= 20 e bh >= 20` | `contorno.py` | Filtro de bounding box |
| `circularidade = 4*pi*Area/P^2 > 0.5` | `contorno.py` | Filtro morfologico |
| `convexidade = Area / Area_hull > 0.7` | `contorno.py` | Rejeicao de ruido concavo |
| `fill_ratio = Area/(bw*bh) >= 0.5` | `contorno.py` | Rejeicao de contorno oco |

## 5. SEPARACAO GOTA-SUBSTRATO - contorno.py

| Formula | Localizacao | Uso |
|---|---|---|
| `largura(y) = sum(img_bin[y,:] > 0)` | `contorno.py` | Perfil de necking |
| `profundidade = (larg_max - larg_min)/larg_max` | `contorno.py` | Confianca do necking |
| `sobel_y = abs(Sobel(gray, dy=1))` | `contorno.py` | Gradiente de superficie |
| `confianca_sobel = clip((pico/media - 1)/3, 0, 1)` | `contorno.py` | Forca da borda horizontal |
| `bin_morf = OPEN(img_bin, kernel retangular anisotropico)` | `contorno.py` | Quebra de ponte gota-substrato |
| `consenso se abs(yA - yB) <= 8` | `contorno.py` | Fusao de tecnicas |

## 6. LINHA BASE E CONTATO - linha_base.py

| Formula | Localizacao | Uso |
|---|---|---|
| `dist = hypot(dx, dy)` | `linha_base.py` | Norma para normalizacao |
| `v_norm = (dx/dist, dy/dist)` se `dist>=eps`, senao `(1,0)` | `linha_base.py` | Normalizacao segura |
| `q = clip(1 - clip(BASELINE_BOTTOM_FRACTION, 0.02, 0.5), 0, 1)` | `linha_base.py` | Quantil da faixa inferior |
| `floor_pts: Y_i >= quantile(Y, q)` | `linha_base.py` | Candidatos ao piso |
| `(vx, vy, x0, y0) = fitLine(floor_pts)` | `linha_base.py` | Ajuste TLS L1 |
| `d_i = abs(vy*(x_i-x0) - vx*(y_i-y0)) / hypot(vx, vy)` | `linha_base.py` | Distancia ponto-reta |
| `MAD = median(abs(d - median(d)))` | `linha_base.py` | Escala robusta |
| `limiar = max(BASELINE_INLIER_MIN_PIXELS, BASELINE_INLIER_MAD_SCALE * 1.4826 * MAD)` | `linha_base.py` | Regra de inliers |
| `Y_baseline = quantile(Y_inliers, 0.90)` | `linha_base.py` | Baseline robusta final |
| `fallback: Y_baseline = max(Y_contorno)` | `linha_base.py` | Compatibilidade |
| `y_roi_top = y_min + roi_top*altura` | `linha_base.py` | Limite superior da ROI |
| `y_roi_bottom = y_max - roi_bottom*altura` | `linha_base.py` | Limite inferior da ROI |
| `margem_base = max(6.0, 0.06*altura)` | `linha_base.py` | Corte anti-contaminacao na base |
| `y_roi_bottom = min(y_roi_bottom, baseline_y - margem_base)` | `linha_base.py` | Ajuste final da ROI |
| `X(Y) = a*Y^2 + b*Y + c` | `linha_base.py` | Extrapolacao por lado |
| `X_contato = X(Y_baseline)` | `linha_base.py` | Ponto de contato estimado |
| `dist = abs(X_lado - x_center)` | `linha_base.py` | Espelhamento quando um lado falha |
| `tolerancia = max(5.0, 0.15*altura)` | `linha_base.py` | Fallback geometrico |

## 7. AJUSTE CIRCULAR E ANGULO - angulo_contato.py

| Formula | Localizacao | Uso |
|---|---|---|
| `u = x - mean(x)` e `v = y - mean(y)` | `angulo_contato.py` | Centralizacao numerica |
| `Suu, Svv, Suv, Suuu, Svvv, Suvv, Suuv` | `angulo_contato.py` | Termos de Kasa |
| `A = [[Suu, Suv], [Suv, Svv]]` | `angulo_contato.py` | Matriz do sistema |
| `B = [(Suuu + Suvv), (Svvv + Suuv)] / 2` | `angulo_contato.py` | Vetor independente |
| `[uc, vc] = solve(A, B)` | `angulo_contato.py` | Centro no espaco centralizado |
| `xc = mean(x) + uc`, `yc = mean(y) + vc` | `angulo_contato.py` | Centro global |
| `R = mean(sqrt((x - xc)^2 + (y - yc)^2))` | `angulo_contato.py` | Raio medio |
| `offset = clip(fator*altura, min, max)` | `angulo_contato.py` | Baseline adaptativa |
| `baseline_ajustada = baseline_y + offset` | `angulo_contato.py` | Linha de referencia angular |
| `window_height = clip(fator*altura, min, max)` | `angulo_contato.py` | Janela de ajuste por lado |
| `mask = (Y < baseline_ajustada - 3) AND (Y > baseline_ajustada - window_height)` | `angulo_contato.py` | Recorte local |
| `residual_i = abs(hypot(x_i-xc0, y_i-yc0) - R0)` | `angulo_contato.py` | Erro radial |
| `inlier se residual_i <= ANGLE_OUTLIER_SIGMA_SCALE * sigma` | `angulo_contato.py` | Filtro sigma |
| `dy = baseline_ajustada - yc` | `angulo_contato.py` | Distancia vertical ao centro |
| `dx = sqrt(max(0, R^2 - dy^2))` | `angulo_contato.py` | Intersecao circulo-reta |
| `x_contato = xc - dx` (esq) ou `xc + dx` (dir) | `angulo_contato.py` | Contato sub-pixel |
| `m_tangente = -(x_contato - xc)/(baseline_ajustada - yc)` | `angulo_contato.py` | Inclinacao da tangente |
| `theta = degrees(atan(abs(m_tangente)))` | `angulo_contato.py` | Angulo base |
| `theta = 180 - theta` se `yc > baseline_ajustada` | `angulo_contato.py` | Ajuste de quadrante |
| `theta_final = clip(theta, 0, 180)` | `angulo_contato.py` | Restricao fisica |
| `dx_dy = 2*a*baseline_y + b` | `angulo_contato.py` | Derivada no fallback polinomial |
| `theta_fb = atan(1/dx_dy)` (ou `pi/2` se `dx_dy=0`) | `angulo_contato.py` | Fallback angular |

## 8. PARAMETROS ATUAIS RELEVANTES - config.json

| Parametro | Valor atual |
|---|---|
| `baseline_bottom_fraction` | `0.10` |
| `baseline_inlier_min_pixels` | `2.0` |
| `baseline_inlier_mad_scale` | `2.5` |
| `baseline_refine_iterations` | `2` |
| `roi_top_exclude` | `0.20` |
| `roi_bottom_exclude` | `0.08` |
| `polyfit_degree` | `2` |
| `angle_baseline_offset_factor` | `0.01` |
| `angle_baseline_offset_min` | `1.5` |
| `angle_baseline_offset_max` | `4.0` |
| `angle_window_height_factor` | `0.55` |
| `angle_window_height_min` | `70` |
| `angle_window_height_max` | `220` |
| `angle_outlier_sigma_scale` | `2.0` |

## 9. CONVERSOES E VISUALIZACAO - main.py e desenho.py

| Formula | Localizacao | Uso |
|---|---|---|
| `ratio = min(canvas_w/img_w, canvas_h/img_h)` | `main.py` | Ajuste da imagem ao canvas |
| `ratio_zoom = ratio * zoom_scale` | `main.py` | Escala com zoom |
| `offset_x = (canvas_w - new_w)/2` e `offset_y = (canvas_h - new_h)/2` | `main.py` | Centralizacao |
| `x_img = (x_canvas - offset_x)/ratio` | `main.py` | Tela -> imagem |
| `y_img = (y_canvas - offset_y)/ratio` | `main.py` | Tela -> imagem |
| `x_img = clip(x_img, 0, w-1)` e `y_img = clip(y_img, 0, h-1)` | `main.py` | Limites da imagem |
| `to_scr(x,y) = (x*ratio + ox, y*ratio + oy)` | `main.py` | Imagem -> tela |
| `baseline_y = (y_esq + y_dir)/2` (arraste manual) | `main.py` | Recalculo de baseline |
| `length = 50 / zoom_scale` | `desenho.py` | Comprimento visual da tangente |
| `P1 = (x - 0.2*dx, y - 0.2*dy)`, `P2 = (x + dx, y + dy)` | `desenho.py` | Segmento da tangente |

---

Fim do documento.
