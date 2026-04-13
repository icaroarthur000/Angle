# Documentacao Matematica do Sistema Angle

Data: 30 de marco de 2026
Projeto: Angle - Contact Angle Measurement System
Objetivo: documentar TODAS as formulas matematicas realmente usadas no codigo atual, em ordem de execucao.

---

## 1. Fluxo Matematico Completo (ordem de execucao)

1. Selecao da ROI (usuario) e conversao de coordenadas tela-imagem em `main.py`
2. Pre-processamento da ROI (caminho principal em `processamento_imagem/filtros.py`, com fallback robusto em `processamento_imagem/preprocess.py`)
3. Extracao do contorno em `processamento_imagem/contorno.py`
4. Deteccao da baseline e pontos de contato em `linha_base/linha_base.py`
5. Calculo angular principal circular + fallback polinomial em `Cal_angulo/angulo_contato.py`
6. Conversoes de visualizacao e desenho das tangentes em `visualizacao/desenho.py`

---

## 2. Coordenadas e ROI (main.py)

### 2.1 Conversao tela -> imagem
Usada em `SelectionWindow.canvas_to_img`:

x_img = (x_tela - offset_x) / ratio

y_img = (y_tela - offset_y) / ratio

com saturacao:

x_img = clip(x_img, 0, w - 1)

y_img = clip(y_img, 0, h - 1)

### 2.2 Conversao imagem -> tela
Usada em renderizacao:

x_tela = x_img * ratio + ox

y_tela = y_img * ratio + oy

### 2.3 Escala de exibicao

SelectionWindow (janela de selecao):

ratio = min(cw / iw, ch / ih)

ContactAngleApp (janela de analise):

ratio = min(cw / iw, ch / ih) * zoom_scale

onde:
- cw, ch: largura e altura do canvas
- iw, ih: largura e altura da imagem

---

## 3. Pre-processamento (formulas realmente implementadas)

## 3.1 Caminho principal: filtros.py

Arquivo: `processamento_imagem/filtros.py`

1. Conversao para cinza:

Gray = cvtColor(BGR, BGR2GRAY)

2. Suavizacao Gaussiana:

Blur = GaussianBlur(Gray, k=(5,5), sigma=0)

3. Binarizacao Otsu invertida:

Bin = THRESH_BINARY_INV + OTSU(Blur)

4. Fechamento morfologico:

Bin = CLOSE(Bin, kernel_eliptico 5x5, iter=1)

## 3.2 Caminho robusto (fallback): preprocess.py

Arquivo: `processamento_imagem/preprocess.py`

Observacao de acionamento:
- Esta rota nao e chamada por falha de contorno.
- Ela e acionada quando a etapa principal de pre-processamento (`filtros.py`) gera excecao no `try/except` de `main.py`.

### 3.2.1 Estimativa de fundo

Regra de suavizacao inicial (gray + denoise):

se nm_gauss > 0:

k = nm_gauss (se impar) senao (nm_gauss + 1)

Gray = GaussianBlur(Gray, (k, k), 0)

k_bg = max(51, (min(h,w)//6) | 1)

se bg_ksize for informado:

k_bg = bg_ksize (se impar) senao (bg_ksize + 1)

Background = GaussianBlur(Gray, (k_bg, k_bg), 0)

### 3.2.2 Correcao por divisao

Corrected = ((Gray + 1) / (Background + 1)) * 128

Corrected = clip(Corrected, 0, 255)

### 3.2.3 CLAHE

Se grade nao for informada:

tile = max(1, int(min(h,w)/50))

tileGrid = (min(8, tile), min(8, tile))

Enhanced = CLAHE(Corrected, clipLimit=2.0, tileGridSize=tileGrid)

### 3.2.4 Limiarizacao adaptativa

blockSize = max(31, (min(h,w)//30) | 1)

blockSize impar e estritamente menor que min(h,w)

max_allowed = max(3, min(h,w) - (1 se min(h,w) for par senao 0))

se blockSize >= min(h,w):

blockSize = max_allowed (se impar) senao (max_allowed - 1)

Binary = AdaptiveThresholdGaussian(Enhanced, THRESH_BINARY_INV, blockSize, C=2)

### 3.2.5 Limpeza morfologica

Binary = OPEN(Binary, kernel_eliptico 3x3, iter=1)

Binary = CLOSE(Binary, kernel_eliptico 3x3, iter=1)

---

## 4. Deteccao de Contorno (contorno.py)

Arquivo: `processamento_imagem/contorno.py`

1. Fechamento inicial:

Processed = CLOSE(img, kernel 3x3, iter=1)

2. Mascara de borda preta:

rectangle(thickness=10) nas bordas da imagem

3. Extracao de contorno externo:

findContours(Processed, RETR_EXTERNAL, CHAIN_APPROX_NONE)

4. Fallback por Canny se vazio:

Edges = Canny(img, 30, 100)

5. Filtro topologico por toque em bordas (margem=5):

touches_left = any(x <= 5)

touches_right = any(x >= w - 5)

touches_top = any(y <= 5)

touches_bottom = any(y >= h - 5)

border_count = touches_left + touches_right + touches_top + touches_bottom

aceita se border_count < 3

6. Filtro de area:

area(contorno) >= 100

7. Filtro final de pontos (margem=10):

10 < x < w-10 e 10 < y < h-10

---

## 5. Baseline e Contato (linha_base.py)

Arquivo: `linha_base/linha_base.py`

## 5.1 Normalizacao segura de vetor

safe_normalize(dx, dy):

dist = hypot(dx, dy)

se dist < 1e-8: retorna (1, 0)

senao: (dx/dist, dy/dist)

## 5.2 Baseline robusta por TLS + filtro MAD (codigo atual)

1. Selecao da faixa inferior por quantil:

q = clip(1 - clip(bottom_fraction, 0.02, 0.5), 0, 1)

y_cut = quantile(Y_contorno, q)

floor_pts = {pontos | Y >= y_cut}

2. Ajuste robusto de reta com fitLine + poda iterativa por MAD:

(vx, vy, x0, y0) = fitLine(floor_pts)

d_i = abs(vy*(x_i-x0) - vx*(y_i-y0)) / hypot(vx, vy)

MAD = median(abs(d - median(d)))

limiar = max(BASELINE_INLIER_MIN_PIXELS, BASELINE_INLIER_MAD_SCALE * 1.4826 * MAD)

3. Baseline final robusta:

Y_base = quantile(Y_inliers, 0.90)

4. Fallback conservador:

Y_base = max(Y_contorno)

## 5.3 Extrapolacao polinomial de contato

Constantes atuais:
- ROI_TOP_EXCLUDE = 0.20
- ROI_BOTTOM_EXCLUDE = 0.08 (default)
- POLYFIT_DEGREE = 2

1. Altura da gota:

height = Y_max - Y_min

2. ROI vertical:

y_roi_top = Y_min + 0.20 * height

y_roi_bottom = Y_max - ROI_BOTTOM_EXCLUDE * height

margem_base = max(6.0, 0.06 * height)

y_roi_bottom = min(y_roi_bottom, Y_base - margem_base)

se y_roi_bottom <= y_roi_top: y_roi_bottom = Y_base - 2.0

3. Separacao por lados:

x_center = media(X_contorno)

esquerda: X < x_center

direita: X >= x_center

4. Ajuste por lado (X em funcao de Y):

X(Y) = aY^2 + bY + c

5. Extrapolacao para baseline:

X_contato = X(Y_base)

6. Espelhamento se um lado falhar:

dist = |X_lado_valido - x_center|

X_lado_faltante = x_center +- dist

7. Fallback geometrico final:

tolerancia = max(5.0, 0.15 * height)

near_baseline = {pontos | Y >= (Y_max - tolerancia)}

X_esq = min(X_near)

X_dir = max(X_near)

---

## 6. Calculo do Angulo (angulo_contato.py)

Arquivo: `Cal_angulo/angulo_contato.py`

Funcao principal: `calcular_angulo_circular(...)`

Observacao de estrategia:
- Nao existe chaveamento previo por aspect ratio neste modulo.
- O motor sempre tenta primeiro o ajuste circular.
- O fallback polinomial e acionado por falha geometrica/numerica (ex.: raio invalido, baseline fora do circulo, erro de solucao).

## 6.1 Calibracao de baseline

offset_calibracao = clip(ANGLE_BASELINE_OFFSET_FACTOR * altura_gota,
						 ANGLE_BASELINE_OFFSET_MIN,
						 ANGLE_BASELINE_OFFSET_MAX)

Y_base_ajustada = Y_base + offset_calibracao

## 6.2 Janela de pontos para ajuste

window_height = clip(ANGLE_WINDOW_HEIGHT_FACTOR * altura_gota,
					 ANGLE_WINDOW_HEIGHT_MIN,
					 ANGLE_WINDOW_HEIGHT_MAX)

mask = (Y < Y_base_ajustada - 3) AND (Y > Y_base_ajustada - window_height)

## 6.3 Selecao por lado

x_center_aprox = (p_esq.x + p_dir.x) / 2

lado esquerdo: X < x_center_aprox

lado direito: X > x_center_aprox

## 6.4 Centralizacao dos pontos

mean_xy = media(local_pts)

pontos_centered = local_pts - mean_xy

## 6.5 Ajuste circular algebrico de Kasa

Funcao: `ajustar_circulo_algebrico(pontos)`

Metodo computacional no codigo atual:
- Resolucao direta do sistema linear dos momentos com `np.linalg.solve` (matriz 2x2), nao `np.linalg.lstsq`.

Dados:

x = pontos[:,0], y = pontos[:,1]

xm = media(x), ym = media(y)

u = x - xm, v = y - ym

Somas:

Suu = soma(u^2)

Svv = soma(v^2)

Suv = soma(u*v)

Suuu = soma(u^3)

Svvv = soma(v^3)

Suvv = soma(u*v^2)

Suuv = soma(u^2*v)

Sistema linear:

A = [[Suu, Suv], [Suv, Svv]]

B = [(Suuu + Suvv)/2, (Svvv + Suuv)/2]

[uc, vc] = solve(A, B)

Se A for singular (LinAlgError), o metodo retorna (0,0,0), o que dispara fallback angular.

Centro global:

xc = xm + uc

yc = ym + vc

Raio:

R = media( sqrt((x - xc)^2 + (y - yc)^2) )

Reconversao no fluxo da funcao principal (apos o ajuste final com pontos centrados):

xc_global = xc + mean_xy[0]

yc_global = yc + mean_xy[1]

Obs.: esta etapa aparece em `calcular_angulo_circular` depois do segundo ajuste circular,
para voltar de coordenadas centradas para coordenadas globais da imagem.

## 6.6 Filtro de outliers por sigma

Nota importante:
- xc0, yc0 e as distancias abaixo sao calculados no espaco centrado
	(`local_pts_centered`), nao nas coordenadas originais da imagem.

d_i = hypot(local_pts_centered[i,0] - xc0, local_pts_centered[i,1] - yc0)

residuals_i = |d_i - R0|

sigma = std(residuals)

inlier se residuals_i <= ANGLE_OUTLIER_SIGMA_SCALE * sigma

Resultado:
- local_pts_filtered = subconjunto de `local_pts_centered` (ainda em espaco centrado).

## 6.7 Intersecao circulo-reta baseline (sub-pixel)

Com baseline horizontal em Y_base_ajustada:

dy = Y_base_ajustada - yc

condicao de existencia: |dy| < R

se |dy| >= R: baseline fora do circulo -> fallback polinomial

dx = sqrt(max(0, R^2 - dy^2))

x_contato = xc - dx (esq) ou xc + dx (dir)

## 6.8 Inclinacao da tangente por derivada implicita

Da equacao do circulo, inclinacao local da tangente no contato:

m_tangente = -(x_contato - xc) / (Y_base_ajustada - yc)

Se denominador = 0: theta = 90 graus

Senao:

theta = atan(|m_tangente|)

theta_graus = degrees(theta)

## 6.9 Ajuste de quadrante hidrofobico

se yc > Y_base_ajustada:

theta_graus = 180 - theta_graus

Resultado final:

theta = clip(theta_graus, 0, 180)

## 6.10 Fallback polinomial angular

Funcao: `_calcular_angulo_polynomial_fallback`

Importante:
- `local_pts` no fallback esta em coordenadas originais da imagem
	(nao centradas).
- O fallback recebe `local_pts`, e nao `local_pts_centered`.

1. Ajuste:

X(Y) = aY^2 + bY + c

2. Derivada:

dX/dY = 2a*Y_base_ajustada + b

Observacao de consistencia:
- No codigo atual, o fallback recebe baseline ajustada (baseline_ajustada),
  portanto a derivada e avaliada em Y_base_ajustada.

3. Conversao para angulo:

theta = atan(1 / (dX/dY))  (ou 90 graus se derivada zero)

4. Ajuste por lado:
- lado esq: se theta<0, soma 180
- lado dir: se theta>0, theta=180-theta; senao usa |theta|

5. Saturacao final: [0, 180]

---

## 7. Visualizacao Matematica (desenho.py)

Arquivo: `visualizacao/desenho.py`

## 7.1 Baseline na tela

y_scr = baseline_y * ratio + offset_y

x_start = offset_x

x_end = offset_x + image_width * ratio

Quando line_params=(vx, vy, x0, y0) estiver disponivel, a baseline inclinada e projetada por:

t_left = (0 - x0) / vx

t_right = (image_width - x0) / vx

y_left = y0 + t_left * vy

y_right = y0 + t_right * vy

## 7.2 Tangentes desenhadas

length = 50 / zoom_scale

Para esquerda:

angle = radians(ae)

dx = length * cos(angle)

dy = -length * sin(angle)

Para direita:

angle = radians(ad)

dx = -length * cos(angle)

dy = -length * sin(angle)

Projecao visual com origem deslocada 20% para baixo:

P1 = (x - 0.2*dx, y - 0.2*dy)

P2 = (x + dx, y + dy)

---

## 8. Resumo Unico de Formulas em Uso

1. SelectionWindow: ratio = min(cw/iw, ch/ih); ContactAngleApp: ratio = min(cw/iw, ch/ih) * zoom_scale
2. x_img = (x_tela - offset_x)/ratio, y_img = (y_tela - offset_y)/ratio
3. Otsu invertido: THRESH_BINARY_INV + OTSU
4. Corrected = ((Gray+1)/(Background+1))*128
5. k_bg = max(51, (min(h,w)//6)|1)
6. tile = max(1, int(min(h,w)/50)); tileGrid = (min(8,tile), min(8,tile))
7. blockSize = max(31, (min(h,w)//30)|1)
8. q = clip(1 - clip(bottom_fraction, 0.02, 0.5), 0, 1); y_cut = quantile(Y, q)
9. floor_pts: Y >= y_cut
10. y_roi_top = Y_min + 0.20*height
11. y_roi_bottom = Y_max - ROI_BOTTOM_EXCLUDE*height (com corte por margem_base)
12. X(Y) = aY^2 + bY + c
13. safe_normalize: (dx,dy)/hypot(dx,dy)
14. Y_base_ajustada = Y_base + clip(fator*altura, min, max)
15. Kasa: solve(A,B) com A=[[Suu,Suv],[Suv,Svv]]
16. R = media(sqrt((x-xc)^2+(y-yc)^2))
17. inlier: residual <= 2*sigma
18. dx = sqrt(max(0, R^2 - dy^2)), dy = Y_base_ajustada - yc
19. m_tangente = -(x_contato-xc)/(Y_base_ajustada-yc)
20. theta = degrees(atan(|m_tangente|))
21. se yc > Y_base_ajustada: theta = 180 - theta
22. fallback: dX/dY = 2a*Y_base_ajustada + b; theta = atan(1/(dX/dY))
23. tangente visual: dx = +/-length*cos(theta), dy = -length*sin(theta)
24. criterio fallback circular: (R <= 0) ou (|Y_base_ajustada - yc| >= R) ou erro de solve/ajuste

---
