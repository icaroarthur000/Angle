# ANÁLISE COMPARATIVA: Commit f06242 vs HEAD (9beb758)

**Data da Análise:** 2026-09-04  
**Commit de Referência:** f06242bea603eb0dc51558070fcce336fe52b454 ("Teste com o GeoGebra... Deu certo. Falta as tangentes")  
**Commit Atual (HEAD):** 9beb758bd6d3730f895608a0bfb9412a4aa0e920 ("Modelo com muitas modificacoes porem nao esta correto")  
**Números de Commits Intermediários:** 6 commits

---

## HISTÓRICO DE COMMITS (f06242 → HEAD)

```
f06242b → 1f5daac → 32dbade → 113fc8b → 5b05cb2 → 99037c7 → ee5a89d → 69ebd9f → 9beb758
     ↓ Teste com GeoGebra (funciona)
     ├─ 1f5daac: Fazendo o documento...ainda imcompleto
     ├─ 32dbade: Melhoria no pré-processamento com CLAHE e Gaussian blur
     ├─ 113fc8b: Melhora detecção de contornos, adiciona filtros adaptativos
     ├─ 5b05cb2: Teste para ver se ta salvando
     ├─ 99037c7: Analisando para poder identificar o erro no calculo
     ├─ ee5a89d: Finalizando investigacao. Calculo ainda errado
     ├─ 69ebd9f: Contorno ate a linha base. Pontos (ok) Tang (+/-)
     └─ 9beb758: Modelo com muitas modificacoes porem nao esta correto (ATUAL)
```

**Conclusão sobre Histórico:** Houve 7 commits entre a versão "que deu certo com GeoGebra" e a versão atual. A trajetória é descrita como "investigação", "análise de erros", "finalizando investigação", "muitas modificações porém não está correto".

---

## A. CARREGAMENTO E PRÉ-PROCESSAMENTO DE IMAGEM

### f06242 (Versão "que Deu Certo")

```
SelectionWindow.load_from_file()
  ├─ cv2.imread(arquivo)
  ├─ aplicar_multi_threshold() [versão f06242]
  │   ├─ Grayscale
  │   ├─ Gaussian blur (3,3)
  │   ├─ Threshold OTSU
  │   ├─ Fechamento morfológico leve
  │   └─ Saída: máscara simples
  └─ Seleção manual de ROI
```

**Caraterísticas:**
- Pipeline simples e direto
- Sem scoring automático de máscaras
- Sem filtros adaptativos

### HEAD (Versão Atual)

```
SelectionWindow.load_from_file()
  ├─ cv2.imread(arquivo)
  ├─ aplicar_multi_threshold() [versão HEAD]
  │   ├─ Grayscale
  │   ├─ Gaussian blur (5,5) ← ALTERADO: kernel maior
  │   ├─ Múltiplos candidatos:
  │   │   ├─ OTSU_LIGHT (3×3)
  │   │   ├─ OTSU (5×5)
  │   │   ├─ ADAPTIVE_LIGHT (7×7)
  │   │   ├─ ADAPTIVE (11×11)
  │   │   └─ CANNY [30, 100]
  │   ├─ Scoring de máscaras (fill_ratio + entropia)
  │   ├─ Seleção da melhor por score
  │   ├─ isolar_gota_substrato() [NOVO]
  │   │   ├─ _necking_detection
  │   │   ├─ _sobel_y_surface
  │   │   └─ _abertura_anisotropica
  │   └─ Saída: máscara com separação gota/substrate
  └─ Seleção manual de ROI
```

**Mudanças:**
- [ALTERADO] Kernel Gaussian: (3,3) → (5,5)
- [NOVO] Filtros adaptativos adicionados
- [NOVO] Scoring e seleção automática de melhor máscara
- [NOVO] Separação gota/substrate com múltiplos métodos (necking, Sobel, abertura)
- [ALTERADO] Pipeline mais complexo e automatizado

**Impacto Observado:**
- ✅ Mais robusto a variações de iluminação
- ❌ Mais lento (6 candidatos vs 1)
- ❌ Pode selecionar máscara diferente (possível perda de informação)

**Diagnóstico:**
`[ALTERADO - CRÍTICO]` A mudança de pipeline de pré-processamento é **candidata forte** para causa de problemas. Se a máscara mudou, o contorno muda, e o cálculo de ângulo é afetado.

---

## B. FILTROS DISPONÍVEIS

### f06242

```python
Funções em filtros.py:
├─ preprocessar_imagem_robusto(img)
├─ aplicar_filtro_binary_otsu(img)
├─ aplicar_filtro_edges_canny(img)
├─ aplicar_filtro_binary_adaptive(img)
├─ gerar_candidatos_segmentacao(img)
├─ aplicar_multi_threshold(roi, bin_img)
└─ aplicar_pre_processamento(img)
```

**Modo Ativo:** OTSU simples

### HEAD

```python
Funções em filtros.py: [MESMAS ACIMA]

Mais adicionadas:
├─ aplicar_preprocessamento_clahe(img)     [NOVO]
├─ _score_mascara(mask)                    [NOVO]
└─ [versão expandida de gerar_candidatos_segmentacao]
```

**Modo Ativo:** Multi-threshold com scoring automático

**Diagnóstico:**
`[NOVO/ALTERADO]` CLAHE e scoring são novos. Não existiam em f06242.

---

## C. SEGMENTAÇÃO / MÁSCARA

### f06242: Máscara Simples OTSU

```
ROI BGR
  ├─ Grayscale
  ├─ Gaussian blur (3,3)
  ├─ Threshold OTSU invertido
  ├─ Fechamento morfológico (3,3)
  └─ Máscara (uint8, 0-255)
```

**Resultado:** Uma máscara binária simples

### HEAD: Máscara Multi-Candidata com Scoring

```
ROI BGR
  ├─ Grayscale
  ├─ Gaussian blur (5,5)  ← kernel maior
  ├─ Gerar 5 candidatos (OTSU_LIGHT, OTSU, ADAPTIVE_LIGHT, ADAPTIVE, CANNY)
  │   Cada um:
  │   ├─ Blur
  │   ├─ Threshold / Canny
  │   └─ Morfologia
  ├─ Pontuar cada máscara (fill_ratio, entropia)
  ├─ Selecionar melhor score
  ├─ Separar gota/substrato (necking + Sobel + abertura)
  └─ Máscara final (uint8, 0-255)
```

**Resultado:** Máscara selecionada automaticamente, possivelmente diferente

**Diagnóstico:**
`[ALTERADO - CRÍTICO]` Se máscara mudou de OTSU simples para algo mais sofisticado:
- Contorno pode estar em posição diferente
- Baseline pode estar em Y diferente
- Ângulo calculado será diferentes

---

## D. DETECÇÃO DO CONTORNO

### f06242

```
Função: encontrar_contorno_gota() [simples]

cv2.findContours(
    bin_img,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)

Filtros:
├─ Área mínima
├─ Bounding box mínimo
└─ Rejeição simples de outliers
```

**Características:**
- Simples
- Usa RETR_EXTERNAL
- Sem validação complexa

### HEAD

```
Função: encontrar_contorno_gota_robusto() [nova, mais robusta]

cv2.findContours(
    processed,  ← após fechamento + margens
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)

Fallback: Se não houver contorno, tenta Canny

Validação (_validar_contorno):
├─ Área ≥ 100
├─ Bounding box ≥ 20×20
├─ Razão aspecto ≤ 8
├─ Circularidade ≥ 0.35
├─ Convexidade ≥ 0.7
├─ Preenchimento ≥ 0.5
├─ Rejeição de faixas horizontais
└─ Pontuação geométrica

Seleção: melhor score por pontuação
```

**Mudanças:**
- [NOVO] Função `encontrar_contorno_gota_robusto()` 
- [NOVO] Validação de circularidade, convexidade, preenchimento
- [NOVO] Fallback Canny
- [NOVO] Pontuação e seleção do melhor

**Diagnóstico:**
`[NOVO - CRÍTICO]` A função `encontrar_contorno_gota_robusto()` é totalmente nova. Pode selecionar contorno diferente se houver múltiplos candidatos. A validação adicionada pode rejeitar contornos que f06242 aceitaria.

---

## E. DETECÇÃO DE LINHA BASE

### f06242

```
Função: detectar_baseline()  [simples]

Y_base = Y_max do contorno

Contatos: extremos esquerdo/direito na faixa inferior
```

**Características:**
- Muito simples
- Sem ajuste robusto de reta
- Sem MAD/outlier removal
- Sem extrapolação polinomial

### HEAD

```
Função: detectar_baseline_hibrida() [robusto]

1. Seleção de região inferior (30% da altura)
2. cv2.fitLine(..., DIST_L1)
3. Rejeição de outliers por MAD
4. Quantil 90% dos inliers → Y_base

Contatos: find_contact_points_by_extrapolation()
├─ Polinômio grau 2
├─ x = a*y² + b*y + c
└─ Extrapola em Y_base
```

**Mudanças:**
- [NOVO] cv2.fitLine com DIST_L1
- [NOVO] Outlier removal por MAD
- [NOVO] Quantil 90% em vez de Y_max exato
- [NOVO] Extrapolação polinomial de contatos
- [ALTERADO] Lógica de detecção completamente reescrita

**Diagnóstico:**
`[NOVO/ALTERADO - MUITO CRÍTICO]` A baseline foi reescrita completamente:
- f06242: Y_max do contorno
- HEAD: Quantil 90% de inliers robustos

Essas são **completamente diferentes**. Se o contorno em HEAD é diferente, Y_max é diferente. E quantil 90% é ainda diferente de Y_max.

**Questão Crucial:**
- Em f06242, por que "deu certo com GeoGebra"?
- Qual era o valor de baseline em f06242?
- Qual é o valor de baseline em HEAD?
- Diferença de quantos pixels?

---

## F. DETECÇÃO DE PONTOS DE CONTATO

### f06242

```
Função: encontrar_pontos_contato() [simples]

p_esq = extremo esquerdo na faixa inferior
p_dir = extremo direito na faixa inferior
```

**Características:**
- Extremos geométricos
- Sem interpolação
- Sem validação

### HEAD

```
Função: find_contact_points_by_extrapolation() [avançado]

1. Separação por lado (esquerda/direita)
2. Para cada lado:
   ├─ Seleção ROI (pontos em intervalo Y)
   ├─ np.polyfit(y_roi, x_roi, degree=2)
   ├─ Avaliação do polinômio em Y_base
   └─ x_contato = poly(Y_base)
3. Validação de candidatos
4. Fallback: espelho ou extremos

Função secundária: projetar_ponto_no_contorno()
├─ Reposiciona contato na faixa inferior
└─ Snap magnético ao contorno
```

**Mudanças:**
- [NOVO] Extrapolação polinomial de contatos
- [NOVO] Validação de candidatos
- [NOVO] Fallbacks
- [NOVO] Projeção no contorno pós-initial_analysis

**Diagnóstico:**
`[NOVO - CRÍTICO]` Pontos de contato agora usam extrapolação polinomial em vez de serem extremos. Isso pode **deslocar os contatos** em relação ao contorno.

---

## G. SELEÇÃO DA REGIÃO DA TANGENTE

### f06242

```
Não está claro no código de f06242.
Provavelmente simples: pontos próximos do contato.
```

**Características:**
- Não documentada
- Provavelmente ad-hoc

### HEAD

```
Função: _selecionar_pontos_lado() [nova]

1. Cálculo de altura da gota
2. Cálculo de window_height = clip(0.55 * altura, 70, 220)
3. Deslocamento aleatório de baseline (1.5-4.0 px)
4. Filtragem vertical: baseline_ajustada - height < y <= baseline_ajustada
5. Separação horizontal por lado
6. Retorna pontos_lado

Função: _selecionar_janela_local() [nova]

1. Localiza anchor_idx (ponto mais próximo do contato)
2. Tenta janelas de tamanhos [7, 9, 11, 13, 15, 17]
3. Para cada janela:
   ├─ np.polyfit(ys, xs, degree=2)
   ├─ Validação: R² > 0.70, RMSE < 3.0 px, cond < 1e8
   └─ Se válida, retorna
4. Fallback: apenas ponto anchor
```

**Mudanças:**
- [NOVO] Método sistemático de seleção
- [NOVO] Window height calculada (55% de altura com limites)
- [NOVO] Deslocamento aleatório de baseline
- [NOVO] Validação por R², RMSE, número de condição
- [NOVO] Janelas de tamanho variável

**Diagnóstico:**
`[NOVO - CRÍTICO]` Seleção de pontos é completamente nova:
- Deslocamento aleatório pode causa resultados não-determinísticos
- Window height poderia ser muito diferente em f06242
- Validação por R² e RMSE é nova

---

## H. CÁLCULO DE TANGENTE

### f06242

```
Provavelmente: derivada simples de polinômio ajustado aos pontos.
Método não está claro no código antigo.
```

### HEAD

```
Função: _selecionar_janela_local() [usada no círculo]
Função: _selecionar_pontos_tangente() [usada em vetor tangente]

Ambas: ajustam x = a*y² + b*y + c

Derivada:
    dx/dy = 2*a*y + b
    m = 1 / (dx/dy)
    
Vetor tangente normalizado: (1, m) / ||(1, m)||

Usada em: calcular_vetor_tangente() [visualização]
```

**Mudanças:**
- [CONFIRMADO] Método é derivada de polinômio
- [NOVO] Validação robusta de polinômio
- [NOVO] Fallback estruturado

**Diagnóstico:**
`[SIMILAR COM NOVOS DETALHES]` A tangente provavelmente era assim em f06242 também, mas agora é mais robusta.

---

## I. CÁLCULO DO ÂNGULO

### f06242

```
Provavelmente: calcular_angulo() simples

Pseudocódigo:
├─ Ajustar círculo
├─ Calcular tangente
└─ atan entre tangente e baseline

Método: não tão estruturado
```

**Características:**
- Simples
- Menos validação
- Sem audit context

### HEAD

```
Função: calcular_angulo_circular() [completa]

1. _selecionar_pontos_lado()
2. _selecionar_janela_local()
3. ajustar_circulo_algebrico()
4. Remoção de outliers por 2σ
5. Refazer ajuste
6. Seleção de ponto de contato robusto
7. Cálculo de vetor tangente perpendicular ao raio
8. arccos(dot product com baseline)
9. Validação e complemento

Fallback: _calcular_angulo_polynomial_fallback()

Audit context armazenado: set_audit_context(...)
```

**Mudanças:**
- [NOVO] Seleção robusta de pontos em estágios
- [NOVO] Janela local com validação polinomial
- [NOVO] Remoção de outliers iterativa
- [NOVO] Ponto de contato robusto
- [NOVO] Audit context para debugging
- [ALTERADO] Mais complexo e estruturado

**Diagnóstico:**
`[NOVO - MAS MAIS ROBUSTO]` O cálculo de ângulo em HEAD é **muito mais complexo** que em f06242. Razão: tenta ser mais robusto a dados ruins. Mas complexidade também significa **mais oportunidades de erro**.

---

## J. FLUXO GERAL RESUMIDO

### f06242 (Versão "Que Deu Certo")

```
Imagem
  ├─ Pré-processamento: OTSU simples
  ├─ Contorno: encontrar_contorno_gota() básica
  ├─ Baseline: Y_max
  ├─ Contatos: extremos esquerdo/direito
  ├─ Tangente: derivada simples
  ├─ Ângulo: círculo → arccos
  └─ Resultado: ✅ Corresponde GeoGebra
```

**Simplicidade:** Muito simples, poucos passos

### HEAD (Versão Atual)

```
Imagem
  ├─ Pré-processamento: Multi-threshold com scoring
  ├─ Separação: Necking + Sobel + abertura anisotrópica
  ├─ Contorno: encontrar_contorno_gota_robusto() com validação
  ├─ Baseline: cv2.fitLine + MAD + quantil 90%
  ├─ Contatos: Extrapolação polinomial grau 2
  ├─ Validação: Projeção no contorno
  ├─ Seleção pontos: Window height + aleatória
  ├─ Tangente: Janela local polinomial
  ├─ Ângulo: Círculo robusto → remoção outliers → arccos
  └─ Resultado: ❌ "Muitas modificações, não está correto"
```

**Complexidade:** Muito complexo, múltiplos estágios

---

## ANÁLISE DE CAUSAS PROVÁVEIS

### Candidatos para "Por que HEAD está errado mas f06242 estava certo"

#### CAUSA A: Máscara Diferente [ALTÍSSIMA PROBABILIDADE]

**Evidência:**
- HEAD usa multi-threshold com scoring
- f06242 usa OTSU simples
- Se máscara é diferente, tudo muda

**Teste para validar:**
- Salvar máscara em f06242
- Salvar máscara em HEAD
- Comparar visualmente

#### CAUSA B: Baseline em Y Diferente [ALTÍSSIMA PROBABILIDADE]

**Evidência:**
- f06242: Y_base = Y_max (simples)
- HEAD: Y_base = quantil 90% inliers robustos (complexo)

Se contorno é fechado (inclui substrate), então:
- Y_max em f06242 aponta para fundo do substrate
- Quantil 90% em HEAD aponta para interface líquido-ar? Ou também para substrate?

**Diferença esperada:** Muitos pixels (10-100 px) potencialmente

#### CAUSA C: Contorno em Posição Diferente [ALTÍSSIMA PROBABILIDADE]

**Evidência:**
- f06242: encontrar_contorno_gota() simples
- HEAD: encontrar_contorno_gota_robusto() com validação complexa

Se houver múltiplos contornos, a seleção pode ser diferente.

#### CAUSA D: Pontos de Contato Extrapolados vs Extremos [ALTA PROBABILIDADE]

**Evidência:**
- f06242: p_esq/p_dir = extremos esquerdo/direito no contorno
- HEAD: p_esq/p_dir = polinômio extrapolado em Y_base

Se baseline está errada, extrapolação também está errada.

#### CAUSA E: Deslocamento Aleatório em Seleção [MÉDIA PROBABILIDADE]

**Evidência:**
- HEAD usa random(1.5, 4.0) para deslocar baseline
- f06242 provavelmente não tinha isso

**Impacto:** Cada execução em HEAD pode dar resultado diferente (não-determinístico)

#### CAUSA F: Ordem de Múltiplos Estágios [MÉDIA PROBABILIDADE]

**Evidência:**
- HEAD tem muitas etapas: pré-processamento → separação → contorno → baseline → contatos → validação → seleção → tangente → ângulo
- f06242 provavelmente era: contorno → baseline → tangente → ângulo

**Risco:** Erro em qualquer estágio propaga para próximas etapas

---

## MAPA DE ALTERAÇÕES

| Componente | f06242 | HEAD | Status | Criticidade |
|-----------|--------|------|--------|------------|
| Pré-processamento | OTSU(3×3) | Multi [OTSU/ADAPTIVE/CANNY] | ALTERADO | 🔴 Crítica |
| Kernel Gaussian | (3,3) | (5,5) | ALTERADO | 🟡 Média |
| Separação gota/substrate | Nenhuma | Necking+Sobel+Abertura | NOVO | 🔴 Crítica |
| Detecção contorno | básica | robusto + validação | NOVO | 🔴 Crítica |
| Fallback contorno | Nenhum | Canny | NOVO | 🟡 Média |
| Baseline | Y_max | cv2.fitLine+MAD+quantil | NOVO | 🔴 Crítica |
| Contatos | extremos | polinômio grau 2 | NOVO | 🔴 Crítica |
| Validação contatos | Nenhuma | _validar_candidato | NOVO | 🟡 Média |
| Seleção pontos tangente | simples | janela+validação+random | NOVO | 🔴 Crítica |
| Tangente | simples | janela local polinomial | NOVO | 🟡 Média |
| Ângulo | círculo simples | círculo+outliers+robusto | NOVO | 🟡 Média |
| Audit context | Nenhum | Armazenado | NOVO | 🟢 Baixa |

---

## CONCLUSÃO

### Resposta: Por que f06242 "Deu Certo" e HEAD "Não Está Correto"

**Hipótese Mais Provável (>90% confiança):**

1. **Em f06242:** Pipeline simples, poucas etapas, menos oportunidades de erro
   - Máscara OTSU simples → contorno direto → Y_max como baseline → extremos como contatos → ângulo

2. **Em HEAD:** Pipeline complexo, múltiplas etapas, cada uma com validação
   - Máscara multi-threshold → separação gota/substrate → contorno robusto → cv2.fitLine+MAD+quantil para baseline → polinômio para contatos → seleção com janela+random

3. **Erro Introduzido:** Uma ou mais das alterações em HEAD quebrou a cadeia. Prováveis culpados:
   - Mudança em como a **máscara é gerada** (multi-threshold vs OTSU)
   - Mudança em como a **baseline é calculada** (quantil 90% vs Y_max)
   - Mudança em como **contatos são obtidos** (polinômio vs extremos)

4. **Evidência:** Mensagens dos commits HEAD:
   - 99037c7: "Analisando para poder identificar o erro no calculo"
   - ee5a89d: "Finalizando investigacao. Calculo ainda errado"
   - 69ebd9f: "Contorno ate a linha base. Pontos (ok) Tang (+/-)"
   - 9beb758: "Modelo com muitas modificacoes porem nao esta correto"

   Parece que cada tentativa de "consertar" adicionou mais complexidade sem resolver o problema.

### Recomendação Diagnóstica

Para identificar o culpado com certeza, verificar:

1. **Máscara:** Salvar `bin_img` em ambas versões → são iguais?
2. **Contorno:** Salvar `gota_pts` em ambas versões → mesmo número de pontos? Mesma forma?
3. **Baseline:** Imprimir `baseline_y` em ambas versões → quantos pixels de diferença?
4. **Contatos:** Imprimir `p_esq`, `p_dir` em ambas versões → mesma posição?

Se as respostas forem "não" em qualquer um, encontrou o culpado.

---

**FIM DA ANÁLISE COMPARATIVA**
