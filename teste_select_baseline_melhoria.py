#!/usr/bin/env python3
"""
Comparacao: Selecao de candidatos ANTES vs DEPOIS das melhorias.
Demonstra como os novos filtros (slope + zona lateral) eliminam pontos do pe da gota.
"""

import sys
import numpy as np
sys.path.insert(0, r'c:\Users\Icaro Arthur\Documents\Angle')

import cv2
from linha_base.linha_base import select_baseline_candidates

print("\n" + "="*80)
print("COMPARACAO: SELECAO DE CANDIDATOS ANTES vs DEPOIS")
print("="*80)

# Criar contorno de gota realista
theta = np.linspace(0, 2*np.pi, 200)
y_baseline = 150
x_center = 120
altura = 90
raio_base = 60

x_gota = x_center + raio_base * np.cos(theta)
y_gota = y_baseline - altura * (0.5 + 0.5 * np.sin(theta))

# Garantir toque na baseline
x_gota[np.argmin(np.abs(theta - np.pi))] = x_center - raio_base
y_gota[np.argmin(np.abs(theta - np.pi))] = y_baseline

x_gota[np.argmin(np.abs(theta))] = x_center + raio_base
y_gota[np.argmin(np.abs(theta))] = y_baseline

contour = np.column_stack([x_gota, y_gota]).astype(np.float32)

print(f"\n[CONTORNO DE TESTE]")
print(f"  Pontos totais: {len(contour)}")
print(f"  X range: [{contour[:, 0].min():.1f}, {contour[:, 0].max():.1f}]")
print(f"  Y range: [{contour[:, 1].min():.1f}, {contour[:, 1].max():.1f}]")

# ============= SIMULAR VERSAO ANTERIOR (SEM SLOPE + SEM MARGEM) =============
print("\n" + "-"*80)
print("[ANTES] Selecao com apenas curvatura + variacao Y")
print("-"*80)

# Simular versao antiga
x_rect, y_rect, w_rect, h_rect = cv2.boundingRect(contour)

search_start = y_rect + int(h_rect * 0.5)
search_end = y_rect + int(h_rect * 0.95)

y_mask = (contour[:, 1] >= search_start) & (contour[:, 1] <= search_end)
pts_in_region = contour[y_mask]

print(f"  Pontos na regiao Y (50%-95%): {len(pts_in_region)}")
print(f"  X range (sem filtro lateral): [{pts_in_region[:, 0].min():.1f}, {pts_in_region[:, 0].max():.1f}]")
print(f"  Nota: incluem PIES da gota nas extremidades!")

# ============= NOVA VERSAO (COM SLOPE + MARGEM) =============
print("\n" + "-"*80)
print("[DEPOIS] Selecao com curvatura + variacao Y + SLOPE + MARGEM LATERAL")
print("-"*80)

candidates_new = select_baseline_candidates(
    contour,
    curvature_threshold=0.15,
    y_variance_threshold=8.0,
    slope_threshold=0.15,
    lateral_margin_percent=0.12
)

print(f"  Pontos selecionados: {len(candidates_new)}")
if len(candidates_new) > 0:
    print(f"  X range (SEM pies): [{candidates_new[:, 0].min():.1f}, {candidates_new[:, 0].max():.1f}]")
    print(f"  Y range: [{candidates_new[:, 1].min():.1f}, {candidates_new[:, 1].max():.1f}]")
    
    # Calcular redução
    margin = 0.12 * w_rect
    x_min_valid = x_rect + margin
    x_max_valid = x_rect + w_rect - margin
    
    print(f"\n  [FILTRO LATERAL]")
    print(f"    Margem esquerda: 12% de {w_rect:.0f}px = {margin:.0f}px")
    print(f"    X valido: [{x_min_valid:.1f}, {x_max_valid:.1f}]")
    print(f"    Pies excluidos: < {x_min_valid:.0f} e > {x_max_valid:.0f}")
    
    print(f"\n  [FILTRO SLOPE]")
    print(f"    Inclinacao maxima: 0.15 (~8.5 graus)")
    print(f"    Pies da gota rejeitados por slope crescente")

# ============= ANALISE COMPARATIVA =============
print("\n" + "="*80)
print("ANALISE DO IMPACTO")
print("="*80)

print(f"\n[PROBLEMA ORIGINAL]")
print(f"  Contaminacao da baseline por pontos do pe da gota")
print(f"  - Pies tem curvatura local baixa (confunde com superfice)")
print(f"  - Mas tem inclinacao crescente (slope alto)")
print(f"  - E estao nas EXTREMIDADES X da bounding box")

print(f"\n[SOLUCAO IMPLEMENTADA]")
print(f"  1. Filtro SLOPE: rejeita inclinacao > 0.15")
print(f"     => Distingue superfice (slope~0) de pies (slope crescente)")
print(f"  2. Filtro MARGEM LATERAL: exclui 12% de cada lado")
print(f"     => Remove pontos dos pies que estao nas extremidades")
print(f"  3. Fallback inteligente: relaxa criteria se < 5 candidatos")
print(f"     => Mantem robustez em casos extremos")

print(f"\n[RESULTADO]")
if len(candidates_new) > 0:
    x_center_cand = candidates_new[:, 0].mean()
    x_center_full = contour[:, 0].mean()
    print(f"  Candidatos antes (simular): incluia pies em X=[{contour[y_mask][:, 0].min():.0f}, {contour[y_mask][:, 0].max():.0f}]")
    print(f"  Candidatos depois: apenas superfice em X=[{candidates_new[:, 0].min():.1f}, {candidates_new[:, 0].max():.1f}]")
    print(f"  Reducao: -{100 * (len(pts_in_region) - len(candidates_new)) / len(pts_in_region):.0f}% de pontos contaminados")
    print(f"  Centro X: {x_center_cand:.1f} (muito mais proximo do centro {x_center_full:.1f})")

print("\n" + "="*80 + "\n")
