# Auditoria do contorno e ultimo pixel

Imagens processadas: 100_geo.png, 130_geo.png, 30_geo.png, 50_geo.png, 75_geo.png

## 100_geo.png
- metodo de segmentacao: OTSU
- fallback Canny no contorno: NAO
- margins: top=1 side=6 bottom=2
- baseline_y: 256.00
- mask_binary: pontos=1664 y_min=36.0 y_max=314.0 gap=-58.0
- after_substrate_removal: pontos=1196 y_min=36.0 y_max=256.0 gap=0.0
- processed_before_final_filter: pontos=1196 y_min=36.0 y_max=256.0 gap=0.0
- after_final_filter: pontos=1196 y_min=36.0 y_max=256.0 gap=0.0
- visual: visualizacoes/100_geo_audit.png

## 130_geo.png
- metodo de segmentacao: OTSU
- fallback Canny no contorno: NAO
- margins: top=1 side=6 bottom=2
- baseline_y: nan
- mask_binary: pontos=1238 y_min=57.0 y_max=221.0 gap=nan
- after_substrate_removal: pontos=1238 y_min=57.0 y_max=221.0 gap=nan
- processed_before_final_filter: pontos=0 y_min=None y_max=None gap=None
- after_final_filter: pontos=0 y_min=None y_max=None gap=None
- visual: visualizacoes/130_geo_audit.png

## 30_geo.png
- metodo de segmentacao: OTSU
- fallback Canny no contorno: NAO
- margins: top=1 side=8 bottom=2
- baseline_y: 386.00
- mask_binary: pontos=2198 y_min=13.0 y_max=447.0 gap=-61.0
- after_substrate_removal: pontos=1148 y_min=13.0 y_max=386.0 gap=0.0
- processed_before_final_filter: pontos=1148 y_min=13.0 y_max=386.0 gap=0.0
- after_final_filter: pontos=1148 y_min=13.0 y_max=386.0 gap=0.0
- visual: visualizacoes/30_geo_audit.png

## 50_geo.png
- metodo de segmentacao: OTSU
- fallback Canny no contorno: NAO
- margins: top=1 side=8 bottom=2
- baseline_y: 376.00
- mask_binary: pontos=1705 y_min=47.0 y_max=439.0 gap=-63.0
- after_substrate_removal: pontos=1145 y_min=47.0 y_max=376.0 gap=0.0
- processed_before_final_filter: pontos=1145 y_min=47.0 y_max=376.0 gap=0.0
- after_final_filter: pontos=1145 y_min=47.0 y_max=376.0 gap=0.0
- visual: visualizacoes/50_geo_audit.png

## 75_geo.png
- metodo de segmentacao: OTSU
- fallback Canny no contorno: NAO
- margins: top=1 side=7 bottom=2
- baseline_y: 303.00
- mask_binary: pontos=1633 y_min=53.0 y_max=369.0 gap=-66.0
- after_substrate_removal: pontos=1063 y_min=53.0 y_max=303.0 gap=0.0
- processed_before_final_filter: pontos=1063 y_min=53.0 y_max=303.0 gap=0.0
- after_final_filter: pontos=1063 y_min=53.0 y_max=303.0 gap=0.0
- visual: visualizacoes/75_geo_audit.png
