# Instruções para Agents de IA - Projeto Angle

## Visão Geral do Projeto

**Propósito**: Sistema de análise de imagem para medição de ângulos de contato (contact angle) em gotas. Arquitetura modular em Python com GUI customtkinter.

**Pipeline de Processamento** (atualizado com baseline híbrida):
1. **Captura** → Arquivo ou câmera (SelectionWindow em main.py)
2. **Seleção ROI** → Usuário desenha retângulo sobre a gota
3. **Pré-processamento** → preprocess.py normaliza iluminação e binariza
4. **Detecção de Contorno** → encontra_contorno_gota() em processamento_imagem/contorno.py
5. **Detecção de Baseline** → Pipeline híbrido (regressão + fallback) em linha_base.py
6. **Cálculo de Ângulo** → ajuste polinomial em Cal_angulo/angulo_contato.py
7. **Visualização** → desenho.py renderiza baseline (inclinada ou horizontal) e resultados

## Arquitetura por Módulo

### main.py (660 linhas)
- **SelectionWindow**: GUI para captura de imagem, seleção ROI com mouse (start_roi → draw_roi → end_roi)
- **AnalysisWindow**: GUI para visualizar resultado, exibir ângulos
- Suporta fallback gracioso (tenta preprocess.py, reverte para filtros.py se falhar)
- Exporta debug_imgs para cada etapa do processamento
- **NOVO**: Integração com pipeline híbrido de baseline

### preprocess.py (230 linhas) - **Pipeline de Pré-processamento Robusto**
**Função principal**: `preprocess_image_for_contact_angle(img_bgr, ...)`
- **Etapa 1**: Denoising com Gaussian Blur
- **Etapa 2**: Background subtraction via divisão `(gray / bg) * 128` para corrigir iluminação não-uniforme
- **Etapa 3**: CLAHE (Contrast Limited Adaptive Histogram Equalization) com grid que escala com a imagem
- **Etapa 4**: Adaptive threshold Gaussian (não Otsu!) para preservar contorno fino, com proteção para imagens pequenas
- **Etapa 5**: Morphological cleanup (closing + opening)
- **Retorna**: `{enhanced_gray, binary, corrected_bgr, debug_imgs}` - todos uint8

**Função secundária**: `save_debug_imgs(debug_dict, out_dir, prefix="dbg")`
- Salva imagens de debug em PNG
- Robusta: converte para uint8, trata exceções sem quebrar

### linha_base/linha_base.py (280 linhas) - **Pipeline Híbrido (NOVO)**
**Novas funções**:
- `_compute_curvature_at_point()`: Curvatura robusta via segunda derivada suavizada
- `select_baseline_candidates()`: Seleciona pontos com curvatura baixa (superfície plana)
- `fit_baseline_with_line()`: Regressão robusta com cv2.fitLine (RANSAC) + validação R²
- `project_contour_onto_baseline()`: Projeção ortogonal para encontrar pontos de contato reais
- `detectar_baseline_hibrida()`: **Orquestrador** → regressão com fallback automático
  - Retorna dict: `{line_params, baseline_y, r_squared, method, p_esq, p_dir}`
  - Método: 'regression' (quando R² ≥ 0.7) ou 'fallback' (cintura)

**Compatibilidade**:
- `detectar_baseline_cintura()` mantida (fallback)
- `encontrar_pontos_contato()` mantida como wrapper

### processamento_imagem/contorno.py
- `encontrar_contorno_gota()`: Encontra maior contorno, tenta MORPH_CLOSE depois Canny como fallback
- Retorna array Nx2 (x,y) ou None
- **Crítico**: Usa `CHAIN_APPROX_NONE` para preservar todos pontos (não simplifica)

### processamento_imagem/filtros.py (Legacy)
- Fallback simples (grayscale → Gaussian blur → Otsu threshold)
- Usado se preprocess.py não estiver disponível

### Cal_angulo/angulo_contato.py
- `calcular_angulo_polinomial()`: Ajuste polinomial 2ª ordem `x = ay² + by + c` (y invertido para melhor fit)
- **Cálculo**: Derivada `dx/dy` na baseline → `angle = arctan(1 / dx_dy)`
- Diferencia lado esquerdo/direito (ajusta sinais para 0-180°)
- Filtra pontos por lado do centro horizontal

### visualizacao/desenho.py (200 linhas) - **Expandido**
**Novas funções**:
- `desenhar_contorno()`: Renderiza limite da gota (cyan)
- `desenhar_pontos_contato()`: Marca pontos de contato (yellow)
- `desenhar_tangentes()`: Renderiza linhas de ângulos (green)

**Função refatorada**:
- `desenhar_baseline()`: Suporta **baseline inclinada**
  - Parâmetros: baseline_y, ratio, offset_x, offset_y, image_width, line_params
  - Se line_params=(vx, vy, x0, y0): renderiza inclinada
  - Se None: renderiza horizontal (fallback)

## Padrões e Convenções Críticas

### Tipagem de Dados
- **Imagens**: BGR (OpenCV), uint8 (salvo durante processamento em float32 temporariamente)
- **Contornos**: Array Nx2 com (x, y) em pixels
- **Dicts**: Funções retornam dicts nomeados (não tuples)
- **Baseline**: `line_params = (vx, vy, x0, y0)` normalizado (ou None se horizontal)

### Ordem de Coordenadas
- **Imagem**: (x=coluna, y=linha), y cresce para baixo
- **Contorno**: Respita esta convenção
- **Canvas/GUI**: Também usa y crescente para baixo

### Processamento de Iluminação
Problema: Imagens de gotas têm reflexos/iluminação não-uniforme. **Solução**: Background subtraction por divisão, não simples subtração.

### ROI e Zoom
SelectionWindow preserva zoom (ratio) e offset para conversão imagem↔canvas. Crítico ao trabalhar com seleção do usuário.

### Baseline Inclinada (NOVO)
- Não assume horizontalidade
- Detectada via regressão robusta (cv2.fitLine)
- Validada com R²
- Renderizada com parâmetros (vx, vy, x0, y0)
- Fallback automático (método de cintura) se regressão falhar

## Fluxos de Trabalho de Desenvolvimento

### Adicionando Novo Filtro de Pré-processamento
1. Editar `preprocess_image_for_contact_angle()` ou criar função nova
2. Retornar dict com chaves `binary` e `enhanced_gray` (main.py usa fallback esperando estas chaves)
3. Testar com `save_debug_imgs()` para visualizar intermediários

### Debug de Contorno Inadequado
1. Verificar `debug_imgs[enhanced_gray]` - contraste suficiente?
2. Testar binarização: é conectado? Tem buracos?
3. Se contorno quebrado: MORPH_CLOSE kernel maior ou CLAHE clipLimit maior
4. Se ruído: Gaussian blur maior ou MORPH_OPEN mais agressivo

### Validando Detecção de Baseline
1. Verificar `baseline_result['method']`: 'regression' ou 'fallback'?
2. Se 'regression': inspecionar `baseline_result['r_squared']` (target: ≥ 0.7)
3. Se 'fallback': check `line_params is None`
4. Inspecionar `baseline_result['p_esq']` e `p_dir` — estão razoáveis?

### Adicionando Nova Métrica (não apenas ângulo)
1. Dados disponíveis após linha_base: gota_pts (contorno), baseline_y, baseline_line_params, p_esq, p_dir
2. Adicionar cálculo em Cal_angulo/
3. Renderizar em desenho.py (usar `to_scr` callback)
4. Expor em GUI (AnalysisWindow)

## Integração e Dependências

### Externas
- **cv2** (OpenCV): Processamento de imagem core + fitLine para regressão
- **numpy**: Álgebra linear, manipulação de arrays
- **customtkinter**: GUI moderna
- **PIL**: Manipulação de imagens para exibição
- **tkinter**: Diálogos de arquivo (filedialog, messagebox)

### Modelos Internos de Dados
- Sempre validar que arrays Nx2 têm dtype int32 ou float32 antes de usar com cv2.contourArea, cv2.convexHull
- Suportar tanto BGR quanto grayscale (main.py fallback trata ambos)

### Fallbacks Robustos
Main.py implementa fallback em cascata:
1. Tentar `preprocess_image_for_contact_angle()` (modo robusto)
2. Fallback para `filtros.aplicar_pre_processamento()` (modo simples)
3. Última alternativa: grayscale + Otsu threshold manual

linha_base.py implementa fallback em cascata:
1. Tentar `detectar_baseline_hibrida()` com regressão (NOVO)
2. Fallback para método de cintura se regressão falhar

Ao modificar pipeline, manter compatibilidade ou atualizar fallback.

## Padrões de Tratamento de Erros

- **Contorno não encontrado**: Funções retornam None ou 0.0, main.py mostra mensagem
- **ROI muito pequeno**: `if len(local_pts) < 5: return 0.0` (várias funções)
- **Baseline inadequada**: Fallback automático ativa (R² < 0.7 ou < 5 candidatos)
- **Imagem corrompida**: Fallback gracioso entre métodos de binarização
- Não usar assertions - usar validações com retorno seguro

## Checklist para Novas Features

- [ ] Testar com imagens de câmera (não apenas arquivos)
- [ ] Validar com gotas de tamanhos variados (pequeno/grande)
- [ ] Garantir compatibilidade com fallback (tipagem de retorno consistente)
- [ ] Adicionar debug_imgs se etapa visual (para troubleshooting)
- [ ] Atualizar AnalysisWindow se nova métrica gerada
- [ ] Testar com imagens inclinadas se envolver baseline
- [ ] Validar R² se envolver regressão

## Documentação Técnica

Arquivos de referência:
- `ANALISE_PIPELINE_BASELINE.md`: Análise crítica da metodologia, justificativas, limitações
- `SUMARIO_REFATORACAO.md`: Guia prático, mudanças necessárias, FAQ
- `test_baseline_pipeline.py`: Testes unitários e exemplos
- `CONCLUSAO_FINAL.md`: Status de entrega e próximos passos

