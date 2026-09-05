import csv, glob, os

files = glob.glob(r'c:/Users/Icaro Arthur/Documents/Angle/audit_outputs/window_audit_temp/*_window_audit.csv')
for f in files:
    rows = []
    with open(f, newline='', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            rows.append(row)
    image = os.path.basename(f).replace('_window_audit.csv','')
    for lado in ['esq','dir']:
        subset = [r for r in rows if r['lado']==lado and r['mode']=='centered']
        subset = sorted(subset, key=lambda r: int(r['n']))
        print('\n', image, lado)
        prev = None
        for r in subset:
            if prev is None:
                prev = r
                continue
            prev_n = int(prev['n'])
            curr_n = int(r['n'])
            prev_theta = float(prev['theta_tan'])
            curr_theta = float(r['theta_tan'])
            prev_dx = float(prev['dx_dy'])
            curr_dx = float(r['dx_dy'])
            prev_rmse = float(prev['rmse'])
            curr_rmse = float(r['rmse'])
            prev_r2 = float(prev['r2'])
            curr_r2 = float(r['r2'])
            prev_cond = float(prev['cond'])
            curr_cond = float(r['cond'])
            print(f"{prev_n}->{curr_n}: dtheta={curr_theta-prev_theta:.2f}, ddx={curr_dx-prev_dx:.2f}, drmse={curr_rmse-prev_rmse:.3f}, dr2={curr_r2-prev_r2:.3f}, dcond={curr_cond-prev_cond:.2e}")
            prev = r
