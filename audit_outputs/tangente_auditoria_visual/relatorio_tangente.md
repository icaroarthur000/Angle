# Auditoria matemática e geométrica da tangente

Escopo: execução do pipeline real sobre as imagens de `imagens_teste`, sem alterar implementação existente.

- Pasta de saída: C:\Users\Icaro Arthur\Documents\Angle\audit_outputs\tangente_auditoria_visual
- Imagens anotadas: C:\Users\Icaro Arthur\Documents\Angle\audit_outputs\tangente_auditoria_visual\visualizacoes
- CSVs: C:\Users\Icaro Arthur\Documents\Angle\audit_outputs\tangente_auditoria_visual\csv

## 30_geo.png

- Imagem analisada: 30_geo.png
- Baseline utilizada: 386.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1148

### Lado esq

- Ponto de contato: [166.0, 386.0]
- Baseline ajustada: 389.730000
- Janela vertical: 205 px
- Altura da gota: 373.000000
- Centro x aproximado: 332.500000
- Quantidade de pontos recebidos pela função: 318
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=241 x=132.000000 y=185.000000
  - ordem=1 index=242 x=132.000000 y=186.000000
  - ordem=2 index=243 x=132.000000 y=187.000000
  - ordem=3 index=244 x=132.000000 y=188.000000
  - ordem=4 index=245 x=132.000000 y=189.000000
  - ordem=5 index=246 x=132.000000 y=190.000000
  - ordem=6 index=247 x=132.000000 y=191.000000
  - ordem=7 index=248 x=131.000000 y=192.000000
  - ordem=8 index=249 x=131.000000 y=193.000000
  - ordem=9 index=250 x=131.000000 y=194.000000
  - ordem=10 index=251 x=131.000000 y=195.000000
  - ordem=11 index=252 x=131.000000 y=196.000000

- Coeficientes do polinômio: a=0.007419, b=-3.665109, c=575.082143
- Derivada dx/dy no contato: 2.062742
- Derivada dy/dx: 0.484792
- RMSE: 24.303950
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/30_geo_audit.png
- CSV contorno: csv/30_geo/30_geo_contorno.csv
- CSV selecionados: csv/30_geo/30_geo_esq_selecionados.csv
- CSV descartados: csv/30_geo/30_geo_esq_descartados.csv
- CSV polyfit: csv/30_geo/30_geo_esq_polyfit.csv
- CSV residuos: csv/30_geo/30_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Lado dir

- Ponto de contato: [499.0, 386.0]
- Baseline ajustada: 389.730000
- Janela vertical: 205 px
- Altura da gota: 373.000000
- Centro x aproximado: 332.500000
- Quantidade de pontos recebidos pela função: 318
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=559 x=333.000000 y=386.000000
  - ordem=1 index=560 x=334.000000 y=386.000000
  - ordem=2 index=561 x=335.000000 y=386.000000
  - ordem=3 index=562 x=336.000000 y=386.000000
  - ordem=4 index=563 x=337.000000 y=386.000000
  - ordem=5 index=564 x=338.000000 y=386.000000
  - ordem=6 index=565 x=339.000000 y=386.000000
  - ordem=7 index=566 x=340.000000 y=386.000000
  - ordem=8 index=567 x=341.000000 y=386.000000
  - ordem=9 index=568 x=342.000000 y=386.000000
  - ordem=10 index=569 x=343.000000 y=386.000000
  - ordem=11 index=570 x=344.000000 y=386.000000

- Coeficientes do polinômio: a=-0.007430, b=3.671244, c=89.274454
- Derivada dx/dy no contato: -2.065056
- Derivada dy/dx: -0.484248
- RMSE: 24.360228
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/30_geo_audit.png
- CSV contorno: csv/30_geo/30_geo_contorno.csv
- CSV selecionados: csv/30_geo/30_geo_dir_selecionados.csv
- CSV descartados: csv/30_geo/30_geo_dir_descartados.csv
- CSV polyfit: csv/30_geo/30_geo_dir_polyfit.csv
- CSV residuos: csv/30_geo/30_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## 50_geo.png

- Imagem analisada: 50_geo.png
- Baseline utilizada: 376.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1145

### Lado esq

- Ponto de contato: [92.0, 376.0]
- Baseline ajustada: 379.290000
- Janela vertical: 180 px
- Altura da gota: 329.000000
- Centro x aproximado: 279.500000
- Quantidade de pontos recebidos pela função: 336
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=221 x=83.000000 y=200.000000
  - ordem=1 index=222 x=83.000000 y=201.000000
  - ordem=2 index=223 x=83.000000 y=202.000000
  - ordem=3 index=224 x=82.000000 y=203.000000
  - ordem=4 index=225 x=82.000000 y=204.000000
  - ordem=5 index=226 x=82.000000 y=205.000000
  - ordem=6 index=227 x=82.000000 y=206.000000
  - ordem=7 index=228 x=82.000000 y=207.000000
  - ordem=8 index=229 x=81.000000 y=208.000000
  - ordem=9 index=230 x=81.000000 y=209.000000
  - ordem=10 index=231 x=81.000000 y=210.000000
  - ordem=11 index=232 x=81.000000 y=211.000000

- Coeficientes do polinômio: a=0.010367, b=-5.493421, c=790.871859
- Derivada dx/dy no contato: 2.302653
- Derivada dy/dx: 0.434282
- RMSE: 36.575448
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/50_geo_audit.png
- CSV contorno: csv/50_geo/50_geo_contorno.csv
- CSV selecionados: csv/50_geo/50_geo_esq_selecionados.csv
- CSV descartados: csv/50_geo/50_geo_esq_descartados.csv
- CSV polyfit: csv/50_geo/50_geo_esq_polyfit.csv
- CSV residuos: csv/50_geo/50_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Lado dir

- Ponto de contato: [467.0, 376.0]
- Baseline ajustada: 379.290000
- Janela vertical: 180 px
- Altura da gota: 329.000000
- Centro x aproximado: 279.500000
- Quantidade de pontos recebidos pela função: 336
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=557 x=280.000000 y=376.000000
  - ordem=1 index=558 x=281.000000 y=376.000000
  - ordem=2 index=559 x=282.000000 y=376.000000
  - ordem=3 index=560 x=283.000000 y=376.000000
  - ordem=4 index=561 x=284.000000 y=376.000000
  - ordem=5 index=562 x=285.000000 y=376.000000
  - ordem=6 index=563 x=286.000000 y=376.000000
  - ordem=7 index=564 x=287.000000 y=376.000000
  - ordem=8 index=565 x=288.000000 y=376.000000
  - ordem=9 index=566 x=289.000000 y=376.000000
  - ordem=10 index=567 x=290.000000 y=376.000000
  - ordem=11 index=568 x=291.000000 y=376.000000

- Coeficientes do polinômio: a=-0.010381, b=5.500525, c=-232.556129
- Derivada dx/dy no contato: -2.306001
- Derivada dy/dx: -0.433651
- RMSE: 36.598009
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/50_geo_audit.png
- CSV contorno: csv/50_geo/50_geo_contorno.csv
- CSV selecionados: csv/50_geo/50_geo_dir_selecionados.csv
- CSV descartados: csv/50_geo/50_geo_dir_descartados.csv
- CSV polyfit: csv/50_geo/50_geo_dir_polyfit.csv
- CSV residuos: csv/50_geo/50_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## 75_geo.png

- Imagem analisada: 75_geo.png
- Baseline utilizada: 303.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1063

### Lado esq

- Ponto de contato: [114.0, 303.0]
- Baseline ajustada: 305.500000
- Janela vertical: 137 px
- Altura da gota: 250.000000
- Centro x aproximado: 316.500000
- Quantidade de pontos recebidos pela função: 331
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=181 x=133.000000 y=169.000000
  - ordem=1 index=182 x=133.000000 y=170.000000
  - ordem=2 index=183 x=132.000000 y=171.000000
  - ordem=3 index=184 x=132.000000 y=172.000000
  - ordem=4 index=185 x=131.000000 y=173.000000
  - ordem=5 index=186 x=131.000000 y=174.000000
  - ordem=6 index=187 x=130.000000 y=175.000000
  - ordem=7 index=188 x=130.000000 y=176.000000
  - ordem=8 index=189 x=129.000000 y=177.000000
  - ordem=9 index=190 x=129.000000 y=178.000000
  - ordem=10 index=191 x=129.000000 y=179.000000
  - ordem=11 index=192 x=128.000000 y=180.000000

- Coeficientes do polinômio: a=0.019428, b=-8.804938, c=1095.554722
- Derivada dx/dy no contato: 2.968182
- Derivada dy/dx: 0.336907
- RMSE: 48.139275
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/75_geo_audit.png
- CSV contorno: csv/75_geo/75_geo_contorno.csv
- CSV selecionados: csv/75_geo/75_geo_esq_selecionados.csv
- CSV descartados: csv/75_geo/75_geo_esq_descartados.csv
- CSV polyfit: csv/75_geo/75_geo_esq_polyfit.csv
- CSV residuos: csv/75_geo/75_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Lado dir

- Ponto de contato: [519.0, 303.0]
- Baseline ajustada: 305.500000
- Janela vertical: 137 px
- Altura da gota: 250.000000
- Centro x aproximado: 316.500000
- Quantidade de pontos recebidos pela função: 332
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=512 x=317.000000 y=303.000000
  - ordem=1 index=513 x=318.000000 y=303.000000
  - ordem=2 index=514 x=319.000000 y=303.000000
  - ordem=3 index=515 x=320.000000 y=303.000000
  - ordem=4 index=516 x=321.000000 y=303.000000
  - ordem=5 index=517 x=322.000000 y=303.000000
  - ordem=6 index=518 x=323.000000 y=303.000000
  - ordem=7 index=519 x=324.000000 y=303.000000
  - ordem=8 index=520 x=325.000000 y=303.000000
  - ordem=9 index=521 x=326.000000 y=303.000000
  - ordem=10 index=522 x=327.000000 y=303.000000
  - ordem=11 index=523 x=328.000000 y=303.000000

- Coeficientes do polinômio: a=-0.019355, b=8.770757, c=-458.443405
- Derivada dx/dy no contato: -2.958185
- Derivada dy/dx: -0.338045
- RMSE: 48.347462
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/75_geo_audit.png
- CSV contorno: csv/75_geo/75_geo_contorno.csv
- CSV selecionados: csv/75_geo/75_geo_dir_selecionados.csv
- CSV descartados: csv/75_geo/75_geo_dir_descartados.csv
- CSV polyfit: csv/75_geo/75_geo_dir_polyfit.csv
- CSV residuos: csv/75_geo/75_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## 100_geo.png

- Imagem analisada: 100_geo.png
- Baseline utilizada: 256.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 1196

### Lado esq

- Ponto de contato: [86.0, 256.0]
- Baseline ajustada: 258.200000
- Janela vertical: 121 px
- Altura da gota: 220.000000
- Centro x aproximado: 351.500000
- Quantidade de pontos recebidos pela função: 384
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=194 x=140.000000 y=138.000000
  - ordem=1 index=195 x=139.000000 y=139.000000
  - ordem=2 index=196 x=138.000000 y=140.000000
  - ordem=3 index=197 x=138.000000 y=141.000000
  - ordem=4 index=198 x=137.000000 y=142.000000
  - ordem=5 index=199 x=136.000000 y=143.000000
  - ordem=6 index=200 x=135.000000 y=144.000000
  - ordem=7 index=201 x=135.000000 y=145.000000
  - ordem=8 index=202 x=134.000000 y=146.000000
  - ordem=9 index=203 x=133.000000 y=147.000000
  - ordem=10 index=204 x=132.000000 y=148.000000
  - ordem=11 index=205 x=132.000000 y=149.000000

- Coeficientes do polinômio: a=0.032337, b=-12.465986, c=1284.541107
- Derivada dx/dy no contato: 4.090744
- Derivada dy/dx: 0.244454
- RMSE: 68.051244
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/100_geo_audit.png
- CSV contorno: csv/100_geo/100_geo_contorno.csv
- CSV selecionados: csv/100_geo/100_geo_esq_selecionados.csv
- CSV descartados: csv/100_geo/100_geo_esq_descartados.csv
- CSV polyfit: csv/100_geo/100_geo_esq_polyfit.csv
- CSV residuos: csv/100_geo/100_geo_esq_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Lado dir

- Ponto de contato: [617.0, 256.0]
- Baseline ajustada: 258.200000
- Janela vertical: 121 px
- Altura da gota: 220.000000
- Centro x aproximado: 351.500000
- Quantidade de pontos recebidos pela função: 384
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=578 x=352.000000 y=256.000000
  - ordem=1 index=579 x=353.000000 y=256.000000
  - ordem=2 index=580 x=354.000000 y=256.000000
  - ordem=3 index=581 x=355.000000 y=256.000000
  - ordem=4 index=582 x=356.000000 y=256.000000
  - ordem=5 index=583 x=357.000000 y=256.000000
  - ordem=6 index=584 x=358.000000 y=256.000000
  - ordem=7 index=585 x=359.000000 y=256.000000
  - ordem=8 index=586 x=360.000000 y=256.000000
  - ordem=9 index=587 x=361.000000 y=256.000000
  - ordem=10 index=588 x=362.000000 y=256.000000
  - ordem=11 index=589 x=363.000000 y=256.000000

- Coeficientes do polinômio: a=-0.032312, b=12.455731, c=-580.569288
- Derivada dx/dy no contato: -4.088066
- Derivada dy/dx: -0.244614
- RMSE: 68.054027
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/100_geo_audit.png
- CSV contorno: csv/100_geo/100_geo_contorno.csv
- CSV selecionados: csv/100_geo/100_geo_dir_selecionados.csv
- CSV descartados: csv/100_geo/100_geo_dir_descartados.csv
- CSV polyfit: csv/100_geo/100_geo_dir_polyfit.csv
- CSV residuos: csv/100_geo/100_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## 130_geo.png

- Imagem analisada: 130_geo.png
- Baseline utilizada: 213.000000
- Função de baseline: floor_seeker_hybrid
- Função de máscara: OTSU
- Pontos do contorno: 733

### Lado esq

- Ponto de contato: [7.0, 213.0]
- Baseline ajustada: 214.560000
- Janela vertical: 85 px
- Altura da gota: 156.000000
- Centro x aproximado: 263.500000
- Quantidade de pontos recebidos pela função: 68
- Status do ajuste: abortou_std_zero

- Pontos usados no polyfit:
  - ordem=0 index=249 x=7.000000 y=213.000000
  - ordem=1 index=250 x=8.000000 y=213.000000
  - ordem=2 index=251 x=9.000000 y=213.000000
  - ordem=3 index=252 x=10.000000 y=213.000000
  - ordem=4 index=253 x=11.000000 y=213.000000
  - ordem=5 index=254 x=12.000000 y=213.000000
  - ordem=6 index=255 x=13.000000 y=213.000000
  - ordem=7 index=256 x=14.000000 y=213.000000
  - ordem=8 index=257 x=15.000000 y=213.000000
  - ordem=9 index=258 x=16.000000 y=213.000000
  - ordem=10 index=259 x=17.000000 y=213.000000
  - ordem=11 index=260 x=18.000000 y=213.000000

- Coeficientes do polinômio: N/A
- Derivada dx/dy no contato: N/A
- Derivada dy/dx: N/A
- RMSE: N/A
- Nota: A funcao real abortou antes do ajuste polinomial por variancia insuficiente nos pontos selecionados.

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

- Ponto de contato: [520.0, 213.0]
- Baseline ajustada: 214.560000
- Janela vertical: 85 px
- Altura da gota: 156.000000
- Centro x aproximado: 263.500000
- Quantidade de pontos recebidos pela função: 149
- Status do ajuste: diagnostico_externo

- Pontos usados no polyfit:
  - ordem=0 index=317 x=455.000000 y=213.000000
  - ordem=1 index=318 x=456.000000 y=213.000000
  - ordem=2 index=319 x=457.000000 y=213.000000
  - ordem=3 index=320 x=458.000000 y=213.000000
  - ordem=4 index=321 x=459.000000 y=213.000000
  - ordem=5 index=322 x=460.000000 y=213.000000
  - ordem=6 index=323 x=461.000000 y=213.000000
  - ordem=7 index=324 x=462.000000 y=213.000000
  - ordem=8 index=325 x=463.000000 y=213.000000
  - ordem=9 index=326 x=464.000000 y=213.000000
  - ordem=10 index=327 x=465.000000 y=213.000000
  - ordem=11 index=328 x=466.000000 y=213.000000

- Coeficientes do polinômio: a=-0.013712, b=4.467293, c=161.873372
- Derivada dx/dy no contato: -1.373919
- Derivada dy/dx: -0.727845
- RMSE: 14.687238
- Nota: A funcao real abortou; o ajuste exibido na auditoria e apenas diagnostico externo com os mesmos pontos.

- Imagem anotada: visualizacoes/130_geo_audit.png
- CSV contorno: csv/130_geo/130_geo_contorno.csv
- CSV selecionados: csv/130_geo/130_geo_dir_selecionados.csv
- CSV descartados: csv/130_geo/130_geo_dir_descartados.csv
- CSV polyfit: csv/130_geo/130_geo_dir_polyfit.csv
- CSV residuos: csv/130_geo/130_geo_dir_residuos.csv

- Conclusões para este lado:
  - Os pontos escolhidos representam corretamente a superfície da gota? PARCIALMENTE
  - Existe algum ponto da base entrando no ajuste? VERIFICAR NO CSV
  - Existe algum ponto espúrio? VERIFICAR NO CSV
  - A tangente visual coincide com a superfície da gota? A VERIFICAR NA IMAGEM
  - A derivada parece coerente? A VERIFICAR
  - O polinômio acompanha bem o contorno? A VERIFICAR
  - O erro parece matemático ou geométrico? A VERIFICAR

### Conclusão da imagem

- A análise da tangente indica que o subconjunto de pontos selecionado não descreve bem a geometria local da gota de forma consistente.
- Nos casos auditados, a função real tende a abortar por variância insuficiente nos pontos do ajuste, ou o ajuste diagnóstico revela uma faixa quase horizontal.

## Conclusão geral

- A matemática do cálculo da tangente não se mostrou robusta para todos os casos da auditoria.
- A seleção de pontos da tangente não representa de forma confiável a superfície local da gota.
- A tangente visual não coincide de modo consistente com a superfície da gota.
- Há inconsistência geométrica observável e, em vários casos, degeneração matemática do ajuste.