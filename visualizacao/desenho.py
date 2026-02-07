def desenhar_baseline(canvas, baseline_y, ratio, offset_x, offset_y, 
                      image_width=None, line_params=None):
    # Se não temos a largura original, estimamos pela largura da tela / ratio
    # image_width aqui deve ser a largura NA TELA (nw no main.py)
    if image_width is None:
        width_scr = canvas.winfo_width()
    else:
        width_scr = image_width

    # Largura original da imagem (aproximada)
    w_original = width_scr / ratio

    if line_params is not None:
        vx, vy, x0, y0 = line_params
        
        # 1. Calcular Y nos extremos da imagem ORIGINAL (X=0 e X=w_original)
        # Equação vetorial: P = P0 + t * V  =>  x = x0 + t*vx
        # t = (x - x0) / vx
        
        if abs(vx) > 1e-6:
            t0 = (0 - x0) / vx
            t1 = (w_original - x0) / vx
            
            y_start_orig = y0 + t0 * vy
            y_end_orig = y0 + t1 * vy
        else:
            # Linha vertical (caso raro/erro), mantemos y0
            y_start_orig = y0
            y_end_orig = y0

        # 2. Converter para coordenadas de TELA
        x_start_scr = offset_x
        y_start_scr = offset_y + (y_start_orig * ratio)
        
        x_end_scr = offset_x + width_scr
        y_end_scr = offset_y + (y_end_orig * ratio)
        
        canvas.create_line(x_start_scr, y_start_scr, x_end_scr, y_end_scr, fill="red", width=2)
        
    else:
        # Fallback horizontal
        y_scr = offset_y + (baseline_y * ratio)
        canvas.create_line(offset_x, y_scr, offset_x + width_scr, y_scr, fill="red", width=2)