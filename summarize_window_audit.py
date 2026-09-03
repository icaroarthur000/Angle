import csv, glob, os, math
from collections import defaultdict

files = glob.glob(r'c:/Users/Icaro Arthur/Documents/Angle/audit_outputs/window_audit_temp/*_window_audit.csv')
for f in files:
    rows = []
    with open(f, newline='', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            rows.append(row)
    image = os.path.basename(f).replace('_window_audit.csv','')
    print('\n==', image, '==')
    for lado in ['esq','dir']:
        subset = [r for r in rows if r['lado']==lado and r['mode']=='centered']
        if not subset:
            continue
        subset = sorted(subset, key=lambda r: (int(r['n']), r['direction']))
        print('lado', lado)
        for r in subset:
            print(' n', r['n'], 'dir', r['direction'], 'theta', round(float(r['theta_tan']),2), 'rmse', round(float(r['rmse']),3), 'r2', round(float(r['r2']),3), 'cond', round(float(r['cond']),1), 'warn', r['warning'])
        print('---')
