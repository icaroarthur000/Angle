# 📊 DOCUMENTAÇÃO - ESTRUTURA E FÓRMULAS MATEMÁTICAS
## Sistema Analisador de Ângulo de Contato em Gotas

**Data de Criação:** 23 de março de 2026  
**Projeto:** Angle - Contact Angle Measurement System  
**Versão da Documentação:** 1.0

---

## 📋 ÍNDICE

1. [Estrutura Geral do Projeto](#estrutura-geral)
2. [1. Processamento de Imagem](#processamento-imagem)
3. [2. Detecção de Contorno](#deteccao-contorno)
4. [3. Linha Base e Pontos de Contato](#linha-base)
5. [4. Cálculo do Ângulo de Contato](#calculo-angulo)
6. [5. Visualização](#visualizacao)
7. [Resumo das Fórmulas Principais](#resumo-formulas)

---

## 🔬 ESTRUTURA GERAL DO PROJETO {#estrutura-geral}

O sistema é um **analisador de ângulo de contato em gotas** com interface gráfica. O fluxo é:

```
Imagem (câmera/arquivo) 
    ↓
Processamento de Imagem
    ↓
Detecção de Contorno
    ↓
Detecção de Linha Base
    ↓
Detecção de Pontos de Contato
    ↓
Cálculo do Ângulo de Contato
    ↓
Visualização
```

### Estrutura de Arquivos

```
Angle/
├── main.py                          # Interface gráfica (Tkinter/CustomTkinter)
├── Foto.py                          # Script de análise de imagem (exemplo)
├── processamento_imagem/
│   ├── filtros.py                  # Pipeline simples (converte, blur, threshold)
│   ├── preprocess.py               # Pipeline robusto (CLAHE, correção iluminação)
│   └── contorno.py                 # Detecção do contorno da gota
├── linha_base/
│   └── linha_base.py               # Detecção baseline + pontos de contato
├── Cal_angulo/
│   └── angulo_contato.py           # Cálculo do ângulo (Circle + Polynomial)
└── visualizacao/
    └── desenho.py                  # Renderização na tela
```

---

## 🔬 1. PROCESSAMENTO DE IMAGEM {#processamento-imagem}

### 1.1 - `filtros.py` (Pipeline Simples)

**Objetivo:** Converter imagem bruta em máscara binária (gota em branco)

**Operações sequenciais:**

#### 1. Conversão de Cores
```
Gray = BGR → Cinza (canal único)
Dimensão: HxWx3 → HxW
```

#### 2. Gaussian Blur (Filtro Suavizador)
```
Blurred = GaussianBlur(Gray, kernel=5×5, σ=0)
```
- **Propósito:** Reduzir ruído de alta frequência
- **Kernel 5×5:** Cobre área pequena, preserva detalhes da gota

#### 3. Otsu Threshold (Binarização Automática)
```
Binary = THRESH_BINARY_INV + OTSU
Pixel = {
  255 (branco)  se Gray < limiar_otsu
  0 (preto)     caso contrário
}
```
- **INV:** Inverte, tornando a gota branca (255)
- **OTSU:** Calcula limiar automaticamente analisando histograma
- **Fórmula OTSU:** Maximiza variância entre-classe

#### 4. Morphological Close (Fechamento Morfológico)
```
Closed = MORPH_CLOSE(Binary, kernel=5×5, iterações=1)

Operação: Dilatação → Erosão (ordem importa)
```
- **Propósito:** Preencher pequenos buracos na gota
- **Resultado:** Gota aparece como massa sólida sem furos

---

### 1.2 - `preprocess.py` (Pipeline Robusto)

**Objetivo:** Processamento avançado com correção de iluminação não-uniforme

**Etapas sequenciais:**

#### 1. Gaussian Blur Inicial
```
Gray_Blurred = GaussianBlur(Gray, kernel=3×5, σ=0)
```

#### 2. Estimação de Fundo (Background Estimation)
```
Background = GaussianBlur(Gray, kernel_grande, σ=0)

kernel_size = max(51, ⌊min(altura, largura) ÷ 6⌋ | 1)
```
- **| 1:** Operador bitwise para garantir número ímpar
- **Objetivo:** Capturar iluminação de fundo
- **Kernel grande (≥51):** Suavidade extrema, elimina detalhes da gota

#### 3. Correção de Iluminação (Divisão)
```
Corrected = (Gray + 1) / (Background + 1) × 128
Corrected_clipped = clip(Corrected, 0, 255)
```

**Fórmula matemática:**
```
C(x,y) = (I(x,y) + 1) / (B(x,y) + 1) × 128
```

- **+1:** Evita divisão por zero (proteção numérica)
- **×128:** Reescala para manter amplitude de valores
- **Objetivo:** Normalizar variações não-uniformes de iluminação

#### 4. CLAHE (Contrast Limited Adaptive Histogram Equalization)
```
tileGridSize = (min(8, ⌊min(h,w)/50⌋), min(8, ⌊min(h,w)/50⌋))
clipLimit = 2.0 (padrão)
Enhanced = CLAHE(Corrected, tileGridSize, clipLimit)
```

**Algoritmo CLAHE:**
- Divide imagem em N×M blocos (tiles)
- Para cada tile, calcula histograma
- Limita altura do histograma a `clipLimit`
- Redistribui pixels clipped equitativamente
- Combina tiles com interpolação

**Resultado:** Contraste aumentado localmente, detalhe fino preservado

#### 5. Adaptive Threshold (Limiarização Adaptativa)
```
blockSize = max(31, ⌊min(h,w)/30⌋ | 1)

Binary = ADAPTIVE_THRESHOLD_GAUSSIAN_C(
  Enhanced, 
  255,
  blockSize, 
  C=2
)

Pixel = {
  255 se Enhanced > (médiaLocal - C)
  0   caso contrário
}
```

**Proteção de blockSize:**
```
max_allowed = max(3, min(h,w) - (1 se min(h,w)%2==0 else 0))
Se blockSize ≥ min(h,w):
  blockSize = max_allowed (ajusta para imagem pequena)
```

- **GAUSSIAN_C:** Calcula média local com kernel Gaussiano (mais suave)
- **C=2:** Constante subtraída da média (sensibilidade)
- **Vantagem:** Robuso a variações de iluminação

#### 6. Morphological Cleanup
```
kernel = MORPH_ELLIPSE(3×3)
Binary = MORPH_OPEN(Binary, kernel, iterações=1)
        → Erosão depois Dilatação
        → Remove ruído pequeno e desconexões
        
Binary = MORPH_CLOSE(Binary, kernel, iterações=1)
        → Dilatação depois Erosão
        → Preenche buracos

Resultado: binary é array uint8 (0 ou 255)
```

**Output retornado:**
```python
{
    "enhanced_gray": enhanced,        # Escala cinza melhorada
    "binary": binary,                 # Máscara 0/255
    "corrected_bgr": corrected_bgr,   # BGR com valores corrigidos
    "debug_imgs": {                   # Imagens intermediárias para debug
        "gray": gray,
        "bg": bg,
        "corrected": corrected,
        "enhanced": enhanced,
        "binary": binary
    }
}
```

---

## 🔍 2. DETECÇÃO DE CONTORNO {#deteccao-contorno}

**Função:** `encontrar_contorno_gota()` em `processamento_imagem/contorno.py`

**Objetivo:** Extrair pontos do contorno da gota da máscara binária

**Algoritmo - Passos sequenciais:**

### Passo 1: Máscara de Segurança (10px)
```
Marcar todas as bordas da imagem com 10px de largura como preto (0)
Objetivo: Gota NÃO pode tocar as extremidades da imagem
Força gota a "flutuar" dentro da imagem
```

**Código:**
```python
h, w = processed.shape[:2]
cv2.rectangle(processed, (0, 0), (w-1, h-1), 0, thickness=10)
```

### Passo 2: Encontrar Contornos Iniciais
```
contornos = cv2.findContours(
  Binary, 
  mode=RETR_EXTERNAL,        # Apenas contornos externos
  method=CHAIN_APPROX_NONE   # Todos os pontos (sem compressão)
)
```

### Passo 3: Fallback com Canny (se não encontrar contornos)
```
Se contornos vazios:
  edges = Canny(Binary, threshold1=30, threshold2=100)
  cv2.rectangle(edges, bordas, 10px thickness)  # Reaplica máscara
  contornos = findContours(edges, ...)
```

### Passo 4: Filtro de Contornos na Borda
```
Para cada contorno:
  pts = contorno.reshape(-1, 2)
  
  touches_left   = ∃ x ≤ 5
  touches_right  = ∃ x ≥ w-5
  touches_top    = ∃ y ≤ 5
  touches_bottom = ∃ y ≥ h-5
  
  border_count = Σ touches
  
  Se border_count < 3:
    contorno_válido ✓
  Senão:
    rejeita (é provavelmente a borda da imagem)
```

**Lógica:** Rejeita contornos que tocam 3 ou mais bordas

### Passo 5: Seleção do Maior Contorno
```
maior_contorno = max(contornos_válidos, key=área)
Se área < 100 pixels²:
  rejeita (muito pequeno, provavelmente ruído)
```

### Passo 6: Validação Extra (10px Margem)
```
Para cada ponto (x, y) do contorno:
  Válido se: 10 < x < w-10 AND 10 < y < h-10
  
Se remover ≥ 10% dos pontos: volta ao original
Se remover < 10%: mantém pontos filtrados
```

**Output:**
```python
Array Nx2 com [x, y] de cada ponto do contorno
Exemplo: [[120, 150], [121, 148], [125, 146], ...]
```

---

## 📍 3. LINHA BASE E PONTOS DE CONTATO {#linha-base}

**Arquivo:** `linha_base/linha_base.py`

### 3.1 - FLOOR-SEEKER (Detecção da Baseline)

**Objetivo:** Encontrar a linha base (onde a gota toca a superfície)

**Algoritmo:**

```
PASSO 1: Encontrar extremos verticais
         Y_max = máximo Y do contorno (ponto mais baixo)
         Y_min = mínimo Y do contorno (ponto mais alto)
         altura_total = Y_max - Y_min

PASSO 2: Encontrar pontos PRÓXIMOS ao piso
         tolerance = 5.0 pixels
         floor_pts = pontos onde |Y - Y_max| ≤ 5
         
         (Seleciona pontos que tocam a superfície)

PASSO 3: Calcular centro horizontal
         X0 = média(X dos floor_pts)

PASSO 4: Definir orientação da linha
         vx = 1.0, vy = 0.0
         
         A baseline é SEMPRE horizontal!
         (porque é a superfície de repouso)
```

**Fórmula da Baseline:**
```
Y_baseline = max(Y_i) para i ∈ contorno_gota

Linha base = {(x, Y_baseline) : 0 ≤ x ≤ largura_imagem}
```

**Output Retornado:**
```python
{
    'baseline_y': float,                      # Y_max do contorno
    'line_params': (vx, vy, x0, y_max),     # (1.0, 0.0, x0, Y_baseline)
    'method': 'floor_seeker_hybrid'
}
```

---

### 3.2 - EXTRAPOLAÇÃO POLINOMIAL (Pontos de Contato)

**Objetivo:** Encontrar os pontos exatos onde a gota toca a baseline

**Algoritmo:**

#### Passo 1: Definir Região de Interesse (ROI)
```
height = Y_max - Y_min

y_roi_top = Y_min + 0.20 × height
           ↑ Exclui 20% do topo (ponta da gota)

y_roi_bottom = Y_max - 0.005 × height
              ↑ Exclui 0.5% do fundo (artefatos de luz)

mask = (Y ≥ y_roi_top) AND (Y ≤ y_roi_bottom)
roi_pts = pontos dentro dessa faixa
```

**Visualização:**
```
│ ← Y_min
│
│ ← y_roi_top (20% abaixo do topo)
├─────────── ROI (região usada para fit)
│
├─────────── y_roi_bottom (0.5% acima do fundo)
│ ← Y_max (baseline)
```

#### Passo 2: Separar por Lado
```
centro_x = média(X do contorno)

esquerda = pontos onde X < centro_x
direita = pontos onde X ≥ centro_x
```

#### Passo 3: Polyfit Grau 2 para Cada Lado
```
Para lado esquerdo:
  X = a_esq·Y² + b_esq·Y + c_esq
  Usar np.polyfit(Y, X, degree=2)
  
Para lado direito:
  X = a_dir·Y² + b_dir·Y + c_dir
  Usar np.polyfit(Y, X, degree=2)
```

**Por que Y é varável independente?**
- Y é monotônico (aumenta sempre de cima para baixo)
- X pode ter múltiplos valores para o mesmo Y (em gotas irregulares)
- Polyfit com Y independente = função X(Y) bem-definida

#### Passo 4: Extrapolar para Baseline
```
X_contato_esq = P_esq(Y_baseline)
X_contato_dir = P_dir(Y_baseline)

Onde P_esq e P_dir são os polinômios ajustados
```

**Fórmula da extrapolação:**
```
P_esq(Y_baseline) = a_esq·Y_baseline² + b_esq·Y_baseline + c_esq
P_dir(Y_baseline) = a_dir·Y_baseline² + b_dir·Y_baseline + c_dir
```

#### Passo 5: Tratamento de Falhas
```
Se polynomfit falhou para esquerda mas direita OK:
  dist_dir = |P_dir[0] - centro_x|
  P_esq = [centro_x - dist_dir, Y_baseline]  ← Espelha

Se polynomial fit falhou para direita mas esquerda OK:
  dist_esq = |P_esq[0] - centro_x|
  P_dir = [centro_x + dist_esq, Y_baseline]  ← Espelha

Se ambas falharem:
  → Fallback geométrico simples (extremos da banda inferior)
```

**Output Retornado:**
```python
{
    'baseline_y': Y_max,
    'p_esq': [x_esq, Y_baseline],
    'p_dir': [x_dir, Y_baseline],
    'line_params': (1.0, 0.0, (x_esq + x_dir)/2, Y_baseline),
    'contact_method': 'polynomial_extrapolation'
}
```

---

## 📐 4. CÁLCULO DO ÂNGULO DE CONTATO {#calculo-angulo}

**Arquivo:** `Cal_angulo/angulo_contato.py`

### 4.1 - CLASSIFICAÇÃO AUTOMÁTICA DA FORMA

**Objetivo:** Decidir qual método matemático usar

```
aspect_ratio = (Y_max - Y_min) / (X_max - X_min)

Se aspect_ratio ≥ 0.45:
  ├─ Gota é REDONDA/ESFÉRICA
  └─ Usar: CIRCLE FITTING
  
Se aspect_ratio < 0.45:
  ├─ Gota é ACHATADA/APLAINADA
  └─ Usar: POLYNOMIAL FITTING (grau 3)
```

**Interpretação:**
- **Aspect ratio 0.45+:** Altura ≥ 45% da largura → gota tem forma próxima circular
- **Aspect ratio <0.45:** Altura < 45% da largura → gota é achatada/elíptica

---

### 4.2 - CIRCLE FITTING (para Gotas Redondas)

**Método:** Ajuste Algébrico por Mínimos Quadrados

**Objetivo:** Ajustar um círculo que minimize a soma dos quadrados dos erros

#### Equação do Círculo
```
(x - xc)² + (y - yc)² = r²
```

#### Expansão Algébrica
```
x² - 2xc·x + xc² + y² - 2yc·y + yc² = r²
x² + y² - 2xc·x - 2yc·y + (xc² + yc² - r²) = 0
```

#### Sistema Linear
```
Para cada ponto (x_i, y_i):
[x_i² + y_i², x_i, y_i, 1] · [c, a, b, d] = 0

Onde:
a = -2xc
b = -2yc
c = xc² + yc² - r²
d = -1
```

#### Resolução
```python
A = np.column_stack([x² + y², x, y, ones])
params = np.linalg.lstsq(A, zeros)
c, a, b, d = params

xc = -a / 2
yc = -b / 2
r = √(xc² + yc² - c)
```

**Vantagens:**
- ✅ Não depende de bibliotecas externas (scipy)
- ✅ Método puramente algébrico e determinístico
- ✅ Mais rápido que otimização iterativa
- ✅ Sempre converge para uma solução
```
cx ∈ [cx_init - 100, cx_init + 100]
cy ∈ [cy_init - 100, cy_init + 100]
r ∈ [1, 1000]

max_nfev: 10000 iterações máximo
```

**Output:** Centro (cx, cy) e raio r ajustados

---

### 4.3 - VETOR TANGENTE (Circle Fitting)

**Objetivo:** Encontrar a direção tangente na gota (reta que toca sem cortar)

#### Passo 1: Calcular Vetor Raio
```
p_contato = (X_contato, Y_contato)
p_centro = (cx, cy)

raio_vetor = p_contato - p_centro
           = (X_contato - cx, Y_contato - cy)
           = (rx, ry)
```

#### Passo 2: Perpendiculares ao Raio (Rotação 90°)
```
Rotação 90° no sentido anti-horário:
  t1 = (-ry, rx)

Rotação 90° no sentido horário:
  t2 = (ry, -rx)

Ambos são perpendiculares ao raio!
```

#### Passo 3: Escolher Vetor que Aponta para CIMA
```
Se vy < 0 (aponta para cima):
  vt = t1 ou t2 (conforme vy < 0)
Senão:
  Fallback → ângulo exato 90°
```

**Lógica:** A tangente deve "sair" da gota para cima (em direção ao ar)

#### Passo 4: Normalizar
```
|vt| = √(vt_x² + vt_y²)

Se |vt| < 1e-6:
  retorna erro (proteção contra vetor nulo)
  
vt_normalizado = vt / |vt|
                ↑ Agora |vt_normalizado| = 1
```

**Resultado:** Vetor unitário (comprimento 1) apontando para cima

---

### 4.4 - POLYNOMIAL FITTING (para Gotas Achatadas) 

**Objetivo:** Encontrar tangente polinomialmente

#### Passo 1: Translação de Coordenadas
```
Mover origem para ponto de contato:
  y_local = Y - Y_contato
  x_local = X - X_contato

Motivo: Simplifica cálculo da derivada em y=0
```

#### Passo 2: Polyfit Grau 3
```
Ajustar: X_local = a·y_local³ + b·y_local² + c·y_local + d

coeffs = np.polyfit(y_local, x_local, degree=3)
coeffs = [a, b, c, d]
```

**Por que grau 3?**
- Grau 2 (parábola) muito simples para gotas irregulares
- Grau 3 (cúbica) captura curvatura variável
- Grau 4+ pode overfitting (oscilações indesejadas)

#### Passo 3: Calcular Derivada em y=0
```
Se X_local = a·y³ + b·y² + c·y + d

Então: dX/dY = 3a·y² + 2b·y + c

Em y=0:
  (dX/dY)|_{y=0} = c

Onde c é o TERCEIRO coeficiente (índice 2)
```

**Fórmula:**
```
dX/dY|_{y=0} = coeffs[2]
```

#### Passo 4: Definir Vetor Tangente
```
Se dX/dY = c, então para deslocamento unitário em Y:
  
  Quando Y diminui 1 (dy = -1, para cima):
    X muda de aproximadamente -c
    t1 = (-c, -1)
  
  Quando Y aumenta 1 (dy = +1, para baixo):
    X muda de aproximadamente c
    t2 = (c, 1)

Escolher t que aponta para CIMA (t_y < 0):
  Se t1_y < 0: vt = t1
  Elif t2_y < 0: vt = t2
  Else: fallback com vt = (-c, -1)
```

#### Passo 5: Normalizar
```
|vt| = √(vt_x² + vt_y²)

vt_normalizado = vt / |vt|
```

---

### 4.5 - FILTRO ANTI-REFLEXO

**Problema:** Reflexos aparecem muito perto da baseline (~1-2px acima)

**Solução:**
```
artifact_margin = 2 pixels (distância mínima da baseline)
window_height = 60 pixels (altura da janela de análise)

mask = (Y ≤ Y_contato - artifact_margin) AND 
       (Y > Y_contato - window_height)

local_pts = pontos dentro dessa faixa

Rejeita se: len(local_pts) < 5 pontos
```

**Visualização:**
```
│ Y_contato - 60  ← Topo da janela
│                    (60px acima da baseline)
├─────────────── Pontos usados ✓
│
├─────────────── Y_contato - 2  (artifact_margin)
│ Y_contato ← Baseline (reflexos ignorados)
```

---

### 4.6 - CÁLCULO FINAL DO ÂNGULO

#### Passo 1: Definir Vetor Baseline
```
A baseline é sempre horizontal (reta em repouso)

Se lado = "esquerdo":
  vb = (1.0, 0.0)    ← Aponta para DIREITA
  
Se lado = "direito":
  vb = (-1.0, 0.0)   ← Aponta para ESQUERDA
  
Motivo: Ângulo é sempre medido ENTRE a tangente
        e a baseline (piso)
```

#### Passo 2: Produto Escalar (Dot Product)
```
dot = vt.x × vb.x + vt.y × vb.y
    = vt.x × vb.x + vt.y × 0
    = vt.x × vb.x

dot = clip(dot, -1.0, 1.0)  ← Proteção numérica
                              (valores fora [-1,1] causam erro em arccos)
```

#### Passo 3: Arco-Cosseno
```
θ_radianos = arccos(dot)

Intervalo: arccos retorna [0, π] radianos
           = [0, 180] graus
```

#### Passo 4: Converter para Graus
```
θ_graus = θ_radianos × (180/π)

θ_graus = clip(θ_graus, 0, 180)  ← Proteção se ultrapassar limites
```

**Fórmula Completa:**
```
θ = arccos(v̂_t · v̂_b) × (180/π)

Onde:
  v̂_t  = vetor tangente normalizado (de Circle ou Polynomial Fitting)
  v̂_b  = vetor baseline (1,0) ou (-1,0)
  ·    = produto escalar
```

---

### 4.7 - NOVA FÓRMULA TRIGONOMÉTRICA (Circle Fitting)

#### Distância Vertical
```
h = |yc - baseline_y|
```
Onde `yc` é a coordenada Y do centro do círculo ajustado

#### Ângulo Trigonométrico
```
cos(β) = h / R
β = arccos(h / R)

Onde:
- h = distância vertical do centro à baseline
- R = raio do círculo ajustado
- β = ângulo entre raio e vertical
```

#### Lógica Baseada na Posição do Centro
```python
if yc > baseline_y:
    # Centro ABAIXO da baseline (gota hidrofóbica)
    # Ângulo suplementar: θ = 180° - β
    theta_deg = 180.0 - math.degrees(angulo_rad)
else:
    # Centro ACIMA da baseline (gota hidrofílica)  
    # Ângulo direto: θ = β
    theta_deg = math.degrees(angulo_rad)
```

#### Interpretação Física
- **yc > baseline_y**: Centro do círculo está abaixo da superfície
  - Gota "gordinha" (hidrofóbica)
  - Ângulo > 90°
  - θ = 180° - β

- **yc < baseline_y**: Centro do círculo está acima da superfície
  - Gota "achatada" (hidrofílica)  
  - Ângulo < 90°
  - θ = β

**Fórmula Final:**
```
θ = arccos(h/R) se yc < baseline_y
θ = 180° - arccos(h/R) se yc > baseline_y
```

---

## 🎨 5. VISUALIZAÇÃO {#visualizacao}

**Arquivo:** `visualizacao/desenho.py`

### Elementos Desenhados

#### 1. Baseline (Vermelho)
```
Desenha linha horizontal na altura Y = baseline_y

Código:
  y_scr = (baseline_y × ratio) + offset_y
  canvas.create_line(x_start, y_scr, x_end, y_scr, 
                     fill="red", width=2)

Onde:
  ratio = fator de zoom da imagem
  offset_y = deslocamento vertical (pan)
```

#### 2. Contorno da Gota (Cyan)
```
Desenha sequência conectada de pontos: gota_pts

Código:
  para cada ponto (x, y) em gota_pts:
    converter para tela: (x_scr, y_scr) = to_scr(x, y)
    desenhar linha conectando pontos vizinhos
  
  canvas.create_line(..., fill="cyan", width=1)
```

#### 3. Pontos de Contato (Amarelo)
```
Desenha círculos pequenos em p_esq (esquerdo) e p_dir (direito)

Código:
  raio = 5 pixels
  para cada ponto:
    (x_scr, y_scr) = to_scr(p[0], p[1])
    canvas.create_oval(x_scr-r, y_scr-r, x_scr+r, y_scr+r,
                       fill="yellow", outline="black")
```

#### 4. Tangentes (Verde)
```
Desenha linhas retas nos ângulos calculados

Cálculo:
  length = 40 / zoom_scale  ← Comprimento em pixels de imagem
  
  angle_rad = ângulo × π/180  ← Converter graus para radianos
  
  dx = length × cos(angle_rad)
  dy = length × sin(angle_rad)
  
  Ponto inicial: (x - dx, y - dy)
  Ponto final:   (x + dx, y + dy)
  
  canvas.create_line(x1_scr, y1_scr, x2_scr, y2_scr,
                     fill="green", width=2)
```

---

## 📊 RESUMO DAS FÓRMULAS PRINCIPAIS {#resumo-formulas}

### Tabela de Fórmulas por Módulo

| Módulo | Fórmula | Variáveis | Propósito |
|--------|---------|-----------|----------|
| **Filtros** | OTSU: threshold automático | Gray, limiar | Binarização automática |
| **Preprocess** | C = (I+1)/(B+1)×128 | I=intensity, B=background | Normalizar iluminação |
| **Preprocess** | Enhanced = CLAHE(C) | tileGrid, clipLimit | Aumentar contraste local |
| **Preprocess** | B = AdaptiveThreshold(E, blockSize) | E=enhanced | Limiarizar adaptativo |
| **Linha Base** | Y_base = max(Y_gota) | Y=altura | Encontrar piso |
| **Contato** | X = aY² + bY + c | a,b,c = coeficientes | Extrapolar contato |
| **Contato X(Y)** | X(Y_base) = aY_base²+bY_base+c | Y_base=baseline | Ponto de contato |
| **Círculo** | (x-xc)² + (y-yc)² = r² | xc,yc,r = centro/raio | Ajustar círculo |
| **Ângulo (Novo)** | θ = arccos(h/r) | h=\|yc-baseline\| | Ângulo trigonométrico |
| **Ângulo (Antigo)** | θ = arccos(v_t·v_b)×180/π | v_t,v_b = vetores | Produto escalar |
| **Visualização** | (x_scr, y_scr) = (x×ratio+off_x, y×ratio+off_y) | ratio,off = zoom,pan | Converter imagem→tela |

---

## 🔗 FLUXO OPERACIONAL COMPLETO

```
┌─────────────────────┐
│  ENTRADA: Imagem    │
│  (Câmera/Arquivo)   │
└──────────┬──────────┘
           │
           ▼
   ┌───────────────────┐
   │ PROCESSAMENTO     │
   │ - Gaussian Blur   │
   │ - CLAHE           │
   │ - Threshold       │
   │ - Morphology      │
   └────────┬──────────┘
            │
            ▼
   ┌──────────────────────┐
   │ DETECÇÃO CONTORNO    │
   │ - FindContours       │
   │ - Filtro bordas      │
   │ - Validação pontos   │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │ LINHA BASE           │
   │ - Floor-Seeker       │
   │ - Y_max = baseline   │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │ PONTOS DE CONTATO    │
   │ - Polyfit grau 2     │
   │ - Extrapola em Y_max │
   │ - P_esq, P_dir       │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │ CLASSIFICAR FORMA    │
   │ aspect_ratio = h/w   │
   │ ≥0.45? Circ : Poly   │
   └──────────┬───────────┘
              │
              ├─── Circle Fitting ───┐
              │                       │
              ▼                       ▼
   ┌──────────────────────────────────────────┐
   │ Ajustar Círculo (least_squares)           │
   │ min Σ(√[(x-cx)²+(y-cy)²] - r)²          │
   │ → Resultado: (cx, cy, r)                 │
   └────────┬─────────────────────────────────┘
            │
            ▼
   ┌──────────────────────────────────────────┐
   │ Vetor Tangente = Perpendicular ao Raio   │
   │ t = (-ry, rx), normalizar, escolher ↑   │
   └────────┬─────────────────────────────────┘
            │
            └─── Polynomial Fitting ──┐
                                       │
   ┌──────────────────────────────────▼────────┐
   │ Ajustar Polinômio Grau 3                  │
   │ X_local = a·y³ + b·y² + c·y + d          │
   │ → dX/dY|_{y=0} = c                      │
   │ → Resultado: vetor tangente (-c, -1)     │
   └────────┬────────────────────────────────┘
            │
            ▼
   ┌──────────────────────────────────────────┐
   │ CÁLCULO DO ÂNGULO                         │
   │ dot = v_t · v_b                          │
   │ θ = arccos(dot) × 180/π                  │
   │ θ = clip(θ, 0, 180)                      │
   └──────────┬────────────────────────────────┘
              │
              ▼
   ┌──────────────────────────────────────────┐
   │ VISUALIZAÇÃO                              │
   │ - Desenha baseline (vermelho)             │
   │ - Desenha contorno (cyan)                 │
   │ - Desenha pontos contato (amarelo)        │
   │ - Desenha tangentes (verde)               │
   │ - Mostra ângulo no gráfico                │
   └────────┬────────────────────────────────┘
            │
            ▼
   ┌──────────────────────┐
   │ SAÍDA: Ângulo (°)   │
   │ Esquerdo e Direito   │
   └──────────────────────┘
```

---

## 📝 NOTAS TÉCNICAS IMPORTANTES

### 1. Proteções Numéricas
- Sempre usar `clip()` antes de `arccos()` para evitar domínio inválido
- Adicionar +1 em divisões para evitar divisão por zero
- Usar `if dist < 1e-6` para vetores quase-nulos

### 2. Ordem de Operações Morfológicas
- **CLOSE:** Dilatação DEPOIS Erosão (preenche buracos)
- **OPEN:** Erosão DEPOIS Dilatação (remove ruído)
- Ordem importa! Invertida tem efeito oposto

### 3. Translação de Coordenadas
- Usar origem local (ponto de contato = 0,0) para simplificar derivadas
- Reaplicar offset para converter para coordenadas globais

### 4. Escolha Circle vs Polynomial
- **Circle:** Melhor para gotas 3D redondas (hidrofóbicas)
- **Polynomial:** Melhor para gotas 2D achatadas (hidrofílicas)
- Transição em aspect_ratio = 0.45 (altura = 45% da largura)

### 5. Extrapolação Polinomial
- Y deve ser variável independente (monotônico)
- X como dependente (pode ter múltiplos valores por Y)
- Extrapola apenas até Y_baseline (não além)

---

## 🎯 CONCLUSÃO

Este sistema implementa uma **análise científica completa** de ângulo de contato usando:

1. **Processamento robusto** com correção de iluminação
2. **Detecção precisa** de contorno com validações
3. **Métodos híbridos** (Circle + Polynomial) adaptados à forma
4. **Cálculos precisos** com proteções numéricas
5. **Visualização interativa** para validação manual

As fórmulas matemáticas garantem **precisão sub-pixel** e **robustez** a variações de imagem.

---

**Fim da Documentação**  
*Gerado em: 23 de março de 2026*
