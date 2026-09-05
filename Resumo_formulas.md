# Documentacao Matematica do Sistema Angle (Versao Final para Professor)

Data: 31 de marco de 2026  
Projeto: Angle - Contact Angle Measurement System  
Objetivo: apresentar, em formato unico e academico, todas as formulas matematicas efetivamente usadas no software atual.

---

## 1. Convencoes e Notacao

- Coordenadas de imagem: $(x, y)$
- Coordenadas de tela: $(x_{tela}, y_{tela})$
- Dimensoes do canvas: $(cw, ch)$
- Dimensoes da imagem: $(iw, ih)$
- Baseline bruta: $Y_{base}$
- Baseline ajustada: $Y_{base}^{adj}$
- Centro do circulo: $(x_c, y_c)$
- Raio do circulo: $R$

---

## 2. Coordenadas e Escala (main.py)

### 2.1 Conversao tela -> imagem (SelectionWindow)

$$
x_{img} = \frac{x_{tela} - offset_x}{ratio},
\quad
y_{img} = \frac{y_{tela} - offset_y}{ratio}
$$

Com saturacao:

$$
x_{img} = clip(x_{img}, 0, w-1),
\quad
y_{img} = clip(y_{img}, 0, h-1)
$$

### 2.2 Conversao imagem -> tela

$$
x_{tela} = x_{img}\cdot ratio + ox,
\quad
y_{tela} = y_{img}\cdot ratio + oy
$$

### 2.3 Escala de exibicao por janela

SelectionWindow (janela de selecao):

$$
ratio = \min\left(\frac{cw}{iw}, \frac{ch}{ih}\right)
$$

ContactAngleApp (janela de analise):

$$
ratio = \min\left(\frac{cw}{iw}, \frac{ch}{ih}\right)\cdot zoom\_scale
$$

---

## 3. Pre-processamento de Imagem

### 3.1 Caminho principal — OTSU (filtros.py: `aplicar_filtro_binary_otsu`)

1) Conversao para cinza:

$$
Gray = cvtColor(BGR, BGR2GRAY)
$$

2) Suavizacao gaussiana:

$$
Blur = GaussianBlur(Gray, (5,5), 0)
$$

3) Binarizacao Otsu invertida:

$$
Bin = THRESH\_BINARY\_INV + OTSU(Blur)
$$

4) Fechamento morfologico:

$$
Bin = CLOSE(Bin, kernel\_eliptico\ 5\times5,\ iter=1)
$$

### 3.1b Pre-processamento robusto (filtros.py: `preprocessar_imagem_robusto`)

Aplicado antes dos metodos de binarizacao quando iluminacao e irregular:

1) CLAHE com grade fixa:

$$
Gray_{clahe} = CLAHE(Gray,\ clipLimit=2.0,\ tileGridSize=8\times8)
$$

2) Suavizacao leve:

$$
saida = GaussianBlur(Gray_{clahe},\ (3,3),\ 0)
$$

### 3.1c Binarizacao Adaptativa (filtros.py: `aplicar_filtro_binary_adaptive`)

$$
blockSize = \max\left(31,\ \left\lfloor\frac{\min(h,w)}{30}\right\rfloor\ \texttt{|}\ 1\right)
$$

$$
Binary = AdaptiveThresholdGaussian(Blur,\ THRESH\_BINARY\_INV,\ blockSize,\ C=2)
$$

$$
Binary = OPEN(Binary,\ kernel\_eliptico\ 3\times3,\ 1) \to CLOSE(Binary,\ 3\times3,\ 1)
$$

### 3.1d Score de mascara e selecao automatica (filtros.py: `_score_mascara`, `aplicar_multi_threshold`)

Rejeita mascaras com fill fora da faixa util:

$$
fill = \frac{pixels_{brancos}}{total},\quad \text{rejeita se } fill < 0.03 \text{ ou } fill > 0.92
$$

Penaliza mascaras muito ruidosas (alta entropia):

$$
entropy = -\sum_{i} p_i \log_2(p_i)
$$

$$
score = 0.7 \cdot fill - 0.3 \cdot \frac{entropy}{8}
$$

Selecao do melhor metodo entre OTSU, ADAPTIVE e CANNY:

$$
mascara = \arg\max_{m \in \{OTSU,\ ADAPTIVE,\ CANNY\}} score(m)
$$

### 3.2 Caminho robusto (preprocess.py)

#### 3.2.1 Denoise inicial (condicional)

Se $nm\_gauss > 0$:

$$
k = \begin{cases}
nm\_gauss, & \text{se } nm\_gauss \text{ for impar} \\
nm\_gauss + 1, & \text{caso contrario}
\end{cases}
$$

$$
Gray = GaussianBlur(Gray, (k,k), 0)
$$

#### 3.2.2 Estimativa de fundo

Sem parametro externo:

$$
k_{bg} = \max\left(51,\left\lfloor\frac{\min(h,w)}{6}\right\rfloor\ \texttt{|}\ 1\right)
$$

Com $bg\_ksize$ informado:

$$
k_{bg} = \begin{cases}
bg\_ksize, & \text{se impar} \\
bg\_ksize + 1, & \text{caso contrario}
\end{cases}
$$

$$
Background = GaussianBlur(Gray, (k_{bg}, k_{bg}), 0)
$$

#### 3.2.3 Correcao de iluminacao por divisao

$$
Corrected = \left(\frac{Gray + 1}{Background + 1}\right)\cdot 128
$$

$$
Corrected = clip(Corrected, 0, 255)
$$

#### 3.2.4 CLAHE

Se grade nao informada:

$$
tile = \max\left(1,\left\lfloor\frac{\min(h,w)}{50}\right\rfloor\right)
$$

$$
tileGrid = (\min(8, tile),\ \min(8, tile))
$$

$$
Enhanced = CLAHE(Corrected,\ clipLimit=2.0,\ tileGridSize=tileGrid)
$$

#### 3.2.5 Limiarizacao adaptativa

$$
blockSize = \max\left(31,\left\lfloor\frac{\min(h,w)}{30}\right\rfloor\ \texttt{|}\ 1\right)
$$

Com ajuste de limite:

$$
max\_allowed = \max\left(3,\ \min(h,w) - \big(1\ \text{se }\min(h,w)\text{ par, senao }0\big)\right)
$$

Se $blockSize \ge \min(h,w)$:

$$
blockSize = \begin{cases}
max\_allowed, & \text{se impar} \\
max\_allowed - 1, & \text{caso contrario}
\end{cases}
$$

$$
Binary = AdaptiveThresholdGaussian(Enhanced,\ THRESH\_BINARY\_INV,\ blockSize,\ C=2)
$$

#### 3.2.6 Limpeza morfologica

$$
Binary = OPEN(Binary,\ kernel\_eliptico\ 3\times3,\ iter=1)
$$

$$
Binary = CLOSE(Binary,\ kernel\_eliptico\ 3\times3,\ iter=1)
$$

---

## 4. Deteccao de Contorno (contorno.py)

### 4.1 Pipeline robusto (`encontrar_contorno_gota_robusto`)

1) Fechamento inicial:

$$
Processed = CLOSE(img,\ kernel\ 3\times3,\ iter=1)
$$

2) Margens adaptativas zeradas (top, side, bottom proporcional a $\min(h,w)$).

3) Contorno externo:

$$
contours = findContours(Processed,\ RETR\_EXTERNAL,\ CHAIN\_APPROX\_NONE)
$$

4) Fallback por Canny se nenhum contorno encontrado:

$$
Edges = Canny(img, 30, 100)
$$

5) Validacao por $\_validar\_contorno$ — criterios aplicados a cada candidato:

$$
Area \ge 100
$$

$$
bw \ge 20\ \land\ bh \ge 20
$$

$$
\frac{\max(bw, bh)}{\min(bw, bh)} < 8
$$

$$
circularidade = \frac{4\pi \cdot Area}{P^2} > MIN\_CIRCULARITY
$$

No codigo atual esse limiar e parametrico:

$$
circularidade > MIN\_CIRCULARITY,
\quad MIN\_CIRCULARITY = obter("min\_circularity", 0.35)
$$

$$
convexidade = \frac{Area}{Area_{hull}} > 0.7
$$

6) Selecao do maior contorno valido, remocao de pontos nas bordas.

### 4.2 Filtros do pipeline original (`encontrar_contorno_gota`)

Filtro topologico de bordas (margem 5):

$$
border\_count = I_{left} + I_{right} + I_{top} + I_{bottom},\quad aceita\ se\ border\_count < 3
$$

Filtro de area:

$$
Area(contorno) \ge 100
$$

Filtro final de pontos (margem 10):

$$
10 < x < w-10\ \land\ 10 < y < h-10
$$

---

## 5. Baseline e Pontos de Contato (linha_base.py)

### 5.1 Normalizacao segura

$$
dist = hypot(dx, dy)
$$

$$
(dx',dy') = \begin{cases}
(1,0), & \text{se } dist < 10^{-8} \\
\left(\frac{dx}{dist},\frac{dy}{dist}\right), & \text{caso contrario}
\end{cases}
$$

### 5.2 Baseline robusta por TLS + filtro MAD

No pipeline atual, a baseline e estimada com ajuste de reta robusto nos pontos inferiores do contorno.

Selecao da faixa inferior por quantil:

$$
q = clip\left(1 - clip(BASELINE\_BOTTOM\_FRACTION,\ 0.02,\ 0.5),\ 0,\ 1\right)
$$

$$
y_{cut} = quantile(Y_{contorno}, q),
\quad floor\_pts = \{pontos\ :\ Y \ge y_{cut}\}
$$

Ajuste de reta por TLS (OpenCV fitLine, norma L1):

$$
(v_x, v_y, x_0, y_0) = fitLine(floor\_pts)
$$

Distancia perpendicular ponto-reta:

$$
d_i = \frac{|v_y(x_i-x_0) - v_x(y_i-y_0)|}{\sqrt{v_x^2+v_y^2}}
$$

Poda robusta por MAD (iterativa):

$$
med = median(d),
\quad MAD = median\left(|d - med|\right)
$$

$$
\sigma_{rob} = 1.4826\cdot MAD,
\quad limiar = \max(BASELINE\_INLIER\_MIN\_PIXELS,\ BASELINE\_INLIER\_MAD\_SCALE\cdot\sigma_{rob})
$$

$$
inlier_i \iff d_i \le limiar
$$

Baseline final (piso fisico robusto):

$$
Y_{base} = quantile(Y_{inliers}, 0.90)
$$

Fallback conservador (compatibilidade):

$$
Y_{base} = \max(Y_{contorno})
$$

### 5.3 Extrapolacao polinomial (grau 2)

Constantes atuais:

$$
ROI\_TOP\_EXCLUDE = 0.20,
\quad ROI\_BOTTOM\_EXCLUDE = 0.08\ (default),
\quad POLYFIT\_DEGREE = 2
$$

Altura:

$$
height = Y_{max} - Y_{min}
$$

ROI vertical:

$$
y_{roi\_top} = Y_{min} + 0.20\cdot height,
\quad y_{roi\_bottom} = Y_{max} - ROI\_BOTTOM\_EXCLUDE\cdot height
$$

Com corte adicional perto da baseline para reduzir contaminacao da saia de contato:

$$
margem\_base = \max(6.0,\ 0.06\cdot height)
$$

$$
y_{roi\_bottom} = \min(y_{roi\_bottom},\ Y_{base} - margem\_base)
$$

Guarda para evitar ROI vazia:

$$
	ext{se } y_{roi\_bottom} \le y_{roi\_top},\ \ y_{roi\_bottom} = Y_{base} - 2.0
$$

Separacao lateral:

$$
x_{center} = media(X_{contorno})
$$

Ajuste por lado:

$$
X(Y) = aY^2 + bY + c
$$

Contato extrapolado:

$$
X_{contato} = X(Y_{base})
$$

Espelhamento de lado faltante:

$$
dist = |X_{lado\_valido} - x_{center}|,
\quad X_{faltante} = x_{center} \pm dist
$$

Fallback geometrico (tolerancia adaptativa):

$$
tolerancia = \max(5.0,\ 0.15 \cdot height)
$$

$$
near\_baseline = \{pontos\ :\ Y \ge Y_{max} - tolerancia\}
$$

$$
X_{esq} = \min\left(X_{near\ :\ X \le x_{center}}\right),
\quad X_{dir} = \max\left(X_{near\ :\ X > x_{center}}\right)
$$

---

## 6. Calculo do Angulo de Contato (angulo_contato.py)

Estrategia do modulo:

- Nao ha chaveamento previo por aspect ratio.
- O calculo principal tenta ajuste circular.
- O fallback polinomial e acionado por falha numerica/geometrica.

### 6.1 Calibracao adaptativa da baseline

No codigo atual, o deslocamento da baseline e proporcional a altura da gota com limites minimo e maximo:

$$
altura = Y_{max} - Y_{min}
$$

$$
offset = clip\left(
ANGLE\_BASELINE\_OFFSET\_FACTOR\cdot altura,
ANGLE\_BASELINE\_OFFSET\_MIN,
ANGLE\_BASELINE\_OFFSET\_MAX
\right)
$$

$$
Y_{base}^{adj} = Y_{base} + offset
$$

### 6.2 Janela de pontos para ajuste (dinamica)

A altura da janela de ajuste e adaptativa:

$$
window\_height = clip\left(
ANGLE\_WINDOW\_HEIGHT\_FACTOR\cdot altura,
ANGLE\_WINDOW\_HEIGHT\_MIN,
ANGLE\_WINDOW\_HEIGHT\_MAX
\right)
$$

Mascara vertical usada no ajuste:

$$
mask = (Y < Y_{base}^{adj} - 3)\ \land\ (Y > Y_{base}^{adj} - window\_height)
$$

### 6.3 Selecao por lado

$$
x_{center\_aprox} = \frac{x_{esq} + x_{dir}}{2}
$$

Lado esquerdo: $X < x_{center\_aprox}$  
Lado direito: $X > x_{center\_aprox}$

### 6.4 Centralizacao

$$
mean\_{xy} = media(local\_pts),
\quad local\_pts\_{centered} = local\_pts - mean\_{xy}
$$

### 6.5 Ajuste circular algebrico de Kasa

No ajuste `ajustar_circulo_algebrico(pontos)`:

$$
u = x - x_m,
\quad v = y - y_m
$$

$$
S_{uu}=\sum u^2,
\ S_{vv}=\sum v^2,
\ S_{uv}=\sum uv,
\ S_{uuu}=\sum u^3,
\ S_{vvv}=\sum v^3,
\ S_{uvv}=\sum uv^2,
\ S_{uuv}=\sum u^2v
$$

$$
A = \begin{bmatrix}S_{uu} & S_{uv} \\ S_{uv} & S_{vv}\end{bmatrix},
\quad
B = \frac{1}{2}\begin{bmatrix}S_{uuu}+S_{uvv} \\ S_{vvv}+S_{uuv}\end{bmatrix}
$$

$$
\begin{bmatrix}u_c \\ v_c\end{bmatrix} = solve(A,B)
$$

$$
x_c = x_m + u_c,
\quad y_c = y_m + v_c,
\quad R = media\left(\sqrt{(x-x_c)^2 + (y-y_c)^2}\right)
$$

Reconversao no fluxo principal (apos ajuste final com pontos centrados):

$$
x_c^{global} = x_c + mean\_{xy}[0],
\quad y_c^{global} = y_c + mean\_{xy}[1]
$$

### 6.6 Filtro de outliers por sigma

No espaco centrado:

$$
d_i = hypot(local\_pts\_{centered}[i,0]-x_{c0},\ local\_pts\_{centered}[i,1]-y_{c0})
$$

$$
residuals_i = |d_i - R_0|,
\quad sigma = std(residuals)
$$

Inlier:

$$
residuals_i \le ANGLE\_OUTLIER\_SIGMA\_SCALE\cdot sigma
$$

No estado atual, o valor default de $ANGLE\_OUTLIER\_SIGMA\_SCALE$ e $2.0$.

### 6.7 Intersecao circulo-reta (sub-pixel)

$$
dy = Y_{base}^{adj} - y_c
$$

Criterio de existencia:

$$
|dy| < R
$$

Se $|dy| \ge R$: fallback polinomial.

$$
dx = \sqrt{\max(0, R^2 - dy^2)}
$$

$$
x_{contato} = \begin{cases}
x_c - dx, & lado\ esq \\
x_c + dx, & lado\ dir
\end{cases}
$$

### 6.8 Tangente por derivada implicita

$$
m_{tangente} = -\frac{x_{contato} - x_c}{Y_{base}^{adj} - y_c}
$$

Se denominador $=0$: $\theta = 90^\circ$.  
Caso geral:

$$
\theta = \arctan(|m_{tangente}|),
\quad \theta_{graus} = degrees(\theta)
$$

### 6.9 Ajuste de quadrante

$$
\text{se } y_c > Y_{base}^{adj},\ \theta_{graus} = 180 - \theta_{graus}
$$

Resultado final:

$$
\theta = clip(\theta_{graus}, 0, 180)
$$

### 6.10 Fallback polinomial angular

Funcao: `_calcular_angulo_polynomial_fallback(local_pts, baseline_y, lado)`

Observacoes de implementacao:

- `local_pts` no fallback esta em coordenadas originais da imagem (nao centradas).
- A derivada e avaliada em $Y_{base}^{adj}$ (baseline ajustada), pois o fallback recebe `baseline_ajustada`.

Ajuste:

$$
X(Y) = aY^2 + bY + c
$$

Derivada:

$$
\frac{dX}{dY} = 2aY_{base}^{adj} + b
$$

Angulo:

$$
\theta = \arctan\left(\frac{1}{dX/dY}\right)
$$

Com tratamento de quadrante por lado e saturacao final em $[0,180]$.

Criterios de disparo do fallback circular:

$$
(R \le 0)\ \lor\ (|Y_{base}^{adj} - y_c| \ge R)\ \lor\ erro\ numerico\ de\ ajuste/solve
$$

---

## 7. Visualizacao Matematica (desenho.py)

### 7.1 Baseline na tela (horizontal ou inclinada)

Caso horizontal (fallback):

$$
y_{scr} = baseline_y\cdot ratio + offset_y
$$

$$
x_{start} = offset_x,
\quad x_{end} = offset_x + image\_width\cdot ratio
$$

Caso inclinada com `line_params=(v_x,v_y,x_0,y_0)`:

$$
t_{left} = \frac{0 - x_0}{v_x},
\quad t_{right} = \frac{image\_width - x_0}{v_x}
$$

$$
y_{left} = y_0 + t_{left}v_y,
\quad y_{right} = y_0 + t_{right}v_y
$$

$$
(x_1,y_1)=(offset_x,\ y_{left}\cdot ratio + offset_y)
$$

$$
(x_2,y_2)=(offset_x + image\_width\cdot ratio,\ y_{right}\cdot ratio + offset_y)
$$

### 7.2 Tangentes desenhadas

$$
length = \frac{50}{zoom\_scale}
$$

Esquerda:

$$
dx = length\cdot\cos(ae_{rad}),
\quad dy = -length\cdot\sin(ae_{rad})
$$

Direita:

$$
dx = -length\cdot\cos(ad_{rad}),
\quad dy = -length\cdot\sin(ad_{rad})
$$

Segmento com projecao de 20%:

$$
P_1 = (x - 0.2\cdot dx,\ y - 0.2\cdot dy),
\quad P_2 = (x + dx,\ y + dy)
$$

---

## 8. Quadro Unico de Formulas (Resumo Executivo)

1. SelectionWindow: $ratio = \min(cw/iw, ch/ih)$
2. ContactAngleApp: $ratio = \min(cw/iw, ch/ih)\cdot zoom\_scale$
3. $x_{img}=(x_{tela}-offset_x)/ratio,\ y_{img}=(y_{tela}-offset_y)/ratio$
4. Otsu invertido: $THRESH\_BINARY\_INV + OTSU$
5. $Corrected=((Gray+1)/(Background+1))\cdot128$
6. $k_{bg}=\max(51,(\min(h,w)//6)|1)$
7. $tile=\max(1,\lfloor\min(h,w)/50\rfloor),\ tileGrid=(\min(8,tile),\min(8,tile))$
8. $blockSize=\max(31,(\min(h,w)//30)|1)$ com ajuste por $max\_allowed$
9. $q=clip(1-clip(bottom\_fraction,0.02,0.5),0,1),\ y_{cut}=quantile(Y,q)$
10. $floor\_pts:\ Y\ge y_{cut}$
11. $y_{roi\_top}=Y_{min}+0.20\cdot height$
12. $y_{roi\_bottom}=Y_{max}-ROI\_BOTTOM\_EXCLUDE\cdot height$ com corte por margem de baseline
13. $X(Y)=aY^2+bY+c$
14. $safe\_normalize=(dx,dy)/hypot(dx,dy)$
15. $Y_{base}^{adj}=Y_{base}+clip(fator\cdot altura,min,max)$
16. Kasa: $solve(A,B)$ com $A=[[S_{uu},S_{uv}],[S_{uv},S_{vv}]]$
17. $R=media(\sqrt{(x-x_c)^2+(y-y_c)^2})$
18. Inlier: $residuals_i\le2\sigma$
19. $dx=\sqrt{\max(0,R^2-dy^2)},\ dy=Y_{base}^{adj}-y_c$
20. $m_{tangente}=-(x_{contato}-x_c)/(Y_{base}^{adj}-y_c)$
21. $\theta=degrees(atan(|m_{tangente}|))$
22. Se $y_c>Y_{base}^{adj}$: $\theta=180-\theta$
23. Fallback: $dX/dY=2aY_{base}^{adj}+b,\ \theta=atan(1/(dX/dY))$
24. Criterio fallback circular: $(R\le0)\lor(|Y_{base}^{adj}-y_c|\ge R)\lor erro\ numerico$
25. Score de mascara: $score=0.7\cdot fill - 0.3\cdot entropy/8$; rejeita $fill<0.03$ ou $fill>0.92$
26. Selecao de metodo: $mascara=\arg\max_{m\in\{OTSU,ADAPTIVE,CANNY\}} score(m)$
27. Validacao de contorno: $Area\ge100,\ bw\ge20,\ bh\ge20,\ circularidade>MIN\_CIRCULARITY\ (default\ 0.35),\ convexidade>0.7$
28. Fallback geometrico: $tolerancia=\max(5.0,\ 0.15\cdot height)$

---

## 9. FORMULAS CONSOLIDADAS DA IMPLEMENTACAO ATUAL

Esta secao consolida as formulas matematicas usadas pelo programa atual e indica onde cada uma e aplicada.

### 9.1 Coordenadas da tela para a imagem

**Arquivo:** `main.py`  
**Funcao:** `SelectionWindow.canvas_to_img()`  
**Aplicacao:** conversao do clique/ROI do canvas para coordenadas da imagem.

$$
x_{img} = \frac{x_{tela}-offset_x}{ratio},
\qquad
y_{img} = \frac{y_{tela}-offset_y}{ratio}
$$

Depois da conversao, o codigo limita os valores aos limites da imagem:

$$
x_{img}=clip(x_{img},0,w-1),
\qquad
y_{img}=clip(y_{img},0,h-1)
$$

### 9.2 Coordenadas da imagem para a tela

**Arquivo:** `main.py`  
**Funcao:** `ContactAngleApp._render_internal()`  
**Aplicacao:** desenho do contorno, baseline, contatos e tangentes no canvas.

$$
x_{tela}=x_{img}\cdot ratio+o_x,
\qquad
y_{tela}=y_{img}\cdot ratio+o_y
$$

### 9.3 Escala de exibicao

**Arquivo:** `main.py`  
**Funcoes:** `SelectionWindow.render_frame()` e `ContactAngleApp._render_internal()`.

Na janela de selecao:

$$
ratio=\min\left(\frac{cw}{iw},\frac{ch}{ih}\right)
$$

Na janela de analise:

$$
ratio=\min\left(\frac{cw}{iw},\frac{ch}{ih}\right)\cdot zoom\_scale
$$

### 9.4 Binarizacao Otsu

**Arquivo:** `processamento_imagem/filtros.py`  
**Funcao:** `aplicar_filtro_binary_otsu()`  
**Aplicacao:** caminho padrao de Binary utilizado pela analise atual.

Conversao de cor:

$$
Gray=cvtColor(BGR, BGR2GRAY)
$$

Suavizacao:

$$
Blur=GaussianBlur(Gray,(5,5),0)
$$

Limiarizacao invertida:

$$
Binary=Threshold(Blur,THRESH\_BINARY\_INV+OTSU)
$$

Fechamento morfologico:

$$
Binary=CLOSE(Binary,K_{ellipse,5\times5},iterations=1)
$$

O fechamento morfologico pode conectar a gota ao substrato. Por isso, o contorno resultante nao deve ser interpretado automaticamente como a interface liquido-ar.

### 9.5 Canny

**Arquivo:** `processamento_imagem/filtros.py`  
**Funcao:** `aplicar_filtro_edges_canny()`  
**Aplicacao:** modo Edges selecionado pelo usuario ou fallback de deteccao.

$$
Gray=cvtColor(BGR,BGR2GRAY)
$$

$$
Blur=GaussianBlur(Gray,(5,5),0)
$$

$$
Edges=Canny(Blur,30,100)
$$

### 9.6 Limiarizacao adaptativa

**Arquivo:** `processamento_imagem/filtros.py`  
**Funcao:** `aplicar_filtro_binary_adaptive()`.

O tamanho do bloco e calculado a partir da menor dimensao da imagem e ajustado para ser impar:

$$
blockSize=max\left(31,\left\lfloor\frac{\min(h,w)}{30}\right\rfloor\right)
$$

O resultado e:

$$
Binary=AdaptiveThresholdGaussian(Blur,THRESH\_BINARY\_INV,blockSize,C=2)
$$

Depois sao aplicados abertura e fechamento morfologicos com kernels elipticos.

### 9.7 Separacao gota/substrato

**Arquivo:** `processamento_imagem/contorno.py`  
**Funcoes:** `isolar_gota_substrato()`, `_necking_detection()`, `_sobel_y_surface()` e `_abertura_anisotropica()`.

O codigo combina evidencias de estreitamento, gradiente vertical e abertura morfologica. A operacao de abertura usa, quando aplicada:

$$
Mask_{aberta}=OPEN(Mask,K_{retangular,9\times3},iterations=1)
$$

O objetivo e remover ou separar a faixa inferior do substrato antes da extracao do contorno. Nem todos os caminhos de filtro passam por essa separacao da mesma forma.

### 9.8 Contorno externo

**Arquivo:** `processamento_imagem/contorno.py`  
**Funcoes:** `encontrar_contorno_gota()` e `encontrar_contorno_gota_robusto()`.

Extracao principal:

```python
cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
```

Formalmente, o contorno retornado e uma sequencia de pontos:

$$
P=\{(x_i,y_i)\}_{i=0}^{n-1}
$$

O OpenCV trata essa fronteira como fechada. Isso significa que o ultimo ponto e conectado ao primeiro para formar a fronteira da componente binaria. Essa linha de fechamento nao e necessariamente uma interface liquido-ar.

Filtros geometricos aplicados em `encontrar_contorno_gota_robusto()` incluem:

$$
Area\ge100
$$

$$
bw\ge20,\qquad bh\ge20
$$

$$
aspecto=\frac{\max(bw,bh)}{\min(bw,bh)}<8
$$

$$
circularidade=\frac{4\pi A}{P^2}>MIN\_CIRCULARITY
$$

O contorno deve ser considerado **contorno bruto da mascara**, nao perfil liquido-ar aberto.

### 9.9 Baseline pelo ajuste robusto

**Arquivo:** `linha_base/linha_base.py`  
**Funcoes:** `detect_baseline_tls()` e `_fit_line_robusta()`  
**Aplicacao:** deteccao da superficie/substrato.

A faixa inferior e selecionada pelo quantil:

$$
q=clip(1-bottom\_fraction,0.02,0.5)
$$

$$
y_{cut}=quantile(Y,q)
$$

$$
floor\_pts=\{(x_i,y_i):y_i\ge y_{cut}\}
$$

O ajuste de reta usa `cv2.fitLine(..., cv2.DIST_L1)` e produz $(v_x,v_y,x_0,y_0)$.

Distancia perpendicular:

$$
d_i=\frac{|v_y(x_i-x_0)-v_x(y_i-y_0)|}{\sqrt{v_x^2+v_y^2}}
$$

Filtro robusto MAD:

$$
med=median(d_i),
\qquad MAD=median(|d_i-med|)
$$

$$
sigma_{rob}=1.4826\cdot MAD
$$

$$
limiar=max(BASELINE\_INLIER\_MIN\_PIXELS,BASELINE\_INLIER\_MAD\_SCALE\cdot sigma_{rob})
$$

Um ponto e inlier se $d_i\le limiar$. A baseline final e:

$$
Y_{base}=quantile(Y_{inliers},0.90)
$$

O fallback usa $Y_{base}=max(Y_{contorno})$.

### 9.10 Extrapolacao dos pontos de contato

**Arquivo:** `linha_base/linha_base.py`  
**Funcao:** `find_contact_points_by_extrapolation()`  
**Aplicacao:** estimativa de $p_{esq}$ e $p_{dir}$.

Para cada lado, o ajuste e:

$$
X(Y)=aY^2+bY+c
$$

com:

```python
coeffs = np.polyfit(y_points, x_points, degree=2)
```

O contato e a extrapolacao na baseline:

$$
p_{contato}=(X(Y_{base}),Y_{base})
$$

O fallback geometrico seleciona extremos da faixa proxima da baseline. Se somente um lado e valido, o outro pode ser espelhado em torno de:

$$
x_{center}=mean(X_{contorno})
$$

### 9.11 Selecao da regiao local

**Arquivo:** `Cal_angulo/angulo_contato.py`  
**Funcao:** `_selecionar_pontos_lado()`  
**Aplicacao:** entrada do ajuste circular e da qualidade.

A altura da janela e:

$$
h_{janela}=clip(ANGLE\_WINDOW\_HEIGHT\_FACTOR\cdot(Y_{max}-Y_{min}),
ANGLE\_WINDOW\_HEIGHT\_MIN,ANGLE\_WINDOW\_HEIGHT\_MAX)
$$

A mascara vertical e:

$$
mask=(Y\le Y_{base}^{adj})\land(Y>Y_{base}^{adj}-h_{janela})
$$

O centro lateral e:

$$
x_{center}=\frac{x_{esq}+x_{dir}}{2}
$$

Esquerda usa $X<x_{center}$; direita usa $X>x_{center}$. Essa selecao ainda pode incluir o fechamento inferior se a mascara Binary estiver conectada ao substrato.

### 9.12 Ajuste circular de Kasa

**Arquivo:** `Cal_angulo/angulo_contato.py`  
**Funcao:** `ajustar_circulo_algebrico()`  
**Aplicacao:** ajuste do arco local para obter centro e raio.

Centralizacao:

$$
u=x-\bar{x},\qquad v=y-\bar{y}
$$

Somatorios:

$$
S_{uu}=\sum u^2,\quad S_{vv}=\sum v^2,\quad S_{uv}=\sum uv
$$

$$
S_{uuu}=\sum u^3,\quad S_{vvv}=\sum v^3,
\quad S_{uvv}=\sum uv^2,\quad S_{uuv}=\sum u^2v
$$

Sistema:

$$
A=\begin{bmatrix}S_{uu}&S_{uv}\\S_{uv}&S_{vv}\end{bmatrix},
\qquad
B=\frac12\begin{bmatrix}S_{uuu}+S_{uvv}\\S_{vvv}+S_{uuv}\end{bmatrix}
$$

$$
\begin{bmatrix}u_c\\v_c\end{bmatrix}=solve(A,B)
$$

$$
x_c=\bar{x}+u_c,\qquad y_c=\bar{y}+v_c
$$

O raio usado pelo codigo e a media das distancias:

$$
R=mean\left(\sqrt{(x_i-x_c)^2+(y_i-y_c)^2}\right)
$$

### 9.13 Tangente polinomial

**Arquivo:** `Cal_angulo/angulo_contato.py`  
**Funcoes:** `_selecionar_pontos_tangente()`, `_calcular_slope_tangente_polynomial()` e `calcular_vetor_tangente()`  
**Aplicacao:** vetor de tangente desenhado na interface.

O ajuste local usa:

$$
X(Y)=aY^2+bY+c
$$

Derivada:

$$
\frac{dX}{dY}=2aY+b
$$

No contato:

$$
m=\frac{dY}{dX}=\frac{1}{2aY_{contato}+b}
$$

Vetor normalizado:

$$
t=\frac{(1,m)}{\sqrt{1+m^2}}
$$

Se $m$ e infinito, o codigo usa o vetor vertical $(0,1)$.

### 9.14 Tangente geometrica do circulo

**Arquivo:** `Cal_angulo/angulo_contato.py`  
**Funcao:** `calcular_angulo_circular()`  
**Aplicacao:** calculo do angulo a partir da tangente perpendicular ao raio.

Vetor raio:

$$
r=(x_{contato}-x_c,y_{contato}-y_c)
$$

Vetor tangente perpendicular:

$$
t=(-r_y,r_x)
$$

Normalizacao:

$$
\hat{t}=\frac{t}{\|t\|}
$$

### 9.15 Intersecao circulo-baseline usada no calculo atual

**Arquivo:** `Cal_angulo/angulo_contato.py`  
**Funcao:** `calcular_angulo_circular()`  
**Aplicacao:** encontra a inclinacao da tangente no contato teorico.

Baseline ajustada:

$$
Y_{base}^{adj}=Y_{base}+3.0
$$

Distancia vertical entre baseline e centro:

$$
dy=Y_{base}^{adj}-y_c
$$

Se $|dy|<R$:

$$
dx=\sqrt{R^2-dy^2}
$$

Contato teorico:

$$
x_{contato}=\begin{cases}x_c-dx,& esquerda\\x_c+dx,& direita\end{cases}
$$

Inclinacao:

$$
m_{tangente}=-\frac{x_{contato}-x_c}{Y_{base}^{adj}-y_c}
$$

Angulo:

$$
	heta=degrees\left(atan(|m_{tangente}|)\right)
$$

Se $y_c>Y_{base}^{adj}$:

$$
	heta=180-\theta
$$

O codigo finaliza com saturacao numerica:

$$
	heta=clip(\theta,0,180)
$$

### 9.16 Qualidade do ajuste

**Arquivo:** `Cal_angulo/angulo_contato.py`  
**Funcao:** `calcular_qualidade_dinamica()`.

Para cada lado, calcula RMSE radial:

$$
d_i=\sqrt{(x_i-x_c)^2+(y_i-y_c)^2}
$$

$$
RMSE=\sqrt{mean((d_i-R)^2)}
$$

Score:

$$
score=exp\left(-\frac{RMSE_{medio}}{QUALITY\_RMSE\_REF\_PX}\right)
$$

com saturacao numerica entre $0$ e $1$.

### 9.17 Visualizacao das tangentes

**Arquivo:** `visualizacao/desenho.py`  
**Funcao:** `desenhar_tangente_vetor()`.

Comprimento desenhado:

$$
L=\frac{50}{zoom\_scale}
$$

Para vetor $(v_x,v_y)$ e contato $(x_c,y_c)$:

$$
P_1=(x_c-v_xL,y_c-v_yL)
$$

$$
P_2=(x_c+v_xL,y_c+v_yL)
$$

Os pontos sao convertidos para tela por:

$$
x_{tela}=x_{img}\cdot ratio+o_x,
\qquad y_{tela}=y_{img}\cdot ratio+o_y
$$

---

## 10. FORMULAS E LOCAIS DE APLICACAO: RESUMO

| Formula | Local | Funcao |
|---|---|---|
| Otsu invertido | `filtros.py` | `aplicar_filtro_binary_otsu()` |
| Fechamento morfologico | `filtros.py` | `aplicar_filtro_binary_otsu()` |
| `findContours(RETR_EXTERNAL, CHAIN_APPROX_NONE)` | `contorno.py` | `encontrar_contorno_gota()` / `_robusto()` |
| Distancia ponto-reta | `linha_base.py` | `_fit_line_robusta()` |
| MAD robusto | `linha_base.py` | `_fit_line_robusta()` |
| Quantil da baseline | `linha_base.py` | `_fit_line_robusta()` |
| `X(Y)=aY^2+bY+c` | `linha_base.py` | `find_contact_points_by_extrapolation()` |
| Janela vertical | `angulo_contato.py` | `_selecionar_pontos_lado()` |
| Circulo Kasa | `angulo_contato.py` | `ajustar_circulo_algebrico()` |
| Remocao por sigma | `angulo_contato.py` | `calcular_angulo_circular()` |
| Tangente polinomial | `angulo_contato.py` | `_calcular_slope_tangente_polynomial()` |
| Intersecao circulo-reta | `angulo_contato.py` | `calcular_angulo_circular()` |
| Tangente perpendicular ao raio | `angulo_contato.py` | `calcular_vetor_tangente()` |
| Coordenadas imagem/tela | `main.py` / `desenho.py` | renderizacao |

## 11. OBSERVACAO SOBRE O CONTORNO BINARY E A INTERFACE LIQUIDO-AR

O filtro Binary nao produz uma curva aberta. Ele produz uma mascara de regiao preenchida. Quando a regiao branca da gota toca a regiao branca do substrato, a componente conexa inclui a parte inferior da gota e o `findContours()` retorna uma fronteira externa fechada.

Assim, existem dois objetos geometricos distintos:

1. **Contorno bruto da mascara:** fronteira fechada da componente binaria, representada por `gota_pts`.
2. **Perfil liquido-ar fisico:** ramo superior/lateral entre os dois contatos com a baseline.

O codigo atual utiliza `gota_pts` diretamente em varias etapas. Portanto, a linha inferior visivel na captura nao e uma nova tangente: ela e o segmento inferior da fronteira da mascara Binary sobre o substrato.

Para a analise fisica, a regra correta e:

```text
gota_pts bruto
	-> baseline e contatos
	-> identificar o caminho continuo entre os contatos
	-> excluir o caminho inferior sobre o substrato
	-> perfil_liquido_ar
	-> tangente e angulo
```

Nao basta desenhar o contorno com `isClosed=False`, porque os mesmos pontos inferiores continuariam contaminando o ajuste. O perfil deve ser separado geometricamente antes do calculo.

## 12. CRITERIOS DE VALIDADE DO PERFIL

Um perfil pode ser considerado fisicamente utilizavel quando:

- existem baseline, contato esquerdo e contato direito;
- os contatos pertencem ao mesmo contorno;
- o caminho entre os contatos e contiguo na ordem do contorno;
- o caminho possui pontos acima da baseline;
- o caminho nao e apenas a linha horizontal do substrato;
- a janela local da tangente comeca proxima ao contato;
- o ajuste circular/polinomial possui pontos suficientes e variacao em X e Y.

Se os dois caminhos do contorno fechado forem igualmente plausiveis, a geometria deve ser marcada como ambigua, em vez de escolher um ramo arbitrariamente.

## 13. APIs E BIBLIOTECAS GRATUITAS

O projeto ja usa as ferramentas principais adequadas:

- **OpenCV:** limiarizacao, morfologia, Canny, Sobel, contornos e `fitLine`.
- **NumPy:** arrays, quantis, distancias, regressao e algebra linear.
- **SciPy:** poderia auxiliar em splines, RANSAC e otimizacao, caso seja incorporado futuramente.
- **scikit-image:** poderia auxiliar em componentes conectados, skeletonization e morfologia.

Nenhuma biblioteca gratuita conhece sozinha a interface liquido-ar. A regra fisica dos contatos e a separacao do ramo superior precisam continuar sendo definidas pelo programa.

---

Fim do documento.
