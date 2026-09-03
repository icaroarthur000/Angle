import csv, glob, os, math
files = glob.glob(r'c:/Users/Icaro Arthur/Documents/Angle/audit_outputs/window_audit_temp/*_window_audit.csv')
for f in files:
    rows = []
    with open(f, newline='', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            rows.append(row)
    print('\nFILE', os.path.basename(f))
    for lado in ['esq','dir']:
        subset = [r for r in rows if r['lado']==lado]
        if not subset:
            continue
        print('lado', lado)
        for n in sorted({int(r['n']) for r in subset}):
            vals = [r for r in subset if int(r['n'])==n]
            print(' n', n, 'modes', len(vals), 'theta', [round(float(r['theta_tan']),2) for r in vals[:10]])
        print('---')
