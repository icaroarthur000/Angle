import sys
import numpy as np
import cv2

sys.path.insert(0, '.')
from processamento_imagem import filtros, contorno
from linha_base import linha_base

IMGS = [
    ('30_geo', 'imagens_teste/30_geo.png'),
    ('50_geo', 'imagens_teste/50_geo.png'),
    ('75_geo', 'imagens_teste/75_geo.png'),
    ('100_geo', 'imagens_teste/100_geo.png'),
    ('130_geo', 'imagens_teste/130_geo.png'),
]

ROI_BOTTOM_EXCLUDE = 0.02
ROI_TOP_EXCLUDE = 0.20
POLYFIT_DEGREE = 2
MIN_POINTS_FOR_FIT = 8


def inspect(name, path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask, _ = filtros.aplicar_multi_threshold(img)
    _, gota = contorno.extrair_mascara_gota(mask, img_gray=gray)
    res = linha_base.detectar_baseline_hibrida(gota, debug=False)
    baseline_y = float(res['baseline_y'])
    y_vals = gota[:, 1]
    y_min, y_max = float(np.min(y_vals)), float(np.max(y_vals))
    height = y_max - y_min
    y_roi_bottom = y_max - ROI_BOTTOM_EXCLUDE * height
    y_roi_top = y_min + ROI_TOP_EXCLUDE * height
    margem_base = max(6.0, 0.06 * height)
    y_roi_bottom = min(y_roi_bottom, float(baseline_y) - margem_base)
    if y_roi_bottom <= y_roi_top:
        y_roi_bottom = float(baseline_y) - 2.0
    roi_mask = (y_vals >= y_roi_top) & (y_vals <= y_roi_bottom)
    roi_pts = gota[roi_mask]
    x_center = float(np.mean(gota[:, 0]))
    print(f'== {name} ==')
    print('baseline_y', baseline_y)
    print('roi', y_roi_top, y_roi_bottom, 'n', len(roi_pts))
    for side_name, side_pts in [('esq', roi_pts[roi_pts[:, 0] < x_center]), ('dir', roi_pts[roi_pts[:, 0] >= x_center])]:
        print(' ', side_name, 'n', len(side_pts))
        if len(side_pts) >= MIN_POINTS_FOR_FIT:
            coeffs = np.polyfit(side_pts[:, 1], side_pts[:, 0], POLYFIT_DEGREE)
            poly = np.poly1d(coeffs)
            x_contact = float(poly(baseline_y))
            print('   coeffs', coeffs, 'x_contact', x_contact)
        else:
            print('   too few for fit')
    adaptive_tol = max(5.0, 0.15 * height)
    near_baseline = gota[gota[:, 1] >= (y_max - adaptive_tol)]
    left = near_baseline[near_baseline[:, 0] <= x_center]
    right = near_baseline[near_baseline[:, 0] > x_center]
    x_esq = float(np.min(left[:, 0])) if len(left) > 0 else float(np.min(near_baseline[:, 0]))
    x_dir = float(np.max(right[:, 0])) if len(right) > 0 else float(np.max(near_baseline[:, 0]))
    print('  fallback near-baseline', x_esq, x_dir)
    print('  production', res['p_esq'], res['p_dir'])

for item in IMGS:
    inspect(*item)
