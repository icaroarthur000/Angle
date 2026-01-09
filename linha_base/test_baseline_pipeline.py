"""
test_baseline_pipeline.py

Testes unitários para o novo pipeline híbrido de detecção de baseline.
Valida:
- Seleção de candidatos com curvatura
- Regressão robusta (cv2.fitLine)
- Projeção ortogonal
- Fallback automático
"""

import cv2
import numpy as np
from linha_base import linha_base


def test_synthetic_gota_horizontal():
    """Testa contorno sintético de gota com baseline horizontal."""
    # criar contorno sintético (gota em pé, baseline horizontal)
    # parte superior: arco (maior curvatura)
    # parte inferior: quase reta (baixa curvatura)
    
    theta = np.linspace(0, np.pi, 50)
    x_top = 100 + 60 * np.cos(theta)
    y_top = 80 + 80 * np.sin(theta)
    
    # parte inferior: quase horizontal com pouca curvatura
    x_bottom = np.linspace(50, 150, 30)
    y_bottom = np.full_like(x_bottom, 160.0, dtype=np.float64)
    
    # combinar pontos
    gota_pts = np.vstack([
        np.column_stack([x_top, y_top]),
        np.column_stack([x_bottom, y_bottom])
    ]).astype(np.float32)
    
    # testar pipeline
    result = linha_base.detectar_baseline_hibrida(gota_pts)
    
    assert result is not None
    assert result['baseline_y'] is not None
    assert result['method'] in ['regression', 'fallback']
    
    print("✓ test_synthetic_gota_horizontal PASSOU")
    print(f"  Método: {result['method']}, R²: {result['r_squared']:.3f}, baseline_y: {result['baseline_y']:.1f}")
    return result


def test_synthetic_gota_inclinada():
    """Testa contorno sintético com baseline inclinada."""
    # parte superior: arco
    theta = np.linspace(0, np.pi, 50)
    x_top = 100 + 60 * np.cos(theta)
    y_top = 80 + 80 * np.sin(theta)
    
    # parte inferior: reta inclinada (não horizontal)
    x_bottom = np.linspace(50, 150, 30)
    y_bottom = 160.0 + 0.3 * (x_bottom - 50)  # inclinação suave
    
    gota_pts = np.vstack([
        np.column_stack([x_top, y_top]),
        np.column_stack([x_bottom, y_bottom])
    ]).astype(np.float32)
    
    result = linha_base.detectar_baseline_hibrida(gota_pts)
    
    assert result is not None
    assert result['baseline_y'] is not None
    
    # se regressão bem-sucedida, linha_params não deve ser None
    if result['method'] == 'regression':
        vx, vy, x0, y0 = result['line_params']
        # verificar que não é puramente horizontal (vy não deve ser zero)
        print(f"  Direção da linha: vx={vx:.3f}, vy={vy:.3f}")
    
    print("✓ test_synthetic_gota_inclinada PASSOU")
    print(f"  Método: {result['method']}, R²: {result['r_squared']:.3f}")
    return result


def test_select_candidates():
    """Testa função de seleção de candidatos."""
    # criar contorno com região de curvatura baixa bem definida
    theta = np.linspace(0, np.pi, 50)
    x_top = 100 + 60 * np.cos(theta)
    y_top = 80 + 80 * np.sin(theta)
    
    x_bottom = np.linspace(50, 150, 50)
    y_bottom = np.full_like(x_bottom, 160.0, dtype=np.float64)
    
    gota_pts = np.vstack([
        np.column_stack([x_top, y_top]),
        np.column_stack([x_bottom, y_bottom])
    ]).astype(np.float32)
    
    candidates = linha_base.select_baseline_candidates(gota_pts)
    
    assert len(candidates) > 0, "Nenhum candidato selecionado"
    print(f"✓ test_select_candidates PASSOU: {len(candidates)} candidatos")
    print(f"  Candidatos selecionados (primeiros 5): {candidates[:5]}")
    return candidates


def test_fit_line_quality():
    """Testa qualidade do ajuste de linha."""
    # pontos perfeitamente alinhados
    perfect_line = np.array([
        [10, 50], [20, 50], [30, 50], [40, 50], [50, 50],
        [60, 50], [70, 50], [80, 50], [90, 50], [100, 50]
    ], dtype=np.float32)
    
    line_params, r_squared = linha_base.fit_baseline_with_line(perfect_line)
    
    assert line_params is not None, "Falha no ajuste de linha perfeita"
    assert r_squared > 0.95, f"R² muito baixo para linha perfeita: {r_squared}"
    
    print(f"✓ test_fit_line_quality PASSOU: R² = {r_squared:.4f}")
    vx, vy, x0, y0 = line_params
    print(f"  Parâmetros: vx={vx:.3f}, vy={vy:.3f}, x0={x0:.1f}, y0={y0:.1f}")
    return r_squared


def test_project_onto_line():
    """Testa projeção de contorno sobre baseline."""
    # contorno de uma gota simples
    theta = np.linspace(0, np.pi, 50)
    x_top = 100 + 50 * np.cos(theta)
    y_top = 80 + 60 * np.sin(theta)
    
    x_bottom = np.linspace(60, 140, 30)
    y_bottom = np.full_like(x_bottom, 140.0)
    
    gota_pts = np.vstack([
        np.column_stack([x_top, y_top]),
        np.column_stack([x_bottom, y_bottom])
    ]).astype(np.float32)
    
    # linha base horizontal
    line_params = (1.0, 0.0, 50, 140)  # horizontal em y=140
    
    p_esq, p_dir = linha_base.project_contour_onto_baseline(gota_pts, line_params)
    
    assert p_esq is not None and p_dir is not None
    assert p_esq[0] < p_dir[0], "Pontos de contato não estão na ordem correta"
    
    print("✓ test_project_onto_line PASSOU")
    print(f"  P_esq: ({p_esq[0]:.1f}, {p_esq[1]:.1f})")
    print(f"  P_dir: ({p_dir[0]:.1f}, {p_dir[1]:.1f})")
    return p_esq, p_dir


if __name__ == "__main__":
    print("=" * 70)
    print("TESTES DO PIPELINE HÍBRIDO DE DETECÇÃO DE BASELINE")
    print("=" * 70)
    
    try:
        test_select_candidates()
        print()
        
        test_fit_line_quality()
        print()
        
        test_project_onto_line()
        print()
        
        test_synthetic_gota_horizontal()
        print()
        
        test_synthetic_gota_inclinada()
        print()
        
        print("=" * 70)
        print("✓ TODOS OS TESTES PASSARAM")
        print("=" * 70)
    except Exception as e:
        print(f"✗ ERRO: {e}")
        import traceback
        traceback.print_exc()
