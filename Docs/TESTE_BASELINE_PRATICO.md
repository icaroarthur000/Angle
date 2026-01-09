# Guia Prático de Teste — Pipeline Híbrido de Baseline

## 🎯 Objetivo

Validar que o sistema de detecção de linha base funciona corretamente com múltiplos usuários, câmeras inclinadas e substratos variados.

---

## 📋 CHECKLIST DE TESTES

### **TESTE 1: Imagem Horizontal (Caso Base)**

**Cenário**: Câmera perpendicular, gota em substrato horizontal

**O que esperar**:
- `method`: 'regression'
- `r_squared`: ≥ 0.85
- `angulo_baseline`: ≈ 0° ± 2°
- `p_esq`, `p_dir`: pontos simétricos no eixo Y

**Como executar**:
```python
# No seu IDE ou script
from linha_base import linha_base

# Importar imagem com gota bem definida
img_bin = cv2.imread("teste_horizontal.png", 0)  # binária
gota_pts = encontrar_contorno_gota(img_bin)

result = linha_base.detectar_baseline_hibrida(gota_pts)
diag = linha_base.diagnosticar_baseline(gota_pts, result)

print(f"Status: {diag['status']}")
print(f"R²: {result['r_squared']:.3f}")
print(f"Ângulo: {diag.get('angulo_baseline', 0):.1f}°")
```

**Critério de Sucesso**: ✅ `diag['status']` == 'OK'

---

### **TESTE 2: Câmera Inclinada (+15°)**

**Cenário**: Câmera rotacionada 15° em relação à vertical

**O que esperar**:
- `method`: 'regression'
- `r_squared`: ≥ 0.75
- `angulo_baseline`: ≈ 15° ± 3°
- A baseline é visualmente inclinada

**Critério de Sucesso**: ✅ `diag['status']` == 'OK' + ângulo estimado ~15°

---

### **TESTE 3: Imagem Muito Pequena (50×50 px)**

**Cenário**: Gota diminuta, quase no limite de detecção

**O que esperar**:
- `method`: 'fallback' (regressão pode falhar)
- `baseline_y`: calculada por cintura
- `diag['status']`: 'FALLBACK'
- Pontos de contato ainda identificáveis

**Critério de Sucesso**: ✅ Não há erro; fallback funciona

---

### **TESTE 4: Contato Muito Estreito**

**Cenário**: Gota tocando superfície em linha muito definida (quase sem espessura)

**O que esperar**:
- `method`: 'regression'
- `r_squared`: ≥ 0.90 (muito linear!)
- `num_candidatos`: pequeno mas bem alinhado
- `diag['status']`: 'OK'

**Critério de Sucesso**: ✅ Detecta regressão com R² muito alto

---

### **TESTE 5: Contato Amplo (Gota Muito Plana)**

**Cenário**: Gota espalhada em substrato, contato muito largo

**O que esperar**:
- `method`: 'regression' OU 'fallback' (depende de R²)
- Se 'regression': `r_squared` ~0.70-0.75
- Se 'fallback': cintura ainda identifica zona de contato

**Critério de Sucesso**: ✅ Ambos os métodos funcionam

---

### **TESTE 6: Imagem com Ruído/Artefatos**

**Cenário**: Imagem com reflexos, poeira, imperfeições

**O que esperar**:
- RANSAC rejeita outliers
- `num_candidatos` pode ser menor
- `r_squared` pode ser 0.65-0.75
- Se R² < 0.7 → fallback cintura ativa

**Critério de Sucesso**: ✅ `diag['status']` != 'ERRO'

---

### **TESTE 7: Contaminação na Superfície**

**Cenário**: Poeira ou imperfeições na linha de contato

**O que esperar**:
- Candidatos podem incluir ou não a contaminação
- Regressão RANSAC filtra outliers
- Se muita contaminação → fallback cintura

**Critério de Sucesso**: ✅ Baseline ainda detectada com sanidade

---

## 📊 TABELA DE RESULTADOS ESPERADOS

| Teste | Método Esperado | R² Esperado | Status Esperado | Ângulo |
|-------|-----------------|-------------|-----------------|--------|
| 1. Horizontal | Regression | ≥0.85 | OK | 0° ± 2° |
| 2. Inclinada +15° | Regression | ≥0.75 | OK | 15° ± 3° |
| 3. Muito Pequena | Fallback | 0 | FALLBACK | 0° |
| 4. Contato Estreito | Regression | ≥0.90 | OK | ~0° |
| 5. Contato Amplo | Regression/Fallback | 0.70+ | OK/FALLBACK | ~0° |
| 6. Com Ruído | Regression/Fallback | 0.65+ | OK/MARGINAL | ~0° |
| 7. Contaminação | Regression/Fallback | 0.60+ | OK/FALLBACK | ~0° |

---

## 🔧 SCRIPT DE TESTE AUTOMATIZADO

```python
import cv2
import numpy as np
from processamento_imagem.contorno import encontrar_contorno_gota
from linha_base.linha_base import detectar_baseline_hibrida, diagnosticar_baseline

def testar_baseline(img_path, nome_teste):
    """Executa teste único e exibe resultado."""
    
    # Carregar imagem
    img = cv2.imread(img_path, 0)
    if img is None:
        print(f"❌ {nome_teste}: Imagem não encontrada")
        return False
    
    # Encontrar contorno
    gota_pts = encontrar_contorno_gota(img)
    if gota_pts is None or len(gota_pts) < 5:
        print(f"❌ {nome_teste}: Contorno não detectado")
        return False
    
    # Detectar baseline
    result = detectar_baseline_hibrida(gota_pts)
    diag = diagnosticar_baseline(gota_pts, result)
    
    # Exibir resultado
    status_ok = diag['status'] in ['OK', 'FALLBACK']
    emoji = "✅" if status_ok else "❌"
    
    print(f"\n{emoji} {nome_teste}")
    print(f"   Status: {diag['status']}")
    print(f"   R²: {result['r_squared']:.3f}")
    print(f"   Método: {result['method']}")
    if 'angulo_baseline' in diag:
        print(f"   Ângulo: {diag['angulo_baseline']:.1f}°")
    print(f"   Msg: {diag['msg']}")
    
    return status_ok

# Executar testes
testes = [
    ("teste_horizontal.png", "Teste 1: Horizontal"),
    ("teste_inclinada_15.png", "Teste 2: Inclinada +15°"),
    ("teste_pequena.png", "Teste 3: Muito Pequena"),
    ("teste_estreito.png", "Teste 4: Contato Estreito"),
    ("teste_amplo.png", "Teste 5: Contato Amplo"),
    ("teste_ruido.png", "Teste 6: Com Ruído"),
    ("teste_contaminacao.png", "Teste 7: Contaminação"),
]

print("="*60)
print("SUITE DE TESTES — LINHA BASE HÍBRIDA")
print("="*60)

resultados = []
for img_path, nome in testes:
    resultado = testar_baseline(img_path, nome)
    resultados.append(resultado)

print("\n" + "="*60)
print(f"RESUMO: {sum(resultados)}/{len(resultados)} testes passaram")
print("="*60)
```

---

## ⚠️ SINAIS DE ALERTA

Se você observar um destes, há problema:

| Sinal de Alerta | Possível Causa | Solução |
|-----------------|----------------|--------|
| `status: ERRO` | Contorno muito pequeno ou inválido | Verificar captura/binária |
| `r_squared: < 0.6` repetidamente | Curvatura não é plana; superfície muito curva | Revisar imagem; mudar substrato? |
| `angulo_baseline: > 45°` | Regressão ajustou em orientação errada | Validação de sanidade deveria rejeitar |
| `method: fallback` sempre | Regressão nunca converge | Baixa qualidade de candidatos; revisar thresholds |
| `p_esq ≈ p_dir` | Pontos de contato não diferenciados | Gota muito pequena ou contato não bem definido |

---

## 📞 TROUBLESHOOTING

### Problema: "method: fallback" em 80% dos testes

**Diagnóstico**:
```python
candidates = select_baseline_candidates(gota_pts)
print(f"Num candidatos: {len(candidates)}")
print(f"Curvatures: min={...}, max={...}")
```

**Soluções**:
1. Aumentar `curvature_threshold` (ex: 0.20 em vez de 0.15)
2. Aumentar `y_variance_threshold` (ex: 10.0 em vez de 8.0)
3. Verificar qualidade da imagem binária

---

### Problema: Ângulo estimado sempre ~0°, mesmo em câmera inclinada

**Diagnóstico**: Câmera pode estar mais alinhada que você pensou, OU imagem não mostra inclinação real.

**Solução**: Tirar foto de referência com transferidor/nível.

---

### Problema: "status: MARGINAL" frequente

**Significa**: R² entre 0.65-0.70 (regressão aceitável mas não ótima).

**Ações**:
- Verificar qualidade de iluminação
- Confirmar binarização está limpa (sem ruído interno)
- Considerar relaxar threshold R² para 0.65 em seu ambiente específico

---

## ✅ CONCLUSÃO DO TESTE

Quando você passar em TODOS os 7 testes:
- ✅ Sistema robusto para múltiplos usuários
- ✅ Câmeras inclinadas suportadas
- ✅ Fallback funcionando
- ✅ Pronto para produção

---

**Engenheiro**: Pesquisador em Visão Computacional  
**Data**: 8 de janeiro de 2026
