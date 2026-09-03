# Auditoria matemática e geométrica da tangente

Escopo: execução do pipeline real sobre as imagens de `imagens_teste`, sem alterar implementação existente.

- Pasta de saída: C:\Users\Icaro Arthur\Documents\Angle\audit_outputs\tangente_auditoria_visual
- Imagens anotadas: C:\Users\Icaro Arthur\Documents\Angle\audit_outputs\tangente_auditoria_visual\visualizacoes
- CSVs: C:\Users\Icaro Arthur\Documents\Angle\audit_outputs\tangente_auditoria_visual\csv

## 30_geo.png

- Imagem analisada: 30_geo.png
- Baseline utilizada: 387.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1150

### Lado esq

- Ponto de contato: [210.96894454300008, 387.0]
- Baseline ajustada: 390.740000
- Janela vertical: 7 px
- Altura da gota: 374.000000
- Centro x aproximado: 332.659172
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=437 x=211.000000 y=378.000000
  - ordem=1 index=438 x=212.000000 y=378.000000
  - ordem=2 index=439 x=213.000000 y=379.000000
  - ordem=3 index=440 x=214.000000 y=380.000000
  - ordem=4 index=441 x=215.000000 y=381.000000
  - ordem=5 index=442 x=216.000000 y=381.000000
  - ordem=6 index=443 x=217.000000 y=382.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: 1.792873
- Derivada dy/dx: 0.557764
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=145.68132774895878

- Imagem anotada: visualizacoes/30_geo_audit.png
- CSV contorno: csv/30_geo/30_geo_contorno.csv
- CSV selecionados: csv/30_geo/30_geo_esq_selecionados.csv
- CSV descartados: csv/30_geo/30_geo_esq_descartados.csv
- CSV polyfit: csv/30_geo/30_geo_esq_polyfit.csv
- CSV residuos: csv/30_geo/30_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Lado dir

- Ponto de contato: [454.3493988929144, 387.0]
- Baseline ajustada: 390.740000
- Janela vertical: 7 px
- Altura da gota: 374.000000
- Centro x aproximado: 332.659172
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=673 x=445.000000 y=384.000000
  - ordem=1 index=674 x=446.000000 y=384.000000
  - ordem=2 index=675 x=447.000000 y=383.000000
  - ordem=3 index=676 x=448.000000 y=382.000000
  - ordem=4 index=677 x=449.000000 y=382.000000
  - ordem=5 index=678 x=450.000000 y=381.000000
  - ordem=6 index=679 x=451.000000 y=380.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: -2.039877
- Derivada dy/dx: -0.490226
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=34.343495836924205

- Imagem anotada: visualizacoes/30_geo_audit.png
- CSV contorno: csv/30_geo/30_geo_contorno.csv
- CSV selecionados: csv/30_geo/30_geo_dir_selecionados.csv
- CSV descartados: csv/30_geo/30_geo_dir_descartados.csv
- CSV polyfit: csv/30_geo/30_geo_dir_polyfit.csv
- CSV residuos: csv/30_geo/30_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## 50_geo.png

- Imagem analisada: 50_geo.png
- Baseline utilizada: 377.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1147

### Lado esq

- Ponto de contato: [120.28381159286822, 377.0]
- Baseline ajustada: 380.300000
- Janela vertical: 7 px
- Altura da gota: 330.000000
- Centro x aproximado: 279.541040
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=394 x=119.000000 y=373.000000
  - ordem=1 index=395 x=120.000000 y=374.000000
  - ordem=2 index=396 x=120.000000 y=375.000000
  - ordem=3 index=397 x=120.000000 y=376.000000
  - ordem=4 index=398 x=120.000000 y=377.000000
  - ordem=5 index=399 x=121.000000 y=377.000000
  - ordem=6 index=400 x=122.000000 y=377.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: 0.511340
- Derivada dy/dx: 1.955645
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=132.8640663967811

- Imagem anotada: visualizacoes/50_geo_audit.png
- CSV contorno: csv/50_geo/50_geo_contorno.csv
- CSV selecionados: csv/50_geo/50_geo_esq_selecionados.csv
- CSV descartados: csv/50_geo/50_geo_esq_descartados.csv
- CSV polyfit: csv/50_geo/50_geo_esq_polyfit.csv
- CSV residuos: csv/50_geo/50_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Lado dir

- Ponto de contato: [438.7982675487727, 377.0]
- Baseline ajustada: 380.300000
- Janela vertical: 7 px
- Altura da gota: 330.000000
- Centro x aproximado: 279.541040
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=713 x=435.000000 y=377.000000
  - ordem=1 index=714 x=436.000000 y=377.000000
  - ordem=2 index=715 x=437.000000 y=377.000000
  - ordem=3 index=716 x=438.000000 y=377.000000
  - ordem=4 index=717 x=439.000000 y=377.000000
  - ordem=5 index=718 x=439.000000 y=376.000000
  - ordem=6 index=719 x=439.000000 y=375.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: -3.000000
- Derivada dy/dx: -0.333333
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=47.1194091510655

- Imagem anotada: visualizacoes/50_geo_audit.png
- CSV contorno: csv/50_geo/50_geo_contorno.csv
- CSV selecionados: csv/50_geo/50_geo_dir_selecionados.csv
- CSV descartados: csv/50_geo/50_geo_dir_descartados.csv
- CSV polyfit: csv/50_geo/50_geo_dir_polyfit.csv
- CSV residuos: csv/50_geo/50_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## 75_geo.png

- Imagem analisada: 75_geo.png
- Baseline utilizada: 304.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1065

### Lado esq

- Ponto de contato: [123.02315673076473, 304.0]
- Baseline ajustada: 306.510000
- Janela vertical: 7 px
- Altura da gota: 251.000000
- Centro x aproximado: 316.591430
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=315 x=120.000000 y=303.000000
  - ordem=1 index=316 x=120.000000 y=304.000000
  - ordem=2 index=317 x=121.000000 y=304.000000
  - ordem=3 index=318 x=122.000000 y=304.000000
  - ordem=4 index=319 x=123.000000 y=304.000000
  - ordem=5 index=320 x=124.000000 y=304.000000
  - ordem=6 index=321 x=125.000000 y=304.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: 2.503897
- Derivada dy/dx: 0.399378
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=116.58198803086952

- Imagem anotada: visualizacoes/75_geo_audit.png
- CSV contorno: csv/75_geo/75_geo_contorno.csv
- CSV selecionados: csv/75_geo/75_geo_esq_selecionados.csv
- CSV descartados: csv/75_geo/75_geo_esq_descartados.csv
- CSV polyfit: csv/75_geo/75_geo_esq_polyfit.csv
- CSV residuos: csv/75_geo/75_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Lado dir

- Ponto de contato: [510.1597029509344, 304.0]
- Baseline ajustada: 306.510000
- Janela vertical: 7 px
- Altura da gota: 251.000000
- Centro x aproximado: 316.591430
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=702 x=506.000000 y=304.000000
  - ordem=1 index=703 x=507.000000 y=304.000000
  - ordem=2 index=704 x=508.000000 y=304.000000
  - ordem=3 index=705 x=509.000000 y=304.000000
  - ordem=4 index=706 x=510.000000 y=304.000000
  - ordem=5 index=707 x=511.000000 y=304.000000
  - ordem=6 index=708 x=512.000000 y=304.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: N/A
- Derivada dy/dx: N/A
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=63.399299379999675

- Imagem anotada: visualizacoes/75_geo_audit.png
- CSV contorno: csv/75_geo/75_geo_contorno.csv
- CSV selecionados: csv/75_geo/75_geo_dir_selecionados.csv
- CSV descartados: csv/75_geo/75_geo_dir_descartados.csv
- CSV polyfit: csv/75_geo/75_geo_dir_polyfit.csv
- CSV residuos: csv/75_geo/75_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## 100_geo.png

- Imagem analisada: 100_geo.png
- Baseline utilizada: 257.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1204

### Lado esq

- Ponto de contato: [90.62190002212017, 257.0]
- Baseline ajustada: 259.210000
- Janela vertical: 7 px
- Altura da gota: 221.000000
- Centro x aproximado: 351.476665
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=317 x=87.000000 y=257.000000
  - ordem=1 index=318 x=88.000000 y=257.000000
  - ordem=2 index=319 x=89.000000 y=257.000000
  - ordem=3 index=320 x=90.000000 y=257.000000
  - ordem=4 index=321 x=91.000000 y=257.000000
  - ordem=5 index=322 x=92.000000 y=257.000000
  - ordem=6 index=323 x=93.000000 y=257.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: N/A
- Derivada dy/dx: N/A
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=102.38199822921092

- Imagem anotada: visualizacoes/100_geo_audit.png
- CSV contorno: csv/100_geo/100_geo_contorno.csv
- CSV selecionados: csv/100_geo/100_geo_esq_selecionados.csv
- CSV descartados: csv/100_geo/100_geo_esq_descartados.csv
- CSV polyfit: csv/100_geo/100_geo_esq_polyfit.csv
- CSV residuos: csv/100_geo/100_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Lado dir

- Ponto de contato: [612.3314297262442, 257.0]
- Baseline ajustada: 259.210000
- Janela vertical: 7 px
- Altura da gota: 221.000000
- Centro x aproximado: 351.476665
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=838 x=608.000000 y=257.000000
  - ordem=1 index=839 x=609.000000 y=257.000000
  - ordem=2 index=840 x=610.000000 y=257.000000
  - ordem=3 index=841 x=611.000000 y=257.000000
  - ordem=4 index=842 x=612.000000 y=257.000000
  - ordem=5 index=843 x=613.000000 y=257.000000
  - ordem=6 index=844 x=614.000000 y=257.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: N/A
- Derivada dy/dx: N/A
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=77.61691905193399

- Imagem anotada: visualizacoes/100_geo_audit.png
- CSV contorno: csv/100_geo/100_geo_contorno.csv
- CSV selecionados: csv/100_geo/100_geo_dir_selecionados.csv
- CSV descartados: csv/100_geo/100_geo_dir_descartados.csv
- CSV polyfit: csv/100_geo/100_geo_dir_polyfit.csv
- CSV residuos: csv/100_geo/100_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## 130_geo.png

- Imagem analisada: 130_geo.png
- Baseline utilizada: 221.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1121

### Lado esq

- Ponto de contato: [284.0, 221.0]
- Baseline ajustada: 222.640000
- Janela vertical: 7 px
- Altura da gota: 164.000000
- Centro x aproximado: 387.887866
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=522 x=280.000000 y=221.000000
  - ordem=1 index=523 x=281.000000 y=221.000000
  - ordem=2 index=524 x=282.000000 y=221.000000
  - ordem=3 index=525 x=283.000000 y=221.000000
  - ordem=4 index=526 x=284.000000 y=221.000000
  - ordem=5 index=527 x=285.000000 y=221.000000
  - ordem=6 index=528 x=286.000000 y=221.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: N/A
- Derivada dy/dx: N/A
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=7.960160782221266

- Imagem anotada: visualizacoes/130_geo_audit.png
- CSV contorno: csv/130_geo/130_geo_contorno.csv
- CSV selecionados: csv/130_geo/130_geo_esq_selecionados.csv
- CSV descartados: csv/130_geo/130_geo_esq_descartados.csv
- CSV polyfit: csv/130_geo/130_geo_esq_polyfit.csv
- CSV residuos: csv/130_geo/130_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Lado dir

- Ponto de contato: [491.77573152771663, 221.0]
- Baseline ajustada: 222.640000
- Janela vertical: 7 px
- Altura da gota: 164.000000
- Centro x aproximado: 387.887866
- Quantidade de pontos recebidos pela função: 7
- Status do ajuste: producao

- Pontos usados no polyfit:
  - ordem=0 index=730 x=488.000000 y=221.000000
  - ordem=1 index=731 x=489.000000 y=221.000000
  - ordem=2 index=732 x=490.000000 y=221.000000
  - ordem=3 index=733 x=491.000000 y=221.000000
  - ordem=4 index=734 x=492.000000 y=221.000000
  - ordem=5 index=735 x=493.000000 y=221.000000
  - ordem=6 index=736 x=494.000000 y=221.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: N/A
- Derivada dy/dx: N/A
- RMSE: N/A
- Nota: metodo=tangente_polynomial; angulo_producao=80.58515377696054

- Imagem anotada: visualizacoes/130_geo_audit.png
- CSV contorno: csv/130_geo/130_geo_contorno.csv
- CSV selecionados: csv/130_geo/130_geo_dir_selecionados.csv
- CSV descartados: csv/130_geo/130_geo_dir_descartados.csv
- CSV polyfit: csv/130_geo/130_geo_dir_polyfit.csv
- CSV residuos: csv/130_geo/130_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? NÃO
  - Existe algum ponto da base entrando no ajuste? SIM
  - Existe algum ponto espúrio? SIM
  - A tangente visual coincide com a superfície da gota? NÃO
  - A derivada parece coerente? NÃO
  - O polinômio acompanha bem o contorno? NÃO
  - O erro parece matemático ou geométrico? Geométrico com degeneração matemática

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## Conclusão geral

- A matemática do cálculo da tangente não se mostrou robusta para todos os casos da auditoria.
- A seleção de pontos da tangente não representa de forma confiável a superfície local da gota.
- A tangente visual não coincide de modo consistente com a superfície da gota.
- Há inconsistência geométrica observável e, em vários casos, degeneração matemática do ajuste.