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

Fim do documento.
