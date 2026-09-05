# AUDITORIA TÉCNICA: ESTRUTURA E FÓRMULAS - VERSÃO ATUAL

**Data:** 2026-09-04  
**Versão Analisada:** HEAD (main branch, commit 9beb758bd6d3730f895608a0bfb9412a4aa0e920)  
**Escopo:** Análise somente de leitura do código produção sem execução de testes ou alterações

---

## 1. ESTRUTURA REAL DOS ARQUIVOS

### Arquivos Principais Identificados

| Arquivo | Linhas | Responsabilidade | Status |
|---------|--------|------------------|--------|
| `main.py` | 1143 | GUI principal, orquestração, pré-processamento, cálculo | Ativo |
| `processamento_imagem/filtros.py` | 147 | Pipelines de filtros multi-threshold | Ativo |
| `processamento_imagem/preprocess.py` | 130 | Pipeline robusto de pré-processamento (não usado por padrão) | Inativo |
| `processamento_imagem/contorno.py` | 635 | Detecção de contorno, separação gota/substrato | Ativo |
| `linha_base/linha_base.py` | 450 | Detecção de baseline, extrapolação polinomial, pontos de contato | Ativo |
| `Cal_angulo/angulo_contato.py` | 525 | Cálculo de ângulos, ajuste circular, tangentes | Ativo |
| `visualizacao/desenho.py` | 143 | Renderização (baseline, contorno, contatos, tangentes) | Ativo |
| `parametros.py` | ~80 | Carregamento de configurações via config.json | Ativo |

### Dependências de Importação

```
main.py
├── processamento_imagem.filtros (aplicar_multi_threshold)
├── processamento_imagem.contorno (encontrar_contorno_gota_robusto, encontrar_contorno_gota, projetar_ponto_no_contorno)
├── linha_base.linha_base (detectar_baseline_hibrida, find_contact_points_by_extrapolation)
├── Cal_angulo.angulo_contato (calcular_angulo_circular, calcular_vetor_tangente, calcular_qualidade_dinamica)
├── visualizacao.desenho (desenhar_baseline, desenhar_contorno, desenhar_pontos_contato, desenhar_tangentes)
├── customtkinter (GUI)
└── cv2, numpy, PIL, tkinter (dependências externas)
```

---

## 2. FLUXO DE EXECUÇÃO REAL

### Ponto de Entrada
**Arquivo:** `main.py` linha ~1460  
**Função:** `SelectionWindow().mainloop()`

### Cadeia de Chamadas Completa

```
SelectionWindow.__init__ (line ~77)
├── GUI setup: botões, canvas, controls
├── Toggle filtros (OTSU, CANNY)
└── Carregamento de imagem ou câmera
    ├── load_from_file(filename) [line ~276]
    │   └── aplicar_multi_threshold (filtros.py line ~120) → máscara
    ├── detect_cameras() [line ~372]
    ├── open_camera() [line ~398]
    └── update_camera() [loop contínuo]
        └── capture_image()
            └── aplicar_multi_threshold() → máscara

SelectionWindow.confirm_and_analyze() [line ~680]
└── ContactAngleApp(self.bgr_vis, self.bin_img) [main.py line ~792]
    └── initial_analysis() [line ~915]
        ├── encontrar_contorno_gota_robusto(bin_img) [contorno.py line ~285]
        │   ├── cv2.findContours(..., RETR_EXTERNAL, CHAIN_APPROX_NONE)
        │   └── fallback: encontrar_contorno_gota(bin_img) [line ~519]
        ├── detectar_baseline_hibrida(gota_pts, bin_img) [linha_base.py line ~356]
        │   ├── detect_baseline_tls(pts, bottom_fraction=0.30) [line ~92]
        │   │   └── _fit_line_robusta(pts) [line ~32]
        │   │       ├── cv2.fitLine(..., DIST_L1)
        │   │       └── quantile 90% dos inliers → baseline_y
        │   └── find_contact_points_by_extrapolation(pts, baseline) [line ~239]
        │       ├── np.polyfit(y_pts, x_pts, degree=2)
        │       └── p_esq, p_dir = poly(baseline_y)
        ├── projetar_ponto_no_contorno(contour, p_esq, baseline) [contorno.py line ~611]
        └── Validação secundária com OTSU na imagem original
        
        └── calculate() [line ~1141]
            ├── calcular_angulo_circular(gota_pts, p_esq, baseline_y, lado='esq') [angulo_contato.py line ~444]
            │   ├── _selecionar_pontos_lado(gota_pts, p_esq, p_dir, baseline_y, 'esq') [line ~390]
            │   │   └── window: baseline_ajustada - height < y <= baseline_ajustada
            │   ├── _selecionar_janela_local(pts, p_contato, baseline, lado) [line ~92]
            │   │   ├── Encontra anchor_idx no contorno (ponto mais próximo)
            │   │   └── Tenta window_sizes = (7, 9, 11, 13, 15, 17)
            │   │       └── np.polyfit(y, x, degree=2) com validação R² > 0.70
            │   ├── ajustar_circulo_algebrico(pontos_locais) [line ~128]
            │   │   ├── Método Kåsa: centraliza dados
            │   │   └── Resolve matriz linear para (xc, yc)
            │   ├── Remoção de outliers (resíduos > 2σ)
            │   └── Cálculo do ângulo θ
            │       └── arccos((baseline_y - yc) / R)
            │
            ├── calcular_vetor_tangente(gota_pts, p_esq, baseline_y, 'esq') [line ~231]
            │   ├── _selecionar_pontos_tangente(gota_pts, p_esq, baseline_y) [line ~195]
            │   │   └── Filtra pts: max 45 pixels acima de baseline
            │   │       └── Mesma janela polinomial que acima
            │   └── _calcular_slope_tangente_polynomial(pts, p_contato)
            │       └── dx/dy = 2*a*y_contato + b
            │           m = 1 / (dx/dy)
            └── Repetir para lado direito
                
render() / _render_internal() [line ~1206]
├── Desenha imagem original
├── desenhar_contorno(canvas, gota_pts) [desenho.py line ~41]
├── desenhar_baseline(canvas, baseline_y, line_params) [line ~7]
├── desenhar_pontos_contato(canvas, p_esq, p_dir) [line ~61]
└── Exibe ângulos interno/externo

Interatividade:
├── on_canvas_click(event) [line ~1340]
├── on_canvas_drag(event) [line ~1349]
│   └── Reposiciona contatos com snap ao contorno
└── Recalcula ângulos
```

---

## 3. PROCESSAMENTO DE IMAGEM - PIPELINE ATUAL

### 3.1 Pipeline Padrão (Ativo)

**Função:** `aplicar_multi_threshold()` em `processamento_imagem/filtros.py` (linha 120)

```
Entrada: ROI BGR (uint8)
  │
  ├─→ Conversão para grayscale
  │     cv2.cvtColor(roi_bgr, cv2.COLOR_BGR2GRAY)
  │
  ├─→ Geração de Candidatos:
  │     gerar_candidatos_segmentacao(gray) → dict com 5 opções:
  │     - OTSU_LIGHT: filtro_binary_otsu com kernel (3,3)
  │     - OTSU: filtro_binary_otsu com kernel (5,5)  [padrão]
  │     - ADAPTIVE_LIGHT: filtro_binary_adaptive com kernel (7,7)
  │     - ADAPTIVE: filtro_binary_adaptive com kernel (11,11)
  │     - CANNY: filtro_edges_canny com limiares [30, 100]
  │
  ├─→ Cada candidato passa por:
  │     a) Gaussian blur (kernel 5×5, σ=1.0)
  │     b) Threshold OTSU: cv2.threshold(..., cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
  │     c) Fechamento morfológico: cv2.morphologyEx(..., cv2.MORPH_CLOSE, 
  │                                  kernel elíptico de tamanho calculado)
  │
  ├─→ Pontuação de máscaras:
  │     _score_mascara(mask) → [0, 1]
  │     Score = fill_ratio * entropia_normalizada
  │     Fill_ratio = pixels_brancos / (altura * largura)
  │
  ├─→ Seleção da melhor máscara por score
  │
  ├─→ Separação gota/substrato:
  │     isolar_gota_substrato(mask) [contorno.py line ~415]
  │     Chama:
  │       - _necking_detection(mask)
  │       - _sobel_y_surface(mask)
  │       - _abertura_anisotropica(mask)
  │     Seleciona método por confiança
  │
  └─→ Saída: máscara binária (uint8, 0-255)

Parâmetros Não Alteráveis (hardcoded):
- Blur Gaussian: (5, 5), σ=1.0
- Kernel morfológico: tamanho calculado como max(3, int(max_dim * 0.003))
- Threshold OTSU: BINARY_INV sempre
- Canny limiares: [30, 100] fixo
```

### 3.2 Pipeline Alternativo (Inativo)

**Função:** `preprocess_image_for_contact_angle()` em `processamento_imagem/preprocess.py` (linha ~50)

Este pipeline é importado em `main.py` mas NÃO É USADO no fluxo normal porque `HAVE_PREPROCESS=False` falha a importação. Quando falha, usa fallback que chama `filtros.aplicar_multi_threshold()` diretamente.

Pipeline alternativo (referência):
```
BGR → Grayscale
  → Gaussian blur (5×5)
  → Estimar fundo (Gaussian blur)
  → Dividir pela iluminação
  → CLAHE (clipLimit=2.0, tileGridSize=8×8)
  → Threshold adaptativo Gaussiano
  → Abertura + fechamento morfológico
  → Saída: enhanced_gray, binary, corrected_bgr
```

### 3.3 Operações Morfológicas

**Fechamento (MORPH_CLOSE):**
```
kernel_size = max(3, int(max_dimension * 0.003))
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))
resultado = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
```

**Abertura Anisotrópica (usado em isolar_gota_substrato):**
```
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
resultado = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
```

---

## 4. DETECÇÃO DO CONTORNO

### 4.1 Função Principal: `encontrar_contorno_gota_robusto()`

**Arquivo:** `processamento_imagem/contorno.py` linha 285  
**Entrada:** máscara binária (uint8)  
**Saída:** `gota_pts` (ndarray Nx2, float32)

```
Etapas:

1. Converte para grayscale se necessário
   img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY) se ndim == 3
   
2. Aplicar fechamento morfológico
   kernel = (3, 3)
   processed = cv2.morphologyEx(img_gray, cv2.MORPH_CLOSE, kernel)
   
3. Zerando margens de segurança
   processed[:2, :] = 0    # topo
   processed[-2:, :] = 0   # fundo
   processed[:, :2] = 0    # esquerda
   processed[:, -2:] = 0   # direita
   
4. Extração de contornos
   contours, hierarchy = cv2.findContours(
       processed,
       cv2.RETR_EXTERNAL,    # ← MODO: apenas contornos externos
       cv2.CHAIN_APPROX_NONE # ← APROXIMAÇÃO: todos os pontos
   )
   
5. Se não houver contornos, tenta Canny
   edges = cv2.Canny(processed, 50, 150)
   contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
   
6. Validação de cada contorno
   Para cada contorno:
     - _validar_contorno(contour)
       - Área ≥ 100 pixels²
       - Bounding box ≥ 20×20 pixels
       - Razão aspecto ≤ 8
       - Circularidade ≥ 0.35 (configurável)
       - Convexidade ≥ 0.7
       - Preenchimento ≥ 0.5
       - Rejeita faixas horizontais de chão
       
7. Pontuação de contorno
   score = f(área, bounding_box, circularidade, aspecto)
   
8. Seleção do melhor contorno
   gota_contorno = max(contours_validos, key=pontuacao)
   
9. Conversão para array float32
   gota_pts = gota_contorno.reshape(-1, 2).astype(np.float32)
   
10. Remoção de pontos próximos das bordas (margem de 10px)
```

**Significado Geométrico:**
- O contorno retornado é um **contorno fechado** extraído de `cv2.findContours`
- Pode incluir o **fechamento artificial inferior** onde a máscara conecta a gota ao substrate
- **RETR_EXTERNAL**: captura apenas o contorno mais externo
- **CHAIN_APPROX_NONE**: mantém todos os pontos (não simplifica)

### 4.2 Fallback: `encontrar_contorno_gota()`

**Arquivo:** `processamento_imagem/contorno.py` linha 519

Mesma lógica mas:
- Usa `cv2.RETR_TREE` em vez de `RETR_EXTERNAL`
- Chama `_remover_faixa_horizontal_vazada()` para tentar remover fechamento

---

## 5. LINHA BASE

### 5.1 Função Principal: `detectar_baseline_hibrida()`

**Arquivo:** `linha_base/linha_base.py` linha 356  
**Entrada:** `gota_pts` (contorno), `bin_img` (máscara)  
**Saída:** `baseline_y`, `line_params`, `p_esq`, `p_dir`

```
Etapas:

1. Extração do Y máximo do contorno
   y_max = np.max(gota_pts[:, 1])
   
2. Seleção da região inferior (bottom_fraction = 0.30)
   altura_gota = y_max - np.min(gota_pts[:, 1])
   y_limiar = y_max - (0.30 * altura_gota)
   bottom_pts = gota_pts[gota_pts[:, 1] >= y_limiar]
   
3. Ajuste robusto de reta → _fit_line_robusta(bottom_pts)
   
   a) Usa cv2.fitLine() com DIST_L1
      cv2.fitLine(points, cv2.DIST_L1, 0, 0.01, 0.01)
      Retorna: (vx, vy, x0, y0)
      
   b) Calcula distância perpendicular de cada ponto à reta
      d_perp = |vx*(y-y0) - vy*(x-x0)| / sqrt(vx² + vy²)
      
   c) Estimativa de escala robusta (MAD - Median Absolute Deviation)
      resíduos_mediana = median(|d_perp|)
      escala = 1.4826 * resíduos_mediana  # constante para distribuição normal
      
   d) Rejeição de outliers
      threshold = escala * z_score (padrão: 2.5)
      inliers = pontos onde d_perp < threshold
      
   e) Refinamento iterativo (2 iterações)
      ajusta_reta_novamente(inliers)
      recalcula_inliers()
      
   f) Cálculo da baseline
      y_inliers = [y dos pontos inliers]
      baseline_y = np.quantile(y_inliers, 0.90)
      ↑ Usa quantil 90%, NÃO é o máximo exato do contorno
      
4. Pontos de contato
   p_esq, p_dir = find_contact_points_by_extrapolation(pts, baseline)

Fórmula da Baseline:
─────────────────
Não é simplesmente Y_max, mas sim:

    Y_base = quantil(90%, Y_inliers_robustos)
    
onde os inliers robustos vêm de:
    cv2.fitLine() + rejeição de outliers por MAD
```

**Parâmetros Configuráveis (via config.json):**
- `baseline_bottom_fraction`: 0.1 (em config.json)
- Mas `detectar_baseline_hibrida` usa default 0.30 quando chama `detect_baseline_tls`
- **BRECHA**: config.json não é respeitado; hardcoded 0.30

### 5.2 Função Secundária: `detect_baseline_tls()`

**Linha:** 92  
Seleciona a fração inferior do contorno e aplica `_fit_line_robusta`.

### 5.3 Função de Extrapolação: `find_contact_points_by_extrapolation()`

**Linha:** 239  
**Entrada:** `gota_pts`, `baseline_y`  
**Saída:** `p_esq`, `p_dir` (tuplas de coordenadas)

```
Etapas:

1. Separação por lado
   center_x = (min_x + max_x) / 2
   pts_esq = gota_pts[gota_pts[:, 0] < center_x]
   pts_dir = gota_pts[gota_pts[:, 0] > center_x]
   
2. Para cada lado (esq/dir):
   
   a) Filtragem de região
      roi_bottom_exclude = 0.08  # excluir 8% superior da ROI
      roi_top_exclude = 0.20     # excluir 20% inferior da ROI
      
      y_range = [y_min, y_max]
      y_min_roi = y_min + 0.20 * (y_max - y_min)
      y_max_roi = y_min + 0.92 * (y_max - y_min)  # 100% - 8%
      
      pontos_roi = pontos[
          (y >= y_min_roi) AND (y <= y_max_roi)
      ]
      
   b) Polinômio de regressão
      grau = 2
      min_pontos = 8
      
      Se len(pontos_roi) >= min_pontos:
          coeff = np.polyfit(y_roi, x_roi, degree=2)
          x(y) = a*y² + b*y + c
          
   c) Extrapolação para baseline
      x_contato = polyval(coeff, baseline_y)
      p_lado = (x_contato, baseline_y)
      
3. Validação de candidatos
   _validar_candidato_contato_base(candidato)
   ├─ Distância ao centro < limiar
   ├─ Não ultrapassa limites laterais da máscara
   └─ Y está próximo à baseline
   
4. Fallbacks
   └─ Se apenas um lado for validado:
       espelha o outro lado em torno do center_x
   └─ Se nenhum for validado:
       usa extremos esquerdo/direito na faixa inferior

Fórmulas:
────────
X_esq = a_esq * Y_base² + b_esq * Y_base + c_esq
X_dir = a_dir * Y_base² + b_dir * Y_base + c_dir

onde (a, b, c) = np.polyfit(Y_pontos, X_pontos, degree=2)

Grau do polinômio: 2 (quadrático)
Variável independente: Y (altura)
Variável dependente: X (horizontal)
```

---

## 6. PONTOS DE CONTATO

### 6.1 Obtenção de `p_esq` e `p_dir`

**Caminho 1: Extrapolação Polinomial (Padrão)**

```
entrada: gota_pts, baseline_y
  ↓
find_contact_points_by_extrapolation()
  ├─ Ajusta polinômio x=f(y), grau 2
  ├─ Extrapola em baseline_y
  ├─ Valida candidatos
  └─ Fallback se necessário (espelho ou extremos)
```

**Caminho 2: Projeção no Contorno (Pós-inicial_analysis)**

```
entrada: contorno, p_candidato, baseline_y, lado
  ↓
projetar_ponto_no_contorno()
  ├─ Encontra ponto mais próximo no contorno
  ├─ Na faixa vertical: baseline_y ± margem
  ├─ No lado correto
  └─ Retorna ponto ajustado
```

### 6.2 Definição de Esquerda/Direita

```
center_x = (min_x + max_x) / 2

lado == "esq" ⟺ x < center_x
lado == "dir" ⟺ x > center_x
```

### 6.3 Validação de Contato

**Função:** `_validar_candidato_contato_base()` em linha_base.py

Critérios:
- Distância euclidiana ao ponto de referência < 25 px
- Ponto está no lado correto (esq/dir)
- Y está próximo à baseline
- Não ultrapassa bordas da máscara

---

## 7. SELEÇÃO DA REGIÃO DA TANGENTE

### 7.1 Função Principal: `_selecionar_pontos_lado()`

**Arquivo:** `Cal_angulo/angulo_contato.py` linha 390  
**Entrada:** `gota_pts`, `p_esq`, `p_dir`, `baseline_y`, `lado`  
**Saída:** array de pontos selecionados

```
Etapas:

1. Cálculo da altura da gota
   y_min = np.min(gota_pts[:, 1])
   y_max = np.max(gota_pts[:, 1])
   altura = y_max - y_min
   
2. Cálculo da altura da janela
   window_height = 0.55 * altura      # fator 0.55
   window_height = clip(
       window_height,
       min=70 px,      # mínimo
       max=220 px      # máximo
   )
   
3. Ajuste da baseline para seleção
   baseline_ajustada = baseline_y - random(1.5, 4.0)
   ↑ Usa offset aleatório entre 1.5 e 4.0 pixels acima
   
4. Filtragem vertical
   mascara_y = (y > baseline_ajustada - window_height) AND (y <= baseline_ajustada)
   pts_verticais = gota_pts[mascara_y]
   
5. Separação horizontal
   center_x = (p_esq.x + p_dir.x) / 2
   
   Se lado == "esq":
       pts_lado = pts_verticais[pts_verticais[:, 0] < center_x]
   Se lado == "dir":
       pts_lado = pts_verticais[pts_verticais[:, 0] > center_x]
       
6. Retorna pts_lado (pode estar vazio se nenhum ponto satisfizer critérios)

Fórmula da Janela:
─────────────────
height = clip(0.55 * (y_max - y_min), 70, 220)

Região válida:
    baseline_ajustada - height < y ≤ baseline_ajustada
    
onde baseline_ajustada ∈ [baseline_y - 4.0, baseline_y - 1.5]
```

### 7.2 Função Secundária: `_selecionar_janela_local()`

**Linha:** 92 (em angulo_contato.py)  
**Entrada:** `contour_pts`, `p_contato`, `baseline_y`, `lado`  
**Saída:** `pontos_janela`, metadados

```
Etapas:

1. Localização do ponto de contato no contorno
   distances = distância euclidiana de cada ponto ao p_contato
   anchor_idx = índice do ponto mais próximo
   
2. Tentativa de janelas de tamanhos crescentes
   window_sizes = [7, 9, 11, 13, 15, 17]
   
   Para cada tamanho:
       a) Extração de pontos
          half = tamanho // 2
          indices = [(anchor_idx + offset) % len] para offset em [-half, +half]
          selected = contour[indices]  # circular wrapping
          
       b) Ajuste polinomial
          Se std(ys) ou std(xs) < 1e-6: pula (pontos colineares)
          coeff = np.polyfit(ys, xs, degree=2)
          x_fit = np.polyval(coeff, ys)
          
       c) Métricas de qualidade
          rmse = sqrt(mean((x_fit - x)²))
          r² = 1 - sum((x_fit - x)²) / sum((x - mean(x))²)
          cond = número de condição da matriz X
          
       d) Validação
          Se r² < 0.70: pula
          Se rmse > 3.0 px: pula
          Se cond > 1e8: pula
          
       e) Se validado, retorna essa janela
       
3. Fallback
   Se nenhuma janela validar, usa apenas o ponto anchor

Critérios de Qualidade:
──────────────────────
- R² mínimo: 0.70
- RMSE máximo: 3.0 px
- Condição máxima: 1e8
- Mínimo de pontos: 4
```

### 7.3 Função Alternativa (Desusada): `_selecionar_pontos_tangente()`

**Linha:** 195  
Similar a `_selecionar_janela_local`, mas com restrições extras:
- Máximo 45 pixels acima de baseline

**NOTA:** Esta função é chamada por `calcular_vetor_tangente()`, que é usada apenas para visualização, não para cálculo de ângulo.

### 7.4 Critérios de Continuidade

- Os índices no contorno são **cíclicos** (wrapping)
- Pontos de diferentes ramos da gota podem ser misturados se o contorno for descontínuo
- **BRECHA CRÍTICA:** O contorno pode fechar artificialmente no fundo, misturando a interface líquido-ar com o fechamento inferior

---

## 8. MÉTODO DA TANGENTE

### 8.1 Métodos Identificados no Código

| Método | Função | Onde é Usado | Status |
|--------|--------|--------------|--------|
| Círculo | `ajustar_circulo_algebrico()` | `calcular_angulo_circular()` | **Ativo (Principal)** |
| Polinômio | `_selecionar_janela_local()` + derivada | `calcular_vetor_tangente()` | Ativo (Visualização) |
| Polynomial Fallback | `_calcular_angulo_polynomial_fallback()` | Fallback de ângulo | Ativo (Backup) |

### 8.2 Método Circular (Principal)

**Função:** `ajustar_circulo_algebrico()` linha 128

```
Entrada: ndarray de pontos (Nx2)
Saída: (xc, yc, R)

Algoritmo (Método Kåsa - Ajuste Algébrico de Círculo):

1. Centralização dos dados
   xm = mean(x)
   ym = mean(y)
   u = x - xm
   v = y - ym
   
2. Construção da matriz
   Suuu = sum(u³)
   Svvv = sum(v³)
   Suu = sum(u²)
   Svv = sum(v²)
   Suv = sum(u*v)
   Suuv = sum(u²*v)
   Svuu = sum(v*u²)
   
3. Resolução do sistema linear 2×2
   [Suu  Suv] [A]   [Suuu + Svuu]
   [Suv  Svv] [B] = [Svvv + Suuv]
   
   A, B = solve(matriz, vetor)
   
4. Centro do círculo
   uc = A / 2
   vc = B / 2
   xc = xm + uc
   yc = ym + vc
   
5. Raio
   R_meio = sqrt(uc² + vc² + (Suu + Svv) / N)
   
Fórmulas:
────────
    uc = A / 2
    vc = B / 2
    
    Centro: (xc, yc) = (xm + uc, ym + vc)
    Raio: R = sqrt(uc² + vc² + (Suu + Svv) / N)
```

### 8.3 Vetor Tangente por Polinômio

**Função:** `_calcular_slope_tangente_polynomial()` linha ~220

```
Entrada: coeficientes [a, b, c] de x = a*y² + b*y + c
         ponto de contato (x_c, y_c)

Fórmula:
    dx/dy = 2*a*y_c + b
    m = 1 / (dx/dy)    ← coeficiente angular (y em relação a x)
    
Vetor tangente:
    t = (1, m) normalizado
    t_norm = t / ||t||

Significado:
- Se dx/dy > 0: interface sobe da esquerda para direita
- Se dx/dy < 0: interface desce da esquerda para direita
- m = inclinação da tangente (vertical em relação a horizontal)
```

### 8.4 Escolha do Sentido da Tangente

No código em `calcular_vetor_tangente()`:
```
Se esq/dir == "esq":
    tangente aponta para direita (x crescente)
Se esq/dir == "dir":
    tangente aponta para esquerda (x decrescente)
    
Normalmente o vetor é ajustado para apontar "para fora" da gota.
```

### 8.5 Normalização

```python
magnitude = np.sqrt(tx² + ty²)
if magnitude > 0:
    tangente_normalizado = (tx / magnitude, ty / magnitude)
else:
    tangente_normalizado = (1, 0)  # padrão horizontal
```

---

## 9. CLASSIFICAÇÃO CÍRCULO vs POLINÔMIO

### 9.1 Existe Classificação Explícita?

**NÃO.**

Não há classificação por `aspect_ratio` ou outro critério que escolha entre "use círculo" ou "use polinômio".

O fluxo é:
1. **Tenta círculo primeiro** (`calcular_angulo_circular`)
2. **Se círculo falhar**, cai para **polinômio** (`_calcular_angulo_polynomial_fallback`)

### 9.2 Condições de Fallback para Polinômio

```python
Se em calcular_angulo_circular():
    - ajustar_circulo_algebrico() lança exceção
    - raio é NaN, infinito ou negativo
    - número de inliers após remoção de outliers < 3
    - geometria degenerada
    
    Então: chamar _calcular_angulo_polynomial_fallback()
```

### 9.3 Implementação do Fallback Polinômio

**Função:** `_calcular_angulo_polynomial_fallback()` linha ~519

```
1. Seleciona pontos da mesma forma que círculo
2. Ajusta polinômio x = a*y² + b*y + c
3. Calcula tangente via derivada
4. Obtém ângulo a partir da tangente
5. Se falhar também, retorna None
```

---

## 10. CÁLCULO DO ÂNGULO

### 10.1 Função Principal: `calcular_angulo_circular()`

**Arquivo:** `Cal_angulo/angulo_contato.py` linha 444  
**Entrada:** `gota_pts`, `p_contato`, `baseline_y`, `lado`  
**Saída:** `ângulo_interno` (float em graus) ou `None`

```
Pseudocódigo:

função calcular_angulo_circular(gota_pts, p_esq, p_dir, baseline_y, lado):

    1. Selecionar pontos da região de contato
       pts_lado = _selecionar_pontos_lado(
           gota_pts, p_esq, p_dir, baseline_y, lado
       )
       
    2. Selecionar janela local polinomial
       pts_janela, metadata = _selecionar_janela_local(
           gota_pts, p_contato, baseline_y, lado
       )
       
    3. Ajustar círculo nos pontos da janela
       xc, yc, R = ajustar_circulo_algebrico(pts_janela)
       
       Se falhar ou R inválido:
           ↓ fallback para polinômio
           return _calcular_angulo_polynomial_fallback(...)
       
    4. Remoção de outliers
       residuos = ||ponto - centro||² - R²
       sigma_residuos = std(residuos)
       inliers = |residuo| < 2.0 * sigma_residuos
       
       Se inliers < 3:
           return None ou fallback
       
    5. Refazer ajuste circular com inliers
       xc_refino, yc_refino, R_refino = ajustar_circulo_algebrico(inliers)
       
    6. Selecionar ponto de contato robusto
       if lado == "esq":
           p_contato_robusto = ponto em inliers com x mínimo
       if lado == "dir":
           p_contato_robusto = ponto em inliers com x máximo
           
    7. Calcular vetor raio
       vetor_raio = (p_contato_robusto.x - xc_refino,
                     p_contato_robusto.y - yc_refino)
       
    8. Vetor tangente (perpendicular ao raio)
       vetor_tangente = (-vetor_raio.y, vetor_raio.x)
       vetor_tangente_norm = vetor_tangente / ||vetor_tangente||
       
    9. Vetor baseline
       vetor_baseline = (1, 0)  ← horizontal
       
    10. Ângulo interno (entre tangente e baseline)
        cos(θ) = dot(vetor_tangente, vetor_baseline) / (||t|| * ||b||)
        θ = arccos(cos_theta)  ← em radianos
        θ_graus = θ * 180 / π
        
        Se θ > 90°: θ_graus = 180° - θ_graus  ← complemento
        
    11. Validar e retornar
        if 0 <= θ_graus <= 180:
            return θ_graus
        else:
            return None
```

### 10.2 Fórmulas Matemáticas Reais

```
=== CÍRCULO ===

Centro: (xc, yc)
Raio: R = sqrt((x_contato - xc)² + (y_contato - yc)²)

=== VETOR RAIO ===

v_raio = (x_contato - xc, y_contato - yc)

=== VETOR TANGENTE (perpendicular ao raio) ===

v_tangente = (-v_raio.y, v_raio.x)
                ou
v_tangente = (v_raio.y, -v_raio.x)  ← dependendo da orientação

v_tangente_norm = v_tangente / ||v_tangente||

=== VETOR BASELINE ===

v_baseline = (1, 0)  ← horizontal para direita

=== ÂNGULO INTERNO (entre tangente e baseline) ===

cos(θ) = dot(v_tangente, v_baseline) / (||v_tangente|| * ||v_baseline||)
       = dot(v_tangente_norm, v_baseline)  ← se v_tangente já normalizado

θ = arccos(cos(θ))  ← radianos, [0, π]
θ_graus = θ * 180 / π  ← graus

=== AJUSTE DE COMPLEMENTO ===

Se θ > 90°:
    θ_graus = 180 - θ_graus
    
Resultado final: θ ∈ [0°, 180°]
```

### 10.3 Tratamento de Sinais e Limitações

| Caso | Saída |
|------|-------|
| cos(θ) > 1 (numérico) | clip para 1, θ = 0° |
| cos(θ) < -1 (numérico) | clip para -1, θ = 180° |
| NaN em residuos | fallback ou None |
| Raio negativo ou zero | fallback ou None |
| Poucos inliers | None |

---

## 11. DOMÍNIO FÍSICO DO ÂNGULO

### 11.1 Valores Permitidos Atualmente no Código

Verificação no código de `calcular_angulo_circular()`:

```python
if not (0 <= theta_degrees <= 180):
    # retorna None ou fallback
```

### 11.2 Domínio Observado

| Valor | Permitido? | Contexto |
|-------|-----------|----------|
| Negativo (-45°) | ❌ Não (retorna None) | Indica erro geométrico |
| 0° | ✅ Sim | Tangente horizontal para direita |
| 0° < θ < 180° | ✅ Sim | Intervalo normal |
| 180° | ✅ Sim | Tangente horizontal para esquerda |
| > 180° (ex: 225°) | ❌ Não (clip ou None) | Não suportado |
| NaN | ❌ Não (fallback) | Erro numérico |
| infinito | ❌ Não (fallback) | Geometria degenerada |

### 11.3 Limitações Observadas

- Ângulos obtuso (> 90°) são **complementados** para ângulos agudos (< 90°)
- Isso significa que um contato muito aberto (ex: 150°) seria reportado como 30°
- **POTENCIAL BRECHA:** Perda de informação sobre hidrofobicidade

---

## 12. VISUALIZAÇÃO

### 12.1 Componentes Desenhados

**Função Principal:** `ContactAngleApp._render_internal()` em main.py linha ~1206

```
Sequência de desenho:

1. Imagem base (canva limpo com imagem original)
   canvas.create_image(...)
   
2. Contorno da gota (ciano)
   desenhar_contorno(canvas, gota_pts)
   └─ cv2 circle para cada ponto do contorno
      cor: (0, 255, 255) ciano
      raio: 1-2 pixels
      
3. Baseline (vermelho + inclinação)
   desenhar_baseline(canvas, baseline_y, line_params)
   └─ linha horizontal em y = baseline_y
      cor: (0, 0, 255) vermelho
      Se line_params disponível:
          desenha reta inclinada usando (vx, vy)
      Else:
          linha horizontal
      
4. Pontos de contato (amarelo com borda)
   desenhar_pontos_contato(canvas, p_esq, p_dir)
   └─ Dois círculos
      cor interior: (0, 255, 255) amarelo
      cor borda: (0, 0, 0) preto
      raio: ~5-8 pixels
      
5. Texto de ângulos (branco)
   canvas.create_text(...)
   ├─ "ângulo_esquerda: XX.XX°"
   ├─ "ângulo_direita: YY.YY°"
   └─ "média: ZZ.ZZ°"
```

### 12.2 Diferenças Entre Visualização e Cálculo

| Aspecto | Visualização | Cálculo |
|---------|--------------|---------|
| Contorno | Desenhado completo (pode incluir fechamento) | Usado com pontos selecionados |
| Baseline | Horizontal vermelho | Pode ter inclinação (vx, vy) |
| Tangente | **NÃO é desenhada** (função existe mas não chamada) | Calculada internamente |
| Pontos de contato | Fixos na posição do usuário | Podem ser ajustados/projetados |

**OBSERVAÇÃO CRÍTICA:** Tangentes **não são visualizadas** apesar da função `desenhar_tangentes()` existir.

---

## 13. DEPENDÊNCIAS ENTRE ETAPAS

### Mapa de Fluxo de Dados

```
Imagem BGR (Câmera ou arquivo)
    ↓
   ROI selecionada pelo usuário
    ↓
filtros.aplicar_multi_threshold()
    ├─ Grayscale
    ├─ Gaussian blur
    ├─ Threshold OTSU/Adaptativo/Canny
    ├─ Pontuação
    └─→ máscara binária (bin_img)
    
bin_img
    ├─→ contorno.encontrar_contorno_gota_robusto()
    │   ├─ cv2.findContours(RETR_EXTERNAL, CHAIN_APPROX_NONE)
    │   └─→ gota_pts (Nx2, float32)
    │
    ├─→ linha_base.detectar_baseline_hibrida()
    │   ├─ cv2.fitLine + MAD outlier removal
    │   ├─ quantil 90%
    │   └─→ baseline_y, line_params (vx, vy), p_esq, p_dir
    │
    └─→ contorno.projetar_ponto_no_contorno()
        ├─ entrada: p_esq, p_dir (candidatos)
        └─→ p_esq, p_dir (ajustados)

gota_pts + baseline_y + p_esq + p_dir
    ↓
angulo_contato.calcular_angulo_circular()
    ├─ _selecionar_pontos_lado(gota_pts, ...)
    ├─ _selecionar_janela_local(gota_pts, p_contato, ...)
    ├─ ajustar_circulo_algebrico(pts_janela)
    │   └─→ xc, yc, R
    ├─ Remoção de outliers
    ├─ Cálculo do vetor tangente
    └─→ θ_esq, θ_dir (graus)

visualizacao.desenho
    ├─ desenhar_baseline(..., baseline_y, line_params)
    ├─ desenhar_contorno(..., gota_pts)
    └─ desenhar_pontos_contato(..., p_esq, p_dir)
    
θ_esq, θ_dir
    ├─ Canvas.create_text(..., f"esq: {θ_esq}°")
    ├─ Canvas.create_text(..., f"dir: {θ_dir}°")
    └─ Canvas.create_text(..., f"média: {(θ_esq + θ_dir) / 2}°")
```

### Significado Geométrico de Cada Dado

| Variável | Tipo | Significado | Geométrico |
|----------|------|------------|-----------|
| `bin_img` | ndarray uint8 | Máscara binária | Pixels brancos = gota, pretos = fundo |
| `gota_pts` | ndarray float32 Nx2 | Contorno | **FECHADO**, pode incluir substrato |
| `baseline_y` | float | Altura da baseline | Interfase esperada gota-ar |
| `line_params` | tuple (vx, vy, x0, y0) | Inclinação da baseline | Direção da reta ajustada |
| `p_esq` | tuple (x, y) | Contato esquerdo | Ponto onde gota toca a baseline |
| `p_dir` | tuple (x, y) | Contato direito | Ponto onde gota toca a baseline |
| `xc, yc, R` | float, float, float | Círculo local | Centro e raio do círculo ajustado |
| `θ` | float [0, 180] | Ângulo interno | Entre tangente e baseline (horizontal) |

---

## 14. FÓRMULAS REALMENTE UTILIZADAS NO CÓDIGO ATUAL

### 14.1 Baseline

```
Y_base = quantil(90%, Y_inliers)

onde inliers vêm de:
    1. cv2.fitLine(pts, cv2.DIST_L1, ...) → (vx, vy, x0, y0)
    2. Distância perpendicular: d = |vx*(y-y0) - vy*(x-x0)| / sqrt(vx² + vy²)
    3. Escala robusta MAD: σ = 1.4826 * mediana(|d|)
    4. Threshold: threshold = σ * z_score (padrão 2.5)
    5. Inliers: |d| < threshold
    6. Refinamento (2 iterações)
    
Y_base NÃO é Y_max. É quantil dos inliers da região inferior.
```

### 14.2 Extrapolação de Contato

```
x(y) = a*y² + b*y + c

Onde:
    (a, b, c) = np.polyfit(Y_pontos_roi, X_pontos_roi, degree=2)
    Y_pontos_roi: pontos na faixa Y ∈ [Y_min + 0.20*(Y_max-Y_min), Y_min + 0.92*(Y_max-Y_min)]
    
Contato extrapolado:
    x_esq = a*Y_base² + b*Y_base + c   (lado esquerdo)
    x_dir = a*Y_base² + b*Y_base + c   (lado direito)
    
p_esq = (x_esq, Y_base)
p_dir = (x_dir, Y_base)
```

### 14.3 Círculo (Método Kåsa)

```
Centralizar: u = x - mean(x), v = y - mean(y)

Resolver sistema:
    [Σu²    Σuv] [A]   [Σu³ + Σuv²]
    [Σuv    Σv²] [B] = [Σv³ + Σu²v]

Parâmetros:
    u_c = A / 2
    v_c = B / 2
    
Centro:
    x_c = mean(x) + u_c
    y_c = mean(y) + v_c
    
Raio:
    R = sqrt(u_c² + v_c² + (Σu² + Σv²) / n)
```

### 14.4 Derivada (Tangente por Polinômio)

```
Se x = a*y² + b*y + c, então:

    dx/dy = 2*a*y + b
    
Inclinação vertical (y em função de x):
    dy/dx = 1 / (dx/dy) = 1 / (2*a*y + b)
    
No ponto de contato:
    m = 1 / (2*a*y_contato + b)
    
Vetor tangente normalizado:
    t = (1, m) / sqrt(1 + m²)
    ou
    t = (dx/dy, 1) / sqrt((dx/dy)² + 1)
```

### 14.5 Ângulo (Entre Tangente e Baseline)

```
Vetor tangente normalizado: t_norm = (tx, ty)
Vetor baseline: b = (1, 0)

Cosseno do ângulo:
    cos(θ) = t_norm · b = tx

Ângulo em radianos:
    θ = arccos(tx)  ← radianos, [0, π]
    
Conversão para graus:
    θ_graus = θ * 180 / π
    
Complemento (se necessário):
    Se θ_graus > 90°:
        θ_graus = 180° - θ_graus
        
Resultado: θ ∈ [0°, 180°]
```

### 14.6 Qualidade Dinâmica

```
Ajuste círculo esquerdo: xc_esq, yc_esq, R_esq
Ajuste círculo direito: xc_dir, yc_dir, R_dir

Para cada lado:
    residuos = ||ponto - centro||² - R²
    rmse_lado = sqrt(mean(residuos²))
    
RMSE médio:
    rmse_medio = (rmse_esq + rmse_dir) / 2
    
Score:
    score = exp(-rmse_medio / quality_rmse_ref_px)
    
    onde quality_rmse_ref_px = 3.0 (configurável)
    
Score normalizado:
    score_clip = clip(score, 0.0, 1.0)
```

---

## 15. DIFERENÇAS: DOCUMENTAÇÃO ANTIGA vs CÓDIGO ATUAL

### Tabela Comparativa

| Item | Documentação Antiga | Código Atual | Igual? | Observações |
|------|--------------------| ------------|--------|------------|
| **Baseline** | Y_max do contorno | Quantil 90% dos inliers robustos | ❌ NÃO | Mudança significativa |
| **Fração inferior** | config.json: baseline_bottom_fraction | Hardcoded: 0.30 | ❌ NÃO | Config não respeitado |
| **Polinômio contato** | Grau mencionado | Grau 2 (quadrático) | ✅ ~SIM | Corresponde |
| **Variáveis polinômio** | (x=f(y)) ou (y=f(x)) | x = f(y) → X em função de Y | ✅ SIM | Correto |
| **Círculo** | Método não especificado | Método Kåsa (algébrico) | ✅ Confirmado | Implementado |
| **Tangente** | Derivada do polinômio | Derivada correta: dx/dy | ✅ SIM | Correspondência |
| **Ângulo interno** | Entre tangente e baseline | arccos(dot product) | ✅ SIM | Fórmula correta |
| **Domínio de ângulo** | Não especificado | [0°, 180°] | ✅ Explícito | Implementado |
| **Método de seleção** | Não clara | Window local polinomial | ⚠️ NOVO | Não era explícito |
| **Janela de altura** | Mencionado como "ajustável" | 0.55 * altura com limites [70, 220] | ✅ Específico | Valores hardcoded |
| **Filtros de imagem** | Multi-threshold genérico | OTSU/ADAPTIVE/CANNY com scoring | ✅ Correspondência | Implementação mais detalhada |
| **Contorno** | Considerado "aberto" (interface) | Realmente **FECHADO** (inclui substrato) | ❌ DIVERGÊNCIA | **CRÍTICO** |

---

## 16. BRECHAS E LACUNAS IDENTIFICADAS

### 16.1 Lacunas Críticas

#### L1: Contorno Fechado em Lugar do Aberto

**Evidência:**
```python
# contorno.py, linha 312
contours, hierarchy = cv2.findContours(
    processed,
    cv2.RETR_EXTERNAL,           # extrai contorno externo
    cv2.CHAIN_APPROX_NONE       # mantém todos os pontos
)
```

**Significado:**
- `cv2.findContours()` retorna contornos FECHADOS
- Máscara binária com fechamento morfológico pode incluir o substrate
- Resultado: contorno contém pontos da interface **líquido-ar** + **fechamento artificial no fundo**

**Impacto:**
- Seleção de pontos de tangente pode incluir pontos do substrate
- Ângulo calculado pode estar deslocado

#### L2: Baseline Não Respeita config.json

**Evidência:**
```python
# linha_base.py, linha 362
def detectar_baseline_hibrida(...):
    return detect_baseline_tls(gota_pts, bottom_fraction=0.30)  # hardcoded!
    # config.json diz: baseline_bottom_fraction = 0.1
```

**Impacto:**
- Parâmetro de configuração não é usado
- Impossível ajustar este comportamento sem código

#### L3: Deslocamento Aleatório da Baseline em _selecionar_pontos_lado()

**Evidência:**
```python
# angulo_contato.py, linha ~405
baseline_ajustada = baseline_y - random(1.5, 4.0)
```

**Problema:**
- A janela de seleção usa baseline DESLOCADA para cima
- Cada chamada pode produzir resultado diferente
- Não é determinístico

**Questão:**
- Por que deslocar? Qual é a justificativa física?

#### L4: Tangentes Não são Desenhadas

**Evidência:**
```python
# desenho.py, linha 79-100
def desenhar_tangentes(...):
    # função existe mas nunca é chamada em _render_internal()
```

**Impacto:**
- Usuário não consegue verificar visualmente se tangente está correta
- Feedback visual insuficiente

#### L5: Dois Métodos de Seleção de Pontos

**Evidência:**
```python
# angulo_contato.py
_selecionar_pontos_lado()        # → seleção vertical + horizontal
_selecionar_janela_local()       # → seleção por janela polinomial + wrapping

# Qual é realmente usado?
# AMBOS: _selecionar_pontos_lado() → seleciona região geral
#        _selecionar_janela_local() → seleciona pontos específicos
```

**Risco:**
- Redundância de lógica
- Possibilidade de pontos mistos ou perdidos

#### L6: Fallback Polinômio Nunca Testado Ativamente

**Evidência:**
```python
# angulo_contato.py, linha ~495
def _calcular_angulo_polynomial_fallback(...):
    # função existe mas é chamada apenas se círculo falhar
    # qual é o comportamento esperado?
```

**Questão:**
- Qual é a qualidade do fallback?
- Quando o círculo falha e polinômio é usado?

---

### 16.2 Possíveis Desalinhamentos

#### D1: Rotação Cíclica de Índices

**Em _selecionar_janela_local():**
```python
indices = [(anchor_idx + offset) % len(contour) for offset in range(-half, half+1)]
```

**Risco:**
- Se o contorno fechar artificialmente, índices cíclicos podem cruzar o "fechamento"
- Pontos selecionados podem vir de lados opostos da gota

#### D2: Window Height Aleatória

**Em _selecionar_pontos_lado():**
```python
baseline_ajustada = baseline_y - random(1.5, 4.0)
```

**Risco:**
- Não reproduzível
- Cada execução pode dar ângulo ligeiramente diferente

#### D3: Conversão de Coordenadas Canvas ↔ Imagem

**Em main.py:**
```python
# SelectionWindow.start_roi(), draw_roi(), end_roi()
# Há conversão de pixels canvas para pixels imagem?
# Há inversão de eixo Y?
```

**Risco:**
- Se conversão estiver errada, ROI selecionada pode estar deslocada

---

### 16.3 Inconsistências de Configuração

| Parâmetro | Fonte | Valor | Status |
|-----------|-------|-------|--------|
| baseline_bottom_fraction | config.json | 0.1 | Ignorado |
| ANGLE_WINDOW_HEIGHT_FACTOR | config.json → parametros.py | 0.55 | Usado |
| ANGLE_BASELINE_OFFSET_MIN | config.json → parametros.py | 1.5 | Usado |
| ANGLE_BASELINE_OFFSET_MAX | config.json → parametros.py | 4.0 | Usado |
| bottom_fraction em detect_baseline_tls() | hardcoded | 0.30 | Não via config |

---

## 17. QUESTÕES QUE PRECISAMOS RESPONDER

### Perguntas Técnicas (Não Soluções)

1. **Contorno Líquido-Ar?**
   - O contorno retornado por `cv2.findContours()` representa **apenas** a interface líquido-ar?
   - Ou inclui o fechamento artificial no substrate?
   - Como verificar?

2. **Fechamento Inferior?**
   - O fechamento inferior do contorno (onde a máscara conecta gota ao fundo) participa do cálculo de ângulo?
   - Se sim, distorce o resultado?
   - Existe código que o remove?

3. **Ponto de Contato Real?**
   - O ponto de contato (p_esq, p_dir) **coincide** com a intersecção física da gota com a baseline?
   - Ou é uma extrapolação polinomial que pode estar deslocada?
   - Qual erro esperado?

4. **Seleção de Tangente Robusta?**
   - A seleção da tangente começa **exatamente** no ponto de contato?
   - Ou usa uma janela deslocada que pode perder o ponto de contato?
   - Qual é a justificativa do deslocamento aleatório (1.5-4.0 px)?

5. **Ramo Físico?**
   - A tangente é calculada sobre o **mesmo ramo** da gota?
   - Se o contorno fechar artificialmente, indices cíclicos podem pular para o outro lado?
   - Como garantir continuidade?

6. **Simetria Esquerda-Direita?**
   - O cálculo atual usa o **mesmo método** nos dois lados?
   - Ou há caminho diferente para esquerda vs direita?
   - Existe fallback diferenciado?

7. **Robustez do Círculo?**
   - Qual é a taxa de sucesso do ajuste circular?
   - Quando falha, qual é a qualidade do fallback polinômio?
   - Como medir isso sem executar testes?

8. **Baseline Inclinada?**
   - A baseline calculada é **sempre horizontal**?
   - Ou pode ter inclinação (vx, vy)?
   - Se inclinada, como afeta o ângulo calculado?
   - A visualização mostra a inclinação corretamente?

9. **Offset Aleatório em Baseline?**
   - Por que existe deslocamento aleatório de 1.5-4.0 pixels em `_selecionar_pontos_lado()`?
   - É intencional para robustez ou bug?
   - Afeta a reproduzibilidade?

10. **Quantil 90% em Baseline?**
    - Por que quantil 90% dos inliers, e não 100% (máximo dos inliers)?
    - Qual é a justificativa estatística?
    - Qual erro é introduzido?

11. **Grau do Polinômio Contato?**
    - Por que grau 2 (quadrático) para extrapolação de contato?
    - Graus 1 ou 3 seriam melhores?
    - Existe validação de grau óptimo?

12. **Métrica de Qualidade?**
    - O score `exp(-rmse / 3.0)` é apropriado para esta aplicação?
    - Qual é a distribuição esperada de rmse?
    - Como calibrar o parâmetro `quality_rmse_ref_px = 3.0`?

---

## RESUMO EXECUTIVO

### Arquivos de Produção Analisados
✅ main.py (1143 linhas)
✅ processamento_imagem/filtros.py (147 linhas)
✅ processamento_imagem/preprocess.py (130 linhas) [inativo]
✅ processamento_imagem/contorno.py (635 linhas)
✅ linha_base/linha_base.py (450 linhas)
✅ Cal_angulo/angulo_contato.py (525 linhas)
✅ visualizacao/desenho.py (143 linhas)

### Documento Gerado
✅ **AUDITORIA_ESTRUTURA_FORMULAS_VERSAO_ATUAL.md** (este arquivo)

### Principais Lacunas Identificadas

1. **Contorno é fechado**, pode incluir substrate
2. **Baseline não respeita config.json**
3. **Offset aleatório** em seleção de pontos
4. **Tangentes não visualizadas**
5. **Redundância** em métodos de seleção
6. **Incompatibilidade** entre config.json e código hardcoded

### Principais Diferenças vs Documentação Antiga

| Aspecto | Mudança |
|---------|---------|
| Baseline | Y_max → quantil 90% inliers robustos |
| Contorno | Documentado como "aberto" → realmente FECHADO |
| Configurações | Parcialmente ignoradas (config.json não respeitado) |
| Seleção de pontos | Método não documentado antes |
| Tangentes | Desenhadas em novo código, mas visualização desativada |

### Próximos Passos Recomendados (Para Futura Investigação)

1. Verificar se contorno inferior deve ser removido
2. Respeitar config.json em `detectar_baseline_hibrida()`
3. Remover aleatoriedade em `_selecionar_pontos_lado()`
4. Ativar visualização de tangentes
5. Documentar justificativa para offset aleatório se intencional
6. Validar grau polinomial de contato
7. Testar taxa de sucesso de ajuste circular vs fallback polinômio

---

**FIM DA AUDITORIA**
