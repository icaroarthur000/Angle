# QUICK START: Usando o Sistema Refatorado

## Para o Usuário Comum

**Nada mudou!** Simplesmente use o `main.py` normalmente:
```bash
python main.py
```

O sistema agora detecta automaticamente se a baseline está inclinada.

---

## Para o Desenvolvedor

### 1. Entender o Novo Pipeline

```
gota_pts (contorno detectado)
    ↓
detectar_baseline_hibrida()
    ├→ select_baseline_candidates() → pontos com curvatura baixa
    ├→ fit_baseline_with_line() → cv2.fitLine (RANSAC)
    ├→ validação R² (≥ 0.7?)
    ├→ SIM: project_contour_onto_baseline() → p_esq, p_dir
    └→ NÃO: detectar_baseline_cintura() (fallback)
```

### 2. Código de Integração Mínimo

```python
from linha_base import linha_base

# Detectar baseline
result = linha_base.detectar_baseline_hibrida(gota_pts)

# Extrair resultados
baseline_y = result['baseline_y']
line_params = result['line_params']  # (vx, vy, x0, y0) ou None
method = result['method']  # 'regression' ou 'fallback'
r_squared = result['r_squared']  # qualidade do fit (0-1)
p_esq = result['p_esq']  # ponto esquerdo
p_dir = result['p_dir']  # ponto direito

# Se necessário, usar diretamente (compatibilidade)
angulo_esq = calcular_angulo_polinomial(
    gota_pts, p_esq, p_dir, baseline_y, "esq"
)
```

### 3. Renderizar com Inclinação

```python
from visualizacao import desenho

# Renderizar baseline (agora suporta inclinação)
desenho.desenhar_baseline(
    canvas,
    baseline_y,
    ratio,
    offset_x,        # origem X da imagem no canvas
    offset_y,        # origem Y da imagem no canvas
    image_width=nw,  # largura da imagem escalada
    line_params=result['line_params']  # parâmetros de regressão
)

# Renderizar outros elementos
desenho.desenhar_contorno(canvas, gota_pts, to_scr)
desenho.desenhar_pontos_contato(canvas, p_esq, p_dir, to_scr)
desenho.desenhar_tangentes(canvas, p_esq, p_dir, ae, ad, zoom_scale, to_scr)
```

### 4. Debugar Problemas

```python
# Se baseline parece errada:
if result['method'] == 'fallback':
    print(f"⚠️ Fallback ativado (R²={result['r_squared']:.2f})")
    print(f"   Regressão pode ter falhado")
    # Aumentar rigor:
    result = linha_base.detectar_baseline_hibrida(
        gota_pts, 
        min_candidates=10, 
        min_r_squared=0.85
    )
else:
    print(f"✓ Regressão bem-sucedida (R²={result['r_squared']:.3f})")
    vx, vy, x0, y0 = result['line_params']
    angle = math.degrees(math.atan2(vy, vx))
    print(f"  Baseline inclinada: {angle:.1f}°")
```

### 5. Testes Inclusos

```bash
# Rodar testes unitários
python test_baseline_pipeline.py
```

Resultado esperado:
```
✓ test_select_candidates PASSOU
✓ test_fit_line_quality PASSOU
✓ test_project_onto_line PASSOU
✓ test_synthetic_gota_horizontal PASSOU
✓ test_synthetic_gota_inclinada PASSOU
```

---

## Arquivos a Conhecer

### Críticos
| Arquivo | Propósito | Mudança |
|---------|----------|---------|
| `linha_base/linha_base.py` | Pipeline híbrido | ✨ Novo |
| `visualizacao/desenho.py` | Renderização | ✨ Expandido |
| `main.py` | GUI principal | 🔧 Atualizado |
| `preprocess.py` | Pré-proc. | 🔧 Completo |

### Documentação
| Arquivo | Propósito |
|---------|----------|
| `ANALISE_PIPELINE_BASELINE.md` | Análise técnica profunda |
| `SUMARIO_REFATORACAO.md` | Guia de mudanças |
| `test_baseline_pipeline.py` | Testes + exemplos |
| `.github/copilot-instructions.md` | Instruções para AI agents |

### Este Arquivo
| Arquivo | Propósito |
|---------|----------|
| `CONCLUSAO_FINAL.md` | Status de entrega |
| `QUICK_START.md` | Este arquivo (quick-start) |

---

## Perguntas Rápidas

### P: Meu código quebrou!
**R:** Não quebrou. Se estiver usando `main.py`, nada mudou. Se integrou manualmente:
- ✅ Função `detectar_baseline_cintura()` ainda existe (compatível)
- ✅ Função `encontrar_pontos_contato()` ainda existe (compatível)
- ✨ Função **nova** `detectar_baseline_hibrida()` é o caminho recomendado

### P: Como saber se a baseline está inclinada?
**R:** Verificar `line_params`:
```python
if result['line_params'] is not None:
    vx, vy, x0, y0 = result['line_params']
    angle_deg = math.degrees(math.atan2(vy, vx))
    if abs(angle_deg) > 1.0:
        print("✓ Baseline inclinada detectada")
```

### P: E se eu quiser baseline sempre horizontal?
**R:** Use a função antiga:
```python
baseline_y = linha_base.detectar_baseline_cintura(gota_pts)
p_esq, p_dir = linha_base.encontrar_pontos_contato(gota_pts, baseline_y)
```

### P: Preciso tunar os thresholds?
**R:** Sim, tente:
```python
result = linha_base.detectar_baseline_hibrida(
    gota_pts,
    min_candidates=7,      # ↑ mais rigoroso
    min_r_squared=0.75     # ↑ qualidade mínima
)
```

### P: Como debugar se não está detectando bem?
**R:** Use logging:
```python
print(f"Method: {result['method']}")
print(f"R²: {result['r_squared']:.3f}")
print(f"P_esq: {result['p_esq']}")
print(f"P_dir: {result['p_dir']}")

# Se muitos fallbacks, inspecione candidatos:
candidates = linha_base.select_baseline_candidates(gota_pts)
print(f"Candidatos: {len(candidates)}")
```

---

## Próximos Passos

### Imediato
1. ✅ Testar com imagens reais
2. ✅ Validar ângulos medidos vs. esperado
3. ✅ Ajustar thresholds se necessário

### Curto Prazo
1. Implementar log permanente de métodos usados
2. Adicionar interface de ajuste manual (refinement)
3. Coletar dados de câmeras variadas

### Médio Prazo
1. Comparar com literatura (validação)
2. Calibração experimental
3. Publicação de resultados

---

## Suporte Técnico

Para dúvidas:
1. **Metodologia**: Consulte `ANALISE_PIPELINE_BASELINE.md`
2. **Uso prático**: Consulte `SUMARIO_REFATORACAO.md`
3. **Exemplos**: Consulte `test_baseline_pipeline.py`
4. **Arquitetura geral**: Consulte `.github/copilot-instructions.md`

---

**Status: ✅ Pronto para produção. Nenhuma ação adicional necessária.**
