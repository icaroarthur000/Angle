# Relatório de auditoria das funções

Este relatório foi gerado executando o pipeline real do projeto sobre as imagens em `imagens_teste` sem alterar a lógica de cálculo.

## Resumo

- Imagens processadas: 5
- Eventos capturados: 15

## Imagem: 100_geo

### Lado: esq

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 1196
- ponto de contato recebido: [86.0, 256.0]
- baseline_y: 256.0
- baseline_ajustada: 258.2
- lado solicitado: esq
- largura da região: 121 px
- altura da gota: 220.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 331.00 | 36.00 | 329.28 | 222.20 | NÃO | fora da faixa vertical |
| 1 | 330.00 | 37.00 | 327.87 | 221.20 | NÃO | fora da faixa vertical |
| 2 | 329.00 | 37.00 | 327.12 | 221.20 | NÃO | fora da faixa vertical |
| 3 | 328.00 | 37.00 | 326.38 | 221.20 | NÃO | fora da faixa vertical |
| 4 | 327.00 | 37.00 | 325.64 | 221.20 | NÃO | fora da faixa vertical |
| 5 | 326.00 | 37.00 | 324.90 | 221.20 | NÃO | fora da faixa vertical |
| 6 | 325.00 | 37.00 | 324.16 | 221.20 | NÃO | fora da faixa vertical |
| 7 | 324.00 | 37.00 | 323.43 | 221.20 | NÃO | fora da faixa vertical |
| 8 | 323.00 | 37.00 | 322.69 | 221.20 | NÃO | fora da faixa vertical |
| 9 | 322.00 | 37.00 | 321.96 | 221.20 | NÃO | fora da faixa vertical |
| 10 | 321.00 | 38.00 | 320.54 | 220.20 | NÃO | fora da faixa vertical |
| 11 | 320.00 | 38.00 | 319.81 | 220.20 | NÃO | fora da faixa vertical |
| 12 | 319.00 | 38.00 | 319.08 | 220.20 | NÃO | fora da faixa vertical |
| 13 | 318.00 | 38.00 | 318.35 | 220.20 | NÃO | fora da faixa vertical |
| 14 | 317.00 | 38.00 | 317.62 | 220.20 | NÃO | fora da faixa vertical |
| 15 | 316.00 | 38.00 | 316.90 | 220.20 | NÃO | fora da faixa vertical |
| 16 | 315.00 | 38.00 | 316.17 | 220.20 | NÃO | fora da faixa vertical |
| 17 | 314.00 | 38.00 | 315.45 | 220.20 | NÃO | fora da faixa vertical |
| 18 | 313.00 | 38.00 | 314.73 | 220.20 | NÃO | fora da faixa vertical |
| 19 | 312.00 | 39.00 | 313.31 | 219.20 | NÃO | fora da faixa vertical |
| 20 | 311.00 | 39.00 | 312.59 | 219.20 | NÃO | fora da faixa vertical |
| 21 | 310.00 | 39.00 | 311.87 | 219.20 | NÃO | fora da faixa vertical |
| 22 | 309.00 | 39.00 | 311.16 | 219.20 | NÃO | fora da faixa vertical |
| 23 | 308.00 | 39.00 | 310.44 | 219.20 | NÃO | fora da faixa vertical |
| 24 | 307.00 | 39.00 | 309.73 | 219.20 | NÃO | fora da faixa vertical |
| 25 | 306.00 | 39.00 | 309.01 | 219.20 | NÃO | fora da faixa vertical |
| 26 | 305.00 | 40.00 | 307.60 | 218.20 | NÃO | fora da faixa vertical |
| 27 | 304.00 | 40.00 | 306.89 | 218.20 | NÃO | fora da faixa vertical |
| 28 | 303.00 | 40.00 | 306.18 | 218.20 | NÃO | fora da faixa vertical |
| 29 | 302.00 | 40.00 | 305.47 | 218.20 | NÃO | fora da faixa vertical |
| 30 | 301.00 | 40.00 | 304.76 | 218.20 | NÃO | fora da faixa vertical |
| 31 | 300.00 | 41.00 | 303.35 | 217.20 | NÃO | fora da faixa vertical |
| 32 | 299.00 | 41.00 | 302.65 | 217.20 | NÃO | fora da faixa vertical |
| 33 | 298.00 | 41.00 | 301.94 | 217.20 | NÃO | fora da faixa vertical |
| 34 | 297.00 | 41.00 | 301.24 | 217.20 | NÃO | fora da faixa vertical |
| 35 | 296.00 | 41.00 | 300.54 | 217.20 | NÃO | fora da faixa vertical |
| 36 | 295.00 | 42.00 | 299.13 | 216.20 | NÃO | fora da faixa vertical |
| 37 | 294.00 | 42.00 | 298.43 | 216.20 | NÃO | fora da faixa vertical |
| 38 | 293.00 | 42.00 | 297.73 | 216.20 | NÃO | fora da faixa vertical |
| 39 | 292.00 | 42.00 | 297.04 | 216.20 | NÃO | fora da faixa vertical |
| 40 | 291.00 | 42.00 | 296.35 | 216.20 | NÃO | fora da faixa vertical |
| 41 | 290.00 | 43.00 | 294.93 | 215.20 | NÃO | fora da faixa vertical |
| 42 | 289.00 | 43.00 | 294.24 | 215.20 | NÃO | fora da faixa vertical |
| 43 | 288.00 | 43.00 | 293.55 | 215.20 | NÃO | fora da faixa vertical |
| 44 | 287.00 | 43.00 | 292.87 | 215.20 | NÃO | fora da faixa vertical |
| 45 | 286.00 | 44.00 | 291.45 | 214.20 | NÃO | fora da faixa vertical |
| 46 | 285.00 | 44.00 | 290.77 | 214.20 | NÃO | fora da faixa vertical |
| 47 | 284.00 | 44.00 | 290.08 | 214.20 | NÃO | fora da faixa vertical |
| 48 | 283.00 | 44.00 | 289.40 | 214.20 | NÃO | fora da faixa vertical |
| 49 | 282.00 | 45.00 | 287.99 | 213.20 | NÃO | fora da faixa vertical |
| 50 | 281.00 | 45.00 | 287.31 | 213.20 | NÃO | fora da faixa vertical |
| 51 | 280.00 | 45.00 | 286.63 | 213.20 | NÃO | fora da faixa vertical |
| 52 | 279.00 | 46.00 | 285.22 | 212.20 | NÃO | fora da faixa vertical |
| 53 | 278.00 | 46.00 | 284.54 | 212.20 | NÃO | fora da faixa vertical |
| 54 | 277.00 | 46.00 | 283.87 | 212.20 | NÃO | fora da faixa vertical |
| 55 | 276.00 | 47.00 | 282.46 | 211.20 | NÃO | fora da faixa vertical |
| 56 | 275.00 | 47.00 | 281.78 | 211.20 | NÃO | fora da faixa vertical |
| 57 | 274.00 | 47.00 | 281.11 | 211.20 | NÃO | fora da faixa vertical |
| 58 | 273.00 | 47.00 | 280.45 | 211.20 | NÃO | fora da faixa vertical |
| 59 | 272.00 | 48.00 | 279.03 | 210.20 | NÃO | fora da faixa vertical |
| 60 | 271.00 | 48.00 | 278.37 | 210.20 | NÃO | fora da faixa vertical |
| 61 | 270.00 | 48.00 | 277.70 | 210.20 | NÃO | fora da faixa vertical |
| 62 | 269.00 | 49.00 | 276.29 | 209.20 | NÃO | fora da faixa vertical |
| 63 | 268.00 | 49.00 | 275.63 | 209.20 | NÃO | fora da faixa vertical |
| 64 | 267.00 | 49.00 | 274.97 | 209.20 | NÃO | fora da faixa vertical |
| 65 | 266.00 | 49.00 | 274.32 | 209.20 | NÃO | fora da faixa vertical |
| 66 | 265.00 | 50.00 | 272.90 | 208.20 | NÃO | fora da faixa vertical |
| 67 | 264.00 | 50.00 | 272.25 | 208.20 | NÃO | fora da faixa vertical |
| 68 | 263.00 | 51.00 | 270.84 | 207.20 | NÃO | fora da faixa vertical |
| 69 | 262.00 | 51.00 | 270.19 | 207.20 | NÃO | fora da faixa vertical |
| 70 | 261.00 | 51.00 | 269.54 | 207.20 | NÃO | fora da faixa vertical |
| 71 | 260.00 | 52.00 | 268.13 | 206.20 | NÃO | fora da faixa vertical |
| 72 | 259.00 | 52.00 | 267.48 | 206.20 | NÃO | fora da faixa vertical |
| 73 | 258.00 | 52.00 | 266.83 | 206.20 | NÃO | fora da faixa vertical |
| 74 | 257.00 | 53.00 | 265.42 | 205.20 | NÃO | fora da faixa vertical |
| 75 | 256.00 | 53.00 | 264.78 | 205.20 | NÃO | fora da faixa vertical |
| 76 | 255.00 | 53.00 | 264.14 | 205.20 | NÃO | fora da faixa vertical |
| 77 | 254.00 | 54.00 | 262.73 | 204.20 | NÃO | fora da faixa vertical |
| 78 | 253.00 | 54.00 | 262.09 | 204.20 | NÃO | fora da faixa vertical |
| 79 | 252.00 | 55.00 | 260.69 | 203.20 | NÃO | fora da faixa vertical |
| 80 | 251.00 | 55.00 | 260.05 | 203.20 | NÃO | fora da faixa vertical |
| 81 | 250.00 | 55.00 | 259.42 | 203.20 | NÃO | fora da faixa vertical |
| 82 | 249.00 | 56.00 | 258.01 | 202.20 | NÃO | fora da faixa vertical |
| 83 | 248.00 | 56.00 | 257.38 | 202.20 | NÃO | fora da faixa vertical |
| 84 | 247.00 | 56.00 | 256.75 | 202.20 | NÃO | fora da faixa vertical |
| 85 | 246.00 | 57.00 | 255.34 | 201.20 | NÃO | fora da faixa vertical |
| 86 | 245.00 | 57.00 | 254.72 | 201.20 | NÃO | fora da faixa vertical |
| 87 | 244.00 | 58.00 | 253.31 | 200.20 | NÃO | fora da faixa vertical |
| 88 | 243.00 | 58.00 | 252.69 | 200.20 | NÃO | fora da faixa vertical |
| 89 | 242.00 | 59.00 | 251.29 | 199.20 | NÃO | fora da faixa vertical |
| 90 | 241.00 | 59.00 | 250.67 | 199.20 | NÃO | fora da faixa vertical |
| 91 | 240.00 | 60.00 | 249.26 | 198.20 | NÃO | fora da faixa vertical |
| 92 | 239.00 | 60.00 | 248.65 | 198.20 | NÃO | fora da faixa vertical |
| 93 | 238.00 | 61.00 | 247.24 | 197.20 | NÃO | fora da faixa vertical |
| 94 | 237.00 | 61.00 | 246.63 | 197.20 | NÃO | fora da faixa vertical |
| 95 | 236.00 | 62.00 | 245.23 | 196.20 | NÃO | fora da faixa vertical |
| 96 | 235.00 | 62.00 | 244.62 | 196.20 | NÃO | fora da faixa vertical |
| 97 | 234.00 | 63.00 | 243.21 | 195.20 | NÃO | fora da faixa vertical |
| 98 | 233.00 | 63.00 | 242.61 | 195.20 | NÃO | fora da faixa vertical |
| 99 | 232.00 | 64.00 | 241.21 | 194.20 | NÃO | fora da faixa vertical |
| 100 | 231.00 | 64.00 | 240.60 | 194.20 | NÃO | fora da faixa vertical |
| 101 | 230.00 | 65.00 | 239.20 | 193.20 | NÃO | fora da faixa vertical |
| 102 | 229.00 | 65.00 | 238.60 | 193.20 | NÃO | fora da faixa vertical |
| 103 | 228.00 | 66.00 | 237.20 | 192.20 | NÃO | fora da faixa vertical |
| 104 | 227.00 | 66.00 | 236.60 | 192.20 | NÃO | fora da faixa vertical |
| 105 | 226.00 | 67.00 | 235.20 | 191.20 | NÃO | fora da faixa vertical |
| 106 | 225.00 | 67.00 | 234.61 | 191.20 | NÃO | fora da faixa vertical |
| 107 | 224.00 | 68.00 | 233.21 | 190.20 | NÃO | fora da faixa vertical |
| 108 | 223.00 | 68.00 | 232.62 | 190.20 | NÃO | fora da faixa vertical |
| 109 | 222.00 | 69.00 | 231.22 | 189.20 | NÃO | fora da faixa vertical |
| 110 | 221.00 | 69.00 | 230.64 | 189.20 | NÃO | fora da faixa vertical |
| 111 | 220.00 | 70.00 | 229.24 | 188.20 | NÃO | fora da faixa vertical |
| 112 | 219.00 | 71.00 | 227.85 | 187.20 | NÃO | fora da faixa vertical |
| 113 | 218.00 | 71.00 | 227.26 | 187.20 | NÃO | fora da faixa vertical |
| 114 | 217.00 | 72.00 | 225.87 | 186.20 | NÃO | fora da faixa vertical |
| 115 | 216.00 | 72.00 | 225.29 | 186.20 | NÃO | fora da faixa vertical |
| 116 | 215.00 | 73.00 | 223.90 | 185.20 | NÃO | fora da faixa vertical |
| 117 | 214.00 | 73.00 | 223.32 | 185.20 | NÃO | fora da faixa vertical |
| 118 | 213.00 | 74.00 | 221.93 | 184.20 | NÃO | fora da faixa vertical |
| 119 | 212.00 | 74.00 | 221.36 | 184.20 | NÃO | fora da faixa vertical |
| 120 | 211.00 | 75.00 | 219.97 | 183.20 | NÃO | fora da faixa vertical |
| 121 | 210.00 | 76.00 | 218.58 | 182.20 | NÃO | fora da faixa vertical |
| 122 | 209.00 | 76.00 | 218.01 | 182.20 | NÃO | fora da faixa vertical |
| 123 | 208.00 | 77.00 | 216.62 | 181.20 | NÃO | fora da faixa vertical |
| 124 | 207.00 | 78.00 | 215.23 | 180.20 | NÃO | fora da faixa vertical |
| 125 | 206.00 | 78.00 | 214.67 | 180.20 | NÃO | fora da faixa vertical |
| 126 | 205.00 | 79.00 | 213.28 | 179.20 | NÃO | fora da faixa vertical |
| 127 | 204.00 | 80.00 | 211.90 | 178.20 | NÃO | fora da faixa vertical |
| 128 | 203.00 | 80.00 | 211.34 | 178.20 | NÃO | fora da faixa vertical |
| 129 | 202.00 | 81.00 | 209.95 | 177.20 | NÃO | fora da faixa vertical |
| 130 | 201.00 | 82.00 | 208.57 | 176.20 | NÃO | fora da faixa vertical |
| 131 | 200.00 | 82.00 | 208.02 | 176.20 | NÃO | fora da faixa vertical |
| 132 | 199.00 | 83.00 | 206.63 | 175.20 | NÃO | fora da faixa vertical |
| 133 | 198.00 | 84.00 | 205.25 | 174.20 | NÃO | fora da faixa vertical |
| 134 | 197.00 | 84.00 | 204.71 | 174.20 | NÃO | fora da faixa vertical |
| 135 | 196.00 | 85.00 | 203.32 | 173.20 | NÃO | fora da faixa vertical |
| 136 | 195.00 | 86.00 | 201.94 | 172.20 | NÃO | fora da faixa vertical |
| 137 | 194.00 | 86.00 | 201.41 | 172.20 | NÃO | fora da faixa vertical |
| 138 | 193.00 | 87.00 | 200.02 | 171.20 | NÃO | fora da faixa vertical |
| 139 | 192.00 | 88.00 | 198.65 | 170.20 | NÃO | fora da faixa vertical |
| 140 | 191.00 | 88.00 | 198.11 | 170.20 | NÃO | fora da faixa vertical |
| 141 | 190.00 | 89.00 | 196.74 | 169.20 | NÃO | fora da faixa vertical |
| 142 | 189.00 | 90.00 | 195.36 | 168.20 | NÃO | fora da faixa vertical |
| 143 | 188.00 | 91.00 | 193.98 | 167.20 | NÃO | fora da faixa vertical |
| 144 | 187.00 | 92.00 | 192.61 | 166.20 | NÃO | fora da faixa vertical |
| 145 | 186.00 | 92.00 | 192.08 | 166.20 | NÃO | fora da faixa vertical |
| 146 | 185.00 | 93.00 | 190.71 | 165.20 | NÃO | fora da faixa vertical |
| 147 | 184.00 | 94.00 | 189.34 | 164.20 | NÃO | fora da faixa vertical |
| 148 | 183.00 | 95.00 | 187.96 | 163.20 | NÃO | fora da faixa vertical |
| 149 | 182.00 | 96.00 | 186.59 | 162.20 | NÃO | fora da faixa vertical |
| 150 | 181.00 | 96.00 | 186.08 | 162.20 | NÃO | fora da faixa vertical |
| 151 | 180.00 | 97.00 | 184.71 | 161.20 | NÃO | fora da faixa vertical |
| 152 | 179.00 | 98.00 | 183.34 | 160.20 | NÃO | fora da faixa vertical |
| 153 | 178.00 | 99.00 | 181.97 | 159.20 | NÃO | fora da faixa vertical |
| 154 | 177.00 | 100.00 | 180.60 | 158.20 | NÃO | fora da faixa vertical |
| 155 | 176.00 | 100.00 | 180.10 | 158.20 | NÃO | fora da faixa vertical |
| 156 | 175.00 | 101.00 | 178.73 | 157.20 | NÃO | fora da faixa vertical |
| 157 | 174.00 | 102.00 | 177.37 | 156.20 | NÃO | fora da faixa vertical |
| 158 | 173.00 | 103.00 | 176.01 | 155.20 | NÃO | fora da faixa vertical |
| 159 | 172.00 | 104.00 | 174.64 | 154.20 | NÃO | fora da faixa vertical |
| 160 | 171.00 | 105.00 | 173.28 | 153.20 | NÃO | fora da faixa vertical |
| 161 | 170.00 | 106.00 | 171.92 | 152.20 | NÃO | fora da faixa vertical |
| 162 | 169.00 | 107.00 | 170.56 | 151.20 | NÃO | fora da faixa vertical |
| 163 | 168.00 | 108.00 | 169.20 | 150.20 | NÃO | fora da faixa vertical |
| 164 | 167.00 | 109.00 | 167.84 | 149.20 | NÃO | fora da faixa vertical |
| 165 | 166.00 | 110.00 | 166.48 | 148.20 | NÃO | fora da faixa vertical |
| 166 | 165.00 | 110.00 | 166.00 | 148.20 | NÃO | fora da faixa vertical |
| 167 | 164.00 | 111.00 | 164.65 | 147.20 | NÃO | fora da faixa vertical |
| 168 | 163.00 | 112.00 | 163.29 | 146.20 | NÃO | fora da faixa vertical |
| 169 | 162.00 | 113.00 | 161.94 | 145.20 | NÃO | fora da faixa vertical |
| 170 | 161.00 | 114.00 | 160.59 | 144.20 | NÃO | fora da faixa vertical |
| 171 | 160.00 | 115.00 | 159.24 | 143.20 | NÃO | fora da faixa vertical |
| 172 | 159.00 | 116.00 | 157.89 | 142.20 | NÃO | fora da faixa vertical |
| 173 | 158.00 | 117.00 | 156.54 | 141.20 | NÃO | fora da faixa vertical |
| 174 | 158.00 | 118.00 | 155.65 | 140.20 | NÃO | fora da faixa vertical |
| 175 | 157.00 | 119.00 | 154.30 | 139.20 | NÃO | fora da faixa vertical |
| 176 | 156.00 | 120.00 | 152.96 | 138.20 | NÃO | fora da faixa vertical |
| 177 | 155.00 | 121.00 | 151.61 | 137.20 | NÃO | fora da faixa vertical |
| 178 | 154.00 | 122.00 | 150.27 | 136.20 | NÃO | fora da faixa vertical |
| 179 | 153.00 | 123.00 | 148.92 | 135.20 | NÃO | fora da faixa vertical |
| 180 | 152.00 | 124.00 | 147.58 | 134.20 | NÃO | fora da faixa vertical |
| 181 | 151.00 | 125.00 | 146.24 | 133.20 | NÃO | fora da faixa vertical |
| 182 | 150.00 | 126.00 | 144.90 | 132.20 | NÃO | fora da faixa vertical |
| 183 | 149.00 | 127.00 | 143.56 | 131.20 | NÃO | fora da faixa vertical |
| 184 | 148.00 | 128.00 | 142.23 | 130.20 | NÃO | fora da faixa vertical |
| 185 | 147.00 | 129.00 | 140.89 | 129.20 | NÃO | fora da faixa vertical |
| 186 | 146.00 | 130.00 | 139.56 | 128.20 | NÃO | fora da faixa vertical |
| 187 | 146.00 | 131.00 | 138.65 | 127.20 | NÃO | fora da faixa vertical |
| 188 | 145.00 | 132.00 | 137.32 | 126.20 | NÃO | fora da faixa vertical |
| 189 | 144.00 | 133.00 | 135.99 | 125.20 | NÃO | fora da faixa vertical |
| 190 | 143.00 | 134.00 | 134.66 | 124.20 | NÃO | fora da faixa vertical |
| 191 | 142.00 | 135.00 | 133.33 | 123.20 | NÃO | fora da faixa vertical |
| 192 | 142.00 | 136.00 | 132.42 | 122.20 | NÃO | fora da faixa vertical |
| 193 | 141.00 | 137.00 | 131.10 | 121.20 | NÃO | fora da faixa vertical |
| 194 | 140.00 | 138.00 | 129.77 | 120.20 | SIM | dentro da janela vertical e do lado solicitado |
| 195 | 139.00 | 139.00 | 128.44 | 119.20 | SIM | dentro da janela vertical e do lado solicitado |
| 196 | 138.00 | 140.00 | 127.12 | 118.20 | SIM | dentro da janela vertical e do lado solicitado |
| 197 | 138.00 | 141.00 | 126.21 | 117.20 | SIM | dentro da janela vertical e do lado solicitado |
| 198 | 137.00 | 142.00 | 124.89 | 116.20 | SIM | dentro da janela vertical e do lado solicitado |
| 199 | 136.00 | 143.00 | 123.57 | 115.20 | SIM | dentro da janela vertical e do lado solicitado |
| 200 | 135.00 | 144.00 | 122.25 | 114.20 | SIM | dentro da janela vertical e do lado solicitado |
| 201 | 135.00 | 145.00 | 121.33 | 113.20 | SIM | dentro da janela vertical e do lado solicitado |
| 202 | 134.00 | 146.00 | 120.02 | 112.20 | SIM | dentro da janela vertical e do lado solicitado |
| 203 | 133.00 | 147.00 | 118.70 | 111.20 | SIM | dentro da janela vertical e do lado solicitado |
| 204 | 132.00 | 148.00 | 117.39 | 110.20 | SIM | dentro da janela vertical e do lado solicitado |
| 205 | 132.00 | 149.00 | 116.47 | 109.20 | SIM | dentro da janela vertical e do lado solicitado |
| 206 | 131.00 | 150.00 | 115.16 | 108.20 | SIM | dentro da janela vertical e do lado solicitado |
| 207 | 130.00 | 151.00 | 113.85 | 107.20 | SIM | dentro da janela vertical e do lado solicitado |
| 208 | 130.00 | 152.00 | 112.92 | 106.20 | SIM | dentro da janela vertical e do lado solicitado |
| 209 | 129.00 | 153.00 | 111.62 | 105.20 | SIM | dentro da janela vertical e do lado solicitado |
| 210 | 128.00 | 154.00 | 110.31 | 104.20 | SIM | dentro da janela vertical e do lado solicitado |
| 211 | 128.00 | 155.00 | 109.38 | 103.20 | SIM | dentro da janela vertical e do lado solicitado |
| 212 | 127.00 | 156.00 | 108.08 | 102.20 | SIM | dentro da janela vertical e do lado solicitado |
| 213 | 126.00 | 157.00 | 106.78 | 101.20 | SIM | dentro da janela vertical e do lado solicitado |
| 214 | 126.00 | 158.00 | 105.85 | 100.20 | SIM | dentro da janela vertical e do lado solicitado |
| 215 | 125.00 | 159.00 | 104.55 | 99.20 | SIM | dentro da janela vertical e do lado solicitado |
| 216 | 124.00 | 160.00 | 103.25 | 98.20 | SIM | dentro da janela vertical e do lado solicitado |
| 217 | 124.00 | 161.00 | 102.32 | 97.20 | SIM | dentro da janela vertical e do lado solicitado |
| 218 | 123.00 | 162.00 | 101.02 | 96.20 | SIM | dentro da janela vertical e do lado solicitado |
| 219 | 122.00 | 163.00 | 99.72 | 95.20 | SIM | dentro da janela vertical e do lado solicitado |
| 220 | 122.00 | 164.00 | 98.79 | 94.20 | SIM | dentro da janela vertical e do lado solicitado |
| 221 | 121.00 | 165.00 | 97.50 | 93.20 | SIM | dentro da janela vertical e do lado solicitado |
| 222 | 121.00 | 166.00 | 96.57 | 92.20 | SIM | dentro da janela vertical e do lado solicitado |
| 223 | 120.00 | 167.00 | 95.27 | 91.20 | SIM | dentro da janela vertical e do lado solicitado |
| 224 | 119.00 | 168.00 | 93.98 | 90.20 | SIM | dentro da janela vertical e do lado solicitado |
| 225 | 119.00 | 169.00 | 93.05 | 89.20 | SIM | dentro da janela vertical e do lado solicitado |
| 226 | 118.00 | 170.00 | 91.76 | 88.20 | SIM | dentro da janela vertical e do lado solicitado |
| 227 | 118.00 | 171.00 | 90.82 | 87.20 | SIM | dentro da janela vertical e do lado solicitado |
| 228 | 117.00 | 172.00 | 89.54 | 86.20 | SIM | dentro da janela vertical e do lado solicitado |
| 229 | 117.00 | 173.00 | 88.60 | 85.20 | SIM | dentro da janela vertical e do lado solicitado |
| 230 | 116.00 | 174.00 | 87.32 | 84.20 | SIM | dentro da janela vertical e do lado solicitado |
| 231 | 115.00 | 175.00 | 86.03 | 83.20 | SIM | dentro da janela vertical e do lado solicitado |
| 232 | 115.00 | 176.00 | 85.09 | 82.20 | SIM | dentro da janela vertical e do lado solicitado |
| 233 | 114.00 | 177.00 | 83.82 | 81.20 | SIM | dentro da janela vertical e do lado solicitado |
| 234 | 114.00 | 178.00 | 82.87 | 80.20 | SIM | dentro da janela vertical e do lado solicitado |
| 235 | 113.00 | 179.00 | 81.60 | 79.20 | SIM | dentro da janela vertical e do lado solicitado |
| 236 | 113.00 | 180.00 | 80.65 | 78.20 | SIM | dentro da janela vertical e do lado solicitado |
| 237 | 112.00 | 181.00 | 79.38 | 77.20 | SIM | dentro da janela vertical e do lado solicitado |
| 238 | 112.00 | 182.00 | 78.43 | 76.20 | SIM | dentro da janela vertical e do lado solicitado |
| 239 | 111.00 | 183.00 | 77.16 | 75.20 | SIM | dentro da janela vertical e do lado solicitado |
| 240 | 111.00 | 184.00 | 76.22 | 74.20 | SIM | dentro da janela vertical e do lado solicitado |
| 241 | 110.00 | 185.00 | 74.95 | 73.20 | SIM | dentro da janela vertical e do lado solicitado |
| 242 | 110.00 | 186.00 | 74.00 | 72.20 | SIM | dentro da janela vertical e do lado solicitado |
| 243 | 109.00 | 187.00 | 72.73 | 71.20 | SIM | dentro da janela vertical e do lado solicitado |
| 244 | 109.00 | 188.00 | 71.78 | 70.20 | SIM | dentro da janela vertical e do lado solicitado |
| 245 | 108.00 | 189.00 | 70.52 | 69.20 | SIM | dentro da janela vertical e do lado solicitado |
| 246 | 108.00 | 190.00 | 69.57 | 68.20 | SIM | dentro da janela vertical e do lado solicitado |
| 247 | 107.00 | 191.00 | 68.31 | 67.20 | SIM | dentro da janela vertical e do lado solicitado |
| 248 | 107.00 | 192.00 | 67.36 | 66.20 | SIM | dentro da janela vertical e do lado solicitado |
| 249 | 106.00 | 193.00 | 66.10 | 65.20 | SIM | dentro da janela vertical e do lado solicitado |
| 250 | 106.00 | 194.00 | 65.15 | 64.20 | SIM | dentro da janela vertical e do lado solicitado |
| 251 | 105.00 | 195.00 | 63.89 | 63.20 | SIM | dentro da janela vertical e do lado solicitado |
| 252 | 105.00 | 196.00 | 62.94 | 62.20 | SIM | dentro da janela vertical e do lado solicitado |
| 253 | 104.00 | 197.00 | 61.68 | 61.20 | SIM | dentro da janela vertical e do lado solicitado |
| 254 | 104.00 | 198.00 | 60.73 | 60.20 | SIM | dentro da janela vertical e do lado solicitado |
| 255 | 103.00 | 199.00 | 59.48 | 59.20 | SIM | dentro da janela vertical e do lado solicitado |
| 256 | 103.00 | 200.00 | 58.52 | 58.20 | SIM | dentro da janela vertical e do lado solicitado |
| 257 | 103.00 | 201.00 | 57.57 | 57.20 | SIM | dentro da janela vertical e do lado solicitado |
| 258 | 102.00 | 202.00 | 56.32 | 56.20 | SIM | dentro da janela vertical e do lado solicitado |
| 259 | 102.00 | 203.00 | 55.36 | 55.20 | SIM | dentro da janela vertical e do lado solicitado |
| 260 | 102.00 | 204.00 | 54.41 | 54.20 | SIM | dentro da janela vertical e do lado solicitado |
| 261 | 101.00 | 205.00 | 53.16 | 53.20 | SIM | dentro da janela vertical e do lado solicitado |
| 262 | 101.00 | 206.00 | 52.20 | 52.20 | SIM | dentro da janela vertical e do lado solicitado |
| 263 | 100.00 | 207.00 | 50.96 | 51.20 | SIM | dentro da janela vertical e do lado solicitado |
| 264 | 100.00 | 208.00 | 50.00 | 50.20 | SIM | dentro da janela vertical e do lado solicitado |
| 265 | 100.00 | 209.00 | 49.04 | 49.20 | SIM | dentro da janela vertical e do lado solicitado |
| 266 | 99.00 | 210.00 | 47.80 | 48.20 | SIM | dentro da janela vertical e do lado solicitado |
| 267 | 99.00 | 211.00 | 46.84 | 47.20 | SIM | dentro da janela vertical e do lado solicitado |
| 268 | 99.00 | 212.00 | 45.88 | 46.20 | SIM | dentro da janela vertical e do lado solicitado |
| 269 | 98.00 | 213.00 | 44.64 | 45.20 | SIM | dentro da janela vertical e do lado solicitado |
| 270 | 98.00 | 214.00 | 43.68 | 44.20 | SIM | dentro da janela vertical e do lado solicitado |
| 271 | 97.00 | 215.00 | 42.45 | 43.20 | SIM | dentro da janela vertical e do lado solicitado |
| 272 | 97.00 | 216.00 | 41.48 | 42.20 | SIM | dentro da janela vertical e do lado solicitado |
| 273 | 97.00 | 217.00 | 40.52 | 41.20 | SIM | dentro da janela vertical e do lado solicitado |
| 274 | 96.00 | 218.00 | 39.29 | 40.20 | SIM | dentro da janela vertical e do lado solicitado |
| 275 | 96.00 | 219.00 | 38.33 | 39.20 | SIM | dentro da janela vertical e do lado solicitado |
| 276 | 96.00 | 220.00 | 37.36 | 38.20 | SIM | dentro da janela vertical e do lado solicitado |
| 277 | 95.00 | 221.00 | 36.14 | 37.20 | SIM | dentro da janela vertical e do lado solicitado |
| 278 | 95.00 | 222.00 | 35.17 | 36.20 | SIM | dentro da janela vertical e do lado solicitado |
| 279 | 95.00 | 223.00 | 34.21 | 35.20 | SIM | dentro da janela vertical e do lado solicitado |
| 280 | 94.00 | 224.00 | 32.98 | 34.20 | SIM | dentro da janela vertical e do lado solicitado |
| 281 | 94.00 | 225.00 | 32.02 | 33.20 | SIM | dentro da janela vertical e do lado solicitado |
| 282 | 94.00 | 226.00 | 31.05 | 32.20 | SIM | dentro da janela vertical e do lado solicitado |
| 283 | 94.00 | 227.00 | 30.08 | 31.20 | SIM | dentro da janela vertical e do lado solicitado |
| 284 | 93.00 | 228.00 | 28.86 | 30.20 | SIM | dentro da janela vertical e do lado solicitado |
| 285 | 93.00 | 229.00 | 27.89 | 29.20 | SIM | dentro da janela vertical e do lado solicitado |
| 286 | 93.00 | 230.00 | 26.93 | 28.20 | SIM | dentro da janela vertical e do lado solicitado |
| 287 | 92.00 | 231.00 | 25.71 | 27.20 | SIM | dentro da janela vertical e do lado solicitado |
| 288 | 92.00 | 232.00 | 24.74 | 26.20 | SIM | dentro da janela vertical e do lado solicitado |
| 289 | 92.00 | 233.00 | 23.77 | 25.20 | SIM | dentro da janela vertical e do lado solicitado |
| 290 | 91.00 | 234.00 | 22.56 | 24.20 | SIM | dentro da janela vertical e do lado solicitado |
| 291 | 91.00 | 235.00 | 21.59 | 23.20 | SIM | dentro da janela vertical e do lado solicitado |
| 292 | 91.00 | 236.00 | 20.62 | 22.20 | SIM | dentro da janela vertical e do lado solicitado |
| 293 | 91.00 | 237.00 | 19.65 | 21.20 | SIM | dentro da janela vertical e do lado solicitado |
| 294 | 90.00 | 238.00 | 18.44 | 20.20 | SIM | dentro da janela vertical e do lado solicitado |
| 295 | 90.00 | 239.00 | 17.46 | 19.20 | SIM | dentro da janela vertical e do lado solicitado |
| 296 | 90.00 | 240.00 | 16.49 | 18.20 | SIM | dentro da janela vertical e do lado solicitado |
| 297 | 90.00 | 241.00 | 15.52 | 17.20 | SIM | dentro da janela vertical e do lado solicitado |
| 298 | 89.00 | 242.00 | 14.32 | 16.20 | SIM | dentro da janela vertical e do lado solicitado |
| 299 | 89.00 | 243.00 | 13.34 | 15.20 | SIM | dentro da janela vertical e do lado solicitado |
| 300 | 89.00 | 244.00 | 12.37 | 14.20 | SIM | dentro da janela vertical e do lado solicitado |
| 301 | 89.00 | 245.00 | 11.40 | 13.20 | SIM | dentro da janela vertical e do lado solicitado |
| 302 | 88.00 | 246.00 | 10.20 | 12.20 | SIM | dentro da janela vertical e do lado solicitado |
| 303 | 88.00 | 247.00 | 9.22 | 11.20 | SIM | dentro da janela vertical e do lado solicitado |
| 304 | 88.00 | 248.00 | 8.25 | 10.20 | SIM | dentro da janela vertical e do lado solicitado |
| 305 | 88.00 | 249.00 | 7.28 | 9.20 | SIM | dentro da janela vertical e do lado solicitado |
| 306 | 88.00 | 250.00 | 6.32 | 8.20 | SIM | dentro da janela vertical e do lado solicitado |
| 307 | 87.00 | 251.00 | 5.10 | 7.20 | SIM | dentro da janela vertical e do lado solicitado |
| 308 | 87.00 | 252.00 | 4.12 | 6.20 | SIM | dentro da janela vertical e do lado solicitado |
| 309 | 87.00 | 253.00 | 3.16 | 5.20 | SIM | dentro da janela vertical e do lado solicitado |
| 310 | 87.00 | 254.00 | 2.24 | 4.20 | SIM | dentro da janela vertical e do lado solicitado |
| 311 | 87.00 | 255.00 | 1.41 | 3.20 | SIM | dentro da janela vertical e do lado solicitado |
| 312 | 86.00 | 256.00 | 0.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 313 | 87.00 | 256.00 | 1.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 314 | 88.00 | 256.00 | 2.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 315 | 89.00 | 256.00 | 3.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 316 | 90.00 | 256.00 | 4.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 317 | 91.00 | 256.00 | 5.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 318 | 92.00 | 256.00 | 6.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 319 | 93.00 | 256.00 | 7.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 320 | 94.00 | 256.00 | 8.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 321 | 95.00 | 256.00 | 9.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 322 | 96.00 | 256.00 | 10.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 323 | 97.00 | 256.00 | 11.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 324 | 98.00 | 256.00 | 12.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 325 | 99.00 | 256.00 | 13.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 326 | 100.00 | 256.00 | 14.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 327 | 101.00 | 256.00 | 15.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 328 | 102.00 | 256.00 | 16.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 329 | 103.00 | 256.00 | 17.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 330 | 104.00 | 256.00 | 18.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 331 | 105.00 | 256.00 | 19.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 332 | 106.00 | 256.00 | 20.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 333 | 107.00 | 256.00 | 21.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 334 | 108.00 | 256.00 | 22.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 335 | 109.00 | 256.00 | 23.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 336 | 110.00 | 256.00 | 24.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 337 | 111.00 | 256.00 | 25.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 338 | 112.00 | 256.00 | 26.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 339 | 113.00 | 256.00 | 27.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 340 | 114.00 | 256.00 | 28.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 341 | 115.00 | 256.00 | 29.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 342 | 116.00 | 256.00 | 30.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 343 | 117.00 | 256.00 | 31.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 344 | 118.00 | 256.00 | 32.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 345 | 119.00 | 256.00 | 33.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 346 | 120.00 | 256.00 | 34.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 347 | 121.00 | 256.00 | 35.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 348 | 122.00 | 256.00 | 36.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 349 | 123.00 | 256.00 | 37.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 350 | 124.00 | 256.00 | 38.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 351 | 125.00 | 256.00 | 39.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 352 | 126.00 | 256.00 | 40.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 353 | 127.00 | 256.00 | 41.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 354 | 128.00 | 256.00 | 42.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 355 | 129.00 | 256.00 | 43.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 356 | 130.00 | 256.00 | 44.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 357 | 131.00 | 256.00 | 45.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 358 | 132.00 | 256.00 | 46.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 359 | 133.00 | 256.00 | 47.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 360 | 134.00 | 256.00 | 48.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 361 | 135.00 | 256.00 | 49.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 362 | 136.00 | 256.00 | 50.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 363 | 137.00 | 256.00 | 51.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 364 | 138.00 | 256.00 | 52.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 365 | 139.00 | 256.00 | 53.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 366 | 140.00 | 256.00 | 54.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 367 | 141.00 | 256.00 | 55.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 368 | 142.00 | 256.00 | 56.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 369 | 143.00 | 256.00 | 57.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 370 | 144.00 | 256.00 | 58.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 371 | 145.00 | 256.00 | 59.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 372 | 146.00 | 256.00 | 60.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 373 | 147.00 | 256.00 | 61.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 374 | 148.00 | 256.00 | 62.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 375 | 149.00 | 256.00 | 63.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 376 | 150.00 | 256.00 | 64.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 377 | 151.00 | 256.00 | 65.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 378 | 152.00 | 256.00 | 66.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 379 | 153.00 | 256.00 | 67.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 380 | 154.00 | 256.00 | 68.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 381 | 155.00 | 256.00 | 69.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 382 | 156.00 | 256.00 | 70.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 383 | 157.00 | 256.00 | 71.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 384 | 158.00 | 256.00 | 72.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 385 | 159.00 | 256.00 | 73.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 386 | 160.00 | 256.00 | 74.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 387 | 161.00 | 256.00 | 75.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 388 | 162.00 | 256.00 | 76.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 389 | 163.00 | 256.00 | 77.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 390 | 164.00 | 256.00 | 78.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 391 | 165.00 | 256.00 | 79.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 392 | 166.00 | 256.00 | 80.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 393 | 167.00 | 256.00 | 81.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 394 | 168.00 | 256.00 | 82.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 395 | 169.00 | 256.00 | 83.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 396 | 170.00 | 256.00 | 84.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 397 | 171.00 | 256.00 | 85.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 398 | 172.00 | 256.00 | 86.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 399 | 173.00 | 256.00 | 87.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 400 | 174.00 | 256.00 | 88.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 401 | 175.00 | 256.00 | 89.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 402 | 176.00 | 256.00 | 90.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 403 | 177.00 | 256.00 | 91.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 404 | 178.00 | 256.00 | 92.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 405 | 179.00 | 256.00 | 93.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 406 | 180.00 | 256.00 | 94.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 407 | 181.00 | 256.00 | 95.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 408 | 182.00 | 256.00 | 96.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 409 | 183.00 | 256.00 | 97.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 410 | 184.00 | 256.00 | 98.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 411 | 185.00 | 256.00 | 99.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 412 | 186.00 | 256.00 | 100.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 413 | 187.00 | 256.00 | 101.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 414 | 188.00 | 256.00 | 102.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 415 | 189.00 | 256.00 | 103.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 416 | 190.00 | 256.00 | 104.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 417 | 191.00 | 256.00 | 105.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 418 | 192.00 | 256.00 | 106.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 419 | 193.00 | 256.00 | 107.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 420 | 194.00 | 256.00 | 108.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 421 | 195.00 | 256.00 | 109.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 422 | 196.00 | 256.00 | 110.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 423 | 197.00 | 256.00 | 111.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 424 | 198.00 | 256.00 | 112.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 425 | 199.00 | 256.00 | 113.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 426 | 200.00 | 256.00 | 114.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 427 | 201.00 | 256.00 | 115.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 428 | 202.00 | 256.00 | 116.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 429 | 203.00 | 256.00 | 117.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 430 | 204.00 | 256.00 | 118.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 431 | 205.00 | 256.00 | 119.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 432 | 206.00 | 256.00 | 120.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 433 | 207.00 | 256.00 | 121.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 434 | 208.00 | 256.00 | 122.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 435 | 209.00 | 256.00 | 123.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 436 | 210.00 | 256.00 | 124.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 437 | 211.00 | 256.00 | 125.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 438 | 212.00 | 256.00 | 126.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 439 | 213.00 | 256.00 | 127.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 440 | 214.00 | 256.00 | 128.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 441 | 215.00 | 256.00 | 129.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 442 | 216.00 | 256.00 | 130.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 443 | 217.00 | 256.00 | 131.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 444 | 218.00 | 256.00 | 132.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 445 | 219.00 | 256.00 | 133.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 446 | 220.00 | 256.00 | 134.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 447 | 221.00 | 256.00 | 135.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 448 | 222.00 | 256.00 | 136.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 449 | 223.00 | 256.00 | 137.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 450 | 224.00 | 256.00 | 138.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 451 | 225.00 | 256.00 | 139.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 452 | 226.00 | 256.00 | 140.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 453 | 227.00 | 256.00 | 141.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 454 | 228.00 | 256.00 | 142.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 455 | 229.00 | 256.00 | 143.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 456 | 230.00 | 256.00 | 144.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 457 | 231.00 | 256.00 | 145.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 458 | 232.00 | 256.00 | 146.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 459 | 233.00 | 256.00 | 147.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 460 | 234.00 | 256.00 | 148.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 461 | 235.00 | 256.00 | 149.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 462 | 236.00 | 256.00 | 150.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 463 | 237.00 | 256.00 | 151.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 464 | 238.00 | 256.00 | 152.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 465 | 239.00 | 256.00 | 153.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 466 | 240.00 | 256.00 | 154.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 467 | 241.00 | 256.00 | 155.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 468 | 242.00 | 256.00 | 156.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 469 | 243.00 | 256.00 | 157.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 470 | 244.00 | 256.00 | 158.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 471 | 245.00 | 256.00 | 159.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 472 | 246.00 | 256.00 | 160.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 473 | 247.00 | 256.00 | 161.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 474 | 248.00 | 256.00 | 162.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 475 | 249.00 | 256.00 | 163.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 476 | 250.00 | 256.00 | 164.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 477 | 251.00 | 256.00 | 165.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 478 | 252.00 | 256.00 | 166.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 479 | 253.00 | 256.00 | 167.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 480 | 254.00 | 256.00 | 168.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 481 | 255.00 | 256.00 | 169.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 482 | 256.00 | 256.00 | 170.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 483 | 257.00 | 256.00 | 171.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 484 | 258.00 | 256.00 | 172.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 485 | 259.00 | 256.00 | 173.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 486 | 260.00 | 256.00 | 174.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 487 | 261.00 | 256.00 | 175.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 488 | 262.00 | 256.00 | 176.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 489 | 263.00 | 256.00 | 177.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 490 | 264.00 | 256.00 | 178.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 491 | 265.00 | 256.00 | 179.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 492 | 266.00 | 256.00 | 180.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 493 | 267.00 | 256.00 | 181.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 494 | 268.00 | 256.00 | 182.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 495 | 269.00 | 256.00 | 183.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 496 | 270.00 | 256.00 | 184.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 497 | 271.00 | 256.00 | 185.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 498 | 272.00 | 256.00 | 186.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 499 | 273.00 | 256.00 | 187.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 500 | 274.00 | 256.00 | 188.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 501 | 275.00 | 256.00 | 189.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 502 | 276.00 | 256.00 | 190.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 503 | 277.00 | 256.00 | 191.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 504 | 278.00 | 256.00 | 192.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 505 | 279.00 | 256.00 | 193.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 506 | 280.00 | 256.00 | 194.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 507 | 281.00 | 256.00 | 195.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 508 | 282.00 | 256.00 | 196.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 509 | 283.00 | 256.00 | 197.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 510 | 284.00 | 256.00 | 198.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 511 | 285.00 | 256.00 | 199.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 512 | 286.00 | 256.00 | 200.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 513 | 287.00 | 256.00 | 201.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 514 | 288.00 | 256.00 | 202.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 515 | 289.00 | 256.00 | 203.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 516 | 290.00 | 256.00 | 204.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 517 | 291.00 | 256.00 | 205.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 518 | 292.00 | 256.00 | 206.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 519 | 293.00 | 256.00 | 207.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 520 | 294.00 | 256.00 | 208.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 521 | 295.00 | 256.00 | 209.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 522 | 296.00 | 256.00 | 210.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 523 | 297.00 | 256.00 | 211.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 524 | 298.00 | 256.00 | 212.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 525 | 299.00 | 256.00 | 213.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 526 | 300.00 | 256.00 | 214.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 527 | 301.00 | 256.00 | 215.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 528 | 302.00 | 256.00 | 216.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 529 | 303.00 | 256.00 | 217.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 530 | 304.00 | 256.00 | 218.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 531 | 305.00 | 256.00 | 219.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 532 | 306.00 | 256.00 | 220.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 533 | 307.00 | 256.00 | 221.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 534 | 308.00 | 256.00 | 222.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 535 | 309.00 | 256.00 | 223.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 536 | 310.00 | 256.00 | 224.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 537 | 311.00 | 256.00 | 225.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 538 | 312.00 | 256.00 | 226.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 539 | 313.00 | 256.00 | 227.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 540 | 314.00 | 256.00 | 228.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 541 | 315.00 | 256.00 | 229.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 542 | 316.00 | 256.00 | 230.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 543 | 317.00 | 256.00 | 231.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 544 | 318.00 | 256.00 | 232.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 545 | 319.00 | 256.00 | 233.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 546 | 320.00 | 256.00 | 234.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 547 | 321.00 | 256.00 | 235.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 548 | 322.00 | 256.00 | 236.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 549 | 323.00 | 256.00 | 237.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 550 | 324.00 | 256.00 | 238.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 551 | 325.00 | 256.00 | 239.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 552 | 326.00 | 256.00 | 240.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 553 | 327.00 | 256.00 | 241.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 554 | 328.00 | 256.00 | 242.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 555 | 329.00 | 256.00 | 243.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 556 | 330.00 | 256.00 | 244.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 557 | 331.00 | 256.00 | 245.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 558 | 332.00 | 256.00 | 246.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 559 | 333.00 | 256.00 | 247.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 560 | 334.00 | 256.00 | 248.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 561 | 335.00 | 256.00 | 249.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 562 | 336.00 | 256.00 | 250.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 563 | 337.00 | 256.00 | 251.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 564 | 338.00 | 256.00 | 252.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 565 | 339.00 | 256.00 | 253.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 566 | 340.00 | 256.00 | 254.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 567 | 341.00 | 256.00 | 255.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 568 | 342.00 | 256.00 | 256.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 569 | 343.00 | 256.00 | 257.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 570 | 344.00 | 256.00 | 258.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 571 | 345.00 | 256.00 | 259.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 572 | 346.00 | 256.00 | 260.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 573 | 347.00 | 256.00 | 261.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 574 | 348.00 | 256.00 | 262.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 575 | 349.00 | 256.00 | 263.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 576 | 350.00 | 256.00 | 264.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 577 | 351.00 | 256.00 | 265.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 578 | 352.00 | 256.00 | 266.00 | 2.20 | NÃO | fora do lado solicitado |
| 579 | 353.00 | 256.00 | 267.00 | 2.20 | NÃO | fora do lado solicitado |
| 580 | 354.00 | 256.00 | 268.00 | 2.20 | NÃO | fora do lado solicitado |
| 581 | 355.00 | 256.00 | 269.00 | 2.20 | NÃO | fora do lado solicitado |
| 582 | 356.00 | 256.00 | 270.00 | 2.20 | NÃO | fora do lado solicitado |
| 583 | 357.00 | 256.00 | 271.00 | 2.20 | NÃO | fora do lado solicitado |
| 584 | 358.00 | 256.00 | 272.00 | 2.20 | NÃO | fora do lado solicitado |
| 585 | 359.00 | 256.00 | 273.00 | 2.20 | NÃO | fora do lado solicitado |
| 586 | 360.00 | 256.00 | 274.00 | 2.20 | NÃO | fora do lado solicitado |
| 587 | 361.00 | 256.00 | 275.00 | 2.20 | NÃO | fora do lado solicitado |
| 588 | 362.00 | 256.00 | 276.00 | 2.20 | NÃO | fora do lado solicitado |
| 589 | 363.00 | 256.00 | 277.00 | 2.20 | NÃO | fora do lado solicitado |
| 590 | 364.00 | 256.00 | 278.00 | 2.20 | NÃO | fora do lado solicitado |
| 591 | 365.00 | 256.00 | 279.00 | 2.20 | NÃO | fora do lado solicitado |
| 592 | 366.00 | 256.00 | 280.00 | 2.20 | NÃO | fora do lado solicitado |
| 593 | 367.00 | 256.00 | 281.00 | 2.20 | NÃO | fora do lado solicitado |
| 594 | 368.00 | 256.00 | 282.00 | 2.20 | NÃO | fora do lado solicitado |
| 595 | 369.00 | 256.00 | 283.00 | 2.20 | NÃO | fora do lado solicitado |
| 596 | 370.00 | 256.00 | 284.00 | 2.20 | NÃO | fora do lado solicitado |
| 597 | 371.00 | 256.00 | 285.00 | 2.20 | NÃO | fora do lado solicitado |
| 598 | 372.00 | 256.00 | 286.00 | 2.20 | NÃO | fora do lado solicitado |
| 599 | 373.00 | 256.00 | 287.00 | 2.20 | NÃO | fora do lado solicitado |
| 600 | 374.00 | 256.00 | 288.00 | 2.20 | NÃO | fora do lado solicitado |
| 601 | 375.00 | 256.00 | 289.00 | 2.20 | NÃO | fora do lado solicitado |
| 602 | 376.00 | 256.00 | 290.00 | 2.20 | NÃO | fora do lado solicitado |
| 603 | 377.00 | 256.00 | 291.00 | 2.20 | NÃO | fora do lado solicitado |
| 604 | 378.00 | 256.00 | 292.00 | 2.20 | NÃO | fora do lado solicitado |
| 605 | 379.00 | 256.00 | 293.00 | 2.20 | NÃO | fora do lado solicitado |
| 606 | 380.00 | 256.00 | 294.00 | 2.20 | NÃO | fora do lado solicitado |
| 607 | 381.00 | 256.00 | 295.00 | 2.20 | NÃO | fora do lado solicitado |
| 608 | 382.00 | 256.00 | 296.00 | 2.20 | NÃO | fora do lado solicitado |
| 609 | 383.00 | 256.00 | 297.00 | 2.20 | NÃO | fora do lado solicitado |
| 610 | 384.00 | 256.00 | 298.00 | 2.20 | NÃO | fora do lado solicitado |
| 611 | 385.00 | 256.00 | 299.00 | 2.20 | NÃO | fora do lado solicitado |
| 612 | 386.00 | 256.00 | 300.00 | 2.20 | NÃO | fora do lado solicitado |
| 613 | 387.00 | 256.00 | 301.00 | 2.20 | NÃO | fora do lado solicitado |
| 614 | 388.00 | 256.00 | 302.00 | 2.20 | NÃO | fora do lado solicitado |
| 615 | 389.00 | 256.00 | 303.00 | 2.20 | NÃO | fora do lado solicitado |
| 616 | 390.00 | 256.00 | 304.00 | 2.20 | NÃO | fora do lado solicitado |
| 617 | 391.00 | 256.00 | 305.00 | 2.20 | NÃO | fora do lado solicitado |
| 618 | 392.00 | 256.00 | 306.00 | 2.20 | NÃO | fora do lado solicitado |
| 619 | 393.00 | 256.00 | 307.00 | 2.20 | NÃO | fora do lado solicitado |
| 620 | 394.00 | 256.00 | 308.00 | 2.20 | NÃO | fora do lado solicitado |
| 621 | 395.00 | 256.00 | 309.00 | 2.20 | NÃO | fora do lado solicitado |
| 622 | 396.00 | 256.00 | 310.00 | 2.20 | NÃO | fora do lado solicitado |
| 623 | 397.00 | 256.00 | 311.00 | 2.20 | NÃO | fora do lado solicitado |
| 624 | 398.00 | 256.00 | 312.00 | 2.20 | NÃO | fora do lado solicitado |
| 625 | 399.00 | 256.00 | 313.00 | 2.20 | NÃO | fora do lado solicitado |
| 626 | 400.00 | 256.00 | 314.00 | 2.20 | NÃO | fora do lado solicitado |
| 627 | 401.00 | 256.00 | 315.00 | 2.20 | NÃO | fora do lado solicitado |
| 628 | 402.00 | 256.00 | 316.00 | 2.20 | NÃO | fora do lado solicitado |
| 629 | 403.00 | 256.00 | 317.00 | 2.20 | NÃO | fora do lado solicitado |
| 630 | 404.00 | 256.00 | 318.00 | 2.20 | NÃO | fora do lado solicitado |
| 631 | 405.00 | 256.00 | 319.00 | 2.20 | NÃO | fora do lado solicitado |
| 632 | 406.00 | 256.00 | 320.00 | 2.20 | NÃO | fora do lado solicitado |
| 633 | 407.00 | 256.00 | 321.00 | 2.20 | NÃO | fora do lado solicitado |
| 634 | 408.00 | 256.00 | 322.00 | 2.20 | NÃO | fora do lado solicitado |
| 635 | 409.00 | 256.00 | 323.00 | 2.20 | NÃO | fora do lado solicitado |
| 636 | 410.00 | 256.00 | 324.00 | 2.20 | NÃO | fora do lado solicitado |
| 637 | 411.00 | 256.00 | 325.00 | 2.20 | NÃO | fora do lado solicitado |
| 638 | 412.00 | 256.00 | 326.00 | 2.20 | NÃO | fora do lado solicitado |
| 639 | 413.00 | 256.00 | 327.00 | 2.20 | NÃO | fora do lado solicitado |
| 640 | 414.00 | 256.00 | 328.00 | 2.20 | NÃO | fora do lado solicitado |
| 641 | 415.00 | 256.00 | 329.00 | 2.20 | NÃO | fora do lado solicitado |
| 642 | 416.00 | 256.00 | 330.00 | 2.20 | NÃO | fora do lado solicitado |
| 643 | 417.00 | 256.00 | 331.00 | 2.20 | NÃO | fora do lado solicitado |
| 644 | 418.00 | 256.00 | 332.00 | 2.20 | NÃO | fora do lado solicitado |
| 645 | 419.00 | 256.00 | 333.00 | 2.20 | NÃO | fora do lado solicitado |
| 646 | 420.00 | 256.00 | 334.00 | 2.20 | NÃO | fora do lado solicitado |
| 647 | 421.00 | 256.00 | 335.00 | 2.20 | NÃO | fora do lado solicitado |
| 648 | 422.00 | 256.00 | 336.00 | 2.20 | NÃO | fora do lado solicitado |
| 649 | 423.00 | 256.00 | 337.00 | 2.20 | NÃO | fora do lado solicitado |
| 650 | 424.00 | 256.00 | 338.00 | 2.20 | NÃO | fora do lado solicitado |
| 651 | 425.00 | 256.00 | 339.00 | 2.20 | NÃO | fora do lado solicitado |
| 652 | 426.00 | 256.00 | 340.00 | 2.20 | NÃO | fora do lado solicitado |
| 653 | 427.00 | 256.00 | 341.00 | 2.20 | NÃO | fora do lado solicitado |
| 654 | 428.00 | 256.00 | 342.00 | 2.20 | NÃO | fora do lado solicitado |
| 655 | 429.00 | 256.00 | 343.00 | 2.20 | NÃO | fora do lado solicitado |
| 656 | 430.00 | 256.00 | 344.00 | 2.20 | NÃO | fora do lado solicitado |
| 657 | 431.00 | 256.00 | 345.00 | 2.20 | NÃO | fora do lado solicitado |
| 658 | 432.00 | 256.00 | 346.00 | 2.20 | NÃO | fora do lado solicitado |
| 659 | 433.00 | 256.00 | 347.00 | 2.20 | NÃO | fora do lado solicitado |
| 660 | 434.00 | 256.00 | 348.00 | 2.20 | NÃO | fora do lado solicitado |
| 661 | 435.00 | 256.00 | 349.00 | 2.20 | NÃO | fora do lado solicitado |
| 662 | 436.00 | 256.00 | 350.00 | 2.20 | NÃO | fora do lado solicitado |
| 663 | 437.00 | 256.00 | 351.00 | 2.20 | NÃO | fora do lado solicitado |
| 664 | 438.00 | 256.00 | 352.00 | 2.20 | NÃO | fora do lado solicitado |
| 665 | 439.00 | 256.00 | 353.00 | 2.20 | NÃO | fora do lado solicitado |
| 666 | 440.00 | 256.00 | 354.00 | 2.20 | NÃO | fora do lado solicitado |
| 667 | 441.00 | 256.00 | 355.00 | 2.20 | NÃO | fora do lado solicitado |
| 668 | 442.00 | 256.00 | 356.00 | 2.20 | NÃO | fora do lado solicitado |
| 669 | 443.00 | 256.00 | 357.00 | 2.20 | NÃO | fora do lado solicitado |
| 670 | 444.00 | 256.00 | 358.00 | 2.20 | NÃO | fora do lado solicitado |
| 671 | 445.00 | 256.00 | 359.00 | 2.20 | NÃO | fora do lado solicitado |
| 672 | 446.00 | 256.00 | 360.00 | 2.20 | NÃO | fora do lado solicitado |
| 673 | 447.00 | 256.00 | 361.00 | 2.20 | NÃO | fora do lado solicitado |
| 674 | 448.00 | 256.00 | 362.00 | 2.20 | NÃO | fora do lado solicitado |
| 675 | 449.00 | 256.00 | 363.00 | 2.20 | NÃO | fora do lado solicitado |
| 676 | 450.00 | 256.00 | 364.00 | 2.20 | NÃO | fora do lado solicitado |
| 677 | 451.00 | 256.00 | 365.00 | 2.20 | NÃO | fora do lado solicitado |
| 678 | 452.00 | 256.00 | 366.00 | 2.20 | NÃO | fora do lado solicitado |
| 679 | 453.00 | 256.00 | 367.00 | 2.20 | NÃO | fora do lado solicitado |
| 680 | 454.00 | 256.00 | 368.00 | 2.20 | NÃO | fora do lado solicitado |
| 681 | 455.00 | 256.00 | 369.00 | 2.20 | NÃO | fora do lado solicitado |
| 682 | 456.00 | 256.00 | 370.00 | 2.20 | NÃO | fora do lado solicitado |
| 683 | 457.00 | 256.00 | 371.00 | 2.20 | NÃO | fora do lado solicitado |
| 684 | 458.00 | 256.00 | 372.00 | 2.20 | NÃO | fora do lado solicitado |
| 685 | 459.00 | 256.00 | 373.00 | 2.20 | NÃO | fora do lado solicitado |
| 686 | 460.00 | 256.00 | 374.00 | 2.20 | NÃO | fora do lado solicitado |
| 687 | 461.00 | 256.00 | 375.00 | 2.20 | NÃO | fora do lado solicitado |
| 688 | 462.00 | 256.00 | 376.00 | 2.20 | NÃO | fora do lado solicitado |
| 689 | 463.00 | 256.00 | 377.00 | 2.20 | NÃO | fora do lado solicitado |
| 690 | 464.00 | 256.00 | 378.00 | 2.20 | NÃO | fora do lado solicitado |
| 691 | 465.00 | 256.00 | 379.00 | 2.20 | NÃO | fora do lado solicitado |
| 692 | 466.00 | 256.00 | 380.00 | 2.20 | NÃO | fora do lado solicitado |
| 693 | 467.00 | 256.00 | 381.00 | 2.20 | NÃO | fora do lado solicitado |
| 694 | 468.00 | 256.00 | 382.00 | 2.20 | NÃO | fora do lado solicitado |
| 695 | 469.00 | 256.00 | 383.00 | 2.20 | NÃO | fora do lado solicitado |
| 696 | 470.00 | 256.00 | 384.00 | 2.20 | NÃO | fora do lado solicitado |
| 697 | 471.00 | 256.00 | 385.00 | 2.20 | NÃO | fora do lado solicitado |
| 698 | 472.00 | 256.00 | 386.00 | 2.20 | NÃO | fora do lado solicitado |
| 699 | 473.00 | 256.00 | 387.00 | 2.20 | NÃO | fora do lado solicitado |
| 700 | 474.00 | 256.00 | 388.00 | 2.20 | NÃO | fora do lado solicitado |
| 701 | 475.00 | 256.00 | 389.00 | 2.20 | NÃO | fora do lado solicitado |
| 702 | 476.00 | 256.00 | 390.00 | 2.20 | NÃO | fora do lado solicitado |
| 703 | 477.00 | 256.00 | 391.00 | 2.20 | NÃO | fora do lado solicitado |
| 704 | 478.00 | 256.00 | 392.00 | 2.20 | NÃO | fora do lado solicitado |
| 705 | 479.00 | 256.00 | 393.00 | 2.20 | NÃO | fora do lado solicitado |
| 706 | 480.00 | 256.00 | 394.00 | 2.20 | NÃO | fora do lado solicitado |
| 707 | 481.00 | 256.00 | 395.00 | 2.20 | NÃO | fora do lado solicitado |
| 708 | 482.00 | 256.00 | 396.00 | 2.20 | NÃO | fora do lado solicitado |
| 709 | 483.00 | 256.00 | 397.00 | 2.20 | NÃO | fora do lado solicitado |
| 710 | 484.00 | 256.00 | 398.00 | 2.20 | NÃO | fora do lado solicitado |
| 711 | 485.00 | 256.00 | 399.00 | 2.20 | NÃO | fora do lado solicitado |
| 712 | 486.00 | 256.00 | 400.00 | 2.20 | NÃO | fora do lado solicitado |
| 713 | 487.00 | 256.00 | 401.00 | 2.20 | NÃO | fora do lado solicitado |
| 714 | 488.00 | 256.00 | 402.00 | 2.20 | NÃO | fora do lado solicitado |
| 715 | 489.00 | 256.00 | 403.00 | 2.20 | NÃO | fora do lado solicitado |
| 716 | 490.00 | 256.00 | 404.00 | 2.20 | NÃO | fora do lado solicitado |
| 717 | 491.00 | 256.00 | 405.00 | 2.20 | NÃO | fora do lado solicitado |
| 718 | 492.00 | 256.00 | 406.00 | 2.20 | NÃO | fora do lado solicitado |
| 719 | 493.00 | 256.00 | 407.00 | 2.20 | NÃO | fora do lado solicitado |
| 720 | 494.00 | 256.00 | 408.00 | 2.20 | NÃO | fora do lado solicitado |
| 721 | 495.00 | 256.00 | 409.00 | 2.20 | NÃO | fora do lado solicitado |
| 722 | 496.00 | 256.00 | 410.00 | 2.20 | NÃO | fora do lado solicitado |
| 723 | 497.00 | 256.00 | 411.00 | 2.20 | NÃO | fora do lado solicitado |
| 724 | 498.00 | 256.00 | 412.00 | 2.20 | NÃO | fora do lado solicitado |
| 725 | 499.00 | 256.00 | 413.00 | 2.20 | NÃO | fora do lado solicitado |
| 726 | 500.00 | 256.00 | 414.00 | 2.20 | NÃO | fora do lado solicitado |
| 727 | 501.00 | 256.00 | 415.00 | 2.20 | NÃO | fora do lado solicitado |
| 728 | 502.00 | 256.00 | 416.00 | 2.20 | NÃO | fora do lado solicitado |
| 729 | 503.00 | 256.00 | 417.00 | 2.20 | NÃO | fora do lado solicitado |
| 730 | 504.00 | 256.00 | 418.00 | 2.20 | NÃO | fora do lado solicitado |
| 731 | 505.00 | 256.00 | 419.00 | 2.20 | NÃO | fora do lado solicitado |
| 732 | 506.00 | 256.00 | 420.00 | 2.20 | NÃO | fora do lado solicitado |
| 733 | 507.00 | 256.00 | 421.00 | 2.20 | NÃO | fora do lado solicitado |
| 734 | 508.00 | 256.00 | 422.00 | 2.20 | NÃO | fora do lado solicitado |
| 735 | 509.00 | 256.00 | 423.00 | 2.20 | NÃO | fora do lado solicitado |
| 736 | 510.00 | 256.00 | 424.00 | 2.20 | NÃO | fora do lado solicitado |
| 737 | 511.00 | 256.00 | 425.00 | 2.20 | NÃO | fora do lado solicitado |
| 738 | 512.00 | 256.00 | 426.00 | 2.20 | NÃO | fora do lado solicitado |
| 739 | 513.00 | 256.00 | 427.00 | 2.20 | NÃO | fora do lado solicitado |
| 740 | 514.00 | 256.00 | 428.00 | 2.20 | NÃO | fora do lado solicitado |
| 741 | 515.00 | 256.00 | 429.00 | 2.20 | NÃO | fora do lado solicitado |
| 742 | 516.00 | 256.00 | 430.00 | 2.20 | NÃO | fora do lado solicitado |
| 743 | 517.00 | 256.00 | 431.00 | 2.20 | NÃO | fora do lado solicitado |
| 744 | 518.00 | 256.00 | 432.00 | 2.20 | NÃO | fora do lado solicitado |
| 745 | 519.00 | 256.00 | 433.00 | 2.20 | NÃO | fora do lado solicitado |
| 746 | 520.00 | 256.00 | 434.00 | 2.20 | NÃO | fora do lado solicitado |
| 747 | 521.00 | 256.00 | 435.00 | 2.20 | NÃO | fora do lado solicitado |
| 748 | 522.00 | 256.00 | 436.00 | 2.20 | NÃO | fora do lado solicitado |
| 749 | 523.00 | 256.00 | 437.00 | 2.20 | NÃO | fora do lado solicitado |
| 750 | 524.00 | 256.00 | 438.00 | 2.20 | NÃO | fora do lado solicitado |
| 751 | 525.00 | 256.00 | 439.00 | 2.20 | NÃO | fora do lado solicitado |
| 752 | 526.00 | 256.00 | 440.00 | 2.20 | NÃO | fora do lado solicitado |
| 753 | 527.00 | 256.00 | 441.00 | 2.20 | NÃO | fora do lado solicitado |
| 754 | 528.00 | 256.00 | 442.00 | 2.20 | NÃO | fora do lado solicitado |
| 755 | 529.00 | 256.00 | 443.00 | 2.20 | NÃO | fora do lado solicitado |
| 756 | 530.00 | 256.00 | 444.00 | 2.20 | NÃO | fora do lado solicitado |
| 757 | 531.00 | 256.00 | 445.00 | 2.20 | NÃO | fora do lado solicitado |
| 758 | 532.00 | 256.00 | 446.00 | 2.20 | NÃO | fora do lado solicitado |
| 759 | 533.00 | 256.00 | 447.00 | 2.20 | NÃO | fora do lado solicitado |
| 760 | 534.00 | 256.00 | 448.00 | 2.20 | NÃO | fora do lado solicitado |
| 761 | 535.00 | 256.00 | 449.00 | 2.20 | NÃO | fora do lado solicitado |
| 762 | 536.00 | 256.00 | 450.00 | 2.20 | NÃO | fora do lado solicitado |
| 763 | 537.00 | 256.00 | 451.00 | 2.20 | NÃO | fora do lado solicitado |
| 764 | 538.00 | 256.00 | 452.00 | 2.20 | NÃO | fora do lado solicitado |
| 765 | 539.00 | 256.00 | 453.00 | 2.20 | NÃO | fora do lado solicitado |
| 766 | 540.00 | 256.00 | 454.00 | 2.20 | NÃO | fora do lado solicitado |
| 767 | 541.00 | 256.00 | 455.00 | 2.20 | NÃO | fora do lado solicitado |
| 768 | 542.00 | 256.00 | 456.00 | 2.20 | NÃO | fora do lado solicitado |
| 769 | 543.00 | 256.00 | 457.00 | 2.20 | NÃO | fora do lado solicitado |
| 770 | 544.00 | 256.00 | 458.00 | 2.20 | NÃO | fora do lado solicitado |
| 771 | 545.00 | 256.00 | 459.00 | 2.20 | NÃO | fora do lado solicitado |
| 772 | 546.00 | 256.00 | 460.00 | 2.20 | NÃO | fora do lado solicitado |
| 773 | 547.00 | 256.00 | 461.00 | 2.20 | NÃO | fora do lado solicitado |
| 774 | 548.00 | 256.00 | 462.00 | 2.20 | NÃO | fora do lado solicitado |
| 775 | 549.00 | 256.00 | 463.00 | 2.20 | NÃO | fora do lado solicitado |
| 776 | 550.00 | 256.00 | 464.00 | 2.20 | NÃO | fora do lado solicitado |
| 777 | 551.00 | 256.00 | 465.00 | 2.20 | NÃO | fora do lado solicitado |
| 778 | 552.00 | 256.00 | 466.00 | 2.20 | NÃO | fora do lado solicitado |
| 779 | 553.00 | 256.00 | 467.00 | 2.20 | NÃO | fora do lado solicitado |
| 780 | 554.00 | 256.00 | 468.00 | 2.20 | NÃO | fora do lado solicitado |
| 781 | 555.00 | 256.00 | 469.00 | 2.20 | NÃO | fora do lado solicitado |
| 782 | 556.00 | 256.00 | 470.00 | 2.20 | NÃO | fora do lado solicitado |
| 783 | 557.00 | 256.00 | 471.00 | 2.20 | NÃO | fora do lado solicitado |
| 784 | 558.00 | 256.00 | 472.00 | 2.20 | NÃO | fora do lado solicitado |
| 785 | 559.00 | 256.00 | 473.00 | 2.20 | NÃO | fora do lado solicitado |
| 786 | 560.00 | 256.00 | 474.00 | 2.20 | NÃO | fora do lado solicitado |
| 787 | 561.00 | 256.00 | 475.00 | 2.20 | NÃO | fora do lado solicitado |
| 788 | 562.00 | 256.00 | 476.00 | 2.20 | NÃO | fora do lado solicitado |
| 789 | 563.00 | 256.00 | 477.00 | 2.20 | NÃO | fora do lado solicitado |
| 790 | 564.00 | 256.00 | 478.00 | 2.20 | NÃO | fora do lado solicitado |
| 791 | 565.00 | 256.00 | 479.00 | 2.20 | NÃO | fora do lado solicitado |
| 792 | 566.00 | 256.00 | 480.00 | 2.20 | NÃO | fora do lado solicitado |
| 793 | 567.00 | 256.00 | 481.00 | 2.20 | NÃO | fora do lado solicitado |
| 794 | 568.00 | 256.00 | 482.00 | 2.20 | NÃO | fora do lado solicitado |
| 795 | 569.00 | 256.00 | 483.00 | 2.20 | NÃO | fora do lado solicitado |
| 796 | 570.00 | 256.00 | 484.00 | 2.20 | NÃO | fora do lado solicitado |
| 797 | 571.00 | 256.00 | 485.00 | 2.20 | NÃO | fora do lado solicitado |
| 798 | 572.00 | 256.00 | 486.00 | 2.20 | NÃO | fora do lado solicitado |
| 799 | 573.00 | 256.00 | 487.00 | 2.20 | NÃO | fora do lado solicitado |
| 800 | 574.00 | 256.00 | 488.00 | 2.20 | NÃO | fora do lado solicitado |
| 801 | 575.00 | 256.00 | 489.00 | 2.20 | NÃO | fora do lado solicitado |
| 802 | 576.00 | 256.00 | 490.00 | 2.20 | NÃO | fora do lado solicitado |
| 803 | 577.00 | 256.00 | 491.00 | 2.20 | NÃO | fora do lado solicitado |
| 804 | 578.00 | 256.00 | 492.00 | 2.20 | NÃO | fora do lado solicitado |
| 805 | 579.00 | 256.00 | 493.00 | 2.20 | NÃO | fora do lado solicitado |
| 806 | 580.00 | 256.00 | 494.00 | 2.20 | NÃO | fora do lado solicitado |
| 807 | 581.00 | 256.00 | 495.00 | 2.20 | NÃO | fora do lado solicitado |
| 808 | 582.00 | 256.00 | 496.00 | 2.20 | NÃO | fora do lado solicitado |
| 809 | 583.00 | 256.00 | 497.00 | 2.20 | NÃO | fora do lado solicitado |
| 810 | 584.00 | 256.00 | 498.00 | 2.20 | NÃO | fora do lado solicitado |
| 811 | 585.00 | 256.00 | 499.00 | 2.20 | NÃO | fora do lado solicitado |
| 812 | 586.00 | 256.00 | 500.00 | 2.20 | NÃO | fora do lado solicitado |
| 813 | 587.00 | 256.00 | 501.00 | 2.20 | NÃO | fora do lado solicitado |
| 814 | 588.00 | 256.00 | 502.00 | 2.20 | NÃO | fora do lado solicitado |
| 815 | 589.00 | 256.00 | 503.00 | 2.20 | NÃO | fora do lado solicitado |
| 816 | 590.00 | 256.00 | 504.00 | 2.20 | NÃO | fora do lado solicitado |
| 817 | 591.00 | 256.00 | 505.00 | 2.20 | NÃO | fora do lado solicitado |
| 818 | 592.00 | 256.00 | 506.00 | 2.20 | NÃO | fora do lado solicitado |
| 819 | 593.00 | 256.00 | 507.00 | 2.20 | NÃO | fora do lado solicitado |
| 820 | 594.00 | 256.00 | 508.00 | 2.20 | NÃO | fora do lado solicitado |
| 821 | 595.00 | 256.00 | 509.00 | 2.20 | NÃO | fora do lado solicitado |
| 822 | 596.00 | 256.00 | 510.00 | 2.20 | NÃO | fora do lado solicitado |
| 823 | 597.00 | 256.00 | 511.00 | 2.20 | NÃO | fora do lado solicitado |
| 824 | 598.00 | 256.00 | 512.00 | 2.20 | NÃO | fora do lado solicitado |
| 825 | 599.00 | 256.00 | 513.00 | 2.20 | NÃO | fora do lado solicitado |
| 826 | 600.00 | 256.00 | 514.00 | 2.20 | NÃO | fora do lado solicitado |
| 827 | 601.00 | 256.00 | 515.00 | 2.20 | NÃO | fora do lado solicitado |
| 828 | 602.00 | 256.00 | 516.00 | 2.20 | NÃO | fora do lado solicitado |
| 829 | 603.00 | 256.00 | 517.00 | 2.20 | NÃO | fora do lado solicitado |
| 830 | 604.00 | 256.00 | 518.00 | 2.20 | NÃO | fora do lado solicitado |
| 831 | 605.00 | 256.00 | 519.00 | 2.20 | NÃO | fora do lado solicitado |
| 832 | 606.00 | 256.00 | 520.00 | 2.20 | NÃO | fora do lado solicitado |
| 833 | 607.00 | 256.00 | 521.00 | 2.20 | NÃO | fora do lado solicitado |
| 834 | 608.00 | 256.00 | 522.00 | 2.20 | NÃO | fora do lado solicitado |
| 835 | 609.00 | 256.00 | 523.00 | 2.20 | NÃO | fora do lado solicitado |
| 836 | 610.00 | 256.00 | 524.00 | 2.20 | NÃO | fora do lado solicitado |
| 837 | 611.00 | 256.00 | 525.00 | 2.20 | NÃO | fora do lado solicitado |
| 838 | 612.00 | 256.00 | 526.00 | 2.20 | NÃO | fora do lado solicitado |
| 839 | 613.00 | 256.00 | 527.00 | 2.20 | NÃO | fora do lado solicitado |
| 840 | 614.00 | 256.00 | 528.00 | 2.20 | NÃO | fora do lado solicitado |
| 841 | 615.00 | 256.00 | 529.00 | 2.20 | NÃO | fora do lado solicitado |
| 842 | 616.00 | 256.00 | 530.00 | 2.20 | NÃO | fora do lado solicitado |
| 843 | 617.00 | 256.00 | 531.00 | 2.20 | NÃO | fora do lado solicitado |
| 844 | 616.00 | 255.00 | 530.00 | 3.20 | NÃO | fora do lado solicitado |
| 845 | 616.00 | 254.00 | 530.00 | 4.20 | NÃO | fora do lado solicitado |
| 846 | 616.00 | 253.00 | 530.01 | 5.20 | NÃO | fora do lado solicitado |
| 847 | 616.00 | 252.00 | 530.02 | 6.20 | NÃO | fora do lado solicitado |
| 848 | 616.00 | 251.00 | 530.02 | 7.20 | NÃO | fora do lado solicitado |
| 849 | 615.00 | 250.00 | 529.03 | 8.20 | NÃO | fora do lado solicitado |
| 850 | 615.00 | 249.00 | 529.05 | 9.20 | NÃO | fora do lado solicitado |
| 851 | 615.00 | 248.00 | 529.06 | 10.20 | NÃO | fora do lado solicitado |
| 852 | 615.00 | 247.00 | 529.08 | 11.20 | NÃO | fora do lado solicitado |
| 853 | 615.00 | 246.00 | 529.09 | 12.20 | NÃO | fora do lado solicitado |
| 854 | 614.00 | 245.00 | 528.11 | 13.20 | NÃO | fora do lado solicitado |
| 855 | 614.00 | 244.00 | 528.14 | 14.20 | NÃO | fora do lado solicitado |
| 856 | 614.00 | 243.00 | 528.16 | 15.20 | NÃO | fora do lado solicitado |
| 857 | 614.00 | 242.00 | 528.19 | 16.20 | NÃO | fora do lado solicitado |
| 858 | 613.00 | 241.00 | 527.21 | 17.20 | NÃO | fora do lado solicitado |
| 859 | 613.00 | 240.00 | 527.24 | 18.20 | NÃO | fora do lado solicitado |
| 860 | 613.00 | 239.00 | 527.27 | 19.20 | NÃO | fora do lado solicitado |
| 861 | 613.00 | 238.00 | 527.31 | 20.20 | NÃO | fora do lado solicitado |
| 862 | 612.00 | 237.00 | 526.34 | 21.20 | NÃO | fora do lado solicitado |
| 863 | 612.00 | 236.00 | 526.38 | 22.20 | NÃO | fora do lado solicitado |
| 864 | 612.00 | 235.00 | 526.42 | 23.20 | NÃO | fora do lado solicitado |
| 865 | 612.00 | 234.00 | 526.46 | 24.20 | NÃO | fora do lado solicitado |
| 866 | 611.00 | 233.00 | 525.50 | 25.20 | NÃO | fora do lado solicitado |
| 867 | 611.00 | 232.00 | 525.55 | 26.20 | NÃO | fora do lado solicitado |
| 868 | 611.00 | 231.00 | 525.59 | 27.20 | NÃO | fora do lado solicitado |
| 869 | 610.00 | 230.00 | 524.64 | 28.20 | NÃO | fora do lado solicitado |
| 870 | 610.00 | 229.00 | 524.70 | 29.20 | NÃO | fora do lado solicitado |
| 871 | 610.00 | 228.00 | 524.75 | 30.20 | NÃO | fora do lado solicitado |
| 872 | 609.00 | 227.00 | 523.80 | 31.20 | NÃO | fora do lado solicitado |
| 873 | 609.00 | 226.00 | 523.86 | 32.20 | NÃO | fora do lado solicitado |
| 874 | 609.00 | 225.00 | 523.92 | 33.20 | NÃO | fora do lado solicitado |
| 875 | 609.00 | 224.00 | 523.98 | 34.20 | NÃO | fora do lado solicitado |
| 876 | 608.00 | 223.00 | 523.04 | 35.20 | NÃO | fora do lado solicitado |
| 877 | 608.00 | 222.00 | 523.11 | 36.20 | NÃO | fora do lado solicitado |
| 878 | 608.00 | 221.00 | 523.17 | 37.20 | NÃO | fora do lado solicitado |
| 879 | 607.00 | 220.00 | 522.24 | 38.20 | NÃO | fora do lado solicitado |
| 880 | 607.00 | 219.00 | 522.31 | 39.20 | NÃO | fora do lado solicitado |
| 881 | 607.00 | 218.00 | 522.38 | 40.20 | NÃO | fora do lado solicitado |
| 882 | 606.00 | 217.00 | 521.46 | 41.20 | NÃO | fora do lado solicitado |
| 883 | 606.00 | 216.00 | 521.54 | 42.20 | NÃO | fora do lado solicitado |
| 884 | 606.00 | 215.00 | 521.61 | 43.20 | NÃO | fora do lado solicitado |
| 885 | 605.00 | 214.00 | 520.70 | 44.20 | NÃO | fora do lado solicitado |
| 886 | 605.00 | 213.00 | 520.78 | 45.20 | NÃO | fora do lado solicitado |
| 887 | 604.00 | 212.00 | 519.87 | 46.20 | NÃO | fora do lado solicitado |
| 888 | 604.00 | 211.00 | 519.95 | 47.20 | NÃO | fora do lado solicitado |
| 889 | 604.00 | 210.00 | 520.04 | 48.20 | NÃO | fora do lado solicitado |
| 890 | 603.00 | 209.00 | 519.13 | 49.20 | NÃO | fora do lado solicitado |
| 891 | 603.00 | 208.00 | 519.22 | 50.20 | NÃO | fora do lado solicitado |
| 892 | 602.00 | 207.00 | 518.32 | 51.20 | NÃO | fora do lado solicitado |
| 893 | 602.00 | 206.00 | 518.42 | 52.20 | NÃO | fora do lado solicitado |
| 894 | 602.00 | 205.00 | 518.51 | 53.20 | NÃO | fora do lado solicitado |
| 895 | 601.00 | 204.00 | 517.62 | 54.20 | NÃO | fora do lado solicitado |
| 896 | 601.00 | 203.00 | 517.72 | 55.20 | NÃO | fora do lado solicitado |
| 897 | 601.00 | 202.00 | 517.82 | 56.20 | NÃO | fora do lado solicitado |
| 898 | 600.00 | 201.00 | 516.93 | 57.20 | NÃO | fora do lado solicitado |
| 899 | 600.00 | 200.00 | 517.04 | 58.20 | NÃO | fora do lado solicitado |
| 900 | 599.00 | 199.00 | 516.16 | 59.20 | NÃO | fora do lado solicitado |
| 901 | 599.00 | 198.00 | 516.27 | 60.20 | NÃO | fora do lado solicitado |
| 902 | 598.00 | 197.00 | 515.39 | 61.20 | NÃO | fora do lado solicitado |
| 903 | 598.00 | 196.00 | 515.50 | 62.20 | NÃO | fora do lado solicitado |
| 904 | 597.00 | 195.00 | 514.63 | 63.20 | NÃO | fora do lado solicitado |
| 905 | 597.00 | 194.00 | 514.75 | 64.20 | NÃO | fora do lado solicitado |
| 906 | 597.00 | 193.00 | 514.87 | 65.20 | NÃO | fora do lado solicitado |
| 907 | 596.00 | 192.00 | 514.00 | 66.20 | NÃO | fora do lado solicitado |
| 908 | 596.00 | 191.00 | 514.13 | 67.20 | NÃO | fora do lado solicitado |
| 909 | 595.00 | 190.00 | 513.26 | 68.20 | NÃO | fora do lado solicitado |
| 910 | 595.00 | 189.00 | 513.39 | 69.20 | NÃO | fora do lado solicitado |
| 911 | 594.00 | 188.00 | 512.53 | 70.20 | NÃO | fora do lado solicitado |
| 912 | 594.00 | 187.00 | 512.66 | 71.20 | NÃO | fora do lado solicitado |
| 913 | 593.00 | 186.00 | 511.81 | 72.20 | NÃO | fora do lado solicitado |
| 914 | 593.00 | 185.00 | 511.95 | 73.20 | NÃO | fora do lado solicitado |
| 915 | 592.00 | 184.00 | 511.10 | 74.20 | NÃO | fora do lado solicitado |
| 916 | 592.00 | 183.00 | 511.24 | 75.20 | NÃO | fora do lado solicitado |
| 917 | 591.00 | 182.00 | 510.39 | 76.20 | NÃO | fora do lado solicitado |
| 918 | 591.00 | 181.00 | 510.54 | 77.20 | NÃO | fora do lado solicitado |
| 919 | 590.00 | 180.00 | 509.70 | 78.20 | NÃO | fora do lado solicitado |
| 920 | 590.00 | 179.00 | 509.85 | 79.20 | NÃO | fora do lado solicitado |
| 921 | 589.00 | 178.00 | 509.01 | 80.20 | NÃO | fora do lado solicitado |
| 922 | 589.00 | 177.00 | 509.17 | 81.20 | NÃO | fora do lado solicitado |
| 923 | 588.00 | 176.00 | 508.33 | 82.20 | NÃO | fora do lado solicitado |
| 924 | 588.00 | 175.00 | 508.49 | 83.20 | NÃO | fora do lado solicitado |
| 925 | 587.00 | 174.00 | 507.67 | 84.20 | NÃO | fora do lado solicitado |
| 926 | 586.00 | 173.00 | 506.84 | 85.20 | NÃO | fora do lado solicitado |
| 927 | 586.00 | 172.00 | 507.01 | 86.20 | NÃO | fora do lado solicitado |
| 928 | 585.00 | 171.00 | 506.19 | 87.20 | NÃO | fora do lado solicitado |
| 929 | 585.00 | 170.00 | 506.36 | 88.20 | NÃO | fora do lado solicitado |
| 930 | 584.00 | 169.00 | 505.54 | 89.20 | NÃO | fora do lado solicitado |
| 931 | 584.00 | 168.00 | 505.72 | 90.20 | NÃO | fora do lado solicitado |
| 932 | 583.00 | 167.00 | 504.91 | 91.20 | NÃO | fora do lado solicitado |
| 933 | 582.00 | 166.00 | 504.10 | 92.20 | NÃO | fora do lado solicitado |
| 934 | 582.00 | 165.00 | 504.28 | 93.20 | NÃO | fora do lado solicitado |
| 935 | 581.00 | 164.00 | 503.48 | 94.20 | NÃO | fora do lado solicitado |
| 936 | 581.00 | 163.00 | 503.66 | 95.20 | NÃO | fora do lado solicitado |
| 937 | 580.00 | 162.00 | 502.86 | 96.20 | NÃO | fora do lado solicitado |
| 938 | 579.00 | 161.00 | 502.07 | 97.20 | NÃO | fora do lado solicitado |
| 939 | 579.00 | 160.00 | 502.26 | 98.20 | NÃO | fora do lado solicitado |
| 940 | 578.00 | 159.00 | 501.47 | 99.20 | NÃO | fora do lado solicitado |
| 941 | 577.00 | 158.00 | 500.68 | 100.20 | NÃO | fora do lado solicitado |
| 942 | 577.00 | 157.00 | 500.88 | 101.20 | NÃO | fora do lado solicitado |
| 943 | 576.00 | 156.00 | 500.10 | 102.20 | NÃO | fora do lado solicitado |
| 944 | 575.00 | 155.00 | 499.32 | 103.20 | NÃO | fora do lado solicitado |
| 945 | 575.00 | 154.00 | 499.52 | 104.20 | NÃO | fora do lado solicitado |
| 946 | 574.00 | 153.00 | 498.75 | 105.20 | NÃO | fora do lado solicitado |
| 947 | 573.00 | 152.00 | 497.98 | 106.20 | NÃO | fora do lado solicitado |
| 948 | 573.00 | 151.00 | 498.19 | 107.20 | NÃO | fora do lado solicitado |
| 949 | 572.00 | 150.00 | 497.43 | 108.20 | NÃO | fora do lado solicitado |
| 950 | 571.00 | 149.00 | 496.66 | 109.20 | NÃO | fora do lado solicitado |
| 951 | 571.00 | 148.00 | 496.88 | 110.20 | NÃO | fora do lado solicitado |
| 952 | 570.00 | 147.00 | 496.12 | 111.20 | NÃO | fora do lado solicitado |
| 953 | 569.00 | 146.00 | 495.37 | 112.20 | NÃO | fora do lado solicitado |
| 954 | 568.00 | 145.00 | 494.62 | 113.20 | NÃO | fora do lado solicitado |
| 955 | 568.00 | 144.00 | 494.84 | 114.20 | NÃO | fora do lado solicitado |
| 956 | 567.00 | 143.00 | 494.10 | 115.20 | NÃO | fora do lado solicitado |
| 957 | 566.00 | 142.00 | 493.35 | 116.20 | NÃO | fora do lado solicitado |
| 958 | 565.00 | 141.00 | 492.61 | 117.20 | NÃO | fora do lado solicitado |
| 959 | 565.00 | 140.00 | 492.85 | 118.20 | NÃO | fora do lado solicitado |
| 960 | 564.00 | 139.00 | 492.11 | 119.20 | NÃO | fora do lado solicitado |
| 961 | 563.00 | 138.00 | 491.38 | 120.20 | NÃO | fora do lado solicitado |
| 962 | 562.00 | 137.00 | 490.65 | 121.20 | NÃO | fora da faixa vertical |
| 963 | 561.00 | 136.00 | 489.92 | 122.20 | NÃO | fora da faixa vertical |
| 964 | 561.00 | 135.00 | 490.17 | 123.20 | NÃO | fora da faixa vertical |
| 965 | 560.00 | 134.00 | 489.45 | 124.20 | NÃO | fora da faixa vertical |
| 966 | 559.00 | 133.00 | 488.73 | 125.20 | NÃO | fora da faixa vertical |
| 967 | 558.00 | 132.00 | 488.02 | 126.20 | NÃO | fora da faixa vertical |
| 968 | 557.00 | 131.00 | 487.30 | 127.20 | NÃO | fora da faixa vertical |
| 969 | 557.00 | 130.00 | 487.56 | 128.20 | NÃO | fora da faixa vertical |
| 970 | 556.00 | 129.00 | 486.86 | 129.20 | NÃO | fora da faixa vertical |
| 971 | 555.00 | 128.00 | 486.15 | 130.20 | NÃO | fora da faixa vertical |
| 972 | 554.00 | 127.00 | 485.45 | 131.20 | NÃO | fora da faixa vertical |
| 973 | 553.00 | 126.00 | 484.76 | 132.20 | NÃO | fora da faixa vertical |
| 974 | 552.00 | 125.00 | 484.06 | 133.20 | NÃO | fora da faixa vertical |
| 975 | 551.00 | 124.00 | 483.37 | 134.20 | NÃO | fora da faixa vertical |
| 976 | 550.00 | 123.00 | 482.69 | 135.20 | NÃO | fora da faixa vertical |
| 977 | 549.00 | 122.00 | 482.00 | 136.20 | NÃO | fora da faixa vertical |
| 978 | 548.00 | 121.00 | 481.32 | 137.20 | NÃO | fora da faixa vertical |
| 979 | 547.00 | 120.00 | 480.64 | 138.20 | NÃO | fora da faixa vertical |
| 980 | 546.00 | 119.00 | 479.97 | 139.20 | NÃO | fora da faixa vertical |
| 981 | 545.00 | 118.00 | 479.30 | 140.20 | NÃO | fora da faixa vertical |
| 982 | 545.00 | 117.00 | 479.59 | 141.20 | NÃO | fora da faixa vertical |
| 983 | 544.00 | 116.00 | 478.92 | 142.20 | NÃO | fora da faixa vertical |
| 984 | 543.00 | 115.00 | 478.26 | 143.20 | NÃO | fora da faixa vertical |
| 985 | 542.00 | 114.00 | 477.60 | 144.20 | NÃO | fora da faixa vertical |
| 986 | 541.00 | 113.00 | 476.94 | 145.20 | NÃO | fora da faixa vertical |
| 987 | 540.00 | 112.00 | 476.29 | 146.20 | NÃO | fora da faixa vertical |
| 988 | 539.00 | 111.00 | 475.64 | 147.20 | NÃO | fora da faixa vertical |
| 989 | 538.00 | 111.00 | 474.69 | 147.20 | NÃO | fora da faixa vertical |
| 990 | 537.00 | 110.00 | 474.04 | 148.20 | NÃO | fora da faixa vertical |
| 991 | 536.00 | 109.00 | 473.40 | 149.20 | NÃO | fora da faixa vertical |
| 992 | 535.00 | 108.00 | 472.76 | 150.20 | NÃO | fora da faixa vertical |
| 993 | 534.00 | 107.00 | 472.13 | 151.20 | NÃO | fora da faixa vertical |
| 994 | 533.00 | 106.00 | 471.50 | 152.20 | NÃO | fora da faixa vertical |
| 995 | 532.00 | 105.00 | 470.87 | 153.20 | NÃO | fora da faixa vertical |
| 996 | 531.00 | 104.00 | 470.24 | 154.20 | NÃO | fora da faixa vertical |
| 997 | 530.00 | 103.00 | 469.62 | 155.20 | NÃO | fora da faixa vertical |
| 998 | 529.00 | 102.00 | 469.00 | 156.20 | NÃO | fora da faixa vertical |
| 999 | 528.00 | 101.00 | 468.39 | 157.20 | NÃO | fora da faixa vertical |
| 1000 | 527.00 | 101.00 | 467.45 | 157.20 | NÃO | fora da faixa vertical |
| 1001 | 526.00 | 100.00 | 466.84 | 158.20 | NÃO | fora da faixa vertical |
| 1002 | 525.00 | 99.00 | 466.23 | 159.20 | NÃO | fora da faixa vertical |
| 1003 | 524.00 | 98.00 | 465.63 | 160.20 | NÃO | fora da faixa vertical |
| 1004 | 523.00 | 97.00 | 465.03 | 161.20 | NÃO | fora da faixa vertical |
| 1005 | 522.00 | 96.00 | 464.43 | 162.20 | NÃO | fora da faixa vertical |
| 1006 | 521.00 | 96.00 | 463.49 | 162.20 | NÃO | fora da faixa vertical |
| 1007 | 520.00 | 95.00 | 462.90 | 163.20 | NÃO | fora da faixa vertical |
| 1008 | 519.00 | 94.00 | 462.31 | 164.20 | NÃO | fora da faixa vertical |
| 1009 | 518.00 | 93.00 | 461.73 | 165.20 | NÃO | fora da faixa vertical |
| 1010 | 517.00 | 92.00 | 461.15 | 166.20 | NÃO | fora da faixa vertical |
| 1011 | 516.00 | 92.00 | 460.21 | 166.20 | NÃO | fora da faixa vertical |
| 1012 | 515.00 | 91.00 | 459.64 | 167.20 | NÃO | fora da faixa vertical |
| 1013 | 514.00 | 90.00 | 459.06 | 168.20 | NÃO | fora da faixa vertical |
| 1014 | 513.00 | 89.00 | 458.50 | 169.20 | NÃO | fora da faixa vertical |
| 1015 | 512.00 | 88.00 | 457.93 | 170.20 | NÃO | fora da faixa vertical |
| 1016 | 511.00 | 88.00 | 457.00 | 170.20 | NÃO | fora da faixa vertical |
| 1017 | 510.00 | 87.00 | 456.44 | 171.20 | NÃO | fora da faixa vertical |
| 1018 | 509.00 | 86.00 | 455.88 | 172.20 | NÃO | fora da faixa vertical |
| 1019 | 508.00 | 86.00 | 454.95 | 172.20 | NÃO | fora da faixa vertical |
| 1020 | 507.00 | 85.00 | 454.40 | 173.20 | NÃO | fora da faixa vertical |
| 1021 | 506.00 | 84.00 | 453.85 | 174.20 | NÃO | fora da faixa vertical |
| 1022 | 505.00 | 84.00 | 452.93 | 174.20 | NÃO | fora da faixa vertical |
| 1023 | 504.00 | 83.00 | 452.39 | 175.20 | NÃO | fora da faixa vertical |
| 1024 | 503.00 | 82.00 | 451.85 | 176.20 | NÃO | fora da faixa vertical |
| 1025 | 502.00 | 82.00 | 450.92 | 176.20 | NÃO | fora da faixa vertical |
| 1026 | 501.00 | 81.00 | 450.39 | 177.20 | NÃO | fora da faixa vertical |
| 1027 | 500.00 | 80.00 | 449.86 | 178.20 | NÃO | fora da faixa vertical |
| 1028 | 499.00 | 80.00 | 448.94 | 178.20 | NÃO | fora da faixa vertical |
| 1029 | 498.00 | 79.00 | 448.41 | 179.20 | NÃO | fora da faixa vertical |
| 1030 | 497.00 | 78.00 | 447.89 | 180.20 | NÃO | fora da faixa vertical |
| 1031 | 496.00 | 78.00 | 446.97 | 180.20 | NÃO | fora da faixa vertical |
| 1032 | 495.00 | 77.00 | 446.45 | 181.20 | NÃO | fora da faixa vertical |
| 1033 | 494.00 | 76.00 | 445.94 | 182.20 | NÃO | fora da faixa vertical |
| 1034 | 493.00 | 76.00 | 445.03 | 182.20 | NÃO | fora da faixa vertical |
| 1035 | 492.00 | 75.00 | 444.52 | 183.20 | NÃO | fora da faixa vertical |
| 1036 | 491.00 | 75.00 | 443.61 | 183.20 | NÃO | fora da faixa vertical |
| 1037 | 490.00 | 74.00 | 443.10 | 184.20 | NÃO | fora da faixa vertical |
| 1038 | 489.00 | 73.00 | 442.60 | 185.20 | NÃO | fora da faixa vertical |
| 1039 | 488.00 | 73.00 | 441.69 | 185.20 | NÃO | fora da faixa vertical |
| 1040 | 487.00 | 72.00 | 441.20 | 186.20 | NÃO | fora da faixa vertical |
| 1041 | 486.00 | 72.00 | 440.29 | 186.20 | NÃO | fora da faixa vertical |
| 1042 | 485.00 | 71.00 | 439.80 | 187.20 | NÃO | fora da faixa vertical |
| 1043 | 484.00 | 71.00 | 438.90 | 187.20 | NÃO | fora da faixa vertical |
| 1044 | 483.00 | 70.00 | 438.41 | 188.20 | NÃO | fora da faixa vertical |
| 1045 | 482.00 | 69.00 | 437.93 | 189.20 | NÃO | fora da faixa vertical |
| 1046 | 481.00 | 69.00 | 437.03 | 189.20 | NÃO | fora da faixa vertical |
| 1047 | 480.00 | 68.00 | 436.55 | 190.20 | NÃO | fora da faixa vertical |
| 1048 | 479.00 | 68.00 | 435.65 | 190.20 | NÃO | fora da faixa vertical |
| 1049 | 478.00 | 67.00 | 435.18 | 191.20 | NÃO | fora da faixa vertical |
| 1050 | 477.00 | 67.00 | 434.28 | 191.20 | NÃO | fora da faixa vertical |
| 1051 | 476.00 | 66.00 | 433.82 | 192.20 | NÃO | fora da faixa vertical |
| 1052 | 475.00 | 66.00 | 432.92 | 192.20 | NÃO | fora da faixa vertical |
| 1053 | 474.00 | 65.00 | 432.46 | 193.20 | NÃO | fora da faixa vertical |
| 1054 | 473.00 | 65.00 | 431.57 | 193.20 | NÃO | fora da faixa vertical |
| 1055 | 472.00 | 64.00 | 431.11 | 194.20 | NÃO | fora da faixa vertical |
| 1056 | 471.00 | 64.00 | 430.22 | 194.20 | NÃO | fora da faixa vertical |
| 1057 | 470.00 | 63.00 | 429.77 | 195.20 | NÃO | fora da faixa vertical |
| 1058 | 469.00 | 63.00 | 428.88 | 195.20 | NÃO | fora da faixa vertical |
| 1059 | 468.00 | 62.00 | 428.44 | 196.20 | NÃO | fora da faixa vertical |
| 1060 | 467.00 | 62.00 | 427.55 | 196.20 | NÃO | fora da faixa vertical |
| 1061 | 466.00 | 61.00 | 427.11 | 197.20 | NÃO | fora da faixa vertical |
| 1062 | 465.00 | 61.00 | 426.22 | 197.20 | NÃO | fora da faixa vertical |
| 1063 | 464.00 | 60.00 | 425.79 | 198.20 | NÃO | fora da faixa vertical |
| 1064 | 463.00 | 60.00 | 424.91 | 198.20 | NÃO | fora da faixa vertical |
| 1065 | 462.00 | 59.00 | 424.48 | 199.20 | NÃO | fora da faixa vertical |
| 1066 | 461.00 | 59.00 | 423.60 | 199.20 | NÃO | fora da faixa vertical |
| 1067 | 460.00 | 58.00 | 423.18 | 200.20 | NÃO | fora da faixa vertical |
| 1068 | 459.00 | 58.00 | 422.29 | 200.20 | NÃO | fora da faixa vertical |
| 1069 | 458.00 | 57.00 | 421.88 | 201.20 | NÃO | fora da faixa vertical |
| 1070 | 457.00 | 57.00 | 421.00 | 201.20 | NÃO | fora da faixa vertical |
| 1071 | 456.00 | 57.00 | 420.12 | 201.20 | NÃO | fora da faixa vertical |
| 1072 | 455.00 | 56.00 | 419.72 | 202.20 | NÃO | fora da faixa vertical |
| 1073 | 454.00 | 56.00 | 418.84 | 202.20 | NÃO | fora da faixa vertical |
| 1074 | 453.00 | 55.00 | 418.44 | 203.20 | NÃO | fora da faixa vertical |
| 1075 | 452.00 | 55.00 | 417.56 | 203.20 | NÃO | fora da faixa vertical |
| 1076 | 451.00 | 55.00 | 416.68 | 203.20 | NÃO | fora da faixa vertical |
| 1077 | 450.00 | 54.00 | 416.29 | 204.20 | NÃO | fora da faixa vertical |
| 1078 | 449.00 | 54.00 | 415.42 | 204.20 | NÃO | fora da faixa vertical |
| 1079 | 448.00 | 54.00 | 414.55 | 204.20 | NÃO | fora da faixa vertical |
| 1080 | 447.00 | 53.00 | 414.16 | 205.20 | NÃO | fora da faixa vertical |
| 1081 | 446.00 | 53.00 | 413.29 | 205.20 | NÃO | fora da faixa vertical |
| 1082 | 445.00 | 52.00 | 412.91 | 206.20 | NÃO | fora da faixa vertical |
| 1083 | 444.00 | 52.00 | 412.04 | 206.20 | NÃO | fora da faixa vertical |
| 1084 | 443.00 | 52.00 | 411.18 | 206.20 | NÃO | fora da faixa vertical |
| 1085 | 442.00 | 51.00 | 410.81 | 207.20 | NÃO | fora da faixa vertical |
| 1086 | 441.00 | 51.00 | 409.94 | 207.20 | NÃO | fora da faixa vertical |
| 1087 | 440.00 | 51.00 | 409.07 | 207.20 | NÃO | fora da faixa vertical |
| 1088 | 439.00 | 50.00 | 408.71 | 208.20 | NÃO | fora da faixa vertical |
| 1089 | 438.00 | 50.00 | 407.85 | 208.20 | NÃO | fora da faixa vertical |
| 1090 | 437.00 | 50.00 | 406.99 | 208.20 | NÃO | fora da faixa vertical |
| 1091 | 436.00 | 49.00 | 406.63 | 209.20 | NÃO | fora da faixa vertical |
| 1092 | 435.00 | 49.00 | 405.77 | 209.20 | NÃO | fora da faixa vertical |
| 1093 | 434.00 | 49.00 | 404.91 | 209.20 | NÃO | fora da faixa vertical |
| 1094 | 433.00 | 48.00 | 404.57 | 210.20 | NÃO | fora da faixa vertical |
| 1095 | 432.00 | 48.00 | 403.71 | 210.20 | NÃO | fora da faixa vertical |
| 1096 | 431.00 | 48.00 | 402.85 | 210.20 | NÃO | fora da faixa vertical |
| 1097 | 430.00 | 47.00 | 402.51 | 211.20 | NÃO | fora da faixa vertical |
| 1098 | 429.00 | 47.00 | 401.66 | 211.20 | NÃO | fora da faixa vertical |
| 1099 | 428.00 | 47.00 | 400.81 | 211.20 | NÃO | fora da faixa vertical |
| 1100 | 427.00 | 47.00 | 399.95 | 211.20 | NÃO | fora da faixa vertical |
| 1101 | 426.00 | 46.00 | 399.62 | 212.20 | NÃO | fora da faixa vertical |
| 1102 | 425.00 | 46.00 | 398.77 | 212.20 | NÃO | fora da faixa vertical |
| 1103 | 424.00 | 46.00 | 397.92 | 212.20 | NÃO | fora da faixa vertical |
| 1104 | 423.00 | 45.00 | 397.61 | 213.20 | NÃO | fora da faixa vertical |
| 1105 | 422.00 | 45.00 | 396.76 | 213.20 | NÃO | fora da faixa vertical |
| 1106 | 421.00 | 45.00 | 395.91 | 213.20 | NÃO | fora da faixa vertical |
| 1107 | 420.00 | 44.00 | 395.60 | 214.20 | NÃO | fora da faixa vertical |
| 1108 | 419.00 | 44.00 | 394.76 | 214.20 | NÃO | fora da faixa vertical |
| 1109 | 418.00 | 44.00 | 393.91 | 214.20 | NÃO | fora da faixa vertical |
| 1110 | 417.00 | 44.00 | 393.07 | 214.20 | NÃO | fora da faixa vertical |
| 1111 | 416.00 | 43.00 | 392.77 | 215.20 | NÃO | fora da faixa vertical |
| 1112 | 415.00 | 43.00 | 391.93 | 215.20 | NÃO | fora da faixa vertical |
| 1113 | 414.00 | 43.00 | 391.09 | 215.20 | NÃO | fora da faixa vertical |
| 1114 | 413.00 | 43.00 | 390.25 | 215.20 | NÃO | fora da faixa vertical |
| 1115 | 412.00 | 42.00 | 389.96 | 216.20 | NÃO | fora da faixa vertical |
| 1116 | 411.00 | 42.00 | 389.13 | 216.20 | NÃO | fora da faixa vertical |
| 1117 | 410.00 | 42.00 | 388.29 | 216.20 | NÃO | fora da faixa vertical |
| 1118 | 409.00 | 42.00 | 387.46 | 216.20 | NÃO | fora da faixa vertical |
| 1119 | 408.00 | 42.00 | 386.63 | 216.20 | NÃO | fora da faixa vertical |
| 1120 | 407.00 | 41.00 | 386.35 | 217.20 | NÃO | fora da faixa vertical |
| 1121 | 406.00 | 41.00 | 385.52 | 217.20 | NÃO | fora da faixa vertical |
| 1122 | 405.00 | 41.00 | 384.69 | 217.20 | NÃO | fora da faixa vertical |
| 1123 | 404.00 | 41.00 | 383.86 | 217.20 | NÃO | fora da faixa vertical |
| 1124 | 403.00 | 41.00 | 383.03 | 217.20 | NÃO | fora da faixa vertical |
| 1125 | 402.00 | 40.00 | 382.77 | 218.20 | NÃO | fora da faixa vertical |
| 1126 | 401.00 | 40.00 | 381.94 | 218.20 | NÃO | fora da faixa vertical |
| 1127 | 400.00 | 40.00 | 381.12 | 218.20 | NÃO | fora da faixa vertical |
| 1128 | 399.00 | 40.00 | 380.30 | 218.20 | NÃO | fora da faixa vertical |
| 1129 | 398.00 | 40.00 | 379.47 | 218.20 | NÃO | fora da faixa vertical |
| 1130 | 397.00 | 39.00 | 379.22 | 219.20 | NÃO | fora da faixa vertical |
| 1131 | 396.00 | 39.00 | 378.40 | 219.20 | NÃO | fora da faixa vertical |
| 1132 | 395.00 | 39.00 | 377.58 | 219.20 | NÃO | fora da faixa vertical |
| 1133 | 394.00 | 39.00 | 376.77 | 219.20 | NÃO | fora da faixa vertical |
| 1134 | 393.00 | 39.00 | 375.95 | 219.20 | NÃO | fora da faixa vertical |
| 1135 | 392.00 | 39.00 | 375.13 | 219.20 | NÃO | fora da faixa vertical |
| 1136 | 391.00 | 39.00 | 374.32 | 219.20 | NÃO | fora da faixa vertical |
| 1137 | 390.00 | 38.00 | 374.09 | 220.20 | NÃO | fora da faixa vertical |
| 1138 | 389.00 | 38.00 | 373.27 | 220.20 | NÃO | fora da faixa vertical |
| 1139 | 388.00 | 38.00 | 372.46 | 220.20 | NÃO | fora da faixa vertical |
| 1140 | 387.00 | 38.00 | 371.65 | 220.20 | NÃO | fora da faixa vertical |
| 1141 | 386.00 | 38.00 | 370.84 | 220.20 | NÃO | fora da faixa vertical |
| 1142 | 385.00 | 38.00 | 370.03 | 220.20 | NÃO | fora da faixa vertical |
| 1143 | 384.00 | 38.00 | 369.23 | 220.20 | NÃO | fora da faixa vertical |
| 1144 | 383.00 | 38.00 | 368.42 | 220.20 | NÃO | fora da faixa vertical |
| 1145 | 382.00 | 38.00 | 367.61 | 220.20 | NÃO | fora da faixa vertical |
| 1146 | 381.00 | 37.00 | 367.40 | 221.20 | NÃO | fora da faixa vertical |
| 1147 | 380.00 | 37.00 | 366.60 | 221.20 | NÃO | fora da faixa vertical |
| 1148 | 379.00 | 37.00 | 365.80 | 221.20 | NÃO | fora da faixa vertical |
| 1149 | 378.00 | 37.00 | 365.00 | 221.20 | NÃO | fora da faixa vertical |
| 1150 | 377.00 | 37.00 | 364.20 | 221.20 | NÃO | fora da faixa vertical |
| 1151 | 376.00 | 37.00 | 363.40 | 221.20 | NÃO | fora da faixa vertical |
| 1152 | 375.00 | 37.00 | 362.60 | 221.20 | NÃO | fora da faixa vertical |
| 1153 | 374.00 | 37.00 | 361.81 | 221.20 | NÃO | fora da faixa vertical |
| 1154 | 373.00 | 37.00 | 361.01 | 221.20 | NÃO | fora da faixa vertical |
| 1155 | 372.00 | 36.00 | 360.83 | 222.20 | NÃO | fora da faixa vertical |
| 1156 | 371.00 | 36.00 | 360.03 | 222.20 | NÃO | fora da faixa vertical |
| 1157 | 370.00 | 36.00 | 359.24 | 222.20 | NÃO | fora da faixa vertical |
| 1158 | 369.00 | 36.00 | 358.45 | 222.20 | NÃO | fora da faixa vertical |
| 1159 | 368.00 | 36.00 | 357.66 | 222.20 | NÃO | fora da faixa vertical |
| 1160 | 367.00 | 36.00 | 356.88 | 222.20 | NÃO | fora da faixa vertical |
| 1161 | 366.00 | 36.00 | 356.09 | 222.20 | NÃO | fora da faixa vertical |
| 1162 | 365.00 | 36.00 | 355.30 | 222.20 | NÃO | fora da faixa vertical |
| 1163 | 364.00 | 36.00 | 354.52 | 222.20 | NÃO | fora da faixa vertical |
| 1164 | 363.00 | 36.00 | 353.74 | 222.20 | NÃO | fora da faixa vertical |
| 1165 | 362.00 | 36.00 | 352.95 | 222.20 | NÃO | fora da faixa vertical |
| 1166 | 361.00 | 36.00 | 352.17 | 222.20 | NÃO | fora da faixa vertical |
| 1167 | 360.00 | 36.00 | 351.39 | 222.20 | NÃO | fora da faixa vertical |
| 1168 | 359.00 | 36.00 | 350.61 | 222.20 | NÃO | fora da faixa vertical |
| 1169 | 358.00 | 36.00 | 349.83 | 222.20 | NÃO | fora da faixa vertical |
| 1170 | 357.00 | 36.00 | 349.06 | 222.20 | NÃO | fora da faixa vertical |
| 1171 | 356.00 | 36.00 | 348.28 | 222.20 | NÃO | fora da faixa vertical |
| 1172 | 355.00 | 36.00 | 347.51 | 222.20 | NÃO | fora da faixa vertical |
| 1173 | 354.00 | 36.00 | 346.73 | 222.20 | NÃO | fora da faixa vertical |
| 1174 | 353.00 | 36.00 | 345.96 | 222.20 | NÃO | fora da faixa vertical |
| 1175 | 352.00 | 36.00 | 345.19 | 222.20 | NÃO | fora da faixa vertical |
| 1176 | 351.00 | 36.00 | 344.42 | 222.20 | NÃO | fora da faixa vertical |
| 1177 | 350.00 | 36.00 | 343.65 | 222.20 | NÃO | fora da faixa vertical |
| 1178 | 349.00 | 36.00 | 342.88 | 222.20 | NÃO | fora da faixa vertical |
| 1179 | 348.00 | 36.00 | 342.12 | 222.20 | NÃO | fora da faixa vertical |
| 1180 | 347.00 | 36.00 | 341.35 | 222.20 | NÃO | fora da faixa vertical |
| 1181 | 346.00 | 36.00 | 340.59 | 222.20 | NÃO | fora da faixa vertical |
| 1182 | 345.00 | 36.00 | 339.82 | 222.20 | NÃO | fora da faixa vertical |
| 1183 | 344.00 | 36.00 | 339.06 | 222.20 | NÃO | fora da faixa vertical |
| 1184 | 343.00 | 36.00 | 338.30 | 222.20 | NÃO | fora da faixa vertical |
| 1185 | 342.00 | 36.00 | 337.54 | 222.20 | NÃO | fora da faixa vertical |
| 1186 | 341.00 | 36.00 | 336.79 | 222.20 | NÃO | fora da faixa vertical |
| 1187 | 340.00 | 36.00 | 336.03 | 222.20 | NÃO | fora da faixa vertical |
| 1188 | 339.00 | 36.00 | 335.27 | 222.20 | NÃO | fora da faixa vertical |
| 1189 | 338.00 | 36.00 | 334.52 | 222.20 | NÃO | fora da faixa vertical |
| 1190 | 337.00 | 36.00 | 333.77 | 222.20 | NÃO | fora da faixa vertical |
| 1191 | 336.00 | 36.00 | 333.02 | 222.20 | NÃO | fora da faixa vertical |
| 1192 | 335.00 | 36.00 | 332.27 | 222.20 | NÃO | fora da faixa vertical |
| 1193 | 334.00 | 36.00 | 331.52 | 222.20 | NÃO | fora da faixa vertical |
| 1194 | 333.00 | 36.00 | 330.77 | 222.20 | NÃO | fora da faixa vertical |
| 1195 | 332.00 | 36.00 | 330.02 | 222.20 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 194 | 140.00 | 138.00 | 54.00 | -120.20 |
| 195 | 139.00 | 139.00 | 53.00 | -119.20 |
| 196 | 138.00 | 140.00 | 52.00 | -118.20 |
| 197 | 138.00 | 141.00 | 52.00 | -117.20 |
| 198 | 137.00 | 142.00 | 51.00 | -116.20 |
| 199 | 136.00 | 143.00 | 50.00 | -115.20 |
| 200 | 135.00 | 144.00 | 49.00 | -114.20 |
| 201 | 135.00 | 145.00 | 49.00 | -113.20 |
| 202 | 134.00 | 146.00 | 48.00 | -112.20 |
| 203 | 133.00 | 147.00 | 47.00 | -111.20 |
| 204 | 132.00 | 148.00 | 46.00 | -110.20 |
| 205 | 132.00 | 149.00 | 46.00 | -109.20 |
| 206 | 131.00 | 150.00 | 45.00 | -108.20 |
| 207 | 130.00 | 151.00 | 44.00 | -107.20 |
| 208 | 130.00 | 152.00 | 44.00 | -106.20 |
| 209 | 129.00 | 153.00 | 43.00 | -105.20 |
| 210 | 128.00 | 154.00 | 42.00 | -104.20 |
| 211 | 128.00 | 155.00 | 42.00 | -103.20 |
| 212 | 127.00 | 156.00 | 41.00 | -102.20 |
| 213 | 126.00 | 157.00 | 40.00 | -101.20 |
| 214 | 126.00 | 158.00 | 40.00 | -100.20 |
| 215 | 125.00 | 159.00 | 39.00 | -99.20 |
| 216 | 124.00 | 160.00 | 38.00 | -98.20 |
| 217 | 124.00 | 161.00 | 38.00 | -97.20 |
| 218 | 123.00 | 162.00 | 37.00 | -96.20 |
| 219 | 122.00 | 163.00 | 36.00 | -95.20 |
| 220 | 122.00 | 164.00 | 36.00 | -94.20 |
| 221 | 121.00 | 165.00 | 35.00 | -93.20 |
| 222 | 121.00 | 166.00 | 35.00 | -92.20 |
| 223 | 120.00 | 167.00 | 34.00 | -91.20 |
| 224 | 119.00 | 168.00 | 33.00 | -90.20 |
| 225 | 119.00 | 169.00 | 33.00 | -89.20 |
| 226 | 118.00 | 170.00 | 32.00 | -88.20 |
| 227 | 118.00 | 171.00 | 32.00 | -87.20 |
| 228 | 117.00 | 172.00 | 31.00 | -86.20 |
| 229 | 117.00 | 173.00 | 31.00 | -85.20 |
| 230 | 116.00 | 174.00 | 30.00 | -84.20 |
| 231 | 115.00 | 175.00 | 29.00 | -83.20 |
| 232 | 115.00 | 176.00 | 29.00 | -82.20 |
| 233 | 114.00 | 177.00 | 28.00 | -81.20 |
| 234 | 114.00 | 178.00 | 28.00 | -80.20 |
| 235 | 113.00 | 179.00 | 27.00 | -79.20 |
| 236 | 113.00 | 180.00 | 27.00 | -78.20 |
| 237 | 112.00 | 181.00 | 26.00 | -77.20 |
| 238 | 112.00 | 182.00 | 26.00 | -76.20 |
| 239 | 111.00 | 183.00 | 25.00 | -75.20 |
| 240 | 111.00 | 184.00 | 25.00 | -74.20 |
| 241 | 110.00 | 185.00 | 24.00 | -73.20 |
| 242 | 110.00 | 186.00 | 24.00 | -72.20 |
| 243 | 109.00 | 187.00 | 23.00 | -71.20 |
| 244 | 109.00 | 188.00 | 23.00 | -70.20 |
| 245 | 108.00 | 189.00 | 22.00 | -69.20 |
| 246 | 108.00 | 190.00 | 22.00 | -68.20 |
| 247 | 107.00 | 191.00 | 21.00 | -67.20 |
| 248 | 107.00 | 192.00 | 21.00 | -66.20 |
| 249 | 106.00 | 193.00 | 20.00 | -65.20 |
| 250 | 106.00 | 194.00 | 20.00 | -64.20 |
| 251 | 105.00 | 195.00 | 19.00 | -63.20 |
| 252 | 105.00 | 196.00 | 19.00 | -62.20 |
| 253 | 104.00 | 197.00 | 18.00 | -61.20 |
| 254 | 104.00 | 198.00 | 18.00 | -60.20 |
| 255 | 103.00 | 199.00 | 17.00 | -59.20 |
| 256 | 103.00 | 200.00 | 17.00 | -58.20 |
| 257 | 103.00 | 201.00 | 17.00 | -57.20 |
| 258 | 102.00 | 202.00 | 16.00 | -56.20 |
| 259 | 102.00 | 203.00 | 16.00 | -55.20 |
| 260 | 102.00 | 204.00 | 16.00 | -54.20 |
| 261 | 101.00 | 205.00 | 15.00 | -53.20 |
| 262 | 101.00 | 206.00 | 15.00 | -52.20 |
| 263 | 100.00 | 207.00 | 14.00 | -51.20 |
| 264 | 100.00 | 208.00 | 14.00 | -50.20 |
| 265 | 100.00 | 209.00 | 14.00 | -49.20 |
| 266 | 99.00 | 210.00 | 13.00 | -48.20 |
| 267 | 99.00 | 211.00 | 13.00 | -47.20 |
| 268 | 99.00 | 212.00 | 13.00 | -46.20 |
| 269 | 98.00 | 213.00 | 12.00 | -45.20 |
| 270 | 98.00 | 214.00 | 12.00 | -44.20 |
| 271 | 97.00 | 215.00 | 11.00 | -43.20 |
| 272 | 97.00 | 216.00 | 11.00 | -42.20 |
| 273 | 97.00 | 217.00 | 11.00 | -41.20 |
| 274 | 96.00 | 218.00 | 10.00 | -40.20 |
| 275 | 96.00 | 219.00 | 10.00 | -39.20 |
| 276 | 96.00 | 220.00 | 10.00 | -38.20 |
| 277 | 95.00 | 221.00 | 9.00 | -37.20 |
| 278 | 95.00 | 222.00 | 9.00 | -36.20 |
| 279 | 95.00 | 223.00 | 9.00 | -35.20 |
| 280 | 94.00 | 224.00 | 8.00 | -34.20 |
| 281 | 94.00 | 225.00 | 8.00 | -33.20 |
| 282 | 94.00 | 226.00 | 8.00 | -32.20 |
| 283 | 94.00 | 227.00 | 8.00 | -31.20 |
| 284 | 93.00 | 228.00 | 7.00 | -30.20 |
| 285 | 93.00 | 229.00 | 7.00 | -29.20 |
| 286 | 93.00 | 230.00 | 7.00 | -28.20 |
| 287 | 92.00 | 231.00 | 6.00 | -27.20 |
| 288 | 92.00 | 232.00 | 6.00 | -26.20 |
| 289 | 92.00 | 233.00 | 6.00 | -25.20 |
| 290 | 91.00 | 234.00 | 5.00 | -24.20 |
| 291 | 91.00 | 235.00 | 5.00 | -23.20 |
| 292 | 91.00 | 236.00 | 5.00 | -22.20 |
| 293 | 91.00 | 237.00 | 5.00 | -21.20 |
| 294 | 90.00 | 238.00 | 4.00 | -20.20 |
| 295 | 90.00 | 239.00 | 4.00 | -19.20 |
| 296 | 90.00 | 240.00 | 4.00 | -18.20 |
| 297 | 90.00 | 241.00 | 4.00 | -17.20 |
| 298 | 89.00 | 242.00 | 3.00 | -16.20 |
| 299 | 89.00 | 243.00 | 3.00 | -15.20 |
| 300 | 89.00 | 244.00 | 3.00 | -14.20 |
| 301 | 89.00 | 245.00 | 3.00 | -13.20 |
| 302 | 88.00 | 246.00 | 2.00 | -12.20 |
| 303 | 88.00 | 247.00 | 2.00 | -11.20 |
| 304 | 88.00 | 248.00 | 2.00 | -10.20 |
| 305 | 88.00 | 249.00 | 2.00 | -9.20 |
| 306 | 88.00 | 250.00 | 2.00 | -8.20 |
| 307 | 87.00 | 251.00 | 1.00 | -7.20 |
| 308 | 87.00 | 252.00 | 1.00 | -6.20 |
| 309 | 87.00 | 253.00 | 1.00 | -5.20 |
| 310 | 87.00 | 254.00 | 1.00 | -4.20 |
| 311 | 87.00 | 255.00 | 1.00 | -3.20 |
| 312 | 86.00 | 256.00 | 0.00 | -2.20 |
| 313 | 87.00 | 256.00 | 1.00 | -2.20 |
| 314 | 88.00 | 256.00 | 2.00 | -2.20 |
| 315 | 89.00 | 256.00 | 3.00 | -2.20 |
| 316 | 90.00 | 256.00 | 4.00 | -2.20 |
| 317 | 91.00 | 256.00 | 5.00 | -2.20 |
| 318 | 92.00 | 256.00 | 6.00 | -2.20 |
| 319 | 93.00 | 256.00 | 7.00 | -2.20 |
| 320 | 94.00 | 256.00 | 8.00 | -2.20 |
| 321 | 95.00 | 256.00 | 9.00 | -2.20 |
| 322 | 96.00 | 256.00 | 10.00 | -2.20 |
| 323 | 97.00 | 256.00 | 11.00 | -2.20 |
| 324 | 98.00 | 256.00 | 12.00 | -2.20 |
| 325 | 99.00 | 256.00 | 13.00 | -2.20 |
| 326 | 100.00 | 256.00 | 14.00 | -2.20 |
| 327 | 101.00 | 256.00 | 15.00 | -2.20 |
| 328 | 102.00 | 256.00 | 16.00 | -2.20 |
| 329 | 103.00 | 256.00 | 17.00 | -2.20 |
| 330 | 104.00 | 256.00 | 18.00 | -2.20 |
| 331 | 105.00 | 256.00 | 19.00 | -2.20 |
| 332 | 106.00 | 256.00 | 20.00 | -2.20 |
| 333 | 107.00 | 256.00 | 21.00 | -2.20 |
| 334 | 108.00 | 256.00 | 22.00 | -2.20 |
| 335 | 109.00 | 256.00 | 23.00 | -2.20 |
| 336 | 110.00 | 256.00 | 24.00 | -2.20 |
| 337 | 111.00 | 256.00 | 25.00 | -2.20 |
| 338 | 112.00 | 256.00 | 26.00 | -2.20 |
| 339 | 113.00 | 256.00 | 27.00 | -2.20 |
| 340 | 114.00 | 256.00 | 28.00 | -2.20 |
| 341 | 115.00 | 256.00 | 29.00 | -2.20 |
| 342 | 116.00 | 256.00 | 30.00 | -2.20 |
| 343 | 117.00 | 256.00 | 31.00 | -2.20 |
| 344 | 118.00 | 256.00 | 32.00 | -2.20 |
| 345 | 119.00 | 256.00 | 33.00 | -2.20 |
| 346 | 120.00 | 256.00 | 34.00 | -2.20 |
| 347 | 121.00 | 256.00 | 35.00 | -2.20 |
| 348 | 122.00 | 256.00 | 36.00 | -2.20 |
| 349 | 123.00 | 256.00 | 37.00 | -2.20 |
| 350 | 124.00 | 256.00 | 38.00 | -2.20 |
| 351 | 125.00 | 256.00 | 39.00 | -2.20 |
| 352 | 126.00 | 256.00 | 40.00 | -2.20 |
| 353 | 127.00 | 256.00 | 41.00 | -2.20 |
| 354 | 128.00 | 256.00 | 42.00 | -2.20 |
| 355 | 129.00 | 256.00 | 43.00 | -2.20 |
| 356 | 130.00 | 256.00 | 44.00 | -2.20 |
| 357 | 131.00 | 256.00 | 45.00 | -2.20 |
| 358 | 132.00 | 256.00 | 46.00 | -2.20 |
| 359 | 133.00 | 256.00 | 47.00 | -2.20 |
| 360 | 134.00 | 256.00 | 48.00 | -2.20 |
| 361 | 135.00 | 256.00 | 49.00 | -2.20 |
| 362 | 136.00 | 256.00 | 50.00 | -2.20 |
| 363 | 137.00 | 256.00 | 51.00 | -2.20 |
| 364 | 138.00 | 256.00 | 52.00 | -2.20 |
| 365 | 139.00 | 256.00 | 53.00 | -2.20 |
| 366 | 140.00 | 256.00 | 54.00 | -2.20 |
| 367 | 141.00 | 256.00 | 55.00 | -2.20 |
| 368 | 142.00 | 256.00 | 56.00 | -2.20 |
| 369 | 143.00 | 256.00 | 57.00 | -2.20 |
| 370 | 144.00 | 256.00 | 58.00 | -2.20 |
| 371 | 145.00 | 256.00 | 59.00 | -2.20 |
| 372 | 146.00 | 256.00 | 60.00 | -2.20 |
| 373 | 147.00 | 256.00 | 61.00 | -2.20 |
| 374 | 148.00 | 256.00 | 62.00 | -2.20 |
| 375 | 149.00 | 256.00 | 63.00 | -2.20 |
| 376 | 150.00 | 256.00 | 64.00 | -2.20 |
| 377 | 151.00 | 256.00 | 65.00 | -2.20 |
| 378 | 152.00 | 256.00 | 66.00 | -2.20 |
| 379 | 153.00 | 256.00 | 67.00 | -2.20 |
| 380 | 154.00 | 256.00 | 68.00 | -2.20 |
| 381 | 155.00 | 256.00 | 69.00 | -2.20 |
| 382 | 156.00 | 256.00 | 70.00 | -2.20 |
| 383 | 157.00 | 256.00 | 71.00 | -2.20 |
| 384 | 158.00 | 256.00 | 72.00 | -2.20 |
| 385 | 159.00 | 256.00 | 73.00 | -2.20 |
| 386 | 160.00 | 256.00 | 74.00 | -2.20 |
| 387 | 161.00 | 256.00 | 75.00 | -2.20 |
| 388 | 162.00 | 256.00 | 76.00 | -2.20 |
| 389 | 163.00 | 256.00 | 77.00 | -2.20 |
| 390 | 164.00 | 256.00 | 78.00 | -2.20 |
| 391 | 165.00 | 256.00 | 79.00 | -2.20 |
| 392 | 166.00 | 256.00 | 80.00 | -2.20 |
| 393 | 167.00 | 256.00 | 81.00 | -2.20 |
| 394 | 168.00 | 256.00 | 82.00 | -2.20 |
| 395 | 169.00 | 256.00 | 83.00 | -2.20 |
| 396 | 170.00 | 256.00 | 84.00 | -2.20 |
| 397 | 171.00 | 256.00 | 85.00 | -2.20 |
| 398 | 172.00 | 256.00 | 86.00 | -2.20 |
| 399 | 173.00 | 256.00 | 87.00 | -2.20 |
| 400 | 174.00 | 256.00 | 88.00 | -2.20 |
| 401 | 175.00 | 256.00 | 89.00 | -2.20 |
| 402 | 176.00 | 256.00 | 90.00 | -2.20 |
| 403 | 177.00 | 256.00 | 91.00 | -2.20 |
| 404 | 178.00 | 256.00 | 92.00 | -2.20 |
| 405 | 179.00 | 256.00 | 93.00 | -2.20 |
| 406 | 180.00 | 256.00 | 94.00 | -2.20 |
| 407 | 181.00 | 256.00 | 95.00 | -2.20 |
| 408 | 182.00 | 256.00 | 96.00 | -2.20 |
| 409 | 183.00 | 256.00 | 97.00 | -2.20 |
| 410 | 184.00 | 256.00 | 98.00 | -2.20 |
| 411 | 185.00 | 256.00 | 99.00 | -2.20 |
| 412 | 186.00 | 256.00 | 100.00 | -2.20 |
| 413 | 187.00 | 256.00 | 101.00 | -2.20 |
| 414 | 188.00 | 256.00 | 102.00 | -2.20 |
| 415 | 189.00 | 256.00 | 103.00 | -2.20 |
| 416 | 190.00 | 256.00 | 104.00 | -2.20 |
| 417 | 191.00 | 256.00 | 105.00 | -2.20 |
| 418 | 192.00 | 256.00 | 106.00 | -2.20 |
| 419 | 193.00 | 256.00 | 107.00 | -2.20 |
| 420 | 194.00 | 256.00 | 108.00 | -2.20 |
| 421 | 195.00 | 256.00 | 109.00 | -2.20 |
| 422 | 196.00 | 256.00 | 110.00 | -2.20 |
| 423 | 197.00 | 256.00 | 111.00 | -2.20 |
| 424 | 198.00 | 256.00 | 112.00 | -2.20 |
| 425 | 199.00 | 256.00 | 113.00 | -2.20 |
| 426 | 200.00 | 256.00 | 114.00 | -2.20 |
| 427 | 201.00 | 256.00 | 115.00 | -2.20 |
| 428 | 202.00 | 256.00 | 116.00 | -2.20 |
| 429 | 203.00 | 256.00 | 117.00 | -2.20 |
| 430 | 204.00 | 256.00 | 118.00 | -2.20 |
| 431 | 205.00 | 256.00 | 119.00 | -2.20 |
| 432 | 206.00 | 256.00 | 120.00 | -2.20 |
| 433 | 207.00 | 256.00 | 121.00 | -2.20 |
| 434 | 208.00 | 256.00 | 122.00 | -2.20 |
| 435 | 209.00 | 256.00 | 123.00 | -2.20 |
| 436 | 210.00 | 256.00 | 124.00 | -2.20 |
| 437 | 211.00 | 256.00 | 125.00 | -2.20 |
| 438 | 212.00 | 256.00 | 126.00 | -2.20 |
| 439 | 213.00 | 256.00 | 127.00 | -2.20 |
| 440 | 214.00 | 256.00 | 128.00 | -2.20 |
| 441 | 215.00 | 256.00 | 129.00 | -2.20 |
| 442 | 216.00 | 256.00 | 130.00 | -2.20 |
| 443 | 217.00 | 256.00 | 131.00 | -2.20 |
| 444 | 218.00 | 256.00 | 132.00 | -2.20 |
| 445 | 219.00 | 256.00 | 133.00 | -2.20 |
| 446 | 220.00 | 256.00 | 134.00 | -2.20 |
| 447 | 221.00 | 256.00 | 135.00 | -2.20 |
| 448 | 222.00 | 256.00 | 136.00 | -2.20 |
| 449 | 223.00 | 256.00 | 137.00 | -2.20 |
| 450 | 224.00 | 256.00 | 138.00 | -2.20 |
| 451 | 225.00 | 256.00 | 139.00 | -2.20 |
| 452 | 226.00 | 256.00 | 140.00 | -2.20 |
| 453 | 227.00 | 256.00 | 141.00 | -2.20 |
| 454 | 228.00 | 256.00 | 142.00 | -2.20 |
| 455 | 229.00 | 256.00 | 143.00 | -2.20 |
| 456 | 230.00 | 256.00 | 144.00 | -2.20 |
| 457 | 231.00 | 256.00 | 145.00 | -2.20 |
| 458 | 232.00 | 256.00 | 146.00 | -2.20 |
| 459 | 233.00 | 256.00 | 147.00 | -2.20 |
| 460 | 234.00 | 256.00 | 148.00 | -2.20 |
| 461 | 235.00 | 256.00 | 149.00 | -2.20 |
| 462 | 236.00 | 256.00 | 150.00 | -2.20 |
| 463 | 237.00 | 256.00 | 151.00 | -2.20 |
| 464 | 238.00 | 256.00 | 152.00 | -2.20 |
| 465 | 239.00 | 256.00 | 153.00 | -2.20 |
| 466 | 240.00 | 256.00 | 154.00 | -2.20 |
| 467 | 241.00 | 256.00 | 155.00 | -2.20 |
| 468 | 242.00 | 256.00 | 156.00 | -2.20 |
| 469 | 243.00 | 256.00 | 157.00 | -2.20 |
| 470 | 244.00 | 256.00 | 158.00 | -2.20 |
| 471 | 245.00 | 256.00 | 159.00 | -2.20 |
| 472 | 246.00 | 256.00 | 160.00 | -2.20 |
| 473 | 247.00 | 256.00 | 161.00 | -2.20 |
| 474 | 248.00 | 256.00 | 162.00 | -2.20 |
| 475 | 249.00 | 256.00 | 163.00 | -2.20 |
| 476 | 250.00 | 256.00 | 164.00 | -2.20 |
| 477 | 251.00 | 256.00 | 165.00 | -2.20 |
| 478 | 252.00 | 256.00 | 166.00 | -2.20 |
| 479 | 253.00 | 256.00 | 167.00 | -2.20 |
| 480 | 254.00 | 256.00 | 168.00 | -2.20 |
| 481 | 255.00 | 256.00 | 169.00 | -2.20 |
| 482 | 256.00 | 256.00 | 170.00 | -2.20 |
| 483 | 257.00 | 256.00 | 171.00 | -2.20 |
| 484 | 258.00 | 256.00 | 172.00 | -2.20 |
| 485 | 259.00 | 256.00 | 173.00 | -2.20 |
| 486 | 260.00 | 256.00 | 174.00 | -2.20 |
| 487 | 261.00 | 256.00 | 175.00 | -2.20 |
| 488 | 262.00 | 256.00 | 176.00 | -2.20 |
| 489 | 263.00 | 256.00 | 177.00 | -2.20 |
| 490 | 264.00 | 256.00 | 178.00 | -2.20 |
| 491 | 265.00 | 256.00 | 179.00 | -2.20 |
| 492 | 266.00 | 256.00 | 180.00 | -2.20 |
| 493 | 267.00 | 256.00 | 181.00 | -2.20 |
| 494 | 268.00 | 256.00 | 182.00 | -2.20 |
| 495 | 269.00 | 256.00 | 183.00 | -2.20 |
| 496 | 270.00 | 256.00 | 184.00 | -2.20 |
| 497 | 271.00 | 256.00 | 185.00 | -2.20 |
| 498 | 272.00 | 256.00 | 186.00 | -2.20 |
| 499 | 273.00 | 256.00 | 187.00 | -2.20 |
| 500 | 274.00 | 256.00 | 188.00 | -2.20 |
| 501 | 275.00 | 256.00 | 189.00 | -2.20 |
| 502 | 276.00 | 256.00 | 190.00 | -2.20 |
| 503 | 277.00 | 256.00 | 191.00 | -2.20 |
| 504 | 278.00 | 256.00 | 192.00 | -2.20 |
| 505 | 279.00 | 256.00 | 193.00 | -2.20 |
| 506 | 280.00 | 256.00 | 194.00 | -2.20 |
| 507 | 281.00 | 256.00 | 195.00 | -2.20 |
| 508 | 282.00 | 256.00 | 196.00 | -2.20 |
| 509 | 283.00 | 256.00 | 197.00 | -2.20 |
| 510 | 284.00 | 256.00 | 198.00 | -2.20 |
| 511 | 285.00 | 256.00 | 199.00 | -2.20 |
| 512 | 286.00 | 256.00 | 200.00 | -2.20 |
| 513 | 287.00 | 256.00 | 201.00 | -2.20 |
| 514 | 288.00 | 256.00 | 202.00 | -2.20 |
| 515 | 289.00 | 256.00 | 203.00 | -2.20 |
| 516 | 290.00 | 256.00 | 204.00 | -2.20 |
| 517 | 291.00 | 256.00 | 205.00 | -2.20 |
| 518 | 292.00 | 256.00 | 206.00 | -2.20 |
| 519 | 293.00 | 256.00 | 207.00 | -2.20 |
| 520 | 294.00 | 256.00 | 208.00 | -2.20 |
| 521 | 295.00 | 256.00 | 209.00 | -2.20 |
| 522 | 296.00 | 256.00 | 210.00 | -2.20 |
| 523 | 297.00 | 256.00 | 211.00 | -2.20 |
| 524 | 298.00 | 256.00 | 212.00 | -2.20 |
| 525 | 299.00 | 256.00 | 213.00 | -2.20 |
| 526 | 300.00 | 256.00 | 214.00 | -2.20 |
| 527 | 301.00 | 256.00 | 215.00 | -2.20 |
| 528 | 302.00 | 256.00 | 216.00 | -2.20 |
| 529 | 303.00 | 256.00 | 217.00 | -2.20 |
| 530 | 304.00 | 256.00 | 218.00 | -2.20 |
| 531 | 305.00 | 256.00 | 219.00 | -2.20 |
| 532 | 306.00 | 256.00 | 220.00 | -2.20 |
| 533 | 307.00 | 256.00 | 221.00 | -2.20 |
| 534 | 308.00 | 256.00 | 222.00 | -2.20 |
| 535 | 309.00 | 256.00 | 223.00 | -2.20 |
| 536 | 310.00 | 256.00 | 224.00 | -2.20 |
| 537 | 311.00 | 256.00 | 225.00 | -2.20 |
| 538 | 312.00 | 256.00 | 226.00 | -2.20 |
| 539 | 313.00 | 256.00 | 227.00 | -2.20 |
| 540 | 314.00 | 256.00 | 228.00 | -2.20 |
| 541 | 315.00 | 256.00 | 229.00 | -2.20 |
| 542 | 316.00 | 256.00 | 230.00 | -2.20 |
| 543 | 317.00 | 256.00 | 231.00 | -2.20 |
| 544 | 318.00 | 256.00 | 232.00 | -2.20 |
| 545 | 319.00 | 256.00 | 233.00 | -2.20 |
| 546 | 320.00 | 256.00 | 234.00 | -2.20 |
| 547 | 321.00 | 256.00 | 235.00 | -2.20 |
| 548 | 322.00 | 256.00 | 236.00 | -2.20 |
| 549 | 323.00 | 256.00 | 237.00 | -2.20 |
| 550 | 324.00 | 256.00 | 238.00 | -2.20 |
| 551 | 325.00 | 256.00 | 239.00 | -2.20 |
| 552 | 326.00 | 256.00 | 240.00 | -2.20 |
| 553 | 327.00 | 256.00 | 241.00 | -2.20 |
| 554 | 328.00 | 256.00 | 242.00 | -2.20 |
| 555 | 329.00 | 256.00 | 243.00 | -2.20 |
| 556 | 330.00 | 256.00 | 244.00 | -2.20 |
| 557 | 331.00 | 256.00 | 245.00 | -2.20 |
| 558 | 332.00 | 256.00 | 246.00 | -2.20 |
| 559 | 333.00 | 256.00 | 247.00 | -2.20 |
| 560 | 334.00 | 256.00 | 248.00 | -2.20 |
| 561 | 335.00 | 256.00 | 249.00 | -2.20 |
| 562 | 336.00 | 256.00 | 250.00 | -2.20 |
| 563 | 337.00 | 256.00 | 251.00 | -2.20 |
| 564 | 338.00 | 256.00 | 252.00 | -2.20 |
| 565 | 339.00 | 256.00 | 253.00 | -2.20 |
| 566 | 340.00 | 256.00 | 254.00 | -2.20 |
| 567 | 341.00 | 256.00 | 255.00 | -2.20 |
| 568 | 342.00 | 256.00 | 256.00 | -2.20 |
| 569 | 343.00 | 256.00 | 257.00 | -2.20 |
| 570 | 344.00 | 256.00 | 258.00 | -2.20 |
| 571 | 345.00 | 256.00 | 259.00 | -2.20 |
| 572 | 346.00 | 256.00 | 260.00 | -2.20 |
| 573 | 347.00 | 256.00 | 261.00 | -2.20 |
| 574 | 348.00 | 256.00 | 262.00 | -2.20 |
| 575 | 349.00 | 256.00 | 263.00 | -2.20 |
| 576 | 350.00 | 256.00 | 264.00 | -2.20 |
| 577 | 351.00 | 256.00 | 265.00 | -2.20 |

- primeiro índice: 194
- último índice: 577
- quantidade: 384
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![100_geo esq](audit_outputs/75_geo_esq_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![100_geo esq polyfit](audit_outputs/75_geo_esq_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

### Lado: dir

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 1196
- ponto de contato recebido: [617.0, 256.0]
- baseline_y: 256.0
- baseline_ajustada: 258.2
- lado solicitado: dir
- largura da região: 121 px
- altura da gota: 220.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 331.00 | 36.00 | 360.83 | 222.20 | NÃO | fora da faixa vertical |
| 1 | 330.00 | 37.00 | 361.01 | 221.20 | NÃO | fora da faixa vertical |
| 2 | 329.00 | 37.00 | 361.81 | 221.20 | NÃO | fora da faixa vertical |
| 3 | 328.00 | 37.00 | 362.60 | 221.20 | NÃO | fora da faixa vertical |
| 4 | 327.00 | 37.00 | 363.40 | 221.20 | NÃO | fora da faixa vertical |
| 5 | 326.00 | 37.00 | 364.20 | 221.20 | NÃO | fora da faixa vertical |
| 6 | 325.00 | 37.00 | 365.00 | 221.20 | NÃO | fora da faixa vertical |
| 7 | 324.00 | 37.00 | 365.80 | 221.20 | NÃO | fora da faixa vertical |
| 8 | 323.00 | 37.00 | 366.60 | 221.20 | NÃO | fora da faixa vertical |
| 9 | 322.00 | 37.00 | 367.40 | 221.20 | NÃO | fora da faixa vertical |
| 10 | 321.00 | 38.00 | 367.61 | 220.20 | NÃO | fora da faixa vertical |
| 11 | 320.00 | 38.00 | 368.42 | 220.20 | NÃO | fora da faixa vertical |
| 12 | 319.00 | 38.00 | 369.23 | 220.20 | NÃO | fora da faixa vertical |
| 13 | 318.00 | 38.00 | 370.03 | 220.20 | NÃO | fora da faixa vertical |
| 14 | 317.00 | 38.00 | 370.84 | 220.20 | NÃO | fora da faixa vertical |
| 15 | 316.00 | 38.00 | 371.65 | 220.20 | NÃO | fora da faixa vertical |
| 16 | 315.00 | 38.00 | 372.46 | 220.20 | NÃO | fora da faixa vertical |
| 17 | 314.00 | 38.00 | 373.27 | 220.20 | NÃO | fora da faixa vertical |
| 18 | 313.00 | 38.00 | 374.09 | 220.20 | NÃO | fora da faixa vertical |
| 19 | 312.00 | 39.00 | 374.32 | 219.20 | NÃO | fora da faixa vertical |
| 20 | 311.00 | 39.00 | 375.13 | 219.20 | NÃO | fora da faixa vertical |
| 21 | 310.00 | 39.00 | 375.95 | 219.20 | NÃO | fora da faixa vertical |
| 22 | 309.00 | 39.00 | 376.77 | 219.20 | NÃO | fora da faixa vertical |
| 23 | 308.00 | 39.00 | 377.58 | 219.20 | NÃO | fora da faixa vertical |
| 24 | 307.00 | 39.00 | 378.40 | 219.20 | NÃO | fora da faixa vertical |
| 25 | 306.00 | 39.00 | 379.22 | 219.20 | NÃO | fora da faixa vertical |
| 26 | 305.00 | 40.00 | 379.47 | 218.20 | NÃO | fora da faixa vertical |
| 27 | 304.00 | 40.00 | 380.30 | 218.20 | NÃO | fora da faixa vertical |
| 28 | 303.00 | 40.00 | 381.12 | 218.20 | NÃO | fora da faixa vertical |
| 29 | 302.00 | 40.00 | 381.94 | 218.20 | NÃO | fora da faixa vertical |
| 30 | 301.00 | 40.00 | 382.77 | 218.20 | NÃO | fora da faixa vertical |
| 31 | 300.00 | 41.00 | 383.03 | 217.20 | NÃO | fora da faixa vertical |
| 32 | 299.00 | 41.00 | 383.86 | 217.20 | NÃO | fora da faixa vertical |
| 33 | 298.00 | 41.00 | 384.69 | 217.20 | NÃO | fora da faixa vertical |
| 34 | 297.00 | 41.00 | 385.52 | 217.20 | NÃO | fora da faixa vertical |
| 35 | 296.00 | 41.00 | 386.35 | 217.20 | NÃO | fora da faixa vertical |
| 36 | 295.00 | 42.00 | 386.63 | 216.20 | NÃO | fora da faixa vertical |
| 37 | 294.00 | 42.00 | 387.46 | 216.20 | NÃO | fora da faixa vertical |
| 38 | 293.00 | 42.00 | 388.29 | 216.20 | NÃO | fora da faixa vertical |
| 39 | 292.00 | 42.00 | 389.13 | 216.20 | NÃO | fora da faixa vertical |
| 40 | 291.00 | 42.00 | 389.96 | 216.20 | NÃO | fora da faixa vertical |
| 41 | 290.00 | 43.00 | 390.25 | 215.20 | NÃO | fora da faixa vertical |
| 42 | 289.00 | 43.00 | 391.09 | 215.20 | NÃO | fora da faixa vertical |
| 43 | 288.00 | 43.00 | 391.93 | 215.20 | NÃO | fora da faixa vertical |
| 44 | 287.00 | 43.00 | 392.77 | 215.20 | NÃO | fora da faixa vertical |
| 45 | 286.00 | 44.00 | 393.07 | 214.20 | NÃO | fora da faixa vertical |
| 46 | 285.00 | 44.00 | 393.91 | 214.20 | NÃO | fora da faixa vertical |
| 47 | 284.00 | 44.00 | 394.76 | 214.20 | NÃO | fora da faixa vertical |
| 48 | 283.00 | 44.00 | 395.60 | 214.20 | NÃO | fora da faixa vertical |
| 49 | 282.00 | 45.00 | 395.91 | 213.20 | NÃO | fora da faixa vertical |
| 50 | 281.00 | 45.00 | 396.76 | 213.20 | NÃO | fora da faixa vertical |
| 51 | 280.00 | 45.00 | 397.61 | 213.20 | NÃO | fora da faixa vertical |
| 52 | 279.00 | 46.00 | 397.92 | 212.20 | NÃO | fora da faixa vertical |
| 53 | 278.00 | 46.00 | 398.77 | 212.20 | NÃO | fora da faixa vertical |
| 54 | 277.00 | 46.00 | 399.62 | 212.20 | NÃO | fora da faixa vertical |
| 55 | 276.00 | 47.00 | 399.95 | 211.20 | NÃO | fora da faixa vertical |
| 56 | 275.00 | 47.00 | 400.81 | 211.20 | NÃO | fora da faixa vertical |
| 57 | 274.00 | 47.00 | 401.66 | 211.20 | NÃO | fora da faixa vertical |
| 58 | 273.00 | 47.00 | 402.51 | 211.20 | NÃO | fora da faixa vertical |
| 59 | 272.00 | 48.00 | 402.85 | 210.20 | NÃO | fora da faixa vertical |
| 60 | 271.00 | 48.00 | 403.71 | 210.20 | NÃO | fora da faixa vertical |
| 61 | 270.00 | 48.00 | 404.57 | 210.20 | NÃO | fora da faixa vertical |
| 62 | 269.00 | 49.00 | 404.91 | 209.20 | NÃO | fora da faixa vertical |
| 63 | 268.00 | 49.00 | 405.77 | 209.20 | NÃO | fora da faixa vertical |
| 64 | 267.00 | 49.00 | 406.63 | 209.20 | NÃO | fora da faixa vertical |
| 65 | 266.00 | 49.00 | 407.49 | 209.20 | NÃO | fora da faixa vertical |
| 66 | 265.00 | 50.00 | 407.85 | 208.20 | NÃO | fora da faixa vertical |
| 67 | 264.00 | 50.00 | 408.71 | 208.20 | NÃO | fora da faixa vertical |
| 68 | 263.00 | 51.00 | 409.07 | 207.20 | NÃO | fora da faixa vertical |
| 69 | 262.00 | 51.00 | 409.94 | 207.20 | NÃO | fora da faixa vertical |
| 70 | 261.00 | 51.00 | 410.81 | 207.20 | NÃO | fora da faixa vertical |
| 71 | 260.00 | 52.00 | 411.18 | 206.20 | NÃO | fora da faixa vertical |
| 72 | 259.00 | 52.00 | 412.04 | 206.20 | NÃO | fora da faixa vertical |
| 73 | 258.00 | 52.00 | 412.91 | 206.20 | NÃO | fora da faixa vertical |
| 74 | 257.00 | 53.00 | 413.29 | 205.20 | NÃO | fora da faixa vertical |
| 75 | 256.00 | 53.00 | 414.16 | 205.20 | NÃO | fora da faixa vertical |
| 76 | 255.00 | 53.00 | 415.03 | 205.20 | NÃO | fora da faixa vertical |
| 77 | 254.00 | 54.00 | 415.42 | 204.20 | NÃO | fora da faixa vertical |
| 78 | 253.00 | 54.00 | 416.29 | 204.20 | NÃO | fora da faixa vertical |
| 79 | 252.00 | 55.00 | 416.68 | 203.20 | NÃO | fora da faixa vertical |
| 80 | 251.00 | 55.00 | 417.56 | 203.20 | NÃO | fora da faixa vertical |
| 81 | 250.00 | 55.00 | 418.44 | 203.20 | NÃO | fora da faixa vertical |
| 82 | 249.00 | 56.00 | 418.84 | 202.20 | NÃO | fora da faixa vertical |
| 83 | 248.00 | 56.00 | 419.72 | 202.20 | NÃO | fora da faixa vertical |
| 84 | 247.00 | 56.00 | 420.59 | 202.20 | NÃO | fora da faixa vertical |
| 85 | 246.00 | 57.00 | 421.00 | 201.20 | NÃO | fora da faixa vertical |
| 86 | 245.00 | 57.00 | 421.88 | 201.20 | NÃO | fora da faixa vertical |
| 87 | 244.00 | 58.00 | 422.29 | 200.20 | NÃO | fora da faixa vertical |
| 88 | 243.00 | 58.00 | 423.18 | 200.20 | NÃO | fora da faixa vertical |
| 89 | 242.00 | 59.00 | 423.60 | 199.20 | NÃO | fora da faixa vertical |
| 90 | 241.00 | 59.00 | 424.48 | 199.20 | NÃO | fora da faixa vertical |
| 91 | 240.00 | 60.00 | 424.91 | 198.20 | NÃO | fora da faixa vertical |
| 92 | 239.00 | 60.00 | 425.79 | 198.20 | NÃO | fora da faixa vertical |
| 93 | 238.00 | 61.00 | 426.22 | 197.20 | NÃO | fora da faixa vertical |
| 94 | 237.00 | 61.00 | 427.11 | 197.20 | NÃO | fora da faixa vertical |
| 95 | 236.00 | 62.00 | 427.55 | 196.20 | NÃO | fora da faixa vertical |
| 96 | 235.00 | 62.00 | 428.44 | 196.20 | NÃO | fora da faixa vertical |
| 97 | 234.00 | 63.00 | 428.88 | 195.20 | NÃO | fora da faixa vertical |
| 98 | 233.00 | 63.00 | 429.77 | 195.20 | NÃO | fora da faixa vertical |
| 99 | 232.00 | 64.00 | 430.22 | 194.20 | NÃO | fora da faixa vertical |
| 100 | 231.00 | 64.00 | 431.11 | 194.20 | NÃO | fora da faixa vertical |
| 101 | 230.00 | 65.00 | 431.57 | 193.20 | NÃO | fora da faixa vertical |
| 102 | 229.00 | 65.00 | 432.46 | 193.20 | NÃO | fora da faixa vertical |
| 103 | 228.00 | 66.00 | 432.92 | 192.20 | NÃO | fora da faixa vertical |
| 104 | 227.00 | 66.00 | 433.82 | 192.20 | NÃO | fora da faixa vertical |
| 105 | 226.00 | 67.00 | 434.28 | 191.20 | NÃO | fora da faixa vertical |
| 106 | 225.00 | 67.00 | 435.18 | 191.20 | NÃO | fora da faixa vertical |
| 107 | 224.00 | 68.00 | 435.65 | 190.20 | NÃO | fora da faixa vertical |
| 108 | 223.00 | 68.00 | 436.55 | 190.20 | NÃO | fora da faixa vertical |
| 109 | 222.00 | 69.00 | 437.03 | 189.20 | NÃO | fora da faixa vertical |
| 110 | 221.00 | 69.00 | 437.93 | 189.20 | NÃO | fora da faixa vertical |
| 111 | 220.00 | 70.00 | 438.41 | 188.20 | NÃO | fora da faixa vertical |
| 112 | 219.00 | 71.00 | 438.90 | 187.20 | NÃO | fora da faixa vertical |
| 113 | 218.00 | 71.00 | 439.80 | 187.20 | NÃO | fora da faixa vertical |
| 114 | 217.00 | 72.00 | 440.29 | 186.20 | NÃO | fora da faixa vertical |
| 115 | 216.00 | 72.00 | 441.20 | 186.20 | NÃO | fora da faixa vertical |
| 116 | 215.00 | 73.00 | 441.69 | 185.20 | NÃO | fora da faixa vertical |
| 117 | 214.00 | 73.00 | 442.60 | 185.20 | NÃO | fora da faixa vertical |
| 118 | 213.00 | 74.00 | 443.10 | 184.20 | NÃO | fora da faixa vertical |
| 119 | 212.00 | 74.00 | 444.01 | 184.20 | NÃO | fora da faixa vertical |
| 120 | 211.00 | 75.00 | 444.52 | 183.20 | NÃO | fora da faixa vertical |
| 121 | 210.00 | 76.00 | 445.03 | 182.20 | NÃO | fora da faixa vertical |
| 122 | 209.00 | 76.00 | 445.94 | 182.20 | NÃO | fora da faixa vertical |
| 123 | 208.00 | 77.00 | 446.45 | 181.20 | NÃO | fora da faixa vertical |
| 124 | 207.00 | 78.00 | 446.97 | 180.20 | NÃO | fora da faixa vertical |
| 125 | 206.00 | 78.00 | 447.89 | 180.20 | NÃO | fora da faixa vertical |
| 126 | 205.00 | 79.00 | 448.41 | 179.20 | NÃO | fora da faixa vertical |
| 127 | 204.00 | 80.00 | 448.94 | 178.20 | NÃO | fora da faixa vertical |
| 128 | 203.00 | 80.00 | 449.86 | 178.20 | NÃO | fora da faixa vertical |
| 129 | 202.00 | 81.00 | 450.39 | 177.20 | NÃO | fora da faixa vertical |
| 130 | 201.00 | 82.00 | 450.92 | 176.20 | NÃO | fora da faixa vertical |
| 131 | 200.00 | 82.00 | 451.85 | 176.20 | NÃO | fora da faixa vertical |
| 132 | 199.00 | 83.00 | 452.39 | 175.20 | NÃO | fora da faixa vertical |
| 133 | 198.00 | 84.00 | 452.93 | 174.20 | NÃO | fora da faixa vertical |
| 134 | 197.00 | 84.00 | 453.85 | 174.20 | NÃO | fora da faixa vertical |
| 135 | 196.00 | 85.00 | 454.40 | 173.20 | NÃO | fora da faixa vertical |
| 136 | 195.00 | 86.00 | 454.95 | 172.20 | NÃO | fora da faixa vertical |
| 137 | 194.00 | 86.00 | 455.88 | 172.20 | NÃO | fora da faixa vertical |
| 138 | 193.00 | 87.00 | 456.44 | 171.20 | NÃO | fora da faixa vertical |
| 139 | 192.00 | 88.00 | 457.00 | 170.20 | NÃO | fora da faixa vertical |
| 140 | 191.00 | 88.00 | 457.93 | 170.20 | NÃO | fora da faixa vertical |
| 141 | 190.00 | 89.00 | 458.50 | 169.20 | NÃO | fora da faixa vertical |
| 142 | 189.00 | 90.00 | 459.06 | 168.20 | NÃO | fora da faixa vertical |
| 143 | 188.00 | 91.00 | 459.64 | 167.20 | NÃO | fora da faixa vertical |
| 144 | 187.00 | 92.00 | 460.21 | 166.20 | NÃO | fora da faixa vertical |
| 145 | 186.00 | 92.00 | 461.15 | 166.20 | NÃO | fora da faixa vertical |
| 146 | 185.00 | 93.00 | 461.73 | 165.20 | NÃO | fora da faixa vertical |
| 147 | 184.00 | 94.00 | 462.31 | 164.20 | NÃO | fora da faixa vertical |
| 148 | 183.00 | 95.00 | 462.90 | 163.20 | NÃO | fora da faixa vertical |
| 149 | 182.00 | 96.00 | 463.49 | 162.20 | NÃO | fora da faixa vertical |
| 150 | 181.00 | 96.00 | 464.43 | 162.20 | NÃO | fora da faixa vertical |
| 151 | 180.00 | 97.00 | 465.03 | 161.20 | NÃO | fora da faixa vertical |
| 152 | 179.00 | 98.00 | 465.63 | 160.20 | NÃO | fora da faixa vertical |
| 153 | 178.00 | 99.00 | 466.23 | 159.20 | NÃO | fora da faixa vertical |
| 154 | 177.00 | 100.00 | 466.84 | 158.20 | NÃO | fora da faixa vertical |
| 155 | 176.00 | 100.00 | 467.78 | 158.20 | NÃO | fora da faixa vertical |
| 156 | 175.00 | 101.00 | 468.39 | 157.20 | NÃO | fora da faixa vertical |
| 157 | 174.00 | 102.00 | 469.00 | 156.20 | NÃO | fora da faixa vertical |
| 158 | 173.00 | 103.00 | 469.62 | 155.20 | NÃO | fora da faixa vertical |
| 159 | 172.00 | 104.00 | 470.24 | 154.20 | NÃO | fora da faixa vertical |
| 160 | 171.00 | 105.00 | 470.87 | 153.20 | NÃO | fora da faixa vertical |
| 161 | 170.00 | 106.00 | 471.50 | 152.20 | NÃO | fora da faixa vertical |
| 162 | 169.00 | 107.00 | 472.13 | 151.20 | NÃO | fora da faixa vertical |
| 163 | 168.00 | 108.00 | 472.76 | 150.20 | NÃO | fora da faixa vertical |
| 164 | 167.00 | 109.00 | 473.40 | 149.20 | NÃO | fora da faixa vertical |
| 165 | 166.00 | 110.00 | 474.04 | 148.20 | NÃO | fora da faixa vertical |
| 166 | 165.00 | 110.00 | 474.99 | 148.20 | NÃO | fora da faixa vertical |
| 167 | 164.00 | 111.00 | 475.64 | 147.20 | NÃO | fora da faixa vertical |
| 168 | 163.00 | 112.00 | 476.29 | 146.20 | NÃO | fora da faixa vertical |
| 169 | 162.00 | 113.00 | 476.94 | 145.20 | NÃO | fora da faixa vertical |
| 170 | 161.00 | 114.00 | 477.60 | 144.20 | NÃO | fora da faixa vertical |
| 171 | 160.00 | 115.00 | 478.26 | 143.20 | NÃO | fora da faixa vertical |
| 172 | 159.00 | 116.00 | 478.92 | 142.20 | NÃO | fora da faixa vertical |
| 173 | 158.00 | 117.00 | 479.59 | 141.20 | NÃO | fora da faixa vertical |
| 174 | 158.00 | 118.00 | 479.30 | 140.20 | NÃO | fora da faixa vertical |
| 175 | 157.00 | 119.00 | 479.97 | 139.20 | NÃO | fora da faixa vertical |
| 176 | 156.00 | 120.00 | 480.64 | 138.20 | NÃO | fora da faixa vertical |
| 177 | 155.00 | 121.00 | 481.32 | 137.20 | NÃO | fora da faixa vertical |
| 178 | 154.00 | 122.00 | 482.00 | 136.20 | NÃO | fora da faixa vertical |
| 179 | 153.00 | 123.00 | 482.69 | 135.20 | NÃO | fora da faixa vertical |
| 180 | 152.00 | 124.00 | 483.37 | 134.20 | NÃO | fora da faixa vertical |
| 181 | 151.00 | 125.00 | 484.06 | 133.20 | NÃO | fora da faixa vertical |
| 182 | 150.00 | 126.00 | 484.76 | 132.20 | NÃO | fora da faixa vertical |
| 183 | 149.00 | 127.00 | 485.45 | 131.20 | NÃO | fora da faixa vertical |
| 184 | 148.00 | 128.00 | 486.15 | 130.20 | NÃO | fora da faixa vertical |
| 185 | 147.00 | 129.00 | 486.86 | 129.20 | NÃO | fora da faixa vertical |
| 186 | 146.00 | 130.00 | 487.56 | 128.20 | NÃO | fora da faixa vertical |
| 187 | 146.00 | 131.00 | 487.30 | 127.20 | NÃO | fora da faixa vertical |
| 188 | 145.00 | 132.00 | 488.02 | 126.20 | NÃO | fora da faixa vertical |
| 189 | 144.00 | 133.00 | 488.73 | 125.20 | NÃO | fora da faixa vertical |
| 190 | 143.00 | 134.00 | 489.45 | 124.20 | NÃO | fora da faixa vertical |
| 191 | 142.00 | 135.00 | 490.17 | 123.20 | NÃO | fora da faixa vertical |
| 192 | 142.00 | 136.00 | 489.92 | 122.20 | NÃO | fora da faixa vertical |
| 193 | 141.00 | 137.00 | 490.65 | 121.20 | NÃO | fora da faixa vertical |
| 194 | 140.00 | 138.00 | 491.38 | 120.20 | NÃO | fora do lado solicitado |
| 195 | 139.00 | 139.00 | 492.11 | 119.20 | NÃO | fora do lado solicitado |
| 196 | 138.00 | 140.00 | 492.85 | 118.20 | NÃO | fora do lado solicitado |
| 197 | 138.00 | 141.00 | 492.61 | 117.20 | NÃO | fora do lado solicitado |
| 198 | 137.00 | 142.00 | 493.35 | 116.20 | NÃO | fora do lado solicitado |
| 199 | 136.00 | 143.00 | 494.10 | 115.20 | NÃO | fora do lado solicitado |
| 200 | 135.00 | 144.00 | 494.84 | 114.20 | NÃO | fora do lado solicitado |
| 201 | 135.00 | 145.00 | 494.62 | 113.20 | NÃO | fora do lado solicitado |
| 202 | 134.00 | 146.00 | 495.37 | 112.20 | NÃO | fora do lado solicitado |
| 203 | 133.00 | 147.00 | 496.12 | 111.20 | NÃO | fora do lado solicitado |
| 204 | 132.00 | 148.00 | 496.88 | 110.20 | NÃO | fora do lado solicitado |
| 205 | 132.00 | 149.00 | 496.66 | 109.20 | NÃO | fora do lado solicitado |
| 206 | 131.00 | 150.00 | 497.43 | 108.20 | NÃO | fora do lado solicitado |
| 207 | 130.00 | 151.00 | 498.19 | 107.20 | NÃO | fora do lado solicitado |
| 208 | 130.00 | 152.00 | 497.98 | 106.20 | NÃO | fora do lado solicitado |
| 209 | 129.00 | 153.00 | 498.75 | 105.20 | NÃO | fora do lado solicitado |
| 210 | 128.00 | 154.00 | 499.52 | 104.20 | NÃO | fora do lado solicitado |
| 211 | 128.00 | 155.00 | 499.32 | 103.20 | NÃO | fora do lado solicitado |
| 212 | 127.00 | 156.00 | 500.10 | 102.20 | NÃO | fora do lado solicitado |
| 213 | 126.00 | 157.00 | 500.88 | 101.20 | NÃO | fora do lado solicitado |
| 214 | 126.00 | 158.00 | 500.68 | 100.20 | NÃO | fora do lado solicitado |
| 215 | 125.00 | 159.00 | 501.47 | 99.20 | NÃO | fora do lado solicitado |
| 216 | 124.00 | 160.00 | 502.26 | 98.20 | NÃO | fora do lado solicitado |
| 217 | 124.00 | 161.00 | 502.07 | 97.20 | NÃO | fora do lado solicitado |
| 218 | 123.00 | 162.00 | 502.86 | 96.20 | NÃO | fora do lado solicitado |
| 219 | 122.00 | 163.00 | 503.66 | 95.20 | NÃO | fora do lado solicitado |
| 220 | 122.00 | 164.00 | 503.48 | 94.20 | NÃO | fora do lado solicitado |
| 221 | 121.00 | 165.00 | 504.28 | 93.20 | NÃO | fora do lado solicitado |
| 222 | 121.00 | 166.00 | 504.10 | 92.20 | NÃO | fora do lado solicitado |
| 223 | 120.00 | 167.00 | 504.91 | 91.20 | NÃO | fora do lado solicitado |
| 224 | 119.00 | 168.00 | 505.72 | 90.20 | NÃO | fora do lado solicitado |
| 225 | 119.00 | 169.00 | 505.54 | 89.20 | NÃO | fora do lado solicitado |
| 226 | 118.00 | 170.00 | 506.36 | 88.20 | NÃO | fora do lado solicitado |
| 227 | 118.00 | 171.00 | 506.19 | 87.20 | NÃO | fora do lado solicitado |
| 228 | 117.00 | 172.00 | 507.01 | 86.20 | NÃO | fora do lado solicitado |
| 229 | 117.00 | 173.00 | 506.84 | 85.20 | NÃO | fora do lado solicitado |
| 230 | 116.00 | 174.00 | 507.67 | 84.20 | NÃO | fora do lado solicitado |
| 231 | 115.00 | 175.00 | 508.49 | 83.20 | NÃO | fora do lado solicitado |
| 232 | 115.00 | 176.00 | 508.33 | 82.20 | NÃO | fora do lado solicitado |
| 233 | 114.00 | 177.00 | 509.17 | 81.20 | NÃO | fora do lado solicitado |
| 234 | 114.00 | 178.00 | 509.01 | 80.20 | NÃO | fora do lado solicitado |
| 235 | 113.00 | 179.00 | 509.85 | 79.20 | NÃO | fora do lado solicitado |
| 236 | 113.00 | 180.00 | 509.70 | 78.20 | NÃO | fora do lado solicitado |
| 237 | 112.00 | 181.00 | 510.54 | 77.20 | NÃO | fora do lado solicitado |
| 238 | 112.00 | 182.00 | 510.39 | 76.20 | NÃO | fora do lado solicitado |
| 239 | 111.00 | 183.00 | 511.24 | 75.20 | NÃO | fora do lado solicitado |
| 240 | 111.00 | 184.00 | 511.10 | 74.20 | NÃO | fora do lado solicitado |
| 241 | 110.00 | 185.00 | 511.95 | 73.20 | NÃO | fora do lado solicitado |
| 242 | 110.00 | 186.00 | 511.81 | 72.20 | NÃO | fora do lado solicitado |
| 243 | 109.00 | 187.00 | 512.66 | 71.20 | NÃO | fora do lado solicitado |
| 244 | 109.00 | 188.00 | 512.53 | 70.20 | NÃO | fora do lado solicitado |
| 245 | 108.00 | 189.00 | 513.39 | 69.20 | NÃO | fora do lado solicitado |
| 246 | 108.00 | 190.00 | 513.26 | 68.20 | NÃO | fora do lado solicitado |
| 247 | 107.00 | 191.00 | 514.13 | 67.20 | NÃO | fora do lado solicitado |
| 248 | 107.00 | 192.00 | 514.00 | 66.20 | NÃO | fora do lado solicitado |
| 249 | 106.00 | 193.00 | 514.87 | 65.20 | NÃO | fora do lado solicitado |
| 250 | 106.00 | 194.00 | 514.75 | 64.20 | NÃO | fora do lado solicitado |
| 251 | 105.00 | 195.00 | 515.62 | 63.20 | NÃO | fora do lado solicitado |
| 252 | 105.00 | 196.00 | 515.50 | 62.20 | NÃO | fora do lado solicitado |
| 253 | 104.00 | 197.00 | 516.38 | 61.20 | NÃO | fora do lado solicitado |
| 254 | 104.00 | 198.00 | 516.27 | 60.20 | NÃO | fora do lado solicitado |
| 255 | 103.00 | 199.00 | 517.15 | 59.20 | NÃO | fora do lado solicitado |
| 256 | 103.00 | 200.00 | 517.04 | 58.20 | NÃO | fora do lado solicitado |
| 257 | 103.00 | 201.00 | 516.93 | 57.20 | NÃO | fora do lado solicitado |
| 258 | 102.00 | 202.00 | 517.82 | 56.20 | NÃO | fora do lado solicitado |
| 259 | 102.00 | 203.00 | 517.72 | 55.20 | NÃO | fora do lado solicitado |
| 260 | 102.00 | 204.00 | 517.62 | 54.20 | NÃO | fora do lado solicitado |
| 261 | 101.00 | 205.00 | 518.51 | 53.20 | NÃO | fora do lado solicitado |
| 262 | 101.00 | 206.00 | 518.42 | 52.20 | NÃO | fora do lado solicitado |
| 263 | 100.00 | 207.00 | 519.32 | 51.20 | NÃO | fora do lado solicitado |
| 264 | 100.00 | 208.00 | 519.22 | 50.20 | NÃO | fora do lado solicitado |
| 265 | 100.00 | 209.00 | 519.13 | 49.20 | NÃO | fora do lado solicitado |
| 266 | 99.00 | 210.00 | 520.04 | 48.20 | NÃO | fora do lado solicitado |
| 267 | 99.00 | 211.00 | 519.95 | 47.20 | NÃO | fora do lado solicitado |
| 268 | 99.00 | 212.00 | 519.87 | 46.20 | NÃO | fora do lado solicitado |
| 269 | 98.00 | 213.00 | 520.78 | 45.20 | NÃO | fora do lado solicitado |
| 270 | 98.00 | 214.00 | 520.70 | 44.20 | NÃO | fora do lado solicitado |
| 271 | 97.00 | 215.00 | 521.61 | 43.20 | NÃO | fora do lado solicitado |
| 272 | 97.00 | 216.00 | 521.54 | 42.20 | NÃO | fora do lado solicitado |
| 273 | 97.00 | 217.00 | 521.46 | 41.20 | NÃO | fora do lado solicitado |
| 274 | 96.00 | 218.00 | 522.38 | 40.20 | NÃO | fora do lado solicitado |
| 275 | 96.00 | 219.00 | 522.31 | 39.20 | NÃO | fora do lado solicitado |
| 276 | 96.00 | 220.00 | 522.24 | 38.20 | NÃO | fora do lado solicitado |
| 277 | 95.00 | 221.00 | 523.17 | 37.20 | NÃO | fora do lado solicitado |
| 278 | 95.00 | 222.00 | 523.11 | 36.20 | NÃO | fora do lado solicitado |
| 279 | 95.00 | 223.00 | 523.04 | 35.20 | NÃO | fora do lado solicitado |
| 280 | 94.00 | 224.00 | 523.98 | 34.20 | NÃO | fora do lado solicitado |
| 281 | 94.00 | 225.00 | 523.92 | 33.20 | NÃO | fora do lado solicitado |
| 282 | 94.00 | 226.00 | 523.86 | 32.20 | NÃO | fora do lado solicitado |
| 283 | 94.00 | 227.00 | 523.80 | 31.20 | NÃO | fora do lado solicitado |
| 284 | 93.00 | 228.00 | 524.75 | 30.20 | NÃO | fora do lado solicitado |
| 285 | 93.00 | 229.00 | 524.70 | 29.20 | NÃO | fora do lado solicitado |
| 286 | 93.00 | 230.00 | 524.64 | 28.20 | NÃO | fora do lado solicitado |
| 287 | 92.00 | 231.00 | 525.59 | 27.20 | NÃO | fora do lado solicitado |
| 288 | 92.00 | 232.00 | 525.55 | 26.20 | NÃO | fora do lado solicitado |
| 289 | 92.00 | 233.00 | 525.50 | 25.20 | NÃO | fora do lado solicitado |
| 290 | 91.00 | 234.00 | 526.46 | 24.20 | NÃO | fora do lado solicitado |
| 291 | 91.00 | 235.00 | 526.42 | 23.20 | NÃO | fora do lado solicitado |
| 292 | 91.00 | 236.00 | 526.38 | 22.20 | NÃO | fora do lado solicitado |
| 293 | 91.00 | 237.00 | 526.34 | 21.20 | NÃO | fora do lado solicitado |
| 294 | 90.00 | 238.00 | 527.31 | 20.20 | NÃO | fora do lado solicitado |
| 295 | 90.00 | 239.00 | 527.27 | 19.20 | NÃO | fora do lado solicitado |
| 296 | 90.00 | 240.00 | 527.24 | 18.20 | NÃO | fora do lado solicitado |
| 297 | 90.00 | 241.00 | 527.21 | 17.20 | NÃO | fora do lado solicitado |
| 298 | 89.00 | 242.00 | 528.19 | 16.20 | NÃO | fora do lado solicitado |
| 299 | 89.00 | 243.00 | 528.16 | 15.20 | NÃO | fora do lado solicitado |
| 300 | 89.00 | 244.00 | 528.14 | 14.20 | NÃO | fora do lado solicitado |
| 301 | 89.00 | 245.00 | 528.11 | 13.20 | NÃO | fora do lado solicitado |
| 302 | 88.00 | 246.00 | 529.09 | 12.20 | NÃO | fora do lado solicitado |
| 303 | 88.00 | 247.00 | 529.08 | 11.20 | NÃO | fora do lado solicitado |
| 304 | 88.00 | 248.00 | 529.06 | 10.20 | NÃO | fora do lado solicitado |
| 305 | 88.00 | 249.00 | 529.05 | 9.20 | NÃO | fora do lado solicitado |
| 306 | 88.00 | 250.00 | 529.03 | 8.20 | NÃO | fora do lado solicitado |
| 307 | 87.00 | 251.00 | 530.02 | 7.20 | NÃO | fora do lado solicitado |
| 308 | 87.00 | 252.00 | 530.02 | 6.20 | NÃO | fora do lado solicitado |
| 309 | 87.00 | 253.00 | 530.01 | 5.20 | NÃO | fora do lado solicitado |
| 310 | 87.00 | 254.00 | 530.00 | 4.20 | NÃO | fora do lado solicitado |
| 311 | 87.00 | 255.00 | 530.00 | 3.20 | NÃO | fora do lado solicitado |
| 312 | 86.00 | 256.00 | 531.00 | 2.20 | NÃO | fora do lado solicitado |
| 313 | 87.00 | 256.00 | 530.00 | 2.20 | NÃO | fora do lado solicitado |
| 314 | 88.00 | 256.00 | 529.00 | 2.20 | NÃO | fora do lado solicitado |
| 315 | 89.00 | 256.00 | 528.00 | 2.20 | NÃO | fora do lado solicitado |
| 316 | 90.00 | 256.00 | 527.00 | 2.20 | NÃO | fora do lado solicitado |
| 317 | 91.00 | 256.00 | 526.00 | 2.20 | NÃO | fora do lado solicitado |
| 318 | 92.00 | 256.00 | 525.00 | 2.20 | NÃO | fora do lado solicitado |
| 319 | 93.00 | 256.00 | 524.00 | 2.20 | NÃO | fora do lado solicitado |
| 320 | 94.00 | 256.00 | 523.00 | 2.20 | NÃO | fora do lado solicitado |
| 321 | 95.00 | 256.00 | 522.00 | 2.20 | NÃO | fora do lado solicitado |
| 322 | 96.00 | 256.00 | 521.00 | 2.20 | NÃO | fora do lado solicitado |
| 323 | 97.00 | 256.00 | 520.00 | 2.20 | NÃO | fora do lado solicitado |
| 324 | 98.00 | 256.00 | 519.00 | 2.20 | NÃO | fora do lado solicitado |
| 325 | 99.00 | 256.00 | 518.00 | 2.20 | NÃO | fora do lado solicitado |
| 326 | 100.00 | 256.00 | 517.00 | 2.20 | NÃO | fora do lado solicitado |
| 327 | 101.00 | 256.00 | 516.00 | 2.20 | NÃO | fora do lado solicitado |
| 328 | 102.00 | 256.00 | 515.00 | 2.20 | NÃO | fora do lado solicitado |
| 329 | 103.00 | 256.00 | 514.00 | 2.20 | NÃO | fora do lado solicitado |
| 330 | 104.00 | 256.00 | 513.00 | 2.20 | NÃO | fora do lado solicitado |
| 331 | 105.00 | 256.00 | 512.00 | 2.20 | NÃO | fora do lado solicitado |
| 332 | 106.00 | 256.00 | 511.00 | 2.20 | NÃO | fora do lado solicitado |
| 333 | 107.00 | 256.00 | 510.00 | 2.20 | NÃO | fora do lado solicitado |
| 334 | 108.00 | 256.00 | 509.00 | 2.20 | NÃO | fora do lado solicitado |
| 335 | 109.00 | 256.00 | 508.00 | 2.20 | NÃO | fora do lado solicitado |
| 336 | 110.00 | 256.00 | 507.00 | 2.20 | NÃO | fora do lado solicitado |
| 337 | 111.00 | 256.00 | 506.00 | 2.20 | NÃO | fora do lado solicitado |
| 338 | 112.00 | 256.00 | 505.00 | 2.20 | NÃO | fora do lado solicitado |
| 339 | 113.00 | 256.00 | 504.00 | 2.20 | NÃO | fora do lado solicitado |
| 340 | 114.00 | 256.00 | 503.00 | 2.20 | NÃO | fora do lado solicitado |
| 341 | 115.00 | 256.00 | 502.00 | 2.20 | NÃO | fora do lado solicitado |
| 342 | 116.00 | 256.00 | 501.00 | 2.20 | NÃO | fora do lado solicitado |
| 343 | 117.00 | 256.00 | 500.00 | 2.20 | NÃO | fora do lado solicitado |
| 344 | 118.00 | 256.00 | 499.00 | 2.20 | NÃO | fora do lado solicitado |
| 345 | 119.00 | 256.00 | 498.00 | 2.20 | NÃO | fora do lado solicitado |
| 346 | 120.00 | 256.00 | 497.00 | 2.20 | NÃO | fora do lado solicitado |
| 347 | 121.00 | 256.00 | 496.00 | 2.20 | NÃO | fora do lado solicitado |
| 348 | 122.00 | 256.00 | 495.00 | 2.20 | NÃO | fora do lado solicitado |
| 349 | 123.00 | 256.00 | 494.00 | 2.20 | NÃO | fora do lado solicitado |
| 350 | 124.00 | 256.00 | 493.00 | 2.20 | NÃO | fora do lado solicitado |
| 351 | 125.00 | 256.00 | 492.00 | 2.20 | NÃO | fora do lado solicitado |
| 352 | 126.00 | 256.00 | 491.00 | 2.20 | NÃO | fora do lado solicitado |
| 353 | 127.00 | 256.00 | 490.00 | 2.20 | NÃO | fora do lado solicitado |
| 354 | 128.00 | 256.00 | 489.00 | 2.20 | NÃO | fora do lado solicitado |
| 355 | 129.00 | 256.00 | 488.00 | 2.20 | NÃO | fora do lado solicitado |
| 356 | 130.00 | 256.00 | 487.00 | 2.20 | NÃO | fora do lado solicitado |
| 357 | 131.00 | 256.00 | 486.00 | 2.20 | NÃO | fora do lado solicitado |
| 358 | 132.00 | 256.00 | 485.00 | 2.20 | NÃO | fora do lado solicitado |
| 359 | 133.00 | 256.00 | 484.00 | 2.20 | NÃO | fora do lado solicitado |
| 360 | 134.00 | 256.00 | 483.00 | 2.20 | NÃO | fora do lado solicitado |
| 361 | 135.00 | 256.00 | 482.00 | 2.20 | NÃO | fora do lado solicitado |
| 362 | 136.00 | 256.00 | 481.00 | 2.20 | NÃO | fora do lado solicitado |
| 363 | 137.00 | 256.00 | 480.00 | 2.20 | NÃO | fora do lado solicitado |
| 364 | 138.00 | 256.00 | 479.00 | 2.20 | NÃO | fora do lado solicitado |
| 365 | 139.00 | 256.00 | 478.00 | 2.20 | NÃO | fora do lado solicitado |
| 366 | 140.00 | 256.00 | 477.00 | 2.20 | NÃO | fora do lado solicitado |
| 367 | 141.00 | 256.00 | 476.00 | 2.20 | NÃO | fora do lado solicitado |
| 368 | 142.00 | 256.00 | 475.00 | 2.20 | NÃO | fora do lado solicitado |
| 369 | 143.00 | 256.00 | 474.00 | 2.20 | NÃO | fora do lado solicitado |
| 370 | 144.00 | 256.00 | 473.00 | 2.20 | NÃO | fora do lado solicitado |
| 371 | 145.00 | 256.00 | 472.00 | 2.20 | NÃO | fora do lado solicitado |
| 372 | 146.00 | 256.00 | 471.00 | 2.20 | NÃO | fora do lado solicitado |
| 373 | 147.00 | 256.00 | 470.00 | 2.20 | NÃO | fora do lado solicitado |
| 374 | 148.00 | 256.00 | 469.00 | 2.20 | NÃO | fora do lado solicitado |
| 375 | 149.00 | 256.00 | 468.00 | 2.20 | NÃO | fora do lado solicitado |
| 376 | 150.00 | 256.00 | 467.00 | 2.20 | NÃO | fora do lado solicitado |
| 377 | 151.00 | 256.00 | 466.00 | 2.20 | NÃO | fora do lado solicitado |
| 378 | 152.00 | 256.00 | 465.00 | 2.20 | NÃO | fora do lado solicitado |
| 379 | 153.00 | 256.00 | 464.00 | 2.20 | NÃO | fora do lado solicitado |
| 380 | 154.00 | 256.00 | 463.00 | 2.20 | NÃO | fora do lado solicitado |
| 381 | 155.00 | 256.00 | 462.00 | 2.20 | NÃO | fora do lado solicitado |
| 382 | 156.00 | 256.00 | 461.00 | 2.20 | NÃO | fora do lado solicitado |
| 383 | 157.00 | 256.00 | 460.00 | 2.20 | NÃO | fora do lado solicitado |
| 384 | 158.00 | 256.00 | 459.00 | 2.20 | NÃO | fora do lado solicitado |
| 385 | 159.00 | 256.00 | 458.00 | 2.20 | NÃO | fora do lado solicitado |
| 386 | 160.00 | 256.00 | 457.00 | 2.20 | NÃO | fora do lado solicitado |
| 387 | 161.00 | 256.00 | 456.00 | 2.20 | NÃO | fora do lado solicitado |
| 388 | 162.00 | 256.00 | 455.00 | 2.20 | NÃO | fora do lado solicitado |
| 389 | 163.00 | 256.00 | 454.00 | 2.20 | NÃO | fora do lado solicitado |
| 390 | 164.00 | 256.00 | 453.00 | 2.20 | NÃO | fora do lado solicitado |
| 391 | 165.00 | 256.00 | 452.00 | 2.20 | NÃO | fora do lado solicitado |
| 392 | 166.00 | 256.00 | 451.00 | 2.20 | NÃO | fora do lado solicitado |
| 393 | 167.00 | 256.00 | 450.00 | 2.20 | NÃO | fora do lado solicitado |
| 394 | 168.00 | 256.00 | 449.00 | 2.20 | NÃO | fora do lado solicitado |
| 395 | 169.00 | 256.00 | 448.00 | 2.20 | NÃO | fora do lado solicitado |
| 396 | 170.00 | 256.00 | 447.00 | 2.20 | NÃO | fora do lado solicitado |
| 397 | 171.00 | 256.00 | 446.00 | 2.20 | NÃO | fora do lado solicitado |
| 398 | 172.00 | 256.00 | 445.00 | 2.20 | NÃO | fora do lado solicitado |
| 399 | 173.00 | 256.00 | 444.00 | 2.20 | NÃO | fora do lado solicitado |
| 400 | 174.00 | 256.00 | 443.00 | 2.20 | NÃO | fora do lado solicitado |
| 401 | 175.00 | 256.00 | 442.00 | 2.20 | NÃO | fora do lado solicitado |
| 402 | 176.00 | 256.00 | 441.00 | 2.20 | NÃO | fora do lado solicitado |
| 403 | 177.00 | 256.00 | 440.00 | 2.20 | NÃO | fora do lado solicitado |
| 404 | 178.00 | 256.00 | 439.00 | 2.20 | NÃO | fora do lado solicitado |
| 405 | 179.00 | 256.00 | 438.00 | 2.20 | NÃO | fora do lado solicitado |
| 406 | 180.00 | 256.00 | 437.00 | 2.20 | NÃO | fora do lado solicitado |
| 407 | 181.00 | 256.00 | 436.00 | 2.20 | NÃO | fora do lado solicitado |
| 408 | 182.00 | 256.00 | 435.00 | 2.20 | NÃO | fora do lado solicitado |
| 409 | 183.00 | 256.00 | 434.00 | 2.20 | NÃO | fora do lado solicitado |
| 410 | 184.00 | 256.00 | 433.00 | 2.20 | NÃO | fora do lado solicitado |
| 411 | 185.00 | 256.00 | 432.00 | 2.20 | NÃO | fora do lado solicitado |
| 412 | 186.00 | 256.00 | 431.00 | 2.20 | NÃO | fora do lado solicitado |
| 413 | 187.00 | 256.00 | 430.00 | 2.20 | NÃO | fora do lado solicitado |
| 414 | 188.00 | 256.00 | 429.00 | 2.20 | NÃO | fora do lado solicitado |
| 415 | 189.00 | 256.00 | 428.00 | 2.20 | NÃO | fora do lado solicitado |
| 416 | 190.00 | 256.00 | 427.00 | 2.20 | NÃO | fora do lado solicitado |
| 417 | 191.00 | 256.00 | 426.00 | 2.20 | NÃO | fora do lado solicitado |
| 418 | 192.00 | 256.00 | 425.00 | 2.20 | NÃO | fora do lado solicitado |
| 419 | 193.00 | 256.00 | 424.00 | 2.20 | NÃO | fora do lado solicitado |
| 420 | 194.00 | 256.00 | 423.00 | 2.20 | NÃO | fora do lado solicitado |
| 421 | 195.00 | 256.00 | 422.00 | 2.20 | NÃO | fora do lado solicitado |
| 422 | 196.00 | 256.00 | 421.00 | 2.20 | NÃO | fora do lado solicitado |
| 423 | 197.00 | 256.00 | 420.00 | 2.20 | NÃO | fora do lado solicitado |
| 424 | 198.00 | 256.00 | 419.00 | 2.20 | NÃO | fora do lado solicitado |
| 425 | 199.00 | 256.00 | 418.00 | 2.20 | NÃO | fora do lado solicitado |
| 426 | 200.00 | 256.00 | 417.00 | 2.20 | NÃO | fora do lado solicitado |
| 427 | 201.00 | 256.00 | 416.00 | 2.20 | NÃO | fora do lado solicitado |
| 428 | 202.00 | 256.00 | 415.00 | 2.20 | NÃO | fora do lado solicitado |
| 429 | 203.00 | 256.00 | 414.00 | 2.20 | NÃO | fora do lado solicitado |
| 430 | 204.00 | 256.00 | 413.00 | 2.20 | NÃO | fora do lado solicitado |
| 431 | 205.00 | 256.00 | 412.00 | 2.20 | NÃO | fora do lado solicitado |
| 432 | 206.00 | 256.00 | 411.00 | 2.20 | NÃO | fora do lado solicitado |
| 433 | 207.00 | 256.00 | 410.00 | 2.20 | NÃO | fora do lado solicitado |
| 434 | 208.00 | 256.00 | 409.00 | 2.20 | NÃO | fora do lado solicitado |
| 435 | 209.00 | 256.00 | 408.00 | 2.20 | NÃO | fora do lado solicitado |
| 436 | 210.00 | 256.00 | 407.00 | 2.20 | NÃO | fora do lado solicitado |
| 437 | 211.00 | 256.00 | 406.00 | 2.20 | NÃO | fora do lado solicitado |
| 438 | 212.00 | 256.00 | 405.00 | 2.20 | NÃO | fora do lado solicitado |
| 439 | 213.00 | 256.00 | 404.00 | 2.20 | NÃO | fora do lado solicitado |
| 440 | 214.00 | 256.00 | 403.00 | 2.20 | NÃO | fora do lado solicitado |
| 441 | 215.00 | 256.00 | 402.00 | 2.20 | NÃO | fora do lado solicitado |
| 442 | 216.00 | 256.00 | 401.00 | 2.20 | NÃO | fora do lado solicitado |
| 443 | 217.00 | 256.00 | 400.00 | 2.20 | NÃO | fora do lado solicitado |
| 444 | 218.00 | 256.00 | 399.00 | 2.20 | NÃO | fora do lado solicitado |
| 445 | 219.00 | 256.00 | 398.00 | 2.20 | NÃO | fora do lado solicitado |
| 446 | 220.00 | 256.00 | 397.00 | 2.20 | NÃO | fora do lado solicitado |
| 447 | 221.00 | 256.00 | 396.00 | 2.20 | NÃO | fora do lado solicitado |
| 448 | 222.00 | 256.00 | 395.00 | 2.20 | NÃO | fora do lado solicitado |
| 449 | 223.00 | 256.00 | 394.00 | 2.20 | NÃO | fora do lado solicitado |
| 450 | 224.00 | 256.00 | 393.00 | 2.20 | NÃO | fora do lado solicitado |
| 451 | 225.00 | 256.00 | 392.00 | 2.20 | NÃO | fora do lado solicitado |
| 452 | 226.00 | 256.00 | 391.00 | 2.20 | NÃO | fora do lado solicitado |
| 453 | 227.00 | 256.00 | 390.00 | 2.20 | NÃO | fora do lado solicitado |
| 454 | 228.00 | 256.00 | 389.00 | 2.20 | NÃO | fora do lado solicitado |
| 455 | 229.00 | 256.00 | 388.00 | 2.20 | NÃO | fora do lado solicitado |
| 456 | 230.00 | 256.00 | 387.00 | 2.20 | NÃO | fora do lado solicitado |
| 457 | 231.00 | 256.00 | 386.00 | 2.20 | NÃO | fora do lado solicitado |
| 458 | 232.00 | 256.00 | 385.00 | 2.20 | NÃO | fora do lado solicitado |
| 459 | 233.00 | 256.00 | 384.00 | 2.20 | NÃO | fora do lado solicitado |
| 460 | 234.00 | 256.00 | 383.00 | 2.20 | NÃO | fora do lado solicitado |
| 461 | 235.00 | 256.00 | 382.00 | 2.20 | NÃO | fora do lado solicitado |
| 462 | 236.00 | 256.00 | 381.00 | 2.20 | NÃO | fora do lado solicitado |
| 463 | 237.00 | 256.00 | 380.00 | 2.20 | NÃO | fora do lado solicitado |
| 464 | 238.00 | 256.00 | 379.00 | 2.20 | NÃO | fora do lado solicitado |
| 465 | 239.00 | 256.00 | 378.00 | 2.20 | NÃO | fora do lado solicitado |
| 466 | 240.00 | 256.00 | 377.00 | 2.20 | NÃO | fora do lado solicitado |
| 467 | 241.00 | 256.00 | 376.00 | 2.20 | NÃO | fora do lado solicitado |
| 468 | 242.00 | 256.00 | 375.00 | 2.20 | NÃO | fora do lado solicitado |
| 469 | 243.00 | 256.00 | 374.00 | 2.20 | NÃO | fora do lado solicitado |
| 470 | 244.00 | 256.00 | 373.00 | 2.20 | NÃO | fora do lado solicitado |
| 471 | 245.00 | 256.00 | 372.00 | 2.20 | NÃO | fora do lado solicitado |
| 472 | 246.00 | 256.00 | 371.00 | 2.20 | NÃO | fora do lado solicitado |
| 473 | 247.00 | 256.00 | 370.00 | 2.20 | NÃO | fora do lado solicitado |
| 474 | 248.00 | 256.00 | 369.00 | 2.20 | NÃO | fora do lado solicitado |
| 475 | 249.00 | 256.00 | 368.00 | 2.20 | NÃO | fora do lado solicitado |
| 476 | 250.00 | 256.00 | 367.00 | 2.20 | NÃO | fora do lado solicitado |
| 477 | 251.00 | 256.00 | 366.00 | 2.20 | NÃO | fora do lado solicitado |
| 478 | 252.00 | 256.00 | 365.00 | 2.20 | NÃO | fora do lado solicitado |
| 479 | 253.00 | 256.00 | 364.00 | 2.20 | NÃO | fora do lado solicitado |
| 480 | 254.00 | 256.00 | 363.00 | 2.20 | NÃO | fora do lado solicitado |
| 481 | 255.00 | 256.00 | 362.00 | 2.20 | NÃO | fora do lado solicitado |
| 482 | 256.00 | 256.00 | 361.00 | 2.20 | NÃO | fora do lado solicitado |
| 483 | 257.00 | 256.00 | 360.00 | 2.20 | NÃO | fora do lado solicitado |
| 484 | 258.00 | 256.00 | 359.00 | 2.20 | NÃO | fora do lado solicitado |
| 485 | 259.00 | 256.00 | 358.00 | 2.20 | NÃO | fora do lado solicitado |
| 486 | 260.00 | 256.00 | 357.00 | 2.20 | NÃO | fora do lado solicitado |
| 487 | 261.00 | 256.00 | 356.00 | 2.20 | NÃO | fora do lado solicitado |
| 488 | 262.00 | 256.00 | 355.00 | 2.20 | NÃO | fora do lado solicitado |
| 489 | 263.00 | 256.00 | 354.00 | 2.20 | NÃO | fora do lado solicitado |
| 490 | 264.00 | 256.00 | 353.00 | 2.20 | NÃO | fora do lado solicitado |
| 491 | 265.00 | 256.00 | 352.00 | 2.20 | NÃO | fora do lado solicitado |
| 492 | 266.00 | 256.00 | 351.00 | 2.20 | NÃO | fora do lado solicitado |
| 493 | 267.00 | 256.00 | 350.00 | 2.20 | NÃO | fora do lado solicitado |
| 494 | 268.00 | 256.00 | 349.00 | 2.20 | NÃO | fora do lado solicitado |
| 495 | 269.00 | 256.00 | 348.00 | 2.20 | NÃO | fora do lado solicitado |
| 496 | 270.00 | 256.00 | 347.00 | 2.20 | NÃO | fora do lado solicitado |
| 497 | 271.00 | 256.00 | 346.00 | 2.20 | NÃO | fora do lado solicitado |
| 498 | 272.00 | 256.00 | 345.00 | 2.20 | NÃO | fora do lado solicitado |
| 499 | 273.00 | 256.00 | 344.00 | 2.20 | NÃO | fora do lado solicitado |
| 500 | 274.00 | 256.00 | 343.00 | 2.20 | NÃO | fora do lado solicitado |
| 501 | 275.00 | 256.00 | 342.00 | 2.20 | NÃO | fora do lado solicitado |
| 502 | 276.00 | 256.00 | 341.00 | 2.20 | NÃO | fora do lado solicitado |
| 503 | 277.00 | 256.00 | 340.00 | 2.20 | NÃO | fora do lado solicitado |
| 504 | 278.00 | 256.00 | 339.00 | 2.20 | NÃO | fora do lado solicitado |
| 505 | 279.00 | 256.00 | 338.00 | 2.20 | NÃO | fora do lado solicitado |
| 506 | 280.00 | 256.00 | 337.00 | 2.20 | NÃO | fora do lado solicitado |
| 507 | 281.00 | 256.00 | 336.00 | 2.20 | NÃO | fora do lado solicitado |
| 508 | 282.00 | 256.00 | 335.00 | 2.20 | NÃO | fora do lado solicitado |
| 509 | 283.00 | 256.00 | 334.00 | 2.20 | NÃO | fora do lado solicitado |
| 510 | 284.00 | 256.00 | 333.00 | 2.20 | NÃO | fora do lado solicitado |
| 511 | 285.00 | 256.00 | 332.00 | 2.20 | NÃO | fora do lado solicitado |
| 512 | 286.00 | 256.00 | 331.00 | 2.20 | NÃO | fora do lado solicitado |
| 513 | 287.00 | 256.00 | 330.00 | 2.20 | NÃO | fora do lado solicitado |
| 514 | 288.00 | 256.00 | 329.00 | 2.20 | NÃO | fora do lado solicitado |
| 515 | 289.00 | 256.00 | 328.00 | 2.20 | NÃO | fora do lado solicitado |
| 516 | 290.00 | 256.00 | 327.00 | 2.20 | NÃO | fora do lado solicitado |
| 517 | 291.00 | 256.00 | 326.00 | 2.20 | NÃO | fora do lado solicitado |
| 518 | 292.00 | 256.00 | 325.00 | 2.20 | NÃO | fora do lado solicitado |
| 519 | 293.00 | 256.00 | 324.00 | 2.20 | NÃO | fora do lado solicitado |
| 520 | 294.00 | 256.00 | 323.00 | 2.20 | NÃO | fora do lado solicitado |
| 521 | 295.00 | 256.00 | 322.00 | 2.20 | NÃO | fora do lado solicitado |
| 522 | 296.00 | 256.00 | 321.00 | 2.20 | NÃO | fora do lado solicitado |
| 523 | 297.00 | 256.00 | 320.00 | 2.20 | NÃO | fora do lado solicitado |
| 524 | 298.00 | 256.00 | 319.00 | 2.20 | NÃO | fora do lado solicitado |
| 525 | 299.00 | 256.00 | 318.00 | 2.20 | NÃO | fora do lado solicitado |
| 526 | 300.00 | 256.00 | 317.00 | 2.20 | NÃO | fora do lado solicitado |
| 527 | 301.00 | 256.00 | 316.00 | 2.20 | NÃO | fora do lado solicitado |
| 528 | 302.00 | 256.00 | 315.00 | 2.20 | NÃO | fora do lado solicitado |
| 529 | 303.00 | 256.00 | 314.00 | 2.20 | NÃO | fora do lado solicitado |
| 530 | 304.00 | 256.00 | 313.00 | 2.20 | NÃO | fora do lado solicitado |
| 531 | 305.00 | 256.00 | 312.00 | 2.20 | NÃO | fora do lado solicitado |
| 532 | 306.00 | 256.00 | 311.00 | 2.20 | NÃO | fora do lado solicitado |
| 533 | 307.00 | 256.00 | 310.00 | 2.20 | NÃO | fora do lado solicitado |
| 534 | 308.00 | 256.00 | 309.00 | 2.20 | NÃO | fora do lado solicitado |
| 535 | 309.00 | 256.00 | 308.00 | 2.20 | NÃO | fora do lado solicitado |
| 536 | 310.00 | 256.00 | 307.00 | 2.20 | NÃO | fora do lado solicitado |
| 537 | 311.00 | 256.00 | 306.00 | 2.20 | NÃO | fora do lado solicitado |
| 538 | 312.00 | 256.00 | 305.00 | 2.20 | NÃO | fora do lado solicitado |
| 539 | 313.00 | 256.00 | 304.00 | 2.20 | NÃO | fora do lado solicitado |
| 540 | 314.00 | 256.00 | 303.00 | 2.20 | NÃO | fora do lado solicitado |
| 541 | 315.00 | 256.00 | 302.00 | 2.20 | NÃO | fora do lado solicitado |
| 542 | 316.00 | 256.00 | 301.00 | 2.20 | NÃO | fora do lado solicitado |
| 543 | 317.00 | 256.00 | 300.00 | 2.20 | NÃO | fora do lado solicitado |
| 544 | 318.00 | 256.00 | 299.00 | 2.20 | NÃO | fora do lado solicitado |
| 545 | 319.00 | 256.00 | 298.00 | 2.20 | NÃO | fora do lado solicitado |
| 546 | 320.00 | 256.00 | 297.00 | 2.20 | NÃO | fora do lado solicitado |
| 547 | 321.00 | 256.00 | 296.00 | 2.20 | NÃO | fora do lado solicitado |
| 548 | 322.00 | 256.00 | 295.00 | 2.20 | NÃO | fora do lado solicitado |
| 549 | 323.00 | 256.00 | 294.00 | 2.20 | NÃO | fora do lado solicitado |
| 550 | 324.00 | 256.00 | 293.00 | 2.20 | NÃO | fora do lado solicitado |
| 551 | 325.00 | 256.00 | 292.00 | 2.20 | NÃO | fora do lado solicitado |
| 552 | 326.00 | 256.00 | 291.00 | 2.20 | NÃO | fora do lado solicitado |
| 553 | 327.00 | 256.00 | 290.00 | 2.20 | NÃO | fora do lado solicitado |
| 554 | 328.00 | 256.00 | 289.00 | 2.20 | NÃO | fora do lado solicitado |
| 555 | 329.00 | 256.00 | 288.00 | 2.20 | NÃO | fora do lado solicitado |
| 556 | 330.00 | 256.00 | 287.00 | 2.20 | NÃO | fora do lado solicitado |
| 557 | 331.00 | 256.00 | 286.00 | 2.20 | NÃO | fora do lado solicitado |
| 558 | 332.00 | 256.00 | 285.00 | 2.20 | NÃO | fora do lado solicitado |
| 559 | 333.00 | 256.00 | 284.00 | 2.20 | NÃO | fora do lado solicitado |
| 560 | 334.00 | 256.00 | 283.00 | 2.20 | NÃO | fora do lado solicitado |
| 561 | 335.00 | 256.00 | 282.00 | 2.20 | NÃO | fora do lado solicitado |
| 562 | 336.00 | 256.00 | 281.00 | 2.20 | NÃO | fora do lado solicitado |
| 563 | 337.00 | 256.00 | 280.00 | 2.20 | NÃO | fora do lado solicitado |
| 564 | 338.00 | 256.00 | 279.00 | 2.20 | NÃO | fora do lado solicitado |
| 565 | 339.00 | 256.00 | 278.00 | 2.20 | NÃO | fora do lado solicitado |
| 566 | 340.00 | 256.00 | 277.00 | 2.20 | NÃO | fora do lado solicitado |
| 567 | 341.00 | 256.00 | 276.00 | 2.20 | NÃO | fora do lado solicitado |
| 568 | 342.00 | 256.00 | 275.00 | 2.20 | NÃO | fora do lado solicitado |
| 569 | 343.00 | 256.00 | 274.00 | 2.20 | NÃO | fora do lado solicitado |
| 570 | 344.00 | 256.00 | 273.00 | 2.20 | NÃO | fora do lado solicitado |
| 571 | 345.00 | 256.00 | 272.00 | 2.20 | NÃO | fora do lado solicitado |
| 572 | 346.00 | 256.00 | 271.00 | 2.20 | NÃO | fora do lado solicitado |
| 573 | 347.00 | 256.00 | 270.00 | 2.20 | NÃO | fora do lado solicitado |
| 574 | 348.00 | 256.00 | 269.00 | 2.20 | NÃO | fora do lado solicitado |
| 575 | 349.00 | 256.00 | 268.00 | 2.20 | NÃO | fora do lado solicitado |
| 576 | 350.00 | 256.00 | 267.00 | 2.20 | NÃO | fora do lado solicitado |
| 577 | 351.00 | 256.00 | 266.00 | 2.20 | NÃO | fora do lado solicitado |
| 578 | 352.00 | 256.00 | 265.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 579 | 353.00 | 256.00 | 264.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 580 | 354.00 | 256.00 | 263.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 581 | 355.00 | 256.00 | 262.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 582 | 356.00 | 256.00 | 261.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 583 | 357.00 | 256.00 | 260.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 584 | 358.00 | 256.00 | 259.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 585 | 359.00 | 256.00 | 258.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 586 | 360.00 | 256.00 | 257.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 587 | 361.00 | 256.00 | 256.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 588 | 362.00 | 256.00 | 255.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 589 | 363.00 | 256.00 | 254.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 590 | 364.00 | 256.00 | 253.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 591 | 365.00 | 256.00 | 252.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 592 | 366.00 | 256.00 | 251.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 593 | 367.00 | 256.00 | 250.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 594 | 368.00 | 256.00 | 249.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 595 | 369.00 | 256.00 | 248.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 596 | 370.00 | 256.00 | 247.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 597 | 371.00 | 256.00 | 246.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 598 | 372.00 | 256.00 | 245.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 599 | 373.00 | 256.00 | 244.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 600 | 374.00 | 256.00 | 243.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 601 | 375.00 | 256.00 | 242.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 602 | 376.00 | 256.00 | 241.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 603 | 377.00 | 256.00 | 240.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 604 | 378.00 | 256.00 | 239.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 605 | 379.00 | 256.00 | 238.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 606 | 380.00 | 256.00 | 237.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 607 | 381.00 | 256.00 | 236.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 608 | 382.00 | 256.00 | 235.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 609 | 383.00 | 256.00 | 234.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 610 | 384.00 | 256.00 | 233.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 611 | 385.00 | 256.00 | 232.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 612 | 386.00 | 256.00 | 231.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 613 | 387.00 | 256.00 | 230.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 614 | 388.00 | 256.00 | 229.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 615 | 389.00 | 256.00 | 228.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 616 | 390.00 | 256.00 | 227.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 617 | 391.00 | 256.00 | 226.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 618 | 392.00 | 256.00 | 225.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 619 | 393.00 | 256.00 | 224.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 620 | 394.00 | 256.00 | 223.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 621 | 395.00 | 256.00 | 222.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 622 | 396.00 | 256.00 | 221.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 623 | 397.00 | 256.00 | 220.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 624 | 398.00 | 256.00 | 219.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 625 | 399.00 | 256.00 | 218.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 626 | 400.00 | 256.00 | 217.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 627 | 401.00 | 256.00 | 216.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 628 | 402.00 | 256.00 | 215.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 629 | 403.00 | 256.00 | 214.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 630 | 404.00 | 256.00 | 213.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 631 | 405.00 | 256.00 | 212.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 632 | 406.00 | 256.00 | 211.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 633 | 407.00 | 256.00 | 210.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 634 | 408.00 | 256.00 | 209.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 635 | 409.00 | 256.00 | 208.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 636 | 410.00 | 256.00 | 207.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 637 | 411.00 | 256.00 | 206.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 638 | 412.00 | 256.00 | 205.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 639 | 413.00 | 256.00 | 204.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 640 | 414.00 | 256.00 | 203.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 641 | 415.00 | 256.00 | 202.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 642 | 416.00 | 256.00 | 201.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 643 | 417.00 | 256.00 | 200.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 644 | 418.00 | 256.00 | 199.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 645 | 419.00 | 256.00 | 198.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 646 | 420.00 | 256.00 | 197.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 647 | 421.00 | 256.00 | 196.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 648 | 422.00 | 256.00 | 195.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 649 | 423.00 | 256.00 | 194.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 650 | 424.00 | 256.00 | 193.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 651 | 425.00 | 256.00 | 192.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 652 | 426.00 | 256.00 | 191.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 653 | 427.00 | 256.00 | 190.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 654 | 428.00 | 256.00 | 189.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 655 | 429.00 | 256.00 | 188.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 656 | 430.00 | 256.00 | 187.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 657 | 431.00 | 256.00 | 186.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 658 | 432.00 | 256.00 | 185.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 659 | 433.00 | 256.00 | 184.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 660 | 434.00 | 256.00 | 183.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 661 | 435.00 | 256.00 | 182.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 662 | 436.00 | 256.00 | 181.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 663 | 437.00 | 256.00 | 180.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 664 | 438.00 | 256.00 | 179.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 665 | 439.00 | 256.00 | 178.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 666 | 440.00 | 256.00 | 177.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 667 | 441.00 | 256.00 | 176.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 668 | 442.00 | 256.00 | 175.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 669 | 443.00 | 256.00 | 174.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 670 | 444.00 | 256.00 | 173.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 671 | 445.00 | 256.00 | 172.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 672 | 446.00 | 256.00 | 171.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 673 | 447.00 | 256.00 | 170.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 674 | 448.00 | 256.00 | 169.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 675 | 449.00 | 256.00 | 168.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 676 | 450.00 | 256.00 | 167.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 677 | 451.00 | 256.00 | 166.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 678 | 452.00 | 256.00 | 165.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 679 | 453.00 | 256.00 | 164.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 680 | 454.00 | 256.00 | 163.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 681 | 455.00 | 256.00 | 162.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 682 | 456.00 | 256.00 | 161.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 683 | 457.00 | 256.00 | 160.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 684 | 458.00 | 256.00 | 159.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 685 | 459.00 | 256.00 | 158.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 686 | 460.00 | 256.00 | 157.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 687 | 461.00 | 256.00 | 156.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 688 | 462.00 | 256.00 | 155.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 689 | 463.00 | 256.00 | 154.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 690 | 464.00 | 256.00 | 153.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 691 | 465.00 | 256.00 | 152.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 692 | 466.00 | 256.00 | 151.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 693 | 467.00 | 256.00 | 150.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 694 | 468.00 | 256.00 | 149.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 695 | 469.00 | 256.00 | 148.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 696 | 470.00 | 256.00 | 147.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 697 | 471.00 | 256.00 | 146.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 698 | 472.00 | 256.00 | 145.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 699 | 473.00 | 256.00 | 144.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 700 | 474.00 | 256.00 | 143.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 701 | 475.00 | 256.00 | 142.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 702 | 476.00 | 256.00 | 141.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 703 | 477.00 | 256.00 | 140.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 704 | 478.00 | 256.00 | 139.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 705 | 479.00 | 256.00 | 138.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 706 | 480.00 | 256.00 | 137.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 707 | 481.00 | 256.00 | 136.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 708 | 482.00 | 256.00 | 135.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 709 | 483.00 | 256.00 | 134.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 710 | 484.00 | 256.00 | 133.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 711 | 485.00 | 256.00 | 132.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 712 | 486.00 | 256.00 | 131.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 713 | 487.00 | 256.00 | 130.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 714 | 488.00 | 256.00 | 129.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 715 | 489.00 | 256.00 | 128.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 716 | 490.00 | 256.00 | 127.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 717 | 491.00 | 256.00 | 126.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 718 | 492.00 | 256.00 | 125.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 719 | 493.00 | 256.00 | 124.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 720 | 494.00 | 256.00 | 123.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 721 | 495.00 | 256.00 | 122.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 722 | 496.00 | 256.00 | 121.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 723 | 497.00 | 256.00 | 120.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 724 | 498.00 | 256.00 | 119.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 725 | 499.00 | 256.00 | 118.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 726 | 500.00 | 256.00 | 117.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 727 | 501.00 | 256.00 | 116.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 728 | 502.00 | 256.00 | 115.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 729 | 503.00 | 256.00 | 114.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 730 | 504.00 | 256.00 | 113.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 731 | 505.00 | 256.00 | 112.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 732 | 506.00 | 256.00 | 111.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 733 | 507.00 | 256.00 | 110.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 734 | 508.00 | 256.00 | 109.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 735 | 509.00 | 256.00 | 108.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 736 | 510.00 | 256.00 | 107.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 737 | 511.00 | 256.00 | 106.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 738 | 512.00 | 256.00 | 105.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 739 | 513.00 | 256.00 | 104.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 740 | 514.00 | 256.00 | 103.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 741 | 515.00 | 256.00 | 102.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 742 | 516.00 | 256.00 | 101.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 743 | 517.00 | 256.00 | 100.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 744 | 518.00 | 256.00 | 99.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 745 | 519.00 | 256.00 | 98.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 746 | 520.00 | 256.00 | 97.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 747 | 521.00 | 256.00 | 96.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 748 | 522.00 | 256.00 | 95.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 749 | 523.00 | 256.00 | 94.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 750 | 524.00 | 256.00 | 93.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 751 | 525.00 | 256.00 | 92.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 752 | 526.00 | 256.00 | 91.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 753 | 527.00 | 256.00 | 90.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 754 | 528.00 | 256.00 | 89.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 755 | 529.00 | 256.00 | 88.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 756 | 530.00 | 256.00 | 87.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 757 | 531.00 | 256.00 | 86.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 758 | 532.00 | 256.00 | 85.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 759 | 533.00 | 256.00 | 84.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 760 | 534.00 | 256.00 | 83.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 761 | 535.00 | 256.00 | 82.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 762 | 536.00 | 256.00 | 81.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 763 | 537.00 | 256.00 | 80.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 764 | 538.00 | 256.00 | 79.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 765 | 539.00 | 256.00 | 78.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 766 | 540.00 | 256.00 | 77.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 767 | 541.00 | 256.00 | 76.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 768 | 542.00 | 256.00 | 75.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 769 | 543.00 | 256.00 | 74.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 770 | 544.00 | 256.00 | 73.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 771 | 545.00 | 256.00 | 72.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 772 | 546.00 | 256.00 | 71.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 773 | 547.00 | 256.00 | 70.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 774 | 548.00 | 256.00 | 69.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 775 | 549.00 | 256.00 | 68.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 776 | 550.00 | 256.00 | 67.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 777 | 551.00 | 256.00 | 66.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 778 | 552.00 | 256.00 | 65.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 779 | 553.00 | 256.00 | 64.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 780 | 554.00 | 256.00 | 63.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 781 | 555.00 | 256.00 | 62.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 782 | 556.00 | 256.00 | 61.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 783 | 557.00 | 256.00 | 60.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 784 | 558.00 | 256.00 | 59.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 785 | 559.00 | 256.00 | 58.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 786 | 560.00 | 256.00 | 57.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 787 | 561.00 | 256.00 | 56.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 788 | 562.00 | 256.00 | 55.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 789 | 563.00 | 256.00 | 54.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 790 | 564.00 | 256.00 | 53.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 791 | 565.00 | 256.00 | 52.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 792 | 566.00 | 256.00 | 51.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 793 | 567.00 | 256.00 | 50.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 794 | 568.00 | 256.00 | 49.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 795 | 569.00 | 256.00 | 48.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 796 | 570.00 | 256.00 | 47.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 797 | 571.00 | 256.00 | 46.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 798 | 572.00 | 256.00 | 45.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 799 | 573.00 | 256.00 | 44.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 800 | 574.00 | 256.00 | 43.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 801 | 575.00 | 256.00 | 42.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 802 | 576.00 | 256.00 | 41.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 803 | 577.00 | 256.00 | 40.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 804 | 578.00 | 256.00 | 39.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 805 | 579.00 | 256.00 | 38.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 806 | 580.00 | 256.00 | 37.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 807 | 581.00 | 256.00 | 36.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 808 | 582.00 | 256.00 | 35.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 809 | 583.00 | 256.00 | 34.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 810 | 584.00 | 256.00 | 33.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 811 | 585.00 | 256.00 | 32.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 812 | 586.00 | 256.00 | 31.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 813 | 587.00 | 256.00 | 30.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 814 | 588.00 | 256.00 | 29.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 815 | 589.00 | 256.00 | 28.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 816 | 590.00 | 256.00 | 27.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 817 | 591.00 | 256.00 | 26.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 818 | 592.00 | 256.00 | 25.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 819 | 593.00 | 256.00 | 24.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 820 | 594.00 | 256.00 | 23.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 821 | 595.00 | 256.00 | 22.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 822 | 596.00 | 256.00 | 21.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 823 | 597.00 | 256.00 | 20.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 824 | 598.00 | 256.00 | 19.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 825 | 599.00 | 256.00 | 18.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 826 | 600.00 | 256.00 | 17.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 827 | 601.00 | 256.00 | 16.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 828 | 602.00 | 256.00 | 15.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 829 | 603.00 | 256.00 | 14.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 830 | 604.00 | 256.00 | 13.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 831 | 605.00 | 256.00 | 12.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 832 | 606.00 | 256.00 | 11.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 833 | 607.00 | 256.00 | 10.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 834 | 608.00 | 256.00 | 9.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 835 | 609.00 | 256.00 | 8.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 836 | 610.00 | 256.00 | 7.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 837 | 611.00 | 256.00 | 6.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 838 | 612.00 | 256.00 | 5.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 839 | 613.00 | 256.00 | 4.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 840 | 614.00 | 256.00 | 3.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 841 | 615.00 | 256.00 | 2.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 842 | 616.00 | 256.00 | 1.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 843 | 617.00 | 256.00 | 0.00 | 2.20 | SIM | dentro da janela vertical e do lado solicitado |
| 844 | 616.00 | 255.00 | 1.41 | 3.20 | SIM | dentro da janela vertical e do lado solicitado |
| 845 | 616.00 | 254.00 | 2.24 | 4.20 | SIM | dentro da janela vertical e do lado solicitado |
| 846 | 616.00 | 253.00 | 3.16 | 5.20 | SIM | dentro da janela vertical e do lado solicitado |
| 847 | 616.00 | 252.00 | 4.12 | 6.20 | SIM | dentro da janela vertical e do lado solicitado |
| 848 | 616.00 | 251.00 | 5.10 | 7.20 | SIM | dentro da janela vertical e do lado solicitado |
| 849 | 615.00 | 250.00 | 6.32 | 8.20 | SIM | dentro da janela vertical e do lado solicitado |
| 850 | 615.00 | 249.00 | 7.28 | 9.20 | SIM | dentro da janela vertical e do lado solicitado |
| 851 | 615.00 | 248.00 | 8.25 | 10.20 | SIM | dentro da janela vertical e do lado solicitado |
| 852 | 615.00 | 247.00 | 9.22 | 11.20 | SIM | dentro da janela vertical e do lado solicitado |
| 853 | 615.00 | 246.00 | 10.20 | 12.20 | SIM | dentro da janela vertical e do lado solicitado |
| 854 | 614.00 | 245.00 | 11.40 | 13.20 | SIM | dentro da janela vertical e do lado solicitado |
| 855 | 614.00 | 244.00 | 12.37 | 14.20 | SIM | dentro da janela vertical e do lado solicitado |
| 856 | 614.00 | 243.00 | 13.34 | 15.20 | SIM | dentro da janela vertical e do lado solicitado |
| 857 | 614.00 | 242.00 | 14.32 | 16.20 | SIM | dentro da janela vertical e do lado solicitado |
| 858 | 613.00 | 241.00 | 15.52 | 17.20 | SIM | dentro da janela vertical e do lado solicitado |
| 859 | 613.00 | 240.00 | 16.49 | 18.20 | SIM | dentro da janela vertical e do lado solicitado |
| 860 | 613.00 | 239.00 | 17.46 | 19.20 | SIM | dentro da janela vertical e do lado solicitado |
| 861 | 613.00 | 238.00 | 18.44 | 20.20 | SIM | dentro da janela vertical e do lado solicitado |
| 862 | 612.00 | 237.00 | 19.65 | 21.20 | SIM | dentro da janela vertical e do lado solicitado |
| 863 | 612.00 | 236.00 | 20.62 | 22.20 | SIM | dentro da janela vertical e do lado solicitado |
| 864 | 612.00 | 235.00 | 21.59 | 23.20 | SIM | dentro da janela vertical e do lado solicitado |
| 865 | 612.00 | 234.00 | 22.56 | 24.20 | SIM | dentro da janela vertical e do lado solicitado |
| 866 | 611.00 | 233.00 | 23.77 | 25.20 | SIM | dentro da janela vertical e do lado solicitado |
| 867 | 611.00 | 232.00 | 24.74 | 26.20 | SIM | dentro da janela vertical e do lado solicitado |
| 868 | 611.00 | 231.00 | 25.71 | 27.20 | SIM | dentro da janela vertical e do lado solicitado |
| 869 | 610.00 | 230.00 | 26.93 | 28.20 | SIM | dentro da janela vertical e do lado solicitado |
| 870 | 610.00 | 229.00 | 27.89 | 29.20 | SIM | dentro da janela vertical e do lado solicitado |
| 871 | 610.00 | 228.00 | 28.86 | 30.20 | SIM | dentro da janela vertical e do lado solicitado |
| 872 | 609.00 | 227.00 | 30.08 | 31.20 | SIM | dentro da janela vertical e do lado solicitado |
| 873 | 609.00 | 226.00 | 31.05 | 32.20 | SIM | dentro da janela vertical e do lado solicitado |
| 874 | 609.00 | 225.00 | 32.02 | 33.20 | SIM | dentro da janela vertical e do lado solicitado |
| 875 | 609.00 | 224.00 | 32.98 | 34.20 | SIM | dentro da janela vertical e do lado solicitado |
| 876 | 608.00 | 223.00 | 34.21 | 35.20 | SIM | dentro da janela vertical e do lado solicitado |
| 877 | 608.00 | 222.00 | 35.17 | 36.20 | SIM | dentro da janela vertical e do lado solicitado |
| 878 | 608.00 | 221.00 | 36.14 | 37.20 | SIM | dentro da janela vertical e do lado solicitado |
| 879 | 607.00 | 220.00 | 37.36 | 38.20 | SIM | dentro da janela vertical e do lado solicitado |
| 880 | 607.00 | 219.00 | 38.33 | 39.20 | SIM | dentro da janela vertical e do lado solicitado |
| 881 | 607.00 | 218.00 | 39.29 | 40.20 | SIM | dentro da janela vertical e do lado solicitado |
| 882 | 606.00 | 217.00 | 40.52 | 41.20 | SIM | dentro da janela vertical e do lado solicitado |
| 883 | 606.00 | 216.00 | 41.48 | 42.20 | SIM | dentro da janela vertical e do lado solicitado |
| 884 | 606.00 | 215.00 | 42.45 | 43.20 | SIM | dentro da janela vertical e do lado solicitado |
| 885 | 605.00 | 214.00 | 43.68 | 44.20 | SIM | dentro da janela vertical e do lado solicitado |
| 886 | 605.00 | 213.00 | 44.64 | 45.20 | SIM | dentro da janela vertical e do lado solicitado |
| 887 | 604.00 | 212.00 | 45.88 | 46.20 | SIM | dentro da janela vertical e do lado solicitado |
| 888 | 604.00 | 211.00 | 46.84 | 47.20 | SIM | dentro da janela vertical e do lado solicitado |
| 889 | 604.00 | 210.00 | 47.80 | 48.20 | SIM | dentro da janela vertical e do lado solicitado |
| 890 | 603.00 | 209.00 | 49.04 | 49.20 | SIM | dentro da janela vertical e do lado solicitado |
| 891 | 603.00 | 208.00 | 50.00 | 50.20 | SIM | dentro da janela vertical e do lado solicitado |
| 892 | 602.00 | 207.00 | 51.24 | 51.20 | SIM | dentro da janela vertical e do lado solicitado |
| 893 | 602.00 | 206.00 | 52.20 | 52.20 | SIM | dentro da janela vertical e do lado solicitado |
| 894 | 602.00 | 205.00 | 53.16 | 53.20 | SIM | dentro da janela vertical e do lado solicitado |
| 895 | 601.00 | 204.00 | 54.41 | 54.20 | SIM | dentro da janela vertical e do lado solicitado |
| 896 | 601.00 | 203.00 | 55.36 | 55.20 | SIM | dentro da janela vertical e do lado solicitado |
| 897 | 601.00 | 202.00 | 56.32 | 56.20 | SIM | dentro da janela vertical e do lado solicitado |
| 898 | 600.00 | 201.00 | 57.57 | 57.20 | SIM | dentro da janela vertical e do lado solicitado |
| 899 | 600.00 | 200.00 | 58.52 | 58.20 | SIM | dentro da janela vertical e do lado solicitado |
| 900 | 599.00 | 199.00 | 59.77 | 59.20 | SIM | dentro da janela vertical e do lado solicitado |
| 901 | 599.00 | 198.00 | 60.73 | 60.20 | SIM | dentro da janela vertical e do lado solicitado |
| 902 | 598.00 | 197.00 | 61.98 | 61.20 | SIM | dentro da janela vertical e do lado solicitado |
| 903 | 598.00 | 196.00 | 62.94 | 62.20 | SIM | dentro da janela vertical e do lado solicitado |
| 904 | 597.00 | 195.00 | 64.20 | 63.20 | SIM | dentro da janela vertical e do lado solicitado |
| 905 | 597.00 | 194.00 | 65.15 | 64.20 | SIM | dentro da janela vertical e do lado solicitado |
| 906 | 597.00 | 193.00 | 66.10 | 65.20 | SIM | dentro da janela vertical e do lado solicitado |
| 907 | 596.00 | 192.00 | 67.36 | 66.20 | SIM | dentro da janela vertical e do lado solicitado |
| 908 | 596.00 | 191.00 | 68.31 | 67.20 | SIM | dentro da janela vertical e do lado solicitado |
| 909 | 595.00 | 190.00 | 69.57 | 68.20 | SIM | dentro da janela vertical e do lado solicitado |
| 910 | 595.00 | 189.00 | 70.52 | 69.20 | SIM | dentro da janela vertical e do lado solicitado |
| 911 | 594.00 | 188.00 | 71.78 | 70.20 | SIM | dentro da janela vertical e do lado solicitado |
| 912 | 594.00 | 187.00 | 72.73 | 71.20 | SIM | dentro da janela vertical e do lado solicitado |
| 913 | 593.00 | 186.00 | 74.00 | 72.20 | SIM | dentro da janela vertical e do lado solicitado |
| 914 | 593.00 | 185.00 | 74.95 | 73.20 | SIM | dentro da janela vertical e do lado solicitado |
| 915 | 592.00 | 184.00 | 76.22 | 74.20 | SIM | dentro da janela vertical e do lado solicitado |
| 916 | 592.00 | 183.00 | 77.16 | 75.20 | SIM | dentro da janela vertical e do lado solicitado |
| 917 | 591.00 | 182.00 | 78.43 | 76.20 | SIM | dentro da janela vertical e do lado solicitado |
| 918 | 591.00 | 181.00 | 79.38 | 77.20 | SIM | dentro da janela vertical e do lado solicitado |
| 919 | 590.00 | 180.00 | 80.65 | 78.20 | SIM | dentro da janela vertical e do lado solicitado |
| 920 | 590.00 | 179.00 | 81.60 | 79.20 | SIM | dentro da janela vertical e do lado solicitado |
| 921 | 589.00 | 178.00 | 82.87 | 80.20 | SIM | dentro da janela vertical e do lado solicitado |
| 922 | 589.00 | 177.00 | 83.82 | 81.20 | SIM | dentro da janela vertical e do lado solicitado |
| 923 | 588.00 | 176.00 | 85.09 | 82.20 | SIM | dentro da janela vertical e do lado solicitado |
| 924 | 588.00 | 175.00 | 86.03 | 83.20 | SIM | dentro da janela vertical e do lado solicitado |
| 925 | 587.00 | 174.00 | 87.32 | 84.20 | SIM | dentro da janela vertical e do lado solicitado |
| 926 | 586.00 | 173.00 | 88.60 | 85.20 | SIM | dentro da janela vertical e do lado solicitado |
| 927 | 586.00 | 172.00 | 89.54 | 86.20 | SIM | dentro da janela vertical e do lado solicitado |
| 928 | 585.00 | 171.00 | 90.82 | 87.20 | SIM | dentro da janela vertical e do lado solicitado |
| 929 | 585.00 | 170.00 | 91.76 | 88.20 | SIM | dentro da janela vertical e do lado solicitado |
| 930 | 584.00 | 169.00 | 93.05 | 89.20 | SIM | dentro da janela vertical e do lado solicitado |
| 931 | 584.00 | 168.00 | 93.98 | 90.20 | SIM | dentro da janela vertical e do lado solicitado |
| 932 | 583.00 | 167.00 | 95.27 | 91.20 | SIM | dentro da janela vertical e do lado solicitado |
| 933 | 582.00 | 166.00 | 96.57 | 92.20 | SIM | dentro da janela vertical e do lado solicitado |
| 934 | 582.00 | 165.00 | 97.50 | 93.20 | SIM | dentro da janela vertical e do lado solicitado |
| 935 | 581.00 | 164.00 | 98.79 | 94.20 | SIM | dentro da janela vertical e do lado solicitado |
| 936 | 581.00 | 163.00 | 99.72 | 95.20 | SIM | dentro da janela vertical e do lado solicitado |
| 937 | 580.00 | 162.00 | 101.02 | 96.20 | SIM | dentro da janela vertical e do lado solicitado |
| 938 | 579.00 | 161.00 | 102.32 | 97.20 | SIM | dentro da janela vertical e do lado solicitado |
| 939 | 579.00 | 160.00 | 103.25 | 98.20 | SIM | dentro da janela vertical e do lado solicitado |
| 940 | 578.00 | 159.00 | 104.55 | 99.20 | SIM | dentro da janela vertical e do lado solicitado |
| 941 | 577.00 | 158.00 | 105.85 | 100.20 | SIM | dentro da janela vertical e do lado solicitado |
| 942 | 577.00 | 157.00 | 106.78 | 101.20 | SIM | dentro da janela vertical e do lado solicitado |
| 943 | 576.00 | 156.00 | 108.08 | 102.20 | SIM | dentro da janela vertical e do lado solicitado |
| 944 | 575.00 | 155.00 | 109.38 | 103.20 | SIM | dentro da janela vertical e do lado solicitado |
| 945 | 575.00 | 154.00 | 110.31 | 104.20 | SIM | dentro da janela vertical e do lado solicitado |
| 946 | 574.00 | 153.00 | 111.62 | 105.20 | SIM | dentro da janela vertical e do lado solicitado |
| 947 | 573.00 | 152.00 | 112.92 | 106.20 | SIM | dentro da janela vertical e do lado solicitado |
| 948 | 573.00 | 151.00 | 113.85 | 107.20 | SIM | dentro da janela vertical e do lado solicitado |
| 949 | 572.00 | 150.00 | 115.16 | 108.20 | SIM | dentro da janela vertical e do lado solicitado |
| 950 | 571.00 | 149.00 | 116.47 | 109.20 | SIM | dentro da janela vertical e do lado solicitado |
| 951 | 571.00 | 148.00 | 117.39 | 110.20 | SIM | dentro da janela vertical e do lado solicitado |
| 952 | 570.00 | 147.00 | 118.70 | 111.20 | SIM | dentro da janela vertical e do lado solicitado |
| 953 | 569.00 | 146.00 | 120.02 | 112.20 | SIM | dentro da janela vertical e do lado solicitado |
| 954 | 568.00 | 145.00 | 121.33 | 113.20 | SIM | dentro da janela vertical e do lado solicitado |
| 955 | 568.00 | 144.00 | 122.25 | 114.20 | SIM | dentro da janela vertical e do lado solicitado |
| 956 | 567.00 | 143.00 | 123.57 | 115.20 | SIM | dentro da janela vertical e do lado solicitado |
| 957 | 566.00 | 142.00 | 124.89 | 116.20 | SIM | dentro da janela vertical e do lado solicitado |
| 958 | 565.00 | 141.00 | 126.21 | 117.20 | SIM | dentro da janela vertical e do lado solicitado |
| 959 | 565.00 | 140.00 | 127.12 | 118.20 | SIM | dentro da janela vertical e do lado solicitado |
| 960 | 564.00 | 139.00 | 128.44 | 119.20 | SIM | dentro da janela vertical e do lado solicitado |
| 961 | 563.00 | 138.00 | 129.77 | 120.20 | SIM | dentro da janela vertical e do lado solicitado |
| 962 | 562.00 | 137.00 | 131.10 | 121.20 | NÃO | fora da faixa vertical |
| 963 | 561.00 | 136.00 | 132.42 | 122.20 | NÃO | fora da faixa vertical |
| 964 | 561.00 | 135.00 | 133.33 | 123.20 | NÃO | fora da faixa vertical |
| 965 | 560.00 | 134.00 | 134.66 | 124.20 | NÃO | fora da faixa vertical |
| 966 | 559.00 | 133.00 | 135.99 | 125.20 | NÃO | fora da faixa vertical |
| 967 | 558.00 | 132.00 | 137.32 | 126.20 | NÃO | fora da faixa vertical |
| 968 | 557.00 | 131.00 | 138.65 | 127.20 | NÃO | fora da faixa vertical |
| 969 | 557.00 | 130.00 | 139.56 | 128.20 | NÃO | fora da faixa vertical |
| 970 | 556.00 | 129.00 | 140.89 | 129.20 | NÃO | fora da faixa vertical |
| 971 | 555.00 | 128.00 | 142.23 | 130.20 | NÃO | fora da faixa vertical |
| 972 | 554.00 | 127.00 | 143.56 | 131.20 | NÃO | fora da faixa vertical |
| 973 | 553.00 | 126.00 | 144.90 | 132.20 | NÃO | fora da faixa vertical |
| 974 | 552.00 | 125.00 | 146.24 | 133.20 | NÃO | fora da faixa vertical |
| 975 | 551.00 | 124.00 | 147.58 | 134.20 | NÃO | fora da faixa vertical |
| 976 | 550.00 | 123.00 | 148.92 | 135.20 | NÃO | fora da faixa vertical |
| 977 | 549.00 | 122.00 | 150.27 | 136.20 | NÃO | fora da faixa vertical |
| 978 | 548.00 | 121.00 | 151.61 | 137.20 | NÃO | fora da faixa vertical |
| 979 | 547.00 | 120.00 | 152.96 | 138.20 | NÃO | fora da faixa vertical |
| 980 | 546.00 | 119.00 | 154.30 | 139.20 | NÃO | fora da faixa vertical |
| 981 | 545.00 | 118.00 | 155.65 | 140.20 | NÃO | fora da faixa vertical |
| 982 | 545.00 | 117.00 | 156.54 | 141.20 | NÃO | fora da faixa vertical |
| 983 | 544.00 | 116.00 | 157.89 | 142.20 | NÃO | fora da faixa vertical |
| 984 | 543.00 | 115.00 | 159.24 | 143.20 | NÃO | fora da faixa vertical |
| 985 | 542.00 | 114.00 | 160.59 | 144.20 | NÃO | fora da faixa vertical |
| 986 | 541.00 | 113.00 | 161.94 | 145.20 | NÃO | fora da faixa vertical |
| 987 | 540.00 | 112.00 | 163.29 | 146.20 | NÃO | fora da faixa vertical |
| 988 | 539.00 | 111.00 | 164.65 | 147.20 | NÃO | fora da faixa vertical |
| 989 | 538.00 | 111.00 | 165.12 | 147.20 | NÃO | fora da faixa vertical |
| 990 | 537.00 | 110.00 | 166.48 | 148.20 | NÃO | fora da faixa vertical |
| 991 | 536.00 | 109.00 | 167.84 | 149.20 | NÃO | fora da faixa vertical |
| 992 | 535.00 | 108.00 | 169.20 | 150.20 | NÃO | fora da faixa vertical |
| 993 | 534.00 | 107.00 | 170.56 | 151.20 | NÃO | fora da faixa vertical |
| 994 | 533.00 | 106.00 | 171.92 | 152.20 | NÃO | fora da faixa vertical |
| 995 | 532.00 | 105.00 | 173.28 | 153.20 | NÃO | fora da faixa vertical |
| 996 | 531.00 | 104.00 | 174.64 | 154.20 | NÃO | fora da faixa vertical |
| 997 | 530.00 | 103.00 | 176.01 | 155.20 | NÃO | fora da faixa vertical |
| 998 | 529.00 | 102.00 | 177.37 | 156.20 | NÃO | fora da faixa vertical |
| 999 | 528.00 | 101.00 | 178.73 | 157.20 | NÃO | fora da faixa vertical |
| 1000 | 527.00 | 101.00 | 179.23 | 157.20 | NÃO | fora da faixa vertical |
| 1001 | 526.00 | 100.00 | 180.60 | 158.20 | NÃO | fora da faixa vertical |
| 1002 | 525.00 | 99.00 | 181.97 | 159.20 | NÃO | fora da faixa vertical |
| 1003 | 524.00 | 98.00 | 183.34 | 160.20 | NÃO | fora da faixa vertical |
| 1004 | 523.00 | 97.00 | 184.71 | 161.20 | NÃO | fora da faixa vertical |
| 1005 | 522.00 | 96.00 | 186.08 | 162.20 | NÃO | fora da faixa vertical |
| 1006 | 521.00 | 96.00 | 186.59 | 162.20 | NÃO | fora da faixa vertical |
| 1007 | 520.00 | 95.00 | 187.96 | 163.20 | NÃO | fora da faixa vertical |
| 1008 | 519.00 | 94.00 | 189.34 | 164.20 | NÃO | fora da faixa vertical |
| 1009 | 518.00 | 93.00 | 190.71 | 165.20 | NÃO | fora da faixa vertical |
| 1010 | 517.00 | 92.00 | 192.08 | 166.20 | NÃO | fora da faixa vertical |
| 1011 | 516.00 | 92.00 | 192.61 | 166.20 | NÃO | fora da faixa vertical |
| 1012 | 515.00 | 91.00 | 193.98 | 167.20 | NÃO | fora da faixa vertical |
| 1013 | 514.00 | 90.00 | 195.36 | 168.20 | NÃO | fora da faixa vertical |
| 1014 | 513.00 | 89.00 | 196.74 | 169.20 | NÃO | fora da faixa vertical |
| 1015 | 512.00 | 88.00 | 198.11 | 170.20 | NÃO | fora da faixa vertical |
| 1016 | 511.00 | 88.00 | 198.65 | 170.20 | NÃO | fora da faixa vertical |
| 1017 | 510.00 | 87.00 | 200.02 | 171.20 | NÃO | fora da faixa vertical |
| 1018 | 509.00 | 86.00 | 201.41 | 172.20 | NÃO | fora da faixa vertical |
| 1019 | 508.00 | 86.00 | 201.94 | 172.20 | NÃO | fora da faixa vertical |
| 1020 | 507.00 | 85.00 | 203.32 | 173.20 | NÃO | fora da faixa vertical |
| 1021 | 506.00 | 84.00 | 204.71 | 174.20 | NÃO | fora da faixa vertical |
| 1022 | 505.00 | 84.00 | 205.25 | 174.20 | NÃO | fora da faixa vertical |
| 1023 | 504.00 | 83.00 | 206.63 | 175.20 | NÃO | fora da faixa vertical |
| 1024 | 503.00 | 82.00 | 208.02 | 176.20 | NÃO | fora da faixa vertical |
| 1025 | 502.00 | 82.00 | 208.57 | 176.20 | NÃO | fora da faixa vertical |
| 1026 | 501.00 | 81.00 | 209.95 | 177.20 | NÃO | fora da faixa vertical |
| 1027 | 500.00 | 80.00 | 211.34 | 178.20 | NÃO | fora da faixa vertical |
| 1028 | 499.00 | 80.00 | 211.90 | 178.20 | NÃO | fora da faixa vertical |
| 1029 | 498.00 | 79.00 | 213.28 | 179.20 | NÃO | fora da faixa vertical |
| 1030 | 497.00 | 78.00 | 214.67 | 180.20 | NÃO | fora da faixa vertical |
| 1031 | 496.00 | 78.00 | 215.23 | 180.20 | NÃO | fora da faixa vertical |
| 1032 | 495.00 | 77.00 | 216.62 | 181.20 | NÃO | fora da faixa vertical |
| 1033 | 494.00 | 76.00 | 218.01 | 182.20 | NÃO | fora da faixa vertical |
| 1034 | 493.00 | 76.00 | 218.58 | 182.20 | NÃO | fora da faixa vertical |
| 1035 | 492.00 | 75.00 | 219.97 | 183.20 | NÃO | fora da faixa vertical |
| 1036 | 491.00 | 75.00 | 220.54 | 183.20 | NÃO | fora da faixa vertical |
| 1037 | 490.00 | 74.00 | 221.93 | 184.20 | NÃO | fora da faixa vertical |
| 1038 | 489.00 | 73.00 | 223.32 | 185.20 | NÃO | fora da faixa vertical |
| 1039 | 488.00 | 73.00 | 223.90 | 185.20 | NÃO | fora da faixa vertical |
| 1040 | 487.00 | 72.00 | 225.29 | 186.20 | NÃO | fora da faixa vertical |
| 1041 | 486.00 | 72.00 | 225.87 | 186.20 | NÃO | fora da faixa vertical |
| 1042 | 485.00 | 71.00 | 227.26 | 187.20 | NÃO | fora da faixa vertical |
| 1043 | 484.00 | 71.00 | 227.85 | 187.20 | NÃO | fora da faixa vertical |
| 1044 | 483.00 | 70.00 | 229.24 | 188.20 | NÃO | fora da faixa vertical |
| 1045 | 482.00 | 69.00 | 230.64 | 189.20 | NÃO | fora da faixa vertical |
| 1046 | 481.00 | 69.00 | 231.22 | 189.20 | NÃO | fora da faixa vertical |
| 1047 | 480.00 | 68.00 | 232.62 | 190.20 | NÃO | fora da faixa vertical |
| 1048 | 479.00 | 68.00 | 233.21 | 190.20 | NÃO | fora da faixa vertical |
| 1049 | 478.00 | 67.00 | 234.61 | 191.20 | NÃO | fora da faixa vertical |
| 1050 | 477.00 | 67.00 | 235.20 | 191.20 | NÃO | fora da faixa vertical |
| 1051 | 476.00 | 66.00 | 236.60 | 192.20 | NÃO | fora da faixa vertical |
| 1052 | 475.00 | 66.00 | 237.20 | 192.20 | NÃO | fora da faixa vertical |
| 1053 | 474.00 | 65.00 | 238.60 | 193.20 | NÃO | fora da faixa vertical |
| 1054 | 473.00 | 65.00 | 239.20 | 193.20 | NÃO | fora da faixa vertical |
| 1055 | 472.00 | 64.00 | 240.60 | 194.20 | NÃO | fora da faixa vertical |
| 1056 | 471.00 | 64.00 | 241.21 | 194.20 | NÃO | fora da faixa vertical |
| 1057 | 470.00 | 63.00 | 242.61 | 195.20 | NÃO | fora da faixa vertical |
| 1058 | 469.00 | 63.00 | 243.21 | 195.20 | NÃO | fora da faixa vertical |
| 1059 | 468.00 | 62.00 | 244.62 | 196.20 | NÃO | fora da faixa vertical |
| 1060 | 467.00 | 62.00 | 245.23 | 196.20 | NÃO | fora da faixa vertical |
| 1061 | 466.00 | 61.00 | 246.63 | 197.20 | NÃO | fora da faixa vertical |
| 1062 | 465.00 | 61.00 | 247.24 | 197.20 | NÃO | fora da faixa vertical |
| 1063 | 464.00 | 60.00 | 248.65 | 198.20 | NÃO | fora da faixa vertical |
| 1064 | 463.00 | 60.00 | 249.26 | 198.20 | NÃO | fora da faixa vertical |
| 1065 | 462.00 | 59.00 | 250.67 | 199.20 | NÃO | fora da faixa vertical |
| 1066 | 461.00 | 59.00 | 251.29 | 199.20 | NÃO | fora da faixa vertical |
| 1067 | 460.00 | 58.00 | 252.69 | 200.20 | NÃO | fora da faixa vertical |
| 1068 | 459.00 | 58.00 | 253.31 | 200.20 | NÃO | fora da faixa vertical |
| 1069 | 458.00 | 57.00 | 254.72 | 201.20 | NÃO | fora da faixa vertical |
| 1070 | 457.00 | 57.00 | 255.34 | 201.20 | NÃO | fora da faixa vertical |
| 1071 | 456.00 | 57.00 | 255.97 | 201.20 | NÃO | fora da faixa vertical |
| 1072 | 455.00 | 56.00 | 257.38 | 202.20 | NÃO | fora da faixa vertical |
| 1073 | 454.00 | 56.00 | 258.01 | 202.20 | NÃO | fora da faixa vertical |
| 1074 | 453.00 | 55.00 | 259.42 | 203.20 | NÃO | fora da faixa vertical |
| 1075 | 452.00 | 55.00 | 260.05 | 203.20 | NÃO | fora da faixa vertical |
| 1076 | 451.00 | 55.00 | 260.69 | 203.20 | NÃO | fora da faixa vertical |
| 1077 | 450.00 | 54.00 | 262.09 | 204.20 | NÃO | fora da faixa vertical |
| 1078 | 449.00 | 54.00 | 262.73 | 204.20 | NÃO | fora da faixa vertical |
| 1079 | 448.00 | 54.00 | 263.37 | 204.20 | NÃO | fora da faixa vertical |
| 1080 | 447.00 | 53.00 | 264.78 | 205.20 | NÃO | fora da faixa vertical |
| 1081 | 446.00 | 53.00 | 265.42 | 205.20 | NÃO | fora da faixa vertical |
| 1082 | 445.00 | 52.00 | 266.83 | 206.20 | NÃO | fora da faixa vertical |
| 1083 | 444.00 | 52.00 | 267.48 | 206.20 | NÃO | fora da faixa vertical |
| 1084 | 443.00 | 52.00 | 268.13 | 206.20 | NÃO | fora da faixa vertical |
| 1085 | 442.00 | 51.00 | 269.54 | 207.20 | NÃO | fora da faixa vertical |
| 1086 | 441.00 | 51.00 | 270.19 | 207.20 | NÃO | fora da faixa vertical |
| 1087 | 440.00 | 51.00 | 270.84 | 207.20 | NÃO | fora da faixa vertical |
| 1088 | 439.00 | 50.00 | 272.25 | 208.20 | NÃO | fora da faixa vertical |
| 1089 | 438.00 | 50.00 | 272.90 | 208.20 | NÃO | fora da faixa vertical |
| 1090 | 437.00 | 50.00 | 273.56 | 208.20 | NÃO | fora da faixa vertical |
| 1091 | 436.00 | 49.00 | 274.97 | 209.20 | NÃO | fora da faixa vertical |
| 1092 | 435.00 | 49.00 | 275.63 | 209.20 | NÃO | fora da faixa vertical |
| 1093 | 434.00 | 49.00 | 276.29 | 209.20 | NÃO | fora da faixa vertical |
| 1094 | 433.00 | 48.00 | 277.70 | 210.20 | NÃO | fora da faixa vertical |
| 1095 | 432.00 | 48.00 | 278.37 | 210.20 | NÃO | fora da faixa vertical |
| 1096 | 431.00 | 48.00 | 279.03 | 210.20 | NÃO | fora da faixa vertical |
| 1097 | 430.00 | 47.00 | 280.45 | 211.20 | NÃO | fora da faixa vertical |
| 1098 | 429.00 | 47.00 | 281.11 | 211.20 | NÃO | fora da faixa vertical |
| 1099 | 428.00 | 47.00 | 281.78 | 211.20 | NÃO | fora da faixa vertical |
| 1100 | 427.00 | 47.00 | 282.46 | 211.20 | NÃO | fora da faixa vertical |
| 1101 | 426.00 | 46.00 | 283.87 | 212.20 | NÃO | fora da faixa vertical |
| 1102 | 425.00 | 46.00 | 284.54 | 212.20 | NÃO | fora da faixa vertical |
| 1103 | 424.00 | 46.00 | 285.22 | 212.20 | NÃO | fora da faixa vertical |
| 1104 | 423.00 | 45.00 | 286.63 | 213.20 | NÃO | fora da faixa vertical |
| 1105 | 422.00 | 45.00 | 287.31 | 213.20 | NÃO | fora da faixa vertical |
| 1106 | 421.00 | 45.00 | 287.99 | 213.20 | NÃO | fora da faixa vertical |
| 1107 | 420.00 | 44.00 | 289.40 | 214.20 | NÃO | fora da faixa vertical |
| 1108 | 419.00 | 44.00 | 290.08 | 214.20 | NÃO | fora da faixa vertical |
| 1109 | 418.00 | 44.00 | 290.77 | 214.20 | NÃO | fora da faixa vertical |
| 1110 | 417.00 | 44.00 | 291.45 | 214.20 | NÃO | fora da faixa vertical |
| 1111 | 416.00 | 43.00 | 292.87 | 215.20 | NÃO | fora da faixa vertical |
| 1112 | 415.00 | 43.00 | 293.55 | 215.20 | NÃO | fora da faixa vertical |
| 1113 | 414.00 | 43.00 | 294.24 | 215.20 | NÃO | fora da faixa vertical |
| 1114 | 413.00 | 43.00 | 294.93 | 215.20 | NÃO | fora da faixa vertical |
| 1115 | 412.00 | 42.00 | 296.35 | 216.20 | NÃO | fora da faixa vertical |
| 1116 | 411.00 | 42.00 | 297.04 | 216.20 | NÃO | fora da faixa vertical |
| 1117 | 410.00 | 42.00 | 297.73 | 216.20 | NÃO | fora da faixa vertical |
| 1118 | 409.00 | 42.00 | 298.43 | 216.20 | NÃO | fora da faixa vertical |
| 1119 | 408.00 | 42.00 | 299.13 | 216.20 | NÃO | fora da faixa vertical |
| 1120 | 407.00 | 41.00 | 300.54 | 217.20 | NÃO | fora da faixa vertical |
| 1121 | 406.00 | 41.00 | 301.24 | 217.20 | NÃO | fora da faixa vertical |
| 1122 | 405.00 | 41.00 | 301.94 | 217.20 | NÃO | fora da faixa vertical |
| 1123 | 404.00 | 41.00 | 302.65 | 217.20 | NÃO | fora da faixa vertical |
| 1124 | 403.00 | 41.00 | 303.35 | 217.20 | NÃO | fora da faixa vertical |
| 1125 | 402.00 | 40.00 | 304.76 | 218.20 | NÃO | fora da faixa vertical |
| 1126 | 401.00 | 40.00 | 305.47 | 218.20 | NÃO | fora da faixa vertical |
| 1127 | 400.00 | 40.00 | 306.18 | 218.20 | NÃO | fora da faixa vertical |
| 1128 | 399.00 | 40.00 | 306.89 | 218.20 | NÃO | fora da faixa vertical |
| 1129 | 398.00 | 40.00 | 307.60 | 218.20 | NÃO | fora da faixa vertical |
| 1130 | 397.00 | 39.00 | 309.01 | 219.20 | NÃO | fora da faixa vertical |
| 1131 | 396.00 | 39.00 | 309.73 | 219.20 | NÃO | fora da faixa vertical |
| 1132 | 395.00 | 39.00 | 310.44 | 219.20 | NÃO | fora da faixa vertical |
| 1133 | 394.00 | 39.00 | 311.16 | 219.20 | NÃO | fora da faixa vertical |
| 1134 | 393.00 | 39.00 | 311.87 | 219.20 | NÃO | fora da faixa vertical |
| 1135 | 392.00 | 39.00 | 312.59 | 219.20 | NÃO | fora da faixa vertical |
| 1136 | 391.00 | 39.00 | 313.31 | 219.20 | NÃO | fora da faixa vertical |
| 1137 | 390.00 | 38.00 | 314.73 | 220.20 | NÃO | fora da faixa vertical |
| 1138 | 389.00 | 38.00 | 315.45 | 220.20 | NÃO | fora da faixa vertical |
| 1139 | 388.00 | 38.00 | 316.17 | 220.20 | NÃO | fora da faixa vertical |
| 1140 | 387.00 | 38.00 | 316.90 | 220.20 | NÃO | fora da faixa vertical |
| 1141 | 386.00 | 38.00 | 317.62 | 220.20 | NÃO | fora da faixa vertical |
| 1142 | 385.00 | 38.00 | 318.35 | 220.20 | NÃO | fora da faixa vertical |
| 1143 | 384.00 | 38.00 | 319.08 | 220.20 | NÃO | fora da faixa vertical |
| 1144 | 383.00 | 38.00 | 319.81 | 220.20 | NÃO | fora da faixa vertical |
| 1145 | 382.00 | 38.00 | 320.54 | 220.20 | NÃO | fora da faixa vertical |
| 1146 | 381.00 | 37.00 | 321.96 | 221.20 | NÃO | fora da faixa vertical |
| 1147 | 380.00 | 37.00 | 322.69 | 221.20 | NÃO | fora da faixa vertical |
| 1148 | 379.00 | 37.00 | 323.43 | 221.20 | NÃO | fora da faixa vertical |
| 1149 | 378.00 | 37.00 | 324.16 | 221.20 | NÃO | fora da faixa vertical |
| 1150 | 377.00 | 37.00 | 324.90 | 221.20 | NÃO | fora da faixa vertical |
| 1151 | 376.00 | 37.00 | 325.64 | 221.20 | NÃO | fora da faixa vertical |
| 1152 | 375.00 | 37.00 | 326.38 | 221.20 | NÃO | fora da faixa vertical |
| 1153 | 374.00 | 37.00 | 327.12 | 221.20 | NÃO | fora da faixa vertical |
| 1154 | 373.00 | 37.00 | 327.87 | 221.20 | NÃO | fora da faixa vertical |
| 1155 | 372.00 | 36.00 | 329.28 | 222.20 | NÃO | fora da faixa vertical |
| 1156 | 371.00 | 36.00 | 330.02 | 222.20 | NÃO | fora da faixa vertical |
| 1157 | 370.00 | 36.00 | 330.77 | 222.20 | NÃO | fora da faixa vertical |
| 1158 | 369.00 | 36.00 | 331.52 | 222.20 | NÃO | fora da faixa vertical |
| 1159 | 368.00 | 36.00 | 332.27 | 222.20 | NÃO | fora da faixa vertical |
| 1160 | 367.00 | 36.00 | 333.02 | 222.20 | NÃO | fora da faixa vertical |
| 1161 | 366.00 | 36.00 | 333.77 | 222.20 | NÃO | fora da faixa vertical |
| 1162 | 365.00 | 36.00 | 334.52 | 222.20 | NÃO | fora da faixa vertical |
| 1163 | 364.00 | 36.00 | 335.27 | 222.20 | NÃO | fora da faixa vertical |
| 1164 | 363.00 | 36.00 | 336.03 | 222.20 | NÃO | fora da faixa vertical |
| 1165 | 362.00 | 36.00 | 336.79 | 222.20 | NÃO | fora da faixa vertical |
| 1166 | 361.00 | 36.00 | 337.54 | 222.20 | NÃO | fora da faixa vertical |
| 1167 | 360.00 | 36.00 | 338.30 | 222.20 | NÃO | fora da faixa vertical |
| 1168 | 359.00 | 36.00 | 339.06 | 222.20 | NÃO | fora da faixa vertical |
| 1169 | 358.00 | 36.00 | 339.82 | 222.20 | NÃO | fora da faixa vertical |
| 1170 | 357.00 | 36.00 | 340.59 | 222.20 | NÃO | fora da faixa vertical |
| 1171 | 356.00 | 36.00 | 341.35 | 222.20 | NÃO | fora da faixa vertical |
| 1172 | 355.00 | 36.00 | 342.12 | 222.20 | NÃO | fora da faixa vertical |
| 1173 | 354.00 | 36.00 | 342.88 | 222.20 | NÃO | fora da faixa vertical |
| 1174 | 353.00 | 36.00 | 343.65 | 222.20 | NÃO | fora da faixa vertical |
| 1175 | 352.00 | 36.00 | 344.42 | 222.20 | NÃO | fora da faixa vertical |
| 1176 | 351.00 | 36.00 | 345.19 | 222.20 | NÃO | fora da faixa vertical |
| 1177 | 350.00 | 36.00 | 345.96 | 222.20 | NÃO | fora da faixa vertical |
| 1178 | 349.00 | 36.00 | 346.73 | 222.20 | NÃO | fora da faixa vertical |
| 1179 | 348.00 | 36.00 | 347.51 | 222.20 | NÃO | fora da faixa vertical |
| 1180 | 347.00 | 36.00 | 348.28 | 222.20 | NÃO | fora da faixa vertical |
| 1181 | 346.00 | 36.00 | 349.06 | 222.20 | NÃO | fora da faixa vertical |
| 1182 | 345.00 | 36.00 | 349.83 | 222.20 | NÃO | fora da faixa vertical |
| 1183 | 344.00 | 36.00 | 350.61 | 222.20 | NÃO | fora da faixa vertical |
| 1184 | 343.00 | 36.00 | 351.39 | 222.20 | NÃO | fora da faixa vertical |
| 1185 | 342.00 | 36.00 | 352.17 | 222.20 | NÃO | fora da faixa vertical |
| 1186 | 341.00 | 36.00 | 352.95 | 222.20 | NÃO | fora da faixa vertical |
| 1187 | 340.00 | 36.00 | 353.74 | 222.20 | NÃO | fora da faixa vertical |
| 1188 | 339.00 | 36.00 | 354.52 | 222.20 | NÃO | fora da faixa vertical |
| 1189 | 338.00 | 36.00 | 355.30 | 222.20 | NÃO | fora da faixa vertical |
| 1190 | 337.00 | 36.00 | 356.09 | 222.20 | NÃO | fora da faixa vertical |
| 1191 | 336.00 | 36.00 | 356.88 | 222.20 | NÃO | fora da faixa vertical |
| 1192 | 335.00 | 36.00 | 357.66 | 222.20 | NÃO | fora da faixa vertical |
| 1193 | 334.00 | 36.00 | 358.45 | 222.20 | NÃO | fora da faixa vertical |
| 1194 | 333.00 | 36.00 | 359.24 | 222.20 | NÃO | fora da faixa vertical |
| 1195 | 332.00 | 36.00 | 360.03 | 222.20 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 578 | 352.00 | 256.00 | -265.00 | -2.20 |
| 579 | 353.00 | 256.00 | -264.00 | -2.20 |
| 580 | 354.00 | 256.00 | -263.00 | -2.20 |
| 581 | 355.00 | 256.00 | -262.00 | -2.20 |
| 582 | 356.00 | 256.00 | -261.00 | -2.20 |
| 583 | 357.00 | 256.00 | -260.00 | -2.20 |
| 584 | 358.00 | 256.00 | -259.00 | -2.20 |
| 585 | 359.00 | 256.00 | -258.00 | -2.20 |
| 586 | 360.00 | 256.00 | -257.00 | -2.20 |
| 587 | 361.00 | 256.00 | -256.00 | -2.20 |
| 588 | 362.00 | 256.00 | -255.00 | -2.20 |
| 589 | 363.00 | 256.00 | -254.00 | -2.20 |
| 590 | 364.00 | 256.00 | -253.00 | -2.20 |
| 591 | 365.00 | 256.00 | -252.00 | -2.20 |
| 592 | 366.00 | 256.00 | -251.00 | -2.20 |
| 593 | 367.00 | 256.00 | -250.00 | -2.20 |
| 594 | 368.00 | 256.00 | -249.00 | -2.20 |
| 595 | 369.00 | 256.00 | -248.00 | -2.20 |
| 596 | 370.00 | 256.00 | -247.00 | -2.20 |
| 597 | 371.00 | 256.00 | -246.00 | -2.20 |
| 598 | 372.00 | 256.00 | -245.00 | -2.20 |
| 599 | 373.00 | 256.00 | -244.00 | -2.20 |
| 600 | 374.00 | 256.00 | -243.00 | -2.20 |
| 601 | 375.00 | 256.00 | -242.00 | -2.20 |
| 602 | 376.00 | 256.00 | -241.00 | -2.20 |
| 603 | 377.00 | 256.00 | -240.00 | -2.20 |
| 604 | 378.00 | 256.00 | -239.00 | -2.20 |
| 605 | 379.00 | 256.00 | -238.00 | -2.20 |
| 606 | 380.00 | 256.00 | -237.00 | -2.20 |
| 607 | 381.00 | 256.00 | -236.00 | -2.20 |
| 608 | 382.00 | 256.00 | -235.00 | -2.20 |
| 609 | 383.00 | 256.00 | -234.00 | -2.20 |
| 610 | 384.00 | 256.00 | -233.00 | -2.20 |
| 611 | 385.00 | 256.00 | -232.00 | -2.20 |
| 612 | 386.00 | 256.00 | -231.00 | -2.20 |
| 613 | 387.00 | 256.00 | -230.00 | -2.20 |
| 614 | 388.00 | 256.00 | -229.00 | -2.20 |
| 615 | 389.00 | 256.00 | -228.00 | -2.20 |
| 616 | 390.00 | 256.00 | -227.00 | -2.20 |
| 617 | 391.00 | 256.00 | -226.00 | -2.20 |
| 618 | 392.00 | 256.00 | -225.00 | -2.20 |
| 619 | 393.00 | 256.00 | -224.00 | -2.20 |
| 620 | 394.00 | 256.00 | -223.00 | -2.20 |
| 621 | 395.00 | 256.00 | -222.00 | -2.20 |
| 622 | 396.00 | 256.00 | -221.00 | -2.20 |
| 623 | 397.00 | 256.00 | -220.00 | -2.20 |
| 624 | 398.00 | 256.00 | -219.00 | -2.20 |
| 625 | 399.00 | 256.00 | -218.00 | -2.20 |
| 626 | 400.00 | 256.00 | -217.00 | -2.20 |
| 627 | 401.00 | 256.00 | -216.00 | -2.20 |
| 628 | 402.00 | 256.00 | -215.00 | -2.20 |
| 629 | 403.00 | 256.00 | -214.00 | -2.20 |
| 630 | 404.00 | 256.00 | -213.00 | -2.20 |
| 631 | 405.00 | 256.00 | -212.00 | -2.20 |
| 632 | 406.00 | 256.00 | -211.00 | -2.20 |
| 633 | 407.00 | 256.00 | -210.00 | -2.20 |
| 634 | 408.00 | 256.00 | -209.00 | -2.20 |
| 635 | 409.00 | 256.00 | -208.00 | -2.20 |
| 636 | 410.00 | 256.00 | -207.00 | -2.20 |
| 637 | 411.00 | 256.00 | -206.00 | -2.20 |
| 638 | 412.00 | 256.00 | -205.00 | -2.20 |
| 639 | 413.00 | 256.00 | -204.00 | -2.20 |
| 640 | 414.00 | 256.00 | -203.00 | -2.20 |
| 641 | 415.00 | 256.00 | -202.00 | -2.20 |
| 642 | 416.00 | 256.00 | -201.00 | -2.20 |
| 643 | 417.00 | 256.00 | -200.00 | -2.20 |
| 644 | 418.00 | 256.00 | -199.00 | -2.20 |
| 645 | 419.00 | 256.00 | -198.00 | -2.20 |
| 646 | 420.00 | 256.00 | -197.00 | -2.20 |
| 647 | 421.00 | 256.00 | -196.00 | -2.20 |
| 648 | 422.00 | 256.00 | -195.00 | -2.20 |
| 649 | 423.00 | 256.00 | -194.00 | -2.20 |
| 650 | 424.00 | 256.00 | -193.00 | -2.20 |
| 651 | 425.00 | 256.00 | -192.00 | -2.20 |
| 652 | 426.00 | 256.00 | -191.00 | -2.20 |
| 653 | 427.00 | 256.00 | -190.00 | -2.20 |
| 654 | 428.00 | 256.00 | -189.00 | -2.20 |
| 655 | 429.00 | 256.00 | -188.00 | -2.20 |
| 656 | 430.00 | 256.00 | -187.00 | -2.20 |
| 657 | 431.00 | 256.00 | -186.00 | -2.20 |
| 658 | 432.00 | 256.00 | -185.00 | -2.20 |
| 659 | 433.00 | 256.00 | -184.00 | -2.20 |
| 660 | 434.00 | 256.00 | -183.00 | -2.20 |
| 661 | 435.00 | 256.00 | -182.00 | -2.20 |
| 662 | 436.00 | 256.00 | -181.00 | -2.20 |
| 663 | 437.00 | 256.00 | -180.00 | -2.20 |
| 664 | 438.00 | 256.00 | -179.00 | -2.20 |
| 665 | 439.00 | 256.00 | -178.00 | -2.20 |
| 666 | 440.00 | 256.00 | -177.00 | -2.20 |
| 667 | 441.00 | 256.00 | -176.00 | -2.20 |
| 668 | 442.00 | 256.00 | -175.00 | -2.20 |
| 669 | 443.00 | 256.00 | -174.00 | -2.20 |
| 670 | 444.00 | 256.00 | -173.00 | -2.20 |
| 671 | 445.00 | 256.00 | -172.00 | -2.20 |
| 672 | 446.00 | 256.00 | -171.00 | -2.20 |
| 673 | 447.00 | 256.00 | -170.00 | -2.20 |
| 674 | 448.00 | 256.00 | -169.00 | -2.20 |
| 675 | 449.00 | 256.00 | -168.00 | -2.20 |
| 676 | 450.00 | 256.00 | -167.00 | -2.20 |
| 677 | 451.00 | 256.00 | -166.00 | -2.20 |
| 678 | 452.00 | 256.00 | -165.00 | -2.20 |
| 679 | 453.00 | 256.00 | -164.00 | -2.20 |
| 680 | 454.00 | 256.00 | -163.00 | -2.20 |
| 681 | 455.00 | 256.00 | -162.00 | -2.20 |
| 682 | 456.00 | 256.00 | -161.00 | -2.20 |
| 683 | 457.00 | 256.00 | -160.00 | -2.20 |
| 684 | 458.00 | 256.00 | -159.00 | -2.20 |
| 685 | 459.00 | 256.00 | -158.00 | -2.20 |
| 686 | 460.00 | 256.00 | -157.00 | -2.20 |
| 687 | 461.00 | 256.00 | -156.00 | -2.20 |
| 688 | 462.00 | 256.00 | -155.00 | -2.20 |
| 689 | 463.00 | 256.00 | -154.00 | -2.20 |
| 690 | 464.00 | 256.00 | -153.00 | -2.20 |
| 691 | 465.00 | 256.00 | -152.00 | -2.20 |
| 692 | 466.00 | 256.00 | -151.00 | -2.20 |
| 693 | 467.00 | 256.00 | -150.00 | -2.20 |
| 694 | 468.00 | 256.00 | -149.00 | -2.20 |
| 695 | 469.00 | 256.00 | -148.00 | -2.20 |
| 696 | 470.00 | 256.00 | -147.00 | -2.20 |
| 697 | 471.00 | 256.00 | -146.00 | -2.20 |
| 698 | 472.00 | 256.00 | -145.00 | -2.20 |
| 699 | 473.00 | 256.00 | -144.00 | -2.20 |
| 700 | 474.00 | 256.00 | -143.00 | -2.20 |
| 701 | 475.00 | 256.00 | -142.00 | -2.20 |
| 702 | 476.00 | 256.00 | -141.00 | -2.20 |
| 703 | 477.00 | 256.00 | -140.00 | -2.20 |
| 704 | 478.00 | 256.00 | -139.00 | -2.20 |
| 705 | 479.00 | 256.00 | -138.00 | -2.20 |
| 706 | 480.00 | 256.00 | -137.00 | -2.20 |
| 707 | 481.00 | 256.00 | -136.00 | -2.20 |
| 708 | 482.00 | 256.00 | -135.00 | -2.20 |
| 709 | 483.00 | 256.00 | -134.00 | -2.20 |
| 710 | 484.00 | 256.00 | -133.00 | -2.20 |
| 711 | 485.00 | 256.00 | -132.00 | -2.20 |
| 712 | 486.00 | 256.00 | -131.00 | -2.20 |
| 713 | 487.00 | 256.00 | -130.00 | -2.20 |
| 714 | 488.00 | 256.00 | -129.00 | -2.20 |
| 715 | 489.00 | 256.00 | -128.00 | -2.20 |
| 716 | 490.00 | 256.00 | -127.00 | -2.20 |
| 717 | 491.00 | 256.00 | -126.00 | -2.20 |
| 718 | 492.00 | 256.00 | -125.00 | -2.20 |
| 719 | 493.00 | 256.00 | -124.00 | -2.20 |
| 720 | 494.00 | 256.00 | -123.00 | -2.20 |
| 721 | 495.00 | 256.00 | -122.00 | -2.20 |
| 722 | 496.00 | 256.00 | -121.00 | -2.20 |
| 723 | 497.00 | 256.00 | -120.00 | -2.20 |
| 724 | 498.00 | 256.00 | -119.00 | -2.20 |
| 725 | 499.00 | 256.00 | -118.00 | -2.20 |
| 726 | 500.00 | 256.00 | -117.00 | -2.20 |
| 727 | 501.00 | 256.00 | -116.00 | -2.20 |
| 728 | 502.00 | 256.00 | -115.00 | -2.20 |
| 729 | 503.00 | 256.00 | -114.00 | -2.20 |
| 730 | 504.00 | 256.00 | -113.00 | -2.20 |
| 731 | 505.00 | 256.00 | -112.00 | -2.20 |
| 732 | 506.00 | 256.00 | -111.00 | -2.20 |
| 733 | 507.00 | 256.00 | -110.00 | -2.20 |
| 734 | 508.00 | 256.00 | -109.00 | -2.20 |
| 735 | 509.00 | 256.00 | -108.00 | -2.20 |
| 736 | 510.00 | 256.00 | -107.00 | -2.20 |
| 737 | 511.00 | 256.00 | -106.00 | -2.20 |
| 738 | 512.00 | 256.00 | -105.00 | -2.20 |
| 739 | 513.00 | 256.00 | -104.00 | -2.20 |
| 740 | 514.00 | 256.00 | -103.00 | -2.20 |
| 741 | 515.00 | 256.00 | -102.00 | -2.20 |
| 742 | 516.00 | 256.00 | -101.00 | -2.20 |
| 743 | 517.00 | 256.00 | -100.00 | -2.20 |
| 744 | 518.00 | 256.00 | -99.00 | -2.20 |
| 745 | 519.00 | 256.00 | -98.00 | -2.20 |
| 746 | 520.00 | 256.00 | -97.00 | -2.20 |
| 747 | 521.00 | 256.00 | -96.00 | -2.20 |
| 748 | 522.00 | 256.00 | -95.00 | -2.20 |
| 749 | 523.00 | 256.00 | -94.00 | -2.20 |
| 750 | 524.00 | 256.00 | -93.00 | -2.20 |
| 751 | 525.00 | 256.00 | -92.00 | -2.20 |
| 752 | 526.00 | 256.00 | -91.00 | -2.20 |
| 753 | 527.00 | 256.00 | -90.00 | -2.20 |
| 754 | 528.00 | 256.00 | -89.00 | -2.20 |
| 755 | 529.00 | 256.00 | -88.00 | -2.20 |
| 756 | 530.00 | 256.00 | -87.00 | -2.20 |
| 757 | 531.00 | 256.00 | -86.00 | -2.20 |
| 758 | 532.00 | 256.00 | -85.00 | -2.20 |
| 759 | 533.00 | 256.00 | -84.00 | -2.20 |
| 760 | 534.00 | 256.00 | -83.00 | -2.20 |
| 761 | 535.00 | 256.00 | -82.00 | -2.20 |
| 762 | 536.00 | 256.00 | -81.00 | -2.20 |
| 763 | 537.00 | 256.00 | -80.00 | -2.20 |
| 764 | 538.00 | 256.00 | -79.00 | -2.20 |
| 765 | 539.00 | 256.00 | -78.00 | -2.20 |
| 766 | 540.00 | 256.00 | -77.00 | -2.20 |
| 767 | 541.00 | 256.00 | -76.00 | -2.20 |
| 768 | 542.00 | 256.00 | -75.00 | -2.20 |
| 769 | 543.00 | 256.00 | -74.00 | -2.20 |
| 770 | 544.00 | 256.00 | -73.00 | -2.20 |
| 771 | 545.00 | 256.00 | -72.00 | -2.20 |
| 772 | 546.00 | 256.00 | -71.00 | -2.20 |
| 773 | 547.00 | 256.00 | -70.00 | -2.20 |
| 774 | 548.00 | 256.00 | -69.00 | -2.20 |
| 775 | 549.00 | 256.00 | -68.00 | -2.20 |
| 776 | 550.00 | 256.00 | -67.00 | -2.20 |
| 777 | 551.00 | 256.00 | -66.00 | -2.20 |
| 778 | 552.00 | 256.00 | -65.00 | -2.20 |
| 779 | 553.00 | 256.00 | -64.00 | -2.20 |
| 780 | 554.00 | 256.00 | -63.00 | -2.20 |
| 781 | 555.00 | 256.00 | -62.00 | -2.20 |
| 782 | 556.00 | 256.00 | -61.00 | -2.20 |
| 783 | 557.00 | 256.00 | -60.00 | -2.20 |
| 784 | 558.00 | 256.00 | -59.00 | -2.20 |
| 785 | 559.00 | 256.00 | -58.00 | -2.20 |
| 786 | 560.00 | 256.00 | -57.00 | -2.20 |
| 787 | 561.00 | 256.00 | -56.00 | -2.20 |
| 788 | 562.00 | 256.00 | -55.00 | -2.20 |
| 789 | 563.00 | 256.00 | -54.00 | -2.20 |
| 790 | 564.00 | 256.00 | -53.00 | -2.20 |
| 791 | 565.00 | 256.00 | -52.00 | -2.20 |
| 792 | 566.00 | 256.00 | -51.00 | -2.20 |
| 793 | 567.00 | 256.00 | -50.00 | -2.20 |
| 794 | 568.00 | 256.00 | -49.00 | -2.20 |
| 795 | 569.00 | 256.00 | -48.00 | -2.20 |
| 796 | 570.00 | 256.00 | -47.00 | -2.20 |
| 797 | 571.00 | 256.00 | -46.00 | -2.20 |
| 798 | 572.00 | 256.00 | -45.00 | -2.20 |
| 799 | 573.00 | 256.00 | -44.00 | -2.20 |
| 800 | 574.00 | 256.00 | -43.00 | -2.20 |
| 801 | 575.00 | 256.00 | -42.00 | -2.20 |
| 802 | 576.00 | 256.00 | -41.00 | -2.20 |
| 803 | 577.00 | 256.00 | -40.00 | -2.20 |
| 804 | 578.00 | 256.00 | -39.00 | -2.20 |
| 805 | 579.00 | 256.00 | -38.00 | -2.20 |
| 806 | 580.00 | 256.00 | -37.00 | -2.20 |
| 807 | 581.00 | 256.00 | -36.00 | -2.20 |
| 808 | 582.00 | 256.00 | -35.00 | -2.20 |
| 809 | 583.00 | 256.00 | -34.00 | -2.20 |
| 810 | 584.00 | 256.00 | -33.00 | -2.20 |
| 811 | 585.00 | 256.00 | -32.00 | -2.20 |
| 812 | 586.00 | 256.00 | -31.00 | -2.20 |
| 813 | 587.00 | 256.00 | -30.00 | -2.20 |
| 814 | 588.00 | 256.00 | -29.00 | -2.20 |
| 815 | 589.00 | 256.00 | -28.00 | -2.20 |
| 816 | 590.00 | 256.00 | -27.00 | -2.20 |
| 817 | 591.00 | 256.00 | -26.00 | -2.20 |
| 818 | 592.00 | 256.00 | -25.00 | -2.20 |
| 819 | 593.00 | 256.00 | -24.00 | -2.20 |
| 820 | 594.00 | 256.00 | -23.00 | -2.20 |
| 821 | 595.00 | 256.00 | -22.00 | -2.20 |
| 822 | 596.00 | 256.00 | -21.00 | -2.20 |
| 823 | 597.00 | 256.00 | -20.00 | -2.20 |
| 824 | 598.00 | 256.00 | -19.00 | -2.20 |
| 825 | 599.00 | 256.00 | -18.00 | -2.20 |
| 826 | 600.00 | 256.00 | -17.00 | -2.20 |
| 827 | 601.00 | 256.00 | -16.00 | -2.20 |
| 828 | 602.00 | 256.00 | -15.00 | -2.20 |
| 829 | 603.00 | 256.00 | -14.00 | -2.20 |
| 830 | 604.00 | 256.00 | -13.00 | -2.20 |
| 831 | 605.00 | 256.00 | -12.00 | -2.20 |
| 832 | 606.00 | 256.00 | -11.00 | -2.20 |
| 833 | 607.00 | 256.00 | -10.00 | -2.20 |
| 834 | 608.00 | 256.00 | -9.00 | -2.20 |
| 835 | 609.00 | 256.00 | -8.00 | -2.20 |
| 836 | 610.00 | 256.00 | -7.00 | -2.20 |
| 837 | 611.00 | 256.00 | -6.00 | -2.20 |
| 838 | 612.00 | 256.00 | -5.00 | -2.20 |
| 839 | 613.00 | 256.00 | -4.00 | -2.20 |
| 840 | 614.00 | 256.00 | -3.00 | -2.20 |
| 841 | 615.00 | 256.00 | -2.00 | -2.20 |
| 842 | 616.00 | 256.00 | -1.00 | -2.20 |
| 843 | 617.00 | 256.00 | 0.00 | -2.20 |
| 844 | 616.00 | 255.00 | -1.00 | -3.20 |
| 845 | 616.00 | 254.00 | -1.00 | -4.20 |
| 846 | 616.00 | 253.00 | -1.00 | -5.20 |
| 847 | 616.00 | 252.00 | -1.00 | -6.20 |
| 848 | 616.00 | 251.00 | -1.00 | -7.20 |
| 849 | 615.00 | 250.00 | -2.00 | -8.20 |
| 850 | 615.00 | 249.00 | -2.00 | -9.20 |
| 851 | 615.00 | 248.00 | -2.00 | -10.20 |
| 852 | 615.00 | 247.00 | -2.00 | -11.20 |
| 853 | 615.00 | 246.00 | -2.00 | -12.20 |
| 854 | 614.00 | 245.00 | -3.00 | -13.20 |
| 855 | 614.00 | 244.00 | -3.00 | -14.20 |
| 856 | 614.00 | 243.00 | -3.00 | -15.20 |
| 857 | 614.00 | 242.00 | -3.00 | -16.20 |
| 858 | 613.00 | 241.00 | -4.00 | -17.20 |
| 859 | 613.00 | 240.00 | -4.00 | -18.20 |
| 860 | 613.00 | 239.00 | -4.00 | -19.20 |
| 861 | 613.00 | 238.00 | -4.00 | -20.20 |
| 862 | 612.00 | 237.00 | -5.00 | -21.20 |
| 863 | 612.00 | 236.00 | -5.00 | -22.20 |
| 864 | 612.00 | 235.00 | -5.00 | -23.20 |
| 865 | 612.00 | 234.00 | -5.00 | -24.20 |
| 866 | 611.00 | 233.00 | -6.00 | -25.20 |
| 867 | 611.00 | 232.00 | -6.00 | -26.20 |
| 868 | 611.00 | 231.00 | -6.00 | -27.20 |
| 869 | 610.00 | 230.00 | -7.00 | -28.20 |
| 870 | 610.00 | 229.00 | -7.00 | -29.20 |
| 871 | 610.00 | 228.00 | -7.00 | -30.20 |
| 872 | 609.00 | 227.00 | -8.00 | -31.20 |
| 873 | 609.00 | 226.00 | -8.00 | -32.20 |
| 874 | 609.00 | 225.00 | -8.00 | -33.20 |
| 875 | 609.00 | 224.00 | -8.00 | -34.20 |
| 876 | 608.00 | 223.00 | -9.00 | -35.20 |
| 877 | 608.00 | 222.00 | -9.00 | -36.20 |
| 878 | 608.00 | 221.00 | -9.00 | -37.20 |
| 879 | 607.00 | 220.00 | -10.00 | -38.20 |
| 880 | 607.00 | 219.00 | -10.00 | -39.20 |
| 881 | 607.00 | 218.00 | -10.00 | -40.20 |
| 882 | 606.00 | 217.00 | -11.00 | -41.20 |
| 883 | 606.00 | 216.00 | -11.00 | -42.20 |
| 884 | 606.00 | 215.00 | -11.00 | -43.20 |
| 885 | 605.00 | 214.00 | -12.00 | -44.20 |
| 886 | 605.00 | 213.00 | -12.00 | -45.20 |
| 887 | 604.00 | 212.00 | -13.00 | -46.20 |
| 888 | 604.00 | 211.00 | -13.00 | -47.20 |
| 889 | 604.00 | 210.00 | -13.00 | -48.20 |
| 890 | 603.00 | 209.00 | -14.00 | -49.20 |
| 891 | 603.00 | 208.00 | -14.00 | -50.20 |
| 892 | 602.00 | 207.00 | -15.00 | -51.20 |
| 893 | 602.00 | 206.00 | -15.00 | -52.20 |
| 894 | 602.00 | 205.00 | -15.00 | -53.20 |
| 895 | 601.00 | 204.00 | -16.00 | -54.20 |
| 896 | 601.00 | 203.00 | -16.00 | -55.20 |
| 897 | 601.00 | 202.00 | -16.00 | -56.20 |
| 898 | 600.00 | 201.00 | -17.00 | -57.20 |
| 899 | 600.00 | 200.00 | -17.00 | -58.20 |
| 900 | 599.00 | 199.00 | -18.00 | -59.20 |
| 901 | 599.00 | 198.00 | -18.00 | -60.20 |
| 902 | 598.00 | 197.00 | -19.00 | -61.20 |
| 903 | 598.00 | 196.00 | -19.00 | -62.20 |
| 904 | 597.00 | 195.00 | -20.00 | -63.20 |
| 905 | 597.00 | 194.00 | -20.00 | -64.20 |
| 906 | 597.00 | 193.00 | -20.00 | -65.20 |
| 907 | 596.00 | 192.00 | -21.00 | -66.20 |
| 908 | 596.00 | 191.00 | -21.00 | -67.20 |
| 909 | 595.00 | 190.00 | -22.00 | -68.20 |
| 910 | 595.00 | 189.00 | -22.00 | -69.20 |
| 911 | 594.00 | 188.00 | -23.00 | -70.20 |
| 912 | 594.00 | 187.00 | -23.00 | -71.20 |
| 913 | 593.00 | 186.00 | -24.00 | -72.20 |
| 914 | 593.00 | 185.00 | -24.00 | -73.20 |
| 915 | 592.00 | 184.00 | -25.00 | -74.20 |
| 916 | 592.00 | 183.00 | -25.00 | -75.20 |
| 917 | 591.00 | 182.00 | -26.00 | -76.20 |
| 918 | 591.00 | 181.00 | -26.00 | -77.20 |
| 919 | 590.00 | 180.00 | -27.00 | -78.20 |
| 920 | 590.00 | 179.00 | -27.00 | -79.20 |
| 921 | 589.00 | 178.00 | -28.00 | -80.20 |
| 922 | 589.00 | 177.00 | -28.00 | -81.20 |
| 923 | 588.00 | 176.00 | -29.00 | -82.20 |
| 924 | 588.00 | 175.00 | -29.00 | -83.20 |
| 925 | 587.00 | 174.00 | -30.00 | -84.20 |
| 926 | 586.00 | 173.00 | -31.00 | -85.20 |
| 927 | 586.00 | 172.00 | -31.00 | -86.20 |
| 928 | 585.00 | 171.00 | -32.00 | -87.20 |
| 929 | 585.00 | 170.00 | -32.00 | -88.20 |
| 930 | 584.00 | 169.00 | -33.00 | -89.20 |
| 931 | 584.00 | 168.00 | -33.00 | -90.20 |
| 932 | 583.00 | 167.00 | -34.00 | -91.20 |
| 933 | 582.00 | 166.00 | -35.00 | -92.20 |
| 934 | 582.00 | 165.00 | -35.00 | -93.20 |
| 935 | 581.00 | 164.00 | -36.00 | -94.20 |
| 936 | 581.00 | 163.00 | -36.00 | -95.20 |
| 937 | 580.00 | 162.00 | -37.00 | -96.20 |
| 938 | 579.00 | 161.00 | -38.00 | -97.20 |
| 939 | 579.00 | 160.00 | -38.00 | -98.20 |
| 940 | 578.00 | 159.00 | -39.00 | -99.20 |
| 941 | 577.00 | 158.00 | -40.00 | -100.20 |
| 942 | 577.00 | 157.00 | -40.00 | -101.20 |
| 943 | 576.00 | 156.00 | -41.00 | -102.20 |
| 944 | 575.00 | 155.00 | -42.00 | -103.20 |
| 945 | 575.00 | 154.00 | -42.00 | -104.20 |
| 946 | 574.00 | 153.00 | -43.00 | -105.20 |
| 947 | 573.00 | 152.00 | -44.00 | -106.20 |
| 948 | 573.00 | 151.00 | -44.00 | -107.20 |
| 949 | 572.00 | 150.00 | -45.00 | -108.20 |
| 950 | 571.00 | 149.00 | -46.00 | -109.20 |
| 951 | 571.00 | 148.00 | -46.00 | -110.20 |
| 952 | 570.00 | 147.00 | -47.00 | -111.20 |
| 953 | 569.00 | 146.00 | -48.00 | -112.20 |
| 954 | 568.00 | 145.00 | -49.00 | -113.20 |
| 955 | 568.00 | 144.00 | -49.00 | -114.20 |
| 956 | 567.00 | 143.00 | -50.00 | -115.20 |
| 957 | 566.00 | 142.00 | -51.00 | -116.20 |
| 958 | 565.00 | 141.00 | -52.00 | -117.20 |
| 959 | 565.00 | 140.00 | -52.00 | -118.20 |
| 960 | 564.00 | 139.00 | -53.00 | -119.20 |
| 961 | 563.00 | 138.00 | -54.00 | -120.20 |

- primeiro índice: 578
- último índice: 961
- quantidade: 384
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![100_geo dir](audit_outputs/75_geo_dir_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![100_geo dir polyfit](audit_outputs/75_geo_dir_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

## Imagem: 130_geo

### Lado: esq

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 733
- ponto de contato recebido: [7.0, 213.0]
- baseline_y: 213.0
- baseline_ajustada: 214.56
- lado solicitado: esq
- largura da região: 85 px
- altura da gota: 156.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 254.00 | 57.00 | 292.14 | 157.56 | NÃO | fora da faixa vertical |
| 1 | 253.00 | 58.00 | 290.76 | 156.56 | NÃO | fora da faixa vertical |
| 2 | 252.00 | 58.00 | 289.91 | 156.56 | NÃO | fora da faixa vertical |
| 3 | 251.00 | 58.00 | 289.07 | 156.56 | NÃO | fora da faixa vertical |
| 4 | 250.00 | 58.00 | 288.23 | 156.56 | NÃO | fora da faixa vertical |
| 5 | 249.00 | 58.00 | 287.38 | 156.56 | NÃO | fora da faixa vertical |
| 6 | 248.00 | 58.00 | 286.54 | 156.56 | NÃO | fora da faixa vertical |
| 7 | 247.00 | 58.00 | 285.70 | 156.56 | NÃO | fora da faixa vertical |
| 8 | 246.00 | 58.00 | 284.86 | 156.56 | NÃO | fora da faixa vertical |
| 9 | 245.00 | 58.00 | 284.02 | 156.56 | NÃO | fora da faixa vertical |
| 10 | 244.00 | 59.00 | 282.64 | 155.56 | NÃO | fora da faixa vertical |
| 11 | 243.00 | 59.00 | 281.80 | 155.56 | NÃO | fora da faixa vertical |
| 12 | 242.00 | 59.00 | 280.96 | 155.56 | NÃO | fora da faixa vertical |
| 13 | 241.00 | 59.00 | 280.13 | 155.56 | NÃO | fora da faixa vertical |
| 14 | 240.00 | 59.00 | 279.29 | 155.56 | NÃO | fora da faixa vertical |
| 15 | 239.00 | 59.00 | 278.46 | 155.56 | NÃO | fora da faixa vertical |
| 16 | 238.00 | 59.00 | 277.63 | 155.56 | NÃO | fora da faixa vertical |
| 17 | 237.00 | 60.00 | 276.24 | 154.56 | NÃO | fora da faixa vertical |
| 18 | 236.00 | 60.00 | 275.41 | 154.56 | NÃO | fora da faixa vertical |
| 19 | 235.00 | 60.00 | 274.58 | 154.56 | NÃO | fora da faixa vertical |
| 20 | 234.00 | 60.00 | 273.75 | 154.56 | NÃO | fora da faixa vertical |
| 21 | 233.00 | 60.00 | 272.92 | 154.56 | NÃO | fora da faixa vertical |
| 22 | 232.00 | 61.00 | 271.53 | 153.56 | NÃO | fora da faixa vertical |
| 23 | 231.00 | 61.00 | 270.70 | 153.56 | NÃO | fora da faixa vertical |
| 24 | 230.00 | 61.00 | 269.88 | 153.56 | NÃO | fora da faixa vertical |
| 25 | 229.00 | 61.00 | 269.05 | 153.56 | NÃO | fora da faixa vertical |
| 26 | 228.00 | 61.00 | 268.23 | 153.56 | NÃO | fora da faixa vertical |
| 27 | 227.00 | 62.00 | 266.84 | 152.56 | NÃO | fora da faixa vertical |
| 28 | 226.00 | 62.00 | 266.01 | 152.56 | NÃO | fora da faixa vertical |
| 29 | 225.00 | 62.00 | 265.19 | 152.56 | NÃO | fora da faixa vertical |
| 30 | 224.00 | 62.00 | 264.37 | 152.56 | NÃO | fora da faixa vertical |
| 31 | 223.00 | 63.00 | 262.98 | 151.56 | NÃO | fora da faixa vertical |
| 32 | 222.00 | 63.00 | 262.15 | 151.56 | NÃO | fora da faixa vertical |
| 33 | 221.00 | 63.00 | 261.34 | 151.56 | NÃO | fora da faixa vertical |
| 34 | 220.00 | 63.00 | 260.52 | 151.56 | NÃO | fora da faixa vertical |
| 35 | 219.00 | 64.00 | 259.12 | 150.56 | NÃO | fora da faixa vertical |
| 36 | 218.00 | 64.00 | 258.31 | 150.56 | NÃO | fora da faixa vertical |
| 37 | 217.00 | 64.00 | 257.49 | 150.56 | NÃO | fora da faixa vertical |
| 38 | 216.00 | 65.00 | 256.10 | 149.56 | NÃO | fora da faixa vertical |
| 39 | 215.00 | 65.00 | 255.28 | 149.56 | NÃO | fora da faixa vertical |
| 40 | 214.00 | 65.00 | 254.47 | 149.56 | NÃO | fora da faixa vertical |
| 41 | 213.00 | 66.00 | 253.07 | 148.56 | NÃO | fora da faixa vertical |
| 42 | 212.00 | 66.00 | 252.26 | 148.56 | NÃO | fora da faixa vertical |
| 43 | 211.00 | 66.00 | 251.45 | 148.56 | NÃO | fora da faixa vertical |
| 44 | 210.00 | 66.00 | 250.64 | 148.56 | NÃO | fora da faixa vertical |
| 45 | 209.00 | 67.00 | 249.24 | 147.56 | NÃO | fora da faixa vertical |
| 46 | 208.00 | 67.00 | 248.43 | 147.56 | NÃO | fora da faixa vertical |
| 47 | 207.00 | 67.00 | 247.62 | 147.56 | NÃO | fora da faixa vertical |
| 48 | 206.00 | 68.00 | 246.22 | 146.56 | NÃO | fora da faixa vertical |
| 49 | 205.00 | 68.00 | 245.42 | 146.56 | NÃO | fora da faixa vertical |
| 50 | 204.00 | 69.00 | 244.02 | 145.56 | NÃO | fora da faixa vertical |
| 51 | 203.00 | 69.00 | 243.21 | 145.56 | NÃO | fora da faixa vertical |
| 52 | 202.00 | 69.00 | 242.41 | 145.56 | NÃO | fora da faixa vertical |
| 53 | 201.00 | 70.00 | 241.01 | 144.56 | NÃO | fora da faixa vertical |
| 54 | 200.00 | 70.00 | 240.20 | 144.56 | NÃO | fora da faixa vertical |
| 55 | 199.00 | 70.00 | 239.40 | 144.56 | NÃO | fora da faixa vertical |
| 56 | 198.00 | 71.00 | 238.00 | 143.56 | NÃO | fora da faixa vertical |
| 57 | 197.00 | 71.00 | 237.20 | 143.56 | NÃO | fora da faixa vertical |
| 58 | 196.00 | 72.00 | 235.80 | 142.56 | NÃO | fora da faixa vertical |
| 59 | 195.00 | 72.00 | 235.00 | 142.56 | NÃO | fora da faixa vertical |
| 60 | 194.00 | 72.00 | 234.20 | 142.56 | NÃO | fora da faixa vertical |
| 61 | 193.00 | 73.00 | 232.80 | 141.56 | NÃO | fora da faixa vertical |
| 62 | 192.00 | 73.00 | 232.00 | 141.56 | NÃO | fora da faixa vertical |
| 63 | 191.00 | 74.00 | 230.60 | 140.56 | NÃO | fora da faixa vertical |
| 64 | 190.00 | 74.00 | 229.80 | 140.56 | NÃO | fora da faixa vertical |
| 65 | 189.00 | 75.00 | 228.40 | 139.56 | NÃO | fora da faixa vertical |
| 66 | 188.00 | 75.00 | 227.61 | 139.56 | NÃO | fora da faixa vertical |
| 67 | 187.00 | 76.00 | 226.21 | 138.56 | NÃO | fora da faixa vertical |
| 68 | 186.00 | 76.00 | 225.41 | 138.56 | NÃO | fora da faixa vertical |
| 69 | 185.00 | 77.00 | 224.01 | 137.56 | NÃO | fora da faixa vertical |
| 70 | 184.00 | 77.00 | 223.22 | 137.56 | NÃO | fora da faixa vertical |
| 71 | 183.00 | 78.00 | 221.81 | 136.56 | NÃO | fora da faixa vertical |
| 72 | 182.00 | 78.00 | 221.02 | 136.56 | NÃO | fora da faixa vertical |
| 73 | 181.00 | 78.00 | 220.23 | 136.56 | NÃO | fora da faixa vertical |
| 74 | 180.00 | 79.00 | 218.83 | 135.56 | NÃO | fora da faixa vertical |
| 75 | 179.00 | 79.00 | 218.04 | 135.56 | NÃO | fora da faixa vertical |
| 76 | 178.00 | 80.00 | 216.63 | 134.56 | NÃO | fora da faixa vertical |
| 77 | 177.00 | 80.00 | 215.84 | 134.56 | NÃO | fora da faixa vertical |
| 78 | 176.00 | 81.00 | 214.44 | 133.56 | NÃO | fora da faixa vertical |
| 79 | 175.00 | 81.00 | 213.65 | 133.56 | NÃO | fora da faixa vertical |
| 80 | 174.00 | 82.00 | 212.25 | 132.56 | NÃO | fora da faixa vertical |
| 81 | 173.00 | 83.00 | 210.85 | 131.56 | NÃO | fora da faixa vertical |
| 82 | 172.00 | 83.00 | 210.06 | 131.56 | NÃO | fora da faixa vertical |
| 83 | 171.00 | 84.00 | 208.66 | 130.56 | NÃO | fora da faixa vertical |
| 84 | 170.00 | 85.00 | 207.25 | 129.56 | NÃO | fora da faixa vertical |
| 85 | 169.00 | 85.00 | 206.47 | 129.56 | NÃO | fora da faixa vertical |
| 86 | 168.00 | 86.00 | 205.06 | 128.56 | NÃO | fora da faixa vertical |
| 87 | 167.00 | 86.00 | 204.28 | 128.56 | NÃO | fora da faixa vertical |
| 88 | 166.00 | 87.00 | 202.87 | 127.56 | NÃO | fora da faixa vertical |
| 89 | 165.00 | 88.00 | 201.47 | 126.56 | NÃO | fora da faixa vertical |
| 90 | 164.00 | 88.00 | 200.68 | 126.56 | NÃO | fora da faixa vertical |
| 91 | 163.00 | 89.00 | 199.28 | 125.56 | NÃO | fora da faixa vertical |
| 92 | 162.00 | 89.00 | 198.50 | 125.56 | NÃO | fora da faixa vertical |
| 93 | 161.00 | 90.00 | 197.09 | 124.56 | NÃO | fora da faixa vertical |
| 94 | 160.00 | 91.00 | 195.69 | 123.56 | NÃO | fora da faixa vertical |
| 95 | 159.00 | 91.00 | 194.91 | 123.56 | NÃO | fora da faixa vertical |
| 96 | 158.00 | 92.00 | 193.50 | 122.56 | NÃO | fora da faixa vertical |
| 97 | 157.00 | 93.00 | 192.09 | 121.56 | NÃO | fora da faixa vertical |
| 98 | 156.00 | 93.00 | 191.31 | 121.56 | NÃO | fora da faixa vertical |
| 99 | 155.00 | 94.00 | 189.91 | 120.56 | NÃO | fora da faixa vertical |
| 100 | 154.00 | 95.00 | 188.50 | 119.56 | NÃO | fora da faixa vertical |
| 101 | 153.00 | 96.00 | 187.10 | 118.56 | NÃO | fora da faixa vertical |
| 102 | 152.00 | 96.00 | 186.32 | 118.56 | NÃO | fora da faixa vertical |
| 103 | 151.00 | 97.00 | 184.91 | 117.56 | NÃO | fora da faixa vertical |
| 104 | 150.00 | 98.00 | 183.50 | 116.56 | NÃO | fora da faixa vertical |
| 105 | 149.00 | 99.00 | 182.10 | 115.56 | NÃO | fora da faixa vertical |
| 106 | 148.00 | 99.00 | 181.32 | 115.56 | NÃO | fora da faixa vertical |
| 107 | 147.00 | 100.00 | 179.91 | 114.56 | NÃO | fora da faixa vertical |
| 108 | 146.00 | 101.00 | 178.51 | 113.56 | NÃO | fora da faixa vertical |
| 109 | 145.00 | 102.00 | 177.10 | 112.56 | NÃO | fora da faixa vertical |
| 110 | 144.00 | 102.00 | 176.32 | 112.56 | NÃO | fora da faixa vertical |
| 111 | 143.00 | 103.00 | 174.92 | 111.56 | NÃO | fora da faixa vertical |
| 112 | 142.00 | 104.00 | 173.51 | 110.56 | NÃO | fora da faixa vertical |
| 113 | 141.00 | 105.00 | 172.10 | 109.56 | NÃO | fora da faixa vertical |
| 114 | 140.00 | 106.00 | 170.70 | 108.56 | NÃO | fora da faixa vertical |
| 115 | 139.00 | 107.00 | 169.29 | 107.56 | NÃO | fora da faixa vertical |
| 116 | 138.00 | 108.00 | 167.89 | 106.56 | NÃO | fora da faixa vertical |
| 117 | 137.00 | 109.00 | 166.48 | 105.56 | NÃO | fora da faixa vertical |
| 118 | 136.00 | 109.00 | 165.70 | 105.56 | NÃO | fora da faixa vertical |
| 119 | 135.00 | 110.00 | 164.30 | 104.56 | NÃO | fora da faixa vertical |
| 120 | 134.00 | 111.00 | 162.89 | 103.56 | NÃO | fora da faixa vertical |
| 121 | 133.00 | 112.00 | 161.48 | 102.56 | NÃO | fora da faixa vertical |
| 122 | 132.00 | 113.00 | 160.08 | 101.56 | NÃO | fora da faixa vertical |
| 123 | 131.00 | 114.00 | 158.67 | 100.56 | NÃO | fora da faixa vertical |
| 124 | 130.00 | 115.00 | 157.27 | 99.56 | NÃO | fora da faixa vertical |
| 125 | 129.00 | 116.00 | 155.86 | 98.56 | NÃO | fora da faixa vertical |
| 126 | 128.00 | 117.00 | 154.46 | 97.56 | NÃO | fora da faixa vertical |
| 127 | 127.00 | 118.00 | 153.05 | 96.56 | NÃO | fora da faixa vertical |
| 128 | 126.00 | 119.00 | 151.65 | 95.56 | NÃO | fora da faixa vertical |
| 129 | 126.00 | 120.00 | 151.03 | 94.56 | NÃO | fora da faixa vertical |
| 130 | 125.00 | 121.00 | 149.63 | 93.56 | NÃO | fora da faixa vertical |
| 131 | 124.00 | 122.00 | 148.22 | 92.56 | NÃO | fora da faixa vertical |
| 132 | 123.00 | 123.00 | 146.82 | 91.56 | NÃO | fora da faixa vertical |
| 133 | 122.00 | 124.00 | 145.42 | 90.56 | NÃO | fora da faixa vertical |
| 134 | 121.00 | 125.00 | 144.01 | 89.56 | NÃO | fora da faixa vertical |
| 135 | 120.00 | 126.00 | 142.61 | 88.56 | NÃO | fora da faixa vertical |
| 136 | 119.00 | 127.00 | 141.21 | 87.56 | NÃO | fora da faixa vertical |
| 137 | 118.00 | 128.00 | 139.81 | 86.56 | NÃO | fora da faixa vertical |
| 138 | 117.00 | 128.00 | 139.01 | 86.56 | NÃO | fora da faixa vertical |
| 139 | 116.00 | 129.00 | 137.61 | 85.56 | NÃO | fora da faixa vertical |
| 140 | 115.00 | 129.00 | 136.82 | 85.56 | NÃO | fora da faixa vertical |
| 141 | 114.00 | 129.00 | 136.03 | 85.56 | NÃO | fora da faixa vertical |
| 142 | 113.00 | 129.00 | 135.25 | 85.56 | NÃO | fora da faixa vertical |
| 143 | 112.00 | 129.00 | 134.47 | 85.56 | NÃO | fora da faixa vertical |
| 144 | 111.00 | 129.00 | 133.69 | 85.56 | NÃO | fora da faixa vertical |
| 145 | 110.00 | 129.00 | 132.91 | 85.56 | NÃO | fora da faixa vertical |
| 146 | 109.00 | 129.00 | 132.14 | 85.56 | NÃO | fora da faixa vertical |
| 147 | 108.00 | 129.00 | 131.37 | 85.56 | NÃO | fora da faixa vertical |
| 148 | 107.00 | 129.00 | 130.60 | 85.56 | NÃO | fora da faixa vertical |
| 149 | 106.00 | 129.00 | 129.83 | 85.56 | NÃO | fora da faixa vertical |
| 150 | 105.00 | 129.00 | 129.07 | 85.56 | NÃO | fora da faixa vertical |
| 151 | 104.00 | 129.00 | 128.32 | 85.56 | NÃO | fora da faixa vertical |
| 152 | 103.00 | 129.00 | 127.56 | 85.56 | NÃO | fora da faixa vertical |
| 153 | 102.00 | 129.00 | 126.81 | 85.56 | NÃO | fora da faixa vertical |
| 154 | 101.00 | 129.00 | 126.06 | 85.56 | NÃO | fora da faixa vertical |
| 155 | 100.00 | 129.00 | 125.32 | 85.56 | NÃO | fora da faixa vertical |
| 156 | 99.00 | 129.00 | 124.58 | 85.56 | NÃO | fora da faixa vertical |
| 157 | 98.00 | 129.00 | 123.84 | 85.56 | NÃO | fora da faixa vertical |
| 158 | 97.00 | 129.00 | 123.11 | 85.56 | NÃO | fora da faixa vertical |
| 159 | 96.00 | 129.00 | 122.38 | 85.56 | NÃO | fora da faixa vertical |
| 160 | 95.00 | 129.00 | 121.66 | 85.56 | NÃO | fora da faixa vertical |
| 161 | 94.00 | 129.00 | 120.93 | 85.56 | NÃO | fora da faixa vertical |
| 162 | 93.00 | 129.00 | 120.22 | 85.56 | NÃO | fora da faixa vertical |
| 163 | 92.00 | 129.00 | 119.50 | 85.56 | NÃO | fora da faixa vertical |
| 164 | 91.00 | 129.00 | 118.79 | 85.56 | NÃO | fora da faixa vertical |
| 165 | 90.00 | 129.00 | 118.09 | 85.56 | NÃO | fora da faixa vertical |
| 166 | 89.00 | 129.00 | 117.39 | 85.56 | NÃO | fora da faixa vertical |
| 167 | 88.00 | 129.00 | 116.69 | 85.56 | NÃO | fora da faixa vertical |
| 168 | 87.00 | 129.00 | 116.00 | 85.56 | NÃO | fora da faixa vertical |
| 169 | 86.00 | 129.00 | 115.31 | 85.56 | NÃO | fora da faixa vertical |
| 170 | 85.00 | 129.00 | 114.63 | 85.56 | NÃO | fora da faixa vertical |
| 171 | 84.00 | 129.00 | 113.95 | 85.56 | NÃO | fora da faixa vertical |
| 172 | 83.00 | 129.00 | 113.28 | 85.56 | NÃO | fora da faixa vertical |
| 173 | 82.00 | 129.00 | 112.61 | 85.56 | NÃO | fora da faixa vertical |
| 174 | 81.00 | 129.00 | 111.95 | 85.56 | NÃO | fora da faixa vertical |
| 175 | 80.00 | 129.00 | 111.29 | 85.56 | NÃO | fora da faixa vertical |
| 176 | 79.00 | 129.00 | 110.63 | 85.56 | NÃO | fora da faixa vertical |
| 177 | 78.00 | 129.00 | 109.99 | 85.56 | NÃO | fora da faixa vertical |
| 178 | 77.00 | 129.00 | 109.34 | 85.56 | NÃO | fora da faixa vertical |
| 179 | 76.00 | 129.00 | 108.71 | 85.56 | NÃO | fora da faixa vertical |
| 180 | 75.00 | 129.00 | 108.07 | 85.56 | NÃO | fora da faixa vertical |
| 181 | 74.00 | 129.00 | 107.45 | 85.56 | NÃO | fora da faixa vertical |
| 182 | 73.00 | 129.00 | 106.83 | 85.56 | NÃO | fora da faixa vertical |
| 183 | 72.00 | 129.00 | 106.21 | 85.56 | NÃO | fora da faixa vertical |
| 184 | 71.00 | 129.00 | 105.60 | 85.56 | NÃO | fora da faixa vertical |
| 185 | 70.00 | 129.00 | 105.00 | 85.56 | NÃO | fora da faixa vertical |
| 186 | 69.00 | 129.00 | 104.40 | 85.56 | NÃO | fora da faixa vertical |
| 187 | 68.00 | 129.00 | 103.81 | 85.56 | NÃO | fora da faixa vertical |
| 188 | 67.00 | 129.00 | 103.23 | 85.56 | NÃO | fora da faixa vertical |
| 189 | 66.00 | 129.00 | 102.65 | 85.56 | NÃO | fora da faixa vertical |
| 190 | 65.00 | 129.00 | 102.08 | 85.56 | NÃO | fora da faixa vertical |
| 191 | 64.00 | 129.00 | 101.51 | 85.56 | NÃO | fora da faixa vertical |
| 192 | 63.00 | 129.00 | 100.96 | 85.56 | NÃO | fora da faixa vertical |
| 193 | 62.00 | 129.00 | 100.40 | 85.56 | NÃO | fora da faixa vertical |
| 194 | 61.00 | 129.00 | 99.86 | 85.56 | NÃO | fora da faixa vertical |
| 195 | 60.00 | 129.00 | 99.32 | 85.56 | NÃO | fora da faixa vertical |
| 196 | 59.00 | 129.00 | 98.79 | 85.56 | NÃO | fora da faixa vertical |
| 197 | 58.00 | 129.00 | 98.27 | 85.56 | NÃO | fora da faixa vertical |
| 198 | 57.00 | 129.00 | 97.75 | 85.56 | NÃO | fora da faixa vertical |
| 199 | 56.00 | 129.00 | 97.25 | 85.56 | NÃO | fora da faixa vertical |
| 200 | 55.00 | 129.00 | 96.75 | 85.56 | NÃO | fora da faixa vertical |
| 201 | 54.00 | 129.00 | 96.25 | 85.56 | NÃO | fora da faixa vertical |
| 202 | 53.00 | 129.00 | 95.77 | 85.56 | NÃO | fora da faixa vertical |
| 203 | 52.00 | 129.00 | 95.29 | 85.56 | NÃO | fora da faixa vertical |
| 204 | 51.00 | 129.00 | 94.83 | 85.56 | NÃO | fora da faixa vertical |
| 205 | 50.00 | 129.00 | 94.37 | 85.56 | NÃO | fora da faixa vertical |
| 206 | 49.00 | 129.00 | 93.91 | 85.56 | NÃO | fora da faixa vertical |
| 207 | 48.00 | 129.00 | 93.47 | 85.56 | NÃO | fora da faixa vertical |
| 208 | 47.00 | 129.00 | 93.04 | 85.56 | NÃO | fora da faixa vertical |
| 209 | 46.00 | 129.00 | 92.61 | 85.56 | NÃO | fora da faixa vertical |
| 210 | 45.00 | 129.00 | 92.20 | 85.56 | NÃO | fora da faixa vertical |
| 211 | 44.00 | 129.00 | 91.79 | 85.56 | NÃO | fora da faixa vertical |
| 212 | 43.00 | 129.00 | 91.39 | 85.56 | NÃO | fora da faixa vertical |
| 213 | 42.00 | 129.00 | 91.00 | 85.56 | NÃO | fora da faixa vertical |
| 214 | 41.00 | 129.00 | 90.62 | 85.56 | NÃO | fora da faixa vertical |
| 215 | 40.00 | 129.00 | 90.25 | 85.56 | NÃO | fora da faixa vertical |
| 216 | 39.00 | 129.00 | 89.89 | 85.56 | NÃO | fora da faixa vertical |
| 217 | 38.00 | 129.00 | 89.54 | 85.56 | NÃO | fora da faixa vertical |
| 218 | 37.00 | 129.00 | 89.20 | 85.56 | NÃO | fora da faixa vertical |
| 219 | 36.00 | 129.00 | 88.87 | 85.56 | NÃO | fora da faixa vertical |
| 220 | 35.00 | 129.00 | 88.54 | 85.56 | NÃO | fora da faixa vertical |
| 221 | 34.00 | 129.00 | 88.23 | 85.56 | NÃO | fora da faixa vertical |
| 222 | 33.00 | 129.00 | 87.93 | 85.56 | NÃO | fora da faixa vertical |
| 223 | 32.00 | 129.00 | 87.64 | 85.56 | NÃO | fora da faixa vertical |
| 224 | 31.00 | 129.00 | 87.36 | 85.56 | NÃO | fora da faixa vertical |
| 225 | 30.00 | 129.00 | 87.09 | 85.56 | NÃO | fora da faixa vertical |
| 226 | 29.00 | 129.00 | 86.83 | 85.56 | NÃO | fora da faixa vertical |
| 227 | 28.00 | 129.00 | 86.59 | 85.56 | NÃO | fora da faixa vertical |
| 228 | 27.00 | 129.00 | 86.35 | 85.56 | NÃO | fora da faixa vertical |
| 229 | 26.00 | 129.00 | 86.12 | 85.56 | NÃO | fora da faixa vertical |
| 230 | 25.00 | 129.00 | 85.91 | 85.56 | NÃO | fora da faixa vertical |
| 231 | 24.00 | 129.00 | 85.70 | 85.56 | NÃO | fora da faixa vertical |
| 232 | 23.00 | 129.00 | 85.51 | 85.56 | NÃO | fora da faixa vertical |
| 233 | 22.00 | 129.00 | 85.33 | 85.56 | NÃO | fora da faixa vertical |
| 234 | 21.00 | 129.00 | 85.16 | 85.56 | NÃO | fora da faixa vertical |
| 235 | 20.00 | 129.00 | 85.00 | 85.56 | NÃO | fora da faixa vertical |
| 236 | 19.00 | 129.00 | 84.85 | 85.56 | NÃO | fora da faixa vertical |
| 237 | 18.00 | 129.00 | 84.72 | 85.56 | NÃO | fora da faixa vertical |
| 238 | 17.00 | 129.00 | 84.59 | 85.56 | NÃO | fora da faixa vertical |
| 239 | 16.00 | 129.00 | 84.48 | 85.56 | NÃO | fora da faixa vertical |
| 240 | 15.00 | 129.00 | 84.38 | 85.56 | NÃO | fora da faixa vertical |
| 241 | 14.00 | 129.00 | 84.29 | 85.56 | NÃO | fora da faixa vertical |
| 242 | 13.00 | 129.00 | 84.21 | 85.56 | NÃO | fora da faixa vertical |
| 243 | 12.00 | 129.00 | 84.15 | 85.56 | NÃO | fora da faixa vertical |
| 244 | 11.00 | 129.00 | 84.10 | 85.56 | NÃO | fora da faixa vertical |
| 245 | 10.00 | 129.00 | 84.05 | 85.56 | NÃO | fora da faixa vertical |
| 246 | 9.00 | 129.00 | 84.02 | 85.56 | NÃO | fora da faixa vertical |
| 247 | 8.00 | 129.00 | 84.01 | 85.56 | NÃO | fora da faixa vertical |
| 248 | 7.00 | 129.00 | 84.00 | 85.56 | NÃO | fora da faixa vertical |
| 249 | 7.00 | 213.00 | 0.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 250 | 8.00 | 213.00 | 1.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 251 | 9.00 | 213.00 | 2.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 252 | 10.00 | 213.00 | 3.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 253 | 11.00 | 213.00 | 4.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 254 | 12.00 | 213.00 | 5.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 255 | 13.00 | 213.00 | 6.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 256 | 14.00 | 213.00 | 7.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 257 | 15.00 | 213.00 | 8.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 258 | 16.00 | 213.00 | 9.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 259 | 17.00 | 213.00 | 10.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 260 | 18.00 | 213.00 | 11.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 261 | 19.00 | 213.00 | 12.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 262 | 20.00 | 213.00 | 13.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 263 | 21.00 | 213.00 | 14.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 264 | 22.00 | 213.00 | 15.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 265 | 23.00 | 213.00 | 16.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 266 | 24.00 | 213.00 | 17.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 267 | 25.00 | 213.00 | 18.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 268 | 26.00 | 213.00 | 19.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 269 | 27.00 | 213.00 | 20.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 270 | 28.00 | 213.00 | 21.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 271 | 29.00 | 213.00 | 22.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 272 | 30.00 | 213.00 | 23.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 273 | 31.00 | 213.00 | 24.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 274 | 32.00 | 213.00 | 25.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 275 | 33.00 | 213.00 | 26.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 276 | 34.00 | 213.00 | 27.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 277 | 35.00 | 213.00 | 28.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 278 | 36.00 | 213.00 | 29.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 279 | 37.00 | 213.00 | 30.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 280 | 38.00 | 213.00 | 31.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 281 | 39.00 | 213.00 | 32.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 282 | 40.00 | 213.00 | 33.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 283 | 41.00 | 213.00 | 34.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 284 | 42.00 | 213.00 | 35.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 285 | 43.00 | 213.00 | 36.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 286 | 44.00 | 213.00 | 37.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 287 | 45.00 | 213.00 | 38.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 288 | 46.00 | 213.00 | 39.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 289 | 47.00 | 213.00 | 40.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 290 | 48.00 | 213.00 | 41.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 291 | 49.00 | 213.00 | 42.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 292 | 50.00 | 213.00 | 43.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 293 | 51.00 | 213.00 | 44.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 294 | 52.00 | 213.00 | 45.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 295 | 53.00 | 213.00 | 46.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 296 | 54.00 | 213.00 | 47.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 297 | 55.00 | 213.00 | 48.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 298 | 56.00 | 213.00 | 49.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 299 | 57.00 | 213.00 | 50.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 300 | 58.00 | 213.00 | 51.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 301 | 59.00 | 213.00 | 52.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 302 | 60.00 | 213.00 | 53.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 303 | 61.00 | 213.00 | 54.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 304 | 62.00 | 213.00 | 55.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 305 | 63.00 | 213.00 | 56.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 306 | 64.00 | 213.00 | 57.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 307 | 65.00 | 213.00 | 58.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 308 | 66.00 | 213.00 | 59.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 309 | 67.00 | 213.00 | 60.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 310 | 68.00 | 213.00 | 61.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 311 | 69.00 | 213.00 | 62.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 312 | 70.00 | 213.00 | 63.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 313 | 71.00 | 213.00 | 64.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 314 | 72.00 | 213.00 | 65.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 315 | 73.00 | 213.00 | 66.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 316 | 74.00 | 213.00 | 67.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 317 | 455.00 | 213.00 | 448.00 | 1.56 | NÃO | fora do lado solicitado |
| 318 | 456.00 | 213.00 | 449.00 | 1.56 | NÃO | fora do lado solicitado |
| 319 | 457.00 | 213.00 | 450.00 | 1.56 | NÃO | fora do lado solicitado |
| 320 | 458.00 | 213.00 | 451.00 | 1.56 | NÃO | fora do lado solicitado |
| 321 | 459.00 | 213.00 | 452.00 | 1.56 | NÃO | fora do lado solicitado |
| 322 | 460.00 | 213.00 | 453.00 | 1.56 | NÃO | fora do lado solicitado |
| 323 | 461.00 | 213.00 | 454.00 | 1.56 | NÃO | fora do lado solicitado |
| 324 | 462.00 | 213.00 | 455.00 | 1.56 | NÃO | fora do lado solicitado |
| 325 | 463.00 | 213.00 | 456.00 | 1.56 | NÃO | fora do lado solicitado |
| 326 | 464.00 | 213.00 | 457.00 | 1.56 | NÃO | fora do lado solicitado |
| 327 | 465.00 | 213.00 | 458.00 | 1.56 | NÃO | fora do lado solicitado |
| 328 | 466.00 | 213.00 | 459.00 | 1.56 | NÃO | fora do lado solicitado |
| 329 | 467.00 | 213.00 | 460.00 | 1.56 | NÃO | fora do lado solicitado |
| 330 | 468.00 | 213.00 | 461.00 | 1.56 | NÃO | fora do lado solicitado |
| 331 | 469.00 | 213.00 | 462.00 | 1.56 | NÃO | fora do lado solicitado |
| 332 | 470.00 | 213.00 | 463.00 | 1.56 | NÃO | fora do lado solicitado |
| 333 | 471.00 | 213.00 | 464.00 | 1.56 | NÃO | fora do lado solicitado |
| 334 | 472.00 | 213.00 | 465.00 | 1.56 | NÃO | fora do lado solicitado |
| 335 | 473.00 | 213.00 | 466.00 | 1.56 | NÃO | fora do lado solicitado |
| 336 | 474.00 | 213.00 | 467.00 | 1.56 | NÃO | fora do lado solicitado |
| 337 | 475.00 | 213.00 | 468.00 | 1.56 | NÃO | fora do lado solicitado |
| 338 | 476.00 | 213.00 | 469.00 | 1.56 | NÃO | fora do lado solicitado |
| 339 | 477.00 | 213.00 | 470.00 | 1.56 | NÃO | fora do lado solicitado |
| 340 | 478.00 | 213.00 | 471.00 | 1.56 | NÃO | fora do lado solicitado |
| 341 | 479.00 | 213.00 | 472.00 | 1.56 | NÃO | fora do lado solicitado |
| 342 | 480.00 | 213.00 | 473.00 | 1.56 | NÃO | fora do lado solicitado |
| 343 | 481.00 | 213.00 | 474.00 | 1.56 | NÃO | fora do lado solicitado |
| 344 | 482.00 | 213.00 | 475.00 | 1.56 | NÃO | fora do lado solicitado |
| 345 | 483.00 | 213.00 | 476.00 | 1.56 | NÃO | fora do lado solicitado |
| 346 | 484.00 | 213.00 | 477.00 | 1.56 | NÃO | fora do lado solicitado |
| 347 | 485.00 | 213.00 | 478.00 | 1.56 | NÃO | fora do lado solicitado |
| 348 | 486.00 | 213.00 | 479.00 | 1.56 | NÃO | fora do lado solicitado |
| 349 | 487.00 | 213.00 | 480.00 | 1.56 | NÃO | fora do lado solicitado |
| 350 | 488.00 | 213.00 | 481.00 | 1.56 | NÃO | fora do lado solicitado |
| 351 | 489.00 | 213.00 | 482.00 | 1.56 | NÃO | fora do lado solicitado |
| 352 | 490.00 | 213.00 | 483.00 | 1.56 | NÃO | fora do lado solicitado |
| 353 | 491.00 | 213.00 | 484.00 | 1.56 | NÃO | fora do lado solicitado |
| 354 | 492.00 | 213.00 | 485.00 | 1.56 | NÃO | fora do lado solicitado |
| 355 | 493.00 | 213.00 | 486.00 | 1.56 | NÃO | fora do lado solicitado |
| 356 | 494.00 | 213.00 | 487.00 | 1.56 | NÃO | fora do lado solicitado |
| 357 | 495.00 | 213.00 | 488.00 | 1.56 | NÃO | fora do lado solicitado |
| 358 | 496.00 | 213.00 | 489.00 | 1.56 | NÃO | fora do lado solicitado |
| 359 | 497.00 | 213.00 | 490.00 | 1.56 | NÃO | fora do lado solicitado |
| 360 | 498.00 | 213.00 | 491.00 | 1.56 | NÃO | fora do lado solicitado |
| 361 | 499.00 | 213.00 | 492.00 | 1.56 | NÃO | fora do lado solicitado |
| 362 | 500.00 | 213.00 | 493.00 | 1.56 | NÃO | fora do lado solicitado |
| 363 | 501.00 | 213.00 | 494.00 | 1.56 | NÃO | fora do lado solicitado |
| 364 | 502.00 | 213.00 | 495.00 | 1.56 | NÃO | fora do lado solicitado |
| 365 | 503.00 | 213.00 | 496.00 | 1.56 | NÃO | fora do lado solicitado |
| 366 | 504.00 | 213.00 | 497.00 | 1.56 | NÃO | fora do lado solicitado |
| 367 | 505.00 | 213.00 | 498.00 | 1.56 | NÃO | fora do lado solicitado |
| 368 | 506.00 | 213.00 | 499.00 | 1.56 | NÃO | fora do lado solicitado |
| 369 | 507.00 | 213.00 | 500.00 | 1.56 | NÃO | fora do lado solicitado |
| 370 | 508.00 | 213.00 | 501.00 | 1.56 | NÃO | fora do lado solicitado |
| 371 | 509.00 | 213.00 | 502.00 | 1.56 | NÃO | fora do lado solicitado |
| 372 | 510.00 | 213.00 | 503.00 | 1.56 | NÃO | fora do lado solicitado |
| 373 | 511.00 | 213.00 | 504.00 | 1.56 | NÃO | fora do lado solicitado |
| 374 | 512.00 | 213.00 | 505.00 | 1.56 | NÃO | fora do lado solicitado |
| 375 | 513.00 | 213.00 | 506.00 | 1.56 | NÃO | fora do lado solicitado |
| 376 | 514.00 | 213.00 | 507.00 | 1.56 | NÃO | fora do lado solicitado |
| 377 | 515.00 | 213.00 | 508.00 | 1.56 | NÃO | fora do lado solicitado |
| 378 | 516.00 | 213.00 | 509.00 | 1.56 | NÃO | fora do lado solicitado |
| 379 | 517.00 | 213.00 | 510.00 | 1.56 | NÃO | fora do lado solicitado |
| 380 | 518.00 | 213.00 | 511.00 | 1.56 | NÃO | fora do lado solicitado |
| 381 | 519.00 | 213.00 | 512.00 | 1.56 | NÃO | fora do lado solicitado |
| 382 | 520.00 | 213.00 | 513.00 | 1.56 | NÃO | fora do lado solicitado |
| 383 | 520.00 | 212.00 | 513.00 | 2.56 | NÃO | fora do lado solicitado |
| 384 | 520.00 | 211.00 | 513.00 | 3.56 | NÃO | fora do lado solicitado |
| 385 | 520.00 | 210.00 | 513.01 | 4.56 | NÃO | fora do lado solicitado |
| 386 | 520.00 | 209.00 | 513.02 | 5.56 | NÃO | fora do lado solicitado |
| 387 | 520.00 | 208.00 | 513.02 | 6.56 | NÃO | fora do lado solicitado |
| 388 | 520.00 | 207.00 | 513.04 | 7.56 | NÃO | fora do lado solicitado |
| 389 | 520.00 | 206.00 | 513.05 | 8.56 | NÃO | fora do lado solicitado |
| 390 | 520.00 | 205.00 | 513.06 | 9.56 | NÃO | fora do lado solicitado |
| 391 | 520.00 | 204.00 | 513.08 | 10.56 | NÃO | fora do lado solicitado |
| 392 | 520.00 | 203.00 | 513.10 | 11.56 | NÃO | fora do lado solicitado |
| 393 | 520.00 | 202.00 | 513.12 | 12.56 | NÃO | fora do lado solicitado |
| 394 | 520.00 | 201.00 | 513.14 | 13.56 | NÃO | fora do lado solicitado |
| 395 | 520.00 | 200.00 | 513.16 | 14.56 | NÃO | fora do lado solicitado |
| 396 | 520.00 | 199.00 | 513.19 | 15.56 | NÃO | fora do lado solicitado |
| 397 | 520.00 | 198.00 | 513.22 | 16.56 | NÃO | fora do lado solicitado |
| 398 | 520.00 | 197.00 | 513.25 | 17.56 | NÃO | fora do lado solicitado |
| 399 | 520.00 | 196.00 | 513.28 | 18.56 | NÃO | fora do lado solicitado |
| 400 | 520.00 | 195.00 | 513.32 | 19.56 | NÃO | fora do lado solicitado |
| 401 | 520.00 | 194.00 | 513.35 | 20.56 | NÃO | fora do lado solicitado |
| 402 | 520.00 | 193.00 | 513.39 | 21.56 | NÃO | fora do lado solicitado |
| 403 | 520.00 | 192.00 | 513.43 | 22.56 | NÃO | fora do lado solicitado |
| 404 | 520.00 | 191.00 | 513.47 | 23.56 | NÃO | fora do lado solicitado |
| 405 | 520.00 | 190.00 | 513.52 | 24.56 | NÃO | fora do lado solicitado |
| 406 | 520.00 | 189.00 | 513.56 | 25.56 | NÃO | fora do lado solicitado |
| 407 | 520.00 | 188.00 | 513.61 | 26.56 | NÃO | fora do lado solicitado |
| 408 | 520.00 | 187.00 | 513.66 | 27.56 | NÃO | fora do lado solicitado |
| 409 | 520.00 | 186.00 | 513.71 | 28.56 | NÃO | fora do lado solicitado |
| 410 | 520.00 | 185.00 | 513.76 | 29.56 | NÃO | fora do lado solicitado |
| 411 | 520.00 | 184.00 | 513.82 | 30.56 | NÃO | fora do lado solicitado |
| 412 | 520.00 | 183.00 | 513.88 | 31.56 | NÃO | fora do lado solicitado |
| 413 | 520.00 | 182.00 | 513.94 | 32.56 | NÃO | fora do lado solicitado |
| 414 | 520.00 | 181.00 | 514.00 | 33.56 | NÃO | fora do lado solicitado |
| 415 | 520.00 | 180.00 | 514.06 | 34.56 | NÃO | fora do lado solicitado |
| 416 | 520.00 | 179.00 | 514.13 | 35.56 | NÃO | fora do lado solicitado |
| 417 | 520.00 | 178.00 | 514.19 | 36.56 | NÃO | fora do lado solicitado |
| 418 | 520.00 | 177.00 | 514.26 | 37.56 | NÃO | fora do lado solicitado |
| 419 | 520.00 | 176.00 | 514.33 | 38.56 | NÃO | fora do lado solicitado |
| 420 | 520.00 | 175.00 | 514.41 | 39.56 | NÃO | fora do lado solicitado |
| 421 | 520.00 | 174.00 | 514.48 | 40.56 | NÃO | fora do lado solicitado |
| 422 | 520.00 | 173.00 | 514.56 | 41.56 | NÃO | fora do lado solicitado |
| 423 | 520.00 | 172.00 | 514.64 | 42.56 | NÃO | fora do lado solicitado |
| 424 | 520.00 | 171.00 | 514.72 | 43.56 | NÃO | fora do lado solicitado |
| 425 | 520.00 | 170.00 | 514.80 | 44.56 | NÃO | fora do lado solicitado |
| 426 | 520.00 | 169.00 | 514.88 | 45.56 | NÃO | fora do lado solicitado |
| 427 | 520.00 | 168.00 | 514.97 | 46.56 | NÃO | fora do lado solicitado |
| 428 | 520.00 | 167.00 | 515.06 | 47.56 | NÃO | fora do lado solicitado |
| 429 | 520.00 | 166.00 | 515.15 | 48.56 | NÃO | fora do lado solicitado |
| 430 | 520.00 | 165.00 | 515.24 | 49.56 | NÃO | fora do lado solicitado |
| 431 | 520.00 | 164.00 | 515.33 | 50.56 | NÃO | fora do lado solicitado |
| 432 | 520.00 | 163.00 | 515.43 | 51.56 | NÃO | fora do lado solicitado |
| 433 | 520.00 | 162.00 | 515.53 | 52.56 | NÃO | fora do lado solicitado |
| 434 | 520.00 | 161.00 | 515.63 | 53.56 | NÃO | fora do lado solicitado |
| 435 | 520.00 | 160.00 | 515.73 | 54.56 | NÃO | fora do lado solicitado |
| 436 | 520.00 | 159.00 | 515.83 | 55.56 | NÃO | fora do lado solicitado |
| 437 | 520.00 | 158.00 | 515.94 | 56.56 | NÃO | fora do lado solicitado |
| 438 | 520.00 | 157.00 | 516.05 | 57.56 | NÃO | fora do lado solicitado |
| 439 | 520.00 | 156.00 | 516.16 | 58.56 | NÃO | fora do lado solicitado |
| 440 | 520.00 | 155.00 | 516.27 | 59.56 | NÃO | fora do lado solicitado |
| 441 | 520.00 | 154.00 | 516.38 | 60.56 | NÃO | fora do lado solicitado |
| 442 | 520.00 | 153.00 | 516.50 | 61.56 | NÃO | fora do lado solicitado |
| 443 | 520.00 | 152.00 | 516.61 | 62.56 | NÃO | fora do lado solicitado |
| 444 | 520.00 | 151.00 | 516.73 | 63.56 | NÃO | fora do lado solicitado |
| 445 | 520.00 | 150.00 | 516.85 | 64.56 | NÃO | fora do lado solicitado |
| 446 | 520.00 | 149.00 | 516.98 | 65.56 | NÃO | fora do lado solicitado |
| 447 | 520.00 | 148.00 | 517.10 | 66.56 | NÃO | fora do lado solicitado |
| 448 | 520.00 | 147.00 | 517.23 | 67.56 | NÃO | fora do lado solicitado |
| 449 | 520.00 | 146.00 | 517.36 | 68.56 | NÃO | fora do lado solicitado |
| 450 | 520.00 | 145.00 | 517.49 | 69.56 | NÃO | fora do lado solicitado |
| 451 | 520.00 | 144.00 | 517.62 | 70.56 | NÃO | fora do lado solicitado |
| 452 | 520.00 | 143.00 | 517.75 | 71.56 | NÃO | fora do lado solicitado |
| 453 | 520.00 | 142.00 | 517.89 | 72.56 | NÃO | fora do lado solicitado |
| 454 | 520.00 | 141.00 | 518.03 | 73.56 | NÃO | fora do lado solicitado |
| 455 | 520.00 | 140.00 | 518.17 | 74.56 | NÃO | fora do lado solicitado |
| 456 | 520.00 | 139.00 | 518.31 | 75.56 | NÃO | fora do lado solicitado |
| 457 | 520.00 | 138.00 | 518.45 | 76.56 | NÃO | fora do lado solicitado |
| 458 | 520.00 | 137.00 | 518.60 | 77.56 | NÃO | fora do lado solicitado |
| 459 | 520.00 | 136.00 | 518.75 | 78.56 | NÃO | fora do lado solicitado |
| 460 | 520.00 | 135.00 | 518.90 | 79.56 | NÃO | fora do lado solicitado |
| 461 | 520.00 | 134.00 | 519.05 | 80.56 | NÃO | fora do lado solicitado |
| 462 | 520.00 | 133.00 | 519.20 | 81.56 | NÃO | fora do lado solicitado |
| 463 | 520.00 | 132.00 | 519.36 | 82.56 | NÃO | fora do lado solicitado |
| 464 | 520.00 | 131.00 | 519.51 | 83.56 | NÃO | fora do lado solicitado |
| 465 | 520.00 | 130.00 | 519.67 | 84.56 | NÃO | fora do lado solicitado |
| 466 | 520.00 | 129.00 | 519.83 | 85.56 | NÃO | fora da faixa vertical |
| 467 | 519.00 | 129.00 | 518.84 | 85.56 | NÃO | fora da faixa vertical |
| 468 | 518.00 | 129.00 | 517.86 | 85.56 | NÃO | fora da faixa vertical |
| 469 | 517.00 | 129.00 | 516.87 | 85.56 | NÃO | fora da faixa vertical |
| 470 | 516.00 | 129.00 | 515.88 | 85.56 | NÃO | fora da faixa vertical |
| 471 | 515.00 | 129.00 | 514.90 | 85.56 | NÃO | fora da faixa vertical |
| 472 | 514.00 | 129.00 | 513.91 | 85.56 | NÃO | fora da faixa vertical |
| 473 | 513.00 | 129.00 | 512.92 | 85.56 | NÃO | fora da faixa vertical |
| 474 | 512.00 | 129.00 | 511.94 | 85.56 | NÃO | fora da faixa vertical |
| 475 | 511.00 | 129.00 | 510.95 | 85.56 | NÃO | fora da faixa vertical |
| 476 | 510.00 | 129.00 | 509.97 | 85.56 | NÃO | fora da faixa vertical |
| 477 | 509.00 | 129.00 | 508.98 | 85.56 | NÃO | fora da faixa vertical |
| 478 | 508.00 | 129.00 | 507.99 | 85.56 | NÃO | fora da faixa vertical |
| 479 | 507.00 | 129.00 | 507.01 | 85.56 | NÃO | fora da faixa vertical |
| 480 | 506.00 | 129.00 | 506.02 | 85.56 | NÃO | fora da faixa vertical |
| 481 | 505.00 | 129.00 | 505.03 | 85.56 | NÃO | fora da faixa vertical |
| 482 | 504.00 | 129.00 | 504.05 | 85.56 | NÃO | fora da faixa vertical |
| 483 | 503.00 | 129.00 | 503.06 | 85.56 | NÃO | fora da faixa vertical |
| 484 | 502.00 | 129.00 | 502.08 | 85.56 | NÃO | fora da faixa vertical |
| 485 | 501.00 | 129.00 | 501.09 | 85.56 | NÃO | fora da faixa vertical |
| 486 | 500.00 | 129.00 | 500.10 | 85.56 | NÃO | fora da faixa vertical |
| 487 | 499.00 | 129.00 | 499.12 | 85.56 | NÃO | fora da faixa vertical |
| 488 | 498.00 | 129.00 | 498.13 | 85.56 | NÃO | fora da faixa vertical |
| 489 | 497.00 | 129.00 | 497.15 | 85.56 | NÃO | fora da faixa vertical |
| 490 | 496.00 | 129.00 | 496.16 | 85.56 | NÃO | fora da faixa vertical |
| 491 | 495.00 | 129.00 | 495.18 | 85.56 | NÃO | fora da faixa vertical |
| 492 | 494.00 | 129.00 | 494.19 | 85.56 | NÃO | fora da faixa vertical |
| 493 | 493.00 | 129.00 | 493.21 | 85.56 | NÃO | fora da faixa vertical |
| 494 | 492.00 | 129.00 | 492.22 | 85.56 | NÃO | fora da faixa vertical |
| 495 | 491.00 | 129.00 | 491.24 | 85.56 | NÃO | fora da faixa vertical |
| 496 | 490.00 | 129.00 | 490.25 | 85.56 | NÃO | fora da faixa vertical |
| 497 | 489.00 | 129.00 | 489.26 | 85.56 | NÃO | fora da faixa vertical |
| 498 | 488.00 | 129.00 | 488.28 | 85.56 | NÃO | fora da faixa vertical |
| 499 | 487.00 | 129.00 | 487.29 | 85.56 | NÃO | fora da faixa vertical |
| 500 | 486.00 | 129.00 | 486.31 | 85.56 | NÃO | fora da faixa vertical |
| 501 | 485.00 | 129.00 | 485.32 | 85.56 | NÃO | fora da faixa vertical |
| 502 | 484.00 | 129.00 | 484.34 | 85.56 | NÃO | fora da faixa vertical |
| 503 | 483.00 | 129.00 | 483.35 | 85.56 | NÃO | fora da faixa vertical |
| 504 | 482.00 | 129.00 | 482.37 | 85.56 | NÃO | fora da faixa vertical |
| 505 | 481.00 | 129.00 | 481.39 | 85.56 | NÃO | fora da faixa vertical |
| 506 | 480.00 | 129.00 | 480.40 | 85.56 | NÃO | fora da faixa vertical |
| 507 | 479.00 | 129.00 | 479.42 | 85.56 | NÃO | fora da faixa vertical |
| 508 | 478.00 | 129.00 | 478.43 | 85.56 | NÃO | fora da faixa vertical |
| 509 | 477.00 | 129.00 | 477.45 | 85.56 | NÃO | fora da faixa vertical |
| 510 | 476.00 | 129.00 | 476.46 | 85.56 | NÃO | fora da faixa vertical |
| 511 | 475.00 | 129.00 | 475.48 | 85.56 | NÃO | fora da faixa vertical |
| 512 | 474.00 | 129.00 | 474.49 | 85.56 | NÃO | fora da faixa vertical |
| 513 | 473.00 | 129.00 | 473.51 | 85.56 | NÃO | fora da faixa vertical |
| 514 | 472.00 | 129.00 | 472.53 | 85.56 | NÃO | fora da faixa vertical |
| 515 | 471.00 | 129.00 | 471.54 | 85.56 | NÃO | fora da faixa vertical |
| 516 | 470.00 | 129.00 | 470.56 | 85.56 | NÃO | fora da faixa vertical |
| 517 | 469.00 | 129.00 | 469.57 | 85.56 | NÃO | fora da faixa vertical |
| 518 | 468.00 | 129.00 | 468.59 | 85.56 | NÃO | fora da faixa vertical |
| 519 | 467.00 | 129.00 | 467.61 | 85.56 | NÃO | fora da faixa vertical |
| 520 | 466.00 | 129.00 | 466.62 | 85.56 | NÃO | fora da faixa vertical |
| 521 | 465.00 | 129.00 | 465.64 | 85.56 | NÃO | fora da faixa vertical |
| 522 | 464.00 | 129.00 | 464.66 | 85.56 | NÃO | fora da faixa vertical |
| 523 | 463.00 | 129.00 | 463.67 | 85.56 | NÃO | fora da faixa vertical |
| 524 | 462.00 | 129.00 | 462.69 | 85.56 | NÃO | fora da faixa vertical |
| 525 | 461.00 | 129.00 | 461.71 | 85.56 | NÃO | fora da faixa vertical |
| 526 | 460.00 | 129.00 | 460.72 | 85.56 | NÃO | fora da faixa vertical |
| 527 | 459.00 | 129.00 | 459.74 | 85.56 | NÃO | fora da faixa vertical |
| 528 | 458.00 | 129.00 | 458.76 | 85.56 | NÃO | fora da faixa vertical |
| 529 | 457.00 | 129.00 | 457.77 | 85.56 | NÃO | fora da faixa vertical |
| 530 | 456.00 | 129.00 | 456.79 | 85.56 | NÃO | fora da faixa vertical |
| 531 | 455.00 | 129.00 | 455.81 | 85.56 | NÃO | fora da faixa vertical |
| 532 | 454.00 | 129.00 | 454.82 | 85.56 | NÃO | fora da faixa vertical |
| 533 | 453.00 | 129.00 | 453.84 | 85.56 | NÃO | fora da faixa vertical |
| 534 | 452.00 | 129.00 | 452.86 | 85.56 | NÃO | fora da faixa vertical |
| 535 | 451.00 | 129.00 | 451.88 | 85.56 | NÃO | fora da faixa vertical |
| 536 | 450.00 | 129.00 | 450.89 | 85.56 | NÃO | fora da faixa vertical |
| 537 | 449.00 | 129.00 | 449.91 | 85.56 | NÃO | fora da faixa vertical |
| 538 | 448.00 | 129.00 | 448.93 | 85.56 | NÃO | fora da faixa vertical |
| 539 | 447.00 | 129.00 | 447.95 | 85.56 | NÃO | fora da faixa vertical |
| 540 | 446.00 | 129.00 | 446.96 | 85.56 | NÃO | fora da faixa vertical |
| 541 | 445.00 | 129.00 | 445.98 | 85.56 | NÃO | fora da faixa vertical |
| 542 | 444.00 | 129.00 | 445.00 | 85.56 | NÃO | fora da faixa vertical |
| 543 | 443.00 | 129.00 | 444.02 | 85.56 | NÃO | fora da faixa vertical |
| 544 | 442.00 | 129.00 | 443.04 | 85.56 | NÃO | fora da faixa vertical |
| 545 | 441.00 | 129.00 | 442.05 | 85.56 | NÃO | fora da faixa vertical |
| 546 | 440.00 | 129.00 | 441.07 | 85.56 | NÃO | fora da faixa vertical |
| 547 | 439.00 | 129.00 | 440.09 | 85.56 | NÃO | fora da faixa vertical |
| 548 | 438.00 | 129.00 | 439.11 | 85.56 | NÃO | fora da faixa vertical |
| 549 | 437.00 | 129.00 | 438.13 | 85.56 | NÃO | fora da faixa vertical |
| 550 | 436.00 | 129.00 | 437.15 | 85.56 | NÃO | fora da faixa vertical |
| 551 | 435.00 | 129.00 | 436.17 | 85.56 | NÃO | fora da faixa vertical |
| 552 | 434.00 | 129.00 | 435.18 | 85.56 | NÃO | fora da faixa vertical |
| 553 | 433.00 | 129.00 | 434.20 | 85.56 | NÃO | fora da faixa vertical |
| 554 | 432.00 | 129.00 | 433.22 | 85.56 | NÃO | fora da faixa vertical |
| 555 | 431.00 | 129.00 | 432.24 | 85.56 | NÃO | fora da faixa vertical |
| 556 | 430.00 | 129.00 | 431.26 | 85.56 | NÃO | fora da faixa vertical |
| 557 | 429.00 | 129.00 | 430.28 | 85.56 | NÃO | fora da faixa vertical |
| 558 | 428.00 | 128.00 | 429.50 | 86.56 | NÃO | fora da faixa vertical |
| 559 | 427.00 | 128.00 | 428.51 | 86.56 | NÃO | fora da faixa vertical |
| 560 | 426.00 | 127.00 | 427.73 | 87.56 | NÃO | fora da faixa vertical |
| 561 | 425.00 | 126.00 | 426.96 | 88.56 | NÃO | fora da faixa vertical |
| 562 | 424.00 | 125.00 | 426.18 | 89.56 | NÃO | fora da faixa vertical |
| 563 | 423.00 | 124.00 | 425.41 | 90.56 | NÃO | fora da faixa vertical |
| 564 | 422.00 | 123.00 | 424.65 | 91.56 | NÃO | fora da faixa vertical |
| 565 | 421.00 | 122.00 | 423.88 | 92.56 | NÃO | fora da faixa vertical |
| 566 | 421.00 | 121.00 | 424.10 | 93.56 | NÃO | fora da faixa vertical |
| 567 | 420.00 | 120.00 | 423.34 | 94.56 | NÃO | fora da faixa vertical |
| 568 | 419.00 | 119.00 | 422.59 | 95.56 | NÃO | fora da faixa vertical |
| 569 | 418.00 | 118.00 | 421.84 | 96.56 | NÃO | fora da faixa vertical |
| 570 | 417.00 | 117.00 | 421.09 | 97.56 | NÃO | fora da faixa vertical |
| 571 | 416.00 | 116.00 | 420.35 | 98.56 | NÃO | fora da faixa vertical |
| 572 | 415.00 | 115.00 | 419.60 | 99.56 | NÃO | fora da faixa vertical |
| 573 | 414.00 | 114.00 | 418.87 | 100.56 | NÃO | fora da faixa vertical |
| 574 | 413.00 | 113.00 | 418.13 | 101.56 | NÃO | fora da faixa vertical |
| 575 | 412.00 | 112.00 | 417.40 | 102.56 | NÃO | fora da faixa vertical |
| 576 | 411.00 | 111.00 | 416.68 | 103.56 | NÃO | fora da faixa vertical |
| 577 | 410.00 | 110.00 | 415.95 | 104.56 | NÃO | fora da faixa vertical |
| 578 | 409.00 | 109.00 | 415.23 | 105.56 | NÃO | fora da faixa vertical |
| 579 | 408.00 | 108.00 | 414.52 | 106.56 | NÃO | fora da faixa vertical |
| 580 | 407.00 | 107.00 | 413.81 | 107.56 | NÃO | fora da faixa vertical |
| 581 | 406.00 | 107.00 | 412.84 | 107.56 | NÃO | fora da faixa vertical |
| 582 | 405.00 | 106.00 | 412.13 | 108.56 | NÃO | fora da faixa vertical |
| 583 | 404.00 | 105.00 | 411.43 | 109.56 | NÃO | fora da faixa vertical |
| 584 | 403.00 | 104.00 | 410.73 | 110.56 | NÃO | fora da faixa vertical |
| 585 | 402.00 | 103.00 | 410.03 | 111.56 | NÃO | fora da faixa vertical |
| 586 | 401.00 | 102.00 | 409.34 | 112.56 | NÃO | fora da faixa vertical |
| 587 | 400.00 | 101.00 | 408.65 | 113.56 | NÃO | fora da faixa vertical |
| 588 | 399.00 | 101.00 | 407.69 | 113.56 | NÃO | fora da faixa vertical |
| 589 | 398.00 | 100.00 | 407.00 | 114.56 | NÃO | fora da faixa vertical |
| 590 | 397.00 | 99.00 | 406.32 | 115.56 | NÃO | fora da faixa vertical |
| 591 | 396.00 | 99.00 | 405.36 | 115.56 | NÃO | fora da faixa vertical |
| 592 | 395.00 | 98.00 | 404.68 | 116.56 | NÃO | fora da faixa vertical |
| 593 | 394.00 | 97.00 | 404.01 | 117.56 | NÃO | fora da faixa vertical |
| 594 | 393.00 | 96.00 | 403.34 | 118.56 | NÃO | fora da faixa vertical |
| 595 | 392.00 | 96.00 | 402.39 | 118.56 | NÃO | fora da faixa vertical |
| 596 | 391.00 | 95.00 | 401.72 | 119.56 | NÃO | fora da faixa vertical |
| 597 | 390.00 | 94.00 | 401.06 | 120.56 | NÃO | fora da faixa vertical |
| 598 | 389.00 | 93.00 | 400.40 | 121.56 | NÃO | fora da faixa vertical |
| 599 | 388.00 | 93.00 | 399.45 | 121.56 | NÃO | fora da faixa vertical |
| 600 | 387.00 | 92.00 | 398.80 | 122.56 | NÃO | fora da faixa vertical |
| 601 | 386.00 | 91.00 | 398.15 | 123.56 | NÃO | fora da faixa vertical |
| 602 | 385.00 | 91.00 | 397.20 | 123.56 | NÃO | fora da faixa vertical |
| 603 | 384.00 | 90.00 | 396.56 | 124.56 | NÃO | fora da faixa vertical |
| 604 | 383.00 | 89.00 | 395.92 | 125.56 | NÃO | fora da faixa vertical |
| 605 | 382.00 | 89.00 | 394.97 | 125.56 | NÃO | fora da faixa vertical |
| 606 | 381.00 | 88.00 | 394.34 | 126.56 | NÃO | fora da faixa vertical |
| 607 | 380.00 | 88.00 | 393.39 | 126.56 | NÃO | fora da faixa vertical |
| 608 | 379.00 | 87.00 | 392.76 | 127.56 | NÃO | fora da faixa vertical |
| 609 | 378.00 | 86.00 | 392.14 | 128.56 | NÃO | fora da faixa vertical |
| 610 | 377.00 | 86.00 | 391.19 | 128.56 | NÃO | fora da faixa vertical |
| 611 | 376.00 | 85.00 | 390.57 | 129.56 | NÃO | fora da faixa vertical |
| 612 | 375.00 | 84.00 | 389.96 | 130.56 | NÃO | fora da faixa vertical |
| 613 | 374.00 | 84.00 | 389.01 | 130.56 | NÃO | fora da faixa vertical |
| 614 | 373.00 | 83.00 | 388.40 | 131.56 | NÃO | fora da faixa vertical |
| 615 | 372.00 | 83.00 | 387.46 | 131.56 | NÃO | fora da faixa vertical |
| 616 | 371.00 | 82.00 | 386.86 | 132.56 | NÃO | fora da faixa vertical |
| 617 | 370.00 | 81.00 | 386.26 | 133.56 | NÃO | fora da faixa vertical |
| 618 | 369.00 | 81.00 | 385.32 | 133.56 | NÃO | fora da faixa vertical |
| 619 | 368.00 | 80.00 | 384.72 | 134.56 | NÃO | fora da faixa vertical |
| 620 | 367.00 | 80.00 | 383.78 | 134.56 | NÃO | fora da faixa vertical |
| 621 | 366.00 | 79.00 | 383.19 | 135.56 | NÃO | fora da faixa vertical |
| 622 | 365.00 | 79.00 | 382.26 | 135.56 | NÃO | fora da faixa vertical |
| 623 | 364.00 | 78.00 | 381.67 | 136.56 | NÃO | fora da faixa vertical |
| 624 | 363.00 | 78.00 | 380.74 | 136.56 | NÃO | fora da faixa vertical |
| 625 | 362.00 | 77.00 | 380.16 | 137.56 | NÃO | fora da faixa vertical |
| 626 | 361.00 | 77.00 | 379.23 | 137.56 | NÃO | fora da faixa vertical |
| 627 | 360.00 | 76.00 | 378.65 | 138.56 | NÃO | fora da faixa vertical |
| 628 | 359.00 | 76.00 | 377.72 | 138.56 | NÃO | fora da faixa vertical |
| 629 | 358.00 | 75.00 | 377.15 | 139.56 | NÃO | fora da faixa vertical |
| 630 | 357.00 | 75.00 | 376.22 | 139.56 | NÃO | fora da faixa vertical |
| 631 | 356.00 | 75.00 | 375.29 | 139.56 | NÃO | fora da faixa vertical |
| 632 | 355.00 | 74.00 | 374.73 | 140.56 | NÃO | fora da faixa vertical |
| 633 | 354.00 | 74.00 | 373.80 | 140.56 | NÃO | fora da faixa vertical |
| 634 | 353.00 | 73.00 | 373.25 | 141.56 | NÃO | fora da faixa vertical |
| 635 | 352.00 | 73.00 | 372.32 | 141.56 | NÃO | fora da faixa vertical |
| 636 | 351.00 | 72.00 | 371.78 | 142.56 | NÃO | fora da faixa vertical |
| 637 | 350.00 | 72.00 | 370.85 | 142.56 | NÃO | fora da faixa vertical |
| 638 | 349.00 | 71.00 | 370.31 | 143.56 | NÃO | fora da faixa vertical |
| 639 | 348.00 | 71.00 | 369.38 | 143.56 | NÃO | fora da faixa vertical |
| 640 | 347.00 | 71.00 | 368.46 | 143.56 | NÃO | fora da faixa vertical |
| 641 | 346.00 | 70.00 | 367.93 | 144.56 | NÃO | fora da faixa vertical |
| 642 | 345.00 | 70.00 | 367.01 | 144.56 | NÃO | fora da faixa vertical |
| 643 | 344.00 | 70.00 | 366.08 | 144.56 | NÃO | fora da faixa vertical |
| 644 | 343.00 | 69.00 | 365.56 | 145.56 | NÃO | fora da faixa vertical |
| 645 | 342.00 | 69.00 | 364.64 | 145.56 | NÃO | fora da faixa vertical |
| 646 | 341.00 | 68.00 | 364.12 | 146.56 | NÃO | fora da faixa vertical |
| 647 | 340.00 | 68.00 | 363.20 | 146.56 | NÃO | fora da faixa vertical |
| 648 | 339.00 | 68.00 | 362.28 | 146.56 | NÃO | fora da faixa vertical |
| 649 | 338.00 | 67.00 | 361.77 | 147.56 | NÃO | fora da faixa vertical |
| 650 | 337.00 | 67.00 | 360.85 | 147.56 | NÃO | fora da faixa vertical |
| 651 | 336.00 | 67.00 | 359.94 | 147.56 | NÃO | fora da faixa vertical |
| 652 | 335.00 | 66.00 | 359.43 | 148.56 | NÃO | fora da faixa vertical |
| 653 | 334.00 | 66.00 | 358.52 | 148.56 | NÃO | fora da faixa vertical |
| 654 | 333.00 | 66.00 | 357.61 | 148.56 | NÃO | fora da faixa vertical |
| 655 | 332.00 | 65.00 | 357.11 | 149.56 | NÃO | fora da faixa vertical |
| 656 | 331.00 | 65.00 | 356.20 | 149.56 | NÃO | fora da faixa vertical |
| 657 | 330.00 | 65.00 | 355.29 | 149.56 | NÃO | fora da faixa vertical |
| 658 | 329.00 | 65.00 | 354.38 | 149.56 | NÃO | fora da faixa vertical |
| 659 | 328.00 | 64.00 | 353.90 | 150.56 | NÃO | fora da faixa vertical |
| 660 | 327.00 | 64.00 | 352.99 | 150.56 | NÃO | fora da faixa vertical |
| 661 | 326.00 | 64.00 | 352.08 | 150.56 | NÃO | fora da faixa vertical |
| 662 | 325.00 | 63.00 | 351.60 | 151.56 | NÃO | fora da faixa vertical |
| 663 | 324.00 | 63.00 | 350.70 | 151.56 | NÃO | fora da faixa vertical |
| 664 | 323.00 | 63.00 | 349.79 | 151.56 | NÃO | fora da faixa vertical |
| 665 | 322.00 | 63.00 | 348.89 | 151.56 | NÃO | fora da faixa vertical |
| 666 | 321.00 | 62.00 | 348.42 | 152.56 | NÃO | fora da faixa vertical |
| 667 | 320.00 | 62.00 | 347.52 | 152.56 | NÃO | fora da faixa vertical |
| 668 | 319.00 | 62.00 | 346.62 | 152.56 | NÃO | fora da faixa vertical |
| 669 | 318.00 | 62.00 | 345.72 | 152.56 | NÃO | fora da faixa vertical |
| 670 | 317.00 | 61.00 | 345.26 | 153.56 | NÃO | fora da faixa vertical |
| 671 | 316.00 | 61.00 | 344.36 | 153.56 | NÃO | fora da faixa vertical |
| 672 | 315.00 | 61.00 | 343.46 | 153.56 | NÃO | fora da faixa vertical |
| 673 | 314.00 | 61.00 | 342.57 | 153.56 | NÃO | fora da faixa vertical |
| 674 | 313.00 | 61.00 | 341.67 | 153.56 | NÃO | fora da faixa vertical |
| 675 | 312.00 | 60.00 | 341.22 | 154.56 | NÃO | fora da faixa vertical |
| 676 | 311.00 | 60.00 | 340.33 | 154.56 | NÃO | fora da faixa vertical |
| 677 | 310.00 | 60.00 | 339.44 | 154.56 | NÃO | fora da faixa vertical |
| 678 | 309.00 | 60.00 | 338.55 | 154.56 | NÃO | fora da faixa vertical |
| 679 | 308.00 | 60.00 | 337.65 | 154.56 | NÃO | fora da faixa vertical |
| 680 | 307.00 | 59.00 | 337.22 | 155.56 | NÃO | fora da faixa vertical |
| 681 | 306.00 | 59.00 | 336.33 | 155.56 | NÃO | fora da faixa vertical |
| 682 | 305.00 | 59.00 | 335.44 | 155.56 | NÃO | fora da faixa vertical |
| 683 | 304.00 | 59.00 | 334.55 | 155.56 | NÃO | fora da faixa vertical |
| 684 | 303.00 | 59.00 | 333.66 | 155.56 | NÃO | fora da faixa vertical |
| 685 | 302.00 | 59.00 | 332.78 | 155.56 | NÃO | fora da faixa vertical |
| 686 | 301.00 | 59.00 | 331.89 | 155.56 | NÃO | fora da faixa vertical |
| 687 | 300.00 | 58.00 | 331.47 | 156.56 | NÃO | fora da faixa vertical |
| 688 | 299.00 | 58.00 | 330.59 | 156.56 | NÃO | fora da faixa vertical |
| 689 | 298.00 | 58.00 | 329.71 | 156.56 | NÃO | fora da faixa vertical |
| 690 | 297.00 | 58.00 | 328.82 | 156.56 | NÃO | fora da faixa vertical |
| 691 | 296.00 | 58.00 | 327.94 | 156.56 | NÃO | fora da faixa vertical |
| 692 | 295.00 | 58.00 | 327.06 | 156.56 | NÃO | fora da faixa vertical |
| 693 | 294.00 | 58.00 | 326.18 | 156.56 | NÃO | fora da faixa vertical |
| 694 | 293.00 | 58.00 | 325.30 | 156.56 | NÃO | fora da faixa vertical |
| 695 | 292.00 | 58.00 | 324.42 | 156.56 | NÃO | fora da faixa vertical |
| 696 | 291.00 | 57.00 | 324.02 | 157.56 | NÃO | fora da faixa vertical |
| 697 | 290.00 | 57.00 | 323.15 | 157.56 | NÃO | fora da faixa vertical |
| 698 | 289.00 | 57.00 | 322.27 | 157.56 | NÃO | fora da faixa vertical |
| 699 | 288.00 | 57.00 | 321.40 | 157.56 | NÃO | fora da faixa vertical |
| 700 | 287.00 | 57.00 | 320.52 | 157.56 | NÃO | fora da faixa vertical |
| 701 | 286.00 | 57.00 | 319.65 | 157.56 | NÃO | fora da faixa vertical |
| 702 | 285.00 | 57.00 | 318.78 | 157.56 | NÃO | fora da faixa vertical |
| 703 | 284.00 | 57.00 | 317.91 | 157.56 | NÃO | fora da faixa vertical |
| 704 | 283.00 | 57.00 | 317.04 | 157.56 | NÃO | fora da faixa vertical |
| 705 | 282.00 | 57.00 | 316.17 | 157.56 | NÃO | fora da faixa vertical |
| 706 | 281.00 | 57.00 | 315.30 | 157.56 | NÃO | fora da faixa vertical |
| 707 | 280.00 | 57.00 | 314.43 | 157.56 | NÃO | fora da faixa vertical |
| 708 | 279.00 | 57.00 | 313.56 | 157.56 | NÃO | fora da faixa vertical |
| 709 | 278.00 | 57.00 | 312.69 | 157.56 | NÃO | fora da faixa vertical |
| 710 | 277.00 | 57.00 | 311.83 | 157.56 | NÃO | fora da faixa vertical |
| 711 | 276.00 | 57.00 | 310.96 | 157.56 | NÃO | fora da faixa vertical |
| 712 | 275.00 | 57.00 | 310.10 | 157.56 | NÃO | fora da faixa vertical |
| 713 | 274.00 | 57.00 | 309.23 | 157.56 | NÃO | fora da faixa vertical |
| 714 | 273.00 | 57.00 | 308.37 | 157.56 | NÃO | fora da faixa vertical |
| 715 | 272.00 | 57.00 | 307.51 | 157.56 | NÃO | fora da faixa vertical |
| 716 | 271.00 | 57.00 | 306.65 | 157.56 | NÃO | fora da faixa vertical |
| 717 | 270.00 | 57.00 | 305.79 | 157.56 | NÃO | fora da faixa vertical |
| 718 | 269.00 | 57.00 | 304.93 | 157.56 | NÃO | fora da faixa vertical |
| 719 | 268.00 | 57.00 | 304.07 | 157.56 | NÃO | fora da faixa vertical |
| 720 | 267.00 | 57.00 | 303.21 | 157.56 | NÃO | fora da faixa vertical |
| 721 | 266.00 | 57.00 | 302.35 | 157.56 | NÃO | fora da faixa vertical |
| 722 | 265.00 | 57.00 | 301.50 | 157.56 | NÃO | fora da faixa vertical |
| 723 | 264.00 | 57.00 | 300.64 | 157.56 | NÃO | fora da faixa vertical |
| 724 | 263.00 | 57.00 | 299.79 | 157.56 | NÃO | fora da faixa vertical |
| 725 | 262.00 | 57.00 | 298.93 | 157.56 | NÃO | fora da faixa vertical |
| 726 | 261.00 | 57.00 | 298.08 | 157.56 | NÃO | fora da faixa vertical |
| 727 | 260.00 | 57.00 | 297.23 | 157.56 | NÃO | fora da faixa vertical |
| 728 | 259.00 | 57.00 | 296.38 | 157.56 | NÃO | fora da faixa vertical |
| 729 | 258.00 | 57.00 | 295.53 | 157.56 | NÃO | fora da faixa vertical |
| 730 | 257.00 | 57.00 | 294.68 | 157.56 | NÃO | fora da faixa vertical |
| 731 | 256.00 | 57.00 | 293.83 | 157.56 | NÃO | fora da faixa vertical |
| 732 | 255.00 | 57.00 | 292.98 | 157.56 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 249 | 7.00 | 213.00 | 0.00 | -1.56 |
| 250 | 8.00 | 213.00 | 1.00 | -1.56 |
| 251 | 9.00 | 213.00 | 2.00 | -1.56 |
| 252 | 10.00 | 213.00 | 3.00 | -1.56 |
| 253 | 11.00 | 213.00 | 4.00 | -1.56 |
| 254 | 12.00 | 213.00 | 5.00 | -1.56 |
| 255 | 13.00 | 213.00 | 6.00 | -1.56 |
| 256 | 14.00 | 213.00 | 7.00 | -1.56 |
| 257 | 15.00 | 213.00 | 8.00 | -1.56 |
| 258 | 16.00 | 213.00 | 9.00 | -1.56 |
| 259 | 17.00 | 213.00 | 10.00 | -1.56 |
| 260 | 18.00 | 213.00 | 11.00 | -1.56 |
| 261 | 19.00 | 213.00 | 12.00 | -1.56 |
| 262 | 20.00 | 213.00 | 13.00 | -1.56 |
| 263 | 21.00 | 213.00 | 14.00 | -1.56 |
| 264 | 22.00 | 213.00 | 15.00 | -1.56 |
| 265 | 23.00 | 213.00 | 16.00 | -1.56 |
| 266 | 24.00 | 213.00 | 17.00 | -1.56 |
| 267 | 25.00 | 213.00 | 18.00 | -1.56 |
| 268 | 26.00 | 213.00 | 19.00 | -1.56 |
| 269 | 27.00 | 213.00 | 20.00 | -1.56 |
| 270 | 28.00 | 213.00 | 21.00 | -1.56 |
| 271 | 29.00 | 213.00 | 22.00 | -1.56 |
| 272 | 30.00 | 213.00 | 23.00 | -1.56 |
| 273 | 31.00 | 213.00 | 24.00 | -1.56 |
| 274 | 32.00 | 213.00 | 25.00 | -1.56 |
| 275 | 33.00 | 213.00 | 26.00 | -1.56 |
| 276 | 34.00 | 213.00 | 27.00 | -1.56 |
| 277 | 35.00 | 213.00 | 28.00 | -1.56 |
| 278 | 36.00 | 213.00 | 29.00 | -1.56 |
| 279 | 37.00 | 213.00 | 30.00 | -1.56 |
| 280 | 38.00 | 213.00 | 31.00 | -1.56 |
| 281 | 39.00 | 213.00 | 32.00 | -1.56 |
| 282 | 40.00 | 213.00 | 33.00 | -1.56 |
| 283 | 41.00 | 213.00 | 34.00 | -1.56 |
| 284 | 42.00 | 213.00 | 35.00 | -1.56 |
| 285 | 43.00 | 213.00 | 36.00 | -1.56 |
| 286 | 44.00 | 213.00 | 37.00 | -1.56 |
| 287 | 45.00 | 213.00 | 38.00 | -1.56 |
| 288 | 46.00 | 213.00 | 39.00 | -1.56 |
| 289 | 47.00 | 213.00 | 40.00 | -1.56 |
| 290 | 48.00 | 213.00 | 41.00 | -1.56 |
| 291 | 49.00 | 213.00 | 42.00 | -1.56 |
| 292 | 50.00 | 213.00 | 43.00 | -1.56 |
| 293 | 51.00 | 213.00 | 44.00 | -1.56 |
| 294 | 52.00 | 213.00 | 45.00 | -1.56 |
| 295 | 53.00 | 213.00 | 46.00 | -1.56 |
| 296 | 54.00 | 213.00 | 47.00 | -1.56 |
| 297 | 55.00 | 213.00 | 48.00 | -1.56 |
| 298 | 56.00 | 213.00 | 49.00 | -1.56 |
| 299 | 57.00 | 213.00 | 50.00 | -1.56 |
| 300 | 58.00 | 213.00 | 51.00 | -1.56 |
| 301 | 59.00 | 213.00 | 52.00 | -1.56 |
| 302 | 60.00 | 213.00 | 53.00 | -1.56 |
| 303 | 61.00 | 213.00 | 54.00 | -1.56 |
| 304 | 62.00 | 213.00 | 55.00 | -1.56 |
| 305 | 63.00 | 213.00 | 56.00 | -1.56 |
| 306 | 64.00 | 213.00 | 57.00 | -1.56 |
| 307 | 65.00 | 213.00 | 58.00 | -1.56 |
| 308 | 66.00 | 213.00 | 59.00 | -1.56 |
| 309 | 67.00 | 213.00 | 60.00 | -1.56 |
| 310 | 68.00 | 213.00 | 61.00 | -1.56 |
| 311 | 69.00 | 213.00 | 62.00 | -1.56 |
| 312 | 70.00 | 213.00 | 63.00 | -1.56 |
| 313 | 71.00 | 213.00 | 64.00 | -1.56 |
| 314 | 72.00 | 213.00 | 65.00 | -1.56 |
| 315 | 73.00 | 213.00 | 66.00 | -1.56 |
| 316 | 74.00 | 213.00 | 67.00 | -1.56 |

- primeiro índice: 249
- último índice: 316
- quantidade: 68
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![130_geo esq](audit_outputs/75_geo_esq_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![130_geo esq polyfit](audit_outputs/75_geo_esq_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

### Lado: dir

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 733
- ponto de contato recebido: [520.0, 213.0]
- baseline_y: 213.0
- baseline_ajustada: 214.56
- lado solicitado: dir
- largura da região: 85 px
- altura da gota: 156.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 254.00 | 57.00 | 308.37 | 157.56 | NÃO | fora da faixa vertical |
| 1 | 253.00 | 58.00 | 308.73 | 156.56 | NÃO | fora da faixa vertical |
| 2 | 252.00 | 58.00 | 309.59 | 156.56 | NÃO | fora da faixa vertical |
| 3 | 251.00 | 58.00 | 310.46 | 156.56 | NÃO | fora da faixa vertical |
| 4 | 250.00 | 58.00 | 311.33 | 156.56 | NÃO | fora da faixa vertical |
| 5 | 249.00 | 58.00 | 312.20 | 156.56 | NÃO | fora da faixa vertical |
| 6 | 248.00 | 58.00 | 313.06 | 156.56 | NÃO | fora da faixa vertical |
| 7 | 247.00 | 58.00 | 313.93 | 156.56 | NÃO | fora da faixa vertical |
| 8 | 246.00 | 58.00 | 314.80 | 156.56 | NÃO | fora da faixa vertical |
| 9 | 245.00 | 58.00 | 315.67 | 156.56 | NÃO | fora da faixa vertical |
| 10 | 244.00 | 59.00 | 316.06 | 155.56 | NÃO | fora da faixa vertical |
| 11 | 243.00 | 59.00 | 316.93 | 155.56 | NÃO | fora da faixa vertical |
| 12 | 242.00 | 59.00 | 317.80 | 155.56 | NÃO | fora da faixa vertical |
| 13 | 241.00 | 59.00 | 318.68 | 155.56 | NÃO | fora da faixa vertical |
| 14 | 240.00 | 59.00 | 319.56 | 155.56 | NÃO | fora da faixa vertical |
| 15 | 239.00 | 59.00 | 320.43 | 155.56 | NÃO | fora da faixa vertical |
| 16 | 238.00 | 59.00 | 321.31 | 155.56 | NÃO | fora da faixa vertical |
| 17 | 237.00 | 60.00 | 321.71 | 154.56 | NÃO | fora da faixa vertical |
| 18 | 236.00 | 60.00 | 322.59 | 154.56 | NÃO | fora da faixa vertical |
| 19 | 235.00 | 60.00 | 323.47 | 154.56 | NÃO | fora da faixa vertical |
| 20 | 234.00 | 60.00 | 324.35 | 154.56 | NÃO | fora da faixa vertical |
| 21 | 233.00 | 60.00 | 325.24 | 154.56 | NÃO | fora da faixa vertical |
| 22 | 232.00 | 61.00 | 325.65 | 153.56 | NÃO | fora da faixa vertical |
| 23 | 231.00 | 61.00 | 326.53 | 153.56 | NÃO | fora da faixa vertical |
| 24 | 230.00 | 61.00 | 327.42 | 153.56 | NÃO | fora da faixa vertical |
| 25 | 229.00 | 61.00 | 328.31 | 153.56 | NÃO | fora da faixa vertical |
| 26 | 228.00 | 61.00 | 329.19 | 153.56 | NÃO | fora da faixa vertical |
| 27 | 227.00 | 62.00 | 329.62 | 152.56 | NÃO | fora da faixa vertical |
| 28 | 226.00 | 62.00 | 330.51 | 152.56 | NÃO | fora da faixa vertical |
| 29 | 225.00 | 62.00 | 331.40 | 152.56 | NÃO | fora da faixa vertical |
| 30 | 224.00 | 62.00 | 332.29 | 152.56 | NÃO | fora da faixa vertical |
| 31 | 223.00 | 63.00 | 332.73 | 151.56 | NÃO | fora da faixa vertical |
| 32 | 222.00 | 63.00 | 333.62 | 151.56 | NÃO | fora da faixa vertical |
| 33 | 221.00 | 63.00 | 334.52 | 151.56 | NÃO | fora da faixa vertical |
| 34 | 220.00 | 63.00 | 335.41 | 151.56 | NÃO | fora da faixa vertical |
| 35 | 219.00 | 64.00 | 335.86 | 150.56 | NÃO | fora da faixa vertical |
| 36 | 218.00 | 64.00 | 336.76 | 150.56 | NÃO | fora da faixa vertical |
| 37 | 217.00 | 64.00 | 337.65 | 150.56 | NÃO | fora da faixa vertical |
| 38 | 216.00 | 65.00 | 338.11 | 149.56 | NÃO | fora da faixa vertical |
| 39 | 215.00 | 65.00 | 339.01 | 149.56 | NÃO | fora da faixa vertical |
| 40 | 214.00 | 65.00 | 339.91 | 149.56 | NÃO | fora da faixa vertical |
| 41 | 213.00 | 66.00 | 340.38 | 148.56 | NÃO | fora da faixa vertical |
| 42 | 212.00 | 66.00 | 341.28 | 148.56 | NÃO | fora da faixa vertical |
| 43 | 211.00 | 66.00 | 342.18 | 148.56 | NÃO | fora da faixa vertical |
| 44 | 210.00 | 66.00 | 343.09 | 148.56 | NÃO | fora da faixa vertical |
| 45 | 209.00 | 67.00 | 343.57 | 147.56 | NÃO | fora da faixa vertical |
| 46 | 208.00 | 67.00 | 344.47 | 147.56 | NÃO | fora da faixa vertical |
| 47 | 207.00 | 67.00 | 345.38 | 147.56 | NÃO | fora da faixa vertical |
| 48 | 206.00 | 68.00 | 345.86 | 146.56 | NÃO | fora da faixa vertical |
| 49 | 205.00 | 68.00 | 346.77 | 146.56 | NÃO | fora da faixa vertical |
| 50 | 204.00 | 69.00 | 347.26 | 145.56 | NÃO | fora da faixa vertical |
| 51 | 203.00 | 69.00 | 348.17 | 145.56 | NÃO | fora da faixa vertical |
| 52 | 202.00 | 69.00 | 349.08 | 145.56 | NÃO | fora da faixa vertical |
| 53 | 201.00 | 70.00 | 349.59 | 144.56 | NÃO | fora da faixa vertical |
| 54 | 200.00 | 70.00 | 350.50 | 144.56 | NÃO | fora da faixa vertical |
| 55 | 199.00 | 70.00 | 351.41 | 144.56 | NÃO | fora da faixa vertical |
| 56 | 198.00 | 71.00 | 351.92 | 143.56 | NÃO | fora da faixa vertical |
| 57 | 197.00 | 71.00 | 352.84 | 143.56 | NÃO | fora da faixa vertical |
| 58 | 196.00 | 72.00 | 353.35 | 142.56 | NÃO | fora da faixa vertical |
| 59 | 195.00 | 72.00 | 354.27 | 142.56 | NÃO | fora da faixa vertical |
| 60 | 194.00 | 72.00 | 355.19 | 142.56 | NÃO | fora da faixa vertical |
| 61 | 193.00 | 73.00 | 355.71 | 141.56 | NÃO | fora da faixa vertical |
| 62 | 192.00 | 73.00 | 356.63 | 141.56 | NÃO | fora da faixa vertical |
| 63 | 191.00 | 74.00 | 357.16 | 140.56 | NÃO | fora da faixa vertical |
| 64 | 190.00 | 74.00 | 358.08 | 140.56 | NÃO | fora da faixa vertical |
| 65 | 189.00 | 75.00 | 358.62 | 139.56 | NÃO | fora da faixa vertical |
| 66 | 188.00 | 75.00 | 359.54 | 139.56 | NÃO | fora da faixa vertical |
| 67 | 187.00 | 76.00 | 360.08 | 138.56 | NÃO | fora da faixa vertical |
| 68 | 186.00 | 76.00 | 361.01 | 138.56 | NÃO | fora da faixa vertical |
| 69 | 185.00 | 77.00 | 361.55 | 137.56 | NÃO | fora da faixa vertical |
| 70 | 184.00 | 77.00 | 362.48 | 137.56 | NÃO | fora da faixa vertical |
| 71 | 183.00 | 78.00 | 363.03 | 136.56 | NÃO | fora da faixa vertical |
| 72 | 182.00 | 78.00 | 363.96 | 136.56 | NÃO | fora da faixa vertical |
| 73 | 181.00 | 78.00 | 364.89 | 136.56 | NÃO | fora da faixa vertical |
| 74 | 180.00 | 79.00 | 365.45 | 135.56 | NÃO | fora da faixa vertical |
| 75 | 179.00 | 79.00 | 366.38 | 135.56 | NÃO | fora da faixa vertical |
| 76 | 178.00 | 80.00 | 366.95 | 134.56 | NÃO | fora da faixa vertical |
| 77 | 177.00 | 80.00 | 367.88 | 134.56 | NÃO | fora da faixa vertical |
| 78 | 176.00 | 81.00 | 368.46 | 133.56 | NÃO | fora da faixa vertical |
| 79 | 175.00 | 81.00 | 369.39 | 133.56 | NÃO | fora da faixa vertical |
| 80 | 174.00 | 82.00 | 369.97 | 132.56 | NÃO | fora da faixa vertical |
| 81 | 173.00 | 83.00 | 370.55 | 131.56 | NÃO | fora da faixa vertical |
| 82 | 172.00 | 83.00 | 371.49 | 131.56 | NÃO | fora da faixa vertical |
| 83 | 171.00 | 84.00 | 372.08 | 130.56 | NÃO | fora da faixa vertical |
| 84 | 170.00 | 85.00 | 372.67 | 129.56 | NÃO | fora da faixa vertical |
| 85 | 169.00 | 85.00 | 373.61 | 129.56 | NÃO | fora da faixa vertical |
| 86 | 168.00 | 86.00 | 374.21 | 128.56 | NÃO | fora da faixa vertical |
| 87 | 167.00 | 86.00 | 375.15 | 128.56 | NÃO | fora da faixa vertical |
| 88 | 166.00 | 87.00 | 375.76 | 127.56 | NÃO | fora da faixa vertical |
| 89 | 165.00 | 88.00 | 376.36 | 126.56 | NÃO | fora da faixa vertical |
| 90 | 164.00 | 88.00 | 377.31 | 126.56 | NÃO | fora da faixa vertical |
| 91 | 163.00 | 89.00 | 377.92 | 125.56 | NÃO | fora da faixa vertical |
| 92 | 162.00 | 89.00 | 378.87 | 125.56 | NÃO | fora da faixa vertical |
| 93 | 161.00 | 90.00 | 379.49 | 124.56 | NÃO | fora da faixa vertical |
| 94 | 160.00 | 91.00 | 380.11 | 123.56 | NÃO | fora da faixa vertical |
| 95 | 159.00 | 91.00 | 381.06 | 123.56 | NÃO | fora da faixa vertical |
| 96 | 158.00 | 92.00 | 381.69 | 122.56 | NÃO | fora da faixa vertical |
| 97 | 157.00 | 93.00 | 382.32 | 121.56 | NÃO | fora da faixa vertical |
| 98 | 156.00 | 93.00 | 383.27 | 121.56 | NÃO | fora da faixa vertical |
| 99 | 155.00 | 94.00 | 383.91 | 120.56 | NÃO | fora da faixa vertical |
| 100 | 154.00 | 95.00 | 384.55 | 119.56 | NÃO | fora da faixa vertical |
| 101 | 153.00 | 96.00 | 385.20 | 118.56 | NÃO | fora da faixa vertical |
| 102 | 152.00 | 96.00 | 386.15 | 118.56 | NÃO | fora da faixa vertical |
| 103 | 151.00 | 97.00 | 386.80 | 117.56 | NÃO | fora da faixa vertical |
| 104 | 150.00 | 98.00 | 387.46 | 116.56 | NÃO | fora da faixa vertical |
| 105 | 149.00 | 99.00 | 388.12 | 115.56 | NÃO | fora da faixa vertical |
| 106 | 148.00 | 99.00 | 389.08 | 115.56 | NÃO | fora da faixa vertical |
| 107 | 147.00 | 100.00 | 389.74 | 114.56 | NÃO | fora da faixa vertical |
| 108 | 146.00 | 101.00 | 390.41 | 113.56 | NÃO | fora da faixa vertical |
| 109 | 145.00 | 102.00 | 391.08 | 112.56 | NÃO | fora da faixa vertical |
| 110 | 144.00 | 102.00 | 392.04 | 112.56 | NÃO | fora da faixa vertical |
| 111 | 143.00 | 103.00 | 392.72 | 111.56 | NÃO | fora da faixa vertical |
| 112 | 142.00 | 104.00 | 393.40 | 110.56 | NÃO | fora da faixa vertical |
| 113 | 141.00 | 105.00 | 394.09 | 109.56 | NÃO | fora da faixa vertical |
| 114 | 140.00 | 106.00 | 394.78 | 108.56 | NÃO | fora da faixa vertical |
| 115 | 139.00 | 107.00 | 395.47 | 107.56 | NÃO | fora da faixa vertical |
| 116 | 138.00 | 108.00 | 396.17 | 106.56 | NÃO | fora da faixa vertical |
| 117 | 137.00 | 109.00 | 396.87 | 105.56 | NÃO | fora da faixa vertical |
| 118 | 136.00 | 109.00 | 397.83 | 105.56 | NÃO | fora da faixa vertical |
| 119 | 135.00 | 110.00 | 398.54 | 104.56 | NÃO | fora da faixa vertical |
| 120 | 134.00 | 111.00 | 399.25 | 103.56 | NÃO | fora da faixa vertical |
| 121 | 133.00 | 112.00 | 399.96 | 102.56 | NÃO | fora da faixa vertical |
| 122 | 132.00 | 113.00 | 400.68 | 101.56 | NÃO | fora da faixa vertical |
| 123 | 131.00 | 114.00 | 401.40 | 100.56 | NÃO | fora da faixa vertical |
| 124 | 130.00 | 115.00 | 402.12 | 99.56 | NÃO | fora da faixa vertical |
| 125 | 129.00 | 116.00 | 402.85 | 98.56 | NÃO | fora da faixa vertical |
| 126 | 128.00 | 117.00 | 403.58 | 97.56 | NÃO | fora da faixa vertical |
| 127 | 127.00 | 118.00 | 404.32 | 96.56 | NÃO | fora da faixa vertical |
| 128 | 126.00 | 119.00 | 405.06 | 95.56 | NÃO | fora da faixa vertical |
| 129 | 126.00 | 120.00 | 404.83 | 94.56 | NÃO | fora da faixa vertical |
| 130 | 125.00 | 121.00 | 405.57 | 93.56 | NÃO | fora da faixa vertical |
| 131 | 124.00 | 122.00 | 406.32 | 92.56 | NÃO | fora da faixa vertical |
| 132 | 123.00 | 123.00 | 407.07 | 91.56 | NÃO | fora da faixa vertical |
| 133 | 122.00 | 124.00 | 407.83 | 90.56 | NÃO | fora da faixa vertical |
| 134 | 121.00 | 125.00 | 408.59 | 89.56 | NÃO | fora da faixa vertical |
| 135 | 120.00 | 126.00 | 409.35 | 88.56 | NÃO | fora da faixa vertical |
| 136 | 119.00 | 127.00 | 410.12 | 87.56 | NÃO | fora da faixa vertical |
| 137 | 118.00 | 128.00 | 410.89 | 86.56 | NÃO | fora da faixa vertical |
| 138 | 117.00 | 128.00 | 411.87 | 86.56 | NÃO | fora da faixa vertical |
| 139 | 116.00 | 129.00 | 412.64 | 85.56 | NÃO | fora da faixa vertical |
| 140 | 115.00 | 129.00 | 413.62 | 85.56 | NÃO | fora da faixa vertical |
| 141 | 114.00 | 129.00 | 414.60 | 85.56 | NÃO | fora da faixa vertical |
| 142 | 113.00 | 129.00 | 415.58 | 85.56 | NÃO | fora da faixa vertical |
| 143 | 112.00 | 129.00 | 416.56 | 85.56 | NÃO | fora da faixa vertical |
| 144 | 111.00 | 129.00 | 417.54 | 85.56 | NÃO | fora da faixa vertical |
| 145 | 110.00 | 129.00 | 418.52 | 85.56 | NÃO | fora da faixa vertical |
| 146 | 109.00 | 129.00 | 419.50 | 85.56 | NÃO | fora da faixa vertical |
| 147 | 108.00 | 129.00 | 420.48 | 85.56 | NÃO | fora da faixa vertical |
| 148 | 107.00 | 129.00 | 421.46 | 85.56 | NÃO | fora da faixa vertical |
| 149 | 106.00 | 129.00 | 422.44 | 85.56 | NÃO | fora da faixa vertical |
| 150 | 105.00 | 129.00 | 423.42 | 85.56 | NÃO | fora da faixa vertical |
| 151 | 104.00 | 129.00 | 424.40 | 85.56 | NÃO | fora da faixa vertical |
| 152 | 103.00 | 129.00 | 425.38 | 85.56 | NÃO | fora da faixa vertical |
| 153 | 102.00 | 129.00 | 426.36 | 85.56 | NÃO | fora da faixa vertical |
| 154 | 101.00 | 129.00 | 427.34 | 85.56 | NÃO | fora da faixa vertical |
| 155 | 100.00 | 129.00 | 428.32 | 85.56 | NÃO | fora da faixa vertical |
| 156 | 99.00 | 129.00 | 429.30 | 85.56 | NÃO | fora da faixa vertical |
| 157 | 98.00 | 129.00 | 430.28 | 85.56 | NÃO | fora da faixa vertical |
| 158 | 97.00 | 129.00 | 431.26 | 85.56 | NÃO | fora da faixa vertical |
| 159 | 96.00 | 129.00 | 432.24 | 85.56 | NÃO | fora da faixa vertical |
| 160 | 95.00 | 129.00 | 433.22 | 85.56 | NÃO | fora da faixa vertical |
| 161 | 94.00 | 129.00 | 434.20 | 85.56 | NÃO | fora da faixa vertical |
| 162 | 93.00 | 129.00 | 435.18 | 85.56 | NÃO | fora da faixa vertical |
| 163 | 92.00 | 129.00 | 436.17 | 85.56 | NÃO | fora da faixa vertical |
| 164 | 91.00 | 129.00 | 437.15 | 85.56 | NÃO | fora da faixa vertical |
| 165 | 90.00 | 129.00 | 438.13 | 85.56 | NÃO | fora da faixa vertical |
| 166 | 89.00 | 129.00 | 439.11 | 85.56 | NÃO | fora da faixa vertical |
| 167 | 88.00 | 129.00 | 440.09 | 85.56 | NÃO | fora da faixa vertical |
| 168 | 87.00 | 129.00 | 441.07 | 85.56 | NÃO | fora da faixa vertical |
| 169 | 86.00 | 129.00 | 442.05 | 85.56 | NÃO | fora da faixa vertical |
| 170 | 85.00 | 129.00 | 443.04 | 85.56 | NÃO | fora da faixa vertical |
| 171 | 84.00 | 129.00 | 444.02 | 85.56 | NÃO | fora da faixa vertical |
| 172 | 83.00 | 129.00 | 445.00 | 85.56 | NÃO | fora da faixa vertical |
| 173 | 82.00 | 129.00 | 445.98 | 85.56 | NÃO | fora da faixa vertical |
| 174 | 81.00 | 129.00 | 446.96 | 85.56 | NÃO | fora da faixa vertical |
| 175 | 80.00 | 129.00 | 447.95 | 85.56 | NÃO | fora da faixa vertical |
| 176 | 79.00 | 129.00 | 448.93 | 85.56 | NÃO | fora da faixa vertical |
| 177 | 78.00 | 129.00 | 449.91 | 85.56 | NÃO | fora da faixa vertical |
| 178 | 77.00 | 129.00 | 450.89 | 85.56 | NÃO | fora da faixa vertical |
| 179 | 76.00 | 129.00 | 451.88 | 85.56 | NÃO | fora da faixa vertical |
| 180 | 75.00 | 129.00 | 452.86 | 85.56 | NÃO | fora da faixa vertical |
| 181 | 74.00 | 129.00 | 453.84 | 85.56 | NÃO | fora da faixa vertical |
| 182 | 73.00 | 129.00 | 454.82 | 85.56 | NÃO | fora da faixa vertical |
| 183 | 72.00 | 129.00 | 455.81 | 85.56 | NÃO | fora da faixa vertical |
| 184 | 71.00 | 129.00 | 456.79 | 85.56 | NÃO | fora da faixa vertical |
| 185 | 70.00 | 129.00 | 457.77 | 85.56 | NÃO | fora da faixa vertical |
| 186 | 69.00 | 129.00 | 458.76 | 85.56 | NÃO | fora da faixa vertical |
| 187 | 68.00 | 129.00 | 459.74 | 85.56 | NÃO | fora da faixa vertical |
| 188 | 67.00 | 129.00 | 460.72 | 85.56 | NÃO | fora da faixa vertical |
| 189 | 66.00 | 129.00 | 461.71 | 85.56 | NÃO | fora da faixa vertical |
| 190 | 65.00 | 129.00 | 462.69 | 85.56 | NÃO | fora da faixa vertical |
| 191 | 64.00 | 129.00 | 463.67 | 85.56 | NÃO | fora da faixa vertical |
| 192 | 63.00 | 129.00 | 464.66 | 85.56 | NÃO | fora da faixa vertical |
| 193 | 62.00 | 129.00 | 465.64 | 85.56 | NÃO | fora da faixa vertical |
| 194 | 61.00 | 129.00 | 466.62 | 85.56 | NÃO | fora da faixa vertical |
| 195 | 60.00 | 129.00 | 467.61 | 85.56 | NÃO | fora da faixa vertical |
| 196 | 59.00 | 129.00 | 468.59 | 85.56 | NÃO | fora da faixa vertical |
| 197 | 58.00 | 129.00 | 469.57 | 85.56 | NÃO | fora da faixa vertical |
| 198 | 57.00 | 129.00 | 470.56 | 85.56 | NÃO | fora da faixa vertical |
| 199 | 56.00 | 129.00 | 471.54 | 85.56 | NÃO | fora da faixa vertical |
| 200 | 55.00 | 129.00 | 472.53 | 85.56 | NÃO | fora da faixa vertical |
| 201 | 54.00 | 129.00 | 473.51 | 85.56 | NÃO | fora da faixa vertical |
| 202 | 53.00 | 129.00 | 474.49 | 85.56 | NÃO | fora da faixa vertical |
| 203 | 52.00 | 129.00 | 475.48 | 85.56 | NÃO | fora da faixa vertical |
| 204 | 51.00 | 129.00 | 476.46 | 85.56 | NÃO | fora da faixa vertical |
| 205 | 50.00 | 129.00 | 477.45 | 85.56 | NÃO | fora da faixa vertical |
| 206 | 49.00 | 129.00 | 478.43 | 85.56 | NÃO | fora da faixa vertical |
| 207 | 48.00 | 129.00 | 479.42 | 85.56 | NÃO | fora da faixa vertical |
| 208 | 47.00 | 129.00 | 480.40 | 85.56 | NÃO | fora da faixa vertical |
| 209 | 46.00 | 129.00 | 481.39 | 85.56 | NÃO | fora da faixa vertical |
| 210 | 45.00 | 129.00 | 482.37 | 85.56 | NÃO | fora da faixa vertical |
| 211 | 44.00 | 129.00 | 483.35 | 85.56 | NÃO | fora da faixa vertical |
| 212 | 43.00 | 129.00 | 484.34 | 85.56 | NÃO | fora da faixa vertical |
| 213 | 42.00 | 129.00 | 485.32 | 85.56 | NÃO | fora da faixa vertical |
| 214 | 41.00 | 129.00 | 486.31 | 85.56 | NÃO | fora da faixa vertical |
| 215 | 40.00 | 129.00 | 487.29 | 85.56 | NÃO | fora da faixa vertical |
| 216 | 39.00 | 129.00 | 488.28 | 85.56 | NÃO | fora da faixa vertical |
| 217 | 38.00 | 129.00 | 489.26 | 85.56 | NÃO | fora da faixa vertical |
| 218 | 37.00 | 129.00 | 490.25 | 85.56 | NÃO | fora da faixa vertical |
| 219 | 36.00 | 129.00 | 491.24 | 85.56 | NÃO | fora da faixa vertical |
| 220 | 35.00 | 129.00 | 492.22 | 85.56 | NÃO | fora da faixa vertical |
| 221 | 34.00 | 129.00 | 493.21 | 85.56 | NÃO | fora da faixa vertical |
| 222 | 33.00 | 129.00 | 494.19 | 85.56 | NÃO | fora da faixa vertical |
| 223 | 32.00 | 129.00 | 495.18 | 85.56 | NÃO | fora da faixa vertical |
| 224 | 31.00 | 129.00 | 496.16 | 85.56 | NÃO | fora da faixa vertical |
| 225 | 30.00 | 129.00 | 497.15 | 85.56 | NÃO | fora da faixa vertical |
| 226 | 29.00 | 129.00 | 498.13 | 85.56 | NÃO | fora da faixa vertical |
| 227 | 28.00 | 129.00 | 499.12 | 85.56 | NÃO | fora da faixa vertical |
| 228 | 27.00 | 129.00 | 500.10 | 85.56 | NÃO | fora da faixa vertical |
| 229 | 26.00 | 129.00 | 501.09 | 85.56 | NÃO | fora da faixa vertical |
| 230 | 25.00 | 129.00 | 502.08 | 85.56 | NÃO | fora da faixa vertical |
| 231 | 24.00 | 129.00 | 503.06 | 85.56 | NÃO | fora da faixa vertical |
| 232 | 23.00 | 129.00 | 504.05 | 85.56 | NÃO | fora da faixa vertical |
| 233 | 22.00 | 129.00 | 505.03 | 85.56 | NÃO | fora da faixa vertical |
| 234 | 21.00 | 129.00 | 506.02 | 85.56 | NÃO | fora da faixa vertical |
| 235 | 20.00 | 129.00 | 507.01 | 85.56 | NÃO | fora da faixa vertical |
| 236 | 19.00 | 129.00 | 507.99 | 85.56 | NÃO | fora da faixa vertical |
| 237 | 18.00 | 129.00 | 508.98 | 85.56 | NÃO | fora da faixa vertical |
| 238 | 17.00 | 129.00 | 509.97 | 85.56 | NÃO | fora da faixa vertical |
| 239 | 16.00 | 129.00 | 510.95 | 85.56 | NÃO | fora da faixa vertical |
| 240 | 15.00 | 129.00 | 511.94 | 85.56 | NÃO | fora da faixa vertical |
| 241 | 14.00 | 129.00 | 512.92 | 85.56 | NÃO | fora da faixa vertical |
| 242 | 13.00 | 129.00 | 513.91 | 85.56 | NÃO | fora da faixa vertical |
| 243 | 12.00 | 129.00 | 514.90 | 85.56 | NÃO | fora da faixa vertical |
| 244 | 11.00 | 129.00 | 515.88 | 85.56 | NÃO | fora da faixa vertical |
| 245 | 10.00 | 129.00 | 516.87 | 85.56 | NÃO | fora da faixa vertical |
| 246 | 9.00 | 129.00 | 517.86 | 85.56 | NÃO | fora da faixa vertical |
| 247 | 8.00 | 129.00 | 518.84 | 85.56 | NÃO | fora da faixa vertical |
| 248 | 7.00 | 129.00 | 519.83 | 85.56 | NÃO | fora da faixa vertical |
| 249 | 7.00 | 213.00 | 513.00 | 1.56 | NÃO | fora do lado solicitado |
| 250 | 8.00 | 213.00 | 512.00 | 1.56 | NÃO | fora do lado solicitado |
| 251 | 9.00 | 213.00 | 511.00 | 1.56 | NÃO | fora do lado solicitado |
| 252 | 10.00 | 213.00 | 510.00 | 1.56 | NÃO | fora do lado solicitado |
| 253 | 11.00 | 213.00 | 509.00 | 1.56 | NÃO | fora do lado solicitado |
| 254 | 12.00 | 213.00 | 508.00 | 1.56 | NÃO | fora do lado solicitado |
| 255 | 13.00 | 213.00 | 507.00 | 1.56 | NÃO | fora do lado solicitado |
| 256 | 14.00 | 213.00 | 506.00 | 1.56 | NÃO | fora do lado solicitado |
| 257 | 15.00 | 213.00 | 505.00 | 1.56 | NÃO | fora do lado solicitado |
| 258 | 16.00 | 213.00 | 504.00 | 1.56 | NÃO | fora do lado solicitado |
| 259 | 17.00 | 213.00 | 503.00 | 1.56 | NÃO | fora do lado solicitado |
| 260 | 18.00 | 213.00 | 502.00 | 1.56 | NÃO | fora do lado solicitado |
| 261 | 19.00 | 213.00 | 501.00 | 1.56 | NÃO | fora do lado solicitado |
| 262 | 20.00 | 213.00 | 500.00 | 1.56 | NÃO | fora do lado solicitado |
| 263 | 21.00 | 213.00 | 499.00 | 1.56 | NÃO | fora do lado solicitado |
| 264 | 22.00 | 213.00 | 498.00 | 1.56 | NÃO | fora do lado solicitado |
| 265 | 23.00 | 213.00 | 497.00 | 1.56 | NÃO | fora do lado solicitado |
| 266 | 24.00 | 213.00 | 496.00 | 1.56 | NÃO | fora do lado solicitado |
| 267 | 25.00 | 213.00 | 495.00 | 1.56 | NÃO | fora do lado solicitado |
| 268 | 26.00 | 213.00 | 494.00 | 1.56 | NÃO | fora do lado solicitado |
| 269 | 27.00 | 213.00 | 493.00 | 1.56 | NÃO | fora do lado solicitado |
| 270 | 28.00 | 213.00 | 492.00 | 1.56 | NÃO | fora do lado solicitado |
| 271 | 29.00 | 213.00 | 491.00 | 1.56 | NÃO | fora do lado solicitado |
| 272 | 30.00 | 213.00 | 490.00 | 1.56 | NÃO | fora do lado solicitado |
| 273 | 31.00 | 213.00 | 489.00 | 1.56 | NÃO | fora do lado solicitado |
| 274 | 32.00 | 213.00 | 488.00 | 1.56 | NÃO | fora do lado solicitado |
| 275 | 33.00 | 213.00 | 487.00 | 1.56 | NÃO | fora do lado solicitado |
| 276 | 34.00 | 213.00 | 486.00 | 1.56 | NÃO | fora do lado solicitado |
| 277 | 35.00 | 213.00 | 485.00 | 1.56 | NÃO | fora do lado solicitado |
| 278 | 36.00 | 213.00 | 484.00 | 1.56 | NÃO | fora do lado solicitado |
| 279 | 37.00 | 213.00 | 483.00 | 1.56 | NÃO | fora do lado solicitado |
| 280 | 38.00 | 213.00 | 482.00 | 1.56 | NÃO | fora do lado solicitado |
| 281 | 39.00 | 213.00 | 481.00 | 1.56 | NÃO | fora do lado solicitado |
| 282 | 40.00 | 213.00 | 480.00 | 1.56 | NÃO | fora do lado solicitado |
| 283 | 41.00 | 213.00 | 479.00 | 1.56 | NÃO | fora do lado solicitado |
| 284 | 42.00 | 213.00 | 478.00 | 1.56 | NÃO | fora do lado solicitado |
| 285 | 43.00 | 213.00 | 477.00 | 1.56 | NÃO | fora do lado solicitado |
| 286 | 44.00 | 213.00 | 476.00 | 1.56 | NÃO | fora do lado solicitado |
| 287 | 45.00 | 213.00 | 475.00 | 1.56 | NÃO | fora do lado solicitado |
| 288 | 46.00 | 213.00 | 474.00 | 1.56 | NÃO | fora do lado solicitado |
| 289 | 47.00 | 213.00 | 473.00 | 1.56 | NÃO | fora do lado solicitado |
| 290 | 48.00 | 213.00 | 472.00 | 1.56 | NÃO | fora do lado solicitado |
| 291 | 49.00 | 213.00 | 471.00 | 1.56 | NÃO | fora do lado solicitado |
| 292 | 50.00 | 213.00 | 470.00 | 1.56 | NÃO | fora do lado solicitado |
| 293 | 51.00 | 213.00 | 469.00 | 1.56 | NÃO | fora do lado solicitado |
| 294 | 52.00 | 213.00 | 468.00 | 1.56 | NÃO | fora do lado solicitado |
| 295 | 53.00 | 213.00 | 467.00 | 1.56 | NÃO | fora do lado solicitado |
| 296 | 54.00 | 213.00 | 466.00 | 1.56 | NÃO | fora do lado solicitado |
| 297 | 55.00 | 213.00 | 465.00 | 1.56 | NÃO | fora do lado solicitado |
| 298 | 56.00 | 213.00 | 464.00 | 1.56 | NÃO | fora do lado solicitado |
| 299 | 57.00 | 213.00 | 463.00 | 1.56 | NÃO | fora do lado solicitado |
| 300 | 58.00 | 213.00 | 462.00 | 1.56 | NÃO | fora do lado solicitado |
| 301 | 59.00 | 213.00 | 461.00 | 1.56 | NÃO | fora do lado solicitado |
| 302 | 60.00 | 213.00 | 460.00 | 1.56 | NÃO | fora do lado solicitado |
| 303 | 61.00 | 213.00 | 459.00 | 1.56 | NÃO | fora do lado solicitado |
| 304 | 62.00 | 213.00 | 458.00 | 1.56 | NÃO | fora do lado solicitado |
| 305 | 63.00 | 213.00 | 457.00 | 1.56 | NÃO | fora do lado solicitado |
| 306 | 64.00 | 213.00 | 456.00 | 1.56 | NÃO | fora do lado solicitado |
| 307 | 65.00 | 213.00 | 455.00 | 1.56 | NÃO | fora do lado solicitado |
| 308 | 66.00 | 213.00 | 454.00 | 1.56 | NÃO | fora do lado solicitado |
| 309 | 67.00 | 213.00 | 453.00 | 1.56 | NÃO | fora do lado solicitado |
| 310 | 68.00 | 213.00 | 452.00 | 1.56 | NÃO | fora do lado solicitado |
| 311 | 69.00 | 213.00 | 451.00 | 1.56 | NÃO | fora do lado solicitado |
| 312 | 70.00 | 213.00 | 450.00 | 1.56 | NÃO | fora do lado solicitado |
| 313 | 71.00 | 213.00 | 449.00 | 1.56 | NÃO | fora do lado solicitado |
| 314 | 72.00 | 213.00 | 448.00 | 1.56 | NÃO | fora do lado solicitado |
| 315 | 73.00 | 213.00 | 447.00 | 1.56 | NÃO | fora do lado solicitado |
| 316 | 74.00 | 213.00 | 446.00 | 1.56 | NÃO | fora do lado solicitado |
| 317 | 455.00 | 213.00 | 65.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 318 | 456.00 | 213.00 | 64.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 319 | 457.00 | 213.00 | 63.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 320 | 458.00 | 213.00 | 62.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 321 | 459.00 | 213.00 | 61.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 322 | 460.00 | 213.00 | 60.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 323 | 461.00 | 213.00 | 59.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 324 | 462.00 | 213.00 | 58.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 325 | 463.00 | 213.00 | 57.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 326 | 464.00 | 213.00 | 56.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 327 | 465.00 | 213.00 | 55.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 328 | 466.00 | 213.00 | 54.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 329 | 467.00 | 213.00 | 53.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 330 | 468.00 | 213.00 | 52.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 331 | 469.00 | 213.00 | 51.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 332 | 470.00 | 213.00 | 50.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 333 | 471.00 | 213.00 | 49.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 334 | 472.00 | 213.00 | 48.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 335 | 473.00 | 213.00 | 47.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 336 | 474.00 | 213.00 | 46.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 337 | 475.00 | 213.00 | 45.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 338 | 476.00 | 213.00 | 44.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 339 | 477.00 | 213.00 | 43.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 340 | 478.00 | 213.00 | 42.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 341 | 479.00 | 213.00 | 41.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 342 | 480.00 | 213.00 | 40.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 343 | 481.00 | 213.00 | 39.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 344 | 482.00 | 213.00 | 38.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 345 | 483.00 | 213.00 | 37.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 346 | 484.00 | 213.00 | 36.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 347 | 485.00 | 213.00 | 35.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 348 | 486.00 | 213.00 | 34.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 349 | 487.00 | 213.00 | 33.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 350 | 488.00 | 213.00 | 32.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 351 | 489.00 | 213.00 | 31.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 352 | 490.00 | 213.00 | 30.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 353 | 491.00 | 213.00 | 29.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 354 | 492.00 | 213.00 | 28.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 355 | 493.00 | 213.00 | 27.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 356 | 494.00 | 213.00 | 26.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 357 | 495.00 | 213.00 | 25.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 358 | 496.00 | 213.00 | 24.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 359 | 497.00 | 213.00 | 23.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 360 | 498.00 | 213.00 | 22.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 361 | 499.00 | 213.00 | 21.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 362 | 500.00 | 213.00 | 20.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 363 | 501.00 | 213.00 | 19.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 364 | 502.00 | 213.00 | 18.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 365 | 503.00 | 213.00 | 17.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 366 | 504.00 | 213.00 | 16.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 367 | 505.00 | 213.00 | 15.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 368 | 506.00 | 213.00 | 14.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 369 | 507.00 | 213.00 | 13.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 370 | 508.00 | 213.00 | 12.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 371 | 509.00 | 213.00 | 11.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 372 | 510.00 | 213.00 | 10.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 373 | 511.00 | 213.00 | 9.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 374 | 512.00 | 213.00 | 8.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 375 | 513.00 | 213.00 | 7.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 376 | 514.00 | 213.00 | 6.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 377 | 515.00 | 213.00 | 5.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 378 | 516.00 | 213.00 | 4.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 379 | 517.00 | 213.00 | 3.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 380 | 518.00 | 213.00 | 2.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 381 | 519.00 | 213.00 | 1.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 382 | 520.00 | 213.00 | 0.00 | 1.56 | SIM | dentro da janela vertical e do lado solicitado |
| 383 | 520.00 | 212.00 | 1.00 | 2.56 | SIM | dentro da janela vertical e do lado solicitado |
| 384 | 520.00 | 211.00 | 2.00 | 3.56 | SIM | dentro da janela vertical e do lado solicitado |
| 385 | 520.00 | 210.00 | 3.00 | 4.56 | SIM | dentro da janela vertical e do lado solicitado |
| 386 | 520.00 | 209.00 | 4.00 | 5.56 | SIM | dentro da janela vertical e do lado solicitado |
| 387 | 520.00 | 208.00 | 5.00 | 6.56 | SIM | dentro da janela vertical e do lado solicitado |
| 388 | 520.00 | 207.00 | 6.00 | 7.56 | SIM | dentro da janela vertical e do lado solicitado |
| 389 | 520.00 | 206.00 | 7.00 | 8.56 | SIM | dentro da janela vertical e do lado solicitado |
| 390 | 520.00 | 205.00 | 8.00 | 9.56 | SIM | dentro da janela vertical e do lado solicitado |
| 391 | 520.00 | 204.00 | 9.00 | 10.56 | SIM | dentro da janela vertical e do lado solicitado |
| 392 | 520.00 | 203.00 | 10.00 | 11.56 | SIM | dentro da janela vertical e do lado solicitado |
| 393 | 520.00 | 202.00 | 11.00 | 12.56 | SIM | dentro da janela vertical e do lado solicitado |
| 394 | 520.00 | 201.00 | 12.00 | 13.56 | SIM | dentro da janela vertical e do lado solicitado |
| 395 | 520.00 | 200.00 | 13.00 | 14.56 | SIM | dentro da janela vertical e do lado solicitado |
| 396 | 520.00 | 199.00 | 14.00 | 15.56 | SIM | dentro da janela vertical e do lado solicitado |
| 397 | 520.00 | 198.00 | 15.00 | 16.56 | SIM | dentro da janela vertical e do lado solicitado |
| 398 | 520.00 | 197.00 | 16.00 | 17.56 | SIM | dentro da janela vertical e do lado solicitado |
| 399 | 520.00 | 196.00 | 17.00 | 18.56 | SIM | dentro da janela vertical e do lado solicitado |
| 400 | 520.00 | 195.00 | 18.00 | 19.56 | SIM | dentro da janela vertical e do lado solicitado |
| 401 | 520.00 | 194.00 | 19.00 | 20.56 | SIM | dentro da janela vertical e do lado solicitado |
| 402 | 520.00 | 193.00 | 20.00 | 21.56 | SIM | dentro da janela vertical e do lado solicitado |
| 403 | 520.00 | 192.00 | 21.00 | 22.56 | SIM | dentro da janela vertical e do lado solicitado |
| 404 | 520.00 | 191.00 | 22.00 | 23.56 | SIM | dentro da janela vertical e do lado solicitado |
| 405 | 520.00 | 190.00 | 23.00 | 24.56 | SIM | dentro da janela vertical e do lado solicitado |
| 406 | 520.00 | 189.00 | 24.00 | 25.56 | SIM | dentro da janela vertical e do lado solicitado |
| 407 | 520.00 | 188.00 | 25.00 | 26.56 | SIM | dentro da janela vertical e do lado solicitado |
| 408 | 520.00 | 187.00 | 26.00 | 27.56 | SIM | dentro da janela vertical e do lado solicitado |
| 409 | 520.00 | 186.00 | 27.00 | 28.56 | SIM | dentro da janela vertical e do lado solicitado |
| 410 | 520.00 | 185.00 | 28.00 | 29.56 | SIM | dentro da janela vertical e do lado solicitado |
| 411 | 520.00 | 184.00 | 29.00 | 30.56 | SIM | dentro da janela vertical e do lado solicitado |
| 412 | 520.00 | 183.00 | 30.00 | 31.56 | SIM | dentro da janela vertical e do lado solicitado |
| 413 | 520.00 | 182.00 | 31.00 | 32.56 | SIM | dentro da janela vertical e do lado solicitado |
| 414 | 520.00 | 181.00 | 32.00 | 33.56 | SIM | dentro da janela vertical e do lado solicitado |
| 415 | 520.00 | 180.00 | 33.00 | 34.56 | SIM | dentro da janela vertical e do lado solicitado |
| 416 | 520.00 | 179.00 | 34.00 | 35.56 | SIM | dentro da janela vertical e do lado solicitado |
| 417 | 520.00 | 178.00 | 35.00 | 36.56 | SIM | dentro da janela vertical e do lado solicitado |
| 418 | 520.00 | 177.00 | 36.00 | 37.56 | SIM | dentro da janela vertical e do lado solicitado |
| 419 | 520.00 | 176.00 | 37.00 | 38.56 | SIM | dentro da janela vertical e do lado solicitado |
| 420 | 520.00 | 175.00 | 38.00 | 39.56 | SIM | dentro da janela vertical e do lado solicitado |
| 421 | 520.00 | 174.00 | 39.00 | 40.56 | SIM | dentro da janela vertical e do lado solicitado |
| 422 | 520.00 | 173.00 | 40.00 | 41.56 | SIM | dentro da janela vertical e do lado solicitado |
| 423 | 520.00 | 172.00 | 41.00 | 42.56 | SIM | dentro da janela vertical e do lado solicitado |
| 424 | 520.00 | 171.00 | 42.00 | 43.56 | SIM | dentro da janela vertical e do lado solicitado |
| 425 | 520.00 | 170.00 | 43.00 | 44.56 | SIM | dentro da janela vertical e do lado solicitado |
| 426 | 520.00 | 169.00 | 44.00 | 45.56 | SIM | dentro da janela vertical e do lado solicitado |
| 427 | 520.00 | 168.00 | 45.00 | 46.56 | SIM | dentro da janela vertical e do lado solicitado |
| 428 | 520.00 | 167.00 | 46.00 | 47.56 | SIM | dentro da janela vertical e do lado solicitado |
| 429 | 520.00 | 166.00 | 47.00 | 48.56 | SIM | dentro da janela vertical e do lado solicitado |
| 430 | 520.00 | 165.00 | 48.00 | 49.56 | SIM | dentro da janela vertical e do lado solicitado |
| 431 | 520.00 | 164.00 | 49.00 | 50.56 | SIM | dentro da janela vertical e do lado solicitado |
| 432 | 520.00 | 163.00 | 50.00 | 51.56 | SIM | dentro da janela vertical e do lado solicitado |
| 433 | 520.00 | 162.00 | 51.00 | 52.56 | SIM | dentro da janela vertical e do lado solicitado |
| 434 | 520.00 | 161.00 | 52.00 | 53.56 | SIM | dentro da janela vertical e do lado solicitado |
| 435 | 520.00 | 160.00 | 53.00 | 54.56 | SIM | dentro da janela vertical e do lado solicitado |
| 436 | 520.00 | 159.00 | 54.00 | 55.56 | SIM | dentro da janela vertical e do lado solicitado |
| 437 | 520.00 | 158.00 | 55.00 | 56.56 | SIM | dentro da janela vertical e do lado solicitado |
| 438 | 520.00 | 157.00 | 56.00 | 57.56 | SIM | dentro da janela vertical e do lado solicitado |
| 439 | 520.00 | 156.00 | 57.00 | 58.56 | SIM | dentro da janela vertical e do lado solicitado |
| 440 | 520.00 | 155.00 | 58.00 | 59.56 | SIM | dentro da janela vertical e do lado solicitado |
| 441 | 520.00 | 154.00 | 59.00 | 60.56 | SIM | dentro da janela vertical e do lado solicitado |
| 442 | 520.00 | 153.00 | 60.00 | 61.56 | SIM | dentro da janela vertical e do lado solicitado |
| 443 | 520.00 | 152.00 | 61.00 | 62.56 | SIM | dentro da janela vertical e do lado solicitado |
| 444 | 520.00 | 151.00 | 62.00 | 63.56 | SIM | dentro da janela vertical e do lado solicitado |
| 445 | 520.00 | 150.00 | 63.00 | 64.56 | SIM | dentro da janela vertical e do lado solicitado |
| 446 | 520.00 | 149.00 | 64.00 | 65.56 | SIM | dentro da janela vertical e do lado solicitado |
| 447 | 520.00 | 148.00 | 65.00 | 66.56 | SIM | dentro da janela vertical e do lado solicitado |
| 448 | 520.00 | 147.00 | 66.00 | 67.56 | SIM | dentro da janela vertical e do lado solicitado |
| 449 | 520.00 | 146.00 | 67.00 | 68.56 | SIM | dentro da janela vertical e do lado solicitado |
| 450 | 520.00 | 145.00 | 68.00 | 69.56 | SIM | dentro da janela vertical e do lado solicitado |
| 451 | 520.00 | 144.00 | 69.00 | 70.56 | SIM | dentro da janela vertical e do lado solicitado |
| 452 | 520.00 | 143.00 | 70.00 | 71.56 | SIM | dentro da janela vertical e do lado solicitado |
| 453 | 520.00 | 142.00 | 71.00 | 72.56 | SIM | dentro da janela vertical e do lado solicitado |
| 454 | 520.00 | 141.00 | 72.00 | 73.56 | SIM | dentro da janela vertical e do lado solicitado |
| 455 | 520.00 | 140.00 | 73.00 | 74.56 | SIM | dentro da janela vertical e do lado solicitado |
| 456 | 520.00 | 139.00 | 74.00 | 75.56 | SIM | dentro da janela vertical e do lado solicitado |
| 457 | 520.00 | 138.00 | 75.00 | 76.56 | SIM | dentro da janela vertical e do lado solicitado |
| 458 | 520.00 | 137.00 | 76.00 | 77.56 | SIM | dentro da janela vertical e do lado solicitado |
| 459 | 520.00 | 136.00 | 77.00 | 78.56 | SIM | dentro da janela vertical e do lado solicitado |
| 460 | 520.00 | 135.00 | 78.00 | 79.56 | SIM | dentro da janela vertical e do lado solicitado |
| 461 | 520.00 | 134.00 | 79.00 | 80.56 | SIM | dentro da janela vertical e do lado solicitado |
| 462 | 520.00 | 133.00 | 80.00 | 81.56 | SIM | dentro da janela vertical e do lado solicitado |
| 463 | 520.00 | 132.00 | 81.00 | 82.56 | SIM | dentro da janela vertical e do lado solicitado |
| 464 | 520.00 | 131.00 | 82.00 | 83.56 | SIM | dentro da janela vertical e do lado solicitado |
| 465 | 520.00 | 130.00 | 83.00 | 84.56 | SIM | dentro da janela vertical e do lado solicitado |
| 466 | 520.00 | 129.00 | 84.00 | 85.56 | NÃO | fora da faixa vertical |
| 467 | 519.00 | 129.00 | 84.01 | 85.56 | NÃO | fora da faixa vertical |
| 468 | 518.00 | 129.00 | 84.02 | 85.56 | NÃO | fora da faixa vertical |
| 469 | 517.00 | 129.00 | 84.05 | 85.56 | NÃO | fora da faixa vertical |
| 470 | 516.00 | 129.00 | 84.10 | 85.56 | NÃO | fora da faixa vertical |
| 471 | 515.00 | 129.00 | 84.15 | 85.56 | NÃO | fora da faixa vertical |
| 472 | 514.00 | 129.00 | 84.21 | 85.56 | NÃO | fora da faixa vertical |
| 473 | 513.00 | 129.00 | 84.29 | 85.56 | NÃO | fora da faixa vertical |
| 474 | 512.00 | 129.00 | 84.38 | 85.56 | NÃO | fora da faixa vertical |
| 475 | 511.00 | 129.00 | 84.48 | 85.56 | NÃO | fora da faixa vertical |
| 476 | 510.00 | 129.00 | 84.59 | 85.56 | NÃO | fora da faixa vertical |
| 477 | 509.00 | 129.00 | 84.72 | 85.56 | NÃO | fora da faixa vertical |
| 478 | 508.00 | 129.00 | 84.85 | 85.56 | NÃO | fora da faixa vertical |
| 479 | 507.00 | 129.00 | 85.00 | 85.56 | NÃO | fora da faixa vertical |
| 480 | 506.00 | 129.00 | 85.16 | 85.56 | NÃO | fora da faixa vertical |
| 481 | 505.00 | 129.00 | 85.33 | 85.56 | NÃO | fora da faixa vertical |
| 482 | 504.00 | 129.00 | 85.51 | 85.56 | NÃO | fora da faixa vertical |
| 483 | 503.00 | 129.00 | 85.70 | 85.56 | NÃO | fora da faixa vertical |
| 484 | 502.00 | 129.00 | 85.91 | 85.56 | NÃO | fora da faixa vertical |
| 485 | 501.00 | 129.00 | 86.12 | 85.56 | NÃO | fora da faixa vertical |
| 486 | 500.00 | 129.00 | 86.35 | 85.56 | NÃO | fora da faixa vertical |
| 487 | 499.00 | 129.00 | 86.59 | 85.56 | NÃO | fora da faixa vertical |
| 488 | 498.00 | 129.00 | 86.83 | 85.56 | NÃO | fora da faixa vertical |
| 489 | 497.00 | 129.00 | 87.09 | 85.56 | NÃO | fora da faixa vertical |
| 490 | 496.00 | 129.00 | 87.36 | 85.56 | NÃO | fora da faixa vertical |
| 491 | 495.00 | 129.00 | 87.64 | 85.56 | NÃO | fora da faixa vertical |
| 492 | 494.00 | 129.00 | 87.93 | 85.56 | NÃO | fora da faixa vertical |
| 493 | 493.00 | 129.00 | 88.23 | 85.56 | NÃO | fora da faixa vertical |
| 494 | 492.00 | 129.00 | 88.54 | 85.56 | NÃO | fora da faixa vertical |
| 495 | 491.00 | 129.00 | 88.87 | 85.56 | NÃO | fora da faixa vertical |
| 496 | 490.00 | 129.00 | 89.20 | 85.56 | NÃO | fora da faixa vertical |
| 497 | 489.00 | 129.00 | 89.54 | 85.56 | NÃO | fora da faixa vertical |
| 498 | 488.00 | 129.00 | 89.89 | 85.56 | NÃO | fora da faixa vertical |
| 499 | 487.00 | 129.00 | 90.25 | 85.56 | NÃO | fora da faixa vertical |
| 500 | 486.00 | 129.00 | 90.62 | 85.56 | NÃO | fora da faixa vertical |
| 501 | 485.00 | 129.00 | 91.00 | 85.56 | NÃO | fora da faixa vertical |
| 502 | 484.00 | 129.00 | 91.39 | 85.56 | NÃO | fora da faixa vertical |
| 503 | 483.00 | 129.00 | 91.79 | 85.56 | NÃO | fora da faixa vertical |
| 504 | 482.00 | 129.00 | 92.20 | 85.56 | NÃO | fora da faixa vertical |
| 505 | 481.00 | 129.00 | 92.61 | 85.56 | NÃO | fora da faixa vertical |
| 506 | 480.00 | 129.00 | 93.04 | 85.56 | NÃO | fora da faixa vertical |
| 507 | 479.00 | 129.00 | 93.47 | 85.56 | NÃO | fora da faixa vertical |
| 508 | 478.00 | 129.00 | 93.91 | 85.56 | NÃO | fora da faixa vertical |
| 509 | 477.00 | 129.00 | 94.37 | 85.56 | NÃO | fora da faixa vertical |
| 510 | 476.00 | 129.00 | 94.83 | 85.56 | NÃO | fora da faixa vertical |
| 511 | 475.00 | 129.00 | 95.29 | 85.56 | NÃO | fora da faixa vertical |
| 512 | 474.00 | 129.00 | 95.77 | 85.56 | NÃO | fora da faixa vertical |
| 513 | 473.00 | 129.00 | 96.25 | 85.56 | NÃO | fora da faixa vertical |
| 514 | 472.00 | 129.00 | 96.75 | 85.56 | NÃO | fora da faixa vertical |
| 515 | 471.00 | 129.00 | 97.25 | 85.56 | NÃO | fora da faixa vertical |
| 516 | 470.00 | 129.00 | 97.75 | 85.56 | NÃO | fora da faixa vertical |
| 517 | 469.00 | 129.00 | 98.27 | 85.56 | NÃO | fora da faixa vertical |
| 518 | 468.00 | 129.00 | 98.79 | 85.56 | NÃO | fora da faixa vertical |
| 519 | 467.00 | 129.00 | 99.32 | 85.56 | NÃO | fora da faixa vertical |
| 520 | 466.00 | 129.00 | 99.86 | 85.56 | NÃO | fora da faixa vertical |
| 521 | 465.00 | 129.00 | 100.40 | 85.56 | NÃO | fora da faixa vertical |
| 522 | 464.00 | 129.00 | 100.96 | 85.56 | NÃO | fora da faixa vertical |
| 523 | 463.00 | 129.00 | 101.51 | 85.56 | NÃO | fora da faixa vertical |
| 524 | 462.00 | 129.00 | 102.08 | 85.56 | NÃO | fora da faixa vertical |
| 525 | 461.00 | 129.00 | 102.65 | 85.56 | NÃO | fora da faixa vertical |
| 526 | 460.00 | 129.00 | 103.23 | 85.56 | NÃO | fora da faixa vertical |
| 527 | 459.00 | 129.00 | 103.81 | 85.56 | NÃO | fora da faixa vertical |
| 528 | 458.00 | 129.00 | 104.40 | 85.56 | NÃO | fora da faixa vertical |
| 529 | 457.00 | 129.00 | 105.00 | 85.56 | NÃO | fora da faixa vertical |
| 530 | 456.00 | 129.00 | 105.60 | 85.56 | NÃO | fora da faixa vertical |
| 531 | 455.00 | 129.00 | 106.21 | 85.56 | NÃO | fora da faixa vertical |
| 532 | 454.00 | 129.00 | 106.83 | 85.56 | NÃO | fora da faixa vertical |
| 533 | 453.00 | 129.00 | 107.45 | 85.56 | NÃO | fora da faixa vertical |
| 534 | 452.00 | 129.00 | 108.07 | 85.56 | NÃO | fora da faixa vertical |
| 535 | 451.00 | 129.00 | 108.71 | 85.56 | NÃO | fora da faixa vertical |
| 536 | 450.00 | 129.00 | 109.34 | 85.56 | NÃO | fora da faixa vertical |
| 537 | 449.00 | 129.00 | 109.99 | 85.56 | NÃO | fora da faixa vertical |
| 538 | 448.00 | 129.00 | 110.63 | 85.56 | NÃO | fora da faixa vertical |
| 539 | 447.00 | 129.00 | 111.29 | 85.56 | NÃO | fora da faixa vertical |
| 540 | 446.00 | 129.00 | 111.95 | 85.56 | NÃO | fora da faixa vertical |
| 541 | 445.00 | 129.00 | 112.61 | 85.56 | NÃO | fora da faixa vertical |
| 542 | 444.00 | 129.00 | 113.28 | 85.56 | NÃO | fora da faixa vertical |
| 543 | 443.00 | 129.00 | 113.95 | 85.56 | NÃO | fora da faixa vertical |
| 544 | 442.00 | 129.00 | 114.63 | 85.56 | NÃO | fora da faixa vertical |
| 545 | 441.00 | 129.00 | 115.31 | 85.56 | NÃO | fora da faixa vertical |
| 546 | 440.00 | 129.00 | 116.00 | 85.56 | NÃO | fora da faixa vertical |
| 547 | 439.00 | 129.00 | 116.69 | 85.56 | NÃO | fora da faixa vertical |
| 548 | 438.00 | 129.00 | 117.39 | 85.56 | NÃO | fora da faixa vertical |
| 549 | 437.00 | 129.00 | 118.09 | 85.56 | NÃO | fora da faixa vertical |
| 550 | 436.00 | 129.00 | 118.79 | 85.56 | NÃO | fora da faixa vertical |
| 551 | 435.00 | 129.00 | 119.50 | 85.56 | NÃO | fora da faixa vertical |
| 552 | 434.00 | 129.00 | 120.22 | 85.56 | NÃO | fora da faixa vertical |
| 553 | 433.00 | 129.00 | 120.93 | 85.56 | NÃO | fora da faixa vertical |
| 554 | 432.00 | 129.00 | 121.66 | 85.56 | NÃO | fora da faixa vertical |
| 555 | 431.00 | 129.00 | 122.38 | 85.56 | NÃO | fora da faixa vertical |
| 556 | 430.00 | 129.00 | 123.11 | 85.56 | NÃO | fora da faixa vertical |
| 557 | 429.00 | 129.00 | 123.84 | 85.56 | NÃO | fora da faixa vertical |
| 558 | 428.00 | 128.00 | 125.26 | 86.56 | NÃO | fora da faixa vertical |
| 559 | 427.00 | 128.00 | 125.99 | 86.56 | NÃO | fora da faixa vertical |
| 560 | 426.00 | 127.00 | 127.40 | 87.56 | NÃO | fora da faixa vertical |
| 561 | 425.00 | 126.00 | 128.82 | 88.56 | NÃO | fora da faixa vertical |
| 562 | 424.00 | 125.00 | 130.23 | 89.56 | NÃO | fora da faixa vertical |
| 563 | 423.00 | 124.00 | 131.64 | 90.56 | NÃO | fora da faixa vertical |
| 564 | 422.00 | 123.00 | 133.06 | 91.56 | NÃO | fora da faixa vertical |
| 565 | 421.00 | 122.00 | 134.47 | 92.56 | NÃO | fora da faixa vertical |
| 566 | 421.00 | 121.00 | 135.15 | 93.56 | NÃO | fora da faixa vertical |
| 567 | 420.00 | 120.00 | 136.56 | 94.56 | NÃO | fora da faixa vertical |
| 568 | 419.00 | 119.00 | 137.97 | 95.56 | NÃO | fora da faixa vertical |
| 569 | 418.00 | 118.00 | 139.39 | 96.56 | NÃO | fora da faixa vertical |
| 570 | 417.00 | 117.00 | 140.80 | 97.56 | NÃO | fora da faixa vertical |
| 571 | 416.00 | 116.00 | 142.21 | 98.56 | NÃO | fora da faixa vertical |
| 572 | 415.00 | 115.00 | 143.63 | 99.56 | NÃO | fora da faixa vertical |
| 573 | 414.00 | 114.00 | 145.04 | 100.56 | NÃO | fora da faixa vertical |
| 574 | 413.00 | 113.00 | 146.45 | 101.56 | NÃO | fora da faixa vertical |
| 575 | 412.00 | 112.00 | 147.87 | 102.56 | NÃO | fora da faixa vertical |
| 576 | 411.00 | 111.00 | 149.28 | 103.56 | NÃO | fora da faixa vertical |
| 577 | 410.00 | 110.00 | 150.70 | 104.56 | NÃO | fora da faixa vertical |
| 578 | 409.00 | 109.00 | 152.11 | 105.56 | NÃO | fora da faixa vertical |
| 579 | 408.00 | 108.00 | 153.52 | 106.56 | NÃO | fora da faixa vertical |
| 580 | 407.00 | 107.00 | 154.94 | 107.56 | NÃO | fora da faixa vertical |
| 581 | 406.00 | 107.00 | 155.67 | 107.56 | NÃO | fora da faixa vertical |
| 582 | 405.00 | 106.00 | 157.08 | 108.56 | NÃO | fora da faixa vertical |
| 583 | 404.00 | 105.00 | 158.49 | 109.56 | NÃO | fora da faixa vertical |
| 584 | 403.00 | 104.00 | 159.91 | 110.56 | NÃO | fora da faixa vertical |
| 585 | 402.00 | 103.00 | 161.32 | 111.56 | NÃO | fora da faixa vertical |
| 586 | 401.00 | 102.00 | 162.73 | 112.56 | NÃO | fora da faixa vertical |
| 587 | 400.00 | 101.00 | 164.15 | 113.56 | NÃO | fora da faixa vertical |
| 588 | 399.00 | 101.00 | 164.88 | 113.56 | NÃO | fora da faixa vertical |
| 589 | 398.00 | 100.00 | 166.29 | 114.56 | NÃO | fora da faixa vertical |
| 590 | 397.00 | 99.00 | 167.71 | 115.56 | NÃO | fora da faixa vertical |
| 591 | 396.00 | 99.00 | 168.44 | 115.56 | NÃO | fora da faixa vertical |
| 592 | 395.00 | 98.00 | 169.85 | 116.56 | NÃO | fora da faixa vertical |
| 593 | 394.00 | 97.00 | 171.27 | 117.56 | NÃO | fora da faixa vertical |
| 594 | 393.00 | 96.00 | 172.68 | 118.56 | NÃO | fora da faixa vertical |
| 595 | 392.00 | 96.00 | 173.42 | 118.56 | NÃO | fora da faixa vertical |
| 596 | 391.00 | 95.00 | 174.83 | 119.56 | NÃO | fora da faixa vertical |
| 597 | 390.00 | 94.00 | 176.24 | 120.56 | NÃO | fora da faixa vertical |
| 598 | 389.00 | 93.00 | 177.65 | 121.56 | NÃO | fora da faixa vertical |
| 599 | 388.00 | 93.00 | 178.39 | 121.56 | NÃO | fora da faixa vertical |
| 600 | 387.00 | 92.00 | 179.81 | 122.56 | NÃO | fora da faixa vertical |
| 601 | 386.00 | 91.00 | 181.22 | 123.56 | NÃO | fora da faixa vertical |
| 602 | 385.00 | 91.00 | 181.96 | 123.56 | NÃO | fora da faixa vertical |
| 603 | 384.00 | 90.00 | 183.37 | 124.56 | NÃO | fora da faixa vertical |
| 604 | 383.00 | 89.00 | 184.78 | 125.56 | NÃO | fora da faixa vertical |
| 605 | 382.00 | 89.00 | 185.53 | 125.56 | NÃO | fora da faixa vertical |
| 606 | 381.00 | 88.00 | 186.94 | 126.56 | NÃO | fora da faixa vertical |
| 607 | 380.00 | 88.00 | 187.68 | 126.56 | NÃO | fora da faixa vertical |
| 608 | 379.00 | 87.00 | 189.10 | 127.56 | NÃO | fora da faixa vertical |
| 609 | 378.00 | 86.00 | 190.51 | 128.56 | NÃO | fora da faixa vertical |
| 610 | 377.00 | 86.00 | 191.25 | 128.56 | NÃO | fora da faixa vertical |
| 611 | 376.00 | 85.00 | 192.67 | 129.56 | NÃO | fora da faixa vertical |
| 612 | 375.00 | 84.00 | 194.08 | 130.56 | NÃO | fora da faixa vertical |
| 613 | 374.00 | 84.00 | 194.83 | 130.56 | NÃO | fora da faixa vertical |
| 614 | 373.00 | 83.00 | 196.24 | 131.56 | NÃO | fora da faixa vertical |
| 615 | 372.00 | 83.00 | 196.99 | 131.56 | NÃO | fora da faixa vertical |
| 616 | 371.00 | 82.00 | 198.40 | 132.56 | NÃO | fora da faixa vertical |
| 617 | 370.00 | 81.00 | 199.81 | 133.56 | NÃO | fora da faixa vertical |
| 618 | 369.00 | 81.00 | 200.56 | 133.56 | NÃO | fora da faixa vertical |
| 619 | 368.00 | 80.00 | 201.97 | 134.56 | NÃO | fora da faixa vertical |
| 620 | 367.00 | 80.00 | 202.73 | 134.56 | NÃO | fora da faixa vertical |
| 621 | 366.00 | 79.00 | 204.14 | 135.56 | NÃO | fora da faixa vertical |
| 622 | 365.00 | 79.00 | 204.89 | 135.56 | NÃO | fora da faixa vertical |
| 623 | 364.00 | 78.00 | 206.30 | 136.56 | NÃO | fora da faixa vertical |
| 624 | 363.00 | 78.00 | 207.06 | 136.56 | NÃO | fora da faixa vertical |
| 625 | 362.00 | 77.00 | 208.47 | 137.56 | NÃO | fora da faixa vertical |
| 626 | 361.00 | 77.00 | 209.23 | 137.56 | NÃO | fora da faixa vertical |
| 627 | 360.00 | 76.00 | 210.64 | 138.56 | NÃO | fora da faixa vertical |
| 628 | 359.00 | 76.00 | 211.40 | 138.56 | NÃO | fora da faixa vertical |
| 629 | 358.00 | 75.00 | 212.81 | 139.56 | NÃO | fora da faixa vertical |
| 630 | 357.00 | 75.00 | 213.57 | 139.56 | NÃO | fora da faixa vertical |
| 631 | 356.00 | 75.00 | 214.34 | 139.56 | NÃO | fora da faixa vertical |
| 632 | 355.00 | 74.00 | 215.75 | 140.56 | NÃO | fora da faixa vertical |
| 633 | 354.00 | 74.00 | 216.51 | 140.56 | NÃO | fora da faixa vertical |
| 634 | 353.00 | 73.00 | 217.92 | 141.56 | NÃO | fora da faixa vertical |
| 635 | 352.00 | 73.00 | 218.69 | 141.56 | NÃO | fora da faixa vertical |
| 636 | 351.00 | 72.00 | 220.10 | 142.56 | NÃO | fora da faixa vertical |
| 637 | 350.00 | 72.00 | 220.86 | 142.56 | NÃO | fora da faixa vertical |
| 638 | 349.00 | 71.00 | 222.27 | 143.56 | NÃO | fora da faixa vertical |
| 639 | 348.00 | 71.00 | 223.04 | 143.56 | NÃO | fora da faixa vertical |
| 640 | 347.00 | 71.00 | 223.81 | 143.56 | NÃO | fora da faixa vertical |
| 641 | 346.00 | 70.00 | 225.22 | 144.56 | NÃO | fora da faixa vertical |
| 642 | 345.00 | 70.00 | 226.00 | 144.56 | NÃO | fora da faixa vertical |
| 643 | 344.00 | 70.00 | 226.77 | 144.56 | NÃO | fora da faixa vertical |
| 644 | 343.00 | 69.00 | 228.18 | 145.56 | NÃO | fora da faixa vertical |
| 645 | 342.00 | 69.00 | 228.95 | 145.56 | NÃO | fora da faixa vertical |
| 646 | 341.00 | 68.00 | 230.36 | 146.56 | NÃO | fora da faixa vertical |
| 647 | 340.00 | 68.00 | 231.14 | 146.56 | NÃO | fora da faixa vertical |
| 648 | 339.00 | 68.00 | 231.92 | 146.56 | NÃO | fora da faixa vertical |
| 649 | 338.00 | 67.00 | 233.32 | 147.56 | NÃO | fora da faixa vertical |
| 650 | 337.00 | 67.00 | 234.10 | 147.56 | NÃO | fora da faixa vertical |
| 651 | 336.00 | 67.00 | 234.89 | 147.56 | NÃO | fora da faixa vertical |
| 652 | 335.00 | 66.00 | 236.29 | 148.56 | NÃO | fora da faixa vertical |
| 653 | 334.00 | 66.00 | 237.08 | 148.56 | NÃO | fora da faixa vertical |
| 654 | 333.00 | 66.00 | 237.86 | 148.56 | NÃO | fora da faixa vertical |
| 655 | 332.00 | 65.00 | 239.27 | 149.56 | NÃO | fora da faixa vertical |
| 656 | 331.00 | 65.00 | 240.05 | 149.56 | NÃO | fora da faixa vertical |
| 657 | 330.00 | 65.00 | 240.84 | 149.56 | NÃO | fora da faixa vertical |
| 658 | 329.00 | 65.00 | 241.63 | 149.56 | NÃO | fora da faixa vertical |
| 659 | 328.00 | 64.00 | 243.03 | 150.56 | NÃO | fora da faixa vertical |
| 660 | 327.00 | 64.00 | 243.82 | 150.56 | NÃO | fora da faixa vertical |
| 661 | 326.00 | 64.00 | 244.62 | 150.56 | NÃO | fora da faixa vertical |
| 662 | 325.00 | 63.00 | 246.02 | 151.56 | NÃO | fora da faixa vertical |
| 663 | 324.00 | 63.00 | 246.81 | 151.56 | NÃO | fora da faixa vertical |
| 664 | 323.00 | 63.00 | 247.61 | 151.56 | NÃO | fora da faixa vertical |
| 665 | 322.00 | 63.00 | 248.40 | 151.56 | NÃO | fora da faixa vertical |
| 666 | 321.00 | 62.00 | 249.80 | 152.56 | NÃO | fora da faixa vertical |
| 667 | 320.00 | 62.00 | 250.60 | 152.56 | NÃO | fora da faixa vertical |
| 668 | 319.00 | 62.00 | 251.40 | 152.56 | NÃO | fora da faixa vertical |
| 669 | 318.00 | 62.00 | 252.20 | 152.56 | NÃO | fora da faixa vertical |
| 670 | 317.00 | 61.00 | 253.60 | 153.56 | NÃO | fora da faixa vertical |
| 671 | 316.00 | 61.00 | 254.40 | 153.56 | NÃO | fora da faixa vertical |
| 672 | 315.00 | 61.00 | 255.20 | 153.56 | NÃO | fora da faixa vertical |
| 673 | 314.00 | 61.00 | 256.01 | 153.56 | NÃO | fora da faixa vertical |
| 674 | 313.00 | 61.00 | 256.81 | 153.56 | NÃO | fora da faixa vertical |
| 675 | 312.00 | 60.00 | 258.21 | 154.56 | NÃO | fora da faixa vertical |
| 676 | 311.00 | 60.00 | 259.02 | 154.56 | NÃO | fora da faixa vertical |
| 677 | 310.00 | 60.00 | 259.82 | 154.56 | NÃO | fora da faixa vertical |
| 678 | 309.00 | 60.00 | 260.63 | 154.56 | NÃO | fora da faixa vertical |
| 679 | 308.00 | 60.00 | 261.44 | 154.56 | NÃO | fora da faixa vertical |
| 680 | 307.00 | 59.00 | 262.84 | 155.56 | NÃO | fora da faixa vertical |
| 681 | 306.00 | 59.00 | 263.65 | 155.56 | NÃO | fora da faixa vertical |
| 682 | 305.00 | 59.00 | 264.46 | 155.56 | NÃO | fora da faixa vertical |
| 683 | 304.00 | 59.00 | 265.28 | 155.56 | NÃO | fora da faixa vertical |
| 684 | 303.00 | 59.00 | 266.09 | 155.56 | NÃO | fora da faixa vertical |
| 685 | 302.00 | 59.00 | 266.91 | 155.56 | NÃO | fora da faixa vertical |
| 686 | 301.00 | 59.00 | 267.73 | 155.56 | NÃO | fora da faixa vertical |
| 687 | 300.00 | 58.00 | 269.12 | 156.56 | NÃO | fora da faixa vertical |
| 688 | 299.00 | 58.00 | 269.94 | 156.56 | NÃO | fora da faixa vertical |
| 689 | 298.00 | 58.00 | 270.76 | 156.56 | NÃO | fora da faixa vertical |
| 690 | 297.00 | 58.00 | 271.58 | 156.56 | NÃO | fora da faixa vertical |
| 691 | 296.00 | 58.00 | 272.40 | 156.56 | NÃO | fora da faixa vertical |
| 692 | 295.00 | 58.00 | 273.22 | 156.56 | NÃO | fora da faixa vertical |
| 693 | 294.00 | 58.00 | 274.05 | 156.56 | NÃO | fora da faixa vertical |
| 694 | 293.00 | 58.00 | 274.87 | 156.56 | NÃO | fora da faixa vertical |
| 695 | 292.00 | 58.00 | 275.70 | 156.56 | NÃO | fora da faixa vertical |
| 696 | 291.00 | 57.00 | 277.09 | 157.56 | NÃO | fora da faixa vertical |
| 697 | 290.00 | 57.00 | 277.91 | 157.56 | NÃO | fora da faixa vertical |
| 698 | 289.00 | 57.00 | 278.74 | 157.56 | NÃO | fora da faixa vertical |
| 699 | 288.00 | 57.00 | 279.57 | 157.56 | NÃO | fora da faixa vertical |
| 700 | 287.00 | 57.00 | 280.40 | 157.56 | NÃO | fora da faixa vertical |
| 701 | 286.00 | 57.00 | 281.23 | 157.56 | NÃO | fora da faixa vertical |
| 702 | 285.00 | 57.00 | 282.07 | 157.56 | NÃO | fora da faixa vertical |
| 703 | 284.00 | 57.00 | 282.90 | 157.56 | NÃO | fora da faixa vertical |
| 704 | 283.00 | 57.00 | 283.73 | 157.56 | NÃO | fora da faixa vertical |
| 705 | 282.00 | 57.00 | 284.57 | 157.56 | NÃO | fora da faixa vertical |
| 706 | 281.00 | 57.00 | 285.41 | 157.56 | NÃO | fora da faixa vertical |
| 707 | 280.00 | 57.00 | 286.24 | 157.56 | NÃO | fora da faixa vertical |
| 708 | 279.00 | 57.00 | 287.08 | 157.56 | NÃO | fora da faixa vertical |
| 709 | 278.00 | 57.00 | 287.92 | 157.56 | NÃO | fora da faixa vertical |
| 710 | 277.00 | 57.00 | 288.76 | 157.56 | NÃO | fora da faixa vertical |
| 711 | 276.00 | 57.00 | 289.61 | 157.56 | NÃO | fora da faixa vertical |
| 712 | 275.00 | 57.00 | 290.45 | 157.56 | NÃO | fora da faixa vertical |
| 713 | 274.00 | 57.00 | 291.29 | 157.56 | NÃO | fora da faixa vertical |
| 714 | 273.00 | 57.00 | 292.14 | 157.56 | NÃO | fora da faixa vertical |
| 715 | 272.00 | 57.00 | 292.98 | 157.56 | NÃO | fora da faixa vertical |
| 716 | 271.00 | 57.00 | 293.83 | 157.56 | NÃO | fora da faixa vertical |
| 717 | 270.00 | 57.00 | 294.68 | 157.56 | NÃO | fora da faixa vertical |
| 718 | 269.00 | 57.00 | 295.53 | 157.56 | NÃO | fora da faixa vertical |
| 719 | 268.00 | 57.00 | 296.38 | 157.56 | NÃO | fora da faixa vertical |
| 720 | 267.00 | 57.00 | 297.23 | 157.56 | NÃO | fora da faixa vertical |
| 721 | 266.00 | 57.00 | 298.08 | 157.56 | NÃO | fora da faixa vertical |
| 722 | 265.00 | 57.00 | 298.93 | 157.56 | NÃO | fora da faixa vertical |
| 723 | 264.00 | 57.00 | 299.79 | 157.56 | NÃO | fora da faixa vertical |
| 724 | 263.00 | 57.00 | 300.64 | 157.56 | NÃO | fora da faixa vertical |
| 725 | 262.00 | 57.00 | 301.50 | 157.56 | NÃO | fora da faixa vertical |
| 726 | 261.00 | 57.00 | 302.35 | 157.56 | NÃO | fora da faixa vertical |
| 727 | 260.00 | 57.00 | 303.21 | 157.56 | NÃO | fora da faixa vertical |
| 728 | 259.00 | 57.00 | 304.07 | 157.56 | NÃO | fora da faixa vertical |
| 729 | 258.00 | 57.00 | 304.93 | 157.56 | NÃO | fora da faixa vertical |
| 730 | 257.00 | 57.00 | 305.79 | 157.56 | NÃO | fora da faixa vertical |
| 731 | 256.00 | 57.00 | 306.65 | 157.56 | NÃO | fora da faixa vertical |
| 732 | 255.00 | 57.00 | 307.51 | 157.56 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 317 | 455.00 | 213.00 | -65.00 | -1.56 |
| 318 | 456.00 | 213.00 | -64.00 | -1.56 |
| 319 | 457.00 | 213.00 | -63.00 | -1.56 |
| 320 | 458.00 | 213.00 | -62.00 | -1.56 |
| 321 | 459.00 | 213.00 | -61.00 | -1.56 |
| 322 | 460.00 | 213.00 | -60.00 | -1.56 |
| 323 | 461.00 | 213.00 | -59.00 | -1.56 |
| 324 | 462.00 | 213.00 | -58.00 | -1.56 |
| 325 | 463.00 | 213.00 | -57.00 | -1.56 |
| 326 | 464.00 | 213.00 | -56.00 | -1.56 |
| 327 | 465.00 | 213.00 | -55.00 | -1.56 |
| 328 | 466.00 | 213.00 | -54.00 | -1.56 |
| 329 | 467.00 | 213.00 | -53.00 | -1.56 |
| 330 | 468.00 | 213.00 | -52.00 | -1.56 |
| 331 | 469.00 | 213.00 | -51.00 | -1.56 |
| 332 | 470.00 | 213.00 | -50.00 | -1.56 |
| 333 | 471.00 | 213.00 | -49.00 | -1.56 |
| 334 | 472.00 | 213.00 | -48.00 | -1.56 |
| 335 | 473.00 | 213.00 | -47.00 | -1.56 |
| 336 | 474.00 | 213.00 | -46.00 | -1.56 |
| 337 | 475.00 | 213.00 | -45.00 | -1.56 |
| 338 | 476.00 | 213.00 | -44.00 | -1.56 |
| 339 | 477.00 | 213.00 | -43.00 | -1.56 |
| 340 | 478.00 | 213.00 | -42.00 | -1.56 |
| 341 | 479.00 | 213.00 | -41.00 | -1.56 |
| 342 | 480.00 | 213.00 | -40.00 | -1.56 |
| 343 | 481.00 | 213.00 | -39.00 | -1.56 |
| 344 | 482.00 | 213.00 | -38.00 | -1.56 |
| 345 | 483.00 | 213.00 | -37.00 | -1.56 |
| 346 | 484.00 | 213.00 | -36.00 | -1.56 |
| 347 | 485.00 | 213.00 | -35.00 | -1.56 |
| 348 | 486.00 | 213.00 | -34.00 | -1.56 |
| 349 | 487.00 | 213.00 | -33.00 | -1.56 |
| 350 | 488.00 | 213.00 | -32.00 | -1.56 |
| 351 | 489.00 | 213.00 | -31.00 | -1.56 |
| 352 | 490.00 | 213.00 | -30.00 | -1.56 |
| 353 | 491.00 | 213.00 | -29.00 | -1.56 |
| 354 | 492.00 | 213.00 | -28.00 | -1.56 |
| 355 | 493.00 | 213.00 | -27.00 | -1.56 |
| 356 | 494.00 | 213.00 | -26.00 | -1.56 |
| 357 | 495.00 | 213.00 | -25.00 | -1.56 |
| 358 | 496.00 | 213.00 | -24.00 | -1.56 |
| 359 | 497.00 | 213.00 | -23.00 | -1.56 |
| 360 | 498.00 | 213.00 | -22.00 | -1.56 |
| 361 | 499.00 | 213.00 | -21.00 | -1.56 |
| 362 | 500.00 | 213.00 | -20.00 | -1.56 |
| 363 | 501.00 | 213.00 | -19.00 | -1.56 |
| 364 | 502.00 | 213.00 | -18.00 | -1.56 |
| 365 | 503.00 | 213.00 | -17.00 | -1.56 |
| 366 | 504.00 | 213.00 | -16.00 | -1.56 |
| 367 | 505.00 | 213.00 | -15.00 | -1.56 |
| 368 | 506.00 | 213.00 | -14.00 | -1.56 |
| 369 | 507.00 | 213.00 | -13.00 | -1.56 |
| 370 | 508.00 | 213.00 | -12.00 | -1.56 |
| 371 | 509.00 | 213.00 | -11.00 | -1.56 |
| 372 | 510.00 | 213.00 | -10.00 | -1.56 |
| 373 | 511.00 | 213.00 | -9.00 | -1.56 |
| 374 | 512.00 | 213.00 | -8.00 | -1.56 |
| 375 | 513.00 | 213.00 | -7.00 | -1.56 |
| 376 | 514.00 | 213.00 | -6.00 | -1.56 |
| 377 | 515.00 | 213.00 | -5.00 | -1.56 |
| 378 | 516.00 | 213.00 | -4.00 | -1.56 |
| 379 | 517.00 | 213.00 | -3.00 | -1.56 |
| 380 | 518.00 | 213.00 | -2.00 | -1.56 |
| 381 | 519.00 | 213.00 | -1.00 | -1.56 |
| 382 | 520.00 | 213.00 | 0.00 | -1.56 |
| 383 | 520.00 | 212.00 | 0.00 | -2.56 |
| 384 | 520.00 | 211.00 | 0.00 | -3.56 |
| 385 | 520.00 | 210.00 | 0.00 | -4.56 |
| 386 | 520.00 | 209.00 | 0.00 | -5.56 |
| 387 | 520.00 | 208.00 | 0.00 | -6.56 |
| 388 | 520.00 | 207.00 | 0.00 | -7.56 |
| 389 | 520.00 | 206.00 | 0.00 | -8.56 |
| 390 | 520.00 | 205.00 | 0.00 | -9.56 |
| 391 | 520.00 | 204.00 | 0.00 | -10.56 |
| 392 | 520.00 | 203.00 | 0.00 | -11.56 |
| 393 | 520.00 | 202.00 | 0.00 | -12.56 |
| 394 | 520.00 | 201.00 | 0.00 | -13.56 |
| 395 | 520.00 | 200.00 | 0.00 | -14.56 |
| 396 | 520.00 | 199.00 | 0.00 | -15.56 |
| 397 | 520.00 | 198.00 | 0.00 | -16.56 |
| 398 | 520.00 | 197.00 | 0.00 | -17.56 |
| 399 | 520.00 | 196.00 | 0.00 | -18.56 |
| 400 | 520.00 | 195.00 | 0.00 | -19.56 |
| 401 | 520.00 | 194.00 | 0.00 | -20.56 |
| 402 | 520.00 | 193.00 | 0.00 | -21.56 |
| 403 | 520.00 | 192.00 | 0.00 | -22.56 |
| 404 | 520.00 | 191.00 | 0.00 | -23.56 |
| 405 | 520.00 | 190.00 | 0.00 | -24.56 |
| 406 | 520.00 | 189.00 | 0.00 | -25.56 |
| 407 | 520.00 | 188.00 | 0.00 | -26.56 |
| 408 | 520.00 | 187.00 | 0.00 | -27.56 |
| 409 | 520.00 | 186.00 | 0.00 | -28.56 |
| 410 | 520.00 | 185.00 | 0.00 | -29.56 |
| 411 | 520.00 | 184.00 | 0.00 | -30.56 |
| 412 | 520.00 | 183.00 | 0.00 | -31.56 |
| 413 | 520.00 | 182.00 | 0.00 | -32.56 |
| 414 | 520.00 | 181.00 | 0.00 | -33.56 |
| 415 | 520.00 | 180.00 | 0.00 | -34.56 |
| 416 | 520.00 | 179.00 | 0.00 | -35.56 |
| 417 | 520.00 | 178.00 | 0.00 | -36.56 |
| 418 | 520.00 | 177.00 | 0.00 | -37.56 |
| 419 | 520.00 | 176.00 | 0.00 | -38.56 |
| 420 | 520.00 | 175.00 | 0.00 | -39.56 |
| 421 | 520.00 | 174.00 | 0.00 | -40.56 |
| 422 | 520.00 | 173.00 | 0.00 | -41.56 |
| 423 | 520.00 | 172.00 | 0.00 | -42.56 |
| 424 | 520.00 | 171.00 | 0.00 | -43.56 |
| 425 | 520.00 | 170.00 | 0.00 | -44.56 |
| 426 | 520.00 | 169.00 | 0.00 | -45.56 |
| 427 | 520.00 | 168.00 | 0.00 | -46.56 |
| 428 | 520.00 | 167.00 | 0.00 | -47.56 |
| 429 | 520.00 | 166.00 | 0.00 | -48.56 |
| 430 | 520.00 | 165.00 | 0.00 | -49.56 |
| 431 | 520.00 | 164.00 | 0.00 | -50.56 |
| 432 | 520.00 | 163.00 | 0.00 | -51.56 |
| 433 | 520.00 | 162.00 | 0.00 | -52.56 |
| 434 | 520.00 | 161.00 | 0.00 | -53.56 |
| 435 | 520.00 | 160.00 | 0.00 | -54.56 |
| 436 | 520.00 | 159.00 | 0.00 | -55.56 |
| 437 | 520.00 | 158.00 | 0.00 | -56.56 |
| 438 | 520.00 | 157.00 | 0.00 | -57.56 |
| 439 | 520.00 | 156.00 | 0.00 | -58.56 |
| 440 | 520.00 | 155.00 | 0.00 | -59.56 |
| 441 | 520.00 | 154.00 | 0.00 | -60.56 |
| 442 | 520.00 | 153.00 | 0.00 | -61.56 |
| 443 | 520.00 | 152.00 | 0.00 | -62.56 |
| 444 | 520.00 | 151.00 | 0.00 | -63.56 |
| 445 | 520.00 | 150.00 | 0.00 | -64.56 |
| 446 | 520.00 | 149.00 | 0.00 | -65.56 |
| 447 | 520.00 | 148.00 | 0.00 | -66.56 |
| 448 | 520.00 | 147.00 | 0.00 | -67.56 |
| 449 | 520.00 | 146.00 | 0.00 | -68.56 |
| 450 | 520.00 | 145.00 | 0.00 | -69.56 |
| 451 | 520.00 | 144.00 | 0.00 | -70.56 |
| 452 | 520.00 | 143.00 | 0.00 | -71.56 |
| 453 | 520.00 | 142.00 | 0.00 | -72.56 |
| 454 | 520.00 | 141.00 | 0.00 | -73.56 |
| 455 | 520.00 | 140.00 | 0.00 | -74.56 |
| 456 | 520.00 | 139.00 | 0.00 | -75.56 |
| 457 | 520.00 | 138.00 | 0.00 | -76.56 |
| 458 | 520.00 | 137.00 | 0.00 | -77.56 |
| 459 | 520.00 | 136.00 | 0.00 | -78.56 |
| 460 | 520.00 | 135.00 | 0.00 | -79.56 |
| 461 | 520.00 | 134.00 | 0.00 | -80.56 |
| 462 | 520.00 | 133.00 | 0.00 | -81.56 |
| 463 | 520.00 | 132.00 | 0.00 | -82.56 |
| 464 | 520.00 | 131.00 | 0.00 | -83.56 |
| 465 | 520.00 | 130.00 | 0.00 | -84.56 |

- primeiro índice: 317
- último índice: 465
- quantidade: 149
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![130_geo dir](audit_outputs/75_geo_dir_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![130_geo dir polyfit](audit_outputs/75_geo_dir_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

## Imagem: 30_geo

### Lado: esq

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 1148
- ponto de contato recebido: [166.0, 386.0]
- baseline_y: 386.0
- baseline_ajustada: 389.73
- lado solicitado: esq
- largura da região: 205 px
- altura da gota: 373.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 317.00 | 13.00 | 402.41 | 376.73 | NÃO | fora da faixa vertical |
| 1 | 316.00 | 14.00 | 401.10 | 375.73 | NÃO | fora da faixa vertical |
| 2 | 315.00 | 14.00 | 400.73 | 375.73 | NÃO | fora da faixa vertical |
| 3 | 314.00 | 14.00 | 400.36 | 375.73 | NÃO | fora da faixa vertical |
| 4 | 313.00 | 14.00 | 399.99 | 375.73 | NÃO | fora da faixa vertical |
| 5 | 312.00 | 14.00 | 399.62 | 375.73 | NÃO | fora da faixa vertical |
| 6 | 311.00 | 14.00 | 399.26 | 375.73 | NÃO | fora da faixa vertical |
| 7 | 310.00 | 14.00 | 398.90 | 375.73 | NÃO | fora da faixa vertical |
| 8 | 309.00 | 14.00 | 398.54 | 375.73 | NÃO | fora da faixa vertical |
| 9 | 308.00 | 14.00 | 398.18 | 375.73 | NÃO | fora da faixa vertical |
| 10 | 307.00 | 14.00 | 397.83 | 375.73 | NÃO | fora da faixa vertical |
| 11 | 306.00 | 15.00 | 396.54 | 374.73 | NÃO | fora da faixa vertical |
| 12 | 305.00 | 15.00 | 396.18 | 374.73 | NÃO | fora da faixa vertical |
| 13 | 304.00 | 15.00 | 395.83 | 374.73 | NÃO | fora da faixa vertical |
| 14 | 303.00 | 15.00 | 395.49 | 374.73 | NÃO | fora da faixa vertical |
| 15 | 302.00 | 15.00 | 395.14 | 374.73 | NÃO | fora da faixa vertical |
| 16 | 301.00 | 15.00 | 394.80 | 374.73 | NÃO | fora da faixa vertical |
| 17 | 300.00 | 15.00 | 394.46 | 374.73 | NÃO | fora da faixa vertical |
| 18 | 299.00 | 15.00 | 394.12 | 374.73 | NÃO | fora da faixa vertical |
| 19 | 298.00 | 16.00 | 392.84 | 373.73 | NÃO | fora da faixa vertical |
| 20 | 297.00 | 16.00 | 392.51 | 373.73 | NÃO | fora da faixa vertical |
| 21 | 296.00 | 16.00 | 392.17 | 373.73 | NÃO | fora da faixa vertical |
| 22 | 295.00 | 16.00 | 391.84 | 373.73 | NÃO | fora da faixa vertical |
| 23 | 294.00 | 16.00 | 391.52 | 373.73 | NÃO | fora da faixa vertical |
| 24 | 293.00 | 17.00 | 390.24 | 372.73 | NÃO | fora da faixa vertical |
| 25 | 292.00 | 17.00 | 389.92 | 372.73 | NÃO | fora da faixa vertical |
| 26 | 291.00 | 17.00 | 389.60 | 372.73 | NÃO | fora da faixa vertical |
| 27 | 290.00 | 17.00 | 389.28 | 372.73 | NÃO | fora da faixa vertical |
| 28 | 289.00 | 18.00 | 388.01 | 371.73 | NÃO | fora da faixa vertical |
| 29 | 288.00 | 18.00 | 387.70 | 371.73 | NÃO | fora da faixa vertical |
| 30 | 287.00 | 18.00 | 387.38 | 371.73 | NÃO | fora da faixa vertical |
| 31 | 286.00 | 18.00 | 387.07 | 371.73 | NÃO | fora da faixa vertical |
| 32 | 285.00 | 18.00 | 386.76 | 371.73 | NÃO | fora da faixa vertical |
| 33 | 284.00 | 19.00 | 385.50 | 370.73 | NÃO | fora da faixa vertical |
| 34 | 283.00 | 19.00 | 385.20 | 370.73 | NÃO | fora da faixa vertical |
| 35 | 282.00 | 19.00 | 384.90 | 370.73 | NÃO | fora da faixa vertical |
| 36 | 281.00 | 19.00 | 384.60 | 370.73 | NÃO | fora da faixa vertical |
| 37 | 280.00 | 20.00 | 383.34 | 369.73 | NÃO | fora da faixa vertical |
| 38 | 279.00 | 20.00 | 383.05 | 369.73 | NÃO | fora da faixa vertical |
| 39 | 278.00 | 20.00 | 382.75 | 369.73 | NÃO | fora da faixa vertical |
| 40 | 277.00 | 21.00 | 381.50 | 368.73 | NÃO | fora da faixa vertical |
| 41 | 276.00 | 21.00 | 381.22 | 368.73 | NÃO | fora da faixa vertical |
| 42 | 275.00 | 21.00 | 380.93 | 368.73 | NÃO | fora da faixa vertical |
| 43 | 274.00 | 21.00 | 380.64 | 368.73 | NÃO | fora da faixa vertical |
| 44 | 273.00 | 22.00 | 379.40 | 367.73 | NÃO | fora da faixa vertical |
| 45 | 272.00 | 22.00 | 379.12 | 367.73 | NÃO | fora da faixa vertical |
| 46 | 271.00 | 22.00 | 378.84 | 367.73 | NÃO | fora da faixa vertical |
| 47 | 270.00 | 23.00 | 377.60 | 366.73 | NÃO | fora da faixa vertical |
| 48 | 269.00 | 23.00 | 377.33 | 366.73 | NÃO | fora da faixa vertical |
| 49 | 268.00 | 23.00 | 377.06 | 366.73 | NÃO | fora da faixa vertical |
| 50 | 267.00 | 24.00 | 375.83 | 365.73 | NÃO | fora da faixa vertical |
| 51 | 266.00 | 24.00 | 375.56 | 365.73 | NÃO | fora da faixa vertical |
| 52 | 265.00 | 24.00 | 375.29 | 365.73 | NÃO | fora da faixa vertical |
| 53 | 264.00 | 25.00 | 374.07 | 364.73 | NÃO | fora da faixa vertical |
| 54 | 263.00 | 25.00 | 373.80 | 364.73 | NÃO | fora da faixa vertical |
| 55 | 262.00 | 26.00 | 372.58 | 363.73 | NÃO | fora da faixa vertical |
| 56 | 261.00 | 26.00 | 372.32 | 363.73 | NÃO | fora da faixa vertical |
| 57 | 260.00 | 26.00 | 372.07 | 363.73 | NÃO | fora da faixa vertical |
| 58 | 259.00 | 27.00 | 370.85 | 362.73 | NÃO | fora da faixa vertical |
| 59 | 258.00 | 27.00 | 370.60 | 362.73 | NÃO | fora da faixa vertical |
| 60 | 257.00 | 27.00 | 370.35 | 362.73 | NÃO | fora da faixa vertical |
| 61 | 256.00 | 28.00 | 369.14 | 361.73 | NÃO | fora da faixa vertical |
| 62 | 255.00 | 28.00 | 368.90 | 361.73 | NÃO | fora da faixa vertical |
| 63 | 254.00 | 29.00 | 367.69 | 360.73 | NÃO | fora da faixa vertical |
| 64 | 253.00 | 29.00 | 367.45 | 360.73 | NÃO | fora da faixa vertical |
| 65 | 252.00 | 29.00 | 367.21 | 360.73 | NÃO | fora da faixa vertical |
| 66 | 251.00 | 30.00 | 366.01 | 359.73 | NÃO | fora da faixa vertical |
| 67 | 250.00 | 30.00 | 365.78 | 359.73 | NÃO | fora da faixa vertical |
| 68 | 249.00 | 31.00 | 364.57 | 358.73 | NÃO | fora da faixa vertical |
| 69 | 248.00 | 31.00 | 364.35 | 358.73 | NÃO | fora da faixa vertical |
| 70 | 247.00 | 32.00 | 363.15 | 357.73 | NÃO | fora da faixa vertical |
| 71 | 246.00 | 32.00 | 362.93 | 357.73 | NÃO | fora da faixa vertical |
| 72 | 245.00 | 33.00 | 361.73 | 356.73 | NÃO | fora da faixa vertical |
| 73 | 244.00 | 33.00 | 361.51 | 356.73 | NÃO | fora da faixa vertical |
| 74 | 243.00 | 34.00 | 360.32 | 355.73 | NÃO | fora da faixa vertical |
| 75 | 242.00 | 34.00 | 360.11 | 355.73 | NÃO | fora da faixa vertical |
| 76 | 241.00 | 35.00 | 358.92 | 354.73 | NÃO | fora da faixa vertical |
| 77 | 240.00 | 35.00 | 358.72 | 354.73 | NÃO | fora da faixa vertical |
| 78 | 239.00 | 36.00 | 357.53 | 353.73 | NÃO | fora da faixa vertical |
| 79 | 238.00 | 36.00 | 357.33 | 353.73 | NÃO | fora da faixa vertical |
| 80 | 237.00 | 37.00 | 356.15 | 352.73 | NÃO | fora da faixa vertical |
| 81 | 236.00 | 37.00 | 355.95 | 352.73 | NÃO | fora da faixa vertical |
| 82 | 235.00 | 38.00 | 354.77 | 351.73 | NÃO | fora da faixa vertical |
| 83 | 234.00 | 38.00 | 354.58 | 351.73 | NÃO | fora da faixa vertical |
| 84 | 233.00 | 39.00 | 353.41 | 350.73 | NÃO | fora da faixa vertical |
| 85 | 232.00 | 40.00 | 352.24 | 349.73 | NÃO | fora da faixa vertical |
| 86 | 231.00 | 40.00 | 352.05 | 349.73 | NÃO | fora da faixa vertical |
| 87 | 230.00 | 41.00 | 350.89 | 348.73 | NÃO | fora da faixa vertical |
| 88 | 229.00 | 41.00 | 350.71 | 348.73 | NÃO | fora da faixa vertical |
| 89 | 228.00 | 42.00 | 349.54 | 347.73 | NÃO | fora da faixa vertical |
| 90 | 227.00 | 43.00 | 348.38 | 346.73 | NÃO | fora da faixa vertical |
| 91 | 226.00 | 43.00 | 348.21 | 346.73 | NÃO | fora da faixa vertical |
| 92 | 225.00 | 44.00 | 347.05 | 345.73 | NÃO | fora da faixa vertical |
| 93 | 224.00 | 44.00 | 346.88 | 345.73 | NÃO | fora da faixa vertical |
| 94 | 223.00 | 45.00 | 345.73 | 344.73 | NÃO | fora da faixa vertical |
| 95 | 222.00 | 46.00 | 344.58 | 343.73 | NÃO | fora da faixa vertical |
| 96 | 221.00 | 46.00 | 344.42 | 343.73 | NÃO | fora da faixa vertical |
| 97 | 220.00 | 47.00 | 343.27 | 342.73 | NÃO | fora da faixa vertical |
| 98 | 219.00 | 48.00 | 342.13 | 341.73 | NÃO | fora da faixa vertical |
| 99 | 218.00 | 48.00 | 341.98 | 341.73 | NÃO | fora da faixa vertical |
| 100 | 217.00 | 49.00 | 340.84 | 340.73 | NÃO | fora da faixa vertical |
| 101 | 216.00 | 50.00 | 339.70 | 339.73 | NÃO | fora da faixa vertical |
| 102 | 215.00 | 50.00 | 339.55 | 339.73 | NÃO | fora da faixa vertical |
| 103 | 214.00 | 51.00 | 338.42 | 338.73 | NÃO | fora da faixa vertical |
| 104 | 213.00 | 52.00 | 337.29 | 337.73 | NÃO | fora da faixa vertical |
| 105 | 212.00 | 53.00 | 336.16 | 336.73 | NÃO | fora da faixa vertical |
| 106 | 211.00 | 53.00 | 336.03 | 336.73 | NÃO | fora da faixa vertical |
| 107 | 210.00 | 54.00 | 334.90 | 335.73 | NÃO | fora da faixa vertical |
| 108 | 209.00 | 55.00 | 333.78 | 334.73 | NÃO | fora da faixa vertical |
| 109 | 208.00 | 56.00 | 332.66 | 333.73 | NÃO | fora da faixa vertical |
| 110 | 207.00 | 56.00 | 332.54 | 333.73 | NÃO | fora da faixa vertical |
| 111 | 206.00 | 57.00 | 331.42 | 332.73 | NÃO | fora da faixa vertical |
| 112 | 205.00 | 58.00 | 330.31 | 331.73 | NÃO | fora da faixa vertical |
| 113 | 204.00 | 59.00 | 329.20 | 330.73 | NÃO | fora da faixa vertical |
| 114 | 203.00 | 59.00 | 329.09 | 330.73 | NÃO | fora da faixa vertical |
| 115 | 202.00 | 60.00 | 327.98 | 329.73 | NÃO | fora da faixa vertical |
| 116 | 201.00 | 61.00 | 326.88 | 328.73 | NÃO | fora da faixa vertical |
| 117 | 200.00 | 62.00 | 325.78 | 327.73 | NÃO | fora da faixa vertical |
| 118 | 199.00 | 63.00 | 324.68 | 326.73 | NÃO | fora da faixa vertical |
| 119 | 198.00 | 64.00 | 323.59 | 325.73 | NÃO | fora da faixa vertical |
| 120 | 197.00 | 65.00 | 322.49 | 324.73 | NÃO | fora da faixa vertical |
| 121 | 196.00 | 66.00 | 321.40 | 323.73 | NÃO | fora da faixa vertical |
| 122 | 195.00 | 67.00 | 320.32 | 322.73 | NÃO | fora da faixa vertical |
| 123 | 194.00 | 68.00 | 319.23 | 321.73 | NÃO | fora da faixa vertical |
| 124 | 193.00 | 69.00 | 318.15 | 320.73 | NÃO | fora da faixa vertical |
| 125 | 192.00 | 69.00 | 318.06 | 320.73 | NÃO | fora da faixa vertical |
| 126 | 191.00 | 70.00 | 316.99 | 319.73 | NÃO | fora da faixa vertical |
| 127 | 190.00 | 71.00 | 315.91 | 318.73 | NÃO | fora da faixa vertical |
| 128 | 189.00 | 72.00 | 314.84 | 317.73 | NÃO | fora da faixa vertical |
| 129 | 188.00 | 73.00 | 313.77 | 316.73 | NÃO | fora da faixa vertical |
| 130 | 188.00 | 74.00 | 312.77 | 315.73 | NÃO | fora da faixa vertical |
| 131 | 187.00 | 75.00 | 311.71 | 314.73 | NÃO | fora da faixa vertical |
| 132 | 186.00 | 76.00 | 310.64 | 313.73 | NÃO | fora da faixa vertical |
| 133 | 185.00 | 77.00 | 309.58 | 312.73 | NÃO | fora da faixa vertical |
| 134 | 184.00 | 78.00 | 308.53 | 311.73 | NÃO | fora da faixa vertical |
| 135 | 183.00 | 79.00 | 307.47 | 310.73 | NÃO | fora da faixa vertical |
| 136 | 182.00 | 80.00 | 306.42 | 309.73 | NÃO | fora da faixa vertical |
| 137 | 181.00 | 81.00 | 305.37 | 308.73 | NÃO | fora da faixa vertical |
| 138 | 180.00 | 82.00 | 304.32 | 307.73 | NÃO | fora da faixa vertical |
| 139 | 179.00 | 83.00 | 303.28 | 306.73 | NÃO | fora da faixa vertical |
| 140 | 179.00 | 84.00 | 302.28 | 305.73 | NÃO | fora da faixa vertical |
| 141 | 178.00 | 85.00 | 301.24 | 304.73 | NÃO | fora da faixa vertical |
| 142 | 177.00 | 86.00 | 300.20 | 303.73 | NÃO | fora da faixa vertical |
| 143 | 176.00 | 87.00 | 299.17 | 302.73 | NÃO | fora da faixa vertical |
| 144 | 175.00 | 88.00 | 298.14 | 301.73 | NÃO | fora da faixa vertical |
| 145 | 174.00 | 89.00 | 297.11 | 300.73 | NÃO | fora da faixa vertical |
| 146 | 174.00 | 90.00 | 296.11 | 299.73 | NÃO | fora da faixa vertical |
| 147 | 173.00 | 91.00 | 295.08 | 298.73 | NÃO | fora da faixa vertical |
| 148 | 172.00 | 92.00 | 294.06 | 297.73 | NÃO | fora da faixa vertical |
| 149 | 171.00 | 93.00 | 293.04 | 296.73 | NÃO | fora da faixa vertical |
| 150 | 171.00 | 94.00 | 292.04 | 295.73 | NÃO | fora da faixa vertical |
| 151 | 170.00 | 95.00 | 291.03 | 294.73 | NÃO | fora da faixa vertical |
| 152 | 169.00 | 96.00 | 290.02 | 293.73 | NÃO | fora da faixa vertical |
| 153 | 168.00 | 97.00 | 289.01 | 292.73 | NÃO | fora da faixa vertical |
| 154 | 168.00 | 98.00 | 288.01 | 291.73 | NÃO | fora da faixa vertical |
| 155 | 167.00 | 99.00 | 287.00 | 290.73 | NÃO | fora da faixa vertical |
| 156 | 166.00 | 100.00 | 286.00 | 289.73 | NÃO | fora da faixa vertical |
| 157 | 165.00 | 101.00 | 285.00 | 288.73 | NÃO | fora da faixa vertical |
| 158 | 165.00 | 102.00 | 284.00 | 287.73 | NÃO | fora da faixa vertical |
| 159 | 164.00 | 103.00 | 283.01 | 286.73 | NÃO | fora da faixa vertical |
| 160 | 163.00 | 104.00 | 282.02 | 285.73 | NÃO | fora da faixa vertical |
| 161 | 163.00 | 105.00 | 281.02 | 284.73 | NÃO | fora da faixa vertical |
| 162 | 162.00 | 106.00 | 280.03 | 283.73 | NÃO | fora da faixa vertical |
| 163 | 161.00 | 107.00 | 279.04 | 282.73 | NÃO | fora da faixa vertical |
| 164 | 161.00 | 108.00 | 278.04 | 281.73 | NÃO | fora da faixa vertical |
| 165 | 160.00 | 109.00 | 277.06 | 280.73 | NÃO | fora da faixa vertical |
| 166 | 160.00 | 110.00 | 276.07 | 279.73 | NÃO | fora da faixa vertical |
| 167 | 159.00 | 111.00 | 275.09 | 278.73 | NÃO | fora da faixa vertical |
| 168 | 158.00 | 112.00 | 274.12 | 277.73 | NÃO | fora da faixa vertical |
| 169 | 158.00 | 113.00 | 273.12 | 276.73 | NÃO | fora da faixa vertical |
| 170 | 157.00 | 114.00 | 272.15 | 275.73 | NÃO | fora da faixa vertical |
| 171 | 157.00 | 115.00 | 271.15 | 274.73 | NÃO | fora da faixa vertical |
| 172 | 156.00 | 116.00 | 270.19 | 273.73 | NÃO | fora da faixa vertical |
| 173 | 155.00 | 117.00 | 269.22 | 272.73 | NÃO | fora da faixa vertical |
| 174 | 155.00 | 118.00 | 268.23 | 271.73 | NÃO | fora da faixa vertical |
| 175 | 154.00 | 119.00 | 267.27 | 270.73 | NÃO | fora da faixa vertical |
| 176 | 154.00 | 120.00 | 266.27 | 269.73 | NÃO | fora da faixa vertical |
| 177 | 153.00 | 121.00 | 265.32 | 268.73 | NÃO | fora da faixa vertical |
| 178 | 153.00 | 122.00 | 264.32 | 267.73 | NÃO | fora da faixa vertical |
| 179 | 152.00 | 123.00 | 263.37 | 266.73 | NÃO | fora da faixa vertical |
| 180 | 152.00 | 124.00 | 262.37 | 265.73 | NÃO | fora da faixa vertical |
| 181 | 151.00 | 125.00 | 261.43 | 264.73 | NÃO | fora da faixa vertical |
| 182 | 151.00 | 126.00 | 260.43 | 263.73 | NÃO | fora da faixa vertical |
| 183 | 150.00 | 127.00 | 259.49 | 262.73 | NÃO | fora da faixa vertical |
| 184 | 150.00 | 128.00 | 258.50 | 261.73 | NÃO | fora da faixa vertical |
| 185 | 149.00 | 129.00 | 257.56 | 260.73 | NÃO | fora da faixa vertical |
| 186 | 149.00 | 130.00 | 256.56 | 259.73 | NÃO | fora da faixa vertical |
| 187 | 148.00 | 131.00 | 255.63 | 258.73 | NÃO | fora da faixa vertical |
| 188 | 148.00 | 132.00 | 254.64 | 257.73 | NÃO | fora da faixa vertical |
| 189 | 147.00 | 133.00 | 253.71 | 256.73 | NÃO | fora da faixa vertical |
| 190 | 147.00 | 134.00 | 252.72 | 255.73 | NÃO | fora da faixa vertical |
| 191 | 146.00 | 135.00 | 251.80 | 254.73 | NÃO | fora da faixa vertical |
| 192 | 146.00 | 136.00 | 250.80 | 253.73 | NÃO | fora da faixa vertical |
| 193 | 146.00 | 137.00 | 249.80 | 252.73 | NÃO | fora da faixa vertical |
| 194 | 145.00 | 138.00 | 248.89 | 251.73 | NÃO | fora da faixa vertical |
| 195 | 145.00 | 139.00 | 247.89 | 250.73 | NÃO | fora da faixa vertical |
| 196 | 144.00 | 140.00 | 246.98 | 249.73 | NÃO | fora da faixa vertical |
| 197 | 144.00 | 141.00 | 245.99 | 248.73 | NÃO | fora da faixa vertical |
| 198 | 144.00 | 142.00 | 244.99 | 247.73 | NÃO | fora da faixa vertical |
| 199 | 143.00 | 143.00 | 244.09 | 246.73 | NÃO | fora da faixa vertical |
| 200 | 143.00 | 144.00 | 243.09 | 245.73 | NÃO | fora da faixa vertical |
| 201 | 143.00 | 145.00 | 242.10 | 244.73 | NÃO | fora da faixa vertical |
| 202 | 142.00 | 146.00 | 241.20 | 243.73 | NÃO | fora da faixa vertical |
| 203 | 142.00 | 147.00 | 240.20 | 242.73 | NÃO | fora da faixa vertical |
| 204 | 141.00 | 148.00 | 239.31 | 241.73 | NÃO | fora da faixa vertical |
| 205 | 141.00 | 149.00 | 238.31 | 240.73 | NÃO | fora da faixa vertical |
| 206 | 141.00 | 150.00 | 237.32 | 239.73 | NÃO | fora da faixa vertical |
| 207 | 140.00 | 151.00 | 236.43 | 238.73 | NÃO | fora da faixa vertical |
| 208 | 140.00 | 152.00 | 235.44 | 237.73 | NÃO | fora da faixa vertical |
| 209 | 140.00 | 153.00 | 234.45 | 236.73 | NÃO | fora da faixa vertical |
| 210 | 139.00 | 154.00 | 233.57 | 235.73 | NÃO | fora da faixa vertical |
| 211 | 139.00 | 155.00 | 232.57 | 234.73 | NÃO | fora da faixa vertical |
| 212 | 139.00 | 156.00 | 231.58 | 233.73 | NÃO | fora da faixa vertical |
| 213 | 139.00 | 157.00 | 230.59 | 232.73 | NÃO | fora da faixa vertical |
| 214 | 138.00 | 158.00 | 229.71 | 231.73 | NÃO | fora da faixa vertical |
| 215 | 138.00 | 159.00 | 228.72 | 230.73 | NÃO | fora da faixa vertical |
| 216 | 138.00 | 160.00 | 227.73 | 229.73 | NÃO | fora da faixa vertical |
| 217 | 137.00 | 161.00 | 226.86 | 228.73 | NÃO | fora da faixa vertical |
| 218 | 137.00 | 162.00 | 225.87 | 227.73 | NÃO | fora da faixa vertical |
| 219 | 137.00 | 163.00 | 224.88 | 226.73 | NÃO | fora da faixa vertical |
| 220 | 137.00 | 164.00 | 223.89 | 225.73 | NÃO | fora da faixa vertical |
| 221 | 136.00 | 165.00 | 223.03 | 224.73 | NÃO | fora da faixa vertical |
| 222 | 136.00 | 166.00 | 222.04 | 223.73 | NÃO | fora da faixa vertical |
| 223 | 136.00 | 167.00 | 221.05 | 222.73 | NÃO | fora da faixa vertical |
| 224 | 136.00 | 168.00 | 220.05 | 221.73 | NÃO | fora da faixa vertical |
| 225 | 135.00 | 169.00 | 219.20 | 220.73 | NÃO | fora da faixa vertical |
| 226 | 135.00 | 170.00 | 218.21 | 219.73 | NÃO | fora da faixa vertical |
| 227 | 135.00 | 171.00 | 217.22 | 218.73 | NÃO | fora da faixa vertical |
| 228 | 135.00 | 172.00 | 216.23 | 217.73 | NÃO | fora da faixa vertical |
| 229 | 135.00 | 173.00 | 215.24 | 216.73 | NÃO | fora da faixa vertical |
| 230 | 134.00 | 174.00 | 214.40 | 215.73 | NÃO | fora da faixa vertical |
| 231 | 134.00 | 175.00 | 213.41 | 214.73 | NÃO | fora da faixa vertical |
| 232 | 134.00 | 176.00 | 212.42 | 213.73 | NÃO | fora da faixa vertical |
| 233 | 134.00 | 177.00 | 211.44 | 212.73 | NÃO | fora da faixa vertical |
| 234 | 134.00 | 178.00 | 210.45 | 211.73 | NÃO | fora da faixa vertical |
| 235 | 133.00 | 179.00 | 209.61 | 210.73 | NÃO | fora da faixa vertical |
| 236 | 133.00 | 180.00 | 208.63 | 209.73 | NÃO | fora da faixa vertical |
| 237 | 133.00 | 181.00 | 207.64 | 208.73 | NÃO | fora da faixa vertical |
| 238 | 133.00 | 182.00 | 206.65 | 207.73 | NÃO | fora da faixa vertical |
| 239 | 133.00 | 183.00 | 205.66 | 206.73 | NÃO | fora da faixa vertical |
| 240 | 132.00 | 184.00 | 204.84 | 205.73 | NÃO | fora da faixa vertical |
| 241 | 132.00 | 185.00 | 203.86 | 204.73 | SIM | dentro da janela vertical e do lado solicitado |
| 242 | 132.00 | 186.00 | 202.87 | 203.73 | SIM | dentro da janela vertical e do lado solicitado |
| 243 | 132.00 | 187.00 | 201.88 | 202.73 | SIM | dentro da janela vertical e do lado solicitado |
| 244 | 132.00 | 188.00 | 200.90 | 201.73 | SIM | dentro da janela vertical e do lado solicitado |
| 245 | 132.00 | 189.00 | 199.91 | 200.73 | SIM | dentro da janela vertical e do lado solicitado |
| 246 | 132.00 | 190.00 | 198.93 | 199.73 | SIM | dentro da janela vertical e do lado solicitado |
| 247 | 132.00 | 191.00 | 197.94 | 198.73 | SIM | dentro da janela vertical e do lado solicitado |
| 248 | 131.00 | 192.00 | 197.13 | 197.73 | SIM | dentro da janela vertical e do lado solicitado |
| 249 | 131.00 | 193.00 | 196.15 | 196.73 | SIM | dentro da janela vertical e do lado solicitado |
| 250 | 131.00 | 194.00 | 195.16 | 195.73 | SIM | dentro da janela vertical e do lado solicitado |
| 251 | 131.00 | 195.00 | 194.18 | 194.73 | SIM | dentro da janela vertical e do lado solicitado |
| 252 | 131.00 | 196.00 | 193.20 | 193.73 | SIM | dentro da janela vertical e do lado solicitado |
| 253 | 131.00 | 197.00 | 192.21 | 192.73 | SIM | dentro da janela vertical e do lado solicitado |
| 254 | 131.00 | 198.00 | 191.23 | 191.73 | SIM | dentro da janela vertical e do lado solicitado |
| 255 | 131.00 | 199.00 | 190.25 | 190.73 | SIM | dentro da janela vertical e do lado solicitado |
| 256 | 130.00 | 200.00 | 189.45 | 189.73 | SIM | dentro da janela vertical e do lado solicitado |
| 257 | 130.00 | 201.00 | 188.47 | 188.73 | SIM | dentro da janela vertical e do lado solicitado |
| 258 | 130.00 | 202.00 | 187.49 | 187.73 | SIM | dentro da janela vertical e do lado solicitado |
| 259 | 130.00 | 203.00 | 186.51 | 186.73 | SIM | dentro da janela vertical e do lado solicitado |
| 260 | 130.00 | 204.00 | 185.53 | 185.73 | SIM | dentro da janela vertical e do lado solicitado |
| 261 | 130.00 | 205.00 | 184.55 | 184.73 | SIM | dentro da janela vertical e do lado solicitado |
| 262 | 130.00 | 206.00 | 183.56 | 183.73 | SIM | dentro da janela vertical e do lado solicitado |
| 263 | 130.00 | 207.00 | 182.58 | 182.73 | SIM | dentro da janela vertical e do lado solicitado |
| 264 | 130.00 | 208.00 | 181.60 | 181.73 | SIM | dentro da janela vertical e do lado solicitado |
| 265 | 130.00 | 209.00 | 180.62 | 180.73 | SIM | dentro da janela vertical e do lado solicitado |
| 266 | 130.00 | 210.00 | 179.64 | 179.73 | SIM | dentro da janela vertical e do lado solicitado |
| 267 | 130.00 | 211.00 | 178.66 | 178.73 | SIM | dentro da janela vertical e do lado solicitado |
| 268 | 130.00 | 212.00 | 177.69 | 177.73 | SIM | dentro da janela vertical e do lado solicitado |
| 269 | 130.00 | 213.00 | 176.71 | 176.73 | SIM | dentro da janela vertical e do lado solicitado |
| 270 | 130.00 | 214.00 | 175.73 | 175.73 | SIM | dentro da janela vertical e do lado solicitado |
| 271 | 130.00 | 215.00 | 174.75 | 174.73 | SIM | dentro da janela vertical e do lado solicitado |
| 272 | 130.00 | 216.00 | 173.77 | 173.73 | SIM | dentro da janela vertical e do lado solicitado |
| 273 | 130.00 | 217.00 | 172.79 | 172.73 | SIM | dentro da janela vertical e do lado solicitado |
| 274 | 130.00 | 218.00 | 171.81 | 171.73 | SIM | dentro da janela vertical e do lado solicitado |
| 275 | 130.00 | 219.00 | 170.84 | 170.73 | SIM | dentro da janela vertical e do lado solicitado |
| 276 | 130.00 | 220.00 | 169.86 | 169.73 | SIM | dentro da janela vertical e do lado solicitado |
| 277 | 130.00 | 221.00 | 168.88 | 168.73 | SIM | dentro da janela vertical e do lado solicitado |
| 278 | 130.00 | 222.00 | 167.90 | 167.73 | SIM | dentro da janela vertical e do lado solicitado |
| 279 | 130.00 | 223.00 | 166.93 | 166.73 | SIM | dentro da janela vertical e do lado solicitado |
| 280 | 130.00 | 224.00 | 165.95 | 165.73 | SIM | dentro da janela vertical e do lado solicitado |
| 281 | 130.00 | 225.00 | 164.98 | 164.73 | SIM | dentro da janela vertical e do lado solicitado |
| 282 | 130.00 | 226.00 | 164.00 | 163.73 | SIM | dentro da janela vertical e do lado solicitado |
| 283 | 130.00 | 227.00 | 163.02 | 162.73 | SIM | dentro da janela vertical e do lado solicitado |
| 284 | 130.00 | 228.00 | 162.05 | 161.73 | SIM | dentro da janela vertical e do lado solicitado |
| 285 | 130.00 | 229.00 | 161.07 | 160.73 | SIM | dentro da janela vertical e do lado solicitado |
| 286 | 130.00 | 230.00 | 160.10 | 159.73 | SIM | dentro da janela vertical e do lado solicitado |
| 287 | 130.00 | 231.00 | 159.13 | 158.73 | SIM | dentro da janela vertical e do lado solicitado |
| 288 | 131.00 | 232.00 | 157.93 | 157.73 | SIM | dentro da janela vertical e do lado solicitado |
| 289 | 131.00 | 233.00 | 156.95 | 156.73 | SIM | dentro da janela vertical e do lado solicitado |
| 290 | 131.00 | 234.00 | 155.98 | 155.73 | SIM | dentro da janela vertical e do lado solicitado |
| 291 | 131.00 | 235.00 | 155.00 | 154.73 | SIM | dentro da janela vertical e do lado solicitado |
| 292 | 131.00 | 236.00 | 154.03 | 153.73 | SIM | dentro da janela vertical e do lado solicitado |
| 293 | 131.00 | 237.00 | 153.06 | 152.73 | SIM | dentro da janela vertical e do lado solicitado |
| 294 | 131.00 | 238.00 | 152.08 | 151.73 | SIM | dentro da janela vertical e do lado solicitado |
| 295 | 131.00 | 239.00 | 151.11 | 150.73 | SIM | dentro da janela vertical e do lado solicitado |
| 296 | 131.00 | 240.00 | 150.14 | 149.73 | SIM | dentro da janela vertical e do lado solicitado |
| 297 | 132.00 | 241.00 | 148.93 | 148.73 | SIM | dentro da janela vertical e do lado solicitado |
| 298 | 132.00 | 242.00 | 147.96 | 147.73 | SIM | dentro da janela vertical e do lado solicitado |
| 299 | 132.00 | 243.00 | 146.99 | 146.73 | SIM | dentro da janela vertical e do lado solicitado |
| 300 | 132.00 | 244.00 | 146.01 | 145.73 | SIM | dentro da janela vertical e do lado solicitado |
| 301 | 132.00 | 245.00 | 145.04 | 144.73 | SIM | dentro da janela vertical e do lado solicitado |
| 302 | 132.00 | 246.00 | 144.07 | 143.73 | SIM | dentro da janela vertical e do lado solicitado |
| 303 | 132.00 | 247.00 | 143.10 | 142.73 | SIM | dentro da janela vertical e do lado solicitado |
| 304 | 133.00 | 248.00 | 141.89 | 141.73 | SIM | dentro da janela vertical e do lado solicitado |
| 305 | 133.00 | 249.00 | 140.92 | 140.73 | SIM | dentro da janela vertical e do lado solicitado |
| 306 | 133.00 | 250.00 | 139.95 | 139.73 | SIM | dentro da janela vertical e do lado solicitado |
| 307 | 133.00 | 251.00 | 138.97 | 138.73 | SIM | dentro da janela vertical e do lado solicitado |
| 308 | 133.00 | 252.00 | 138.00 | 137.73 | SIM | dentro da janela vertical e do lado solicitado |
| 309 | 134.00 | 253.00 | 136.80 | 136.73 | SIM | dentro da janela vertical e do lado solicitado |
| 310 | 134.00 | 254.00 | 135.82 | 135.73 | SIM | dentro da janela vertical e do lado solicitado |
| 311 | 134.00 | 255.00 | 134.85 | 134.73 | SIM | dentro da janela vertical e do lado solicitado |
| 312 | 134.00 | 256.00 | 133.88 | 133.73 | SIM | dentro da janela vertical e do lado solicitado |
| 313 | 134.00 | 257.00 | 132.91 | 132.73 | SIM | dentro da janela vertical e do lado solicitado |
| 314 | 135.00 | 258.00 | 131.70 | 131.73 | SIM | dentro da janela vertical e do lado solicitado |
| 315 | 135.00 | 259.00 | 130.73 | 130.73 | SIM | dentro da janela vertical e do lado solicitado |
| 316 | 135.00 | 260.00 | 129.76 | 129.73 | SIM | dentro da janela vertical e do lado solicitado |
| 317 | 135.00 | 261.00 | 128.79 | 128.73 | SIM | dentro da janela vertical e do lado solicitado |
| 318 | 135.00 | 262.00 | 127.82 | 127.73 | SIM | dentro da janela vertical e do lado solicitado |
| 319 | 136.00 | 263.00 | 126.61 | 126.73 | SIM | dentro da janela vertical e do lado solicitado |
| 320 | 136.00 | 264.00 | 125.63 | 125.73 | SIM | dentro da janela vertical e do lado solicitado |
| 321 | 136.00 | 265.00 | 124.66 | 124.73 | SIM | dentro da janela vertical e do lado solicitado |
| 322 | 136.00 | 266.00 | 123.69 | 123.73 | SIM | dentro da janela vertical e do lado solicitado |
| 323 | 137.00 | 267.00 | 122.48 | 122.73 | SIM | dentro da janela vertical e do lado solicitado |
| 324 | 137.00 | 268.00 | 121.51 | 121.73 | SIM | dentro da janela vertical e do lado solicitado |
| 325 | 137.00 | 269.00 | 120.54 | 120.73 | SIM | dentro da janela vertical e do lado solicitado |
| 326 | 137.00 | 270.00 | 119.57 | 119.73 | SIM | dentro da janela vertical e do lado solicitado |
| 327 | 138.00 | 271.00 | 118.36 | 118.73 | SIM | dentro da janela vertical e do lado solicitado |
| 328 | 138.00 | 272.00 | 117.39 | 117.73 | SIM | dentro da janela vertical e do lado solicitado |
| 329 | 138.00 | 273.00 | 116.42 | 116.73 | SIM | dentro da janela vertical e do lado solicitado |
| 330 | 139.00 | 274.00 | 115.21 | 115.73 | SIM | dentro da janela vertical e do lado solicitado |
| 331 | 139.00 | 275.00 | 114.24 | 114.73 | SIM | dentro da janela vertical e do lado solicitado |
| 332 | 139.00 | 276.00 | 113.27 | 113.73 | SIM | dentro da janela vertical e do lado solicitado |
| 333 | 139.00 | 277.00 | 112.29 | 112.73 | SIM | dentro da janela vertical e do lado solicitado |
| 334 | 140.00 | 278.00 | 111.09 | 111.73 | SIM | dentro da janela vertical e do lado solicitado |
| 335 | 140.00 | 279.00 | 110.11 | 110.73 | SIM | dentro da janela vertical e do lado solicitado |
| 336 | 140.00 | 280.00 | 109.14 | 109.73 | SIM | dentro da janela vertical e do lado solicitado |
| 337 | 141.00 | 281.00 | 107.94 | 108.73 | SIM | dentro da janela vertical e do lado solicitado |
| 338 | 141.00 | 282.00 | 106.96 | 107.73 | SIM | dentro da janela vertical e do lado solicitado |
| 339 | 141.00 | 283.00 | 105.99 | 106.73 | SIM | dentro da janela vertical e do lado solicitado |
| 340 | 142.00 | 284.00 | 104.79 | 105.73 | SIM | dentro da janela vertical e do lado solicitado |
| 341 | 142.00 | 285.00 | 103.81 | 104.73 | SIM | dentro da janela vertical e do lado solicitado |
| 342 | 142.00 | 286.00 | 102.84 | 103.73 | SIM | dentro da janela vertical e do lado solicitado |
| 343 | 143.00 | 287.00 | 101.64 | 102.73 | SIM | dentro da janela vertical e do lado solicitado |
| 344 | 143.00 | 288.00 | 100.66 | 101.73 | SIM | dentro da janela vertical e do lado solicitado |
| 345 | 144.00 | 289.00 | 99.46 | 100.73 | SIM | dentro da janela vertical e do lado solicitado |
| 346 | 144.00 | 290.00 | 98.49 | 99.73 | SIM | dentro da janela vertical e do lado solicitado |
| 347 | 144.00 | 291.00 | 97.51 | 98.73 | SIM | dentro da janela vertical e do lado solicitado |
| 348 | 145.00 | 292.00 | 96.32 | 97.73 | SIM | dentro da janela vertical e do lado solicitado |
| 349 | 145.00 | 293.00 | 95.34 | 96.73 | SIM | dentro da janela vertical e do lado solicitado |
| 350 | 145.00 | 294.00 | 94.37 | 95.73 | SIM | dentro da janela vertical e do lado solicitado |
| 351 | 146.00 | 295.00 | 93.17 | 94.73 | SIM | dentro da janela vertical e do lado solicitado |
| 352 | 146.00 | 296.00 | 92.20 | 93.73 | SIM | dentro da janela vertical e do lado solicitado |
| 353 | 147.00 | 297.00 | 91.01 | 92.73 | SIM | dentro da janela vertical e do lado solicitado |
| 354 | 147.00 | 298.00 | 90.03 | 91.73 | SIM | dentro da janela vertical e do lado solicitado |
| 355 | 148.00 | 299.00 | 88.84 | 90.73 | SIM | dentro da janela vertical e do lado solicitado |
| 356 | 148.00 | 300.00 | 87.86 | 89.73 | SIM | dentro da janela vertical e do lado solicitado |
| 357 | 149.00 | 301.00 | 86.68 | 88.73 | SIM | dentro da janela vertical e do lado solicitado |
| 358 | 149.00 | 302.00 | 85.70 | 87.73 | SIM | dentro da janela vertical e do lado solicitado |
| 359 | 150.00 | 303.00 | 84.53 | 86.73 | SIM | dentro da janela vertical e do lado solicitado |
| 360 | 150.00 | 304.00 | 83.55 | 85.73 | SIM | dentro da janela vertical e do lado solicitado |
| 361 | 151.00 | 305.00 | 82.38 | 84.73 | SIM | dentro da janela vertical e do lado solicitado |
| 362 | 151.00 | 306.00 | 81.39 | 83.73 | SIM | dentro da janela vertical e do lado solicitado |
| 363 | 152.00 | 307.00 | 80.23 | 82.73 | SIM | dentro da janela vertical e do lado solicitado |
| 364 | 152.00 | 308.00 | 79.25 | 81.73 | SIM | dentro da janela vertical e do lado solicitado |
| 365 | 153.00 | 309.00 | 78.09 | 80.73 | SIM | dentro da janela vertical e do lado solicitado |
| 366 | 153.00 | 310.00 | 77.10 | 79.73 | SIM | dentro da janela vertical e do lado solicitado |
| 367 | 154.00 | 311.00 | 75.95 | 78.73 | SIM | dentro da janela vertical e do lado solicitado |
| 368 | 154.00 | 312.00 | 74.97 | 77.73 | SIM | dentro da janela vertical e do lado solicitado |
| 369 | 155.00 | 313.00 | 73.82 | 76.73 | SIM | dentro da janela vertical e do lado solicitado |
| 370 | 155.00 | 314.00 | 72.84 | 75.73 | SIM | dentro da janela vertical e do lado solicitado |
| 371 | 156.00 | 315.00 | 71.70 | 74.73 | SIM | dentro da janela vertical e do lado solicitado |
| 372 | 157.00 | 316.00 | 70.58 | 73.73 | SIM | dentro da janela vertical e do lado solicitado |
| 373 | 157.00 | 317.00 | 69.58 | 72.73 | SIM | dentro da janela vertical e do lado solicitado |
| 374 | 158.00 | 318.00 | 68.47 | 71.73 | SIM | dentro da janela vertical e do lado solicitado |
| 375 | 158.00 | 319.00 | 67.48 | 70.73 | SIM | dentro da janela vertical e do lado solicitado |
| 376 | 159.00 | 320.00 | 66.37 | 69.73 | SIM | dentro da janela vertical e do lado solicitado |
| 377 | 160.00 | 321.00 | 65.28 | 68.73 | SIM | dentro da janela vertical e do lado solicitado |
| 378 | 160.00 | 322.00 | 64.28 | 67.73 | SIM | dentro da janela vertical e do lado solicitado |
| 379 | 161.00 | 323.00 | 63.20 | 66.73 | SIM | dentro da janela vertical e do lado solicitado |
| 380 | 161.00 | 324.00 | 62.20 | 65.73 | SIM | dentro da janela vertical e do lado solicitado |
| 381 | 162.00 | 325.00 | 61.13 | 64.73 | SIM | dentro da janela vertical e do lado solicitado |
| 382 | 163.00 | 326.00 | 60.07 | 63.73 | SIM | dentro da janela vertical e do lado solicitado |
| 383 | 163.00 | 327.00 | 59.08 | 62.73 | SIM | dentro da janela vertical e do lado solicitado |
| 384 | 164.00 | 328.00 | 58.03 | 61.73 | SIM | dentro da janela vertical e do lado solicitado |
| 385 | 165.00 | 329.00 | 57.01 | 60.73 | SIM | dentro da janela vertical e do lado solicitado |
| 386 | 165.00 | 330.00 | 56.01 | 59.73 | SIM | dentro da janela vertical e do lado solicitado |
| 387 | 166.00 | 331.00 | 55.00 | 58.73 | SIM | dentro da janela vertical e do lado solicitado |
| 388 | 167.00 | 332.00 | 54.01 | 57.73 | SIM | dentro da janela vertical e do lado solicitado |
| 389 | 167.00 | 333.00 | 53.01 | 56.73 | SIM | dentro da janela vertical e do lado solicitado |
| 390 | 168.00 | 334.00 | 52.04 | 55.73 | SIM | dentro da janela vertical e do lado solicitado |
| 391 | 169.00 | 335.00 | 51.09 | 54.73 | SIM | dentro da janela vertical e do lado solicitado |
| 392 | 170.00 | 336.00 | 50.16 | 53.73 | SIM | dentro da janela vertical e do lado solicitado |
| 393 | 170.00 | 337.00 | 49.16 | 52.73 | SIM | dentro da janela vertical e do lado solicitado |
| 394 | 171.00 | 338.00 | 48.26 | 51.73 | SIM | dentro da janela vertical e do lado solicitado |
| 395 | 172.00 | 339.00 | 47.38 | 50.73 | SIM | dentro da janela vertical e do lado solicitado |
| 396 | 173.00 | 340.00 | 46.53 | 49.73 | SIM | dentro da janela vertical e do lado solicitado |
| 397 | 173.00 | 341.00 | 45.54 | 48.73 | SIM | dentro da janela vertical e do lado solicitado |
| 398 | 174.00 | 342.00 | 44.72 | 47.73 | SIM | dentro da janela vertical e do lado solicitado |
| 399 | 175.00 | 343.00 | 43.93 | 46.73 | SIM | dentro da janela vertical e do lado solicitado |
| 400 | 176.00 | 344.00 | 43.17 | 45.73 | SIM | dentro da janela vertical e do lado solicitado |
| 401 | 177.00 | 345.00 | 42.45 | 44.73 | SIM | dentro da janela vertical e do lado solicitado |
| 402 | 177.00 | 346.00 | 41.48 | 43.73 | SIM | dentro da janela vertical e do lado solicitado |
| 403 | 178.00 | 347.00 | 40.80 | 42.73 | SIM | dentro da janela vertical e do lado solicitado |
| 404 | 179.00 | 348.00 | 40.16 | 41.73 | SIM | dentro da janela vertical e do lado solicitado |
| 405 | 180.00 | 349.00 | 39.56 | 40.73 | SIM | dentro da janela vertical e do lado solicitado |
| 406 | 181.00 | 350.00 | 39.00 | 39.73 | SIM | dentro da janela vertical e do lado solicitado |
| 407 | 182.00 | 351.00 | 38.48 | 38.73 | SIM | dentro da janela vertical e do lado solicitado |
| 408 | 183.00 | 352.00 | 38.01 | 37.73 | SIM | dentro da janela vertical e do lado solicitado |
| 409 | 184.00 | 353.00 | 37.59 | 36.73 | SIM | dentro da janela vertical e do lado solicitado |
| 410 | 185.00 | 354.00 | 37.22 | 35.73 | SIM | dentro da janela vertical e do lado solicitado |
| 411 | 186.00 | 355.00 | 36.89 | 34.73 | SIM | dentro da janela vertical e do lado solicitado |
| 412 | 186.00 | 356.00 | 36.06 | 33.73 | SIM | dentro da janela vertical e do lado solicitado |
| 413 | 187.00 | 357.00 | 35.81 | 32.73 | SIM | dentro da janela vertical e do lado solicitado |
| 414 | 188.00 | 358.00 | 35.61 | 31.73 | SIM | dentro da janela vertical e do lado solicitado |
| 415 | 189.00 | 359.00 | 35.47 | 30.73 | SIM | dentro da janela vertical e do lado solicitado |
| 416 | 190.00 | 360.00 | 35.38 | 29.73 | SIM | dentro da janela vertical e do lado solicitado |
| 417 | 191.00 | 361.00 | 35.36 | 28.73 | SIM | dentro da janela vertical e do lado solicitado |
| 418 | 192.00 | 361.00 | 36.07 | 28.73 | SIM | dentro da janela vertical e do lado solicitado |
| 419 | 193.00 | 362.00 | 36.12 | 27.73 | SIM | dentro da janela vertical e do lado solicitado |
| 420 | 194.00 | 363.00 | 36.24 | 26.73 | SIM | dentro da janela vertical e do lado solicitado |
| 421 | 195.00 | 364.00 | 36.40 | 25.73 | SIM | dentro da janela vertical e do lado solicitado |
| 422 | 196.00 | 365.00 | 36.62 | 24.73 | SIM | dentro da janela vertical e do lado solicitado |
| 423 | 197.00 | 366.00 | 36.89 | 23.73 | SIM | dentro da janela vertical e do lado solicitado |
| 424 | 198.00 | 367.00 | 37.22 | 22.73 | SIM | dentro da janela vertical e do lado solicitado |
| 425 | 199.00 | 368.00 | 37.59 | 21.73 | SIM | dentro da janela vertical e do lado solicitado |
| 426 | 200.00 | 369.00 | 38.01 | 20.73 | SIM | dentro da janela vertical e do lado solicitado |
| 427 | 201.00 | 370.00 | 38.48 | 19.73 | SIM | dentro da janela vertical e do lado solicitado |
| 428 | 202.00 | 371.00 | 39.00 | 18.73 | SIM | dentro da janela vertical e do lado solicitado |
| 429 | 203.00 | 372.00 | 39.56 | 17.73 | SIM | dentro da janela vertical e do lado solicitado |
| 430 | 204.00 | 372.00 | 40.50 | 17.73 | SIM | dentro da janela vertical e do lado solicitado |
| 431 | 205.00 | 373.00 | 41.11 | 16.73 | SIM | dentro da janela vertical e do lado solicitado |
| 432 | 206.00 | 374.00 | 41.76 | 15.73 | SIM | dentro da janela vertical e do lado solicitado |
| 433 | 207.00 | 375.00 | 42.45 | 14.73 | SIM | dentro da janela vertical e do lado solicitado |
| 434 | 208.00 | 375.00 | 43.42 | 14.73 | SIM | dentro da janela vertical e do lado solicitado |
| 435 | 209.00 | 376.00 | 44.15 | 13.73 | SIM | dentro da janela vertical e do lado solicitado |
| 436 | 210.00 | 377.00 | 44.91 | 12.73 | SIM | dentro da janela vertical e do lado solicitado |
| 437 | 211.00 | 378.00 | 45.71 | 11.73 | SIM | dentro da janela vertical e do lado solicitado |
| 438 | 212.00 | 378.00 | 46.69 | 11.73 | SIM | dentro da janela vertical e do lado solicitado |
| 439 | 213.00 | 379.00 | 47.52 | 10.73 | SIM | dentro da janela vertical e do lado solicitado |
| 440 | 214.00 | 380.00 | 48.37 | 9.73 | SIM | dentro da janela vertical e do lado solicitado |
| 441 | 215.00 | 381.00 | 49.25 | 8.73 | SIM | dentro da janela vertical e do lado solicitado |
| 442 | 216.00 | 381.00 | 50.25 | 8.73 | SIM | dentro da janela vertical e do lado solicitado |
| 443 | 217.00 | 382.00 | 51.16 | 7.73 | SIM | dentro da janela vertical e do lado solicitado |
| 444 | 218.00 | 383.00 | 52.09 | 6.73 | SIM | dentro da janela vertical e do lado solicitado |
| 445 | 219.00 | 384.00 | 53.04 | 5.73 | SIM | dentro da janela vertical e do lado solicitado |
| 446 | 220.00 | 384.00 | 54.04 | 5.73 | SIM | dentro da janela vertical e do lado solicitado |
| 447 | 221.00 | 385.00 | 55.01 | 4.73 | SIM | dentro da janela vertical e do lado solicitado |
| 448 | 222.00 | 386.00 | 56.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 449 | 223.00 | 386.00 | 57.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 450 | 224.00 | 386.00 | 58.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 451 | 225.00 | 386.00 | 59.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 452 | 226.00 | 386.00 | 60.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 453 | 227.00 | 386.00 | 61.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 454 | 228.00 | 386.00 | 62.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 455 | 229.00 | 386.00 | 63.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 456 | 230.00 | 386.00 | 64.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 457 | 231.00 | 386.00 | 65.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 458 | 232.00 | 386.00 | 66.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 459 | 233.00 | 386.00 | 67.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 460 | 234.00 | 386.00 | 68.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 461 | 235.00 | 386.00 | 69.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 462 | 236.00 | 386.00 | 70.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 463 | 237.00 | 386.00 | 71.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 464 | 238.00 | 386.00 | 72.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 465 | 239.00 | 386.00 | 73.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 466 | 240.00 | 386.00 | 74.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 467 | 241.00 | 386.00 | 75.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 468 | 242.00 | 386.00 | 76.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 469 | 243.00 | 386.00 | 77.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 470 | 244.00 | 386.00 | 78.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 471 | 245.00 | 386.00 | 79.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 472 | 246.00 | 386.00 | 80.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 473 | 247.00 | 386.00 | 81.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 474 | 248.00 | 386.00 | 82.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 475 | 249.00 | 386.00 | 83.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 476 | 250.00 | 386.00 | 84.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 477 | 251.00 | 386.00 | 85.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 478 | 252.00 | 386.00 | 86.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 479 | 253.00 | 386.00 | 87.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 480 | 254.00 | 386.00 | 88.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 481 | 255.00 | 386.00 | 89.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 482 | 256.00 | 386.00 | 90.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 483 | 257.00 | 386.00 | 91.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 484 | 258.00 | 386.00 | 92.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 485 | 259.00 | 386.00 | 93.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 486 | 260.00 | 386.00 | 94.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 487 | 261.00 | 386.00 | 95.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 488 | 262.00 | 386.00 | 96.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 489 | 263.00 | 386.00 | 97.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 490 | 264.00 | 386.00 | 98.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 491 | 265.00 | 386.00 | 99.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 492 | 266.00 | 386.00 | 100.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 493 | 267.00 | 386.00 | 101.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 494 | 268.00 | 386.00 | 102.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 495 | 269.00 | 386.00 | 103.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 496 | 270.00 | 386.00 | 104.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 497 | 271.00 | 386.00 | 105.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 498 | 272.00 | 386.00 | 106.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 499 | 273.00 | 386.00 | 107.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 500 | 274.00 | 386.00 | 108.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 501 | 275.00 | 386.00 | 109.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 502 | 276.00 | 386.00 | 110.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 503 | 277.00 | 386.00 | 111.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 504 | 278.00 | 386.00 | 112.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 505 | 279.00 | 386.00 | 113.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 506 | 280.00 | 386.00 | 114.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 507 | 281.00 | 386.00 | 115.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 508 | 282.00 | 386.00 | 116.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 509 | 283.00 | 386.00 | 117.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 510 | 284.00 | 386.00 | 118.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 511 | 285.00 | 386.00 | 119.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 512 | 286.00 | 386.00 | 120.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 513 | 287.00 | 386.00 | 121.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 514 | 288.00 | 386.00 | 122.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 515 | 289.00 | 386.00 | 123.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 516 | 290.00 | 386.00 | 124.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 517 | 291.00 | 386.00 | 125.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 518 | 292.00 | 386.00 | 126.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 519 | 293.00 | 386.00 | 127.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 520 | 294.00 | 386.00 | 128.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 521 | 295.00 | 386.00 | 129.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 522 | 296.00 | 386.00 | 130.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 523 | 297.00 | 386.00 | 131.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 524 | 298.00 | 386.00 | 132.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 525 | 299.00 | 386.00 | 133.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 526 | 300.00 | 386.00 | 134.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 527 | 301.00 | 386.00 | 135.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 528 | 302.00 | 386.00 | 136.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 529 | 303.00 | 386.00 | 137.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 530 | 304.00 | 386.00 | 138.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 531 | 305.00 | 386.00 | 139.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 532 | 306.00 | 386.00 | 140.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 533 | 307.00 | 386.00 | 141.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 534 | 308.00 | 386.00 | 142.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 535 | 309.00 | 386.00 | 143.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 536 | 310.00 | 386.00 | 144.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 537 | 311.00 | 386.00 | 145.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 538 | 312.00 | 386.00 | 146.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 539 | 313.00 | 386.00 | 147.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 540 | 314.00 | 386.00 | 148.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 541 | 315.00 | 386.00 | 149.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 542 | 316.00 | 386.00 | 150.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 543 | 317.00 | 386.00 | 151.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 544 | 318.00 | 386.00 | 152.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 545 | 319.00 | 386.00 | 153.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 546 | 320.00 | 386.00 | 154.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 547 | 321.00 | 386.00 | 155.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 548 | 322.00 | 386.00 | 156.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 549 | 323.00 | 386.00 | 157.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 550 | 324.00 | 386.00 | 158.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 551 | 325.00 | 386.00 | 159.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 552 | 326.00 | 386.00 | 160.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 553 | 327.00 | 386.00 | 161.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 554 | 328.00 | 386.00 | 162.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 555 | 329.00 | 386.00 | 163.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 556 | 330.00 | 386.00 | 164.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 557 | 331.00 | 386.00 | 165.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 558 | 332.00 | 386.00 | 166.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 559 | 333.00 | 386.00 | 167.00 | 3.73 | NÃO | fora do lado solicitado |
| 560 | 334.00 | 386.00 | 168.00 | 3.73 | NÃO | fora do lado solicitado |
| 561 | 335.00 | 386.00 | 169.00 | 3.73 | NÃO | fora do lado solicitado |
| 562 | 336.00 | 386.00 | 170.00 | 3.73 | NÃO | fora do lado solicitado |
| 563 | 337.00 | 386.00 | 171.00 | 3.73 | NÃO | fora do lado solicitado |
| 564 | 338.00 | 386.00 | 172.00 | 3.73 | NÃO | fora do lado solicitado |
| 565 | 339.00 | 386.00 | 173.00 | 3.73 | NÃO | fora do lado solicitado |
| 566 | 340.00 | 386.00 | 174.00 | 3.73 | NÃO | fora do lado solicitado |
| 567 | 341.00 | 386.00 | 175.00 | 3.73 | NÃO | fora do lado solicitado |
| 568 | 342.00 | 386.00 | 176.00 | 3.73 | NÃO | fora do lado solicitado |
| 569 | 343.00 | 386.00 | 177.00 | 3.73 | NÃO | fora do lado solicitado |
| 570 | 344.00 | 386.00 | 178.00 | 3.73 | NÃO | fora do lado solicitado |
| 571 | 345.00 | 386.00 | 179.00 | 3.73 | NÃO | fora do lado solicitado |
| 572 | 346.00 | 386.00 | 180.00 | 3.73 | NÃO | fora do lado solicitado |
| 573 | 347.00 | 386.00 | 181.00 | 3.73 | NÃO | fora do lado solicitado |
| 574 | 348.00 | 386.00 | 182.00 | 3.73 | NÃO | fora do lado solicitado |
| 575 | 349.00 | 386.00 | 183.00 | 3.73 | NÃO | fora do lado solicitado |
| 576 | 350.00 | 386.00 | 184.00 | 3.73 | NÃO | fora do lado solicitado |
| 577 | 351.00 | 386.00 | 185.00 | 3.73 | NÃO | fora do lado solicitado |
| 578 | 352.00 | 386.00 | 186.00 | 3.73 | NÃO | fora do lado solicitado |
| 579 | 353.00 | 386.00 | 187.00 | 3.73 | NÃO | fora do lado solicitado |
| 580 | 354.00 | 386.00 | 188.00 | 3.73 | NÃO | fora do lado solicitado |
| 581 | 355.00 | 386.00 | 189.00 | 3.73 | NÃO | fora do lado solicitado |
| 582 | 356.00 | 386.00 | 190.00 | 3.73 | NÃO | fora do lado solicitado |
| 583 | 357.00 | 386.00 | 191.00 | 3.73 | NÃO | fora do lado solicitado |
| 584 | 358.00 | 386.00 | 192.00 | 3.73 | NÃO | fora do lado solicitado |
| 585 | 359.00 | 386.00 | 193.00 | 3.73 | NÃO | fora do lado solicitado |
| 586 | 360.00 | 386.00 | 194.00 | 3.73 | NÃO | fora do lado solicitado |
| 587 | 361.00 | 386.00 | 195.00 | 3.73 | NÃO | fora do lado solicitado |
| 588 | 362.00 | 386.00 | 196.00 | 3.73 | NÃO | fora do lado solicitado |
| 589 | 363.00 | 386.00 | 197.00 | 3.73 | NÃO | fora do lado solicitado |
| 590 | 364.00 | 386.00 | 198.00 | 3.73 | NÃO | fora do lado solicitado |
| 591 | 365.00 | 386.00 | 199.00 | 3.73 | NÃO | fora do lado solicitado |
| 592 | 366.00 | 386.00 | 200.00 | 3.73 | NÃO | fora do lado solicitado |
| 593 | 367.00 | 386.00 | 201.00 | 3.73 | NÃO | fora do lado solicitado |
| 594 | 368.00 | 386.00 | 202.00 | 3.73 | NÃO | fora do lado solicitado |
| 595 | 369.00 | 386.00 | 203.00 | 3.73 | NÃO | fora do lado solicitado |
| 596 | 370.00 | 386.00 | 204.00 | 3.73 | NÃO | fora do lado solicitado |
| 597 | 371.00 | 386.00 | 205.00 | 3.73 | NÃO | fora do lado solicitado |
| 598 | 372.00 | 386.00 | 206.00 | 3.73 | NÃO | fora do lado solicitado |
| 599 | 373.00 | 386.00 | 207.00 | 3.73 | NÃO | fora do lado solicitado |
| 600 | 374.00 | 386.00 | 208.00 | 3.73 | NÃO | fora do lado solicitado |
| 601 | 375.00 | 386.00 | 209.00 | 3.73 | NÃO | fora do lado solicitado |
| 602 | 376.00 | 386.00 | 210.00 | 3.73 | NÃO | fora do lado solicitado |
| 603 | 377.00 | 386.00 | 211.00 | 3.73 | NÃO | fora do lado solicitado |
| 604 | 378.00 | 386.00 | 212.00 | 3.73 | NÃO | fora do lado solicitado |
| 605 | 379.00 | 386.00 | 213.00 | 3.73 | NÃO | fora do lado solicitado |
| 606 | 380.00 | 386.00 | 214.00 | 3.73 | NÃO | fora do lado solicitado |
| 607 | 381.00 | 386.00 | 215.00 | 3.73 | NÃO | fora do lado solicitado |
| 608 | 382.00 | 386.00 | 216.00 | 3.73 | NÃO | fora do lado solicitado |
| 609 | 383.00 | 386.00 | 217.00 | 3.73 | NÃO | fora do lado solicitado |
| 610 | 384.00 | 386.00 | 218.00 | 3.73 | NÃO | fora do lado solicitado |
| 611 | 385.00 | 386.00 | 219.00 | 3.73 | NÃO | fora do lado solicitado |
| 612 | 386.00 | 386.00 | 220.00 | 3.73 | NÃO | fora do lado solicitado |
| 613 | 387.00 | 386.00 | 221.00 | 3.73 | NÃO | fora do lado solicitado |
| 614 | 388.00 | 386.00 | 222.00 | 3.73 | NÃO | fora do lado solicitado |
| 615 | 389.00 | 386.00 | 223.00 | 3.73 | NÃO | fora do lado solicitado |
| 616 | 390.00 | 386.00 | 224.00 | 3.73 | NÃO | fora do lado solicitado |
| 617 | 391.00 | 386.00 | 225.00 | 3.73 | NÃO | fora do lado solicitado |
| 618 | 392.00 | 386.00 | 226.00 | 3.73 | NÃO | fora do lado solicitado |
| 619 | 393.00 | 386.00 | 227.00 | 3.73 | NÃO | fora do lado solicitado |
| 620 | 394.00 | 386.00 | 228.00 | 3.73 | NÃO | fora do lado solicitado |
| 621 | 395.00 | 386.00 | 229.00 | 3.73 | NÃO | fora do lado solicitado |
| 622 | 396.00 | 386.00 | 230.00 | 3.73 | NÃO | fora do lado solicitado |
| 623 | 397.00 | 386.00 | 231.00 | 3.73 | NÃO | fora do lado solicitado |
| 624 | 398.00 | 386.00 | 232.00 | 3.73 | NÃO | fora do lado solicitado |
| 625 | 399.00 | 386.00 | 233.00 | 3.73 | NÃO | fora do lado solicitado |
| 626 | 400.00 | 386.00 | 234.00 | 3.73 | NÃO | fora do lado solicitado |
| 627 | 401.00 | 386.00 | 235.00 | 3.73 | NÃO | fora do lado solicitado |
| 628 | 402.00 | 386.00 | 236.00 | 3.73 | NÃO | fora do lado solicitado |
| 629 | 403.00 | 386.00 | 237.00 | 3.73 | NÃO | fora do lado solicitado |
| 630 | 404.00 | 386.00 | 238.00 | 3.73 | NÃO | fora do lado solicitado |
| 631 | 405.00 | 386.00 | 239.00 | 3.73 | NÃO | fora do lado solicitado |
| 632 | 406.00 | 386.00 | 240.00 | 3.73 | NÃO | fora do lado solicitado |
| 633 | 407.00 | 386.00 | 241.00 | 3.73 | NÃO | fora do lado solicitado |
| 634 | 408.00 | 386.00 | 242.00 | 3.73 | NÃO | fora do lado solicitado |
| 635 | 409.00 | 386.00 | 243.00 | 3.73 | NÃO | fora do lado solicitado |
| 636 | 410.00 | 386.00 | 244.00 | 3.73 | NÃO | fora do lado solicitado |
| 637 | 411.00 | 386.00 | 245.00 | 3.73 | NÃO | fora do lado solicitado |
| 638 | 412.00 | 386.00 | 246.00 | 3.73 | NÃO | fora do lado solicitado |
| 639 | 413.00 | 386.00 | 247.00 | 3.73 | NÃO | fora do lado solicitado |
| 640 | 414.00 | 386.00 | 248.00 | 3.73 | NÃO | fora do lado solicitado |
| 641 | 415.00 | 386.00 | 249.00 | 3.73 | NÃO | fora do lado solicitado |
| 642 | 416.00 | 386.00 | 250.00 | 3.73 | NÃO | fora do lado solicitado |
| 643 | 417.00 | 386.00 | 251.00 | 3.73 | NÃO | fora do lado solicitado |
| 644 | 418.00 | 386.00 | 252.00 | 3.73 | NÃO | fora do lado solicitado |
| 645 | 419.00 | 386.00 | 253.00 | 3.73 | NÃO | fora do lado solicitado |
| 646 | 420.00 | 386.00 | 254.00 | 3.73 | NÃO | fora do lado solicitado |
| 647 | 421.00 | 386.00 | 255.00 | 3.73 | NÃO | fora do lado solicitado |
| 648 | 422.00 | 386.00 | 256.00 | 3.73 | NÃO | fora do lado solicitado |
| 649 | 423.00 | 386.00 | 257.00 | 3.73 | NÃO | fora do lado solicitado |
| 650 | 424.00 | 386.00 | 258.00 | 3.73 | NÃO | fora do lado solicitado |
| 651 | 425.00 | 386.00 | 259.00 | 3.73 | NÃO | fora do lado solicitado |
| 652 | 426.00 | 386.00 | 260.00 | 3.73 | NÃO | fora do lado solicitado |
| 653 | 427.00 | 386.00 | 261.00 | 3.73 | NÃO | fora do lado solicitado |
| 654 | 428.00 | 386.00 | 262.00 | 3.73 | NÃO | fora do lado solicitado |
| 655 | 429.00 | 386.00 | 263.00 | 3.73 | NÃO | fora do lado solicitado |
| 656 | 430.00 | 386.00 | 264.00 | 3.73 | NÃO | fora do lado solicitado |
| 657 | 431.00 | 386.00 | 265.00 | 3.73 | NÃO | fora do lado solicitado |
| 658 | 432.00 | 386.00 | 266.00 | 3.73 | NÃO | fora do lado solicitado |
| 659 | 433.00 | 386.00 | 267.00 | 3.73 | NÃO | fora do lado solicitado |
| 660 | 434.00 | 386.00 | 268.00 | 3.73 | NÃO | fora do lado solicitado |
| 661 | 435.00 | 386.00 | 269.00 | 3.73 | NÃO | fora do lado solicitado |
| 662 | 436.00 | 386.00 | 270.00 | 3.73 | NÃO | fora do lado solicitado |
| 663 | 437.00 | 386.00 | 271.00 | 3.73 | NÃO | fora do lado solicitado |
| 664 | 438.00 | 386.00 | 272.00 | 3.73 | NÃO | fora do lado solicitado |
| 665 | 439.00 | 386.00 | 273.00 | 3.73 | NÃO | fora do lado solicitado |
| 666 | 440.00 | 386.00 | 274.00 | 3.73 | NÃO | fora do lado solicitado |
| 667 | 441.00 | 386.00 | 275.00 | 3.73 | NÃO | fora do lado solicitado |
| 668 | 442.00 | 386.00 | 276.00 | 3.73 | NÃO | fora do lado solicitado |
| 669 | 443.00 | 386.00 | 277.00 | 3.73 | NÃO | fora do lado solicitado |
| 670 | 444.00 | 385.00 | 278.00 | 4.73 | NÃO | fora do lado solicitado |
| 671 | 445.00 | 384.00 | 279.01 | 5.73 | NÃO | fora do lado solicitado |
| 672 | 446.00 | 384.00 | 280.01 | 5.73 | NÃO | fora do lado solicitado |
| 673 | 447.00 | 383.00 | 281.02 | 6.73 | NÃO | fora do lado solicitado |
| 674 | 448.00 | 382.00 | 282.03 | 7.73 | NÃO | fora do lado solicitado |
| 675 | 449.00 | 382.00 | 283.03 | 7.73 | NÃO | fora do lado solicitado |
| 676 | 450.00 | 381.00 | 284.04 | 8.73 | NÃO | fora do lado solicitado |
| 677 | 451.00 | 380.00 | 285.06 | 9.73 | NÃO | fora do lado solicitado |
| 678 | 452.00 | 379.00 | 286.09 | 10.73 | NÃO | fora do lado solicitado |
| 679 | 453.00 | 379.00 | 287.09 | 10.73 | NÃO | fora do lado solicitado |
| 680 | 454.00 | 378.00 | 288.11 | 11.73 | NÃO | fora do lado solicitado |
| 681 | 455.00 | 377.00 | 289.14 | 12.73 | NÃO | fora do lado solicitado |
| 682 | 456.00 | 376.00 | 290.17 | 13.73 | NÃO | fora do lado solicitado |
| 683 | 457.00 | 376.00 | 291.17 | 13.73 | NÃO | fora do lado solicitado |
| 684 | 458.00 | 375.00 | 292.21 | 14.73 | NÃO | fora do lado solicitado |
| 685 | 459.00 | 374.00 | 293.25 | 15.73 | NÃO | fora do lado solicitado |
| 686 | 460.00 | 373.00 | 294.29 | 16.73 | NÃO | fora do lado solicitado |
| 687 | 461.00 | 373.00 | 295.29 | 16.73 | NÃO | fora do lado solicitado |
| 688 | 462.00 | 372.00 | 296.33 | 17.73 | NÃO | fora do lado solicitado |
| 689 | 463.00 | 371.00 | 297.38 | 18.73 | NÃO | fora do lado solicitado |
| 690 | 464.00 | 370.00 | 298.43 | 19.73 | NÃO | fora do lado solicitado |
| 691 | 465.00 | 369.00 | 299.48 | 20.73 | NÃO | fora do lado solicitado |
| 692 | 466.00 | 368.00 | 300.54 | 21.73 | NÃO | fora do lado solicitado |
| 693 | 467.00 | 367.00 | 301.60 | 22.73 | NÃO | fora do lado solicitado |
| 694 | 468.00 | 366.00 | 302.66 | 23.73 | NÃO | fora do lado solicitado |
| 695 | 469.00 | 365.00 | 303.73 | 24.73 | NÃO | fora do lado solicitado |
| 696 | 470.00 | 364.00 | 304.80 | 25.73 | NÃO | fora do lado solicitado |
| 697 | 471.00 | 363.00 | 305.87 | 26.73 | NÃO | fora do lado solicitado |
| 698 | 472.00 | 363.00 | 306.86 | 26.73 | NÃO | fora do lado solicitado |
| 699 | 473.00 | 362.00 | 307.94 | 27.73 | NÃO | fora do lado solicitado |
| 700 | 474.00 | 361.00 | 309.01 | 28.73 | NÃO | fora do lado solicitado |
| 701 | 475.00 | 360.00 | 310.09 | 29.73 | NÃO | fora do lado solicitado |
| 702 | 476.00 | 359.00 | 311.17 | 30.73 | NÃO | fora do lado solicitado |
| 703 | 477.00 | 358.00 | 312.26 | 31.73 | NÃO | fora do lado solicitado |
| 704 | 478.00 | 357.00 | 313.34 | 32.73 | NÃO | fora do lado solicitado |
| 705 | 479.00 | 356.00 | 314.43 | 33.73 | NÃO | fora do lado solicitado |
| 706 | 480.00 | 355.00 | 315.53 | 34.73 | NÃO | fora do lado solicitado |
| 707 | 481.00 | 354.00 | 316.62 | 35.73 | NÃO | fora do lado solicitado |
| 708 | 482.00 | 353.00 | 317.72 | 36.73 | NÃO | fora do lado solicitado |
| 709 | 483.00 | 352.00 | 318.82 | 37.73 | NÃO | fora do lado solicitado |
| 710 | 483.00 | 351.00 | 318.93 | 38.73 | NÃO | fora do lado solicitado |
| 711 | 484.00 | 350.00 | 320.03 | 39.73 | NÃO | fora do lado solicitado |
| 712 | 485.00 | 349.00 | 321.14 | 40.73 | NÃO | fora do lado solicitado |
| 713 | 486.00 | 348.00 | 322.25 | 41.73 | NÃO | fora do lado solicitado |
| 714 | 487.00 | 347.00 | 323.36 | 42.73 | NÃO | fora do lado solicitado |
| 715 | 488.00 | 346.00 | 324.47 | 43.73 | NÃO | fora do lado solicitado |
| 716 | 489.00 | 345.00 | 325.59 | 44.73 | NÃO | fora do lado solicitado |
| 717 | 490.00 | 344.00 | 326.71 | 45.73 | NÃO | fora do lado solicitado |
| 718 | 490.00 | 343.00 | 326.84 | 46.73 | NÃO | fora do lado solicitado |
| 719 | 491.00 | 342.00 | 327.96 | 47.73 | NÃO | fora do lado solicitado |
| 720 | 492.00 | 341.00 | 329.09 | 48.73 | NÃO | fora do lado solicitado |
| 721 | 493.00 | 340.00 | 330.22 | 49.73 | NÃO | fora do lado solicitado |
| 722 | 493.00 | 339.00 | 330.36 | 50.73 | NÃO | fora do lado solicitado |
| 723 | 494.00 | 338.00 | 331.49 | 51.73 | NÃO | fora do lado solicitado |
| 724 | 495.00 | 337.00 | 332.63 | 52.73 | NÃO | fora do lado solicitado |
| 725 | 496.00 | 336.00 | 333.77 | 53.73 | NÃO | fora do lado solicitado |
| 726 | 496.00 | 335.00 | 333.92 | 54.73 | NÃO | fora do lado solicitado |
| 727 | 497.00 | 334.00 | 335.06 | 55.73 | NÃO | fora do lado solicitado |
| 728 | 498.00 | 333.00 | 336.20 | 56.73 | NÃO | fora do lado solicitado |
| 729 | 499.00 | 332.00 | 337.35 | 57.73 | NÃO | fora do lado solicitado |
| 730 | 499.00 | 331.00 | 337.51 | 58.73 | NÃO | fora do lado solicitado |
| 731 | 500.00 | 330.00 | 338.66 | 59.73 | NÃO | fora do lado solicitado |
| 732 | 501.00 | 329.00 | 339.81 | 60.73 | NÃO | fora do lado solicitado |
| 733 | 501.00 | 328.00 | 339.98 | 61.73 | NÃO | fora do lado solicitado |
| 734 | 502.00 | 327.00 | 341.14 | 62.73 | NÃO | fora do lado solicitado |
| 735 | 503.00 | 326.00 | 342.30 | 63.73 | NÃO | fora do lado solicitado |
| 736 | 503.00 | 325.00 | 342.48 | 64.73 | NÃO | fora do lado solicitado |
| 737 | 504.00 | 324.00 | 343.64 | 65.73 | NÃO | fora do lado solicitado |
| 738 | 504.00 | 323.00 | 343.82 | 66.73 | NÃO | fora do lado solicitado |
| 739 | 505.00 | 322.00 | 344.99 | 67.73 | NÃO | fora do lado solicitado |
| 740 | 506.00 | 321.00 | 346.16 | 68.73 | NÃO | fora do lado solicitado |
| 741 | 506.00 | 320.00 | 346.35 | 69.73 | NÃO | fora do lado solicitado |
| 742 | 507.00 | 319.00 | 347.52 | 70.73 | NÃO | fora do lado solicitado |
| 743 | 507.00 | 318.00 | 347.71 | 71.73 | NÃO | fora do lado solicitado |
| 744 | 508.00 | 317.00 | 348.89 | 72.73 | NÃO | fora do lado solicitado |
| 745 | 509.00 | 316.00 | 350.07 | 73.73 | NÃO | fora do lado solicitado |
| 746 | 509.00 | 315.00 | 350.27 | 74.73 | NÃO | fora do lado solicitado |
| 747 | 510.00 | 314.00 | 351.45 | 75.73 | NÃO | fora do lado solicitado |
| 748 | 510.00 | 313.00 | 351.66 | 76.73 | NÃO | fora do lado solicitado |
| 749 | 511.00 | 312.00 | 352.85 | 77.73 | NÃO | fora do lado solicitado |
| 750 | 511.00 | 311.00 | 353.06 | 78.73 | NÃO | fora do lado solicitado |
| 751 | 512.00 | 310.00 | 354.25 | 79.73 | NÃO | fora do lado solicitado |
| 752 | 512.00 | 309.00 | 354.46 | 80.73 | NÃO | fora do lado solicitado |
| 753 | 513.00 | 308.00 | 355.66 | 81.73 | NÃO | fora do lado solicitado |
| 754 | 513.00 | 307.00 | 355.88 | 82.73 | NÃO | fora do lado solicitado |
| 755 | 514.00 | 306.00 | 357.08 | 83.73 | NÃO | fora do lado solicitado |
| 756 | 514.00 | 305.00 | 357.30 | 84.73 | NÃO | fora do lado solicitado |
| 757 | 515.00 | 304.00 | 358.50 | 85.73 | NÃO | fora do lado solicitado |
| 758 | 515.00 | 303.00 | 358.73 | 86.73 | NÃO | fora do lado solicitado |
| 759 | 516.00 | 302.00 | 359.94 | 87.73 | NÃO | fora do lado solicitado |
| 760 | 516.00 | 301.00 | 360.17 | 88.73 | NÃO | fora do lado solicitado |
| 761 | 517.00 | 300.00 | 361.38 | 89.73 | NÃO | fora do lado solicitado |
| 762 | 517.00 | 299.00 | 361.62 | 90.73 | NÃO | fora do lado solicitado |
| 763 | 518.00 | 298.00 | 362.83 | 91.73 | NÃO | fora do lado solicitado |
| 764 | 518.00 | 297.00 | 363.08 | 92.73 | NÃO | fora do lado solicitado |
| 765 | 519.00 | 296.00 | 364.29 | 93.73 | NÃO | fora do lado solicitado |
| 766 | 519.00 | 295.00 | 364.54 | 94.73 | NÃO | fora do lado solicitado |
| 767 | 520.00 | 294.00 | 365.76 | 95.73 | NÃO | fora do lado solicitado |
| 768 | 520.00 | 293.00 | 366.01 | 96.73 | NÃO | fora do lado solicitado |
| 769 | 521.00 | 292.00 | 367.23 | 97.73 | NÃO | fora do lado solicitado |
| 770 | 521.00 | 291.00 | 367.49 | 98.73 | NÃO | fora do lado solicitado |
| 771 | 521.00 | 290.00 | 367.75 | 99.73 | NÃO | fora do lado solicitado |
| 772 | 522.00 | 289.00 | 368.98 | 100.73 | NÃO | fora do lado solicitado |
| 773 | 522.00 | 288.00 | 369.24 | 101.73 | NÃO | fora do lado solicitado |
| 774 | 522.00 | 287.00 | 369.51 | 102.73 | NÃO | fora do lado solicitado |
| 775 | 523.00 | 286.00 | 370.74 | 103.73 | NÃO | fora do lado solicitado |
| 776 | 523.00 | 285.00 | 371.01 | 104.73 | NÃO | fora do lado solicitado |
| 777 | 524.00 | 284.00 | 372.25 | 105.73 | NÃO | fora do lado solicitado |
| 778 | 524.00 | 283.00 | 372.52 | 106.73 | NÃO | fora do lado solicitado |
| 779 | 524.00 | 282.00 | 372.80 | 107.73 | NÃO | fora do lado solicitado |
| 780 | 525.00 | 281.00 | 374.04 | 108.73 | NÃO | fora do lado solicitado |
| 781 | 525.00 | 280.00 | 374.32 | 109.73 | NÃO | fora do lado solicitado |
| 782 | 525.00 | 279.00 | 374.61 | 110.73 | NÃO | fora do lado solicitado |
| 783 | 526.00 | 278.00 | 375.85 | 111.73 | NÃO | fora do lado solicitado |
| 784 | 526.00 | 277.00 | 376.14 | 112.73 | NÃO | fora do lado solicitado |
| 785 | 526.00 | 276.00 | 376.43 | 113.73 | NÃO | fora do lado solicitado |
| 786 | 526.00 | 275.00 | 376.72 | 114.73 | NÃO | fora do lado solicitado |
| 787 | 527.00 | 274.00 | 377.97 | 115.73 | NÃO | fora do lado solicitado |
| 788 | 527.00 | 273.00 | 378.27 | 116.73 | NÃO | fora do lado solicitado |
| 789 | 527.00 | 272.00 | 378.57 | 117.73 | NÃO | fora do lado solicitado |
| 790 | 528.00 | 271.00 | 379.83 | 118.73 | NÃO | fora do lado solicitado |
| 791 | 528.00 | 270.00 | 380.13 | 119.73 | NÃO | fora do lado solicitado |
| 792 | 528.00 | 269.00 | 380.44 | 120.73 | NÃO | fora do lado solicitado |
| 793 | 528.00 | 268.00 | 380.75 | 121.73 | NÃO | fora do lado solicitado |
| 794 | 529.00 | 267.00 | 382.01 | 122.73 | NÃO | fora do lado solicitado |
| 795 | 529.00 | 266.00 | 382.32 | 123.73 | NÃO | fora do lado solicitado |
| 796 | 529.00 | 265.00 | 382.64 | 124.73 | NÃO | fora do lado solicitado |
| 797 | 529.00 | 264.00 | 382.95 | 125.73 | NÃO | fora do lado solicitado |
| 798 | 530.00 | 263.00 | 384.22 | 126.73 | NÃO | fora do lado solicitado |
| 799 | 530.00 | 262.00 | 384.54 | 127.73 | NÃO | fora do lado solicitado |
| 800 | 530.00 | 261.00 | 384.86 | 128.73 | NÃO | fora do lado solicitado |
| 801 | 530.00 | 260.00 | 385.19 | 129.73 | NÃO | fora do lado solicitado |
| 802 | 530.00 | 259.00 | 385.52 | 130.73 | NÃO | fora do lado solicitado |
| 803 | 531.00 | 258.00 | 386.79 | 131.73 | NÃO | fora do lado solicitado |
| 804 | 531.00 | 257.00 | 387.13 | 132.73 | NÃO | fora do lado solicitado |
| 805 | 531.00 | 256.00 | 387.46 | 133.73 | NÃO | fora do lado solicitado |
| 806 | 531.00 | 255.00 | 387.80 | 134.73 | NÃO | fora do lado solicitado |
| 807 | 532.00 | 254.00 | 389.08 | 135.73 | NÃO | fora do lado solicitado |
| 808 | 532.00 | 253.00 | 389.42 | 136.73 | NÃO | fora do lado solicitado |
| 809 | 532.00 | 252.00 | 389.76 | 137.73 | NÃO | fora do lado solicitado |
| 810 | 532.00 | 251.00 | 390.10 | 138.73 | NÃO | fora do lado solicitado |
| 811 | 532.00 | 250.00 | 390.45 | 139.73 | NÃO | fora do lado solicitado |
| 812 | 533.00 | 249.00 | 391.74 | 140.73 | NÃO | fora do lado solicitado |
| 813 | 533.00 | 248.00 | 392.09 | 141.73 | NÃO | fora do lado solicitado |
| 814 | 533.00 | 247.00 | 392.44 | 142.73 | NÃO | fora do lado solicitado |
| 815 | 533.00 | 246.00 | 392.80 | 143.73 | NÃO | fora do lado solicitado |
| 816 | 533.00 | 245.00 | 393.15 | 144.73 | NÃO | fora do lado solicitado |
| 817 | 533.00 | 244.00 | 393.51 | 145.73 | NÃO | fora do lado solicitado |
| 818 | 533.00 | 243.00 | 393.88 | 146.73 | NÃO | fora do lado solicitado |
| 819 | 534.00 | 242.00 | 395.17 | 147.73 | NÃO | fora do lado solicitado |
| 820 | 534.00 | 241.00 | 395.54 | 148.73 | NÃO | fora do lado solicitado |
| 821 | 534.00 | 240.00 | 395.90 | 149.73 | NÃO | fora do lado solicitado |
| 822 | 534.00 | 239.00 | 396.27 | 150.73 | NÃO | fora do lado solicitado |
| 823 | 534.00 | 238.00 | 396.65 | 151.73 | NÃO | fora do lado solicitado |
| 824 | 534.00 | 237.00 | 397.02 | 152.73 | NÃO | fora do lado solicitado |
| 825 | 534.00 | 236.00 | 397.40 | 153.73 | NÃO | fora do lado solicitado |
| 826 | 534.00 | 235.00 | 397.78 | 154.73 | NÃO | fora do lado solicitado |
| 827 | 535.00 | 234.00 | 399.08 | 155.73 | NÃO | fora do lado solicitado |
| 828 | 535.00 | 233.00 | 399.46 | 156.73 | NÃO | fora do lado solicitado |
| 829 | 535.00 | 232.00 | 399.85 | 157.73 | NÃO | fora do lado solicitado |
| 830 | 535.00 | 231.00 | 400.23 | 158.73 | NÃO | fora do lado solicitado |
| 831 | 535.00 | 230.00 | 400.62 | 159.73 | NÃO | fora do lado solicitado |
| 832 | 535.00 | 229.00 | 401.01 | 160.73 | NÃO | fora do lado solicitado |
| 833 | 535.00 | 228.00 | 401.40 | 161.73 | NÃO | fora do lado solicitado |
| 834 | 535.00 | 227.00 | 401.80 | 162.73 | NÃO | fora do lado solicitado |
| 835 | 535.00 | 226.00 | 402.20 | 163.73 | NÃO | fora do lado solicitado |
| 836 | 535.00 | 225.00 | 402.59 | 164.73 | NÃO | fora do lado solicitado |
| 837 | 535.00 | 224.00 | 403.00 | 165.73 | NÃO | fora do lado solicitado |
| 838 | 535.00 | 223.00 | 403.40 | 166.73 | NÃO | fora do lado solicitado |
| 839 | 535.00 | 222.00 | 403.80 | 167.73 | NÃO | fora do lado solicitado |
| 840 | 535.00 | 221.00 | 404.21 | 168.73 | NÃO | fora do lado solicitado |
| 841 | 535.00 | 220.00 | 404.62 | 169.73 | NÃO | fora do lado solicitado |
| 842 | 535.00 | 219.00 | 405.03 | 170.73 | NÃO | fora do lado solicitado |
| 843 | 535.00 | 218.00 | 405.44 | 171.73 | NÃO | fora do lado solicitado |
| 844 | 535.00 | 217.00 | 405.86 | 172.73 | NÃO | fora do lado solicitado |
| 845 | 535.00 | 216.00 | 406.28 | 173.73 | NÃO | fora do lado solicitado |
| 846 | 535.00 | 215.00 | 406.70 | 174.73 | NÃO | fora do lado solicitado |
| 847 | 535.00 | 214.00 | 407.12 | 175.73 | NÃO | fora do lado solicitado |
| 848 | 535.00 | 213.00 | 407.54 | 176.73 | NÃO | fora do lado solicitado |
| 849 | 535.00 | 212.00 | 407.97 | 177.73 | NÃO | fora do lado solicitado |
| 850 | 535.00 | 211.00 | 408.39 | 178.73 | NÃO | fora do lado solicitado |
| 851 | 535.00 | 210.00 | 408.82 | 179.73 | NÃO | fora do lado solicitado |
| 852 | 535.00 | 209.00 | 409.26 | 180.73 | NÃO | fora do lado solicitado |
| 853 | 535.00 | 208.00 | 409.69 | 181.73 | NÃO | fora do lado solicitado |
| 854 | 535.00 | 207.00 | 410.12 | 182.73 | NÃO | fora do lado solicitado |
| 855 | 535.00 | 206.00 | 410.56 | 183.73 | NÃO | fora do lado solicitado |
| 856 | 535.00 | 205.00 | 411.00 | 184.73 | NÃO | fora do lado solicitado |
| 857 | 535.00 | 204.00 | 411.44 | 185.73 | NÃO | fora do lado solicitado |
| 858 | 535.00 | 203.00 | 411.89 | 186.73 | NÃO | fora do lado solicitado |
| 859 | 535.00 | 202.00 | 412.33 | 187.73 | NÃO | fora do lado solicitado |
| 860 | 535.00 | 201.00 | 412.78 | 188.73 | NÃO | fora do lado solicitado |
| 861 | 535.00 | 200.00 | 413.23 | 189.73 | NÃO | fora do lado solicitado |
| 862 | 535.00 | 199.00 | 413.68 | 190.73 | NÃO | fora do lado solicitado |
| 863 | 535.00 | 198.00 | 414.13 | 191.73 | NÃO | fora do lado solicitado |
| 864 | 534.00 | 197.00 | 413.70 | 192.73 | NÃO | fora do lado solicitado |
| 865 | 534.00 | 196.00 | 414.15 | 193.73 | NÃO | fora do lado solicitado |
| 866 | 534.00 | 195.00 | 414.61 | 194.73 | NÃO | fora do lado solicitado |
| 867 | 534.00 | 194.00 | 415.08 | 195.73 | NÃO | fora do lado solicitado |
| 868 | 534.00 | 193.00 | 415.54 | 196.73 | NÃO | fora do lado solicitado |
| 869 | 534.00 | 192.00 | 416.00 | 197.73 | NÃO | fora do lado solicitado |
| 870 | 534.00 | 191.00 | 416.47 | 198.73 | NÃO | fora do lado solicitado |
| 871 | 534.00 | 190.00 | 416.94 | 199.73 | NÃO | fora do lado solicitado |
| 872 | 533.00 | 189.00 | 416.53 | 200.73 | NÃO | fora do lado solicitado |
| 873 | 533.00 | 188.00 | 417.00 | 201.73 | NÃO | fora do lado solicitado |
| 874 | 533.00 | 187.00 | 417.48 | 202.73 | NÃO | fora do lado solicitado |
| 875 | 533.00 | 186.00 | 417.96 | 203.73 | NÃO | fora do lado solicitado |
| 876 | 533.00 | 185.00 | 418.44 | 204.73 | NÃO | fora do lado solicitado |
| 877 | 533.00 | 184.00 | 418.92 | 205.73 | NÃO | fora da faixa vertical |
| 878 | 533.00 | 183.00 | 419.40 | 206.73 | NÃO | fora da faixa vertical |
| 879 | 533.00 | 182.00 | 419.89 | 207.73 | NÃO | fora da faixa vertical |
| 880 | 532.00 | 181.00 | 419.50 | 208.73 | NÃO | fora da faixa vertical |
| 881 | 532.00 | 180.00 | 419.99 | 209.73 | NÃO | fora da faixa vertical |
| 882 | 532.00 | 179.00 | 420.48 | 210.73 | NÃO | fora da faixa vertical |
| 883 | 532.00 | 178.00 | 420.98 | 211.73 | NÃO | fora da faixa vertical |
| 884 | 532.00 | 177.00 | 421.47 | 212.73 | NÃO | fora da faixa vertical |
| 885 | 531.00 | 176.00 | 421.10 | 213.73 | NÃO | fora da faixa vertical |
| 886 | 531.00 | 175.00 | 421.60 | 214.73 | NÃO | fora da faixa vertical |
| 887 | 531.00 | 174.00 | 422.10 | 215.73 | NÃO | fora da faixa vertical |
| 888 | 531.00 | 173.00 | 422.60 | 216.73 | NÃO | fora da faixa vertical |
| 889 | 530.00 | 172.00 | 422.25 | 217.73 | NÃO | fora da faixa vertical |
| 890 | 530.00 | 171.00 | 422.75 | 218.73 | NÃO | fora da faixa vertical |
| 891 | 530.00 | 170.00 | 423.26 | 219.73 | NÃO | fora da faixa vertical |
| 892 | 530.00 | 169.00 | 423.77 | 220.73 | NÃO | fora da faixa vertical |
| 893 | 530.00 | 168.00 | 424.29 | 221.73 | NÃO | fora da faixa vertical |
| 894 | 529.00 | 167.00 | 423.95 | 222.73 | NÃO | fora da faixa vertical |
| 895 | 529.00 | 166.00 | 424.46 | 223.73 | NÃO | fora da faixa vertical |
| 896 | 529.00 | 165.00 | 424.98 | 224.73 | NÃO | fora da faixa vertical |
| 897 | 529.00 | 164.00 | 425.50 | 225.73 | NÃO | fora da faixa vertical |
| 898 | 528.00 | 163.00 | 425.17 | 226.73 | NÃO | fora da faixa vertical |
| 899 | 528.00 | 162.00 | 425.70 | 227.73 | NÃO | fora da faixa vertical |
| 900 | 528.00 | 161.00 | 426.23 | 228.73 | NÃO | fora da faixa vertical |
| 901 | 528.00 | 160.00 | 426.76 | 229.73 | NÃO | fora da faixa vertical |
| 902 | 527.00 | 159.00 | 426.44 | 230.73 | NÃO | fora da faixa vertical |
| 903 | 527.00 | 158.00 | 426.97 | 231.73 | NÃO | fora da faixa vertical |
| 904 | 527.00 | 157.00 | 427.51 | 232.73 | NÃO | fora da faixa vertical |
| 905 | 526.00 | 156.00 | 427.20 | 233.73 | NÃO | fora da faixa vertical |
| 906 | 526.00 | 155.00 | 427.74 | 234.73 | NÃO | fora da faixa vertical |
| 907 | 526.00 | 154.00 | 428.28 | 235.73 | NÃO | fora da faixa vertical |
| 908 | 526.00 | 153.00 | 428.82 | 236.73 | NÃO | fora da faixa vertical |
| 909 | 525.00 | 152.00 | 428.53 | 237.73 | NÃO | fora da faixa vertical |
| 910 | 525.00 | 151.00 | 429.08 | 238.73 | NÃO | fora da faixa vertical |
| 911 | 525.00 | 150.00 | 429.62 | 239.73 | NÃO | fora da faixa vertical |
| 912 | 524.00 | 149.00 | 429.34 | 240.73 | NÃO | fora da faixa vertical |
| 913 | 524.00 | 148.00 | 429.89 | 241.73 | NÃO | fora da faixa vertical |
| 914 | 523.00 | 147.00 | 429.62 | 242.73 | NÃO | fora da faixa vertical |
| 915 | 523.00 | 146.00 | 430.17 | 243.73 | NÃO | fora da faixa vertical |
| 916 | 523.00 | 145.00 | 430.73 | 244.73 | NÃO | fora da faixa vertical |
| 917 | 522.00 | 144.00 | 430.46 | 245.73 | NÃO | fora da faixa vertical |
| 918 | 522.00 | 143.00 | 431.03 | 246.73 | NÃO | fora da faixa vertical |
| 919 | 522.00 | 142.00 | 431.59 | 247.73 | NÃO | fora da faixa vertical |
| 920 | 521.00 | 141.00 | 431.34 | 248.73 | NÃO | fora da faixa vertical |
| 921 | 521.00 | 140.00 | 431.90 | 249.73 | NÃO | fora da faixa vertical |
| 922 | 520.00 | 139.00 | 431.65 | 250.73 | NÃO | fora da faixa vertical |
| 923 | 520.00 | 138.00 | 432.23 | 251.73 | NÃO | fora da faixa vertical |
| 924 | 520.00 | 137.00 | 432.80 | 252.73 | NÃO | fora da faixa vertical |
| 925 | 519.00 | 136.00 | 432.56 | 253.73 | NÃO | fora da faixa vertical |
| 926 | 519.00 | 135.00 | 433.14 | 254.73 | NÃO | fora da faixa vertical |
| 927 | 518.00 | 134.00 | 432.91 | 255.73 | NÃO | fora da faixa vertical |
| 928 | 518.00 | 133.00 | 433.49 | 256.73 | NÃO | fora da faixa vertical |
| 929 | 517.00 | 132.00 | 433.26 | 257.73 | NÃO | fora da faixa vertical |
| 930 | 517.00 | 131.00 | 433.85 | 258.73 | NÃO | fora da faixa vertical |
| 931 | 516.00 | 130.00 | 433.63 | 259.73 | NÃO | fora da faixa vertical |
| 932 | 516.00 | 129.00 | 434.22 | 260.73 | NÃO | fora da faixa vertical |
| 933 | 515.00 | 128.00 | 434.01 | 261.73 | NÃO | fora da faixa vertical |
| 934 | 515.00 | 127.00 | 434.61 | 262.73 | NÃO | fora da faixa vertical |
| 935 | 514.00 | 126.00 | 434.40 | 263.73 | NÃO | fora da faixa vertical |
| 936 | 514.00 | 125.00 | 435.00 | 264.73 | NÃO | fora da faixa vertical |
| 937 | 513.00 | 124.00 | 434.80 | 265.73 | NÃO | fora da faixa vertical |
| 938 | 513.00 | 123.00 | 435.41 | 266.73 | NÃO | fora da faixa vertical |
| 939 | 512.00 | 122.00 | 435.21 | 267.73 | NÃO | fora da faixa vertical |
| 940 | 512.00 | 121.00 | 435.82 | 268.73 | NÃO | fora da faixa vertical |
| 941 | 511.00 | 120.00 | 435.64 | 269.73 | NÃO | fora da faixa vertical |
| 942 | 511.00 | 119.00 | 436.25 | 270.73 | NÃO | fora da faixa vertical |
| 943 | 510.00 | 118.00 | 436.07 | 271.73 | NÃO | fora da faixa vertical |
| 944 | 510.00 | 117.00 | 436.69 | 272.73 | NÃO | fora da faixa vertical |
| 945 | 509.00 | 116.00 | 436.52 | 273.73 | NÃO | fora da faixa vertical |
| 946 | 509.00 | 115.00 | 437.14 | 274.73 | NÃO | fora da faixa vertical |
| 947 | 508.00 | 114.00 | 436.98 | 275.73 | NÃO | fora da faixa vertical |
| 948 | 507.00 | 113.00 | 436.82 | 276.73 | NÃO | fora da faixa vertical |
| 949 | 507.00 | 112.00 | 437.44 | 277.73 | NÃO | fora da faixa vertical |
| 950 | 506.00 | 111.00 | 437.29 | 278.73 | NÃO | fora da faixa vertical |
| 951 | 506.00 | 110.00 | 437.92 | 279.73 | NÃO | fora da faixa vertical |
| 952 | 505.00 | 109.00 | 437.78 | 280.73 | NÃO | fora da faixa vertical |
| 953 | 504.00 | 108.00 | 437.64 | 281.73 | NÃO | fora da faixa vertical |
| 954 | 504.00 | 107.00 | 438.28 | 282.73 | NÃO | fora da faixa vertical |
| 955 | 503.00 | 106.00 | 438.14 | 283.73 | NÃO | fora da faixa vertical |
| 956 | 503.00 | 105.00 | 438.78 | 284.73 | NÃO | fora da faixa vertical |
| 957 | 502.00 | 104.00 | 438.66 | 285.73 | NÃO | fora da faixa vertical |
| 958 | 501.00 | 103.00 | 438.54 | 286.73 | NÃO | fora da faixa vertical |
| 959 | 501.00 | 102.00 | 439.18 | 287.73 | NÃO | fora da faixa vertical |
| 960 | 500.00 | 101.00 | 439.07 | 288.73 | NÃO | fora da faixa vertical |
| 961 | 499.00 | 100.00 | 438.96 | 289.73 | NÃO | fora da faixa vertical |
| 962 | 498.00 | 99.00 | 438.85 | 290.73 | NÃO | fora da faixa vertical |
| 963 | 498.00 | 98.00 | 439.51 | 291.73 | NÃO | fora da faixa vertical |
| 964 | 497.00 | 97.00 | 439.41 | 292.73 | NÃO | fora da faixa vertical |
| 965 | 496.00 | 96.00 | 439.32 | 293.73 | NÃO | fora da faixa vertical |
| 966 | 495.00 | 95.00 | 439.23 | 294.73 | NÃO | fora da faixa vertical |
| 967 | 495.00 | 94.00 | 439.89 | 295.73 | NÃO | fora da faixa vertical |
| 968 | 494.00 | 93.00 | 439.81 | 296.73 | NÃO | fora da faixa vertical |
| 969 | 493.00 | 92.00 | 439.73 | 297.73 | NÃO | fora da faixa vertical |
| 970 | 492.00 | 91.00 | 439.66 | 298.73 | NÃO | fora da faixa vertical |
| 971 | 492.00 | 90.00 | 440.33 | 299.73 | NÃO | fora da faixa vertical |
| 972 | 491.00 | 89.00 | 440.27 | 300.73 | NÃO | fora da faixa vertical |
| 973 | 490.00 | 88.00 | 440.20 | 301.73 | NÃO | fora da faixa vertical |
| 974 | 489.00 | 87.00 | 440.15 | 302.73 | NÃO | fora da faixa vertical |
| 975 | 489.00 | 86.00 | 440.83 | 303.73 | NÃO | fora da faixa vertical |
| 976 | 488.00 | 85.00 | 440.78 | 304.73 | NÃO | fora da faixa vertical |
| 977 | 487.00 | 84.00 | 440.73 | 305.73 | NÃO | fora da faixa vertical |
| 978 | 486.00 | 83.00 | 440.69 | 306.73 | NÃO | fora da faixa vertical |
| 979 | 485.00 | 82.00 | 440.66 | 307.73 | NÃO | fora da faixa vertical |
| 980 | 484.00 | 81.00 | 440.62 | 308.73 | NÃO | fora da faixa vertical |
| 981 | 483.00 | 80.00 | 440.60 | 309.73 | NÃO | fora da faixa vertical |
| 982 | 482.00 | 79.00 | 440.57 | 310.73 | NÃO | fora da faixa vertical |
| 983 | 481.00 | 78.00 | 440.56 | 311.73 | NÃO | fora da faixa vertical |
| 984 | 480.00 | 77.00 | 440.54 | 312.73 | NÃO | fora da faixa vertical |
| 985 | 480.00 | 76.00 | 441.24 | 313.73 | NÃO | fora da faixa vertical |
| 986 | 479.00 | 75.00 | 441.24 | 314.73 | NÃO | fora da faixa vertical |
| 987 | 478.00 | 74.00 | 441.23 | 315.73 | NÃO | fora da faixa vertical |
| 988 | 477.00 | 73.00 | 441.24 | 316.73 | NÃO | fora da faixa vertical |
| 989 | 476.00 | 72.00 | 441.24 | 317.73 | NÃO | fora da faixa vertical |
| 990 | 475.00 | 71.00 | 441.26 | 318.73 | NÃO | fora da faixa vertical |
| 991 | 474.00 | 70.00 | 441.27 | 319.73 | NÃO | fora da faixa vertical |
| 992 | 473.00 | 69.00 | 441.29 | 320.73 | NÃO | fora da faixa vertical |
| 993 | 472.00 | 68.00 | 441.32 | 321.73 | NÃO | fora da faixa vertical |
| 994 | 471.00 | 67.00 | 441.35 | 322.73 | NÃO | fora da faixa vertical |
| 995 | 470.00 | 66.00 | 441.38 | 323.73 | NÃO | fora da faixa vertical |
| 996 | 469.00 | 65.00 | 441.42 | 324.73 | NÃO | fora da faixa vertical |
| 997 | 468.00 | 65.00 | 440.73 | 324.73 | NÃO | fora da faixa vertical |
| 998 | 467.00 | 64.00 | 440.78 | 325.73 | NÃO | fora da faixa vertical |
| 999 | 466.00 | 63.00 | 440.83 | 326.73 | NÃO | fora da faixa vertical |
| 1000 | 465.00 | 62.00 | 440.88 | 327.73 | NÃO | fora da faixa vertical |
| 1001 | 464.00 | 61.00 | 440.94 | 328.73 | NÃO | fora da faixa vertical |
| 1002 | 463.00 | 60.00 | 441.00 | 329.73 | NÃO | fora da faixa vertical |
| 1003 | 462.00 | 59.00 | 441.07 | 330.73 | NÃO | fora da faixa vertical |
| 1004 | 461.00 | 58.00 | 441.15 | 331.73 | NÃO | fora da faixa vertical |
| 1005 | 460.00 | 58.00 | 440.48 | 331.73 | NÃO | fora da faixa vertical |
| 1006 | 459.00 | 57.00 | 440.56 | 332.73 | NÃO | fora da faixa vertical |
| 1007 | 458.00 | 56.00 | 440.64 | 333.73 | NÃO | fora da faixa vertical |
| 1008 | 457.00 | 56.00 | 439.98 | 333.73 | NÃO | fora da faixa vertical |
| 1009 | 456.00 | 55.00 | 440.07 | 334.73 | NÃO | fora da faixa vertical |
| 1010 | 455.00 | 54.00 | 440.16 | 335.73 | NÃO | fora da faixa vertical |
| 1011 | 454.00 | 53.00 | 440.26 | 336.73 | NÃO | fora da faixa vertical |
| 1012 | 453.00 | 53.00 | 439.61 | 336.73 | NÃO | fora da faixa vertical |
| 1013 | 452.00 | 52.00 | 439.72 | 337.73 | NÃO | fora da faixa vertical |
| 1014 | 451.00 | 51.00 | 439.83 | 338.73 | NÃO | fora da faixa vertical |
| 1015 | 450.00 | 50.00 | 439.95 | 339.73 | NÃO | fora da faixa vertical |
| 1016 | 449.00 | 50.00 | 439.30 | 339.73 | NÃO | fora da faixa vertical |
| 1017 | 448.00 | 49.00 | 439.42 | 340.73 | NÃO | fora da faixa vertical |
| 1018 | 447.00 | 48.00 | 439.55 | 341.73 | NÃO | fora da faixa vertical |
| 1019 | 446.00 | 48.00 | 438.91 | 341.73 | NÃO | fora da faixa vertical |
| 1020 | 445.00 | 47.00 | 439.05 | 342.73 | NÃO | fora da faixa vertical |
| 1021 | 444.00 | 46.00 | 439.19 | 343.73 | NÃO | fora da faixa vertical |
| 1022 | 443.00 | 46.00 | 438.55 | 343.73 | NÃO | fora da faixa vertical |
| 1023 | 442.00 | 45.00 | 438.70 | 344.73 | NÃO | fora da faixa vertical |
| 1024 | 441.00 | 44.00 | 438.85 | 345.73 | NÃO | fora da faixa vertical |
| 1025 | 440.00 | 44.00 | 438.22 | 345.73 | NÃO | fora da faixa vertical |
| 1026 | 439.00 | 43.00 | 438.38 | 346.73 | NÃO | fora da faixa vertical |
| 1027 | 438.00 | 43.00 | 437.76 | 346.73 | NÃO | fora da faixa vertical |
| 1028 | 437.00 | 42.00 | 437.92 | 347.73 | NÃO | fora da faixa vertical |
| 1029 | 436.00 | 41.00 | 438.09 | 348.73 | NÃO | fora da faixa vertical |
| 1030 | 435.00 | 41.00 | 437.48 | 348.73 | NÃO | fora da faixa vertical |
| 1031 | 434.00 | 40.00 | 437.65 | 349.73 | NÃO | fora da faixa vertical |
| 1032 | 433.00 | 39.00 | 437.83 | 350.73 | NÃO | fora da faixa vertical |
| 1033 | 432.00 | 39.00 | 437.22 | 350.73 | NÃO | fora da faixa vertical |
| 1034 | 431.00 | 38.00 | 437.41 | 351.73 | NÃO | fora da faixa vertical |
| 1035 | 430.00 | 38.00 | 436.81 | 351.73 | NÃO | fora da faixa vertical |
| 1036 | 429.00 | 37.00 | 437.00 | 352.73 | NÃO | fora da faixa vertical |
| 1037 | 428.00 | 37.00 | 436.40 | 352.73 | NÃO | fora da faixa vertical |
| 1038 | 427.00 | 36.00 | 436.60 | 353.73 | NÃO | fora da faixa vertical |
| 1039 | 426.00 | 36.00 | 436.00 | 353.73 | NÃO | fora da faixa vertical |
| 1040 | 425.00 | 35.00 | 436.21 | 354.73 | NÃO | fora da faixa vertical |
| 1041 | 424.00 | 35.00 | 435.62 | 354.73 | NÃO | fora da faixa vertical |
| 1042 | 423.00 | 34.00 | 435.84 | 355.73 | NÃO | fora da faixa vertical |
| 1043 | 422.00 | 34.00 | 435.25 | 355.73 | NÃO | fora da faixa vertical |
| 1044 | 421.00 | 33.00 | 435.47 | 356.73 | NÃO | fora da faixa vertical |
| 1045 | 420.00 | 33.00 | 434.89 | 356.73 | NÃO | fora da faixa vertical |
| 1046 | 419.00 | 32.00 | 435.11 | 357.73 | NÃO | fora da faixa vertical |
| 1047 | 418.00 | 32.00 | 434.53 | 357.73 | NÃO | fora da faixa vertical |
| 1048 | 417.00 | 31.00 | 434.77 | 358.73 | NÃO | fora da faixa vertical |
| 1049 | 416.00 | 31.00 | 434.19 | 358.73 | NÃO | fora da faixa vertical |
| 1050 | 415.00 | 30.00 | 434.44 | 359.73 | NÃO | fora da faixa vertical |
| 1051 | 414.00 | 30.00 | 433.87 | 359.73 | NÃO | fora da faixa vertical |
| 1052 | 413.00 | 29.00 | 434.12 | 360.73 | NÃO | fora da faixa vertical |
| 1053 | 412.00 | 29.00 | 433.55 | 360.73 | NÃO | fora da faixa vertical |
| 1054 | 411.00 | 28.00 | 433.81 | 361.73 | NÃO | fora da faixa vertical |
| 1055 | 410.00 | 28.00 | 433.24 | 361.73 | NÃO | fora da faixa vertical |
| 1056 | 409.00 | 28.00 | 432.68 | 361.73 | NÃO | fora da faixa vertical |
| 1057 | 408.00 | 27.00 | 432.95 | 362.73 | NÃO | fora da faixa vertical |
| 1058 | 407.00 | 27.00 | 432.39 | 362.73 | NÃO | fora da faixa vertical |
| 1059 | 406.00 | 27.00 | 431.83 | 362.73 | NÃO | fora da faixa vertical |
| 1060 | 405.00 | 26.00 | 432.11 | 363.73 | NÃO | fora da faixa vertical |
| 1061 | 404.00 | 26.00 | 431.56 | 363.73 | NÃO | fora da faixa vertical |
| 1062 | 403.00 | 25.00 | 431.84 | 364.73 | NÃO | fora da faixa vertical |
| 1063 | 402.00 | 25.00 | 431.30 | 364.73 | NÃO | fora da faixa vertical |
| 1064 | 401.00 | 25.00 | 430.75 | 364.73 | NÃO | fora da faixa vertical |
| 1065 | 400.00 | 24.00 | 431.05 | 365.73 | NÃO | fora da faixa vertical |
| 1066 | 399.00 | 24.00 | 430.50 | 365.73 | NÃO | fora da faixa vertical |
| 1067 | 398.00 | 24.00 | 429.96 | 365.73 | NÃO | fora da faixa vertical |
| 1068 | 397.00 | 23.00 | 430.27 | 366.73 | NÃO | fora da faixa vertical |
| 1069 | 396.00 | 23.00 | 429.73 | 366.73 | NÃO | fora da faixa vertical |
| 1070 | 395.00 | 23.00 | 429.20 | 366.73 | NÃO | fora da faixa vertical |
| 1071 | 394.00 | 22.00 | 429.51 | 367.73 | NÃO | fora da faixa vertical |
| 1072 | 393.00 | 22.00 | 428.98 | 367.73 | NÃO | fora da faixa vertical |
| 1073 | 392.00 | 22.00 | 428.45 | 367.73 | NÃO | fora da faixa vertical |
| 1074 | 391.00 | 21.00 | 428.78 | 368.73 | NÃO | fora da faixa vertical |
| 1075 | 390.00 | 21.00 | 428.25 | 368.73 | NÃO | fora da faixa vertical |
| 1076 | 389.00 | 21.00 | 427.73 | 368.73 | NÃO | fora da faixa vertical |
| 1077 | 388.00 | 21.00 | 427.21 | 368.73 | NÃO | fora da faixa vertical |
| 1078 | 387.00 | 20.00 | 427.55 | 369.73 | NÃO | fora da faixa vertical |
| 1079 | 386.00 | 20.00 | 427.03 | 369.73 | NÃO | fora da faixa vertical |
| 1080 | 385.00 | 20.00 | 426.52 | 369.73 | NÃO | fora da faixa vertical |
| 1081 | 384.00 | 19.00 | 426.86 | 370.73 | NÃO | fora da faixa vertical |
| 1082 | 383.00 | 19.00 | 426.35 | 370.73 | NÃO | fora da faixa vertical |
| 1083 | 382.00 | 19.00 | 425.85 | 370.73 | NÃO | fora da faixa vertical |
| 1084 | 381.00 | 19.00 | 425.34 | 370.73 | NÃO | fora da faixa vertical |
| 1085 | 380.00 | 18.00 | 425.70 | 371.73 | NÃO | fora da faixa vertical |
| 1086 | 379.00 | 18.00 | 425.20 | 371.73 | NÃO | fora da faixa vertical |
| 1087 | 378.00 | 18.00 | 424.70 | 371.73 | NÃO | fora da faixa vertical |
| 1088 | 377.00 | 18.00 | 424.20 | 371.73 | NÃO | fora da faixa vertical |
| 1089 | 376.00 | 17.00 | 424.57 | 372.73 | NÃO | fora da faixa vertical |
| 1090 | 375.00 | 17.00 | 424.08 | 372.73 | NÃO | fora da faixa vertical |
| 1091 | 374.00 | 17.00 | 423.59 | 372.73 | NÃO | fora da faixa vertical |
| 1092 | 373.00 | 17.00 | 423.10 | 372.73 | NÃO | fora da faixa vertical |
| 1093 | 372.00 | 17.00 | 422.61 | 372.73 | NÃO | fora da faixa vertical |
| 1094 | 371.00 | 16.00 | 423.00 | 373.73 | NÃO | fora da faixa vertical |
| 1095 | 370.00 | 16.00 | 422.51 | 373.73 | NÃO | fora da faixa vertical |
| 1096 | 369.00 | 16.00 | 422.03 | 373.73 | NÃO | fora da faixa vertical |
| 1097 | 368.00 | 16.00 | 421.55 | 373.73 | NÃO | fora da faixa vertical |
| 1098 | 367.00 | 16.00 | 421.07 | 373.73 | NÃO | fora da faixa vertical |
| 1099 | 366.00 | 15.00 | 421.47 | 374.73 | NÃO | fora da faixa vertical |
| 1100 | 365.00 | 15.00 | 421.00 | 374.73 | NÃO | fora da faixa vertical |
| 1101 | 364.00 | 15.00 | 420.53 | 374.73 | NÃO | fora da faixa vertical |
| 1102 | 363.00 | 15.00 | 420.06 | 374.73 | NÃO | fora da faixa vertical |
| 1103 | 362.00 | 15.00 | 419.59 | 374.73 | NÃO | fora da faixa vertical |
| 1104 | 361.00 | 15.00 | 419.13 | 374.73 | NÃO | fora da faixa vertical |
| 1105 | 360.00 | 15.00 | 418.66 | 374.73 | NÃO | fora da faixa vertical |
| 1106 | 359.00 | 15.00 | 418.20 | 374.73 | NÃO | fora da faixa vertical |
| 1107 | 358.00 | 14.00 | 418.63 | 375.73 | NÃO | fora da faixa vertical |
| 1108 | 357.00 | 14.00 | 418.17 | 375.73 | NÃO | fora da faixa vertical |
| 1109 | 356.00 | 14.00 | 417.71 | 375.73 | NÃO | fora da faixa vertical |
| 1110 | 355.00 | 14.00 | 417.26 | 375.73 | NÃO | fora da faixa vertical |
| 1111 | 354.00 | 14.00 | 416.81 | 375.73 | NÃO | fora da faixa vertical |
| 1112 | 353.00 | 14.00 | 416.36 | 375.73 | NÃO | fora da faixa vertical |
| 1113 | 352.00 | 14.00 | 415.91 | 375.73 | NÃO | fora da faixa vertical |
| 1114 | 351.00 | 14.00 | 415.46 | 375.73 | NÃO | fora da faixa vertical |
| 1115 | 350.00 | 14.00 | 415.02 | 375.73 | NÃO | fora da faixa vertical |
| 1116 | 349.00 | 14.00 | 414.58 | 375.73 | NÃO | fora da faixa vertical |
| 1117 | 348.00 | 13.00 | 415.03 | 376.73 | NÃO | fora da faixa vertical |
| 1118 | 347.00 | 13.00 | 414.60 | 376.73 | NÃO | fora da faixa vertical |
| 1119 | 346.00 | 13.00 | 414.16 | 376.73 | NÃO | fora da faixa vertical |
| 1120 | 345.00 | 13.00 | 413.73 | 376.73 | NÃO | fora da faixa vertical |
| 1121 | 344.00 | 13.00 | 413.30 | 376.73 | NÃO | fora da faixa vertical |
| 1122 | 343.00 | 13.00 | 412.87 | 376.73 | NÃO | fora da faixa vertical |
| 1123 | 342.00 | 13.00 | 412.44 | 376.73 | NÃO | fora da faixa vertical |
| 1124 | 341.00 | 13.00 | 412.01 | 376.73 | NÃO | fora da faixa vertical |
| 1125 | 340.00 | 13.00 | 411.59 | 376.73 | NÃO | fora da faixa vertical |
| 1126 | 339.00 | 13.00 | 411.17 | 376.73 | NÃO | fora da faixa vertical |
| 1127 | 338.00 | 13.00 | 410.75 | 376.73 | NÃO | fora da faixa vertical |
| 1128 | 337.00 | 13.00 | 410.33 | 376.73 | NÃO | fora da faixa vertical |
| 1129 | 336.00 | 13.00 | 409.91 | 376.73 | NÃO | fora da faixa vertical |
| 1130 | 335.00 | 13.00 | 409.50 | 376.73 | NÃO | fora da faixa vertical |
| 1131 | 334.00 | 13.00 | 409.09 | 376.73 | NÃO | fora da faixa vertical |
| 1132 | 333.00 | 13.00 | 408.68 | 376.73 | NÃO | fora da faixa vertical |
| 1133 | 332.00 | 13.00 | 408.27 | 376.73 | NÃO | fora da faixa vertical |
| 1134 | 331.00 | 13.00 | 407.87 | 376.73 | NÃO | fora da faixa vertical |
| 1135 | 330.00 | 13.00 | 407.46 | 376.73 | NÃO | fora da faixa vertical |
| 1136 | 329.00 | 13.00 | 407.06 | 376.73 | NÃO | fora da faixa vertical |
| 1137 | 328.00 | 13.00 | 406.66 | 376.73 | NÃO | fora da faixa vertical |
| 1138 | 327.00 | 13.00 | 406.26 | 376.73 | NÃO | fora da faixa vertical |
| 1139 | 326.00 | 13.00 | 405.87 | 376.73 | NÃO | fora da faixa vertical |
| 1140 | 325.00 | 13.00 | 405.48 | 376.73 | NÃO | fora da faixa vertical |
| 1141 | 324.00 | 13.00 | 405.08 | 376.73 | NÃO | fora da faixa vertical |
| 1142 | 323.00 | 13.00 | 404.69 | 376.73 | NÃO | fora da faixa vertical |
| 1143 | 322.00 | 13.00 | 404.31 | 376.73 | NÃO | fora da faixa vertical |
| 1144 | 321.00 | 13.00 | 403.92 | 376.73 | NÃO | fora da faixa vertical |
| 1145 | 320.00 | 13.00 | 403.54 | 376.73 | NÃO | fora da faixa vertical |
| 1146 | 319.00 | 13.00 | 403.16 | 376.73 | NÃO | fora da faixa vertical |
| 1147 | 318.00 | 13.00 | 402.78 | 376.73 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 241 | 132.00 | 185.00 | -34.00 | -204.73 |
| 242 | 132.00 | 186.00 | -34.00 | -203.73 |
| 243 | 132.00 | 187.00 | -34.00 | -202.73 |
| 244 | 132.00 | 188.00 | -34.00 | -201.73 |
| 245 | 132.00 | 189.00 | -34.00 | -200.73 |
| 246 | 132.00 | 190.00 | -34.00 | -199.73 |
| 247 | 132.00 | 191.00 | -34.00 | -198.73 |
| 248 | 131.00 | 192.00 | -35.00 | -197.73 |
| 249 | 131.00 | 193.00 | -35.00 | -196.73 |
| 250 | 131.00 | 194.00 | -35.00 | -195.73 |
| 251 | 131.00 | 195.00 | -35.00 | -194.73 |
| 252 | 131.00 | 196.00 | -35.00 | -193.73 |
| 253 | 131.00 | 197.00 | -35.00 | -192.73 |
| 254 | 131.00 | 198.00 | -35.00 | -191.73 |
| 255 | 131.00 | 199.00 | -35.00 | -190.73 |
| 256 | 130.00 | 200.00 | -36.00 | -189.73 |
| 257 | 130.00 | 201.00 | -36.00 | -188.73 |
| 258 | 130.00 | 202.00 | -36.00 | -187.73 |
| 259 | 130.00 | 203.00 | -36.00 | -186.73 |
| 260 | 130.00 | 204.00 | -36.00 | -185.73 |
| 261 | 130.00 | 205.00 | -36.00 | -184.73 |
| 262 | 130.00 | 206.00 | -36.00 | -183.73 |
| 263 | 130.00 | 207.00 | -36.00 | -182.73 |
| 264 | 130.00 | 208.00 | -36.00 | -181.73 |
| 265 | 130.00 | 209.00 | -36.00 | -180.73 |
| 266 | 130.00 | 210.00 | -36.00 | -179.73 |
| 267 | 130.00 | 211.00 | -36.00 | -178.73 |
| 268 | 130.00 | 212.00 | -36.00 | -177.73 |
| 269 | 130.00 | 213.00 | -36.00 | -176.73 |
| 270 | 130.00 | 214.00 | -36.00 | -175.73 |
| 271 | 130.00 | 215.00 | -36.00 | -174.73 |
| 272 | 130.00 | 216.00 | -36.00 | -173.73 |
| 273 | 130.00 | 217.00 | -36.00 | -172.73 |
| 274 | 130.00 | 218.00 | -36.00 | -171.73 |
| 275 | 130.00 | 219.00 | -36.00 | -170.73 |
| 276 | 130.00 | 220.00 | -36.00 | -169.73 |
| 277 | 130.00 | 221.00 | -36.00 | -168.73 |
| 278 | 130.00 | 222.00 | -36.00 | -167.73 |
| 279 | 130.00 | 223.00 | -36.00 | -166.73 |
| 280 | 130.00 | 224.00 | -36.00 | -165.73 |
| 281 | 130.00 | 225.00 | -36.00 | -164.73 |
| 282 | 130.00 | 226.00 | -36.00 | -163.73 |
| 283 | 130.00 | 227.00 | -36.00 | -162.73 |
| 284 | 130.00 | 228.00 | -36.00 | -161.73 |
| 285 | 130.00 | 229.00 | -36.00 | -160.73 |
| 286 | 130.00 | 230.00 | -36.00 | -159.73 |
| 287 | 130.00 | 231.00 | -36.00 | -158.73 |
| 288 | 131.00 | 232.00 | -35.00 | -157.73 |
| 289 | 131.00 | 233.00 | -35.00 | -156.73 |
| 290 | 131.00 | 234.00 | -35.00 | -155.73 |
| 291 | 131.00 | 235.00 | -35.00 | -154.73 |
| 292 | 131.00 | 236.00 | -35.00 | -153.73 |
| 293 | 131.00 | 237.00 | -35.00 | -152.73 |
| 294 | 131.00 | 238.00 | -35.00 | -151.73 |
| 295 | 131.00 | 239.00 | -35.00 | -150.73 |
| 296 | 131.00 | 240.00 | -35.00 | -149.73 |
| 297 | 132.00 | 241.00 | -34.00 | -148.73 |
| 298 | 132.00 | 242.00 | -34.00 | -147.73 |
| 299 | 132.00 | 243.00 | -34.00 | -146.73 |
| 300 | 132.00 | 244.00 | -34.00 | -145.73 |
| 301 | 132.00 | 245.00 | -34.00 | -144.73 |
| 302 | 132.00 | 246.00 | -34.00 | -143.73 |
| 303 | 132.00 | 247.00 | -34.00 | -142.73 |
| 304 | 133.00 | 248.00 | -33.00 | -141.73 |
| 305 | 133.00 | 249.00 | -33.00 | -140.73 |
| 306 | 133.00 | 250.00 | -33.00 | -139.73 |
| 307 | 133.00 | 251.00 | -33.00 | -138.73 |
| 308 | 133.00 | 252.00 | -33.00 | -137.73 |
| 309 | 134.00 | 253.00 | -32.00 | -136.73 |
| 310 | 134.00 | 254.00 | -32.00 | -135.73 |
| 311 | 134.00 | 255.00 | -32.00 | -134.73 |
| 312 | 134.00 | 256.00 | -32.00 | -133.73 |
| 313 | 134.00 | 257.00 | -32.00 | -132.73 |
| 314 | 135.00 | 258.00 | -31.00 | -131.73 |
| 315 | 135.00 | 259.00 | -31.00 | -130.73 |
| 316 | 135.00 | 260.00 | -31.00 | -129.73 |
| 317 | 135.00 | 261.00 | -31.00 | -128.73 |
| 318 | 135.00 | 262.00 | -31.00 | -127.73 |
| 319 | 136.00 | 263.00 | -30.00 | -126.73 |
| 320 | 136.00 | 264.00 | -30.00 | -125.73 |
| 321 | 136.00 | 265.00 | -30.00 | -124.73 |
| 322 | 136.00 | 266.00 | -30.00 | -123.73 |
| 323 | 137.00 | 267.00 | -29.00 | -122.73 |
| 324 | 137.00 | 268.00 | -29.00 | -121.73 |
| 325 | 137.00 | 269.00 | -29.00 | -120.73 |
| 326 | 137.00 | 270.00 | -29.00 | -119.73 |
| 327 | 138.00 | 271.00 | -28.00 | -118.73 |
| 328 | 138.00 | 272.00 | -28.00 | -117.73 |
| 329 | 138.00 | 273.00 | -28.00 | -116.73 |
| 330 | 139.00 | 274.00 | -27.00 | -115.73 |
| 331 | 139.00 | 275.00 | -27.00 | -114.73 |
| 332 | 139.00 | 276.00 | -27.00 | -113.73 |
| 333 | 139.00 | 277.00 | -27.00 | -112.73 |
| 334 | 140.00 | 278.00 | -26.00 | -111.73 |
| 335 | 140.00 | 279.00 | -26.00 | -110.73 |
| 336 | 140.00 | 280.00 | -26.00 | -109.73 |
| 337 | 141.00 | 281.00 | -25.00 | -108.73 |
| 338 | 141.00 | 282.00 | -25.00 | -107.73 |
| 339 | 141.00 | 283.00 | -25.00 | -106.73 |
| 340 | 142.00 | 284.00 | -24.00 | -105.73 |
| 341 | 142.00 | 285.00 | -24.00 | -104.73 |
| 342 | 142.00 | 286.00 | -24.00 | -103.73 |
| 343 | 143.00 | 287.00 | -23.00 | -102.73 |
| 344 | 143.00 | 288.00 | -23.00 | -101.73 |
| 345 | 144.00 | 289.00 | -22.00 | -100.73 |
| 346 | 144.00 | 290.00 | -22.00 | -99.73 |
| 347 | 144.00 | 291.00 | -22.00 | -98.73 |
| 348 | 145.00 | 292.00 | -21.00 | -97.73 |
| 349 | 145.00 | 293.00 | -21.00 | -96.73 |
| 350 | 145.00 | 294.00 | -21.00 | -95.73 |
| 351 | 146.00 | 295.00 | -20.00 | -94.73 |
| 352 | 146.00 | 296.00 | -20.00 | -93.73 |
| 353 | 147.00 | 297.00 | -19.00 | -92.73 |
| 354 | 147.00 | 298.00 | -19.00 | -91.73 |
| 355 | 148.00 | 299.00 | -18.00 | -90.73 |
| 356 | 148.00 | 300.00 | -18.00 | -89.73 |
| 357 | 149.00 | 301.00 | -17.00 | -88.73 |
| 358 | 149.00 | 302.00 | -17.00 | -87.73 |
| 359 | 150.00 | 303.00 | -16.00 | -86.73 |
| 360 | 150.00 | 304.00 | -16.00 | -85.73 |
| 361 | 151.00 | 305.00 | -15.00 | -84.73 |
| 362 | 151.00 | 306.00 | -15.00 | -83.73 |
| 363 | 152.00 | 307.00 | -14.00 | -82.73 |
| 364 | 152.00 | 308.00 | -14.00 | -81.73 |
| 365 | 153.00 | 309.00 | -13.00 | -80.73 |
| 366 | 153.00 | 310.00 | -13.00 | -79.73 |
| 367 | 154.00 | 311.00 | -12.00 | -78.73 |
| 368 | 154.00 | 312.00 | -12.00 | -77.73 |
| 369 | 155.00 | 313.00 | -11.00 | -76.73 |
| 370 | 155.00 | 314.00 | -11.00 | -75.73 |
| 371 | 156.00 | 315.00 | -10.00 | -74.73 |
| 372 | 157.00 | 316.00 | -9.00 | -73.73 |
| 373 | 157.00 | 317.00 | -9.00 | -72.73 |
| 374 | 158.00 | 318.00 | -8.00 | -71.73 |
| 375 | 158.00 | 319.00 | -8.00 | -70.73 |
| 376 | 159.00 | 320.00 | -7.00 | -69.73 |
| 377 | 160.00 | 321.00 | -6.00 | -68.73 |
| 378 | 160.00 | 322.00 | -6.00 | -67.73 |
| 379 | 161.00 | 323.00 | -5.00 | -66.73 |
| 380 | 161.00 | 324.00 | -5.00 | -65.73 |
| 381 | 162.00 | 325.00 | -4.00 | -64.73 |
| 382 | 163.00 | 326.00 | -3.00 | -63.73 |
| 383 | 163.00 | 327.00 | -3.00 | -62.73 |
| 384 | 164.00 | 328.00 | -2.00 | -61.73 |
| 385 | 165.00 | 329.00 | -1.00 | -60.73 |
| 386 | 165.00 | 330.00 | -1.00 | -59.73 |
| 387 | 166.00 | 331.00 | 0.00 | -58.73 |
| 388 | 167.00 | 332.00 | 1.00 | -57.73 |
| 389 | 167.00 | 333.00 | 1.00 | -56.73 |
| 390 | 168.00 | 334.00 | 2.00 | -55.73 |
| 391 | 169.00 | 335.00 | 3.00 | -54.73 |
| 392 | 170.00 | 336.00 | 4.00 | -53.73 |
| 393 | 170.00 | 337.00 | 4.00 | -52.73 |
| 394 | 171.00 | 338.00 | 5.00 | -51.73 |
| 395 | 172.00 | 339.00 | 6.00 | -50.73 |
| 396 | 173.00 | 340.00 | 7.00 | -49.73 |
| 397 | 173.00 | 341.00 | 7.00 | -48.73 |
| 398 | 174.00 | 342.00 | 8.00 | -47.73 |
| 399 | 175.00 | 343.00 | 9.00 | -46.73 |
| 400 | 176.00 | 344.00 | 10.00 | -45.73 |
| 401 | 177.00 | 345.00 | 11.00 | -44.73 |
| 402 | 177.00 | 346.00 | 11.00 | -43.73 |
| 403 | 178.00 | 347.00 | 12.00 | -42.73 |
| 404 | 179.00 | 348.00 | 13.00 | -41.73 |
| 405 | 180.00 | 349.00 | 14.00 | -40.73 |
| 406 | 181.00 | 350.00 | 15.00 | -39.73 |
| 407 | 182.00 | 351.00 | 16.00 | -38.73 |
| 408 | 183.00 | 352.00 | 17.00 | -37.73 |
| 409 | 184.00 | 353.00 | 18.00 | -36.73 |
| 410 | 185.00 | 354.00 | 19.00 | -35.73 |
| 411 | 186.00 | 355.00 | 20.00 | -34.73 |
| 412 | 186.00 | 356.00 | 20.00 | -33.73 |
| 413 | 187.00 | 357.00 | 21.00 | -32.73 |
| 414 | 188.00 | 358.00 | 22.00 | -31.73 |
| 415 | 189.00 | 359.00 | 23.00 | -30.73 |
| 416 | 190.00 | 360.00 | 24.00 | -29.73 |
| 417 | 191.00 | 361.00 | 25.00 | -28.73 |
| 418 | 192.00 | 361.00 | 26.00 | -28.73 |
| 419 | 193.00 | 362.00 | 27.00 | -27.73 |
| 420 | 194.00 | 363.00 | 28.00 | -26.73 |
| 421 | 195.00 | 364.00 | 29.00 | -25.73 |
| 422 | 196.00 | 365.00 | 30.00 | -24.73 |
| 423 | 197.00 | 366.00 | 31.00 | -23.73 |
| 424 | 198.00 | 367.00 | 32.00 | -22.73 |
| 425 | 199.00 | 368.00 | 33.00 | -21.73 |
| 426 | 200.00 | 369.00 | 34.00 | -20.73 |
| 427 | 201.00 | 370.00 | 35.00 | -19.73 |
| 428 | 202.00 | 371.00 | 36.00 | -18.73 |
| 429 | 203.00 | 372.00 | 37.00 | -17.73 |
| 430 | 204.00 | 372.00 | 38.00 | -17.73 |
| 431 | 205.00 | 373.00 | 39.00 | -16.73 |
| 432 | 206.00 | 374.00 | 40.00 | -15.73 |
| 433 | 207.00 | 375.00 | 41.00 | -14.73 |
| 434 | 208.00 | 375.00 | 42.00 | -14.73 |
| 435 | 209.00 | 376.00 | 43.00 | -13.73 |
| 436 | 210.00 | 377.00 | 44.00 | -12.73 |
| 437 | 211.00 | 378.00 | 45.00 | -11.73 |
| 438 | 212.00 | 378.00 | 46.00 | -11.73 |
| 439 | 213.00 | 379.00 | 47.00 | -10.73 |
| 440 | 214.00 | 380.00 | 48.00 | -9.73 |
| 441 | 215.00 | 381.00 | 49.00 | -8.73 |
| 442 | 216.00 | 381.00 | 50.00 | -8.73 |
| 443 | 217.00 | 382.00 | 51.00 | -7.73 |
| 444 | 218.00 | 383.00 | 52.00 | -6.73 |
| 445 | 219.00 | 384.00 | 53.00 | -5.73 |
| 446 | 220.00 | 384.00 | 54.00 | -5.73 |
| 447 | 221.00 | 385.00 | 55.00 | -4.73 |
| 448 | 222.00 | 386.00 | 56.00 | -3.73 |
| 449 | 223.00 | 386.00 | 57.00 | -3.73 |
| 450 | 224.00 | 386.00 | 58.00 | -3.73 |
| 451 | 225.00 | 386.00 | 59.00 | -3.73 |
| 452 | 226.00 | 386.00 | 60.00 | -3.73 |
| 453 | 227.00 | 386.00 | 61.00 | -3.73 |
| 454 | 228.00 | 386.00 | 62.00 | -3.73 |
| 455 | 229.00 | 386.00 | 63.00 | -3.73 |
| 456 | 230.00 | 386.00 | 64.00 | -3.73 |
| 457 | 231.00 | 386.00 | 65.00 | -3.73 |
| 458 | 232.00 | 386.00 | 66.00 | -3.73 |
| 459 | 233.00 | 386.00 | 67.00 | -3.73 |
| 460 | 234.00 | 386.00 | 68.00 | -3.73 |
| 461 | 235.00 | 386.00 | 69.00 | -3.73 |
| 462 | 236.00 | 386.00 | 70.00 | -3.73 |
| 463 | 237.00 | 386.00 | 71.00 | -3.73 |
| 464 | 238.00 | 386.00 | 72.00 | -3.73 |
| 465 | 239.00 | 386.00 | 73.00 | -3.73 |
| 466 | 240.00 | 386.00 | 74.00 | -3.73 |
| 467 | 241.00 | 386.00 | 75.00 | -3.73 |
| 468 | 242.00 | 386.00 | 76.00 | -3.73 |
| 469 | 243.00 | 386.00 | 77.00 | -3.73 |
| 470 | 244.00 | 386.00 | 78.00 | -3.73 |
| 471 | 245.00 | 386.00 | 79.00 | -3.73 |
| 472 | 246.00 | 386.00 | 80.00 | -3.73 |
| 473 | 247.00 | 386.00 | 81.00 | -3.73 |
| 474 | 248.00 | 386.00 | 82.00 | -3.73 |
| 475 | 249.00 | 386.00 | 83.00 | -3.73 |
| 476 | 250.00 | 386.00 | 84.00 | -3.73 |
| 477 | 251.00 | 386.00 | 85.00 | -3.73 |
| 478 | 252.00 | 386.00 | 86.00 | -3.73 |
| 479 | 253.00 | 386.00 | 87.00 | -3.73 |
| 480 | 254.00 | 386.00 | 88.00 | -3.73 |
| 481 | 255.00 | 386.00 | 89.00 | -3.73 |
| 482 | 256.00 | 386.00 | 90.00 | -3.73 |
| 483 | 257.00 | 386.00 | 91.00 | -3.73 |
| 484 | 258.00 | 386.00 | 92.00 | -3.73 |
| 485 | 259.00 | 386.00 | 93.00 | -3.73 |
| 486 | 260.00 | 386.00 | 94.00 | -3.73 |
| 487 | 261.00 | 386.00 | 95.00 | -3.73 |
| 488 | 262.00 | 386.00 | 96.00 | -3.73 |
| 489 | 263.00 | 386.00 | 97.00 | -3.73 |
| 490 | 264.00 | 386.00 | 98.00 | -3.73 |
| 491 | 265.00 | 386.00 | 99.00 | -3.73 |
| 492 | 266.00 | 386.00 | 100.00 | -3.73 |
| 493 | 267.00 | 386.00 | 101.00 | -3.73 |
| 494 | 268.00 | 386.00 | 102.00 | -3.73 |
| 495 | 269.00 | 386.00 | 103.00 | -3.73 |
| 496 | 270.00 | 386.00 | 104.00 | -3.73 |
| 497 | 271.00 | 386.00 | 105.00 | -3.73 |
| 498 | 272.00 | 386.00 | 106.00 | -3.73 |
| 499 | 273.00 | 386.00 | 107.00 | -3.73 |
| 500 | 274.00 | 386.00 | 108.00 | -3.73 |
| 501 | 275.00 | 386.00 | 109.00 | -3.73 |
| 502 | 276.00 | 386.00 | 110.00 | -3.73 |
| 503 | 277.00 | 386.00 | 111.00 | -3.73 |
| 504 | 278.00 | 386.00 | 112.00 | -3.73 |
| 505 | 279.00 | 386.00 | 113.00 | -3.73 |
| 506 | 280.00 | 386.00 | 114.00 | -3.73 |
| 507 | 281.00 | 386.00 | 115.00 | -3.73 |
| 508 | 282.00 | 386.00 | 116.00 | -3.73 |
| 509 | 283.00 | 386.00 | 117.00 | -3.73 |
| 510 | 284.00 | 386.00 | 118.00 | -3.73 |
| 511 | 285.00 | 386.00 | 119.00 | -3.73 |
| 512 | 286.00 | 386.00 | 120.00 | -3.73 |
| 513 | 287.00 | 386.00 | 121.00 | -3.73 |
| 514 | 288.00 | 386.00 | 122.00 | -3.73 |
| 515 | 289.00 | 386.00 | 123.00 | -3.73 |
| 516 | 290.00 | 386.00 | 124.00 | -3.73 |
| 517 | 291.00 | 386.00 | 125.00 | -3.73 |
| 518 | 292.00 | 386.00 | 126.00 | -3.73 |
| 519 | 293.00 | 386.00 | 127.00 | -3.73 |
| 520 | 294.00 | 386.00 | 128.00 | -3.73 |
| 521 | 295.00 | 386.00 | 129.00 | -3.73 |
| 522 | 296.00 | 386.00 | 130.00 | -3.73 |
| 523 | 297.00 | 386.00 | 131.00 | -3.73 |
| 524 | 298.00 | 386.00 | 132.00 | -3.73 |
| 525 | 299.00 | 386.00 | 133.00 | -3.73 |
| 526 | 300.00 | 386.00 | 134.00 | -3.73 |
| 527 | 301.00 | 386.00 | 135.00 | -3.73 |
| 528 | 302.00 | 386.00 | 136.00 | -3.73 |
| 529 | 303.00 | 386.00 | 137.00 | -3.73 |
| 530 | 304.00 | 386.00 | 138.00 | -3.73 |
| 531 | 305.00 | 386.00 | 139.00 | -3.73 |
| 532 | 306.00 | 386.00 | 140.00 | -3.73 |
| 533 | 307.00 | 386.00 | 141.00 | -3.73 |
| 534 | 308.00 | 386.00 | 142.00 | -3.73 |
| 535 | 309.00 | 386.00 | 143.00 | -3.73 |
| 536 | 310.00 | 386.00 | 144.00 | -3.73 |
| 537 | 311.00 | 386.00 | 145.00 | -3.73 |
| 538 | 312.00 | 386.00 | 146.00 | -3.73 |
| 539 | 313.00 | 386.00 | 147.00 | -3.73 |
| 540 | 314.00 | 386.00 | 148.00 | -3.73 |
| 541 | 315.00 | 386.00 | 149.00 | -3.73 |
| 542 | 316.00 | 386.00 | 150.00 | -3.73 |
| 543 | 317.00 | 386.00 | 151.00 | -3.73 |
| 544 | 318.00 | 386.00 | 152.00 | -3.73 |
| 545 | 319.00 | 386.00 | 153.00 | -3.73 |
| 546 | 320.00 | 386.00 | 154.00 | -3.73 |
| 547 | 321.00 | 386.00 | 155.00 | -3.73 |
| 548 | 322.00 | 386.00 | 156.00 | -3.73 |
| 549 | 323.00 | 386.00 | 157.00 | -3.73 |
| 550 | 324.00 | 386.00 | 158.00 | -3.73 |
| 551 | 325.00 | 386.00 | 159.00 | -3.73 |
| 552 | 326.00 | 386.00 | 160.00 | -3.73 |
| 553 | 327.00 | 386.00 | 161.00 | -3.73 |
| 554 | 328.00 | 386.00 | 162.00 | -3.73 |
| 555 | 329.00 | 386.00 | 163.00 | -3.73 |
| 556 | 330.00 | 386.00 | 164.00 | -3.73 |
| 557 | 331.00 | 386.00 | 165.00 | -3.73 |
| 558 | 332.00 | 386.00 | 166.00 | -3.73 |

- primeiro índice: 241
- último índice: 558
- quantidade: 318
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![30_geo esq](audit_outputs/75_geo_esq_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![30_geo esq polyfit](audit_outputs/75_geo_esq_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

### Lado: dir

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 1148
- ponto de contato recebido: [499.0, 386.0]
- baseline_y: 386.0
- baseline_ajustada: 389.73
- lado solicitado: dir
- largura da região: 205 px
- altura da gota: 373.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 317.00 | 13.00 | 415.03 | 376.73 | NÃO | fora da faixa vertical |
| 1 | 316.00 | 14.00 | 414.58 | 375.73 | NÃO | fora da faixa vertical |
| 2 | 315.00 | 14.00 | 415.02 | 375.73 | NÃO | fora da faixa vertical |
| 3 | 314.00 | 14.00 | 415.46 | 375.73 | NÃO | fora da faixa vertical |
| 4 | 313.00 | 14.00 | 415.91 | 375.73 | NÃO | fora da faixa vertical |
| 5 | 312.00 | 14.00 | 416.36 | 375.73 | NÃO | fora da faixa vertical |
| 6 | 311.00 | 14.00 | 416.81 | 375.73 | NÃO | fora da faixa vertical |
| 7 | 310.00 | 14.00 | 417.26 | 375.73 | NÃO | fora da faixa vertical |
| 8 | 309.00 | 14.00 | 417.71 | 375.73 | NÃO | fora da faixa vertical |
| 9 | 308.00 | 14.00 | 418.17 | 375.73 | NÃO | fora da faixa vertical |
| 10 | 307.00 | 14.00 | 418.63 | 375.73 | NÃO | fora da faixa vertical |
| 11 | 306.00 | 15.00 | 418.20 | 374.73 | NÃO | fora da faixa vertical |
| 12 | 305.00 | 15.00 | 418.66 | 374.73 | NÃO | fora da faixa vertical |
| 13 | 304.00 | 15.00 | 419.13 | 374.73 | NÃO | fora da faixa vertical |
| 14 | 303.00 | 15.00 | 419.59 | 374.73 | NÃO | fora da faixa vertical |
| 15 | 302.00 | 15.00 | 420.06 | 374.73 | NÃO | fora da faixa vertical |
| 16 | 301.00 | 15.00 | 420.53 | 374.73 | NÃO | fora da faixa vertical |
| 17 | 300.00 | 15.00 | 421.00 | 374.73 | NÃO | fora da faixa vertical |
| 18 | 299.00 | 15.00 | 421.47 | 374.73 | NÃO | fora da faixa vertical |
| 19 | 298.00 | 16.00 | 421.07 | 373.73 | NÃO | fora da faixa vertical |
| 20 | 297.00 | 16.00 | 421.55 | 373.73 | NÃO | fora da faixa vertical |
| 21 | 296.00 | 16.00 | 422.03 | 373.73 | NÃO | fora da faixa vertical |
| 22 | 295.00 | 16.00 | 422.51 | 373.73 | NÃO | fora da faixa vertical |
| 23 | 294.00 | 16.00 | 423.00 | 373.73 | NÃO | fora da faixa vertical |
| 24 | 293.00 | 17.00 | 422.61 | 372.73 | NÃO | fora da faixa vertical |
| 25 | 292.00 | 17.00 | 423.10 | 372.73 | NÃO | fora da faixa vertical |
| 26 | 291.00 | 17.00 | 423.59 | 372.73 | NÃO | fora da faixa vertical |
| 27 | 290.00 | 17.00 | 424.08 | 372.73 | NÃO | fora da faixa vertical |
| 28 | 289.00 | 18.00 | 423.70 | 371.73 | NÃO | fora da faixa vertical |
| 29 | 288.00 | 18.00 | 424.20 | 371.73 | NÃO | fora da faixa vertical |
| 30 | 287.00 | 18.00 | 424.70 | 371.73 | NÃO | fora da faixa vertical |
| 31 | 286.00 | 18.00 | 425.20 | 371.73 | NÃO | fora da faixa vertical |
| 32 | 285.00 | 18.00 | 425.70 | 371.73 | NÃO | fora da faixa vertical |
| 33 | 284.00 | 19.00 | 425.34 | 370.73 | NÃO | fora da faixa vertical |
| 34 | 283.00 | 19.00 | 425.85 | 370.73 | NÃO | fora da faixa vertical |
| 35 | 282.00 | 19.00 | 426.35 | 370.73 | NÃO | fora da faixa vertical |
| 36 | 281.00 | 19.00 | 426.86 | 370.73 | NÃO | fora da faixa vertical |
| 37 | 280.00 | 20.00 | 426.52 | 369.73 | NÃO | fora da faixa vertical |
| 38 | 279.00 | 20.00 | 427.03 | 369.73 | NÃO | fora da faixa vertical |
| 39 | 278.00 | 20.00 | 427.55 | 369.73 | NÃO | fora da faixa vertical |
| 40 | 277.00 | 21.00 | 427.21 | 368.73 | NÃO | fora da faixa vertical |
| 41 | 276.00 | 21.00 | 427.73 | 368.73 | NÃO | fora da faixa vertical |
| 42 | 275.00 | 21.00 | 428.25 | 368.73 | NÃO | fora da faixa vertical |
| 43 | 274.00 | 21.00 | 428.78 | 368.73 | NÃO | fora da faixa vertical |
| 44 | 273.00 | 22.00 | 428.45 | 367.73 | NÃO | fora da faixa vertical |
| 45 | 272.00 | 22.00 | 428.98 | 367.73 | NÃO | fora da faixa vertical |
| 46 | 271.00 | 22.00 | 429.51 | 367.73 | NÃO | fora da faixa vertical |
| 47 | 270.00 | 23.00 | 429.20 | 366.73 | NÃO | fora da faixa vertical |
| 48 | 269.00 | 23.00 | 429.73 | 366.73 | NÃO | fora da faixa vertical |
| 49 | 268.00 | 23.00 | 430.27 | 366.73 | NÃO | fora da faixa vertical |
| 50 | 267.00 | 24.00 | 429.96 | 365.73 | NÃO | fora da faixa vertical |
| 51 | 266.00 | 24.00 | 430.50 | 365.73 | NÃO | fora da faixa vertical |
| 52 | 265.00 | 24.00 | 431.05 | 365.73 | NÃO | fora da faixa vertical |
| 53 | 264.00 | 25.00 | 430.75 | 364.73 | NÃO | fora da faixa vertical |
| 54 | 263.00 | 25.00 | 431.30 | 364.73 | NÃO | fora da faixa vertical |
| 55 | 262.00 | 26.00 | 431.01 | 363.73 | NÃO | fora da faixa vertical |
| 56 | 261.00 | 26.00 | 431.56 | 363.73 | NÃO | fora da faixa vertical |
| 57 | 260.00 | 26.00 | 432.11 | 363.73 | NÃO | fora da faixa vertical |
| 58 | 259.00 | 27.00 | 431.83 | 362.73 | NÃO | fora da faixa vertical |
| 59 | 258.00 | 27.00 | 432.39 | 362.73 | NÃO | fora da faixa vertical |
| 60 | 257.00 | 27.00 | 432.95 | 362.73 | NÃO | fora da faixa vertical |
| 61 | 256.00 | 28.00 | 432.68 | 361.73 | NÃO | fora da faixa vertical |
| 62 | 255.00 | 28.00 | 433.24 | 361.73 | NÃO | fora da faixa vertical |
| 63 | 254.00 | 29.00 | 432.98 | 360.73 | NÃO | fora da faixa vertical |
| 64 | 253.00 | 29.00 | 433.55 | 360.73 | NÃO | fora da faixa vertical |
| 65 | 252.00 | 29.00 | 434.12 | 360.73 | NÃO | fora da faixa vertical |
| 66 | 251.00 | 30.00 | 433.87 | 359.73 | NÃO | fora da faixa vertical |
| 67 | 250.00 | 30.00 | 434.44 | 359.73 | NÃO | fora da faixa vertical |
| 68 | 249.00 | 31.00 | 434.19 | 358.73 | NÃO | fora da faixa vertical |
| 69 | 248.00 | 31.00 | 434.77 | 358.73 | NÃO | fora da faixa vertical |
| 70 | 247.00 | 32.00 | 434.53 | 357.73 | NÃO | fora da faixa vertical |
| 71 | 246.00 | 32.00 | 435.11 | 357.73 | NÃO | fora da faixa vertical |
| 72 | 245.00 | 33.00 | 434.89 | 356.73 | NÃO | fora da faixa vertical |
| 73 | 244.00 | 33.00 | 435.47 | 356.73 | NÃO | fora da faixa vertical |
| 74 | 243.00 | 34.00 | 435.25 | 355.73 | NÃO | fora da faixa vertical |
| 75 | 242.00 | 34.00 | 435.84 | 355.73 | NÃO | fora da faixa vertical |
| 76 | 241.00 | 35.00 | 435.62 | 354.73 | NÃO | fora da faixa vertical |
| 77 | 240.00 | 35.00 | 436.21 | 354.73 | NÃO | fora da faixa vertical |
| 78 | 239.00 | 36.00 | 436.00 | 353.73 | NÃO | fora da faixa vertical |
| 79 | 238.00 | 36.00 | 436.60 | 353.73 | NÃO | fora da faixa vertical |
| 80 | 237.00 | 37.00 | 436.40 | 352.73 | NÃO | fora da faixa vertical |
| 81 | 236.00 | 37.00 | 437.00 | 352.73 | NÃO | fora da faixa vertical |
| 82 | 235.00 | 38.00 | 436.81 | 351.73 | NÃO | fora da faixa vertical |
| 83 | 234.00 | 38.00 | 437.41 | 351.73 | NÃO | fora da faixa vertical |
| 84 | 233.00 | 39.00 | 437.22 | 350.73 | NÃO | fora da faixa vertical |
| 85 | 232.00 | 40.00 | 437.04 | 349.73 | NÃO | fora da faixa vertical |
| 86 | 231.00 | 40.00 | 437.65 | 349.73 | NÃO | fora da faixa vertical |
| 87 | 230.00 | 41.00 | 437.48 | 348.73 | NÃO | fora da faixa vertical |
| 88 | 229.00 | 41.00 | 438.09 | 348.73 | NÃO | fora da faixa vertical |
| 89 | 228.00 | 42.00 | 437.92 | 347.73 | NÃO | fora da faixa vertical |
| 90 | 227.00 | 43.00 | 437.76 | 346.73 | NÃO | fora da faixa vertical |
| 91 | 226.00 | 43.00 | 438.38 | 346.73 | NÃO | fora da faixa vertical |
| 92 | 225.00 | 44.00 | 438.22 | 345.73 | NÃO | fora da faixa vertical |
| 93 | 224.00 | 44.00 | 438.85 | 345.73 | NÃO | fora da faixa vertical |
| 94 | 223.00 | 45.00 | 438.70 | 344.73 | NÃO | fora da faixa vertical |
| 95 | 222.00 | 46.00 | 438.55 | 343.73 | NÃO | fora da faixa vertical |
| 96 | 221.00 | 46.00 | 439.19 | 343.73 | NÃO | fora da faixa vertical |
| 97 | 220.00 | 47.00 | 439.05 | 342.73 | NÃO | fora da faixa vertical |
| 98 | 219.00 | 48.00 | 438.91 | 341.73 | NÃO | fora da faixa vertical |
| 99 | 218.00 | 48.00 | 439.55 | 341.73 | NÃO | fora da faixa vertical |
| 100 | 217.00 | 49.00 | 439.42 | 340.73 | NÃO | fora da faixa vertical |
| 101 | 216.00 | 50.00 | 439.30 | 339.73 | NÃO | fora da faixa vertical |
| 102 | 215.00 | 50.00 | 439.95 | 339.73 | NÃO | fora da faixa vertical |
| 103 | 214.00 | 51.00 | 439.83 | 338.73 | NÃO | fora da faixa vertical |
| 104 | 213.00 | 52.00 | 439.72 | 337.73 | NÃO | fora da faixa vertical |
| 105 | 212.00 | 53.00 | 439.61 | 336.73 | NÃO | fora da faixa vertical |
| 106 | 211.00 | 53.00 | 440.26 | 336.73 | NÃO | fora da faixa vertical |
| 107 | 210.00 | 54.00 | 440.16 | 335.73 | NÃO | fora da faixa vertical |
| 108 | 209.00 | 55.00 | 440.07 | 334.73 | NÃO | fora da faixa vertical |
| 109 | 208.00 | 56.00 | 439.98 | 333.73 | NÃO | fora da faixa vertical |
| 110 | 207.00 | 56.00 | 440.64 | 333.73 | NÃO | fora da faixa vertical |
| 111 | 206.00 | 57.00 | 440.56 | 332.73 | NÃO | fora da faixa vertical |
| 112 | 205.00 | 58.00 | 440.48 | 331.73 | NÃO | fora da faixa vertical |
| 113 | 204.00 | 59.00 | 440.40 | 330.73 | NÃO | fora da faixa vertical |
| 114 | 203.00 | 59.00 | 441.07 | 330.73 | NÃO | fora da faixa vertical |
| 115 | 202.00 | 60.00 | 441.00 | 329.73 | NÃO | fora da faixa vertical |
| 116 | 201.00 | 61.00 | 440.94 | 328.73 | NÃO | fora da faixa vertical |
| 117 | 200.00 | 62.00 | 440.88 | 327.73 | NÃO | fora da faixa vertical |
| 118 | 199.00 | 63.00 | 440.83 | 326.73 | NÃO | fora da faixa vertical |
| 119 | 198.00 | 64.00 | 440.78 | 325.73 | NÃO | fora da faixa vertical |
| 120 | 197.00 | 65.00 | 440.73 | 324.73 | NÃO | fora da faixa vertical |
| 121 | 196.00 | 66.00 | 440.69 | 323.73 | NÃO | fora da faixa vertical |
| 122 | 195.00 | 67.00 | 440.66 | 322.73 | NÃO | fora da faixa vertical |
| 123 | 194.00 | 68.00 | 440.62 | 321.73 | NÃO | fora da faixa vertical |
| 124 | 193.00 | 69.00 | 440.60 | 320.73 | NÃO | fora da faixa vertical |
| 125 | 192.00 | 69.00 | 441.29 | 320.73 | NÃO | fora da faixa vertical |
| 126 | 191.00 | 70.00 | 441.27 | 319.73 | NÃO | fora da faixa vertical |
| 127 | 190.00 | 71.00 | 441.26 | 318.73 | NÃO | fora da faixa vertical |
| 128 | 189.00 | 72.00 | 441.24 | 317.73 | NÃO | fora da faixa vertical |
| 129 | 188.00 | 73.00 | 441.24 | 316.73 | NÃO | fora da faixa vertical |
| 130 | 188.00 | 74.00 | 440.53 | 315.73 | NÃO | fora da faixa vertical |
| 131 | 187.00 | 75.00 | 440.53 | 314.73 | NÃO | fora da faixa vertical |
| 132 | 186.00 | 76.00 | 440.53 | 313.73 | NÃO | fora da faixa vertical |
| 133 | 185.00 | 77.00 | 440.54 | 312.73 | NÃO | fora da faixa vertical |
| 134 | 184.00 | 78.00 | 440.56 | 311.73 | NÃO | fora da faixa vertical |
| 135 | 183.00 | 79.00 | 440.57 | 310.73 | NÃO | fora da faixa vertical |
| 136 | 182.00 | 80.00 | 440.60 | 309.73 | NÃO | fora da faixa vertical |
| 137 | 181.00 | 81.00 | 440.62 | 308.73 | NÃO | fora da faixa vertical |
| 138 | 180.00 | 82.00 | 440.66 | 307.73 | NÃO | fora da faixa vertical |
| 139 | 179.00 | 83.00 | 440.69 | 306.73 | NÃO | fora da faixa vertical |
| 140 | 179.00 | 84.00 | 440.00 | 305.73 | NÃO | fora da faixa vertical |
| 141 | 178.00 | 85.00 | 440.05 | 304.73 | NÃO | fora da faixa vertical |
| 142 | 177.00 | 86.00 | 440.10 | 303.73 | NÃO | fora da faixa vertical |
| 143 | 176.00 | 87.00 | 440.15 | 302.73 | NÃO | fora da faixa vertical |
| 144 | 175.00 | 88.00 | 440.20 | 301.73 | NÃO | fora da faixa vertical |
| 145 | 174.00 | 89.00 | 440.27 | 300.73 | NÃO | fora da faixa vertical |
| 146 | 174.00 | 90.00 | 439.59 | 299.73 | NÃO | fora da faixa vertical |
| 147 | 173.00 | 91.00 | 439.66 | 298.73 | NÃO | fora da faixa vertical |
| 148 | 172.00 | 92.00 | 439.73 | 297.73 | NÃO | fora da faixa vertical |
| 149 | 171.00 | 93.00 | 439.81 | 296.73 | NÃO | fora da faixa vertical |
| 150 | 171.00 | 94.00 | 439.14 | 295.73 | NÃO | fora da faixa vertical |
| 151 | 170.00 | 95.00 | 439.23 | 294.73 | NÃO | fora da faixa vertical |
| 152 | 169.00 | 96.00 | 439.32 | 293.73 | NÃO | fora da faixa vertical |
| 153 | 168.00 | 97.00 | 439.41 | 292.73 | NÃO | fora da faixa vertical |
| 154 | 168.00 | 98.00 | 438.75 | 291.73 | NÃO | fora da faixa vertical |
| 155 | 167.00 | 99.00 | 438.85 | 290.73 | NÃO | fora da faixa vertical |
| 156 | 166.00 | 100.00 | 438.96 | 289.73 | NÃO | fora da faixa vertical |
| 157 | 165.00 | 101.00 | 439.07 | 288.73 | NÃO | fora da faixa vertical |
| 158 | 165.00 | 102.00 | 438.42 | 287.73 | NÃO | fora da faixa vertical |
| 159 | 164.00 | 103.00 | 438.54 | 286.73 | NÃO | fora da faixa vertical |
| 160 | 163.00 | 104.00 | 438.66 | 285.73 | NÃO | fora da faixa vertical |
| 161 | 163.00 | 105.00 | 438.01 | 284.73 | NÃO | fora da faixa vertical |
| 162 | 162.00 | 106.00 | 438.14 | 283.73 | NÃO | fora da faixa vertical |
| 163 | 161.00 | 107.00 | 438.28 | 282.73 | NÃO | fora da faixa vertical |
| 164 | 161.00 | 108.00 | 437.64 | 281.73 | NÃO | fora da faixa vertical |
| 165 | 160.00 | 109.00 | 437.78 | 280.73 | NÃO | fora da faixa vertical |
| 166 | 160.00 | 110.00 | 437.15 | 279.73 | NÃO | fora da faixa vertical |
| 167 | 159.00 | 111.00 | 437.29 | 278.73 | NÃO | fora da faixa vertical |
| 168 | 158.00 | 112.00 | 437.44 | 277.73 | NÃO | fora da faixa vertical |
| 169 | 158.00 | 113.00 | 436.82 | 276.73 | NÃO | fora da faixa vertical |
| 170 | 157.00 | 114.00 | 436.98 | 275.73 | NÃO | fora da faixa vertical |
| 171 | 157.00 | 115.00 | 436.35 | 274.73 | NÃO | fora da faixa vertical |
| 172 | 156.00 | 116.00 | 436.52 | 273.73 | NÃO | fora da faixa vertical |
| 173 | 155.00 | 117.00 | 436.69 | 272.73 | NÃO | fora da faixa vertical |
| 174 | 155.00 | 118.00 | 436.07 | 271.73 | NÃO | fora da faixa vertical |
| 175 | 154.00 | 119.00 | 436.25 | 270.73 | NÃO | fora da faixa vertical |
| 176 | 154.00 | 120.00 | 435.64 | 269.73 | NÃO | fora da faixa vertical |
| 177 | 153.00 | 121.00 | 435.82 | 268.73 | NÃO | fora da faixa vertical |
| 178 | 153.00 | 122.00 | 435.21 | 267.73 | NÃO | fora da faixa vertical |
| 179 | 152.00 | 123.00 | 435.41 | 266.73 | NÃO | fora da faixa vertical |
| 180 | 152.00 | 124.00 | 434.80 | 265.73 | NÃO | fora da faixa vertical |
| 181 | 151.00 | 125.00 | 435.00 | 264.73 | NÃO | fora da faixa vertical |
| 182 | 151.00 | 126.00 | 434.40 | 263.73 | NÃO | fora da faixa vertical |
| 183 | 150.00 | 127.00 | 434.61 | 262.73 | NÃO | fora da faixa vertical |
| 184 | 150.00 | 128.00 | 434.01 | 261.73 | NÃO | fora da faixa vertical |
| 185 | 149.00 | 129.00 | 434.22 | 260.73 | NÃO | fora da faixa vertical |
| 186 | 149.00 | 130.00 | 433.63 | 259.73 | NÃO | fora da faixa vertical |
| 187 | 148.00 | 131.00 | 433.85 | 258.73 | NÃO | fora da faixa vertical |
| 188 | 148.00 | 132.00 | 433.26 | 257.73 | NÃO | fora da faixa vertical |
| 189 | 147.00 | 133.00 | 433.49 | 256.73 | NÃO | fora da faixa vertical |
| 190 | 147.00 | 134.00 | 432.91 | 255.73 | NÃO | fora da faixa vertical |
| 191 | 146.00 | 135.00 | 433.14 | 254.73 | NÃO | fora da faixa vertical |
| 192 | 146.00 | 136.00 | 432.56 | 253.73 | NÃO | fora da faixa vertical |
| 193 | 146.00 | 137.00 | 431.98 | 252.73 | NÃO | fora da faixa vertical |
| 194 | 145.00 | 138.00 | 432.23 | 251.73 | NÃO | fora da faixa vertical |
| 195 | 145.00 | 139.00 | 431.65 | 250.73 | NÃO | fora da faixa vertical |
| 196 | 144.00 | 140.00 | 431.90 | 249.73 | NÃO | fora da faixa vertical |
| 197 | 144.00 | 141.00 | 431.34 | 248.73 | NÃO | fora da faixa vertical |
| 198 | 144.00 | 142.00 | 430.77 | 247.73 | NÃO | fora da faixa vertical |
| 199 | 143.00 | 143.00 | 431.03 | 246.73 | NÃO | fora da faixa vertical |
| 200 | 143.00 | 144.00 | 430.46 | 245.73 | NÃO | fora da faixa vertical |
| 201 | 143.00 | 145.00 | 429.90 | 244.73 | NÃO | fora da faixa vertical |
| 202 | 142.00 | 146.00 | 430.17 | 243.73 | NÃO | fora da faixa vertical |
| 203 | 142.00 | 147.00 | 429.62 | 242.73 | NÃO | fora da faixa vertical |
| 204 | 141.00 | 148.00 | 429.89 | 241.73 | NÃO | fora da faixa vertical |
| 205 | 141.00 | 149.00 | 429.34 | 240.73 | NÃO | fora da faixa vertical |
| 206 | 141.00 | 150.00 | 428.79 | 239.73 | NÃO | fora da faixa vertical |
| 207 | 140.00 | 151.00 | 429.08 | 238.73 | NÃO | fora da faixa vertical |
| 208 | 140.00 | 152.00 | 428.53 | 237.73 | NÃO | fora da faixa vertical |
| 209 | 140.00 | 153.00 | 427.98 | 236.73 | NÃO | fora da faixa vertical |
| 210 | 139.00 | 154.00 | 428.28 | 235.73 | NÃO | fora da faixa vertical |
| 211 | 139.00 | 155.00 | 427.74 | 234.73 | NÃO | fora da faixa vertical |
| 212 | 139.00 | 156.00 | 427.20 | 233.73 | NÃO | fora da faixa vertical |
| 213 | 139.00 | 157.00 | 426.66 | 232.73 | NÃO | fora da faixa vertical |
| 214 | 138.00 | 158.00 | 426.97 | 231.73 | NÃO | fora da faixa vertical |
| 215 | 138.00 | 159.00 | 426.44 | 230.73 | NÃO | fora da faixa vertical |
| 216 | 138.00 | 160.00 | 425.91 | 229.73 | NÃO | fora da faixa vertical |
| 217 | 137.00 | 161.00 | 426.23 | 228.73 | NÃO | fora da faixa vertical |
| 218 | 137.00 | 162.00 | 425.70 | 227.73 | NÃO | fora da faixa vertical |
| 219 | 137.00 | 163.00 | 425.17 | 226.73 | NÃO | fora da faixa vertical |
| 220 | 137.00 | 164.00 | 424.65 | 225.73 | NÃO | fora da faixa vertical |
| 221 | 136.00 | 165.00 | 424.98 | 224.73 | NÃO | fora da faixa vertical |
| 222 | 136.00 | 166.00 | 424.46 | 223.73 | NÃO | fora da faixa vertical |
| 223 | 136.00 | 167.00 | 423.95 | 222.73 | NÃO | fora da faixa vertical |
| 224 | 136.00 | 168.00 | 423.43 | 221.73 | NÃO | fora da faixa vertical |
| 225 | 135.00 | 169.00 | 423.77 | 220.73 | NÃO | fora da faixa vertical |
| 226 | 135.00 | 170.00 | 423.26 | 219.73 | NÃO | fora da faixa vertical |
| 227 | 135.00 | 171.00 | 422.75 | 218.73 | NÃO | fora da faixa vertical |
| 228 | 135.00 | 172.00 | 422.25 | 217.73 | NÃO | fora da faixa vertical |
| 229 | 135.00 | 173.00 | 421.74 | 216.73 | NÃO | fora da faixa vertical |
| 230 | 134.00 | 174.00 | 422.10 | 215.73 | NÃO | fora da faixa vertical |
| 231 | 134.00 | 175.00 | 421.60 | 214.73 | NÃO | fora da faixa vertical |
| 232 | 134.00 | 176.00 | 421.10 | 213.73 | NÃO | fora da faixa vertical |
| 233 | 134.00 | 177.00 | 420.60 | 212.73 | NÃO | fora da faixa vertical |
| 234 | 134.00 | 178.00 | 420.11 | 211.73 | NÃO | fora da faixa vertical |
| 235 | 133.00 | 179.00 | 420.48 | 210.73 | NÃO | fora da faixa vertical |
| 236 | 133.00 | 180.00 | 419.99 | 209.73 | NÃO | fora da faixa vertical |
| 237 | 133.00 | 181.00 | 419.50 | 208.73 | NÃO | fora da faixa vertical |
| 238 | 133.00 | 182.00 | 419.01 | 207.73 | NÃO | fora da faixa vertical |
| 239 | 133.00 | 183.00 | 418.53 | 206.73 | NÃO | fora da faixa vertical |
| 240 | 132.00 | 184.00 | 418.92 | 205.73 | NÃO | fora da faixa vertical |
| 241 | 132.00 | 185.00 | 418.44 | 204.73 | NÃO | fora do lado solicitado |
| 242 | 132.00 | 186.00 | 417.96 | 203.73 | NÃO | fora do lado solicitado |
| 243 | 132.00 | 187.00 | 417.48 | 202.73 | NÃO | fora do lado solicitado |
| 244 | 132.00 | 188.00 | 417.00 | 201.73 | NÃO | fora do lado solicitado |
| 245 | 132.00 | 189.00 | 416.53 | 200.73 | NÃO | fora do lado solicitado |
| 246 | 132.00 | 190.00 | 416.06 | 199.73 | NÃO | fora do lado solicitado |
| 247 | 132.00 | 191.00 | 415.59 | 198.73 | NÃO | fora do lado solicitado |
| 248 | 131.00 | 192.00 | 416.00 | 197.73 | NÃO | fora do lado solicitado |
| 249 | 131.00 | 193.00 | 415.54 | 196.73 | NÃO | fora do lado solicitado |
| 250 | 131.00 | 194.00 | 415.08 | 195.73 | NÃO | fora do lado solicitado |
| 251 | 131.00 | 195.00 | 414.61 | 194.73 | NÃO | fora do lado solicitado |
| 252 | 131.00 | 196.00 | 414.15 | 193.73 | NÃO | fora do lado solicitado |
| 253 | 131.00 | 197.00 | 413.70 | 192.73 | NÃO | fora do lado solicitado |
| 254 | 131.00 | 198.00 | 413.24 | 191.73 | NÃO | fora do lado solicitado |
| 255 | 131.00 | 199.00 | 412.79 | 190.73 | NÃO | fora do lado solicitado |
| 256 | 130.00 | 200.00 | 413.23 | 189.73 | NÃO | fora do lado solicitado |
| 257 | 130.00 | 201.00 | 412.78 | 188.73 | NÃO | fora do lado solicitado |
| 258 | 130.00 | 202.00 | 412.33 | 187.73 | NÃO | fora do lado solicitado |
| 259 | 130.00 | 203.00 | 411.89 | 186.73 | NÃO | fora do lado solicitado |
| 260 | 130.00 | 204.00 | 411.44 | 185.73 | NÃO | fora do lado solicitado |
| 261 | 130.00 | 205.00 | 411.00 | 184.73 | NÃO | fora do lado solicitado |
| 262 | 130.00 | 206.00 | 410.56 | 183.73 | NÃO | fora do lado solicitado |
| 263 | 130.00 | 207.00 | 410.12 | 182.73 | NÃO | fora do lado solicitado |
| 264 | 130.00 | 208.00 | 409.69 | 181.73 | NÃO | fora do lado solicitado |
| 265 | 130.00 | 209.00 | 409.26 | 180.73 | NÃO | fora do lado solicitado |
| 266 | 130.00 | 210.00 | 408.82 | 179.73 | NÃO | fora do lado solicitado |
| 267 | 130.00 | 211.00 | 408.39 | 178.73 | NÃO | fora do lado solicitado |
| 268 | 130.00 | 212.00 | 407.97 | 177.73 | NÃO | fora do lado solicitado |
| 269 | 130.00 | 213.00 | 407.54 | 176.73 | NÃO | fora do lado solicitado |
| 270 | 130.00 | 214.00 | 407.12 | 175.73 | NÃO | fora do lado solicitado |
| 271 | 130.00 | 215.00 | 406.70 | 174.73 | NÃO | fora do lado solicitado |
| 272 | 130.00 | 216.00 | 406.28 | 173.73 | NÃO | fora do lado solicitado |
| 273 | 130.00 | 217.00 | 405.86 | 172.73 | NÃO | fora do lado solicitado |
| 274 | 130.00 | 218.00 | 405.44 | 171.73 | NÃO | fora do lado solicitado |
| 275 | 130.00 | 219.00 | 405.03 | 170.73 | NÃO | fora do lado solicitado |
| 276 | 130.00 | 220.00 | 404.62 | 169.73 | NÃO | fora do lado solicitado |
| 277 | 130.00 | 221.00 | 404.21 | 168.73 | NÃO | fora do lado solicitado |
| 278 | 130.00 | 222.00 | 403.80 | 167.73 | NÃO | fora do lado solicitado |
| 279 | 130.00 | 223.00 | 403.40 | 166.73 | NÃO | fora do lado solicitado |
| 280 | 130.00 | 224.00 | 403.00 | 165.73 | NÃO | fora do lado solicitado |
| 281 | 130.00 | 225.00 | 402.59 | 164.73 | NÃO | fora do lado solicitado |
| 282 | 130.00 | 226.00 | 402.20 | 163.73 | NÃO | fora do lado solicitado |
| 283 | 130.00 | 227.00 | 401.80 | 162.73 | NÃO | fora do lado solicitado |
| 284 | 130.00 | 228.00 | 401.40 | 161.73 | NÃO | fora do lado solicitado |
| 285 | 130.00 | 229.00 | 401.01 | 160.73 | NÃO | fora do lado solicitado |
| 286 | 130.00 | 230.00 | 400.62 | 159.73 | NÃO | fora do lado solicitado |
| 287 | 130.00 | 231.00 | 400.23 | 158.73 | NÃO | fora do lado solicitado |
| 288 | 131.00 | 232.00 | 398.92 | 157.73 | NÃO | fora do lado solicitado |
| 289 | 131.00 | 233.00 | 398.54 | 156.73 | NÃO | fora do lado solicitado |
| 290 | 131.00 | 234.00 | 398.16 | 155.73 | NÃO | fora do lado solicitado |
| 291 | 131.00 | 235.00 | 397.78 | 154.73 | NÃO | fora do lado solicitado |
| 292 | 131.00 | 236.00 | 397.40 | 153.73 | NÃO | fora do lado solicitado |
| 293 | 131.00 | 237.00 | 397.02 | 152.73 | NÃO | fora do lado solicitado |
| 294 | 131.00 | 238.00 | 396.65 | 151.73 | NÃO | fora do lado solicitado |
| 295 | 131.00 | 239.00 | 396.27 | 150.73 | NÃO | fora do lado solicitado |
| 296 | 131.00 | 240.00 | 395.90 | 149.73 | NÃO | fora do lado solicitado |
| 297 | 132.00 | 241.00 | 394.61 | 148.73 | NÃO | fora do lado solicitado |
| 298 | 132.00 | 242.00 | 394.24 | 147.73 | NÃO | fora do lado solicitado |
| 299 | 132.00 | 243.00 | 393.88 | 146.73 | NÃO | fora do lado solicitado |
| 300 | 132.00 | 244.00 | 393.51 | 145.73 | NÃO | fora do lado solicitado |
| 301 | 132.00 | 245.00 | 393.15 | 144.73 | NÃO | fora do lado solicitado |
| 302 | 132.00 | 246.00 | 392.80 | 143.73 | NÃO | fora do lado solicitado |
| 303 | 132.00 | 247.00 | 392.44 | 142.73 | NÃO | fora do lado solicitado |
| 304 | 133.00 | 248.00 | 391.15 | 141.73 | NÃO | fora do lado solicitado |
| 305 | 133.00 | 249.00 | 390.80 | 140.73 | NÃO | fora do lado solicitado |
| 306 | 133.00 | 250.00 | 390.45 | 139.73 | NÃO | fora do lado solicitado |
| 307 | 133.00 | 251.00 | 390.10 | 138.73 | NÃO | fora do lado solicitado |
| 308 | 133.00 | 252.00 | 389.76 | 137.73 | NÃO | fora do lado solicitado |
| 309 | 134.00 | 253.00 | 388.48 | 136.73 | NÃO | fora do lado solicitado |
| 310 | 134.00 | 254.00 | 388.14 | 135.73 | NÃO | fora do lado solicitado |
| 311 | 134.00 | 255.00 | 387.80 | 134.73 | NÃO | fora do lado solicitado |
| 312 | 134.00 | 256.00 | 387.46 | 133.73 | NÃO | fora do lado solicitado |
| 313 | 134.00 | 257.00 | 387.13 | 132.73 | NÃO | fora do lado solicitado |
| 314 | 135.00 | 258.00 | 385.85 | 131.73 | NÃO | fora do lado solicitado |
| 315 | 135.00 | 259.00 | 385.52 | 130.73 | NÃO | fora do lado solicitado |
| 316 | 135.00 | 260.00 | 385.19 | 129.73 | NÃO | fora do lado solicitado |
| 317 | 135.00 | 261.00 | 384.86 | 128.73 | NÃO | fora do lado solicitado |
| 318 | 135.00 | 262.00 | 384.54 | 127.73 | NÃO | fora do lado solicitado |
| 319 | 136.00 | 263.00 | 383.27 | 126.73 | NÃO | fora do lado solicitado |
| 320 | 136.00 | 264.00 | 382.95 | 125.73 | NÃO | fora do lado solicitado |
| 321 | 136.00 | 265.00 | 382.64 | 124.73 | NÃO | fora do lado solicitado |
| 322 | 136.00 | 266.00 | 382.32 | 123.73 | NÃO | fora do lado solicitado |
| 323 | 137.00 | 267.00 | 381.06 | 122.73 | NÃO | fora do lado solicitado |
| 324 | 137.00 | 268.00 | 380.75 | 121.73 | NÃO | fora do lado solicitado |
| 325 | 137.00 | 269.00 | 380.44 | 120.73 | NÃO | fora do lado solicitado |
| 326 | 137.00 | 270.00 | 380.13 | 119.73 | NÃO | fora do lado solicitado |
| 327 | 138.00 | 271.00 | 378.87 | 118.73 | NÃO | fora do lado solicitado |
| 328 | 138.00 | 272.00 | 378.57 | 117.73 | NÃO | fora do lado solicitado |
| 329 | 138.00 | 273.00 | 378.27 | 116.73 | NÃO | fora do lado solicitado |
| 330 | 139.00 | 274.00 | 377.02 | 115.73 | NÃO | fora do lado solicitado |
| 331 | 139.00 | 275.00 | 376.72 | 114.73 | NÃO | fora do lado solicitado |
| 332 | 139.00 | 276.00 | 376.43 | 113.73 | NÃO | fora do lado solicitado |
| 333 | 139.00 | 277.00 | 376.14 | 112.73 | NÃO | fora do lado solicitado |
| 334 | 140.00 | 278.00 | 374.89 | 111.73 | NÃO | fora do lado solicitado |
| 335 | 140.00 | 279.00 | 374.61 | 110.73 | NÃO | fora do lado solicitado |
| 336 | 140.00 | 280.00 | 374.32 | 109.73 | NÃO | fora do lado solicitado |
| 337 | 141.00 | 281.00 | 373.08 | 108.73 | NÃO | fora do lado solicitado |
| 338 | 141.00 | 282.00 | 372.80 | 107.73 | NÃO | fora do lado solicitado |
| 339 | 141.00 | 283.00 | 372.52 | 106.73 | NÃO | fora do lado solicitado |
| 340 | 142.00 | 284.00 | 371.29 | 105.73 | NÃO | fora do lado solicitado |
| 341 | 142.00 | 285.00 | 371.01 | 104.73 | NÃO | fora do lado solicitado |
| 342 | 142.00 | 286.00 | 370.74 | 103.73 | NÃO | fora do lado solicitado |
| 343 | 143.00 | 287.00 | 369.51 | 102.73 | NÃO | fora do lado solicitado |
| 344 | 143.00 | 288.00 | 369.24 | 101.73 | NÃO | fora do lado solicitado |
| 345 | 144.00 | 289.00 | 368.01 | 100.73 | NÃO | fora do lado solicitado |
| 346 | 144.00 | 290.00 | 367.75 | 99.73 | NÃO | fora do lado solicitado |
| 347 | 144.00 | 291.00 | 367.49 | 98.73 | NÃO | fora do lado solicitado |
| 348 | 145.00 | 292.00 | 366.27 | 97.73 | NÃO | fora do lado solicitado |
| 349 | 145.00 | 293.00 | 366.01 | 96.73 | NÃO | fora do lado solicitado |
| 350 | 145.00 | 294.00 | 365.76 | 95.73 | NÃO | fora do lado solicitado |
| 351 | 146.00 | 295.00 | 364.54 | 94.73 | NÃO | fora do lado solicitado |
| 352 | 146.00 | 296.00 | 364.29 | 93.73 | NÃO | fora do lado solicitado |
| 353 | 147.00 | 297.00 | 363.08 | 92.73 | NÃO | fora do lado solicitado |
| 354 | 147.00 | 298.00 | 362.83 | 91.73 | NÃO | fora do lado solicitado |
| 355 | 148.00 | 299.00 | 361.62 | 90.73 | NÃO | fora do lado solicitado |
| 356 | 148.00 | 300.00 | 361.38 | 89.73 | NÃO | fora do lado solicitado |
| 357 | 149.00 | 301.00 | 360.17 | 88.73 | NÃO | fora do lado solicitado |
| 358 | 149.00 | 302.00 | 359.94 | 87.73 | NÃO | fora do lado solicitado |
| 359 | 150.00 | 303.00 | 358.73 | 86.73 | NÃO | fora do lado solicitado |
| 360 | 150.00 | 304.00 | 358.50 | 85.73 | NÃO | fora do lado solicitado |
| 361 | 151.00 | 305.00 | 357.30 | 84.73 | NÃO | fora do lado solicitado |
| 362 | 151.00 | 306.00 | 357.08 | 83.73 | NÃO | fora do lado solicitado |
| 363 | 152.00 | 307.00 | 355.88 | 82.73 | NÃO | fora do lado solicitado |
| 364 | 152.00 | 308.00 | 355.66 | 81.73 | NÃO | fora do lado solicitado |
| 365 | 153.00 | 309.00 | 354.46 | 80.73 | NÃO | fora do lado solicitado |
| 366 | 153.00 | 310.00 | 354.25 | 79.73 | NÃO | fora do lado solicitado |
| 367 | 154.00 | 311.00 | 353.06 | 78.73 | NÃO | fora do lado solicitado |
| 368 | 154.00 | 312.00 | 352.85 | 77.73 | NÃO | fora do lado solicitado |
| 369 | 155.00 | 313.00 | 351.66 | 76.73 | NÃO | fora do lado solicitado |
| 370 | 155.00 | 314.00 | 351.45 | 75.73 | NÃO | fora do lado solicitado |
| 371 | 156.00 | 315.00 | 350.27 | 74.73 | NÃO | fora do lado solicitado |
| 372 | 157.00 | 316.00 | 349.09 | 73.73 | NÃO | fora do lado solicitado |
| 373 | 157.00 | 317.00 | 348.89 | 72.73 | NÃO | fora do lado solicitado |
| 374 | 158.00 | 318.00 | 347.71 | 71.73 | NÃO | fora do lado solicitado |
| 375 | 158.00 | 319.00 | 347.52 | 70.73 | NÃO | fora do lado solicitado |
| 376 | 159.00 | 320.00 | 346.35 | 69.73 | NÃO | fora do lado solicitado |
| 377 | 160.00 | 321.00 | 345.18 | 68.73 | NÃO | fora do lado solicitado |
| 378 | 160.00 | 322.00 | 344.99 | 67.73 | NÃO | fora do lado solicitado |
| 379 | 161.00 | 323.00 | 343.82 | 66.73 | NÃO | fora do lado solicitado |
| 380 | 161.00 | 324.00 | 343.64 | 65.73 | NÃO | fora do lado solicitado |
| 381 | 162.00 | 325.00 | 342.48 | 64.73 | NÃO | fora do lado solicitado |
| 382 | 163.00 | 326.00 | 341.32 | 63.73 | NÃO | fora do lado solicitado |
| 383 | 163.00 | 327.00 | 341.14 | 62.73 | NÃO | fora do lado solicitado |
| 384 | 164.00 | 328.00 | 339.98 | 61.73 | NÃO | fora do lado solicitado |
| 385 | 165.00 | 329.00 | 338.83 | 60.73 | NÃO | fora do lado solicitado |
| 386 | 165.00 | 330.00 | 338.66 | 59.73 | NÃO | fora do lado solicitado |
| 387 | 166.00 | 331.00 | 337.51 | 58.73 | NÃO | fora do lado solicitado |
| 388 | 167.00 | 332.00 | 336.36 | 57.73 | NÃO | fora do lado solicitado |
| 389 | 167.00 | 333.00 | 336.20 | 56.73 | NÃO | fora do lado solicitado |
| 390 | 168.00 | 334.00 | 335.06 | 55.73 | NÃO | fora do lado solicitado |
| 391 | 169.00 | 335.00 | 333.92 | 54.73 | NÃO | fora do lado solicitado |
| 392 | 170.00 | 336.00 | 332.78 | 53.73 | NÃO | fora do lado solicitado |
| 393 | 170.00 | 337.00 | 332.63 | 52.73 | NÃO | fora do lado solicitado |
| 394 | 171.00 | 338.00 | 331.49 | 51.73 | NÃO | fora do lado solicitado |
| 395 | 172.00 | 339.00 | 330.36 | 50.73 | NÃO | fora do lado solicitado |
| 396 | 173.00 | 340.00 | 329.23 | 49.73 | NÃO | fora do lado solicitado |
| 397 | 173.00 | 341.00 | 329.09 | 48.73 | NÃO | fora do lado solicitado |
| 398 | 174.00 | 342.00 | 327.96 | 47.73 | NÃO | fora do lado solicitado |
| 399 | 175.00 | 343.00 | 326.84 | 46.73 | NÃO | fora do lado solicitado |
| 400 | 176.00 | 344.00 | 325.72 | 45.73 | NÃO | fora do lado solicitado |
| 401 | 177.00 | 345.00 | 324.60 | 44.73 | NÃO | fora do lado solicitado |
| 402 | 177.00 | 346.00 | 324.47 | 43.73 | NÃO | fora do lado solicitado |
| 403 | 178.00 | 347.00 | 323.36 | 42.73 | NÃO | fora do lado solicitado |
| 404 | 179.00 | 348.00 | 322.25 | 41.73 | NÃO | fora do lado solicitado |
| 405 | 180.00 | 349.00 | 321.14 | 40.73 | NÃO | fora do lado solicitado |
| 406 | 181.00 | 350.00 | 320.03 | 39.73 | NÃO | fora do lado solicitado |
| 407 | 182.00 | 351.00 | 318.93 | 38.73 | NÃO | fora do lado solicitado |
| 408 | 183.00 | 352.00 | 317.82 | 37.73 | NÃO | fora do lado solicitado |
| 409 | 184.00 | 353.00 | 316.72 | 36.73 | NÃO | fora do lado solicitado |
| 410 | 185.00 | 354.00 | 315.63 | 35.73 | NÃO | fora do lado solicitado |
| 411 | 186.00 | 355.00 | 314.53 | 34.73 | NÃO | fora do lado solicitado |
| 412 | 186.00 | 356.00 | 314.43 | 33.73 | NÃO | fora do lado solicitado |
| 413 | 187.00 | 357.00 | 313.34 | 32.73 | NÃO | fora do lado solicitado |
| 414 | 188.00 | 358.00 | 312.26 | 31.73 | NÃO | fora do lado solicitado |
| 415 | 189.00 | 359.00 | 311.17 | 30.73 | NÃO | fora do lado solicitado |
| 416 | 190.00 | 360.00 | 310.09 | 29.73 | NÃO | fora do lado solicitado |
| 417 | 191.00 | 361.00 | 309.01 | 28.73 | NÃO | fora do lado solicitado |
| 418 | 192.00 | 361.00 | 308.02 | 28.73 | NÃO | fora do lado solicitado |
| 419 | 193.00 | 362.00 | 306.94 | 27.73 | NÃO | fora do lado solicitado |
| 420 | 194.00 | 363.00 | 305.87 | 26.73 | NÃO | fora do lado solicitado |
| 421 | 195.00 | 364.00 | 304.80 | 25.73 | NÃO | fora do lado solicitado |
| 422 | 196.00 | 365.00 | 303.73 | 24.73 | NÃO | fora do lado solicitado |
| 423 | 197.00 | 366.00 | 302.66 | 23.73 | NÃO | fora do lado solicitado |
| 424 | 198.00 | 367.00 | 301.60 | 22.73 | NÃO | fora do lado solicitado |
| 425 | 199.00 | 368.00 | 300.54 | 21.73 | NÃO | fora do lado solicitado |
| 426 | 200.00 | 369.00 | 299.48 | 20.73 | NÃO | fora do lado solicitado |
| 427 | 201.00 | 370.00 | 298.43 | 19.73 | NÃO | fora do lado solicitado |
| 428 | 202.00 | 371.00 | 297.38 | 18.73 | NÃO | fora do lado solicitado |
| 429 | 203.00 | 372.00 | 296.33 | 17.73 | NÃO | fora do lado solicitado |
| 430 | 204.00 | 372.00 | 295.33 | 17.73 | NÃO | fora do lado solicitado |
| 431 | 205.00 | 373.00 | 294.29 | 16.73 | NÃO | fora do lado solicitado |
| 432 | 206.00 | 374.00 | 293.25 | 15.73 | NÃO | fora do lado solicitado |
| 433 | 207.00 | 375.00 | 292.21 | 14.73 | NÃO | fora do lado solicitado |
| 434 | 208.00 | 375.00 | 291.21 | 14.73 | NÃO | fora do lado solicitado |
| 435 | 209.00 | 376.00 | 290.17 | 13.73 | NÃO | fora do lado solicitado |
| 436 | 210.00 | 377.00 | 289.14 | 12.73 | NÃO | fora do lado solicitado |
| 437 | 211.00 | 378.00 | 288.11 | 11.73 | NÃO | fora do lado solicitado |
| 438 | 212.00 | 378.00 | 287.11 | 11.73 | NÃO | fora do lado solicitado |
| 439 | 213.00 | 379.00 | 286.09 | 10.73 | NÃO | fora do lado solicitado |
| 440 | 214.00 | 380.00 | 285.06 | 9.73 | NÃO | fora do lado solicitado |
| 441 | 215.00 | 381.00 | 284.04 | 8.73 | NÃO | fora do lado solicitado |
| 442 | 216.00 | 381.00 | 283.04 | 8.73 | NÃO | fora do lado solicitado |
| 443 | 217.00 | 382.00 | 282.03 | 7.73 | NÃO | fora do lado solicitado |
| 444 | 218.00 | 383.00 | 281.02 | 6.73 | NÃO | fora do lado solicitado |
| 445 | 219.00 | 384.00 | 280.01 | 5.73 | NÃO | fora do lado solicitado |
| 446 | 220.00 | 384.00 | 279.01 | 5.73 | NÃO | fora do lado solicitado |
| 447 | 221.00 | 385.00 | 278.00 | 4.73 | NÃO | fora do lado solicitado |
| 448 | 222.00 | 386.00 | 277.00 | 3.73 | NÃO | fora do lado solicitado |
| 449 | 223.00 | 386.00 | 276.00 | 3.73 | NÃO | fora do lado solicitado |
| 450 | 224.00 | 386.00 | 275.00 | 3.73 | NÃO | fora do lado solicitado |
| 451 | 225.00 | 386.00 | 274.00 | 3.73 | NÃO | fora do lado solicitado |
| 452 | 226.00 | 386.00 | 273.00 | 3.73 | NÃO | fora do lado solicitado |
| 453 | 227.00 | 386.00 | 272.00 | 3.73 | NÃO | fora do lado solicitado |
| 454 | 228.00 | 386.00 | 271.00 | 3.73 | NÃO | fora do lado solicitado |
| 455 | 229.00 | 386.00 | 270.00 | 3.73 | NÃO | fora do lado solicitado |
| 456 | 230.00 | 386.00 | 269.00 | 3.73 | NÃO | fora do lado solicitado |
| 457 | 231.00 | 386.00 | 268.00 | 3.73 | NÃO | fora do lado solicitado |
| 458 | 232.00 | 386.00 | 267.00 | 3.73 | NÃO | fora do lado solicitado |
| 459 | 233.00 | 386.00 | 266.00 | 3.73 | NÃO | fora do lado solicitado |
| 460 | 234.00 | 386.00 | 265.00 | 3.73 | NÃO | fora do lado solicitado |
| 461 | 235.00 | 386.00 | 264.00 | 3.73 | NÃO | fora do lado solicitado |
| 462 | 236.00 | 386.00 | 263.00 | 3.73 | NÃO | fora do lado solicitado |
| 463 | 237.00 | 386.00 | 262.00 | 3.73 | NÃO | fora do lado solicitado |
| 464 | 238.00 | 386.00 | 261.00 | 3.73 | NÃO | fora do lado solicitado |
| 465 | 239.00 | 386.00 | 260.00 | 3.73 | NÃO | fora do lado solicitado |
| 466 | 240.00 | 386.00 | 259.00 | 3.73 | NÃO | fora do lado solicitado |
| 467 | 241.00 | 386.00 | 258.00 | 3.73 | NÃO | fora do lado solicitado |
| 468 | 242.00 | 386.00 | 257.00 | 3.73 | NÃO | fora do lado solicitado |
| 469 | 243.00 | 386.00 | 256.00 | 3.73 | NÃO | fora do lado solicitado |
| 470 | 244.00 | 386.00 | 255.00 | 3.73 | NÃO | fora do lado solicitado |
| 471 | 245.00 | 386.00 | 254.00 | 3.73 | NÃO | fora do lado solicitado |
| 472 | 246.00 | 386.00 | 253.00 | 3.73 | NÃO | fora do lado solicitado |
| 473 | 247.00 | 386.00 | 252.00 | 3.73 | NÃO | fora do lado solicitado |
| 474 | 248.00 | 386.00 | 251.00 | 3.73 | NÃO | fora do lado solicitado |
| 475 | 249.00 | 386.00 | 250.00 | 3.73 | NÃO | fora do lado solicitado |
| 476 | 250.00 | 386.00 | 249.00 | 3.73 | NÃO | fora do lado solicitado |
| 477 | 251.00 | 386.00 | 248.00 | 3.73 | NÃO | fora do lado solicitado |
| 478 | 252.00 | 386.00 | 247.00 | 3.73 | NÃO | fora do lado solicitado |
| 479 | 253.00 | 386.00 | 246.00 | 3.73 | NÃO | fora do lado solicitado |
| 480 | 254.00 | 386.00 | 245.00 | 3.73 | NÃO | fora do lado solicitado |
| 481 | 255.00 | 386.00 | 244.00 | 3.73 | NÃO | fora do lado solicitado |
| 482 | 256.00 | 386.00 | 243.00 | 3.73 | NÃO | fora do lado solicitado |
| 483 | 257.00 | 386.00 | 242.00 | 3.73 | NÃO | fora do lado solicitado |
| 484 | 258.00 | 386.00 | 241.00 | 3.73 | NÃO | fora do lado solicitado |
| 485 | 259.00 | 386.00 | 240.00 | 3.73 | NÃO | fora do lado solicitado |
| 486 | 260.00 | 386.00 | 239.00 | 3.73 | NÃO | fora do lado solicitado |
| 487 | 261.00 | 386.00 | 238.00 | 3.73 | NÃO | fora do lado solicitado |
| 488 | 262.00 | 386.00 | 237.00 | 3.73 | NÃO | fora do lado solicitado |
| 489 | 263.00 | 386.00 | 236.00 | 3.73 | NÃO | fora do lado solicitado |
| 490 | 264.00 | 386.00 | 235.00 | 3.73 | NÃO | fora do lado solicitado |
| 491 | 265.00 | 386.00 | 234.00 | 3.73 | NÃO | fora do lado solicitado |
| 492 | 266.00 | 386.00 | 233.00 | 3.73 | NÃO | fora do lado solicitado |
| 493 | 267.00 | 386.00 | 232.00 | 3.73 | NÃO | fora do lado solicitado |
| 494 | 268.00 | 386.00 | 231.00 | 3.73 | NÃO | fora do lado solicitado |
| 495 | 269.00 | 386.00 | 230.00 | 3.73 | NÃO | fora do lado solicitado |
| 496 | 270.00 | 386.00 | 229.00 | 3.73 | NÃO | fora do lado solicitado |
| 497 | 271.00 | 386.00 | 228.00 | 3.73 | NÃO | fora do lado solicitado |
| 498 | 272.00 | 386.00 | 227.00 | 3.73 | NÃO | fora do lado solicitado |
| 499 | 273.00 | 386.00 | 226.00 | 3.73 | NÃO | fora do lado solicitado |
| 500 | 274.00 | 386.00 | 225.00 | 3.73 | NÃO | fora do lado solicitado |
| 501 | 275.00 | 386.00 | 224.00 | 3.73 | NÃO | fora do lado solicitado |
| 502 | 276.00 | 386.00 | 223.00 | 3.73 | NÃO | fora do lado solicitado |
| 503 | 277.00 | 386.00 | 222.00 | 3.73 | NÃO | fora do lado solicitado |
| 504 | 278.00 | 386.00 | 221.00 | 3.73 | NÃO | fora do lado solicitado |
| 505 | 279.00 | 386.00 | 220.00 | 3.73 | NÃO | fora do lado solicitado |
| 506 | 280.00 | 386.00 | 219.00 | 3.73 | NÃO | fora do lado solicitado |
| 507 | 281.00 | 386.00 | 218.00 | 3.73 | NÃO | fora do lado solicitado |
| 508 | 282.00 | 386.00 | 217.00 | 3.73 | NÃO | fora do lado solicitado |
| 509 | 283.00 | 386.00 | 216.00 | 3.73 | NÃO | fora do lado solicitado |
| 510 | 284.00 | 386.00 | 215.00 | 3.73 | NÃO | fora do lado solicitado |
| 511 | 285.00 | 386.00 | 214.00 | 3.73 | NÃO | fora do lado solicitado |
| 512 | 286.00 | 386.00 | 213.00 | 3.73 | NÃO | fora do lado solicitado |
| 513 | 287.00 | 386.00 | 212.00 | 3.73 | NÃO | fora do lado solicitado |
| 514 | 288.00 | 386.00 | 211.00 | 3.73 | NÃO | fora do lado solicitado |
| 515 | 289.00 | 386.00 | 210.00 | 3.73 | NÃO | fora do lado solicitado |
| 516 | 290.00 | 386.00 | 209.00 | 3.73 | NÃO | fora do lado solicitado |
| 517 | 291.00 | 386.00 | 208.00 | 3.73 | NÃO | fora do lado solicitado |
| 518 | 292.00 | 386.00 | 207.00 | 3.73 | NÃO | fora do lado solicitado |
| 519 | 293.00 | 386.00 | 206.00 | 3.73 | NÃO | fora do lado solicitado |
| 520 | 294.00 | 386.00 | 205.00 | 3.73 | NÃO | fora do lado solicitado |
| 521 | 295.00 | 386.00 | 204.00 | 3.73 | NÃO | fora do lado solicitado |
| 522 | 296.00 | 386.00 | 203.00 | 3.73 | NÃO | fora do lado solicitado |
| 523 | 297.00 | 386.00 | 202.00 | 3.73 | NÃO | fora do lado solicitado |
| 524 | 298.00 | 386.00 | 201.00 | 3.73 | NÃO | fora do lado solicitado |
| 525 | 299.00 | 386.00 | 200.00 | 3.73 | NÃO | fora do lado solicitado |
| 526 | 300.00 | 386.00 | 199.00 | 3.73 | NÃO | fora do lado solicitado |
| 527 | 301.00 | 386.00 | 198.00 | 3.73 | NÃO | fora do lado solicitado |
| 528 | 302.00 | 386.00 | 197.00 | 3.73 | NÃO | fora do lado solicitado |
| 529 | 303.00 | 386.00 | 196.00 | 3.73 | NÃO | fora do lado solicitado |
| 530 | 304.00 | 386.00 | 195.00 | 3.73 | NÃO | fora do lado solicitado |
| 531 | 305.00 | 386.00 | 194.00 | 3.73 | NÃO | fora do lado solicitado |
| 532 | 306.00 | 386.00 | 193.00 | 3.73 | NÃO | fora do lado solicitado |
| 533 | 307.00 | 386.00 | 192.00 | 3.73 | NÃO | fora do lado solicitado |
| 534 | 308.00 | 386.00 | 191.00 | 3.73 | NÃO | fora do lado solicitado |
| 535 | 309.00 | 386.00 | 190.00 | 3.73 | NÃO | fora do lado solicitado |
| 536 | 310.00 | 386.00 | 189.00 | 3.73 | NÃO | fora do lado solicitado |
| 537 | 311.00 | 386.00 | 188.00 | 3.73 | NÃO | fora do lado solicitado |
| 538 | 312.00 | 386.00 | 187.00 | 3.73 | NÃO | fora do lado solicitado |
| 539 | 313.00 | 386.00 | 186.00 | 3.73 | NÃO | fora do lado solicitado |
| 540 | 314.00 | 386.00 | 185.00 | 3.73 | NÃO | fora do lado solicitado |
| 541 | 315.00 | 386.00 | 184.00 | 3.73 | NÃO | fora do lado solicitado |
| 542 | 316.00 | 386.00 | 183.00 | 3.73 | NÃO | fora do lado solicitado |
| 543 | 317.00 | 386.00 | 182.00 | 3.73 | NÃO | fora do lado solicitado |
| 544 | 318.00 | 386.00 | 181.00 | 3.73 | NÃO | fora do lado solicitado |
| 545 | 319.00 | 386.00 | 180.00 | 3.73 | NÃO | fora do lado solicitado |
| 546 | 320.00 | 386.00 | 179.00 | 3.73 | NÃO | fora do lado solicitado |
| 547 | 321.00 | 386.00 | 178.00 | 3.73 | NÃO | fora do lado solicitado |
| 548 | 322.00 | 386.00 | 177.00 | 3.73 | NÃO | fora do lado solicitado |
| 549 | 323.00 | 386.00 | 176.00 | 3.73 | NÃO | fora do lado solicitado |
| 550 | 324.00 | 386.00 | 175.00 | 3.73 | NÃO | fora do lado solicitado |
| 551 | 325.00 | 386.00 | 174.00 | 3.73 | NÃO | fora do lado solicitado |
| 552 | 326.00 | 386.00 | 173.00 | 3.73 | NÃO | fora do lado solicitado |
| 553 | 327.00 | 386.00 | 172.00 | 3.73 | NÃO | fora do lado solicitado |
| 554 | 328.00 | 386.00 | 171.00 | 3.73 | NÃO | fora do lado solicitado |
| 555 | 329.00 | 386.00 | 170.00 | 3.73 | NÃO | fora do lado solicitado |
| 556 | 330.00 | 386.00 | 169.00 | 3.73 | NÃO | fora do lado solicitado |
| 557 | 331.00 | 386.00 | 168.00 | 3.73 | NÃO | fora do lado solicitado |
| 558 | 332.00 | 386.00 | 167.00 | 3.73 | NÃO | fora do lado solicitado |
| 559 | 333.00 | 386.00 | 166.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 560 | 334.00 | 386.00 | 165.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 561 | 335.00 | 386.00 | 164.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 562 | 336.00 | 386.00 | 163.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 563 | 337.00 | 386.00 | 162.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 564 | 338.00 | 386.00 | 161.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 565 | 339.00 | 386.00 | 160.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 566 | 340.00 | 386.00 | 159.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 567 | 341.00 | 386.00 | 158.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 568 | 342.00 | 386.00 | 157.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 569 | 343.00 | 386.00 | 156.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 570 | 344.00 | 386.00 | 155.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 571 | 345.00 | 386.00 | 154.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 572 | 346.00 | 386.00 | 153.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 573 | 347.00 | 386.00 | 152.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 574 | 348.00 | 386.00 | 151.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 575 | 349.00 | 386.00 | 150.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 576 | 350.00 | 386.00 | 149.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 577 | 351.00 | 386.00 | 148.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 578 | 352.00 | 386.00 | 147.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 579 | 353.00 | 386.00 | 146.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 580 | 354.00 | 386.00 | 145.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 581 | 355.00 | 386.00 | 144.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 582 | 356.00 | 386.00 | 143.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 583 | 357.00 | 386.00 | 142.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 584 | 358.00 | 386.00 | 141.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 585 | 359.00 | 386.00 | 140.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 586 | 360.00 | 386.00 | 139.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 587 | 361.00 | 386.00 | 138.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 588 | 362.00 | 386.00 | 137.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 589 | 363.00 | 386.00 | 136.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 590 | 364.00 | 386.00 | 135.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 591 | 365.00 | 386.00 | 134.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 592 | 366.00 | 386.00 | 133.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 593 | 367.00 | 386.00 | 132.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 594 | 368.00 | 386.00 | 131.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 595 | 369.00 | 386.00 | 130.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 596 | 370.00 | 386.00 | 129.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 597 | 371.00 | 386.00 | 128.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 598 | 372.00 | 386.00 | 127.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 599 | 373.00 | 386.00 | 126.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 600 | 374.00 | 386.00 | 125.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 601 | 375.00 | 386.00 | 124.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 602 | 376.00 | 386.00 | 123.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 603 | 377.00 | 386.00 | 122.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 604 | 378.00 | 386.00 | 121.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 605 | 379.00 | 386.00 | 120.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 606 | 380.00 | 386.00 | 119.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 607 | 381.00 | 386.00 | 118.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 608 | 382.00 | 386.00 | 117.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 609 | 383.00 | 386.00 | 116.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 610 | 384.00 | 386.00 | 115.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 611 | 385.00 | 386.00 | 114.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 612 | 386.00 | 386.00 | 113.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 613 | 387.00 | 386.00 | 112.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 614 | 388.00 | 386.00 | 111.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 615 | 389.00 | 386.00 | 110.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 616 | 390.00 | 386.00 | 109.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 617 | 391.00 | 386.00 | 108.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 618 | 392.00 | 386.00 | 107.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 619 | 393.00 | 386.00 | 106.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 620 | 394.00 | 386.00 | 105.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 621 | 395.00 | 386.00 | 104.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 622 | 396.00 | 386.00 | 103.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 623 | 397.00 | 386.00 | 102.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 624 | 398.00 | 386.00 | 101.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 625 | 399.00 | 386.00 | 100.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 626 | 400.00 | 386.00 | 99.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 627 | 401.00 | 386.00 | 98.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 628 | 402.00 | 386.00 | 97.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 629 | 403.00 | 386.00 | 96.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 630 | 404.00 | 386.00 | 95.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 631 | 405.00 | 386.00 | 94.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 632 | 406.00 | 386.00 | 93.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 633 | 407.00 | 386.00 | 92.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 634 | 408.00 | 386.00 | 91.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 635 | 409.00 | 386.00 | 90.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 636 | 410.00 | 386.00 | 89.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 637 | 411.00 | 386.00 | 88.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 638 | 412.00 | 386.00 | 87.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 639 | 413.00 | 386.00 | 86.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 640 | 414.00 | 386.00 | 85.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 641 | 415.00 | 386.00 | 84.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 642 | 416.00 | 386.00 | 83.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 643 | 417.00 | 386.00 | 82.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 644 | 418.00 | 386.00 | 81.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 645 | 419.00 | 386.00 | 80.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 646 | 420.00 | 386.00 | 79.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 647 | 421.00 | 386.00 | 78.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 648 | 422.00 | 386.00 | 77.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 649 | 423.00 | 386.00 | 76.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 650 | 424.00 | 386.00 | 75.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 651 | 425.00 | 386.00 | 74.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 652 | 426.00 | 386.00 | 73.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 653 | 427.00 | 386.00 | 72.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 654 | 428.00 | 386.00 | 71.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 655 | 429.00 | 386.00 | 70.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 656 | 430.00 | 386.00 | 69.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 657 | 431.00 | 386.00 | 68.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 658 | 432.00 | 386.00 | 67.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 659 | 433.00 | 386.00 | 66.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 660 | 434.00 | 386.00 | 65.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 661 | 435.00 | 386.00 | 64.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 662 | 436.00 | 386.00 | 63.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 663 | 437.00 | 386.00 | 62.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 664 | 438.00 | 386.00 | 61.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 665 | 439.00 | 386.00 | 60.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 666 | 440.00 | 386.00 | 59.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 667 | 441.00 | 386.00 | 58.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 668 | 442.00 | 386.00 | 57.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 669 | 443.00 | 386.00 | 56.00 | 3.73 | SIM | dentro da janela vertical e do lado solicitado |
| 670 | 444.00 | 385.00 | 55.01 | 4.73 | SIM | dentro da janela vertical e do lado solicitado |
| 671 | 445.00 | 384.00 | 54.04 | 5.73 | SIM | dentro da janela vertical e do lado solicitado |
| 672 | 446.00 | 384.00 | 53.04 | 5.73 | SIM | dentro da janela vertical e do lado solicitado |
| 673 | 447.00 | 383.00 | 52.09 | 6.73 | SIM | dentro da janela vertical e do lado solicitado |
| 674 | 448.00 | 382.00 | 51.16 | 7.73 | SIM | dentro da janela vertical e do lado solicitado |
| 675 | 449.00 | 382.00 | 50.16 | 7.73 | SIM | dentro da janela vertical e do lado solicitado |
| 676 | 450.00 | 381.00 | 49.25 | 8.73 | SIM | dentro da janela vertical e do lado solicitado |
| 677 | 451.00 | 380.00 | 48.37 | 9.73 | SIM | dentro da janela vertical e do lado solicitado |
| 678 | 452.00 | 379.00 | 47.52 | 10.73 | SIM | dentro da janela vertical e do lado solicitado |
| 679 | 453.00 | 379.00 | 46.53 | 10.73 | SIM | dentro da janela vertical e do lado solicitado |
| 680 | 454.00 | 378.00 | 45.71 | 11.73 | SIM | dentro da janela vertical e do lado solicitado |
| 681 | 455.00 | 377.00 | 44.91 | 12.73 | SIM | dentro da janela vertical e do lado solicitado |
| 682 | 456.00 | 376.00 | 44.15 | 13.73 | SIM | dentro da janela vertical e do lado solicitado |
| 683 | 457.00 | 376.00 | 43.17 | 13.73 | SIM | dentro da janela vertical e do lado solicitado |
| 684 | 458.00 | 375.00 | 42.45 | 14.73 | SIM | dentro da janela vertical e do lado solicitado |
| 685 | 459.00 | 374.00 | 41.76 | 15.73 | SIM | dentro da janela vertical e do lado solicitado |
| 686 | 460.00 | 373.00 | 41.11 | 16.73 | SIM | dentro da janela vertical e do lado solicitado |
| 687 | 461.00 | 373.00 | 40.16 | 16.73 | SIM | dentro da janela vertical e do lado solicitado |
| 688 | 462.00 | 372.00 | 39.56 | 17.73 | SIM | dentro da janela vertical e do lado solicitado |
| 689 | 463.00 | 371.00 | 39.00 | 18.73 | SIM | dentro da janela vertical e do lado solicitado |
| 690 | 464.00 | 370.00 | 38.48 | 19.73 | SIM | dentro da janela vertical e do lado solicitado |
| 691 | 465.00 | 369.00 | 38.01 | 20.73 | SIM | dentro da janela vertical e do lado solicitado |
| 692 | 466.00 | 368.00 | 37.59 | 21.73 | SIM | dentro da janela vertical e do lado solicitado |
| 693 | 467.00 | 367.00 | 37.22 | 22.73 | SIM | dentro da janela vertical e do lado solicitado |
| 694 | 468.00 | 366.00 | 36.89 | 23.73 | SIM | dentro da janela vertical e do lado solicitado |
| 695 | 469.00 | 365.00 | 36.62 | 24.73 | SIM | dentro da janela vertical e do lado solicitado |
| 696 | 470.00 | 364.00 | 36.40 | 25.73 | SIM | dentro da janela vertical e do lado solicitado |
| 697 | 471.00 | 363.00 | 36.24 | 26.73 | SIM | dentro da janela vertical e do lado solicitado |
| 698 | 472.00 | 363.00 | 35.47 | 26.73 | SIM | dentro da janela vertical e do lado solicitado |
| 699 | 473.00 | 362.00 | 35.38 | 27.73 | SIM | dentro da janela vertical e do lado solicitado |
| 700 | 474.00 | 361.00 | 35.36 | 28.73 | SIM | dentro da janela vertical e do lado solicitado |
| 701 | 475.00 | 360.00 | 35.38 | 29.73 | SIM | dentro da janela vertical e do lado solicitado |
| 702 | 476.00 | 359.00 | 35.47 | 30.73 | SIM | dentro da janela vertical e do lado solicitado |
| 703 | 477.00 | 358.00 | 35.61 | 31.73 | SIM | dentro da janela vertical e do lado solicitado |
| 704 | 478.00 | 357.00 | 35.81 | 32.73 | SIM | dentro da janela vertical e do lado solicitado |
| 705 | 479.00 | 356.00 | 36.06 | 33.73 | SIM | dentro da janela vertical e do lado solicitado |
| 706 | 480.00 | 355.00 | 36.36 | 34.73 | SIM | dentro da janela vertical e do lado solicitado |
| 707 | 481.00 | 354.00 | 36.72 | 35.73 | SIM | dentro da janela vertical e do lado solicitado |
| 708 | 482.00 | 353.00 | 37.12 | 36.73 | SIM | dentro da janela vertical e do lado solicitado |
| 709 | 483.00 | 352.00 | 37.58 | 37.73 | SIM | dentro da janela vertical e do lado solicitado |
| 710 | 483.00 | 351.00 | 38.48 | 38.73 | SIM | dentro da janela vertical e do lado solicitado |
| 711 | 484.00 | 350.00 | 39.00 | 39.73 | SIM | dentro da janela vertical e do lado solicitado |
| 712 | 485.00 | 349.00 | 39.56 | 40.73 | SIM | dentro da janela vertical e do lado solicitado |
| 713 | 486.00 | 348.00 | 40.16 | 41.73 | SIM | dentro da janela vertical e do lado solicitado |
| 714 | 487.00 | 347.00 | 40.80 | 42.73 | SIM | dentro da janela vertical e do lado solicitado |
| 715 | 488.00 | 346.00 | 41.48 | 43.73 | SIM | dentro da janela vertical e do lado solicitado |
| 716 | 489.00 | 345.00 | 42.20 | 44.73 | SIM | dentro da janela vertical e do lado solicitado |
| 717 | 490.00 | 344.00 | 42.95 | 45.73 | SIM | dentro da janela vertical e do lado solicitado |
| 718 | 490.00 | 343.00 | 43.93 | 46.73 | SIM | dentro da janela vertical e do lado solicitado |
| 719 | 491.00 | 342.00 | 44.72 | 47.73 | SIM | dentro da janela vertical e do lado solicitado |
| 720 | 492.00 | 341.00 | 45.54 | 48.73 | SIM | dentro da janela vertical e do lado solicitado |
| 721 | 493.00 | 340.00 | 46.39 | 49.73 | SIM | dentro da janela vertical e do lado solicitado |
| 722 | 493.00 | 339.00 | 47.38 | 50.73 | SIM | dentro da janela vertical e do lado solicitado |
| 723 | 494.00 | 338.00 | 48.26 | 51.73 | SIM | dentro da janela vertical e do lado solicitado |
| 724 | 495.00 | 337.00 | 49.16 | 52.73 | SIM | dentro da janela vertical e do lado solicitado |
| 725 | 496.00 | 336.00 | 50.09 | 53.73 | SIM | dentro da janela vertical e do lado solicitado |
| 726 | 496.00 | 335.00 | 51.09 | 54.73 | SIM | dentro da janela vertical e do lado solicitado |
| 727 | 497.00 | 334.00 | 52.04 | 55.73 | SIM | dentro da janela vertical e do lado solicitado |
| 728 | 498.00 | 333.00 | 53.01 | 56.73 | SIM | dentro da janela vertical e do lado solicitado |
| 729 | 499.00 | 332.00 | 54.00 | 57.73 | SIM | dentro da janela vertical e do lado solicitado |
| 730 | 499.00 | 331.00 | 55.00 | 58.73 | SIM | dentro da janela vertical e do lado solicitado |
| 731 | 500.00 | 330.00 | 56.01 | 59.73 | SIM | dentro da janela vertical e do lado solicitado |
| 732 | 501.00 | 329.00 | 57.04 | 60.73 | SIM | dentro da janela vertical e do lado solicitado |
| 733 | 501.00 | 328.00 | 58.03 | 61.73 | SIM | dentro da janela vertical e do lado solicitado |
| 734 | 502.00 | 327.00 | 59.08 | 62.73 | SIM | dentro da janela vertical e do lado solicitado |
| 735 | 503.00 | 326.00 | 60.13 | 63.73 | SIM | dentro da janela vertical e do lado solicitado |
| 736 | 503.00 | 325.00 | 61.13 | 64.73 | SIM | dentro da janela vertical e do lado solicitado |
| 737 | 504.00 | 324.00 | 62.20 | 65.73 | SIM | dentro da janela vertical e do lado solicitado |
| 738 | 504.00 | 323.00 | 63.20 | 66.73 | SIM | dentro da janela vertical e do lado solicitado |
| 739 | 505.00 | 322.00 | 64.28 | 67.73 | SIM | dentro da janela vertical e do lado solicitado |
| 740 | 506.00 | 321.00 | 65.38 | 68.73 | SIM | dentro da janela vertical e do lado solicitado |
| 741 | 506.00 | 320.00 | 66.37 | 69.73 | SIM | dentro da janela vertical e do lado solicitado |
| 742 | 507.00 | 319.00 | 67.48 | 70.73 | SIM | dentro da janela vertical e do lado solicitado |
| 743 | 507.00 | 318.00 | 68.47 | 71.73 | SIM | dentro da janela vertical e do lado solicitado |
| 744 | 508.00 | 317.00 | 69.58 | 72.73 | SIM | dentro da janela vertical e do lado solicitado |
| 745 | 509.00 | 316.00 | 70.71 | 73.73 | SIM | dentro da janela vertical e do lado solicitado |
| 746 | 509.00 | 315.00 | 71.70 | 74.73 | SIM | dentro da janela vertical e do lado solicitado |
| 747 | 510.00 | 314.00 | 72.84 | 75.73 | SIM | dentro da janela vertical e do lado solicitado |
| 748 | 510.00 | 313.00 | 73.82 | 76.73 | SIM | dentro da janela vertical e do lado solicitado |
| 749 | 511.00 | 312.00 | 74.97 | 77.73 | SIM | dentro da janela vertical e do lado solicitado |
| 750 | 511.00 | 311.00 | 75.95 | 78.73 | SIM | dentro da janela vertical e do lado solicitado |
| 751 | 512.00 | 310.00 | 77.10 | 79.73 | SIM | dentro da janela vertical e do lado solicitado |
| 752 | 512.00 | 309.00 | 78.09 | 80.73 | SIM | dentro da janela vertical e do lado solicitado |
| 753 | 513.00 | 308.00 | 79.25 | 81.73 | SIM | dentro da janela vertical e do lado solicitado |
| 754 | 513.00 | 307.00 | 80.23 | 82.73 | SIM | dentro da janela vertical e do lado solicitado |
| 755 | 514.00 | 306.00 | 81.39 | 83.73 | SIM | dentro da janela vertical e do lado solicitado |
| 756 | 514.00 | 305.00 | 82.38 | 84.73 | SIM | dentro da janela vertical e do lado solicitado |
| 757 | 515.00 | 304.00 | 83.55 | 85.73 | SIM | dentro da janela vertical e do lado solicitado |
| 758 | 515.00 | 303.00 | 84.53 | 86.73 | SIM | dentro da janela vertical e do lado solicitado |
| 759 | 516.00 | 302.00 | 85.70 | 87.73 | SIM | dentro da janela vertical e do lado solicitado |
| 760 | 516.00 | 301.00 | 86.68 | 88.73 | SIM | dentro da janela vertical e do lado solicitado |
| 761 | 517.00 | 300.00 | 87.86 | 89.73 | SIM | dentro da janela vertical e do lado solicitado |
| 762 | 517.00 | 299.00 | 88.84 | 90.73 | SIM | dentro da janela vertical e do lado solicitado |
| 763 | 518.00 | 298.00 | 90.03 | 91.73 | SIM | dentro da janela vertical e do lado solicitado |
| 764 | 518.00 | 297.00 | 91.01 | 92.73 | SIM | dentro da janela vertical e do lado solicitado |
| 765 | 519.00 | 296.00 | 92.20 | 93.73 | SIM | dentro da janela vertical e do lado solicitado |
| 766 | 519.00 | 295.00 | 93.17 | 94.73 | SIM | dentro da janela vertical e do lado solicitado |
| 767 | 520.00 | 294.00 | 94.37 | 95.73 | SIM | dentro da janela vertical e do lado solicitado |
| 768 | 520.00 | 293.00 | 95.34 | 96.73 | SIM | dentro da janela vertical e do lado solicitado |
| 769 | 521.00 | 292.00 | 96.54 | 97.73 | SIM | dentro da janela vertical e do lado solicitado |
| 770 | 521.00 | 291.00 | 97.51 | 98.73 | SIM | dentro da janela vertical e do lado solicitado |
| 771 | 521.00 | 290.00 | 98.49 | 99.73 | SIM | dentro da janela vertical e do lado solicitado |
| 772 | 522.00 | 289.00 | 99.69 | 100.73 | SIM | dentro da janela vertical e do lado solicitado |
| 773 | 522.00 | 288.00 | 100.66 | 101.73 | SIM | dentro da janela vertical e do lado solicitado |
| 774 | 522.00 | 287.00 | 101.64 | 102.73 | SIM | dentro da janela vertical e do lado solicitado |
| 775 | 523.00 | 286.00 | 102.84 | 103.73 | SIM | dentro da janela vertical e do lado solicitado |
| 776 | 523.00 | 285.00 | 103.81 | 104.73 | SIM | dentro da janela vertical e do lado solicitado |
| 777 | 524.00 | 284.00 | 105.02 | 105.73 | SIM | dentro da janela vertical e do lado solicitado |
| 778 | 524.00 | 283.00 | 105.99 | 106.73 | SIM | dentro da janela vertical e do lado solicitado |
| 779 | 524.00 | 282.00 | 106.96 | 107.73 | SIM | dentro da janela vertical e do lado solicitado |
| 780 | 525.00 | 281.00 | 108.17 | 108.73 | SIM | dentro da janela vertical e do lado solicitado |
| 781 | 525.00 | 280.00 | 109.14 | 109.73 | SIM | dentro da janela vertical e do lado solicitado |
| 782 | 525.00 | 279.00 | 110.11 | 110.73 | SIM | dentro da janela vertical e do lado solicitado |
| 783 | 526.00 | 278.00 | 111.32 | 111.73 | SIM | dentro da janela vertical e do lado solicitado |
| 784 | 526.00 | 277.00 | 112.29 | 112.73 | SIM | dentro da janela vertical e do lado solicitado |
| 785 | 526.00 | 276.00 | 113.27 | 113.73 | SIM | dentro da janela vertical e do lado solicitado |
| 786 | 526.00 | 275.00 | 114.24 | 114.73 | SIM | dentro da janela vertical e do lado solicitado |
| 787 | 527.00 | 274.00 | 115.45 | 115.73 | SIM | dentro da janela vertical e do lado solicitado |
| 788 | 527.00 | 273.00 | 116.42 | 116.73 | SIM | dentro da janela vertical e do lado solicitado |
| 789 | 527.00 | 272.00 | 117.39 | 117.73 | SIM | dentro da janela vertical e do lado solicitado |
| 790 | 528.00 | 271.00 | 118.60 | 118.73 | SIM | dentro da janela vertical e do lado solicitado |
| 791 | 528.00 | 270.00 | 119.57 | 119.73 | SIM | dentro da janela vertical e do lado solicitado |
| 792 | 528.00 | 269.00 | 120.54 | 120.73 | SIM | dentro da janela vertical e do lado solicitado |
| 793 | 528.00 | 268.00 | 121.51 | 121.73 | SIM | dentro da janela vertical e do lado solicitado |
| 794 | 529.00 | 267.00 | 122.72 | 122.73 | SIM | dentro da janela vertical e do lado solicitado |
| 795 | 529.00 | 266.00 | 123.69 | 123.73 | SIM | dentro da janela vertical e do lado solicitado |
| 796 | 529.00 | 265.00 | 124.66 | 124.73 | SIM | dentro da janela vertical e do lado solicitado |
| 797 | 529.00 | 264.00 | 125.63 | 125.73 | SIM | dentro da janela vertical e do lado solicitado |
| 798 | 530.00 | 263.00 | 126.85 | 126.73 | SIM | dentro da janela vertical e do lado solicitado |
| 799 | 530.00 | 262.00 | 127.82 | 127.73 | SIM | dentro da janela vertical e do lado solicitado |
| 800 | 530.00 | 261.00 | 128.79 | 128.73 | SIM | dentro da janela vertical e do lado solicitado |
| 801 | 530.00 | 260.00 | 129.76 | 129.73 | SIM | dentro da janela vertical e do lado solicitado |
| 802 | 530.00 | 259.00 | 130.73 | 130.73 | SIM | dentro da janela vertical e do lado solicitado |
| 803 | 531.00 | 258.00 | 131.94 | 131.73 | SIM | dentro da janela vertical e do lado solicitado |
| 804 | 531.00 | 257.00 | 132.91 | 132.73 | SIM | dentro da janela vertical e do lado solicitado |
| 805 | 531.00 | 256.00 | 133.88 | 133.73 | SIM | dentro da janela vertical e do lado solicitado |
| 806 | 531.00 | 255.00 | 134.85 | 134.73 | SIM | dentro da janela vertical e do lado solicitado |
| 807 | 532.00 | 254.00 | 136.06 | 135.73 | SIM | dentro da janela vertical e do lado solicitado |
| 808 | 532.00 | 253.00 | 137.03 | 136.73 | SIM | dentro da janela vertical e do lado solicitado |
| 809 | 532.00 | 252.00 | 138.00 | 137.73 | SIM | dentro da janela vertical e do lado solicitado |
| 810 | 532.00 | 251.00 | 138.97 | 138.73 | SIM | dentro da janela vertical e do lado solicitado |
| 811 | 532.00 | 250.00 | 139.95 | 139.73 | SIM | dentro da janela vertical e do lado solicitado |
| 812 | 533.00 | 249.00 | 141.16 | 140.73 | SIM | dentro da janela vertical e do lado solicitado |
| 813 | 533.00 | 248.00 | 142.13 | 141.73 | SIM | dentro da janela vertical e do lado solicitado |
| 814 | 533.00 | 247.00 | 143.10 | 142.73 | SIM | dentro da janela vertical e do lado solicitado |
| 815 | 533.00 | 246.00 | 144.07 | 143.73 | SIM | dentro da janela vertical e do lado solicitado |
| 816 | 533.00 | 245.00 | 145.04 | 144.73 | SIM | dentro da janela vertical e do lado solicitado |
| 817 | 533.00 | 244.00 | 146.01 | 145.73 | SIM | dentro da janela vertical e do lado solicitado |
| 818 | 533.00 | 243.00 | 146.99 | 146.73 | SIM | dentro da janela vertical e do lado solicitado |
| 819 | 534.00 | 242.00 | 148.19 | 147.73 | SIM | dentro da janela vertical e do lado solicitado |
| 820 | 534.00 | 241.00 | 149.16 | 148.73 | SIM | dentro da janela vertical e do lado solicitado |
| 821 | 534.00 | 240.00 | 150.14 | 149.73 | SIM | dentro da janela vertical e do lado solicitado |
| 822 | 534.00 | 239.00 | 151.11 | 150.73 | SIM | dentro da janela vertical e do lado solicitado |
| 823 | 534.00 | 238.00 | 152.08 | 151.73 | SIM | dentro da janela vertical e do lado solicitado |
| 824 | 534.00 | 237.00 | 153.06 | 152.73 | SIM | dentro da janela vertical e do lado solicitado |
| 825 | 534.00 | 236.00 | 154.03 | 153.73 | SIM | dentro da janela vertical e do lado solicitado |
| 826 | 534.00 | 235.00 | 155.00 | 154.73 | SIM | dentro da janela vertical e do lado solicitado |
| 827 | 535.00 | 234.00 | 156.20 | 155.73 | SIM | dentro da janela vertical e do lado solicitado |
| 828 | 535.00 | 233.00 | 157.18 | 156.73 | SIM | dentro da janela vertical e do lado solicitado |
| 829 | 535.00 | 232.00 | 158.15 | 157.73 | SIM | dentro da janela vertical e do lado solicitado |
| 830 | 535.00 | 231.00 | 159.13 | 158.73 | SIM | dentro da janela vertical e do lado solicitado |
| 831 | 535.00 | 230.00 | 160.10 | 159.73 | SIM | dentro da janela vertical e do lado solicitado |
| 832 | 535.00 | 229.00 | 161.07 | 160.73 | SIM | dentro da janela vertical e do lado solicitado |
| 833 | 535.00 | 228.00 | 162.05 | 161.73 | SIM | dentro da janela vertical e do lado solicitado |
| 834 | 535.00 | 227.00 | 163.02 | 162.73 | SIM | dentro da janela vertical e do lado solicitado |
| 835 | 535.00 | 226.00 | 164.00 | 163.73 | SIM | dentro da janela vertical e do lado solicitado |
| 836 | 535.00 | 225.00 | 164.98 | 164.73 | SIM | dentro da janela vertical e do lado solicitado |
| 837 | 535.00 | 224.00 | 165.95 | 165.73 | SIM | dentro da janela vertical e do lado solicitado |
| 838 | 535.00 | 223.00 | 166.93 | 166.73 | SIM | dentro da janela vertical e do lado solicitado |
| 839 | 535.00 | 222.00 | 167.90 | 167.73 | SIM | dentro da janela vertical e do lado solicitado |
| 840 | 535.00 | 221.00 | 168.88 | 168.73 | SIM | dentro da janela vertical e do lado solicitado |
| 841 | 535.00 | 220.00 | 169.86 | 169.73 | SIM | dentro da janela vertical e do lado solicitado |
| 842 | 535.00 | 219.00 | 170.84 | 170.73 | SIM | dentro da janela vertical e do lado solicitado |
| 843 | 535.00 | 218.00 | 171.81 | 171.73 | SIM | dentro da janela vertical e do lado solicitado |
| 844 | 535.00 | 217.00 | 172.79 | 172.73 | SIM | dentro da janela vertical e do lado solicitado |
| 845 | 535.00 | 216.00 | 173.77 | 173.73 | SIM | dentro da janela vertical e do lado solicitado |
| 846 | 535.00 | 215.00 | 174.75 | 174.73 | SIM | dentro da janela vertical e do lado solicitado |
| 847 | 535.00 | 214.00 | 175.73 | 175.73 | SIM | dentro da janela vertical e do lado solicitado |
| 848 | 535.00 | 213.00 | 176.71 | 176.73 | SIM | dentro da janela vertical e do lado solicitado |
| 849 | 535.00 | 212.00 | 177.69 | 177.73 | SIM | dentro da janela vertical e do lado solicitado |
| 850 | 535.00 | 211.00 | 178.66 | 178.73 | SIM | dentro da janela vertical e do lado solicitado |
| 851 | 535.00 | 210.00 | 179.64 | 179.73 | SIM | dentro da janela vertical e do lado solicitado |
| 852 | 535.00 | 209.00 | 180.62 | 180.73 | SIM | dentro da janela vertical e do lado solicitado |
| 853 | 535.00 | 208.00 | 181.60 | 181.73 | SIM | dentro da janela vertical e do lado solicitado |
| 854 | 535.00 | 207.00 | 182.58 | 182.73 | SIM | dentro da janela vertical e do lado solicitado |
| 855 | 535.00 | 206.00 | 183.56 | 183.73 | SIM | dentro da janela vertical e do lado solicitado |
| 856 | 535.00 | 205.00 | 184.55 | 184.73 | SIM | dentro da janela vertical e do lado solicitado |
| 857 | 535.00 | 204.00 | 185.53 | 185.73 | SIM | dentro da janela vertical e do lado solicitado |
| 858 | 535.00 | 203.00 | 186.51 | 186.73 | SIM | dentro da janela vertical e do lado solicitado |
| 859 | 535.00 | 202.00 | 187.49 | 187.73 | SIM | dentro da janela vertical e do lado solicitado |
| 860 | 535.00 | 201.00 | 188.47 | 188.73 | SIM | dentro da janela vertical e do lado solicitado |
| 861 | 535.00 | 200.00 | 189.45 | 189.73 | SIM | dentro da janela vertical e do lado solicitado |
| 862 | 535.00 | 199.00 | 190.43 | 190.73 | SIM | dentro da janela vertical e do lado solicitado |
| 863 | 535.00 | 198.00 | 191.42 | 191.73 | SIM | dentro da janela vertical e do lado solicitado |
| 864 | 534.00 | 197.00 | 192.21 | 192.73 | SIM | dentro da janela vertical e do lado solicitado |
| 865 | 534.00 | 196.00 | 193.20 | 193.73 | SIM | dentro da janela vertical e do lado solicitado |
| 866 | 534.00 | 195.00 | 194.18 | 194.73 | SIM | dentro da janela vertical e do lado solicitado |
| 867 | 534.00 | 194.00 | 195.16 | 195.73 | SIM | dentro da janela vertical e do lado solicitado |
| 868 | 534.00 | 193.00 | 196.15 | 196.73 | SIM | dentro da janela vertical e do lado solicitado |
| 869 | 534.00 | 192.00 | 197.13 | 197.73 | SIM | dentro da janela vertical e do lado solicitado |
| 870 | 534.00 | 191.00 | 198.12 | 198.73 | SIM | dentro da janela vertical e do lado solicitado |
| 871 | 534.00 | 190.00 | 199.10 | 199.73 | SIM | dentro da janela vertical e do lado solicitado |
| 872 | 533.00 | 189.00 | 199.91 | 200.73 | SIM | dentro da janela vertical e do lado solicitado |
| 873 | 533.00 | 188.00 | 200.90 | 201.73 | SIM | dentro da janela vertical e do lado solicitado |
| 874 | 533.00 | 187.00 | 201.88 | 202.73 | SIM | dentro da janela vertical e do lado solicitado |
| 875 | 533.00 | 186.00 | 202.87 | 203.73 | SIM | dentro da janela vertical e do lado solicitado |
| 876 | 533.00 | 185.00 | 203.86 | 204.73 | SIM | dentro da janela vertical e do lado solicitado |
| 877 | 533.00 | 184.00 | 204.84 | 205.73 | NÃO | fora da faixa vertical |
| 878 | 533.00 | 183.00 | 205.83 | 206.73 | NÃO | fora da faixa vertical |
| 879 | 533.00 | 182.00 | 206.81 | 207.73 | NÃO | fora da faixa vertical |
| 880 | 532.00 | 181.00 | 207.64 | 208.73 | NÃO | fora da faixa vertical |
| 881 | 532.00 | 180.00 | 208.63 | 209.73 | NÃO | fora da faixa vertical |
| 882 | 532.00 | 179.00 | 209.61 | 210.73 | NÃO | fora da faixa vertical |
| 883 | 532.00 | 178.00 | 210.60 | 211.73 | NÃO | fora da faixa vertical |
| 884 | 532.00 | 177.00 | 211.59 | 212.73 | NÃO | fora da faixa vertical |
| 885 | 531.00 | 176.00 | 212.42 | 213.73 | NÃO | fora da faixa vertical |
| 886 | 531.00 | 175.00 | 213.41 | 214.73 | NÃO | fora da faixa vertical |
| 887 | 531.00 | 174.00 | 214.40 | 215.73 | NÃO | fora da faixa vertical |
| 888 | 531.00 | 173.00 | 215.39 | 216.73 | NÃO | fora da faixa vertical |
| 889 | 530.00 | 172.00 | 216.23 | 217.73 | NÃO | fora da faixa vertical |
| 890 | 530.00 | 171.00 | 217.22 | 218.73 | NÃO | fora da faixa vertical |
| 891 | 530.00 | 170.00 | 218.21 | 219.73 | NÃO | fora da faixa vertical |
| 892 | 530.00 | 169.00 | 219.20 | 220.73 | NÃO | fora da faixa vertical |
| 893 | 530.00 | 168.00 | 220.19 | 221.73 | NÃO | fora da faixa vertical |
| 894 | 529.00 | 167.00 | 221.05 | 222.73 | NÃO | fora da faixa vertical |
| 895 | 529.00 | 166.00 | 222.04 | 223.73 | NÃO | fora da faixa vertical |
| 896 | 529.00 | 165.00 | 223.03 | 224.73 | NÃO | fora da faixa vertical |
| 897 | 529.00 | 164.00 | 224.02 | 225.73 | NÃO | fora da faixa vertical |
| 898 | 528.00 | 163.00 | 224.88 | 226.73 | NÃO | fora da faixa vertical |
| 899 | 528.00 | 162.00 | 225.87 | 227.73 | NÃO | fora da faixa vertical |
| 900 | 528.00 | 161.00 | 226.86 | 228.73 | NÃO | fora da faixa vertical |
| 901 | 528.00 | 160.00 | 227.85 | 229.73 | NÃO | fora da faixa vertical |
| 902 | 527.00 | 159.00 | 228.72 | 230.73 | NÃO | fora da faixa vertical |
| 903 | 527.00 | 158.00 | 229.71 | 231.73 | NÃO | fora da faixa vertical |
| 904 | 527.00 | 157.00 | 230.71 | 232.73 | NÃO | fora da faixa vertical |
| 905 | 526.00 | 156.00 | 231.58 | 233.73 | NÃO | fora da faixa vertical |
| 906 | 526.00 | 155.00 | 232.57 | 234.73 | NÃO | fora da faixa vertical |
| 907 | 526.00 | 154.00 | 233.57 | 235.73 | NÃO | fora da faixa vertical |
| 908 | 526.00 | 153.00 | 234.56 | 236.73 | NÃO | fora da faixa vertical |
| 909 | 525.00 | 152.00 | 235.44 | 237.73 | NÃO | fora da faixa vertical |
| 910 | 525.00 | 151.00 | 236.43 | 238.73 | NÃO | fora da faixa vertical |
| 911 | 525.00 | 150.00 | 237.43 | 239.73 | NÃO | fora da faixa vertical |
| 912 | 524.00 | 149.00 | 238.31 | 240.73 | NÃO | fora da faixa vertical |
| 913 | 524.00 | 148.00 | 239.31 | 241.73 | NÃO | fora da faixa vertical |
| 914 | 523.00 | 147.00 | 240.20 | 242.73 | NÃO | fora da faixa vertical |
| 915 | 523.00 | 146.00 | 241.20 | 243.73 | NÃO | fora da faixa vertical |
| 916 | 523.00 | 145.00 | 242.19 | 244.73 | NÃO | fora da faixa vertical |
| 917 | 522.00 | 144.00 | 243.09 | 245.73 | NÃO | fora da faixa vertical |
| 918 | 522.00 | 143.00 | 244.09 | 246.73 | NÃO | fora da faixa vertical |
| 919 | 522.00 | 142.00 | 245.08 | 247.73 | NÃO | fora da faixa vertical |
| 920 | 521.00 | 141.00 | 245.99 | 248.73 | NÃO | fora da faixa vertical |
| 921 | 521.00 | 140.00 | 246.98 | 249.73 | NÃO | fora da faixa vertical |
| 922 | 520.00 | 139.00 | 247.89 | 250.73 | NÃO | fora da faixa vertical |
| 923 | 520.00 | 138.00 | 248.89 | 251.73 | NÃO | fora da faixa vertical |
| 924 | 520.00 | 137.00 | 249.88 | 252.73 | NÃO | fora da faixa vertical |
| 925 | 519.00 | 136.00 | 250.80 | 253.73 | NÃO | fora da faixa vertical |
| 926 | 519.00 | 135.00 | 251.80 | 254.73 | NÃO | fora da faixa vertical |
| 927 | 518.00 | 134.00 | 252.72 | 255.73 | NÃO | fora da faixa vertical |
| 928 | 518.00 | 133.00 | 253.71 | 256.73 | NÃO | fora da faixa vertical |
| 929 | 517.00 | 132.00 | 254.64 | 257.73 | NÃO | fora da faixa vertical |
| 930 | 517.00 | 131.00 | 255.63 | 258.73 | NÃO | fora da faixa vertical |
| 931 | 516.00 | 130.00 | 256.56 | 259.73 | NÃO | fora da faixa vertical |
| 932 | 516.00 | 129.00 | 257.56 | 260.73 | NÃO | fora da faixa vertical |
| 933 | 515.00 | 128.00 | 258.50 | 261.73 | NÃO | fora da faixa vertical |
| 934 | 515.00 | 127.00 | 259.49 | 262.73 | NÃO | fora da faixa vertical |
| 935 | 514.00 | 126.00 | 260.43 | 263.73 | NÃO | fora da faixa vertical |
| 936 | 514.00 | 125.00 | 261.43 | 264.73 | NÃO | fora da faixa vertical |
| 937 | 513.00 | 124.00 | 262.37 | 265.73 | NÃO | fora da faixa vertical |
| 938 | 513.00 | 123.00 | 263.37 | 266.73 | NÃO | fora da faixa vertical |
| 939 | 512.00 | 122.00 | 264.32 | 267.73 | NÃO | fora da faixa vertical |
| 940 | 512.00 | 121.00 | 265.32 | 268.73 | NÃO | fora da faixa vertical |
| 941 | 511.00 | 120.00 | 266.27 | 269.73 | NÃO | fora da faixa vertical |
| 942 | 511.00 | 119.00 | 267.27 | 270.73 | NÃO | fora da faixa vertical |
| 943 | 510.00 | 118.00 | 268.23 | 271.73 | NÃO | fora da faixa vertical |
| 944 | 510.00 | 117.00 | 269.22 | 272.73 | NÃO | fora da faixa vertical |
| 945 | 509.00 | 116.00 | 270.19 | 273.73 | NÃO | fora da faixa vertical |
| 946 | 509.00 | 115.00 | 271.18 | 274.73 | NÃO | fora da faixa vertical |
| 947 | 508.00 | 114.00 | 272.15 | 275.73 | NÃO | fora da faixa vertical |
| 948 | 507.00 | 113.00 | 273.12 | 276.73 | NÃO | fora da faixa vertical |
| 949 | 507.00 | 112.00 | 274.12 | 277.73 | NÃO | fora da faixa vertical |
| 950 | 506.00 | 111.00 | 275.09 | 278.73 | NÃO | fora da faixa vertical |
| 951 | 506.00 | 110.00 | 276.09 | 279.73 | NÃO | fora da faixa vertical |
| 952 | 505.00 | 109.00 | 277.06 | 280.73 | NÃO | fora da faixa vertical |
| 953 | 504.00 | 108.00 | 278.04 | 281.73 | NÃO | fora da faixa vertical |
| 954 | 504.00 | 107.00 | 279.04 | 282.73 | NÃO | fora da faixa vertical |
| 955 | 503.00 | 106.00 | 280.03 | 283.73 | NÃO | fora da faixa vertical |
| 956 | 503.00 | 105.00 | 281.03 | 284.73 | NÃO | fora da faixa vertical |
| 957 | 502.00 | 104.00 | 282.02 | 285.73 | NÃO | fora da faixa vertical |
| 958 | 501.00 | 103.00 | 283.01 | 286.73 | NÃO | fora da faixa vertical |
| 959 | 501.00 | 102.00 | 284.01 | 287.73 | NÃO | fora da faixa vertical |
| 960 | 500.00 | 101.00 | 285.00 | 288.73 | NÃO | fora da faixa vertical |
| 961 | 499.00 | 100.00 | 286.00 | 289.73 | NÃO | fora da faixa vertical |
| 962 | 498.00 | 99.00 | 287.00 | 290.73 | NÃO | fora da faixa vertical |
| 963 | 498.00 | 98.00 | 288.00 | 291.73 | NÃO | fora da faixa vertical |
| 964 | 497.00 | 97.00 | 289.01 | 292.73 | NÃO | fora da faixa vertical |
| 965 | 496.00 | 96.00 | 290.02 | 293.73 | NÃO | fora da faixa vertical |
| 966 | 495.00 | 95.00 | 291.03 | 294.73 | NÃO | fora da faixa vertical |
| 967 | 495.00 | 94.00 | 292.03 | 295.73 | NÃO | fora da faixa vertical |
| 968 | 494.00 | 93.00 | 293.04 | 296.73 | NÃO | fora da faixa vertical |
| 969 | 493.00 | 92.00 | 294.06 | 297.73 | NÃO | fora da faixa vertical |
| 970 | 492.00 | 91.00 | 295.08 | 298.73 | NÃO | fora da faixa vertical |
| 971 | 492.00 | 90.00 | 296.08 | 299.73 | NÃO | fora da faixa vertical |
| 972 | 491.00 | 89.00 | 297.11 | 300.73 | NÃO | fora da faixa vertical |
| 973 | 490.00 | 88.00 | 298.14 | 301.73 | NÃO | fora da faixa vertical |
| 974 | 489.00 | 87.00 | 299.17 | 302.73 | NÃO | fora da faixa vertical |
| 975 | 489.00 | 86.00 | 300.17 | 303.73 | NÃO | fora da faixa vertical |
| 976 | 488.00 | 85.00 | 301.20 | 304.73 | NÃO | fora da faixa vertical |
| 977 | 487.00 | 84.00 | 302.24 | 305.73 | NÃO | fora da faixa vertical |
| 978 | 486.00 | 83.00 | 303.28 | 306.73 | NÃO | fora da faixa vertical |
| 979 | 485.00 | 82.00 | 304.32 | 307.73 | NÃO | fora da faixa vertical |
| 980 | 484.00 | 81.00 | 305.37 | 308.73 | NÃO | fora da faixa vertical |
| 981 | 483.00 | 80.00 | 306.42 | 309.73 | NÃO | fora da faixa vertical |
| 982 | 482.00 | 79.00 | 307.47 | 310.73 | NÃO | fora da faixa vertical |
| 983 | 481.00 | 78.00 | 308.53 | 311.73 | NÃO | fora da faixa vertical |
| 984 | 480.00 | 77.00 | 309.58 | 312.73 | NÃO | fora da faixa vertical |
| 985 | 480.00 | 76.00 | 310.58 | 313.73 | NÃO | fora da faixa vertical |
| 986 | 479.00 | 75.00 | 311.64 | 314.73 | NÃO | fora da faixa vertical |
| 987 | 478.00 | 74.00 | 312.71 | 315.73 | NÃO | fora da faixa vertical |
| 988 | 477.00 | 73.00 | 313.77 | 316.73 | NÃO | fora da faixa vertical |
| 989 | 476.00 | 72.00 | 314.84 | 317.73 | NÃO | fora da faixa vertical |
| 990 | 475.00 | 71.00 | 315.91 | 318.73 | NÃO | fora da faixa vertical |
| 991 | 474.00 | 70.00 | 316.99 | 319.73 | NÃO | fora da faixa vertical |
| 992 | 473.00 | 69.00 | 318.06 | 320.73 | NÃO | fora da faixa vertical |
| 993 | 472.00 | 68.00 | 319.14 | 321.73 | NÃO | fora da faixa vertical |
| 994 | 471.00 | 67.00 | 320.23 | 322.73 | NÃO | fora da faixa vertical |
| 995 | 470.00 | 66.00 | 321.31 | 323.73 | NÃO | fora da faixa vertical |
| 996 | 469.00 | 65.00 | 322.40 | 324.73 | NÃO | fora da faixa vertical |
| 997 | 468.00 | 65.00 | 322.49 | 324.73 | NÃO | fora da faixa vertical |
| 998 | 467.00 | 64.00 | 323.59 | 325.73 | NÃO | fora da faixa vertical |
| 999 | 466.00 | 63.00 | 324.68 | 326.73 | NÃO | fora da faixa vertical |
| 1000 | 465.00 | 62.00 | 325.78 | 327.73 | NÃO | fora da faixa vertical |
| 1001 | 464.00 | 61.00 | 326.88 | 328.73 | NÃO | fora da faixa vertical |
| 1002 | 463.00 | 60.00 | 327.98 | 329.73 | NÃO | fora da faixa vertical |
| 1003 | 462.00 | 59.00 | 329.09 | 330.73 | NÃO | fora da faixa vertical |
| 1004 | 461.00 | 58.00 | 330.19 | 331.73 | NÃO | fora da faixa vertical |
| 1005 | 460.00 | 58.00 | 330.31 | 331.73 | NÃO | fora da faixa vertical |
| 1006 | 459.00 | 57.00 | 331.42 | 332.73 | NÃO | fora da faixa vertical |
| 1007 | 458.00 | 56.00 | 332.54 | 333.73 | NÃO | fora da faixa vertical |
| 1008 | 457.00 | 56.00 | 332.66 | 333.73 | NÃO | fora da faixa vertical |
| 1009 | 456.00 | 55.00 | 333.78 | 334.73 | NÃO | fora da faixa vertical |
| 1010 | 455.00 | 54.00 | 334.90 | 335.73 | NÃO | fora da faixa vertical |
| 1011 | 454.00 | 53.00 | 336.03 | 336.73 | NÃO | fora da faixa vertical |
| 1012 | 453.00 | 53.00 | 336.16 | 336.73 | NÃO | fora da faixa vertical |
| 1013 | 452.00 | 52.00 | 337.29 | 337.73 | NÃO | fora da faixa vertical |
| 1014 | 451.00 | 51.00 | 338.42 | 338.73 | NÃO | fora da faixa vertical |
| 1015 | 450.00 | 50.00 | 339.55 | 339.73 | NÃO | fora da faixa vertical |
| 1016 | 449.00 | 50.00 | 339.70 | 339.73 | NÃO | fora da faixa vertical |
| 1017 | 448.00 | 49.00 | 340.84 | 340.73 | NÃO | fora da faixa vertical |
| 1018 | 447.00 | 48.00 | 341.98 | 341.73 | NÃO | fora da faixa vertical |
| 1019 | 446.00 | 48.00 | 342.13 | 341.73 | NÃO | fora da faixa vertical |
| 1020 | 445.00 | 47.00 | 343.27 | 342.73 | NÃO | fora da faixa vertical |
| 1021 | 444.00 | 46.00 | 344.42 | 343.73 | NÃO | fora da faixa vertical |
| 1022 | 443.00 | 46.00 | 344.58 | 343.73 | NÃO | fora da faixa vertical |
| 1023 | 442.00 | 45.00 | 345.73 | 344.73 | NÃO | fora da faixa vertical |
| 1024 | 441.00 | 44.00 | 346.88 | 345.73 | NÃO | fora da faixa vertical |
| 1025 | 440.00 | 44.00 | 347.05 | 345.73 | NÃO | fora da faixa vertical |
| 1026 | 439.00 | 43.00 | 348.21 | 346.73 | NÃO | fora da faixa vertical |
| 1027 | 438.00 | 43.00 | 348.38 | 346.73 | NÃO | fora da faixa vertical |
| 1028 | 437.00 | 42.00 | 349.54 | 347.73 | NÃO | fora da faixa vertical |
| 1029 | 436.00 | 41.00 | 350.71 | 348.73 | NÃO | fora da faixa vertical |
| 1030 | 435.00 | 41.00 | 350.89 | 348.73 | NÃO | fora da faixa vertical |
| 1031 | 434.00 | 40.00 | 352.05 | 349.73 | NÃO | fora da faixa vertical |
| 1032 | 433.00 | 39.00 | 353.22 | 350.73 | NÃO | fora da faixa vertical |
| 1033 | 432.00 | 39.00 | 353.41 | 350.73 | NÃO | fora da faixa vertical |
| 1034 | 431.00 | 38.00 | 354.58 | 351.73 | NÃO | fora da faixa vertical |
| 1035 | 430.00 | 38.00 | 354.77 | 351.73 | NÃO | fora da faixa vertical |
| 1036 | 429.00 | 37.00 | 355.95 | 352.73 | NÃO | fora da faixa vertical |
| 1037 | 428.00 | 37.00 | 356.15 | 352.73 | NÃO | fora da faixa vertical |
| 1038 | 427.00 | 36.00 | 357.33 | 353.73 | NÃO | fora da faixa vertical |
| 1039 | 426.00 | 36.00 | 357.53 | 353.73 | NÃO | fora da faixa vertical |
| 1040 | 425.00 | 35.00 | 358.72 | 354.73 | NÃO | fora da faixa vertical |
| 1041 | 424.00 | 35.00 | 358.92 | 354.73 | NÃO | fora da faixa vertical |
| 1042 | 423.00 | 34.00 | 360.11 | 355.73 | NÃO | fora da faixa vertical |
| 1043 | 422.00 | 34.00 | 360.32 | 355.73 | NÃO | fora da faixa vertical |
| 1044 | 421.00 | 33.00 | 361.51 | 356.73 | NÃO | fora da faixa vertical |
| 1045 | 420.00 | 33.00 | 361.73 | 356.73 | NÃO | fora da faixa vertical |
| 1046 | 419.00 | 32.00 | 362.93 | 357.73 | NÃO | fora da faixa vertical |
| 1047 | 418.00 | 32.00 | 363.15 | 357.73 | NÃO | fora da faixa vertical |
| 1048 | 417.00 | 31.00 | 364.35 | 358.73 | NÃO | fora da faixa vertical |
| 1049 | 416.00 | 31.00 | 364.57 | 358.73 | NÃO | fora da faixa vertical |
| 1050 | 415.00 | 30.00 | 365.78 | 359.73 | NÃO | fora da faixa vertical |
| 1051 | 414.00 | 30.00 | 366.01 | 359.73 | NÃO | fora da faixa vertical |
| 1052 | 413.00 | 29.00 | 367.21 | 360.73 | NÃO | fora da faixa vertical |
| 1053 | 412.00 | 29.00 | 367.45 | 360.73 | NÃO | fora da faixa vertical |
| 1054 | 411.00 | 28.00 | 368.66 | 361.73 | NÃO | fora da faixa vertical |
| 1055 | 410.00 | 28.00 | 368.90 | 361.73 | NÃO | fora da faixa vertical |
| 1056 | 409.00 | 28.00 | 369.14 | 361.73 | NÃO | fora da faixa vertical |
| 1057 | 408.00 | 27.00 | 370.35 | 362.73 | NÃO | fora da faixa vertical |
| 1058 | 407.00 | 27.00 | 370.60 | 362.73 | NÃO | fora da faixa vertical |
| 1059 | 406.00 | 27.00 | 370.85 | 362.73 | NÃO | fora da faixa vertical |
| 1060 | 405.00 | 26.00 | 372.07 | 363.73 | NÃO | fora da faixa vertical |
| 1061 | 404.00 | 26.00 | 372.32 | 363.73 | NÃO | fora da faixa vertical |
| 1062 | 403.00 | 25.00 | 373.55 | 364.73 | NÃO | fora da faixa vertical |
| 1063 | 402.00 | 25.00 | 373.80 | 364.73 | NÃO | fora da faixa vertical |
| 1064 | 401.00 | 25.00 | 374.07 | 364.73 | NÃO | fora da faixa vertical |
| 1065 | 400.00 | 24.00 | 375.29 | 365.73 | NÃO | fora da faixa vertical |
| 1066 | 399.00 | 24.00 | 375.56 | 365.73 | NÃO | fora da faixa vertical |
| 1067 | 398.00 | 24.00 | 375.83 | 365.73 | NÃO | fora da faixa vertical |
| 1068 | 397.00 | 23.00 | 377.06 | 366.73 | NÃO | fora da faixa vertical |
| 1069 | 396.00 | 23.00 | 377.33 | 366.73 | NÃO | fora da faixa vertical |
| 1070 | 395.00 | 23.00 | 377.60 | 366.73 | NÃO | fora da faixa vertical |
| 1071 | 394.00 | 22.00 | 378.84 | 367.73 | NÃO | fora da faixa vertical |
| 1072 | 393.00 | 22.00 | 379.12 | 367.73 | NÃO | fora da faixa vertical |
| 1073 | 392.00 | 22.00 | 379.40 | 367.73 | NÃO | fora da faixa vertical |
| 1074 | 391.00 | 21.00 | 380.64 | 368.73 | NÃO | fora da faixa vertical |
| 1075 | 390.00 | 21.00 | 380.93 | 368.73 | NÃO | fora da faixa vertical |
| 1076 | 389.00 | 21.00 | 381.22 | 368.73 | NÃO | fora da faixa vertical |
| 1077 | 388.00 | 21.00 | 381.50 | 368.73 | NÃO | fora da faixa vertical |
| 1078 | 387.00 | 20.00 | 382.75 | 369.73 | NÃO | fora da faixa vertical |
| 1079 | 386.00 | 20.00 | 383.05 | 369.73 | NÃO | fora da faixa vertical |
| 1080 | 385.00 | 20.00 | 383.34 | 369.73 | NÃO | fora da faixa vertical |
| 1081 | 384.00 | 19.00 | 384.60 | 370.73 | NÃO | fora da faixa vertical |
| 1082 | 383.00 | 19.00 | 384.90 | 370.73 | NÃO | fora da faixa vertical |
| 1083 | 382.00 | 19.00 | 385.20 | 370.73 | NÃO | fora da faixa vertical |
| 1084 | 381.00 | 19.00 | 385.50 | 370.73 | NÃO | fora da faixa vertical |
| 1085 | 380.00 | 18.00 | 386.76 | 371.73 | NÃO | fora da faixa vertical |
| 1086 | 379.00 | 18.00 | 387.07 | 371.73 | NÃO | fora da faixa vertical |
| 1087 | 378.00 | 18.00 | 387.38 | 371.73 | NÃO | fora da faixa vertical |
| 1088 | 377.00 | 18.00 | 387.70 | 371.73 | NÃO | fora da faixa vertical |
| 1089 | 376.00 | 17.00 | 388.96 | 372.73 | NÃO | fora da faixa vertical |
| 1090 | 375.00 | 17.00 | 389.28 | 372.73 | NÃO | fora da faixa vertical |
| 1091 | 374.00 | 17.00 | 389.60 | 372.73 | NÃO | fora da faixa vertical |
| 1092 | 373.00 | 17.00 | 389.92 | 372.73 | NÃO | fora da faixa vertical |
| 1093 | 372.00 | 17.00 | 390.24 | 372.73 | NÃO | fora da faixa vertical |
| 1094 | 371.00 | 16.00 | 391.52 | 373.73 | NÃO | fora da faixa vertical |
| 1095 | 370.00 | 16.00 | 391.84 | 373.73 | NÃO | fora da faixa vertical |
| 1096 | 369.00 | 16.00 | 392.17 | 373.73 | NÃO | fora da faixa vertical |
| 1097 | 368.00 | 16.00 | 392.51 | 373.73 | NÃO | fora da faixa vertical |
| 1098 | 367.00 | 16.00 | 392.84 | 373.73 | NÃO | fora da faixa vertical |
| 1099 | 366.00 | 15.00 | 394.12 | 374.73 | NÃO | fora da faixa vertical |
| 1100 | 365.00 | 15.00 | 394.46 | 374.73 | NÃO | fora da faixa vertical |
| 1101 | 364.00 | 15.00 | 394.80 | 374.73 | NÃO | fora da faixa vertical |
| 1102 | 363.00 | 15.00 | 395.14 | 374.73 | NÃO | fora da faixa vertical |
| 1103 | 362.00 | 15.00 | 395.49 | 374.73 | NÃO | fora da faixa vertical |
| 1104 | 361.00 | 15.00 | 395.83 | 374.73 | NÃO | fora da faixa vertical |
| 1105 | 360.00 | 15.00 | 396.18 | 374.73 | NÃO | fora da faixa vertical |
| 1106 | 359.00 | 15.00 | 396.54 | 374.73 | NÃO | fora da faixa vertical |
| 1107 | 358.00 | 14.00 | 397.83 | 375.73 | NÃO | fora da faixa vertical |
| 1108 | 357.00 | 14.00 | 398.18 | 375.73 | NÃO | fora da faixa vertical |
| 1109 | 356.00 | 14.00 | 398.54 | 375.73 | NÃO | fora da faixa vertical |
| 1110 | 355.00 | 14.00 | 398.90 | 375.73 | NÃO | fora da faixa vertical |
| 1111 | 354.00 | 14.00 | 399.26 | 375.73 | NÃO | fora da faixa vertical |
| 1112 | 353.00 | 14.00 | 399.62 | 375.73 | NÃO | fora da faixa vertical |
| 1113 | 352.00 | 14.00 | 399.99 | 375.73 | NÃO | fora da faixa vertical |
| 1114 | 351.00 | 14.00 | 400.36 | 375.73 | NÃO | fora da faixa vertical |
| 1115 | 350.00 | 14.00 | 400.73 | 375.73 | NÃO | fora da faixa vertical |
| 1116 | 349.00 | 14.00 | 401.10 | 375.73 | NÃO | fora da faixa vertical |
| 1117 | 348.00 | 13.00 | 402.41 | 376.73 | NÃO | fora da faixa vertical |
| 1118 | 347.00 | 13.00 | 402.78 | 376.73 | NÃO | fora da faixa vertical |
| 1119 | 346.00 | 13.00 | 403.16 | 376.73 | NÃO | fora da faixa vertical |
| 1120 | 345.00 | 13.00 | 403.54 | 376.73 | NÃO | fora da faixa vertical |
| 1121 | 344.00 | 13.00 | 403.92 | 376.73 | NÃO | fora da faixa vertical |
| 1122 | 343.00 | 13.00 | 404.31 | 376.73 | NÃO | fora da faixa vertical |
| 1123 | 342.00 | 13.00 | 404.69 | 376.73 | NÃO | fora da faixa vertical |
| 1124 | 341.00 | 13.00 | 405.08 | 376.73 | NÃO | fora da faixa vertical |
| 1125 | 340.00 | 13.00 | 405.48 | 376.73 | NÃO | fora da faixa vertical |
| 1126 | 339.00 | 13.00 | 405.87 | 376.73 | NÃO | fora da faixa vertical |
| 1127 | 338.00 | 13.00 | 406.26 | 376.73 | NÃO | fora da faixa vertical |
| 1128 | 337.00 | 13.00 | 406.66 | 376.73 | NÃO | fora da faixa vertical |
| 1129 | 336.00 | 13.00 | 407.06 | 376.73 | NÃO | fora da faixa vertical |
| 1130 | 335.00 | 13.00 | 407.46 | 376.73 | NÃO | fora da faixa vertical |
| 1131 | 334.00 | 13.00 | 407.87 | 376.73 | NÃO | fora da faixa vertical |
| 1132 | 333.00 | 13.00 | 408.27 | 376.73 | NÃO | fora da faixa vertical |
| 1133 | 332.00 | 13.00 | 408.68 | 376.73 | NÃO | fora da faixa vertical |
| 1134 | 331.00 | 13.00 | 409.09 | 376.73 | NÃO | fora da faixa vertical |
| 1135 | 330.00 | 13.00 | 409.50 | 376.73 | NÃO | fora da faixa vertical |
| 1136 | 329.00 | 13.00 | 409.91 | 376.73 | NÃO | fora da faixa vertical |
| 1137 | 328.00 | 13.00 | 410.33 | 376.73 | NÃO | fora da faixa vertical |
| 1138 | 327.00 | 13.00 | 410.75 | 376.73 | NÃO | fora da faixa vertical |
| 1139 | 326.00 | 13.00 | 411.17 | 376.73 | NÃO | fora da faixa vertical |
| 1140 | 325.00 | 13.00 | 411.59 | 376.73 | NÃO | fora da faixa vertical |
| 1141 | 324.00 | 13.00 | 412.01 | 376.73 | NÃO | fora da faixa vertical |
| 1142 | 323.00 | 13.00 | 412.44 | 376.73 | NÃO | fora da faixa vertical |
| 1143 | 322.00 | 13.00 | 412.87 | 376.73 | NÃO | fora da faixa vertical |
| 1144 | 321.00 | 13.00 | 413.30 | 376.73 | NÃO | fora da faixa vertical |
| 1145 | 320.00 | 13.00 | 413.73 | 376.73 | NÃO | fora da faixa vertical |
| 1146 | 319.00 | 13.00 | 414.16 | 376.73 | NÃO | fora da faixa vertical |
| 1147 | 318.00 | 13.00 | 414.60 | 376.73 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 559 | 333.00 | 386.00 | -166.00 | -3.73 |
| 560 | 334.00 | 386.00 | -165.00 | -3.73 |
| 561 | 335.00 | 386.00 | -164.00 | -3.73 |
| 562 | 336.00 | 386.00 | -163.00 | -3.73 |
| 563 | 337.00 | 386.00 | -162.00 | -3.73 |
| 564 | 338.00 | 386.00 | -161.00 | -3.73 |
| 565 | 339.00 | 386.00 | -160.00 | -3.73 |
| 566 | 340.00 | 386.00 | -159.00 | -3.73 |
| 567 | 341.00 | 386.00 | -158.00 | -3.73 |
| 568 | 342.00 | 386.00 | -157.00 | -3.73 |
| 569 | 343.00 | 386.00 | -156.00 | -3.73 |
| 570 | 344.00 | 386.00 | -155.00 | -3.73 |
| 571 | 345.00 | 386.00 | -154.00 | -3.73 |
| 572 | 346.00 | 386.00 | -153.00 | -3.73 |
| 573 | 347.00 | 386.00 | -152.00 | -3.73 |
| 574 | 348.00 | 386.00 | -151.00 | -3.73 |
| 575 | 349.00 | 386.00 | -150.00 | -3.73 |
| 576 | 350.00 | 386.00 | -149.00 | -3.73 |
| 577 | 351.00 | 386.00 | -148.00 | -3.73 |
| 578 | 352.00 | 386.00 | -147.00 | -3.73 |
| 579 | 353.00 | 386.00 | -146.00 | -3.73 |
| 580 | 354.00 | 386.00 | -145.00 | -3.73 |
| 581 | 355.00 | 386.00 | -144.00 | -3.73 |
| 582 | 356.00 | 386.00 | -143.00 | -3.73 |
| 583 | 357.00 | 386.00 | -142.00 | -3.73 |
| 584 | 358.00 | 386.00 | -141.00 | -3.73 |
| 585 | 359.00 | 386.00 | -140.00 | -3.73 |
| 586 | 360.00 | 386.00 | -139.00 | -3.73 |
| 587 | 361.00 | 386.00 | -138.00 | -3.73 |
| 588 | 362.00 | 386.00 | -137.00 | -3.73 |
| 589 | 363.00 | 386.00 | -136.00 | -3.73 |
| 590 | 364.00 | 386.00 | -135.00 | -3.73 |
| 591 | 365.00 | 386.00 | -134.00 | -3.73 |
| 592 | 366.00 | 386.00 | -133.00 | -3.73 |
| 593 | 367.00 | 386.00 | -132.00 | -3.73 |
| 594 | 368.00 | 386.00 | -131.00 | -3.73 |
| 595 | 369.00 | 386.00 | -130.00 | -3.73 |
| 596 | 370.00 | 386.00 | -129.00 | -3.73 |
| 597 | 371.00 | 386.00 | -128.00 | -3.73 |
| 598 | 372.00 | 386.00 | -127.00 | -3.73 |
| 599 | 373.00 | 386.00 | -126.00 | -3.73 |
| 600 | 374.00 | 386.00 | -125.00 | -3.73 |
| 601 | 375.00 | 386.00 | -124.00 | -3.73 |
| 602 | 376.00 | 386.00 | -123.00 | -3.73 |
| 603 | 377.00 | 386.00 | -122.00 | -3.73 |
| 604 | 378.00 | 386.00 | -121.00 | -3.73 |
| 605 | 379.00 | 386.00 | -120.00 | -3.73 |
| 606 | 380.00 | 386.00 | -119.00 | -3.73 |
| 607 | 381.00 | 386.00 | -118.00 | -3.73 |
| 608 | 382.00 | 386.00 | -117.00 | -3.73 |
| 609 | 383.00 | 386.00 | -116.00 | -3.73 |
| 610 | 384.00 | 386.00 | -115.00 | -3.73 |
| 611 | 385.00 | 386.00 | -114.00 | -3.73 |
| 612 | 386.00 | 386.00 | -113.00 | -3.73 |
| 613 | 387.00 | 386.00 | -112.00 | -3.73 |
| 614 | 388.00 | 386.00 | -111.00 | -3.73 |
| 615 | 389.00 | 386.00 | -110.00 | -3.73 |
| 616 | 390.00 | 386.00 | -109.00 | -3.73 |
| 617 | 391.00 | 386.00 | -108.00 | -3.73 |
| 618 | 392.00 | 386.00 | -107.00 | -3.73 |
| 619 | 393.00 | 386.00 | -106.00 | -3.73 |
| 620 | 394.00 | 386.00 | -105.00 | -3.73 |
| 621 | 395.00 | 386.00 | -104.00 | -3.73 |
| 622 | 396.00 | 386.00 | -103.00 | -3.73 |
| 623 | 397.00 | 386.00 | -102.00 | -3.73 |
| 624 | 398.00 | 386.00 | -101.00 | -3.73 |
| 625 | 399.00 | 386.00 | -100.00 | -3.73 |
| 626 | 400.00 | 386.00 | -99.00 | -3.73 |
| 627 | 401.00 | 386.00 | -98.00 | -3.73 |
| 628 | 402.00 | 386.00 | -97.00 | -3.73 |
| 629 | 403.00 | 386.00 | -96.00 | -3.73 |
| 630 | 404.00 | 386.00 | -95.00 | -3.73 |
| 631 | 405.00 | 386.00 | -94.00 | -3.73 |
| 632 | 406.00 | 386.00 | -93.00 | -3.73 |
| 633 | 407.00 | 386.00 | -92.00 | -3.73 |
| 634 | 408.00 | 386.00 | -91.00 | -3.73 |
| 635 | 409.00 | 386.00 | -90.00 | -3.73 |
| 636 | 410.00 | 386.00 | -89.00 | -3.73 |
| 637 | 411.00 | 386.00 | -88.00 | -3.73 |
| 638 | 412.00 | 386.00 | -87.00 | -3.73 |
| 639 | 413.00 | 386.00 | -86.00 | -3.73 |
| 640 | 414.00 | 386.00 | -85.00 | -3.73 |
| 641 | 415.00 | 386.00 | -84.00 | -3.73 |
| 642 | 416.00 | 386.00 | -83.00 | -3.73 |
| 643 | 417.00 | 386.00 | -82.00 | -3.73 |
| 644 | 418.00 | 386.00 | -81.00 | -3.73 |
| 645 | 419.00 | 386.00 | -80.00 | -3.73 |
| 646 | 420.00 | 386.00 | -79.00 | -3.73 |
| 647 | 421.00 | 386.00 | -78.00 | -3.73 |
| 648 | 422.00 | 386.00 | -77.00 | -3.73 |
| 649 | 423.00 | 386.00 | -76.00 | -3.73 |
| 650 | 424.00 | 386.00 | -75.00 | -3.73 |
| 651 | 425.00 | 386.00 | -74.00 | -3.73 |
| 652 | 426.00 | 386.00 | -73.00 | -3.73 |
| 653 | 427.00 | 386.00 | -72.00 | -3.73 |
| 654 | 428.00 | 386.00 | -71.00 | -3.73 |
| 655 | 429.00 | 386.00 | -70.00 | -3.73 |
| 656 | 430.00 | 386.00 | -69.00 | -3.73 |
| 657 | 431.00 | 386.00 | -68.00 | -3.73 |
| 658 | 432.00 | 386.00 | -67.00 | -3.73 |
| 659 | 433.00 | 386.00 | -66.00 | -3.73 |
| 660 | 434.00 | 386.00 | -65.00 | -3.73 |
| 661 | 435.00 | 386.00 | -64.00 | -3.73 |
| 662 | 436.00 | 386.00 | -63.00 | -3.73 |
| 663 | 437.00 | 386.00 | -62.00 | -3.73 |
| 664 | 438.00 | 386.00 | -61.00 | -3.73 |
| 665 | 439.00 | 386.00 | -60.00 | -3.73 |
| 666 | 440.00 | 386.00 | -59.00 | -3.73 |
| 667 | 441.00 | 386.00 | -58.00 | -3.73 |
| 668 | 442.00 | 386.00 | -57.00 | -3.73 |
| 669 | 443.00 | 386.00 | -56.00 | -3.73 |
| 670 | 444.00 | 385.00 | -55.00 | -4.73 |
| 671 | 445.00 | 384.00 | -54.00 | -5.73 |
| 672 | 446.00 | 384.00 | -53.00 | -5.73 |
| 673 | 447.00 | 383.00 | -52.00 | -6.73 |
| 674 | 448.00 | 382.00 | -51.00 | -7.73 |
| 675 | 449.00 | 382.00 | -50.00 | -7.73 |
| 676 | 450.00 | 381.00 | -49.00 | -8.73 |
| 677 | 451.00 | 380.00 | -48.00 | -9.73 |
| 678 | 452.00 | 379.00 | -47.00 | -10.73 |
| 679 | 453.00 | 379.00 | -46.00 | -10.73 |
| 680 | 454.00 | 378.00 | -45.00 | -11.73 |
| 681 | 455.00 | 377.00 | -44.00 | -12.73 |
| 682 | 456.00 | 376.00 | -43.00 | -13.73 |
| 683 | 457.00 | 376.00 | -42.00 | -13.73 |
| 684 | 458.00 | 375.00 | -41.00 | -14.73 |
| 685 | 459.00 | 374.00 | -40.00 | -15.73 |
| 686 | 460.00 | 373.00 | -39.00 | -16.73 |
| 687 | 461.00 | 373.00 | -38.00 | -16.73 |
| 688 | 462.00 | 372.00 | -37.00 | -17.73 |
| 689 | 463.00 | 371.00 | -36.00 | -18.73 |
| 690 | 464.00 | 370.00 | -35.00 | -19.73 |
| 691 | 465.00 | 369.00 | -34.00 | -20.73 |
| 692 | 466.00 | 368.00 | -33.00 | -21.73 |
| 693 | 467.00 | 367.00 | -32.00 | -22.73 |
| 694 | 468.00 | 366.00 | -31.00 | -23.73 |
| 695 | 469.00 | 365.00 | -30.00 | -24.73 |
| 696 | 470.00 | 364.00 | -29.00 | -25.73 |
| 697 | 471.00 | 363.00 | -28.00 | -26.73 |
| 698 | 472.00 | 363.00 | -27.00 | -26.73 |
| 699 | 473.00 | 362.00 | -26.00 | -27.73 |
| 700 | 474.00 | 361.00 | -25.00 | -28.73 |
| 701 | 475.00 | 360.00 | -24.00 | -29.73 |
| 702 | 476.00 | 359.00 | -23.00 | -30.73 |
| 703 | 477.00 | 358.00 | -22.00 | -31.73 |
| 704 | 478.00 | 357.00 | -21.00 | -32.73 |
| 705 | 479.00 | 356.00 | -20.00 | -33.73 |
| 706 | 480.00 | 355.00 | -19.00 | -34.73 |
| 707 | 481.00 | 354.00 | -18.00 | -35.73 |
| 708 | 482.00 | 353.00 | -17.00 | -36.73 |
| 709 | 483.00 | 352.00 | -16.00 | -37.73 |
| 710 | 483.00 | 351.00 | -16.00 | -38.73 |
| 711 | 484.00 | 350.00 | -15.00 | -39.73 |
| 712 | 485.00 | 349.00 | -14.00 | -40.73 |
| 713 | 486.00 | 348.00 | -13.00 | -41.73 |
| 714 | 487.00 | 347.00 | -12.00 | -42.73 |
| 715 | 488.00 | 346.00 | -11.00 | -43.73 |
| 716 | 489.00 | 345.00 | -10.00 | -44.73 |
| 717 | 490.00 | 344.00 | -9.00 | -45.73 |
| 718 | 490.00 | 343.00 | -9.00 | -46.73 |
| 719 | 491.00 | 342.00 | -8.00 | -47.73 |
| 720 | 492.00 | 341.00 | -7.00 | -48.73 |
| 721 | 493.00 | 340.00 | -6.00 | -49.73 |
| 722 | 493.00 | 339.00 | -6.00 | -50.73 |
| 723 | 494.00 | 338.00 | -5.00 | -51.73 |
| 724 | 495.00 | 337.00 | -4.00 | -52.73 |
| 725 | 496.00 | 336.00 | -3.00 | -53.73 |
| 726 | 496.00 | 335.00 | -3.00 | -54.73 |
| 727 | 497.00 | 334.00 | -2.00 | -55.73 |
| 728 | 498.00 | 333.00 | -1.00 | -56.73 |
| 729 | 499.00 | 332.00 | 0.00 | -57.73 |
| 730 | 499.00 | 331.00 | 0.00 | -58.73 |
| 731 | 500.00 | 330.00 | 1.00 | -59.73 |
| 732 | 501.00 | 329.00 | 2.00 | -60.73 |
| 733 | 501.00 | 328.00 | 2.00 | -61.73 |
| 734 | 502.00 | 327.00 | 3.00 | -62.73 |
| 735 | 503.00 | 326.00 | 4.00 | -63.73 |
| 736 | 503.00 | 325.00 | 4.00 | -64.73 |
| 737 | 504.00 | 324.00 | 5.00 | -65.73 |
| 738 | 504.00 | 323.00 | 5.00 | -66.73 |
| 739 | 505.00 | 322.00 | 6.00 | -67.73 |
| 740 | 506.00 | 321.00 | 7.00 | -68.73 |
| 741 | 506.00 | 320.00 | 7.00 | -69.73 |
| 742 | 507.00 | 319.00 | 8.00 | -70.73 |
| 743 | 507.00 | 318.00 | 8.00 | -71.73 |
| 744 | 508.00 | 317.00 | 9.00 | -72.73 |
| 745 | 509.00 | 316.00 | 10.00 | -73.73 |
| 746 | 509.00 | 315.00 | 10.00 | -74.73 |
| 747 | 510.00 | 314.00 | 11.00 | -75.73 |
| 748 | 510.00 | 313.00 | 11.00 | -76.73 |
| 749 | 511.00 | 312.00 | 12.00 | -77.73 |
| 750 | 511.00 | 311.00 | 12.00 | -78.73 |
| 751 | 512.00 | 310.00 | 13.00 | -79.73 |
| 752 | 512.00 | 309.00 | 13.00 | -80.73 |
| 753 | 513.00 | 308.00 | 14.00 | -81.73 |
| 754 | 513.00 | 307.00 | 14.00 | -82.73 |
| 755 | 514.00 | 306.00 | 15.00 | -83.73 |
| 756 | 514.00 | 305.00 | 15.00 | -84.73 |
| 757 | 515.00 | 304.00 | 16.00 | -85.73 |
| 758 | 515.00 | 303.00 | 16.00 | -86.73 |
| 759 | 516.00 | 302.00 | 17.00 | -87.73 |
| 760 | 516.00 | 301.00 | 17.00 | -88.73 |
| 761 | 517.00 | 300.00 | 18.00 | -89.73 |
| 762 | 517.00 | 299.00 | 18.00 | -90.73 |
| 763 | 518.00 | 298.00 | 19.00 | -91.73 |
| 764 | 518.00 | 297.00 | 19.00 | -92.73 |
| 765 | 519.00 | 296.00 | 20.00 | -93.73 |
| 766 | 519.00 | 295.00 | 20.00 | -94.73 |
| 767 | 520.00 | 294.00 | 21.00 | -95.73 |
| 768 | 520.00 | 293.00 | 21.00 | -96.73 |
| 769 | 521.00 | 292.00 | 22.00 | -97.73 |
| 770 | 521.00 | 291.00 | 22.00 | -98.73 |
| 771 | 521.00 | 290.00 | 22.00 | -99.73 |
| 772 | 522.00 | 289.00 | 23.00 | -100.73 |
| 773 | 522.00 | 288.00 | 23.00 | -101.73 |
| 774 | 522.00 | 287.00 | 23.00 | -102.73 |
| 775 | 523.00 | 286.00 | 24.00 | -103.73 |
| 776 | 523.00 | 285.00 | 24.00 | -104.73 |
| 777 | 524.00 | 284.00 | 25.00 | -105.73 |
| 778 | 524.00 | 283.00 | 25.00 | -106.73 |
| 779 | 524.00 | 282.00 | 25.00 | -107.73 |
| 780 | 525.00 | 281.00 | 26.00 | -108.73 |
| 781 | 525.00 | 280.00 | 26.00 | -109.73 |
| 782 | 525.00 | 279.00 | 26.00 | -110.73 |
| 783 | 526.00 | 278.00 | 27.00 | -111.73 |
| 784 | 526.00 | 277.00 | 27.00 | -112.73 |
| 785 | 526.00 | 276.00 | 27.00 | -113.73 |
| 786 | 526.00 | 275.00 | 27.00 | -114.73 |
| 787 | 527.00 | 274.00 | 28.00 | -115.73 |
| 788 | 527.00 | 273.00 | 28.00 | -116.73 |
| 789 | 527.00 | 272.00 | 28.00 | -117.73 |
| 790 | 528.00 | 271.00 | 29.00 | -118.73 |
| 791 | 528.00 | 270.00 | 29.00 | -119.73 |
| 792 | 528.00 | 269.00 | 29.00 | -120.73 |
| 793 | 528.00 | 268.00 | 29.00 | -121.73 |
| 794 | 529.00 | 267.00 | 30.00 | -122.73 |
| 795 | 529.00 | 266.00 | 30.00 | -123.73 |
| 796 | 529.00 | 265.00 | 30.00 | -124.73 |
| 797 | 529.00 | 264.00 | 30.00 | -125.73 |
| 798 | 530.00 | 263.00 | 31.00 | -126.73 |
| 799 | 530.00 | 262.00 | 31.00 | -127.73 |
| 800 | 530.00 | 261.00 | 31.00 | -128.73 |
| 801 | 530.00 | 260.00 | 31.00 | -129.73 |
| 802 | 530.00 | 259.00 | 31.00 | -130.73 |
| 803 | 531.00 | 258.00 | 32.00 | -131.73 |
| 804 | 531.00 | 257.00 | 32.00 | -132.73 |
| 805 | 531.00 | 256.00 | 32.00 | -133.73 |
| 806 | 531.00 | 255.00 | 32.00 | -134.73 |
| 807 | 532.00 | 254.00 | 33.00 | -135.73 |
| 808 | 532.00 | 253.00 | 33.00 | -136.73 |
| 809 | 532.00 | 252.00 | 33.00 | -137.73 |
| 810 | 532.00 | 251.00 | 33.00 | -138.73 |
| 811 | 532.00 | 250.00 | 33.00 | -139.73 |
| 812 | 533.00 | 249.00 | 34.00 | -140.73 |
| 813 | 533.00 | 248.00 | 34.00 | -141.73 |
| 814 | 533.00 | 247.00 | 34.00 | -142.73 |
| 815 | 533.00 | 246.00 | 34.00 | -143.73 |
| 816 | 533.00 | 245.00 | 34.00 | -144.73 |
| 817 | 533.00 | 244.00 | 34.00 | -145.73 |
| 818 | 533.00 | 243.00 | 34.00 | -146.73 |
| 819 | 534.00 | 242.00 | 35.00 | -147.73 |
| 820 | 534.00 | 241.00 | 35.00 | -148.73 |
| 821 | 534.00 | 240.00 | 35.00 | -149.73 |
| 822 | 534.00 | 239.00 | 35.00 | -150.73 |
| 823 | 534.00 | 238.00 | 35.00 | -151.73 |
| 824 | 534.00 | 237.00 | 35.00 | -152.73 |
| 825 | 534.00 | 236.00 | 35.00 | -153.73 |
| 826 | 534.00 | 235.00 | 35.00 | -154.73 |
| 827 | 535.00 | 234.00 | 36.00 | -155.73 |
| 828 | 535.00 | 233.00 | 36.00 | -156.73 |
| 829 | 535.00 | 232.00 | 36.00 | -157.73 |
| 830 | 535.00 | 231.00 | 36.00 | -158.73 |
| 831 | 535.00 | 230.00 | 36.00 | -159.73 |
| 832 | 535.00 | 229.00 | 36.00 | -160.73 |
| 833 | 535.00 | 228.00 | 36.00 | -161.73 |
| 834 | 535.00 | 227.00 | 36.00 | -162.73 |
| 835 | 535.00 | 226.00 | 36.00 | -163.73 |
| 836 | 535.00 | 225.00 | 36.00 | -164.73 |
| 837 | 535.00 | 224.00 | 36.00 | -165.73 |
| 838 | 535.00 | 223.00 | 36.00 | -166.73 |
| 839 | 535.00 | 222.00 | 36.00 | -167.73 |
| 840 | 535.00 | 221.00 | 36.00 | -168.73 |
| 841 | 535.00 | 220.00 | 36.00 | -169.73 |
| 842 | 535.00 | 219.00 | 36.00 | -170.73 |
| 843 | 535.00 | 218.00 | 36.00 | -171.73 |
| 844 | 535.00 | 217.00 | 36.00 | -172.73 |
| 845 | 535.00 | 216.00 | 36.00 | -173.73 |
| 846 | 535.00 | 215.00 | 36.00 | -174.73 |
| 847 | 535.00 | 214.00 | 36.00 | -175.73 |
| 848 | 535.00 | 213.00 | 36.00 | -176.73 |
| 849 | 535.00 | 212.00 | 36.00 | -177.73 |
| 850 | 535.00 | 211.00 | 36.00 | -178.73 |
| 851 | 535.00 | 210.00 | 36.00 | -179.73 |
| 852 | 535.00 | 209.00 | 36.00 | -180.73 |
| 853 | 535.00 | 208.00 | 36.00 | -181.73 |
| 854 | 535.00 | 207.00 | 36.00 | -182.73 |
| 855 | 535.00 | 206.00 | 36.00 | -183.73 |
| 856 | 535.00 | 205.00 | 36.00 | -184.73 |
| 857 | 535.00 | 204.00 | 36.00 | -185.73 |
| 858 | 535.00 | 203.00 | 36.00 | -186.73 |
| 859 | 535.00 | 202.00 | 36.00 | -187.73 |
| 860 | 535.00 | 201.00 | 36.00 | -188.73 |
| 861 | 535.00 | 200.00 | 36.00 | -189.73 |
| 862 | 535.00 | 199.00 | 36.00 | -190.73 |
| 863 | 535.00 | 198.00 | 36.00 | -191.73 |
| 864 | 534.00 | 197.00 | 35.00 | -192.73 |
| 865 | 534.00 | 196.00 | 35.00 | -193.73 |
| 866 | 534.00 | 195.00 | 35.00 | -194.73 |
| 867 | 534.00 | 194.00 | 35.00 | -195.73 |
| 868 | 534.00 | 193.00 | 35.00 | -196.73 |
| 869 | 534.00 | 192.00 | 35.00 | -197.73 |
| 870 | 534.00 | 191.00 | 35.00 | -198.73 |
| 871 | 534.00 | 190.00 | 35.00 | -199.73 |
| 872 | 533.00 | 189.00 | 34.00 | -200.73 |
| 873 | 533.00 | 188.00 | 34.00 | -201.73 |
| 874 | 533.00 | 187.00 | 34.00 | -202.73 |
| 875 | 533.00 | 186.00 | 34.00 | -203.73 |
| 876 | 533.00 | 185.00 | 34.00 | -204.73 |

- primeiro índice: 559
- último índice: 876
- quantidade: 318
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![30_geo dir](audit_outputs/75_geo_dir_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![30_geo dir polyfit](audit_outputs/75_geo_dir_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

## Imagem: 50_geo

### Lado: esq

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 1145
- ponto de contato recebido: [92.0, 376.0]
- baseline_y: 376.0
- baseline_ajustada: 379.29
- lado solicitado: esq
- largura da região: 180 px
- altura da gota: 329.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 264.00 | 47.00 | 371.25 | 332.29 | NÃO | fora da faixa vertical |
| 1 | 263.00 | 48.00 | 369.90 | 331.29 | NÃO | fora da faixa vertical |
| 2 | 262.00 | 48.00 | 369.44 | 331.29 | NÃO | fora da faixa vertical |
| 3 | 261.00 | 48.00 | 368.98 | 331.29 | NÃO | fora da faixa vertical |
| 4 | 260.00 | 48.00 | 368.52 | 331.29 | NÃO | fora da faixa vertical |
| 5 | 259.00 | 48.00 | 368.07 | 331.29 | NÃO | fora da faixa vertical |
| 6 | 258.00 | 48.00 | 367.61 | 331.29 | NÃO | fora da faixa vertical |
| 7 | 257.00 | 48.00 | 367.16 | 331.29 | NÃO | fora da faixa vertical |
| 8 | 256.00 | 48.00 | 366.72 | 331.29 | NÃO | fora da faixa vertical |
| 9 | 255.00 | 49.00 | 365.37 | 330.29 | NÃO | fora da faixa vertical |
| 10 | 254.00 | 49.00 | 364.93 | 330.29 | NÃO | fora da faixa vertical |
| 11 | 253.00 | 49.00 | 364.49 | 330.29 | NÃO | fora da faixa vertical |
| 12 | 252.00 | 49.00 | 364.05 | 330.29 | NÃO | fora da faixa vertical |
| 13 | 251.00 | 49.00 | 363.61 | 330.29 | NÃO | fora da faixa vertical |
| 14 | 250.00 | 49.00 | 363.17 | 330.29 | NÃO | fora da faixa vertical |
| 15 | 249.00 | 49.00 | 362.74 | 330.29 | NÃO | fora da faixa vertical |
| 16 | 248.00 | 49.00 | 362.31 | 330.29 | NÃO | fora da faixa vertical |
| 17 | 247.00 | 50.00 | 360.97 | 329.29 | NÃO | fora da faixa vertical |
| 18 | 246.00 | 50.00 | 360.54 | 329.29 | NÃO | fora da faixa vertical |
| 19 | 245.00 | 50.00 | 360.12 | 329.29 | NÃO | fora da faixa vertical |
| 20 | 244.00 | 50.00 | 359.69 | 329.29 | NÃO | fora da faixa vertical |
| 21 | 243.00 | 50.00 | 359.27 | 329.29 | NÃO | fora da faixa vertical |
| 22 | 242.00 | 51.00 | 357.95 | 328.29 | NÃO | fora da faixa vertical |
| 23 | 241.00 | 51.00 | 357.53 | 328.29 | NÃO | fora da faixa vertical |
| 24 | 240.00 | 51.00 | 357.11 | 328.29 | NÃO | fora da faixa vertical |
| 25 | 239.00 | 51.00 | 356.70 | 328.29 | NÃO | fora da faixa vertical |
| 26 | 238.00 | 51.00 | 356.29 | 328.29 | NÃO | fora da faixa vertical |
| 27 | 237.00 | 52.00 | 354.97 | 327.29 | NÃO | fora da faixa vertical |
| 28 | 236.00 | 52.00 | 354.56 | 327.29 | NÃO | fora da faixa vertical |
| 29 | 235.00 | 52.00 | 354.15 | 327.29 | NÃO | fora da faixa vertical |
| 30 | 234.00 | 52.00 | 353.75 | 327.29 | NÃO | fora da faixa vertical |
| 31 | 233.00 | 52.00 | 353.35 | 327.29 | NÃO | fora da faixa vertical |
| 32 | 232.00 | 53.00 | 352.04 | 326.29 | NÃO | fora da faixa vertical |
| 33 | 231.00 | 53.00 | 351.64 | 326.29 | NÃO | fora da faixa vertical |
| 34 | 230.00 | 53.00 | 351.24 | 326.29 | NÃO | fora da faixa vertical |
| 35 | 229.00 | 53.00 | 350.85 | 326.29 | NÃO | fora da faixa vertical |
| 36 | 228.00 | 54.00 | 349.54 | 325.29 | NÃO | fora da faixa vertical |
| 37 | 227.00 | 54.00 | 349.15 | 325.29 | NÃO | fora da faixa vertical |
| 38 | 226.00 | 54.00 | 348.77 | 325.29 | NÃO | fora da faixa vertical |
| 39 | 225.00 | 54.00 | 348.39 | 325.29 | NÃO | fora da faixa vertical |
| 40 | 224.00 | 55.00 | 347.08 | 324.29 | NÃO | fora da faixa vertical |
| 41 | 223.00 | 55.00 | 346.70 | 324.29 | NÃO | fora da faixa vertical |
| 42 | 222.00 | 55.00 | 346.32 | 324.29 | NÃO | fora da faixa vertical |
| 43 | 221.00 | 56.00 | 345.02 | 323.29 | NÃO | fora da faixa vertical |
| 44 | 220.00 | 56.00 | 344.65 | 323.29 | NÃO | fora da faixa vertical |
| 45 | 219.00 | 56.00 | 344.28 | 323.29 | NÃO | fora da faixa vertical |
| 46 | 218.00 | 56.00 | 343.91 | 323.29 | NÃO | fora da faixa vertical |
| 47 | 217.00 | 57.00 | 342.62 | 322.29 | NÃO | fora da faixa vertical |
| 48 | 216.00 | 57.00 | 342.25 | 322.29 | NÃO | fora da faixa vertical |
| 49 | 215.00 | 57.00 | 341.89 | 322.29 | NÃO | fora da faixa vertical |
| 50 | 214.00 | 58.00 | 340.60 | 321.29 | NÃO | fora da faixa vertical |
| 51 | 213.00 | 58.00 | 340.24 | 321.29 | NÃO | fora da faixa vertical |
| 52 | 212.00 | 58.00 | 339.89 | 321.29 | NÃO | fora da faixa vertical |
| 53 | 211.00 | 59.00 | 338.60 | 320.29 | NÃO | fora da faixa vertical |
| 54 | 210.00 | 59.00 | 338.25 | 320.29 | NÃO | fora da faixa vertical |
| 55 | 209.00 | 60.00 | 336.96 | 319.29 | NÃO | fora da faixa vertical |
| 56 | 208.00 | 60.00 | 336.62 | 319.29 | NÃO | fora da faixa vertical |
| 57 | 207.00 | 60.00 | 336.28 | 319.29 | NÃO | fora da faixa vertical |
| 58 | 206.00 | 61.00 | 334.99 | 318.29 | NÃO | fora da faixa vertical |
| 59 | 205.00 | 61.00 | 334.66 | 318.29 | NÃO | fora da faixa vertical |
| 60 | 204.00 | 61.00 | 334.32 | 318.29 | NÃO | fora da faixa vertical |
| 61 | 203.00 | 62.00 | 333.04 | 317.29 | NÃO | fora da faixa vertical |
| 62 | 202.00 | 62.00 | 332.71 | 317.29 | NÃO | fora da faixa vertical |
| 63 | 201.00 | 63.00 | 331.44 | 316.29 | NÃO | fora da faixa vertical |
| 64 | 200.00 | 63.00 | 331.11 | 316.29 | NÃO | fora da faixa vertical |
| 65 | 199.00 | 63.00 | 330.78 | 316.29 | NÃO | fora da faixa vertical |
| 66 | 198.00 | 64.00 | 329.51 | 315.29 | NÃO | fora da faixa vertical |
| 67 | 197.00 | 64.00 | 329.19 | 315.29 | NÃO | fora da faixa vertical |
| 68 | 196.00 | 65.00 | 327.93 | 314.29 | NÃO | fora da faixa vertical |
| 69 | 195.00 | 65.00 | 327.61 | 314.29 | NÃO | fora da faixa vertical |
| 70 | 194.00 | 66.00 | 326.35 | 313.29 | NÃO | fora da faixa vertical |
| 71 | 193.00 | 66.00 | 326.04 | 313.29 | NÃO | fora da faixa vertical |
| 72 | 192.00 | 67.00 | 324.78 | 312.29 | NÃO | fora da faixa vertical |
| 73 | 191.00 | 67.00 | 324.47 | 312.29 | NÃO | fora da faixa vertical |
| 74 | 190.00 | 68.00 | 323.22 | 311.29 | NÃO | fora da faixa vertical |
| 75 | 189.00 | 68.00 | 322.91 | 311.29 | NÃO | fora da faixa vertical |
| 76 | 188.00 | 69.00 | 321.66 | 310.29 | NÃO | fora da faixa vertical |
| 77 | 187.00 | 69.00 | 321.36 | 310.29 | NÃO | fora da faixa vertical |
| 78 | 186.00 | 70.00 | 320.11 | 309.29 | NÃO | fora da faixa vertical |
| 79 | 185.00 | 70.00 | 319.82 | 309.29 | NÃO | fora da faixa vertical |
| 80 | 184.00 | 71.00 | 318.57 | 308.29 | NÃO | fora da faixa vertical |
| 81 | 183.00 | 71.00 | 318.29 | 308.29 | NÃO | fora da faixa vertical |
| 82 | 182.00 | 72.00 | 317.04 | 307.29 | NÃO | fora da faixa vertical |
| 83 | 181.00 | 72.00 | 316.76 | 307.29 | NÃO | fora da faixa vertical |
| 84 | 180.00 | 73.00 | 315.52 | 306.29 | NÃO | fora da faixa vertical |
| 85 | 179.00 | 74.00 | 314.28 | 305.29 | NÃO | fora da faixa vertical |
| 86 | 178.00 | 74.00 | 314.01 | 305.29 | NÃO | fora da faixa vertical |
| 87 | 177.00 | 75.00 | 312.77 | 304.29 | NÃO | fora da faixa vertical |
| 88 | 176.00 | 75.00 | 312.50 | 304.29 | NÃO | fora da faixa vertical |
| 89 | 175.00 | 76.00 | 311.27 | 303.29 | NÃO | fora da faixa vertical |
| 90 | 174.00 | 77.00 | 310.04 | 302.29 | NÃO | fora da faixa vertical |
| 91 | 173.00 | 77.00 | 309.78 | 302.29 | NÃO | fora da faixa vertical |
| 92 | 172.00 | 78.00 | 308.55 | 301.29 | NÃO | fora da faixa vertical |
| 93 | 171.00 | 78.00 | 308.29 | 301.29 | NÃO | fora da faixa vertical |
| 94 | 170.00 | 79.00 | 307.07 | 300.29 | NÃO | fora da faixa vertical |
| 95 | 169.00 | 80.00 | 305.85 | 299.29 | NÃO | fora da faixa vertical |
| 96 | 168.00 | 80.00 | 305.60 | 299.29 | NÃO | fora da faixa vertical |
| 97 | 167.00 | 81.00 | 304.38 | 298.29 | NÃO | fora da faixa vertical |
| 98 | 166.00 | 82.00 | 303.17 | 297.29 | NÃO | fora da faixa vertical |
| 99 | 165.00 | 82.00 | 302.93 | 297.29 | NÃO | fora da faixa vertical |
| 100 | 164.00 | 83.00 | 301.72 | 296.29 | NÃO | fora da faixa vertical |
| 101 | 163.00 | 84.00 | 300.51 | 295.29 | NÃO | fora da faixa vertical |
| 102 | 162.00 | 85.00 | 299.30 | 294.29 | NÃO | fora da faixa vertical |
| 103 | 161.00 | 85.00 | 299.07 | 294.29 | NÃO | fora da faixa vertical |
| 104 | 160.00 | 86.00 | 297.87 | 293.29 | NÃO | fora da faixa vertical |
| 105 | 159.00 | 87.00 | 296.66 | 292.29 | NÃO | fora da faixa vertical |
| 106 | 158.00 | 88.00 | 295.47 | 291.29 | NÃO | fora da faixa vertical |
| 107 | 157.00 | 88.00 | 295.24 | 291.29 | NÃO | fora da faixa vertical |
| 108 | 156.00 | 89.00 | 294.05 | 290.29 | NÃO | fora da faixa vertical |
| 109 | 155.00 | 90.00 | 292.86 | 289.29 | NÃO | fora da faixa vertical |
| 110 | 154.00 | 91.00 | 291.67 | 288.29 | NÃO | fora da faixa vertical |
| 111 | 153.00 | 91.00 | 291.45 | 288.29 | NÃO | fora da faixa vertical |
| 112 | 152.00 | 92.00 | 290.27 | 287.29 | NÃO | fora da faixa vertical |
| 113 | 151.00 | 93.00 | 289.08 | 286.29 | NÃO | fora da faixa vertical |
| 114 | 150.00 | 94.00 | 287.90 | 285.29 | NÃO | fora da faixa vertical |
| 115 | 149.00 | 95.00 | 286.72 | 284.29 | NÃO | fora da faixa vertical |
| 116 | 148.00 | 95.00 | 286.53 | 284.29 | NÃO | fora da faixa vertical |
| 117 | 147.00 | 96.00 | 285.35 | 283.29 | NÃO | fora da faixa vertical |
| 118 | 146.00 | 97.00 | 284.18 | 282.29 | NÃO | fora da faixa vertical |
| 119 | 145.00 | 98.00 | 283.01 | 281.29 | NÃO | fora da faixa vertical |
| 120 | 144.00 | 99.00 | 281.84 | 280.29 | NÃO | fora da faixa vertical |
| 121 | 143.00 | 100.00 | 280.67 | 279.29 | NÃO | fora da faixa vertical |
| 122 | 142.00 | 101.00 | 279.51 | 278.29 | NÃO | fora da faixa vertical |
| 123 | 141.00 | 102.00 | 278.35 | 277.29 | NÃO | fora da faixa vertical |
| 124 | 140.00 | 103.00 | 277.19 | 276.29 | NÃO | fora da faixa vertical |
| 125 | 139.00 | 104.00 | 276.03 | 275.29 | NÃO | fora da faixa vertical |
| 126 | 138.00 | 105.00 | 274.88 | 274.29 | NÃO | fora da faixa vertical |
| 127 | 137.00 | 106.00 | 273.72 | 273.29 | NÃO | fora da faixa vertical |
| 128 | 136.00 | 107.00 | 272.57 | 272.29 | NÃO | fora da faixa vertical |
| 129 | 135.00 | 108.00 | 271.43 | 271.29 | NÃO | fora da faixa vertical |
| 130 | 134.00 | 109.00 | 270.28 | 270.29 | NÃO | fora da faixa vertical |
| 131 | 133.00 | 110.00 | 269.14 | 269.29 | NÃO | fora da faixa vertical |
| 132 | 132.00 | 111.00 | 268.00 | 268.29 | NÃO | fora da faixa vertical |
| 133 | 131.00 | 112.00 | 266.87 | 267.29 | NÃO | fora da faixa vertical |
| 134 | 130.00 | 113.00 | 265.73 | 266.29 | NÃO | fora da faixa vertical |
| 135 | 129.00 | 114.00 | 264.60 | 265.29 | NÃO | fora da faixa vertical |
| 136 | 128.00 | 115.00 | 263.47 | 264.29 | NÃO | fora da faixa vertical |
| 137 | 127.00 | 116.00 | 262.35 | 263.29 | NÃO | fora da faixa vertical |
| 138 | 126.00 | 117.00 | 261.22 | 262.29 | NÃO | fora da faixa vertical |
| 139 | 126.00 | 118.00 | 260.23 | 261.29 | NÃO | fora da faixa vertical |
| 140 | 125.00 | 119.00 | 259.11 | 260.29 | NÃO | fora da faixa vertical |
| 141 | 124.00 | 120.00 | 257.99 | 259.29 | NÃO | fora da faixa vertical |
| 142 | 123.00 | 121.00 | 256.88 | 258.29 | NÃO | fora da faixa vertical |
| 143 | 122.00 | 122.00 | 255.77 | 257.29 | NÃO | fora da faixa vertical |
| 144 | 121.00 | 123.00 | 254.66 | 256.29 | NÃO | fora da faixa vertical |
| 145 | 121.00 | 124.00 | 253.66 | 255.29 | NÃO | fora da faixa vertical |
| 146 | 120.00 | 125.00 | 252.56 | 254.29 | NÃO | fora da faixa vertical |
| 147 | 119.00 | 126.00 | 251.45 | 253.29 | NÃO | fora da faixa vertical |
| 148 | 118.00 | 127.00 | 250.35 | 252.29 | NÃO | fora da faixa vertical |
| 149 | 118.00 | 128.00 | 249.36 | 251.29 | NÃO | fora da faixa vertical |
| 150 | 117.00 | 129.00 | 248.26 | 250.29 | NÃO | fora da faixa vertical |
| 151 | 116.00 | 130.00 | 247.17 | 249.29 | NÃO | fora da faixa vertical |
| 152 | 115.00 | 131.00 | 246.08 | 248.29 | NÃO | fora da faixa vertical |
| 153 | 115.00 | 132.00 | 245.08 | 247.29 | NÃO | fora da faixa vertical |
| 154 | 114.00 | 133.00 | 243.99 | 246.29 | NÃO | fora da faixa vertical |
| 155 | 113.00 | 134.00 | 242.91 | 245.29 | NÃO | fora da faixa vertical |
| 156 | 112.00 | 135.00 | 241.83 | 244.29 | NÃO | fora da faixa vertical |
| 157 | 112.00 | 136.00 | 240.83 | 243.29 | NÃO | fora da faixa vertical |
| 158 | 111.00 | 137.00 | 239.75 | 242.29 | NÃO | fora da faixa vertical |
| 159 | 110.00 | 138.00 | 238.68 | 241.29 | NÃO | fora da faixa vertical |
| 160 | 110.00 | 139.00 | 237.68 | 240.29 | NÃO | fora da faixa vertical |
| 161 | 109.00 | 140.00 | 236.61 | 239.29 | NÃO | fora da faixa vertical |
| 162 | 109.00 | 141.00 | 235.61 | 238.29 | NÃO | fora da faixa vertical |
| 163 | 108.00 | 142.00 | 234.55 | 237.29 | NÃO | fora da faixa vertical |
| 164 | 107.00 | 143.00 | 233.48 | 236.29 | NÃO | fora da faixa vertical |
| 165 | 107.00 | 144.00 | 232.48 | 235.29 | NÃO | fora da faixa vertical |
| 166 | 106.00 | 145.00 | 231.42 | 234.29 | NÃO | fora da faixa vertical |
| 167 | 105.00 | 146.00 | 230.37 | 233.29 | NÃO | fora da faixa vertical |
| 168 | 105.00 | 147.00 | 229.37 | 232.29 | NÃO | fora da faixa vertical |
| 169 | 104.00 | 148.00 | 228.32 | 231.29 | NÃO | fora da faixa vertical |
| 170 | 104.00 | 149.00 | 227.32 | 230.29 | NÃO | fora da faixa vertical |
| 171 | 103.00 | 150.00 | 226.27 | 229.29 | NÃO | fora da faixa vertical |
| 172 | 102.00 | 151.00 | 225.22 | 228.29 | NÃO | fora da faixa vertical |
| 173 | 102.00 | 152.00 | 224.22 | 227.29 | NÃO | fora da faixa vertical |
| 174 | 101.00 | 153.00 | 223.18 | 226.29 | NÃO | fora da faixa vertical |
| 175 | 101.00 | 154.00 | 222.18 | 225.29 | NÃO | fora da faixa vertical |
| 176 | 100.00 | 155.00 | 221.14 | 224.29 | NÃO | fora da faixa vertical |
| 177 | 100.00 | 156.00 | 220.15 | 223.29 | NÃO | fora da faixa vertical |
| 178 | 99.00 | 157.00 | 219.11 | 222.29 | NÃO | fora da faixa vertical |
| 179 | 99.00 | 158.00 | 218.11 | 221.29 | NÃO | fora da faixa vertical |
| 180 | 98.00 | 159.00 | 217.08 | 220.29 | NÃO | fora da faixa vertical |
| 181 | 98.00 | 160.00 | 216.08 | 219.29 | NÃO | fora da faixa vertical |
| 182 | 97.00 | 161.00 | 215.06 | 218.29 | NÃO | fora da faixa vertical |
| 183 | 97.00 | 162.00 | 214.06 | 217.29 | NÃO | fora da faixa vertical |
| 184 | 96.00 | 163.00 | 213.04 | 216.29 | NÃO | fora da faixa vertical |
| 185 | 96.00 | 164.00 | 212.04 | 215.29 | NÃO | fora da faixa vertical |
| 186 | 95.00 | 165.00 | 211.02 | 214.29 | NÃO | fora da faixa vertical |
| 187 | 95.00 | 166.00 | 210.02 | 213.29 | NÃO | fora da faixa vertical |
| 188 | 94.00 | 167.00 | 209.01 | 212.29 | NÃO | fora da faixa vertical |
| 189 | 94.00 | 168.00 | 208.01 | 211.29 | NÃO | fora da faixa vertical |
| 190 | 93.00 | 169.00 | 207.00 | 210.29 | NÃO | fora da faixa vertical |
| 191 | 93.00 | 170.00 | 206.00 | 209.29 | NÃO | fora da faixa vertical |
| 192 | 93.00 | 171.00 | 205.00 | 208.29 | NÃO | fora da faixa vertical |
| 193 | 92.00 | 172.00 | 204.00 | 207.29 | NÃO | fora da faixa vertical |
| 194 | 92.00 | 173.00 | 203.00 | 206.29 | NÃO | fora da faixa vertical |
| 195 | 91.00 | 174.00 | 202.00 | 205.29 | NÃO | fora da faixa vertical |
| 196 | 91.00 | 175.00 | 201.00 | 204.29 | NÃO | fora da faixa vertical |
| 197 | 91.00 | 176.00 | 200.00 | 203.29 | NÃO | fora da faixa vertical |
| 198 | 90.00 | 177.00 | 199.01 | 202.29 | NÃO | fora da faixa vertical |
| 199 | 90.00 | 178.00 | 198.01 | 201.29 | NÃO | fora da faixa vertical |
| 200 | 90.00 | 179.00 | 197.01 | 200.29 | NÃO | fora da faixa vertical |
| 201 | 89.00 | 180.00 | 196.02 | 199.29 | NÃO | fora da faixa vertical |
| 202 | 89.00 | 181.00 | 195.02 | 198.29 | NÃO | fora da faixa vertical |
| 203 | 88.00 | 182.00 | 194.04 | 197.29 | NÃO | fora da faixa vertical |
| 204 | 88.00 | 183.00 | 193.04 | 196.29 | NÃO | fora da faixa vertical |
| 205 | 88.00 | 184.00 | 192.04 | 195.29 | NÃO | fora da faixa vertical |
| 206 | 87.00 | 185.00 | 191.07 | 194.29 | NÃO | fora da faixa vertical |
| 207 | 87.00 | 186.00 | 190.07 | 193.29 | NÃO | fora da faixa vertical |
| 208 | 87.00 | 187.00 | 189.07 | 192.29 | NÃO | fora da faixa vertical |
| 209 | 86.00 | 188.00 | 188.10 | 191.29 | NÃO | fora da faixa vertical |
| 210 | 86.00 | 189.00 | 187.10 | 190.29 | NÃO | fora da faixa vertical |
| 211 | 86.00 | 190.00 | 186.10 | 189.29 | NÃO | fora da faixa vertical |
| 212 | 86.00 | 191.00 | 185.10 | 188.29 | NÃO | fora da faixa vertical |
| 213 | 85.00 | 192.00 | 184.13 | 187.29 | NÃO | fora da faixa vertical |
| 214 | 85.00 | 193.00 | 183.13 | 186.29 | NÃO | fora da faixa vertical |
| 215 | 85.00 | 194.00 | 182.13 | 185.29 | NÃO | fora da faixa vertical |
| 216 | 84.00 | 195.00 | 181.18 | 184.29 | NÃO | fora da faixa vertical |
| 217 | 84.00 | 196.00 | 180.18 | 183.29 | NÃO | fora da faixa vertical |
| 218 | 84.00 | 197.00 | 179.18 | 182.29 | NÃO | fora da faixa vertical |
| 219 | 84.00 | 198.00 | 178.18 | 181.29 | NÃO | fora da faixa vertical |
| 220 | 83.00 | 199.00 | 177.23 | 180.29 | NÃO | fora da faixa vertical |
| 221 | 83.00 | 200.00 | 176.23 | 179.29 | SIM | dentro da janela vertical e do lado solicitado |
| 222 | 83.00 | 201.00 | 175.23 | 178.29 | SIM | dentro da janela vertical e do lado solicitado |
| 223 | 83.00 | 202.00 | 174.23 | 177.29 | SIM | dentro da janela vertical e do lado solicitado |
| 224 | 82.00 | 203.00 | 173.29 | 176.29 | SIM | dentro da janela vertical e do lado solicitado |
| 225 | 82.00 | 204.00 | 172.29 | 175.29 | SIM | dentro da janela vertical e do lado solicitado |
| 226 | 82.00 | 205.00 | 171.29 | 174.29 | SIM | dentro da janela vertical e do lado solicitado |
| 227 | 82.00 | 206.00 | 170.29 | 173.29 | SIM | dentro da janela vertical e do lado solicitado |
| 228 | 82.00 | 207.00 | 169.30 | 172.29 | SIM | dentro da janela vertical e do lado solicitado |
| 229 | 81.00 | 208.00 | 168.36 | 171.29 | SIM | dentro da janela vertical e do lado solicitado |
| 230 | 81.00 | 209.00 | 167.36 | 170.29 | SIM | dentro da janela vertical e do lado solicitado |
| 231 | 81.00 | 210.00 | 166.36 | 169.29 | SIM | dentro da janela vertical e do lado solicitado |
| 232 | 81.00 | 211.00 | 165.37 | 168.29 | SIM | dentro da janela vertical e do lado solicitado |
| 233 | 81.00 | 212.00 | 164.37 | 167.29 | SIM | dentro da janela vertical e do lado solicitado |
| 234 | 80.00 | 213.00 | 163.44 | 166.29 | SIM | dentro da janela vertical e do lado solicitado |
| 235 | 80.00 | 214.00 | 162.44 | 165.29 | SIM | dentro da janela vertical e do lado solicitado |
| 236 | 80.00 | 215.00 | 161.45 | 164.29 | SIM | dentro da janela vertical e do lado solicitado |
| 237 | 80.00 | 216.00 | 160.45 | 163.29 | SIM | dentro da janela vertical e do lado solicitado |
| 238 | 80.00 | 217.00 | 159.45 | 162.29 | SIM | dentro da janela vertical e do lado solicitado |
| 239 | 79.00 | 218.00 | 158.53 | 161.29 | SIM | dentro da janela vertical e do lado solicitado |
| 240 | 79.00 | 219.00 | 157.54 | 160.29 | SIM | dentro da janela vertical e do lado solicitado |
| 241 | 79.00 | 220.00 | 156.54 | 159.29 | SIM | dentro da janela vertical e do lado solicitado |
| 242 | 79.00 | 221.00 | 155.54 | 158.29 | SIM | dentro da janela vertical e do lado solicitado |
| 243 | 79.00 | 222.00 | 154.55 | 157.29 | SIM | dentro da janela vertical e do lado solicitado |
| 244 | 79.00 | 223.00 | 153.55 | 156.29 | SIM | dentro da janela vertical e do lado solicitado |
| 245 | 79.00 | 224.00 | 152.55 | 155.29 | SIM | dentro da janela vertical e do lado solicitado |
| 246 | 79.00 | 225.00 | 151.56 | 154.29 | SIM | dentro da janela vertical e do lado solicitado |
| 247 | 78.00 | 226.00 | 150.65 | 153.29 | SIM | dentro da janela vertical e do lado solicitado |
| 248 | 78.00 | 227.00 | 149.66 | 152.29 | SIM | dentro da janela vertical e do lado solicitado |
| 249 | 78.00 | 228.00 | 148.66 | 151.29 | SIM | dentro da janela vertical e do lado solicitado |
| 250 | 78.00 | 229.00 | 147.67 | 150.29 | SIM | dentro da janela vertical e do lado solicitado |
| 251 | 78.00 | 230.00 | 146.67 | 149.29 | SIM | dentro da janela vertical e do lado solicitado |
| 252 | 78.00 | 231.00 | 145.67 | 148.29 | SIM | dentro da janela vertical e do lado solicitado |
| 253 | 78.00 | 232.00 | 144.68 | 147.29 | SIM | dentro da janela vertical e do lado solicitado |
| 254 | 78.00 | 233.00 | 143.68 | 146.29 | SIM | dentro da janela vertical e do lado solicitado |
| 255 | 77.00 | 234.00 | 142.79 | 145.29 | SIM | dentro da janela vertical e do lado solicitado |
| 256 | 77.00 | 235.00 | 141.80 | 144.29 | SIM | dentro da janela vertical e do lado solicitado |
| 257 | 77.00 | 236.00 | 140.80 | 143.29 | SIM | dentro da janela vertical e do lado solicitado |
| 258 | 77.00 | 237.00 | 139.81 | 142.29 | SIM | dentro da janela vertical e do lado solicitado |
| 259 | 77.00 | 238.00 | 138.81 | 141.29 | SIM | dentro da janela vertical e do lado solicitado |
| 260 | 77.00 | 239.00 | 137.82 | 140.29 | SIM | dentro da janela vertical e do lado solicitado |
| 261 | 77.00 | 240.00 | 136.82 | 139.29 | SIM | dentro da janela vertical e do lado solicitado |
| 262 | 77.00 | 241.00 | 135.83 | 138.29 | SIM | dentro da janela vertical e do lado solicitado |
| 263 | 77.00 | 242.00 | 134.84 | 137.29 | SIM | dentro da janela vertical e do lado solicitado |
| 264 | 77.00 | 243.00 | 133.84 | 136.29 | SIM | dentro da janela vertical e do lado solicitado |
| 265 | 77.00 | 244.00 | 132.85 | 135.29 | SIM | dentro da janela vertical e do lado solicitado |
| 266 | 77.00 | 245.00 | 131.86 | 134.29 | SIM | dentro da janela vertical e do lado solicitado |
| 267 | 77.00 | 246.00 | 130.86 | 133.29 | SIM | dentro da janela vertical e do lado solicitado |
| 268 | 77.00 | 247.00 | 129.87 | 132.29 | SIM | dentro da janela vertical e do lado solicitado |
| 269 | 77.00 | 248.00 | 128.88 | 131.29 | SIM | dentro da janela vertical e do lado solicitado |
| 270 | 77.00 | 249.00 | 127.88 | 130.29 | SIM | dentro da janela vertical e do lado solicitado |
| 271 | 77.00 | 250.00 | 126.89 | 129.29 | SIM | dentro da janela vertical e do lado solicitado |
| 272 | 77.00 | 251.00 | 125.90 | 128.29 | SIM | dentro da janela vertical e do lado solicitado |
| 273 | 77.00 | 252.00 | 124.90 | 127.29 | SIM | dentro da janela vertical e do lado solicitado |
| 274 | 77.00 | 253.00 | 123.91 | 126.29 | SIM | dentro da janela vertical e do lado solicitado |
| 275 | 77.00 | 254.00 | 122.92 | 125.29 | SIM | dentro da janela vertical e do lado solicitado |
| 276 | 77.00 | 255.00 | 121.93 | 124.29 | SIM | dentro da janela vertical e do lado solicitado |
| 277 | 77.00 | 256.00 | 120.93 | 123.29 | SIM | dentro da janela vertical e do lado solicitado |
| 278 | 77.00 | 257.00 | 119.94 | 122.29 | SIM | dentro da janela vertical e do lado solicitado |
| 279 | 77.00 | 258.00 | 118.95 | 121.29 | SIM | dentro da janela vertical e do lado solicitado |
| 280 | 77.00 | 259.00 | 117.96 | 120.29 | SIM | dentro da janela vertical e do lado solicitado |
| 281 | 77.00 | 260.00 | 116.97 | 119.29 | SIM | dentro da janela vertical e do lado solicitado |
| 282 | 77.00 | 261.00 | 115.97 | 118.29 | SIM | dentro da janela vertical e do lado solicitado |
| 283 | 77.00 | 262.00 | 114.98 | 117.29 | SIM | dentro da janela vertical e do lado solicitado |
| 284 | 77.00 | 263.00 | 113.99 | 116.29 | SIM | dentro da janela vertical e do lado solicitado |
| 285 | 77.00 | 264.00 | 113.00 | 115.29 | SIM | dentro da janela vertical e do lado solicitado |
| 286 | 77.00 | 265.00 | 112.01 | 114.29 | SIM | dentro da janela vertical e do lado solicitado |
| 287 | 78.00 | 266.00 | 110.89 | 113.29 | SIM | dentro da janela vertical e do lado solicitado |
| 288 | 78.00 | 267.00 | 109.90 | 112.29 | SIM | dentro da janela vertical e do lado solicitado |
| 289 | 78.00 | 268.00 | 108.90 | 111.29 | SIM | dentro da janela vertical e do lado solicitado |
| 290 | 78.00 | 269.00 | 107.91 | 110.29 | SIM | dentro da janela vertical e do lado solicitado |
| 291 | 78.00 | 270.00 | 106.92 | 109.29 | SIM | dentro da janela vertical e do lado solicitado |
| 292 | 78.00 | 271.00 | 105.93 | 108.29 | SIM | dentro da janela vertical e do lado solicitado |
| 293 | 78.00 | 272.00 | 104.94 | 107.29 | SIM | dentro da janela vertical e do lado solicitado |
| 294 | 78.00 | 273.00 | 103.95 | 106.29 | SIM | dentro da janela vertical e do lado solicitado |
| 295 | 78.00 | 274.00 | 102.96 | 105.29 | SIM | dentro da janela vertical e do lado solicitado |
| 296 | 79.00 | 275.00 | 101.83 | 104.29 | SIM | dentro da janela vertical e do lado solicitado |
| 297 | 79.00 | 276.00 | 100.84 | 103.29 | SIM | dentro da janela vertical e do lado solicitado |
| 298 | 79.00 | 277.00 | 99.85 | 102.29 | SIM | dentro da janela vertical e do lado solicitado |
| 299 | 79.00 | 278.00 | 98.86 | 101.29 | SIM | dentro da janela vertical e do lado solicitado |
| 300 | 79.00 | 279.00 | 97.87 | 100.29 | SIM | dentro da janela vertical e do lado solicitado |
| 301 | 79.00 | 280.00 | 96.88 | 99.29 | SIM | dentro da janela vertical e do lado solicitado |
| 302 | 79.00 | 281.00 | 95.89 | 98.29 | SIM | dentro da janela vertical e do lado solicitado |
| 303 | 79.00 | 282.00 | 94.89 | 97.29 | SIM | dentro da janela vertical e do lado solicitado |
| 304 | 80.00 | 283.00 | 93.77 | 96.29 | SIM | dentro da janela vertical e do lado solicitado |
| 305 | 80.00 | 284.00 | 92.78 | 95.29 | SIM | dentro da janela vertical e do lado solicitado |
| 306 | 80.00 | 285.00 | 91.79 | 94.29 | SIM | dentro da janela vertical e do lado solicitado |
| 307 | 80.00 | 286.00 | 90.80 | 93.29 | SIM | dentro da janela vertical e do lado solicitado |
| 308 | 80.00 | 287.00 | 89.81 | 92.29 | SIM | dentro da janela vertical e do lado solicitado |
| 309 | 81.00 | 288.00 | 88.68 | 91.29 | SIM | dentro da janela vertical e do lado solicitado |
| 310 | 81.00 | 289.00 | 87.69 | 90.29 | SIM | dentro da janela vertical e do lado solicitado |
| 311 | 81.00 | 290.00 | 86.70 | 89.29 | SIM | dentro da janela vertical e do lado solicitado |
| 312 | 81.00 | 291.00 | 85.71 | 88.29 | SIM | dentro da janela vertical e do lado solicitado |
| 313 | 82.00 | 292.00 | 84.59 | 87.29 | SIM | dentro da janela vertical e do lado solicitado |
| 314 | 82.00 | 293.00 | 83.60 | 86.29 | SIM | dentro da janela vertical e do lado solicitado |
| 315 | 82.00 | 294.00 | 82.61 | 85.29 | SIM | dentro da janela vertical e do lado solicitado |
| 316 | 82.00 | 295.00 | 81.61 | 84.29 | SIM | dentro da janela vertical e do lado solicitado |
| 317 | 82.00 | 296.00 | 80.62 | 83.29 | SIM | dentro da janela vertical e do lado solicitado |
| 318 | 83.00 | 297.00 | 79.51 | 82.29 | SIM | dentro da janela vertical e do lado solicitado |
| 319 | 83.00 | 298.00 | 78.52 | 81.29 | SIM | dentro da janela vertical e do lado solicitado |
| 320 | 83.00 | 299.00 | 77.52 | 80.29 | SIM | dentro da janela vertical e do lado solicitado |
| 321 | 83.00 | 300.00 | 76.53 | 79.29 | SIM | dentro da janela vertical e do lado solicitado |
| 322 | 84.00 | 301.00 | 75.43 | 78.29 | SIM | dentro da janela vertical e do lado solicitado |
| 323 | 84.00 | 302.00 | 74.43 | 77.29 | SIM | dentro da janela vertical e do lado solicitado |
| 324 | 84.00 | 303.00 | 73.44 | 76.29 | SIM | dentro da janela vertical e do lado solicitado |
| 325 | 84.00 | 304.00 | 72.44 | 75.29 | SIM | dentro da janela vertical e do lado solicitado |
| 326 | 85.00 | 305.00 | 71.34 | 74.29 | SIM | dentro da janela vertical e do lado solicitado |
| 327 | 85.00 | 306.00 | 70.35 | 73.29 | SIM | dentro da janela vertical e do lado solicitado |
| 328 | 85.00 | 307.00 | 69.35 | 72.29 | SIM | dentro da janela vertical e do lado solicitado |
| 329 | 86.00 | 308.00 | 68.26 | 71.29 | SIM | dentro da janela vertical e do lado solicitado |
| 330 | 86.00 | 309.00 | 67.27 | 70.29 | SIM | dentro da janela vertical e do lado solicitado |
| 331 | 86.00 | 310.00 | 66.27 | 69.29 | SIM | dentro da janela vertical e do lado solicitado |
| 332 | 86.00 | 311.00 | 65.28 | 68.29 | SIM | dentro da janela vertical e do lado solicitado |
| 333 | 87.00 | 312.00 | 64.20 | 67.29 | SIM | dentro da janela vertical e do lado solicitado |
| 334 | 87.00 | 313.00 | 63.20 | 66.29 | SIM | dentro da janela vertical e do lado solicitado |
| 335 | 87.00 | 314.00 | 62.20 | 65.29 | SIM | dentro da janela vertical e do lado solicitado |
| 336 | 88.00 | 315.00 | 61.13 | 64.29 | SIM | dentro da janela vertical e do lado solicitado |
| 337 | 88.00 | 316.00 | 60.13 | 63.29 | SIM | dentro da janela vertical e do lado solicitado |
| 338 | 88.00 | 317.00 | 59.14 | 62.29 | SIM | dentro da janela vertical e do lado solicitado |
| 339 | 89.00 | 318.00 | 58.08 | 61.29 | SIM | dentro da janela vertical e do lado solicitado |
| 340 | 89.00 | 319.00 | 57.08 | 60.29 | SIM | dentro da janela vertical e do lado solicitado |
| 341 | 89.00 | 320.00 | 56.08 | 59.29 | SIM | dentro da janela vertical e do lado solicitado |
| 342 | 90.00 | 321.00 | 55.04 | 58.29 | SIM | dentro da janela vertical e do lado solicitado |
| 343 | 90.00 | 322.00 | 54.04 | 57.29 | SIM | dentro da janela vertical e do lado solicitado |
| 344 | 91.00 | 323.00 | 53.01 | 56.29 | SIM | dentro da janela vertical e do lado solicitado |
| 345 | 91.00 | 324.00 | 52.01 | 55.29 | SIM | dentro da janela vertical e do lado solicitado |
| 346 | 91.00 | 325.00 | 51.01 | 54.29 | SIM | dentro da janela vertical e do lado solicitado |
| 347 | 92.00 | 326.00 | 50.00 | 53.29 | SIM | dentro da janela vertical e do lado solicitado |
| 348 | 92.00 | 327.00 | 49.00 | 52.29 | SIM | dentro da janela vertical e do lado solicitado |
| 349 | 92.00 | 328.00 | 48.00 | 51.29 | SIM | dentro da janela vertical e do lado solicitado |
| 350 | 93.00 | 329.00 | 47.01 | 50.29 | SIM | dentro da janela vertical e do lado solicitado |
| 351 | 93.00 | 330.00 | 46.01 | 49.29 | SIM | dentro da janela vertical e do lado solicitado |
| 352 | 94.00 | 331.00 | 45.04 | 48.29 | SIM | dentro da janela vertical e do lado solicitado |
| 353 | 94.00 | 332.00 | 44.05 | 47.29 | SIM | dentro da janela vertical e do lado solicitado |
| 354 | 95.00 | 333.00 | 43.10 | 46.29 | SIM | dentro da janela vertical e do lado solicitado |
| 355 | 95.00 | 334.00 | 42.11 | 45.29 | SIM | dentro da janela vertical e do lado solicitado |
| 356 | 96.00 | 335.00 | 41.19 | 44.29 | SIM | dentro da janela vertical e do lado solicitado |
| 357 | 96.00 | 336.00 | 40.20 | 43.29 | SIM | dentro da janela vertical e do lado solicitado |
| 358 | 97.00 | 337.00 | 39.32 | 42.29 | SIM | dentro da janela vertical e do lado solicitado |
| 359 | 97.00 | 338.00 | 38.33 | 41.29 | SIM | dentro da janela vertical e do lado solicitado |
| 360 | 98.00 | 339.00 | 37.48 | 40.29 | SIM | dentro da janela vertical e do lado solicitado |
| 361 | 98.00 | 340.00 | 36.50 | 39.29 | SIM | dentro da janela vertical e do lado solicitado |
| 362 | 99.00 | 341.00 | 35.69 | 38.29 | SIM | dentro da janela vertical e do lado solicitado |
| 363 | 99.00 | 342.00 | 34.71 | 37.29 | SIM | dentro da janela vertical e do lado solicitado |
| 364 | 100.00 | 343.00 | 33.96 | 36.29 | SIM | dentro da janela vertical e do lado solicitado |
| 365 | 100.00 | 344.00 | 32.98 | 35.29 | SIM | dentro da janela vertical e do lado solicitado |
| 366 | 101.00 | 345.00 | 32.28 | 34.29 | SIM | dentro da janela vertical e do lado solicitado |
| 367 | 101.00 | 346.00 | 31.32 | 33.29 | SIM | dentro da janela vertical e do lado solicitado |
| 368 | 102.00 | 347.00 | 30.68 | 32.29 | SIM | dentro da janela vertical e do lado solicitado |
| 369 | 102.00 | 348.00 | 29.73 | 31.29 | SIM | dentro da janela vertical e do lado solicitado |
| 370 | 103.00 | 349.00 | 29.15 | 30.29 | SIM | dentro da janela vertical e do lado solicitado |
| 371 | 103.00 | 350.00 | 28.23 | 29.29 | SIM | dentro da janela vertical e do lado solicitado |
| 372 | 104.00 | 351.00 | 27.73 | 28.29 | SIM | dentro da janela vertical e do lado solicitado |
| 373 | 105.00 | 352.00 | 27.29 | 27.29 | SIM | dentro da janela vertical e do lado solicitado |
| 374 | 105.00 | 353.00 | 26.42 | 26.29 | SIM | dentro da janela vertical e do lado solicitado |
| 375 | 106.00 | 354.00 | 26.08 | 25.29 | SIM | dentro da janela vertical e do lado solicitado |
| 376 | 107.00 | 355.00 | 25.81 | 24.29 | SIM | dentro da janela vertical e do lado solicitado |
| 377 | 107.00 | 356.00 | 25.00 | 23.29 | SIM | dentro da janela vertical e do lado solicitado |
| 378 | 108.00 | 357.00 | 24.84 | 22.29 | SIM | dentro da janela vertical e do lado solicitado |
| 379 | 108.00 | 358.00 | 24.08 | 21.29 | SIM | dentro da janela vertical e do lado solicitado |
| 380 | 109.00 | 359.00 | 24.04 | 20.29 | SIM | dentro da janela vertical e do lado solicitado |
| 381 | 110.00 | 360.00 | 24.08 | 19.29 | SIM | dentro da janela vertical e do lado solicitado |
| 382 | 110.00 | 361.00 | 23.43 | 18.29 | SIM | dentro da janela vertical e do lado solicitado |
| 383 | 111.00 | 362.00 | 23.60 | 17.29 | SIM | dentro da janela vertical e do lado solicitado |
| 384 | 112.00 | 363.00 | 23.85 | 16.29 | SIM | dentro da janela vertical e do lado solicitado |
| 385 | 112.00 | 364.00 | 23.32 | 15.29 | SIM | dentro da janela vertical e do lado solicitado |
| 386 | 113.00 | 365.00 | 23.71 | 14.29 | SIM | dentro da janela vertical e do lado solicitado |
| 387 | 114.00 | 366.00 | 24.17 | 13.29 | SIM | dentro da janela vertical e do lado solicitado |
| 388 | 114.00 | 367.00 | 23.77 | 12.29 | SIM | dentro da janela vertical e do lado solicitado |
| 389 | 115.00 | 368.00 | 24.35 | 11.29 | SIM | dentro da janela vertical e do lado solicitado |
| 390 | 116.00 | 369.00 | 25.00 | 10.29 | SIM | dentro da janela vertical e do lado solicitado |
| 391 | 117.00 | 370.00 | 25.71 | 9.29 | SIM | dentro da janela vertical e do lado solicitado |
| 392 | 117.00 | 371.00 | 25.50 | 8.29 | SIM | dentro da janela vertical e do lado solicitado |
| 393 | 118.00 | 372.00 | 26.31 | 7.29 | SIM | dentro da janela vertical e do lado solicitado |
| 394 | 119.00 | 373.00 | 27.17 | 6.29 | SIM | dentro da janela vertical e do lado solicitado |
| 395 | 120.00 | 374.00 | 28.07 | 5.29 | SIM | dentro da janela vertical e do lado solicitado |
| 396 | 120.00 | 375.00 | 28.02 | 4.29 | SIM | dentro da janela vertical e do lado solicitado |
| 397 | 120.00 | 376.00 | 28.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 398 | 121.00 | 376.00 | 29.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 399 | 122.00 | 376.00 | 30.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 400 | 123.00 | 376.00 | 31.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 401 | 124.00 | 376.00 | 32.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 402 | 125.00 | 376.00 | 33.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 403 | 126.00 | 376.00 | 34.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 404 | 127.00 | 376.00 | 35.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 405 | 128.00 | 376.00 | 36.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 406 | 129.00 | 376.00 | 37.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 407 | 130.00 | 376.00 | 38.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 408 | 131.00 | 376.00 | 39.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 409 | 132.00 | 376.00 | 40.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 410 | 133.00 | 376.00 | 41.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 411 | 134.00 | 376.00 | 42.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 412 | 135.00 | 376.00 | 43.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 413 | 136.00 | 376.00 | 44.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 414 | 137.00 | 376.00 | 45.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 415 | 138.00 | 376.00 | 46.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 416 | 139.00 | 376.00 | 47.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 417 | 140.00 | 376.00 | 48.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 418 | 141.00 | 376.00 | 49.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 419 | 142.00 | 376.00 | 50.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 420 | 143.00 | 376.00 | 51.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 421 | 144.00 | 376.00 | 52.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 422 | 145.00 | 376.00 | 53.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 423 | 146.00 | 376.00 | 54.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 424 | 147.00 | 376.00 | 55.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 425 | 148.00 | 376.00 | 56.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 426 | 149.00 | 376.00 | 57.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 427 | 150.00 | 376.00 | 58.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 428 | 151.00 | 376.00 | 59.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 429 | 152.00 | 376.00 | 60.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 430 | 153.00 | 376.00 | 61.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 431 | 154.00 | 376.00 | 62.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 432 | 155.00 | 376.00 | 63.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 433 | 156.00 | 376.00 | 64.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 434 | 157.00 | 376.00 | 65.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 435 | 158.00 | 376.00 | 66.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 436 | 159.00 | 376.00 | 67.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 437 | 160.00 | 376.00 | 68.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 438 | 161.00 | 376.00 | 69.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 439 | 162.00 | 376.00 | 70.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 440 | 163.00 | 376.00 | 71.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 441 | 164.00 | 376.00 | 72.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 442 | 165.00 | 376.00 | 73.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 443 | 166.00 | 376.00 | 74.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 444 | 167.00 | 376.00 | 75.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 445 | 168.00 | 376.00 | 76.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 446 | 169.00 | 376.00 | 77.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 447 | 170.00 | 376.00 | 78.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 448 | 171.00 | 376.00 | 79.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 449 | 172.00 | 376.00 | 80.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 450 | 173.00 | 376.00 | 81.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 451 | 174.00 | 376.00 | 82.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 452 | 175.00 | 376.00 | 83.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 453 | 176.00 | 376.00 | 84.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 454 | 177.00 | 376.00 | 85.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 455 | 178.00 | 376.00 | 86.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 456 | 179.00 | 376.00 | 87.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 457 | 180.00 | 376.00 | 88.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 458 | 181.00 | 376.00 | 89.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 459 | 182.00 | 376.00 | 90.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 460 | 183.00 | 376.00 | 91.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 461 | 184.00 | 376.00 | 92.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 462 | 185.00 | 376.00 | 93.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 463 | 186.00 | 376.00 | 94.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 464 | 187.00 | 376.00 | 95.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 465 | 188.00 | 376.00 | 96.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 466 | 189.00 | 376.00 | 97.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 467 | 190.00 | 376.00 | 98.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 468 | 191.00 | 376.00 | 99.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 469 | 192.00 | 376.00 | 100.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 470 | 193.00 | 376.00 | 101.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 471 | 194.00 | 376.00 | 102.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 472 | 195.00 | 376.00 | 103.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 473 | 196.00 | 376.00 | 104.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 474 | 197.00 | 376.00 | 105.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 475 | 198.00 | 376.00 | 106.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 476 | 199.00 | 376.00 | 107.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 477 | 200.00 | 376.00 | 108.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 478 | 201.00 | 376.00 | 109.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 479 | 202.00 | 376.00 | 110.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 480 | 203.00 | 376.00 | 111.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 481 | 204.00 | 376.00 | 112.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 482 | 205.00 | 376.00 | 113.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 483 | 206.00 | 376.00 | 114.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 484 | 207.00 | 376.00 | 115.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 485 | 208.00 | 376.00 | 116.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 486 | 209.00 | 376.00 | 117.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 487 | 210.00 | 376.00 | 118.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 488 | 211.00 | 376.00 | 119.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 489 | 212.00 | 376.00 | 120.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 490 | 213.00 | 376.00 | 121.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 491 | 214.00 | 376.00 | 122.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 492 | 215.00 | 376.00 | 123.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 493 | 216.00 | 376.00 | 124.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 494 | 217.00 | 376.00 | 125.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 495 | 218.00 | 376.00 | 126.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 496 | 219.00 | 376.00 | 127.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 497 | 220.00 | 376.00 | 128.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 498 | 221.00 | 376.00 | 129.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 499 | 222.00 | 376.00 | 130.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 500 | 223.00 | 376.00 | 131.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 501 | 224.00 | 376.00 | 132.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 502 | 225.00 | 376.00 | 133.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 503 | 226.00 | 376.00 | 134.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 504 | 227.00 | 376.00 | 135.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 505 | 228.00 | 376.00 | 136.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 506 | 229.00 | 376.00 | 137.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 507 | 230.00 | 376.00 | 138.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 508 | 231.00 | 376.00 | 139.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 509 | 232.00 | 376.00 | 140.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 510 | 233.00 | 376.00 | 141.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 511 | 234.00 | 376.00 | 142.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 512 | 235.00 | 376.00 | 143.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 513 | 236.00 | 376.00 | 144.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 514 | 237.00 | 376.00 | 145.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 515 | 238.00 | 376.00 | 146.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 516 | 239.00 | 376.00 | 147.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 517 | 240.00 | 376.00 | 148.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 518 | 241.00 | 376.00 | 149.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 519 | 242.00 | 376.00 | 150.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 520 | 243.00 | 376.00 | 151.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 521 | 244.00 | 376.00 | 152.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 522 | 245.00 | 376.00 | 153.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 523 | 246.00 | 376.00 | 154.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 524 | 247.00 | 376.00 | 155.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 525 | 248.00 | 376.00 | 156.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 526 | 249.00 | 376.00 | 157.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 527 | 250.00 | 376.00 | 158.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 528 | 251.00 | 376.00 | 159.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 529 | 252.00 | 376.00 | 160.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 530 | 253.00 | 376.00 | 161.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 531 | 254.00 | 376.00 | 162.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 532 | 255.00 | 376.00 | 163.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 533 | 256.00 | 376.00 | 164.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 534 | 257.00 | 376.00 | 165.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 535 | 258.00 | 376.00 | 166.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 536 | 259.00 | 376.00 | 167.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 537 | 260.00 | 376.00 | 168.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 538 | 261.00 | 376.00 | 169.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 539 | 262.00 | 376.00 | 170.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 540 | 263.00 | 376.00 | 171.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 541 | 264.00 | 376.00 | 172.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 542 | 265.00 | 376.00 | 173.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 543 | 266.00 | 376.00 | 174.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 544 | 267.00 | 376.00 | 175.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 545 | 268.00 | 376.00 | 176.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 546 | 269.00 | 376.00 | 177.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 547 | 270.00 | 376.00 | 178.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 548 | 271.00 | 376.00 | 179.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 549 | 272.00 | 376.00 | 180.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 550 | 273.00 | 376.00 | 181.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 551 | 274.00 | 376.00 | 182.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 552 | 275.00 | 376.00 | 183.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 553 | 276.00 | 376.00 | 184.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 554 | 277.00 | 376.00 | 185.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 555 | 278.00 | 376.00 | 186.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 556 | 279.00 | 376.00 | 187.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 557 | 280.00 | 376.00 | 188.00 | 3.29 | NÃO | fora do lado solicitado |
| 558 | 281.00 | 376.00 | 189.00 | 3.29 | NÃO | fora do lado solicitado |
| 559 | 282.00 | 376.00 | 190.00 | 3.29 | NÃO | fora do lado solicitado |
| 560 | 283.00 | 376.00 | 191.00 | 3.29 | NÃO | fora do lado solicitado |
| 561 | 284.00 | 376.00 | 192.00 | 3.29 | NÃO | fora do lado solicitado |
| 562 | 285.00 | 376.00 | 193.00 | 3.29 | NÃO | fora do lado solicitado |
| 563 | 286.00 | 376.00 | 194.00 | 3.29 | NÃO | fora do lado solicitado |
| 564 | 287.00 | 376.00 | 195.00 | 3.29 | NÃO | fora do lado solicitado |
| 565 | 288.00 | 376.00 | 196.00 | 3.29 | NÃO | fora do lado solicitado |
| 566 | 289.00 | 376.00 | 197.00 | 3.29 | NÃO | fora do lado solicitado |
| 567 | 290.00 | 376.00 | 198.00 | 3.29 | NÃO | fora do lado solicitado |
| 568 | 291.00 | 376.00 | 199.00 | 3.29 | NÃO | fora do lado solicitado |
| 569 | 292.00 | 376.00 | 200.00 | 3.29 | NÃO | fora do lado solicitado |
| 570 | 293.00 | 376.00 | 201.00 | 3.29 | NÃO | fora do lado solicitado |
| 571 | 294.00 | 376.00 | 202.00 | 3.29 | NÃO | fora do lado solicitado |
| 572 | 295.00 | 376.00 | 203.00 | 3.29 | NÃO | fora do lado solicitado |
| 573 | 296.00 | 376.00 | 204.00 | 3.29 | NÃO | fora do lado solicitado |
| 574 | 297.00 | 376.00 | 205.00 | 3.29 | NÃO | fora do lado solicitado |
| 575 | 298.00 | 376.00 | 206.00 | 3.29 | NÃO | fora do lado solicitado |
| 576 | 299.00 | 376.00 | 207.00 | 3.29 | NÃO | fora do lado solicitado |
| 577 | 300.00 | 376.00 | 208.00 | 3.29 | NÃO | fora do lado solicitado |
| 578 | 301.00 | 376.00 | 209.00 | 3.29 | NÃO | fora do lado solicitado |
| 579 | 302.00 | 376.00 | 210.00 | 3.29 | NÃO | fora do lado solicitado |
| 580 | 303.00 | 376.00 | 211.00 | 3.29 | NÃO | fora do lado solicitado |
| 581 | 304.00 | 376.00 | 212.00 | 3.29 | NÃO | fora do lado solicitado |
| 582 | 305.00 | 376.00 | 213.00 | 3.29 | NÃO | fora do lado solicitado |
| 583 | 306.00 | 376.00 | 214.00 | 3.29 | NÃO | fora do lado solicitado |
| 584 | 307.00 | 376.00 | 215.00 | 3.29 | NÃO | fora do lado solicitado |
| 585 | 308.00 | 376.00 | 216.00 | 3.29 | NÃO | fora do lado solicitado |
| 586 | 309.00 | 376.00 | 217.00 | 3.29 | NÃO | fora do lado solicitado |
| 587 | 310.00 | 376.00 | 218.00 | 3.29 | NÃO | fora do lado solicitado |
| 588 | 311.00 | 376.00 | 219.00 | 3.29 | NÃO | fora do lado solicitado |
| 589 | 312.00 | 376.00 | 220.00 | 3.29 | NÃO | fora do lado solicitado |
| 590 | 313.00 | 376.00 | 221.00 | 3.29 | NÃO | fora do lado solicitado |
| 591 | 314.00 | 376.00 | 222.00 | 3.29 | NÃO | fora do lado solicitado |
| 592 | 315.00 | 376.00 | 223.00 | 3.29 | NÃO | fora do lado solicitado |
| 593 | 316.00 | 376.00 | 224.00 | 3.29 | NÃO | fora do lado solicitado |
| 594 | 317.00 | 376.00 | 225.00 | 3.29 | NÃO | fora do lado solicitado |
| 595 | 318.00 | 376.00 | 226.00 | 3.29 | NÃO | fora do lado solicitado |
| 596 | 319.00 | 376.00 | 227.00 | 3.29 | NÃO | fora do lado solicitado |
| 597 | 320.00 | 376.00 | 228.00 | 3.29 | NÃO | fora do lado solicitado |
| 598 | 321.00 | 376.00 | 229.00 | 3.29 | NÃO | fora do lado solicitado |
| 599 | 322.00 | 376.00 | 230.00 | 3.29 | NÃO | fora do lado solicitado |
| 600 | 323.00 | 376.00 | 231.00 | 3.29 | NÃO | fora do lado solicitado |
| 601 | 324.00 | 376.00 | 232.00 | 3.29 | NÃO | fora do lado solicitado |
| 602 | 325.00 | 376.00 | 233.00 | 3.29 | NÃO | fora do lado solicitado |
| 603 | 326.00 | 376.00 | 234.00 | 3.29 | NÃO | fora do lado solicitado |
| 604 | 327.00 | 376.00 | 235.00 | 3.29 | NÃO | fora do lado solicitado |
| 605 | 328.00 | 376.00 | 236.00 | 3.29 | NÃO | fora do lado solicitado |
| 606 | 329.00 | 376.00 | 237.00 | 3.29 | NÃO | fora do lado solicitado |
| 607 | 330.00 | 376.00 | 238.00 | 3.29 | NÃO | fora do lado solicitado |
| 608 | 331.00 | 376.00 | 239.00 | 3.29 | NÃO | fora do lado solicitado |
| 609 | 332.00 | 376.00 | 240.00 | 3.29 | NÃO | fora do lado solicitado |
| 610 | 333.00 | 376.00 | 241.00 | 3.29 | NÃO | fora do lado solicitado |
| 611 | 334.00 | 376.00 | 242.00 | 3.29 | NÃO | fora do lado solicitado |
| 612 | 335.00 | 376.00 | 243.00 | 3.29 | NÃO | fora do lado solicitado |
| 613 | 336.00 | 376.00 | 244.00 | 3.29 | NÃO | fora do lado solicitado |
| 614 | 337.00 | 376.00 | 245.00 | 3.29 | NÃO | fora do lado solicitado |
| 615 | 338.00 | 376.00 | 246.00 | 3.29 | NÃO | fora do lado solicitado |
| 616 | 339.00 | 376.00 | 247.00 | 3.29 | NÃO | fora do lado solicitado |
| 617 | 340.00 | 376.00 | 248.00 | 3.29 | NÃO | fora do lado solicitado |
| 618 | 341.00 | 376.00 | 249.00 | 3.29 | NÃO | fora do lado solicitado |
| 619 | 342.00 | 376.00 | 250.00 | 3.29 | NÃO | fora do lado solicitado |
| 620 | 343.00 | 376.00 | 251.00 | 3.29 | NÃO | fora do lado solicitado |
| 621 | 344.00 | 376.00 | 252.00 | 3.29 | NÃO | fora do lado solicitado |
| 622 | 345.00 | 376.00 | 253.00 | 3.29 | NÃO | fora do lado solicitado |
| 623 | 346.00 | 376.00 | 254.00 | 3.29 | NÃO | fora do lado solicitado |
| 624 | 347.00 | 376.00 | 255.00 | 3.29 | NÃO | fora do lado solicitado |
| 625 | 348.00 | 376.00 | 256.00 | 3.29 | NÃO | fora do lado solicitado |
| 626 | 349.00 | 376.00 | 257.00 | 3.29 | NÃO | fora do lado solicitado |
| 627 | 350.00 | 376.00 | 258.00 | 3.29 | NÃO | fora do lado solicitado |
| 628 | 351.00 | 376.00 | 259.00 | 3.29 | NÃO | fora do lado solicitado |
| 629 | 352.00 | 376.00 | 260.00 | 3.29 | NÃO | fora do lado solicitado |
| 630 | 353.00 | 376.00 | 261.00 | 3.29 | NÃO | fora do lado solicitado |
| 631 | 354.00 | 376.00 | 262.00 | 3.29 | NÃO | fora do lado solicitado |
| 632 | 355.00 | 376.00 | 263.00 | 3.29 | NÃO | fora do lado solicitado |
| 633 | 356.00 | 376.00 | 264.00 | 3.29 | NÃO | fora do lado solicitado |
| 634 | 357.00 | 376.00 | 265.00 | 3.29 | NÃO | fora do lado solicitado |
| 635 | 358.00 | 376.00 | 266.00 | 3.29 | NÃO | fora do lado solicitado |
| 636 | 359.00 | 376.00 | 267.00 | 3.29 | NÃO | fora do lado solicitado |
| 637 | 360.00 | 376.00 | 268.00 | 3.29 | NÃO | fora do lado solicitado |
| 638 | 361.00 | 376.00 | 269.00 | 3.29 | NÃO | fora do lado solicitado |
| 639 | 362.00 | 376.00 | 270.00 | 3.29 | NÃO | fora do lado solicitado |
| 640 | 363.00 | 376.00 | 271.00 | 3.29 | NÃO | fora do lado solicitado |
| 641 | 364.00 | 376.00 | 272.00 | 3.29 | NÃO | fora do lado solicitado |
| 642 | 365.00 | 376.00 | 273.00 | 3.29 | NÃO | fora do lado solicitado |
| 643 | 366.00 | 376.00 | 274.00 | 3.29 | NÃO | fora do lado solicitado |
| 644 | 367.00 | 376.00 | 275.00 | 3.29 | NÃO | fora do lado solicitado |
| 645 | 368.00 | 376.00 | 276.00 | 3.29 | NÃO | fora do lado solicitado |
| 646 | 369.00 | 376.00 | 277.00 | 3.29 | NÃO | fora do lado solicitado |
| 647 | 370.00 | 376.00 | 278.00 | 3.29 | NÃO | fora do lado solicitado |
| 648 | 371.00 | 376.00 | 279.00 | 3.29 | NÃO | fora do lado solicitado |
| 649 | 372.00 | 376.00 | 280.00 | 3.29 | NÃO | fora do lado solicitado |
| 650 | 373.00 | 376.00 | 281.00 | 3.29 | NÃO | fora do lado solicitado |
| 651 | 374.00 | 376.00 | 282.00 | 3.29 | NÃO | fora do lado solicitado |
| 652 | 375.00 | 376.00 | 283.00 | 3.29 | NÃO | fora do lado solicitado |
| 653 | 376.00 | 376.00 | 284.00 | 3.29 | NÃO | fora do lado solicitado |
| 654 | 377.00 | 376.00 | 285.00 | 3.29 | NÃO | fora do lado solicitado |
| 655 | 378.00 | 376.00 | 286.00 | 3.29 | NÃO | fora do lado solicitado |
| 656 | 379.00 | 376.00 | 287.00 | 3.29 | NÃO | fora do lado solicitado |
| 657 | 380.00 | 376.00 | 288.00 | 3.29 | NÃO | fora do lado solicitado |
| 658 | 381.00 | 376.00 | 289.00 | 3.29 | NÃO | fora do lado solicitado |
| 659 | 382.00 | 376.00 | 290.00 | 3.29 | NÃO | fora do lado solicitado |
| 660 | 383.00 | 376.00 | 291.00 | 3.29 | NÃO | fora do lado solicitado |
| 661 | 384.00 | 376.00 | 292.00 | 3.29 | NÃO | fora do lado solicitado |
| 662 | 385.00 | 376.00 | 293.00 | 3.29 | NÃO | fora do lado solicitado |
| 663 | 386.00 | 376.00 | 294.00 | 3.29 | NÃO | fora do lado solicitado |
| 664 | 387.00 | 376.00 | 295.00 | 3.29 | NÃO | fora do lado solicitado |
| 665 | 388.00 | 376.00 | 296.00 | 3.29 | NÃO | fora do lado solicitado |
| 666 | 389.00 | 376.00 | 297.00 | 3.29 | NÃO | fora do lado solicitado |
| 667 | 390.00 | 376.00 | 298.00 | 3.29 | NÃO | fora do lado solicitado |
| 668 | 391.00 | 376.00 | 299.00 | 3.29 | NÃO | fora do lado solicitado |
| 669 | 392.00 | 376.00 | 300.00 | 3.29 | NÃO | fora do lado solicitado |
| 670 | 393.00 | 376.00 | 301.00 | 3.29 | NÃO | fora do lado solicitado |
| 671 | 394.00 | 376.00 | 302.00 | 3.29 | NÃO | fora do lado solicitado |
| 672 | 395.00 | 376.00 | 303.00 | 3.29 | NÃO | fora do lado solicitado |
| 673 | 396.00 | 376.00 | 304.00 | 3.29 | NÃO | fora do lado solicitado |
| 674 | 397.00 | 376.00 | 305.00 | 3.29 | NÃO | fora do lado solicitado |
| 675 | 398.00 | 376.00 | 306.00 | 3.29 | NÃO | fora do lado solicitado |
| 676 | 399.00 | 376.00 | 307.00 | 3.29 | NÃO | fora do lado solicitado |
| 677 | 400.00 | 376.00 | 308.00 | 3.29 | NÃO | fora do lado solicitado |
| 678 | 401.00 | 376.00 | 309.00 | 3.29 | NÃO | fora do lado solicitado |
| 679 | 402.00 | 376.00 | 310.00 | 3.29 | NÃO | fora do lado solicitado |
| 680 | 403.00 | 376.00 | 311.00 | 3.29 | NÃO | fora do lado solicitado |
| 681 | 404.00 | 376.00 | 312.00 | 3.29 | NÃO | fora do lado solicitado |
| 682 | 405.00 | 376.00 | 313.00 | 3.29 | NÃO | fora do lado solicitado |
| 683 | 406.00 | 376.00 | 314.00 | 3.29 | NÃO | fora do lado solicitado |
| 684 | 407.00 | 376.00 | 315.00 | 3.29 | NÃO | fora do lado solicitado |
| 685 | 408.00 | 376.00 | 316.00 | 3.29 | NÃO | fora do lado solicitado |
| 686 | 409.00 | 376.00 | 317.00 | 3.29 | NÃO | fora do lado solicitado |
| 687 | 410.00 | 376.00 | 318.00 | 3.29 | NÃO | fora do lado solicitado |
| 688 | 411.00 | 376.00 | 319.00 | 3.29 | NÃO | fora do lado solicitado |
| 689 | 412.00 | 376.00 | 320.00 | 3.29 | NÃO | fora do lado solicitado |
| 690 | 413.00 | 376.00 | 321.00 | 3.29 | NÃO | fora do lado solicitado |
| 691 | 414.00 | 376.00 | 322.00 | 3.29 | NÃO | fora do lado solicitado |
| 692 | 415.00 | 376.00 | 323.00 | 3.29 | NÃO | fora do lado solicitado |
| 693 | 416.00 | 376.00 | 324.00 | 3.29 | NÃO | fora do lado solicitado |
| 694 | 417.00 | 376.00 | 325.00 | 3.29 | NÃO | fora do lado solicitado |
| 695 | 418.00 | 376.00 | 326.00 | 3.29 | NÃO | fora do lado solicitado |
| 696 | 419.00 | 376.00 | 327.00 | 3.29 | NÃO | fora do lado solicitado |
| 697 | 420.00 | 376.00 | 328.00 | 3.29 | NÃO | fora do lado solicitado |
| 698 | 421.00 | 376.00 | 329.00 | 3.29 | NÃO | fora do lado solicitado |
| 699 | 422.00 | 376.00 | 330.00 | 3.29 | NÃO | fora do lado solicitado |
| 700 | 423.00 | 376.00 | 331.00 | 3.29 | NÃO | fora do lado solicitado |
| 701 | 424.00 | 376.00 | 332.00 | 3.29 | NÃO | fora do lado solicitado |
| 702 | 425.00 | 376.00 | 333.00 | 3.29 | NÃO | fora do lado solicitado |
| 703 | 426.00 | 376.00 | 334.00 | 3.29 | NÃO | fora do lado solicitado |
| 704 | 427.00 | 376.00 | 335.00 | 3.29 | NÃO | fora do lado solicitado |
| 705 | 428.00 | 376.00 | 336.00 | 3.29 | NÃO | fora do lado solicitado |
| 706 | 429.00 | 376.00 | 337.00 | 3.29 | NÃO | fora do lado solicitado |
| 707 | 430.00 | 376.00 | 338.00 | 3.29 | NÃO | fora do lado solicitado |
| 708 | 431.00 | 376.00 | 339.00 | 3.29 | NÃO | fora do lado solicitado |
| 709 | 432.00 | 376.00 | 340.00 | 3.29 | NÃO | fora do lado solicitado |
| 710 | 433.00 | 376.00 | 341.00 | 3.29 | NÃO | fora do lado solicitado |
| 711 | 434.00 | 376.00 | 342.00 | 3.29 | NÃO | fora do lado solicitado |
| 712 | 435.00 | 376.00 | 343.00 | 3.29 | NÃO | fora do lado solicitado |
| 713 | 436.00 | 376.00 | 344.00 | 3.29 | NÃO | fora do lado solicitado |
| 714 | 437.00 | 376.00 | 345.00 | 3.29 | NÃO | fora do lado solicitado |
| 715 | 438.00 | 376.00 | 346.00 | 3.29 | NÃO | fora do lado solicitado |
| 716 | 439.00 | 376.00 | 347.00 | 3.29 | NÃO | fora do lado solicitado |
| 717 | 439.00 | 375.00 | 347.00 | 4.29 | NÃO | fora do lado solicitado |
| 718 | 440.00 | 374.00 | 348.01 | 5.29 | NÃO | fora do lado solicitado |
| 719 | 440.00 | 373.00 | 348.01 | 6.29 | NÃO | fora do lado solicitado |
| 720 | 441.00 | 372.00 | 349.02 | 7.29 | NÃO | fora do lado solicitado |
| 721 | 442.00 | 371.00 | 350.04 | 8.29 | NÃO | fora do lado solicitado |
| 722 | 443.00 | 370.00 | 351.05 | 9.29 | NÃO | fora do lado solicitado |
| 723 | 443.00 | 369.00 | 351.07 | 10.29 | NÃO | fora do lado solicitado |
| 724 | 444.00 | 368.00 | 352.09 | 11.29 | NÃO | fora do lado solicitado |
| 725 | 445.00 | 367.00 | 353.11 | 12.29 | NÃO | fora do lado solicitado |
| 726 | 446.00 | 366.00 | 354.14 | 13.29 | NÃO | fora do lado solicitado |
| 727 | 446.00 | 365.00 | 354.17 | 14.29 | NÃO | fora do lado solicitado |
| 728 | 447.00 | 364.00 | 355.20 | 15.29 | NÃO | fora do lado solicitado |
| 729 | 448.00 | 363.00 | 356.24 | 16.29 | NÃO | fora do lado solicitado |
| 730 | 448.00 | 362.00 | 356.28 | 17.29 | NÃO | fora do lado solicitado |
| 731 | 449.00 | 361.00 | 357.31 | 18.29 | NÃO | fora do lado solicitado |
| 732 | 450.00 | 360.00 | 358.36 | 19.29 | NÃO | fora do lado solicitado |
| 733 | 450.00 | 359.00 | 358.40 | 20.29 | NÃO | fora do lado solicitado |
| 734 | 451.00 | 358.00 | 359.45 | 21.29 | NÃO | fora do lado solicitado |
| 735 | 451.00 | 357.00 | 359.50 | 22.29 | NÃO | fora do lado solicitado |
| 736 | 452.00 | 356.00 | 360.56 | 23.29 | NÃO | fora do lado solicitado |
| 737 | 453.00 | 355.00 | 361.61 | 24.29 | NÃO | fora do lado solicitado |
| 738 | 453.00 | 354.00 | 361.67 | 25.29 | NÃO | fora do lado solicitado |
| 739 | 454.00 | 353.00 | 362.73 | 26.29 | NÃO | fora do lado solicitado |
| 740 | 454.00 | 352.00 | 362.79 | 27.29 | NÃO | fora do lado solicitado |
| 741 | 455.00 | 351.00 | 363.86 | 28.29 | NÃO | fora do lado solicitado |
| 742 | 456.00 | 350.00 | 364.93 | 29.29 | NÃO | fora do lado solicitado |
| 743 | 456.00 | 349.00 | 365.00 | 30.29 | NÃO | fora do lado solicitado |
| 744 | 457.00 | 348.00 | 366.07 | 31.29 | NÃO | fora do lado solicitado |
| 745 | 457.00 | 347.00 | 366.15 | 32.29 | NÃO | fora do lado solicitado |
| 746 | 458.00 | 346.00 | 367.23 | 33.29 | NÃO | fora do lado solicitado |
| 747 | 458.00 | 345.00 | 367.31 | 34.29 | NÃO | fora do lado solicitado |
| 748 | 459.00 | 344.00 | 368.39 | 35.29 | NÃO | fora do lado solicitado |
| 749 | 459.00 | 343.00 | 368.48 | 36.29 | NÃO | fora do lado solicitado |
| 750 | 460.00 | 342.00 | 369.57 | 37.29 | NÃO | fora do lado solicitado |
| 751 | 460.00 | 341.00 | 369.66 | 38.29 | NÃO | fora do lado solicitado |
| 752 | 461.00 | 340.00 | 370.75 | 39.29 | NÃO | fora do lado solicitado |
| 753 | 461.00 | 339.00 | 370.85 | 40.29 | NÃO | fora do lado solicitado |
| 754 | 462.00 | 338.00 | 371.95 | 41.29 | NÃO | fora do lado solicitado |
| 755 | 462.00 | 337.00 | 372.05 | 42.29 | NÃO | fora do lado solicitado |
| 756 | 463.00 | 336.00 | 373.15 | 43.29 | NÃO | fora do lado solicitado |
| 757 | 463.00 | 335.00 | 373.26 | 44.29 | NÃO | fora do lado solicitado |
| 758 | 464.00 | 334.00 | 374.36 | 45.29 | NÃO | fora do lado solicitado |
| 759 | 464.00 | 333.00 | 374.48 | 46.29 | NÃO | fora do lado solicitado |
| 760 | 465.00 | 332.00 | 375.59 | 47.29 | NÃO | fora do lado solicitado |
| 761 | 465.00 | 331.00 | 375.70 | 48.29 | NÃO | fora do lado solicitado |
| 762 | 466.00 | 330.00 | 376.82 | 49.29 | NÃO | fora do lado solicitado |
| 763 | 466.00 | 329.00 | 376.94 | 50.29 | NÃO | fora do lado solicitado |
| 764 | 467.00 | 328.00 | 378.06 | 51.29 | NÃO | fora do lado solicitado |
| 765 | 467.00 | 327.00 | 378.19 | 52.29 | NÃO | fora do lado solicitado |
| 766 | 468.00 | 326.00 | 379.31 | 53.29 | NÃO | fora do lado solicitado |
| 767 | 468.00 | 325.00 | 379.44 | 54.29 | NÃO | fora do lado solicitado |
| 768 | 468.00 | 324.00 | 379.58 | 55.29 | NÃO | fora do lado solicitado |
| 769 | 469.00 | 323.00 | 380.71 | 56.29 | NÃO | fora do lado solicitado |
| 770 | 469.00 | 322.00 | 380.85 | 57.29 | NÃO | fora do lado solicitado |
| 771 | 469.00 | 321.00 | 380.99 | 58.29 | NÃO | fora do lado solicitado |
| 772 | 470.00 | 320.00 | 382.13 | 59.29 | NÃO | fora do lado solicitado |
| 773 | 470.00 | 319.00 | 382.27 | 60.29 | NÃO | fora do lado solicitado |
| 774 | 471.00 | 318.00 | 383.41 | 61.29 | NÃO | fora do lado solicitado |
| 775 | 471.00 | 317.00 | 383.56 | 62.29 | NÃO | fora do lado solicitado |
| 776 | 471.00 | 316.00 | 383.72 | 63.29 | NÃO | fora do lado solicitado |
| 777 | 472.00 | 315.00 | 384.86 | 64.29 | NÃO | fora do lado solicitado |
| 778 | 472.00 | 314.00 | 385.02 | 65.29 | NÃO | fora do lado solicitado |
| 779 | 472.00 | 313.00 | 385.19 | 66.29 | NÃO | fora do lado solicitado |
| 780 | 473.00 | 312.00 | 386.34 | 67.29 | NÃO | fora do lado solicitado |
| 781 | 473.00 | 311.00 | 386.50 | 68.29 | NÃO | fora do lado solicitado |
| 782 | 473.00 | 310.00 | 386.67 | 69.29 | NÃO | fora do lado solicitado |
| 783 | 473.00 | 309.00 | 386.85 | 70.29 | NÃO | fora do lado solicitado |
| 784 | 474.00 | 308.00 | 388.01 | 71.29 | NÃO | fora do lado solicitado |
| 785 | 474.00 | 307.00 | 388.18 | 72.29 | NÃO | fora do lado solicitado |
| 786 | 474.00 | 306.00 | 388.36 | 73.29 | NÃO | fora do lado solicitado |
| 787 | 475.00 | 305.00 | 389.53 | 74.29 | NÃO | fora do lado solicitado |
| 788 | 475.00 | 304.00 | 389.71 | 75.29 | NÃO | fora do lado solicitado |
| 789 | 475.00 | 303.00 | 389.89 | 76.29 | NÃO | fora do lado solicitado |
| 790 | 475.00 | 302.00 | 390.08 | 77.29 | NÃO | fora do lado solicitado |
| 791 | 476.00 | 301.00 | 391.26 | 78.29 | NÃO | fora do lado solicitado |
| 792 | 476.00 | 300.00 | 391.45 | 79.29 | NÃO | fora do lado solicitado |
| 793 | 476.00 | 299.00 | 391.64 | 80.29 | NÃO | fora do lado solicitado |
| 794 | 476.00 | 298.00 | 391.84 | 81.29 | NÃO | fora do lado solicitado |
| 795 | 477.00 | 297.00 | 393.02 | 82.29 | NÃO | fora do lado solicitado |
| 796 | 477.00 | 296.00 | 393.22 | 83.29 | NÃO | fora do lado solicitado |
| 797 | 477.00 | 295.00 | 393.43 | 84.29 | NÃO | fora do lado solicitado |
| 798 | 477.00 | 294.00 | 393.64 | 85.29 | NÃO | fora do lado solicitado |
| 799 | 478.00 | 293.00 | 394.82 | 86.29 | NÃO | fora do lado solicitado |
| 800 | 478.00 | 292.00 | 395.03 | 87.29 | NÃO | fora do lado solicitado |
| 801 | 478.00 | 291.00 | 395.25 | 88.29 | NÃO | fora do lado solicitado |
| 802 | 478.00 | 290.00 | 395.46 | 89.29 | NÃO | fora do lado solicitado |
| 803 | 478.00 | 289.00 | 395.68 | 90.29 | NÃO | fora do lado solicitado |
| 804 | 479.00 | 288.00 | 396.88 | 91.29 | NÃO | fora do lado solicitado |
| 805 | 479.00 | 287.00 | 397.10 | 92.29 | NÃO | fora do lado solicitado |
| 806 | 479.00 | 286.00 | 397.33 | 93.29 | NÃO | fora do lado solicitado |
| 807 | 479.00 | 285.00 | 397.56 | 94.29 | NÃO | fora do lado solicitado |
| 808 | 479.00 | 284.00 | 397.79 | 95.29 | NÃO | fora do lado solicitado |
| 809 | 480.00 | 283.00 | 398.99 | 96.29 | NÃO | fora do lado solicitado |
| 810 | 480.00 | 282.00 | 399.22 | 97.29 | NÃO | fora do lado solicitado |
| 811 | 480.00 | 281.00 | 399.46 | 98.29 | NÃO | fora do lado solicitado |
| 812 | 480.00 | 280.00 | 399.70 | 99.29 | NÃO | fora do lado solicitado |
| 813 | 480.00 | 279.00 | 399.94 | 100.29 | NÃO | fora do lado solicitado |
| 814 | 480.00 | 278.00 | 400.18 | 101.29 | NÃO | fora do lado solicitado |
| 815 | 480.00 | 277.00 | 400.43 | 102.29 | NÃO | fora do lado solicitado |
| 816 | 481.00 | 276.00 | 401.65 | 103.29 | NÃO | fora do lado solicitado |
| 817 | 481.00 | 275.00 | 401.90 | 104.29 | NÃO | fora do lado solicitado |
| 818 | 481.00 | 274.00 | 402.15 | 105.29 | NÃO | fora do lado solicitado |
| 819 | 481.00 | 273.00 | 402.41 | 106.29 | NÃO | fora do lado solicitado |
| 820 | 481.00 | 272.00 | 402.66 | 107.29 | NÃO | fora do lado solicitado |
| 821 | 481.00 | 271.00 | 402.92 | 108.29 | NÃO | fora do lado solicitado |
| 822 | 481.00 | 270.00 | 403.18 | 109.29 | NÃO | fora do lado solicitado |
| 823 | 481.00 | 269.00 | 403.45 | 110.29 | NÃO | fora do lado solicitado |
| 824 | 482.00 | 268.00 | 404.68 | 111.29 | NÃO | fora do lado solicitado |
| 825 | 482.00 | 267.00 | 404.95 | 112.29 | NÃO | fora do lado solicitado |
| 826 | 482.00 | 266.00 | 405.22 | 113.29 | NÃO | fora do lado solicitado |
| 827 | 482.00 | 265.00 | 405.49 | 114.29 | NÃO | fora do lado solicitado |
| 828 | 482.00 | 264.00 | 405.76 | 115.29 | NÃO | fora do lado solicitado |
| 829 | 482.00 | 263.00 | 406.04 | 116.29 | NÃO | fora do lado solicitado |
| 830 | 482.00 | 262.00 | 406.32 | 117.29 | NÃO | fora do lado solicitado |
| 831 | 482.00 | 261.00 | 406.60 | 118.29 | NÃO | fora do lado solicitado |
| 832 | 482.00 | 260.00 | 406.89 | 119.29 | NÃO | fora do lado solicitado |
| 833 | 482.00 | 259.00 | 407.17 | 120.29 | NÃO | fora do lado solicitado |
| 834 | 482.00 | 258.00 | 407.46 | 121.29 | NÃO | fora do lado solicitado |
| 835 | 482.00 | 257.00 | 407.75 | 122.29 | NÃO | fora do lado solicitado |
| 836 | 482.00 | 256.00 | 408.04 | 123.29 | NÃO | fora do lado solicitado |
| 837 | 482.00 | 255.00 | 408.34 | 124.29 | NÃO | fora do lado solicitado |
| 838 | 482.00 | 254.00 | 408.64 | 125.29 | NÃO | fora do lado solicitado |
| 839 | 482.00 | 253.00 | 408.94 | 126.29 | NÃO | fora do lado solicitado |
| 840 | 482.00 | 252.00 | 409.24 | 127.29 | NÃO | fora do lado solicitado |
| 841 | 482.00 | 251.00 | 409.54 | 128.29 | NÃO | fora do lado solicitado |
| 842 | 482.00 | 250.00 | 409.85 | 129.29 | NÃO | fora do lado solicitado |
| 843 | 482.00 | 249.00 | 410.16 | 130.29 | NÃO | fora do lado solicitado |
| 844 | 482.00 | 248.00 | 410.47 | 131.29 | NÃO | fora do lado solicitado |
| 845 | 482.00 | 247.00 | 410.78 | 132.29 | NÃO | fora do lado solicitado |
| 846 | 482.00 | 246.00 | 411.10 | 133.29 | NÃO | fora do lado solicitado |
| 847 | 482.00 | 245.00 | 411.41 | 134.29 | NÃO | fora do lado solicitado |
| 848 | 482.00 | 244.00 | 411.73 | 135.29 | NÃO | fora do lado solicitado |
| 849 | 482.00 | 243.00 | 412.05 | 136.29 | NÃO | fora do lado solicitado |
| 850 | 482.00 | 242.00 | 412.38 | 137.29 | NÃO | fora do lado solicitado |
| 851 | 482.00 | 241.00 | 412.70 | 138.29 | NÃO | fora do lado solicitado |
| 852 | 482.00 | 240.00 | 413.03 | 139.29 | NÃO | fora do lado solicitado |
| 853 | 482.00 | 239.00 | 413.36 | 140.29 | NÃO | fora do lado solicitado |
| 854 | 482.00 | 238.00 | 413.70 | 141.29 | NÃO | fora do lado solicitado |
| 855 | 482.00 | 237.00 | 414.03 | 142.29 | NÃO | fora do lado solicitado |
| 856 | 482.00 | 236.00 | 414.37 | 143.29 | NÃO | fora do lado solicitado |
| 857 | 482.00 | 235.00 | 414.71 | 144.29 | NÃO | fora do lado solicitado |
| 858 | 482.00 | 234.00 | 415.05 | 145.29 | NÃO | fora do lado solicitado |
| 859 | 482.00 | 233.00 | 415.39 | 146.29 | NÃO | fora do lado solicitado |
| 860 | 482.00 | 232.00 | 415.74 | 147.29 | NÃO | fora do lado solicitado |
| 861 | 481.00 | 231.00 | 415.15 | 148.29 | NÃO | fora do lado solicitado |
| 862 | 481.00 | 230.00 | 415.50 | 149.29 | NÃO | fora do lado solicitado |
| 863 | 481.00 | 229.00 | 415.85 | 150.29 | NÃO | fora do lado solicitado |
| 864 | 481.00 | 228.00 | 416.20 | 151.29 | NÃO | fora do lado solicitado |
| 865 | 481.00 | 227.00 | 416.56 | 152.29 | NÃO | fora do lado solicitado |
| 866 | 481.00 | 226.00 | 416.92 | 153.29 | NÃO | fora do lado solicitado |
| 867 | 481.00 | 225.00 | 417.28 | 154.29 | NÃO | fora do lado solicitado |
| 868 | 481.00 | 224.00 | 417.64 | 155.29 | NÃO | fora do lado solicitado |
| 869 | 480.00 | 223.00 | 417.08 | 156.29 | NÃO | fora do lado solicitado |
| 870 | 480.00 | 222.00 | 417.44 | 157.29 | NÃO | fora do lado solicitado |
| 871 | 480.00 | 221.00 | 417.81 | 158.29 | NÃO | fora do lado solicitado |
| 872 | 480.00 | 220.00 | 418.19 | 159.29 | NÃO | fora do lado solicitado |
| 873 | 480.00 | 219.00 | 418.56 | 160.29 | NÃO | fora do lado solicitado |
| 874 | 480.00 | 218.00 | 418.94 | 161.29 | NÃO | fora do lado solicitado |
| 875 | 480.00 | 217.00 | 419.31 | 162.29 | NÃO | fora do lado solicitado |
| 876 | 480.00 | 216.00 | 419.70 | 163.29 | NÃO | fora do lado solicitado |
| 877 | 479.00 | 215.00 | 419.15 | 164.29 | NÃO | fora do lado solicitado |
| 878 | 479.00 | 214.00 | 419.54 | 165.29 | NÃO | fora do lado solicitado |
| 879 | 479.00 | 213.00 | 419.93 | 166.29 | NÃO | fora do lado solicitado |
| 880 | 479.00 | 212.00 | 420.32 | 167.29 | NÃO | fora do lado solicitado |
| 881 | 479.00 | 211.00 | 420.71 | 168.29 | NÃO | fora do lado solicitado |
| 882 | 478.00 | 210.00 | 420.18 | 169.29 | NÃO | fora do lado solicitado |
| 883 | 478.00 | 209.00 | 420.58 | 170.29 | NÃO | fora do lado solicitado |
| 884 | 478.00 | 208.00 | 420.98 | 171.29 | NÃO | fora do lado solicitado |
| 885 | 478.00 | 207.00 | 421.38 | 172.29 | NÃO | fora do lado solicitado |
| 886 | 477.00 | 206.00 | 420.86 | 173.29 | NÃO | fora do lado solicitado |
| 887 | 477.00 | 205.00 | 421.27 | 174.29 | NÃO | fora do lado solicitado |
| 888 | 477.00 | 204.00 | 421.67 | 175.29 | NÃO | fora do lado solicitado |
| 889 | 477.00 | 203.00 | 422.08 | 176.29 | NÃO | fora do lado solicitado |
| 890 | 477.00 | 202.00 | 422.49 | 177.29 | NÃO | fora do lado solicitado |
| 891 | 476.00 | 201.00 | 422.00 | 178.29 | NÃO | fora do lado solicitado |
| 892 | 476.00 | 200.00 | 422.41 | 179.29 | NÃO | fora do lado solicitado |
| 893 | 476.00 | 199.00 | 422.83 | 180.29 | NÃO | fora da faixa vertical |
| 894 | 476.00 | 198.00 | 423.25 | 181.29 | NÃO | fora da faixa vertical |
| 895 | 475.00 | 197.00 | 422.76 | 182.29 | NÃO | fora da faixa vertical |
| 896 | 475.00 | 196.00 | 423.19 | 183.29 | NÃO | fora da faixa vertical |
| 897 | 475.00 | 195.00 | 423.62 | 184.29 | NÃO | fora da faixa vertical |
| 898 | 475.00 | 194.00 | 424.04 | 185.29 | NÃO | fora da faixa vertical |
| 899 | 474.00 | 193.00 | 423.57 | 186.29 | NÃO | fora da faixa vertical |
| 900 | 474.00 | 192.00 | 424.00 | 187.29 | NÃO | fora da faixa vertical |
| 901 | 474.00 | 191.00 | 424.44 | 188.29 | NÃO | fora da faixa vertical |
| 902 | 473.00 | 190.00 | 423.98 | 189.29 | NÃO | fora da faixa vertical |
| 903 | 473.00 | 189.00 | 424.42 | 190.29 | NÃO | fora da faixa vertical |
| 904 | 473.00 | 188.00 | 424.86 | 191.29 | NÃO | fora da faixa vertical |
| 905 | 473.00 | 187.00 | 425.30 | 192.29 | NÃO | fora da faixa vertical |
| 906 | 472.00 | 186.00 | 424.85 | 193.29 | NÃO | fora da faixa vertical |
| 907 | 472.00 | 185.00 | 425.30 | 194.29 | NÃO | fora da faixa vertical |
| 908 | 472.00 | 184.00 | 425.75 | 195.29 | NÃO | fora da faixa vertical |
| 909 | 471.00 | 183.00 | 425.31 | 196.29 | NÃO | fora da faixa vertical |
| 910 | 471.00 | 182.00 | 425.77 | 197.29 | NÃO | fora da faixa vertical |
| 911 | 470.00 | 181.00 | 425.33 | 198.29 | NÃO | fora da faixa vertical |
| 912 | 470.00 | 180.00 | 425.79 | 199.29 | NÃO | fora da faixa vertical |
| 913 | 470.00 | 179.00 | 426.25 | 200.29 | NÃO | fora da faixa vertical |
| 914 | 469.00 | 178.00 | 425.83 | 201.29 | NÃO | fora da faixa vertical |
| 915 | 469.00 | 177.00 | 426.30 | 202.29 | NÃO | fora da faixa vertical |
| 916 | 469.00 | 176.00 | 426.77 | 203.29 | NÃO | fora da faixa vertical |
| 917 | 468.00 | 175.00 | 426.35 | 204.29 | NÃO | fora da faixa vertical |
| 918 | 468.00 | 174.00 | 426.83 | 205.29 | NÃO | fora da faixa vertical |
| 919 | 467.00 | 173.00 | 426.42 | 206.29 | NÃO | fora da faixa vertical |
| 920 | 467.00 | 172.00 | 426.90 | 207.29 | NÃO | fora da faixa vertical |
| 921 | 467.00 | 171.00 | 427.38 | 208.29 | NÃO | fora da faixa vertical |
| 922 | 466.00 | 170.00 | 426.98 | 209.29 | NÃO | fora da faixa vertical |
| 923 | 466.00 | 169.00 | 427.46 | 210.29 | NÃO | fora da faixa vertical |
| 924 | 465.00 | 168.00 | 427.07 | 211.29 | NÃO | fora da faixa vertical |
| 925 | 465.00 | 167.00 | 427.56 | 212.29 | NÃO | fora da faixa vertical |
| 926 | 464.00 | 166.00 | 427.18 | 213.29 | NÃO | fora da faixa vertical |
| 927 | 464.00 | 165.00 | 427.67 | 214.29 | NÃO | fora da faixa vertical |
| 928 | 463.00 | 164.00 | 427.30 | 215.29 | NÃO | fora da faixa vertical |
| 929 | 463.00 | 163.00 | 427.80 | 216.29 | NÃO | fora da faixa vertical |
| 930 | 462.00 | 162.00 | 427.43 | 217.29 | NÃO | fora da faixa vertical |
| 931 | 462.00 | 161.00 | 427.93 | 218.29 | NÃO | fora da faixa vertical |
| 932 | 461.00 | 160.00 | 427.57 | 219.29 | NÃO | fora da faixa vertical |
| 933 | 461.00 | 159.00 | 428.08 | 220.29 | NÃO | fora da faixa vertical |
| 934 | 460.00 | 158.00 | 427.72 | 221.29 | NÃO | fora da faixa vertical |
| 935 | 460.00 | 157.00 | 428.23 | 222.29 | NÃO | fora da faixa vertical |
| 936 | 459.00 | 156.00 | 427.89 | 223.29 | NÃO | fora da faixa vertical |
| 937 | 459.00 | 155.00 | 428.40 | 224.29 | NÃO | fora da faixa vertical |
| 938 | 458.00 | 154.00 | 428.07 | 225.29 | NÃO | fora da faixa vertical |
| 939 | 458.00 | 153.00 | 428.58 | 226.29 | NÃO | fora da faixa vertical |
| 940 | 457.00 | 152.00 | 428.25 | 227.29 | NÃO | fora da faixa vertical |
| 941 | 457.00 | 151.00 | 428.78 | 228.29 | NÃO | fora da faixa vertical |
| 942 | 456.00 | 150.00 | 428.45 | 229.29 | NÃO | fora da faixa vertical |
| 943 | 455.00 | 149.00 | 428.13 | 230.29 | NÃO | fora da faixa vertical |
| 944 | 455.00 | 148.00 | 428.66 | 231.29 | NÃO | fora da faixa vertical |
| 945 | 454.00 | 147.00 | 428.35 | 232.29 | NÃO | fora da faixa vertical |
| 946 | 454.00 | 146.00 | 428.89 | 233.29 | NÃO | fora da faixa vertical |
| 947 | 453.00 | 145.00 | 428.58 | 234.29 | NÃO | fora da faixa vertical |
| 948 | 452.00 | 144.00 | 428.28 | 235.29 | NÃO | fora da faixa vertical |
| 949 | 452.00 | 143.00 | 428.82 | 236.29 | NÃO | fora da faixa vertical |
| 950 | 451.00 | 142.00 | 428.53 | 237.29 | NÃO | fora da faixa vertical |
| 951 | 451.00 | 141.00 | 429.08 | 238.29 | NÃO | fora da faixa vertical |
| 952 | 450.00 | 140.00 | 428.79 | 239.29 | NÃO | fora da faixa vertical |
| 953 | 449.00 | 139.00 | 428.51 | 240.29 | NÃO | fora da faixa vertical |
| 954 | 449.00 | 138.00 | 429.06 | 241.29 | NÃO | fora da faixa vertical |
| 955 | 448.00 | 137.00 | 428.79 | 242.29 | NÃO | fora da faixa vertical |
| 956 | 448.00 | 136.00 | 429.34 | 243.29 | NÃO | fora da faixa vertical |
| 957 | 447.00 | 135.00 | 429.08 | 244.29 | NÃO | fora da faixa vertical |
| 958 | 446.00 | 134.00 | 428.81 | 245.29 | NÃO | fora da faixa vertical |
| 959 | 445.00 | 133.00 | 428.55 | 246.29 | NÃO | fora da faixa vertical |
| 960 | 445.00 | 132.00 | 429.12 | 247.29 | NÃO | fora da faixa vertical |
| 961 | 444.00 | 131.00 | 428.87 | 248.29 | NÃO | fora da faixa vertical |
| 962 | 443.00 | 130.00 | 428.62 | 249.29 | NÃO | fora da faixa vertical |
| 963 | 442.00 | 129.00 | 428.38 | 250.29 | NÃO | fora da faixa vertical |
| 964 | 442.00 | 128.00 | 428.96 | 251.29 | NÃO | fora da faixa vertical |
| 965 | 441.00 | 127.00 | 428.72 | 252.29 | NÃO | fora da faixa vertical |
| 966 | 440.00 | 126.00 | 428.49 | 253.29 | NÃO | fora da faixa vertical |
| 967 | 439.00 | 125.00 | 428.26 | 254.29 | NÃO | fora da faixa vertical |
| 968 | 439.00 | 124.00 | 428.85 | 255.29 | NÃO | fora da faixa vertical |
| 969 | 438.00 | 123.00 | 428.63 | 256.29 | NÃO | fora da faixa vertical |
| 970 | 437.00 | 122.00 | 428.42 | 257.29 | NÃO | fora da faixa vertical |
| 971 | 436.00 | 121.00 | 428.21 | 258.29 | NÃO | fora da faixa vertical |
| 972 | 436.00 | 120.00 | 428.80 | 259.29 | NÃO | fora da faixa vertical |
| 973 | 435.00 | 119.00 | 428.60 | 260.29 | NÃO | fora da faixa vertical |
| 974 | 434.00 | 118.00 | 428.40 | 261.29 | NÃO | fora da faixa vertical |
| 975 | 433.00 | 117.00 | 428.21 | 262.29 | NÃO | fora da faixa vertical |
| 976 | 432.00 | 116.00 | 428.02 | 263.29 | NÃO | fora da faixa vertical |
| 977 | 431.00 | 115.00 | 427.83 | 264.29 | NÃO | fora da faixa vertical |
| 978 | 430.00 | 114.00 | 427.65 | 265.29 | NÃO | fora da faixa vertical |
| 979 | 429.00 | 113.00 | 427.48 | 266.29 | NÃO | fora da faixa vertical |
| 980 | 428.00 | 112.00 | 427.31 | 267.29 | NÃO | fora da faixa vertical |
| 981 | 427.00 | 111.00 | 427.14 | 268.29 | NÃO | fora da faixa vertical |
| 982 | 426.00 | 110.00 | 426.98 | 269.29 | NÃO | fora da faixa vertical |
| 983 | 425.00 | 109.00 | 426.82 | 270.29 | NÃO | fora da faixa vertical |
| 984 | 425.00 | 108.00 | 427.45 | 271.29 | NÃO | fora da faixa vertical |
| 985 | 424.00 | 107.00 | 427.30 | 272.29 | NÃO | fora da faixa vertical |
| 986 | 423.00 | 106.00 | 427.15 | 273.29 | NÃO | fora da faixa vertical |
| 987 | 422.00 | 105.00 | 427.01 | 274.29 | NÃO | fora da faixa vertical |
| 988 | 421.00 | 104.00 | 426.88 | 275.29 | NÃO | fora da faixa vertical |
| 989 | 420.00 | 103.00 | 426.75 | 276.29 | NÃO | fora da faixa vertical |
| 990 | 419.00 | 103.00 | 425.98 | 276.29 | NÃO | fora da faixa vertical |
| 991 | 418.00 | 102.00 | 425.85 | 277.29 | NÃO | fora da faixa vertical |
| 992 | 417.00 | 101.00 | 425.73 | 278.29 | NÃO | fora da faixa vertical |
| 993 | 416.00 | 100.00 | 425.62 | 279.29 | NÃO | fora da faixa vertical |
| 994 | 415.00 | 99.00 | 425.51 | 280.29 | NÃO | fora da faixa vertical |
| 995 | 414.00 | 98.00 | 425.40 | 281.29 | NÃO | fora da faixa vertical |
| 996 | 413.00 | 97.00 | 425.30 | 282.29 | NÃO | fora da faixa vertical |
| 997 | 412.00 | 96.00 | 425.21 | 283.29 | NÃO | fora da faixa vertical |
| 998 | 411.00 | 95.00 | 425.11 | 284.29 | NÃO | fora da faixa vertical |
| 999 | 410.00 | 94.00 | 425.03 | 285.29 | NÃO | fora da faixa vertical |
| 1000 | 409.00 | 94.00 | 424.28 | 285.29 | NÃO | fora da faixa vertical |
| 1001 | 408.00 | 93.00 | 424.20 | 286.29 | NÃO | fora da faixa vertical |
| 1002 | 407.00 | 92.00 | 424.12 | 287.29 | NÃO | fora da faixa vertical |
| 1003 | 406.00 | 91.00 | 424.05 | 288.29 | NÃO | fora da faixa vertical |
| 1004 | 405.00 | 90.00 | 423.99 | 289.29 | NÃO | fora da faixa vertical |
| 1005 | 404.00 | 90.00 | 423.25 | 289.29 | NÃO | fora da faixa vertical |
| 1006 | 403.00 | 89.00 | 423.19 | 290.29 | NÃO | fora da faixa vertical |
| 1007 | 402.00 | 88.00 | 423.14 | 291.29 | NÃO | fora da faixa vertical |
| 1008 | 401.00 | 87.00 | 423.09 | 292.29 | NÃO | fora da faixa vertical |
| 1009 | 400.00 | 87.00 | 422.36 | 292.29 | NÃO | fora da faixa vertical |
| 1010 | 399.00 | 86.00 | 422.31 | 293.29 | NÃO | fora da faixa vertical |
| 1011 | 398.00 | 85.00 | 422.28 | 294.29 | NÃO | fora da faixa vertical |
| 1012 | 397.00 | 84.00 | 422.24 | 295.29 | NÃO | fora da faixa vertical |
| 1013 | 396.00 | 84.00 | 421.52 | 295.29 | NÃO | fora da faixa vertical |
| 1014 | 395.00 | 83.00 | 421.49 | 296.29 | NÃO | fora da faixa vertical |
| 1015 | 394.00 | 82.00 | 421.47 | 297.29 | NÃO | fora da faixa vertical |
| 1016 | 393.00 | 82.00 | 420.76 | 297.29 | NÃO | fora da faixa vertical |
| 1017 | 392.00 | 81.00 | 420.74 | 298.29 | NÃO | fora da faixa vertical |
| 1018 | 391.00 | 80.00 | 420.73 | 299.29 | NÃO | fora da faixa vertical |
| 1019 | 390.00 | 80.00 | 420.02 | 299.29 | NÃO | fora da faixa vertical |
| 1020 | 389.00 | 79.00 | 420.02 | 300.29 | NÃO | fora da faixa vertical |
| 1021 | 388.00 | 78.00 | 420.02 | 301.29 | NÃO | fora da faixa vertical |
| 1022 | 387.00 | 78.00 | 419.32 | 301.29 | NÃO | fora da faixa vertical |
| 1023 | 386.00 | 77.00 | 419.33 | 302.29 | NÃO | fora da faixa vertical |
| 1024 | 385.00 | 77.00 | 418.63 | 302.29 | NÃO | fora da faixa vertical |
| 1025 | 384.00 | 76.00 | 418.65 | 303.29 | NÃO | fora da faixa vertical |
| 1026 | 383.00 | 75.00 | 418.67 | 304.29 | NÃO | fora da faixa vertical |
| 1027 | 382.00 | 75.00 | 417.97 | 304.29 | NÃO | fora da faixa vertical |
| 1028 | 381.00 | 74.00 | 418.00 | 305.29 | NÃO | fora da faixa vertical |
| 1029 | 380.00 | 73.00 | 418.03 | 306.29 | NÃO | fora da faixa vertical |
| 1030 | 379.00 | 73.00 | 417.35 | 306.29 | NÃO | fora da faixa vertical |
| 1031 | 378.00 | 72.00 | 417.39 | 307.29 | NÃO | fora da faixa vertical |
| 1032 | 377.00 | 72.00 | 416.70 | 307.29 | NÃO | fora da faixa vertical |
| 1033 | 376.00 | 71.00 | 416.75 | 308.29 | NÃO | fora da faixa vertical |
| 1034 | 375.00 | 71.00 | 416.07 | 308.29 | NÃO | fora da faixa vertical |
| 1035 | 374.00 | 70.00 | 416.12 | 309.29 | NÃO | fora da faixa vertical |
| 1036 | 373.00 | 70.00 | 415.45 | 309.29 | NÃO | fora da faixa vertical |
| 1037 | 372.00 | 69.00 | 415.51 | 310.29 | NÃO | fora da faixa vertical |
| 1038 | 371.00 | 69.00 | 414.84 | 310.29 | NÃO | fora da faixa vertical |
| 1039 | 370.00 | 68.00 | 414.91 | 311.29 | NÃO | fora da faixa vertical |
| 1040 | 369.00 | 68.00 | 414.24 | 311.29 | NÃO | fora da faixa vertical |
| 1041 | 368.00 | 67.00 | 414.32 | 312.29 | NÃO | fora da faixa vertical |
| 1042 | 367.00 | 67.00 | 413.65 | 312.29 | NÃO | fora da faixa vertical |
| 1043 | 366.00 | 66.00 | 413.73 | 313.29 | NÃO | fora da faixa vertical |
| 1044 | 365.00 | 66.00 | 413.07 | 313.29 | NÃO | fora da faixa vertical |
| 1045 | 364.00 | 65.00 | 413.16 | 314.29 | NÃO | fora da faixa vertical |
| 1046 | 363.00 | 65.00 | 412.51 | 314.29 | NÃO | fora da faixa vertical |
| 1047 | 362.00 | 64.00 | 412.61 | 315.29 | NÃO | fora da faixa vertical |
| 1048 | 361.00 | 64.00 | 411.95 | 315.29 | NÃO | fora da faixa vertical |
| 1049 | 360.00 | 63.00 | 412.06 | 316.29 | NÃO | fora da faixa vertical |
| 1050 | 359.00 | 63.00 | 411.41 | 316.29 | NÃO | fora da faixa vertical |
| 1051 | 358.00 | 62.00 | 411.52 | 317.29 | NÃO | fora da faixa vertical |
| 1052 | 357.00 | 62.00 | 410.88 | 317.29 | NÃO | fora da faixa vertical |
| 1053 | 356.00 | 62.00 | 410.23 | 317.29 | NÃO | fora da faixa vertical |
| 1054 | 355.00 | 61.00 | 410.36 | 318.29 | NÃO | fora da faixa vertical |
| 1055 | 354.00 | 61.00 | 409.72 | 318.29 | NÃO | fora da faixa vertical |
| 1056 | 353.00 | 61.00 | 409.08 | 318.29 | NÃO | fora da faixa vertical |
| 1057 | 352.00 | 60.00 | 409.21 | 319.29 | NÃO | fora da faixa vertical |
| 1058 | 351.00 | 60.00 | 408.58 | 319.29 | NÃO | fora da faixa vertical |
| 1059 | 350.00 | 59.00 | 408.72 | 320.29 | NÃO | fora da faixa vertical |
| 1060 | 349.00 | 59.00 | 408.09 | 320.29 | NÃO | fora da faixa vertical |
| 1061 | 348.00 | 59.00 | 407.46 | 320.29 | NÃO | fora da faixa vertical |
| 1062 | 347.00 | 58.00 | 407.61 | 321.29 | NÃO | fora da faixa vertical |
| 1063 | 346.00 | 58.00 | 406.99 | 321.29 | NÃO | fora da faixa vertical |
| 1064 | 345.00 | 58.00 | 406.37 | 321.29 | NÃO | fora da faixa vertical |
| 1065 | 344.00 | 57.00 | 406.53 | 322.29 | NÃO | fora da faixa vertical |
| 1066 | 343.00 | 57.00 | 405.91 | 322.29 | NÃO | fora da faixa vertical |
| 1067 | 342.00 | 57.00 | 405.29 | 322.29 | NÃO | fora da faixa vertical |
| 1068 | 341.00 | 56.00 | 405.46 | 323.29 | NÃO | fora da faixa vertical |
| 1069 | 340.00 | 56.00 | 404.85 | 323.29 | NÃO | fora da faixa vertical |
| 1070 | 339.00 | 56.00 | 404.24 | 323.29 | NÃO | fora da faixa vertical |
| 1071 | 338.00 | 56.00 | 403.63 | 323.29 | NÃO | fora da faixa vertical |
| 1072 | 337.00 | 55.00 | 403.81 | 324.29 | NÃO | fora da faixa vertical |
| 1073 | 336.00 | 55.00 | 403.21 | 324.29 | NÃO | fora da faixa vertical |
| 1074 | 335.00 | 55.00 | 402.60 | 324.29 | NÃO | fora da faixa vertical |
| 1075 | 334.00 | 54.00 | 402.80 | 325.29 | NÃO | fora da faixa vertical |
| 1076 | 333.00 | 54.00 | 402.20 | 325.29 | NÃO | fora da faixa vertical |
| 1077 | 332.00 | 54.00 | 401.60 | 325.29 | NÃO | fora da faixa vertical |
| 1078 | 331.00 | 54.00 | 401.00 | 325.29 | NÃO | fora da faixa vertical |
| 1079 | 330.00 | 53.00 | 401.21 | 326.29 | NÃO | fora da faixa vertical |
| 1080 | 329.00 | 53.00 | 400.62 | 326.29 | NÃO | fora da faixa vertical |
| 1081 | 328.00 | 53.00 | 400.03 | 326.29 | NÃO | fora da faixa vertical |
| 1082 | 327.00 | 53.00 | 399.44 | 326.29 | NÃO | fora da faixa vertical |
| 1083 | 326.00 | 52.00 | 399.66 | 327.29 | NÃO | fora da faixa vertical |
| 1084 | 325.00 | 52.00 | 399.08 | 327.29 | NÃO | fora da faixa vertical |
| 1085 | 324.00 | 52.00 | 398.50 | 327.29 | NÃO | fora da faixa vertical |
| 1086 | 323.00 | 52.00 | 397.92 | 327.29 | NÃO | fora da faixa vertical |
| 1087 | 322.00 | 52.00 | 397.34 | 327.29 | NÃO | fora da faixa vertical |
| 1088 | 321.00 | 51.00 | 397.58 | 328.29 | NÃO | fora da faixa vertical |
| 1089 | 320.00 | 51.00 | 397.00 | 328.29 | NÃO | fora da faixa vertical |
| 1090 | 319.00 | 51.00 | 396.43 | 328.29 | NÃO | fora da faixa vertical |
| 1091 | 318.00 | 51.00 | 395.85 | 328.29 | NÃO | fora da faixa vertical |
| 1092 | 317.00 | 51.00 | 395.28 | 328.29 | NÃO | fora da faixa vertical |
| 1093 | 316.00 | 50.00 | 395.54 | 329.29 | NÃO | fora da faixa vertical |
| 1094 | 315.00 | 50.00 | 394.97 | 329.29 | NÃO | fora da faixa vertical |
| 1095 | 314.00 | 50.00 | 394.41 | 329.29 | NÃO | fora da faixa vertical |
| 1096 | 313.00 | 50.00 | 393.85 | 329.29 | NÃO | fora da faixa vertical |
| 1097 | 312.00 | 50.00 | 393.29 | 329.29 | NÃO | fora da faixa vertical |
| 1098 | 311.00 | 49.00 | 393.56 | 330.29 | NÃO | fora da faixa vertical |
| 1099 | 310.00 | 49.00 | 393.01 | 330.29 | NÃO | fora da faixa vertical |
| 1100 | 309.00 | 49.00 | 392.45 | 330.29 | NÃO | fora da faixa vertical |
| 1101 | 308.00 | 49.00 | 391.90 | 330.29 | NÃO | fora da faixa vertical |
| 1102 | 307.00 | 49.00 | 391.35 | 330.29 | NÃO | fora da faixa vertical |
| 1103 | 306.00 | 49.00 | 390.80 | 330.29 | NÃO | fora da faixa vertical |
| 1104 | 305.00 | 49.00 | 390.25 | 330.29 | NÃO | fora da faixa vertical |
| 1105 | 304.00 | 48.00 | 390.55 | 331.29 | NÃO | fora da faixa vertical |
| 1106 | 303.00 | 48.00 | 390.01 | 331.29 | NÃO | fora da faixa vertical |
| 1107 | 302.00 | 48.00 | 389.47 | 331.29 | NÃO | fora da faixa vertical |
| 1108 | 301.00 | 48.00 | 388.93 | 331.29 | NÃO | fora da faixa vertical |
| 1109 | 300.00 | 48.00 | 388.39 | 331.29 | NÃO | fora da faixa vertical |
| 1110 | 299.00 | 48.00 | 387.86 | 331.29 | NÃO | fora da faixa vertical |
| 1111 | 298.00 | 48.00 | 387.32 | 331.29 | NÃO | fora da faixa vertical |
| 1112 | 297.00 | 48.00 | 386.79 | 331.29 | NÃO | fora da faixa vertical |
| 1113 | 296.00 | 48.00 | 386.26 | 331.29 | NÃO | fora da faixa vertical |
| 1114 | 295.00 | 47.00 | 386.59 | 332.29 | NÃO | fora da faixa vertical |
| 1115 | 294.00 | 47.00 | 386.06 | 332.29 | NÃO | fora da faixa vertical |
| 1116 | 293.00 | 47.00 | 385.54 | 332.29 | NÃO | fora da faixa vertical |
| 1117 | 292.00 | 47.00 | 385.02 | 332.29 | NÃO | fora da faixa vertical |
| 1118 | 291.00 | 47.00 | 384.50 | 332.29 | NÃO | fora da faixa vertical |
| 1119 | 290.00 | 47.00 | 383.99 | 332.29 | NÃO | fora da faixa vertical |
| 1120 | 289.00 | 47.00 | 383.47 | 332.29 | NÃO | fora da faixa vertical |
| 1121 | 288.00 | 47.00 | 382.96 | 332.29 | NÃO | fora da faixa vertical |
| 1122 | 287.00 | 47.00 | 382.45 | 332.29 | NÃO | fora da faixa vertical |
| 1123 | 286.00 | 47.00 | 381.94 | 332.29 | NÃO | fora da faixa vertical |
| 1124 | 285.00 | 47.00 | 381.43 | 332.29 | NÃO | fora da faixa vertical |
| 1125 | 284.00 | 47.00 | 380.93 | 332.29 | NÃO | fora da faixa vertical |
| 1126 | 283.00 | 47.00 | 380.42 | 332.29 | NÃO | fora da faixa vertical |
| 1127 | 282.00 | 47.00 | 379.92 | 332.29 | NÃO | fora da faixa vertical |
| 1128 | 281.00 | 47.00 | 379.42 | 332.29 | NÃO | fora da faixa vertical |
| 1129 | 280.00 | 47.00 | 378.93 | 332.29 | NÃO | fora da faixa vertical |
| 1130 | 279.00 | 47.00 | 378.43 | 332.29 | NÃO | fora da faixa vertical |
| 1131 | 278.00 | 47.00 | 377.94 | 332.29 | NÃO | fora da faixa vertical |
| 1132 | 277.00 | 47.00 | 377.45 | 332.29 | NÃO | fora da faixa vertical |
| 1133 | 276.00 | 47.00 | 376.96 | 332.29 | NÃO | fora da faixa vertical |
| 1134 | 275.00 | 47.00 | 376.47 | 332.29 | NÃO | fora da faixa vertical |
| 1135 | 274.00 | 47.00 | 375.99 | 332.29 | NÃO | fora da faixa vertical |
| 1136 | 273.00 | 47.00 | 375.50 | 332.29 | NÃO | fora da faixa vertical |
| 1137 | 272.00 | 47.00 | 375.02 | 332.29 | NÃO | fora da faixa vertical |
| 1138 | 271.00 | 47.00 | 374.54 | 332.29 | NÃO | fora da faixa vertical |
| 1139 | 270.00 | 47.00 | 374.07 | 332.29 | NÃO | fora da faixa vertical |
| 1140 | 269.00 | 47.00 | 373.59 | 332.29 | NÃO | fora da faixa vertical |
| 1141 | 268.00 | 47.00 | 373.12 | 332.29 | NÃO | fora da faixa vertical |
| 1142 | 267.00 | 47.00 | 372.65 | 332.29 | NÃO | fora da faixa vertical |
| 1143 | 266.00 | 47.00 | 372.18 | 332.29 | NÃO | fora da faixa vertical |
| 1144 | 265.00 | 47.00 | 371.71 | 332.29 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 221 | 83.00 | 200.00 | -9.00 | -179.29 |
| 222 | 83.00 | 201.00 | -9.00 | -178.29 |
| 223 | 83.00 | 202.00 | -9.00 | -177.29 |
| 224 | 82.00 | 203.00 | -10.00 | -176.29 |
| 225 | 82.00 | 204.00 | -10.00 | -175.29 |
| 226 | 82.00 | 205.00 | -10.00 | -174.29 |
| 227 | 82.00 | 206.00 | -10.00 | -173.29 |
| 228 | 82.00 | 207.00 | -10.00 | -172.29 |
| 229 | 81.00 | 208.00 | -11.00 | -171.29 |
| 230 | 81.00 | 209.00 | -11.00 | -170.29 |
| 231 | 81.00 | 210.00 | -11.00 | -169.29 |
| 232 | 81.00 | 211.00 | -11.00 | -168.29 |
| 233 | 81.00 | 212.00 | -11.00 | -167.29 |
| 234 | 80.00 | 213.00 | -12.00 | -166.29 |
| 235 | 80.00 | 214.00 | -12.00 | -165.29 |
| 236 | 80.00 | 215.00 | -12.00 | -164.29 |
| 237 | 80.00 | 216.00 | -12.00 | -163.29 |
| 238 | 80.00 | 217.00 | -12.00 | -162.29 |
| 239 | 79.00 | 218.00 | -13.00 | -161.29 |
| 240 | 79.00 | 219.00 | -13.00 | -160.29 |
| 241 | 79.00 | 220.00 | -13.00 | -159.29 |
| 242 | 79.00 | 221.00 | -13.00 | -158.29 |
| 243 | 79.00 | 222.00 | -13.00 | -157.29 |
| 244 | 79.00 | 223.00 | -13.00 | -156.29 |
| 245 | 79.00 | 224.00 | -13.00 | -155.29 |
| 246 | 79.00 | 225.00 | -13.00 | -154.29 |
| 247 | 78.00 | 226.00 | -14.00 | -153.29 |
| 248 | 78.00 | 227.00 | -14.00 | -152.29 |
| 249 | 78.00 | 228.00 | -14.00 | -151.29 |
| 250 | 78.00 | 229.00 | -14.00 | -150.29 |
| 251 | 78.00 | 230.00 | -14.00 | -149.29 |
| 252 | 78.00 | 231.00 | -14.00 | -148.29 |
| 253 | 78.00 | 232.00 | -14.00 | -147.29 |
| 254 | 78.00 | 233.00 | -14.00 | -146.29 |
| 255 | 77.00 | 234.00 | -15.00 | -145.29 |
| 256 | 77.00 | 235.00 | -15.00 | -144.29 |
| 257 | 77.00 | 236.00 | -15.00 | -143.29 |
| 258 | 77.00 | 237.00 | -15.00 | -142.29 |
| 259 | 77.00 | 238.00 | -15.00 | -141.29 |
| 260 | 77.00 | 239.00 | -15.00 | -140.29 |
| 261 | 77.00 | 240.00 | -15.00 | -139.29 |
| 262 | 77.00 | 241.00 | -15.00 | -138.29 |
| 263 | 77.00 | 242.00 | -15.00 | -137.29 |
| 264 | 77.00 | 243.00 | -15.00 | -136.29 |
| 265 | 77.00 | 244.00 | -15.00 | -135.29 |
| 266 | 77.00 | 245.00 | -15.00 | -134.29 |
| 267 | 77.00 | 246.00 | -15.00 | -133.29 |
| 268 | 77.00 | 247.00 | -15.00 | -132.29 |
| 269 | 77.00 | 248.00 | -15.00 | -131.29 |
| 270 | 77.00 | 249.00 | -15.00 | -130.29 |
| 271 | 77.00 | 250.00 | -15.00 | -129.29 |
| 272 | 77.00 | 251.00 | -15.00 | -128.29 |
| 273 | 77.00 | 252.00 | -15.00 | -127.29 |
| 274 | 77.00 | 253.00 | -15.00 | -126.29 |
| 275 | 77.00 | 254.00 | -15.00 | -125.29 |
| 276 | 77.00 | 255.00 | -15.00 | -124.29 |
| 277 | 77.00 | 256.00 | -15.00 | -123.29 |
| 278 | 77.00 | 257.00 | -15.00 | -122.29 |
| 279 | 77.00 | 258.00 | -15.00 | -121.29 |
| 280 | 77.00 | 259.00 | -15.00 | -120.29 |
| 281 | 77.00 | 260.00 | -15.00 | -119.29 |
| 282 | 77.00 | 261.00 | -15.00 | -118.29 |
| 283 | 77.00 | 262.00 | -15.00 | -117.29 |
| 284 | 77.00 | 263.00 | -15.00 | -116.29 |
| 285 | 77.00 | 264.00 | -15.00 | -115.29 |
| 286 | 77.00 | 265.00 | -15.00 | -114.29 |
| 287 | 78.00 | 266.00 | -14.00 | -113.29 |
| 288 | 78.00 | 267.00 | -14.00 | -112.29 |
| 289 | 78.00 | 268.00 | -14.00 | -111.29 |
| 290 | 78.00 | 269.00 | -14.00 | -110.29 |
| 291 | 78.00 | 270.00 | -14.00 | -109.29 |
| 292 | 78.00 | 271.00 | -14.00 | -108.29 |
| 293 | 78.00 | 272.00 | -14.00 | -107.29 |
| 294 | 78.00 | 273.00 | -14.00 | -106.29 |
| 295 | 78.00 | 274.00 | -14.00 | -105.29 |
| 296 | 79.00 | 275.00 | -13.00 | -104.29 |
| 297 | 79.00 | 276.00 | -13.00 | -103.29 |
| 298 | 79.00 | 277.00 | -13.00 | -102.29 |
| 299 | 79.00 | 278.00 | -13.00 | -101.29 |
| 300 | 79.00 | 279.00 | -13.00 | -100.29 |
| 301 | 79.00 | 280.00 | -13.00 | -99.29 |
| 302 | 79.00 | 281.00 | -13.00 | -98.29 |
| 303 | 79.00 | 282.00 | -13.00 | -97.29 |
| 304 | 80.00 | 283.00 | -12.00 | -96.29 |
| 305 | 80.00 | 284.00 | -12.00 | -95.29 |
| 306 | 80.00 | 285.00 | -12.00 | -94.29 |
| 307 | 80.00 | 286.00 | -12.00 | -93.29 |
| 308 | 80.00 | 287.00 | -12.00 | -92.29 |
| 309 | 81.00 | 288.00 | -11.00 | -91.29 |
| 310 | 81.00 | 289.00 | -11.00 | -90.29 |
| 311 | 81.00 | 290.00 | -11.00 | -89.29 |
| 312 | 81.00 | 291.00 | -11.00 | -88.29 |
| 313 | 82.00 | 292.00 | -10.00 | -87.29 |
| 314 | 82.00 | 293.00 | -10.00 | -86.29 |
| 315 | 82.00 | 294.00 | -10.00 | -85.29 |
| 316 | 82.00 | 295.00 | -10.00 | -84.29 |
| 317 | 82.00 | 296.00 | -10.00 | -83.29 |
| 318 | 83.00 | 297.00 | -9.00 | -82.29 |
| 319 | 83.00 | 298.00 | -9.00 | -81.29 |
| 320 | 83.00 | 299.00 | -9.00 | -80.29 |
| 321 | 83.00 | 300.00 | -9.00 | -79.29 |
| 322 | 84.00 | 301.00 | -8.00 | -78.29 |
| 323 | 84.00 | 302.00 | -8.00 | -77.29 |
| 324 | 84.00 | 303.00 | -8.00 | -76.29 |
| 325 | 84.00 | 304.00 | -8.00 | -75.29 |
| 326 | 85.00 | 305.00 | -7.00 | -74.29 |
| 327 | 85.00 | 306.00 | -7.00 | -73.29 |
| 328 | 85.00 | 307.00 | -7.00 | -72.29 |
| 329 | 86.00 | 308.00 | -6.00 | -71.29 |
| 330 | 86.00 | 309.00 | -6.00 | -70.29 |
| 331 | 86.00 | 310.00 | -6.00 | -69.29 |
| 332 | 86.00 | 311.00 | -6.00 | -68.29 |
| 333 | 87.00 | 312.00 | -5.00 | -67.29 |
| 334 | 87.00 | 313.00 | -5.00 | -66.29 |
| 335 | 87.00 | 314.00 | -5.00 | -65.29 |
| 336 | 88.00 | 315.00 | -4.00 | -64.29 |
| 337 | 88.00 | 316.00 | -4.00 | -63.29 |
| 338 | 88.00 | 317.00 | -4.00 | -62.29 |
| 339 | 89.00 | 318.00 | -3.00 | -61.29 |
| 340 | 89.00 | 319.00 | -3.00 | -60.29 |
| 341 | 89.00 | 320.00 | -3.00 | -59.29 |
| 342 | 90.00 | 321.00 | -2.00 | -58.29 |
| 343 | 90.00 | 322.00 | -2.00 | -57.29 |
| 344 | 91.00 | 323.00 | -1.00 | -56.29 |
| 345 | 91.00 | 324.00 | -1.00 | -55.29 |
| 346 | 91.00 | 325.00 | -1.00 | -54.29 |
| 347 | 92.00 | 326.00 | 0.00 | -53.29 |
| 348 | 92.00 | 327.00 | 0.00 | -52.29 |
| 349 | 92.00 | 328.00 | 0.00 | -51.29 |
| 350 | 93.00 | 329.00 | 1.00 | -50.29 |
| 351 | 93.00 | 330.00 | 1.00 | -49.29 |
| 352 | 94.00 | 331.00 | 2.00 | -48.29 |
| 353 | 94.00 | 332.00 | 2.00 | -47.29 |
| 354 | 95.00 | 333.00 | 3.00 | -46.29 |
| 355 | 95.00 | 334.00 | 3.00 | -45.29 |
| 356 | 96.00 | 335.00 | 4.00 | -44.29 |
| 357 | 96.00 | 336.00 | 4.00 | -43.29 |
| 358 | 97.00 | 337.00 | 5.00 | -42.29 |
| 359 | 97.00 | 338.00 | 5.00 | -41.29 |
| 360 | 98.00 | 339.00 | 6.00 | -40.29 |
| 361 | 98.00 | 340.00 | 6.00 | -39.29 |
| 362 | 99.00 | 341.00 | 7.00 | -38.29 |
| 363 | 99.00 | 342.00 | 7.00 | -37.29 |
| 364 | 100.00 | 343.00 | 8.00 | -36.29 |
| 365 | 100.00 | 344.00 | 8.00 | -35.29 |
| 366 | 101.00 | 345.00 | 9.00 | -34.29 |
| 367 | 101.00 | 346.00 | 9.00 | -33.29 |
| 368 | 102.00 | 347.00 | 10.00 | -32.29 |
| 369 | 102.00 | 348.00 | 10.00 | -31.29 |
| 370 | 103.00 | 349.00 | 11.00 | -30.29 |
| 371 | 103.00 | 350.00 | 11.00 | -29.29 |
| 372 | 104.00 | 351.00 | 12.00 | -28.29 |
| 373 | 105.00 | 352.00 | 13.00 | -27.29 |
| 374 | 105.00 | 353.00 | 13.00 | -26.29 |
| 375 | 106.00 | 354.00 | 14.00 | -25.29 |
| 376 | 107.00 | 355.00 | 15.00 | -24.29 |
| 377 | 107.00 | 356.00 | 15.00 | -23.29 |
| 378 | 108.00 | 357.00 | 16.00 | -22.29 |
| 379 | 108.00 | 358.00 | 16.00 | -21.29 |
| 380 | 109.00 | 359.00 | 17.00 | -20.29 |
| 381 | 110.00 | 360.00 | 18.00 | -19.29 |
| 382 | 110.00 | 361.00 | 18.00 | -18.29 |
| 383 | 111.00 | 362.00 | 19.00 | -17.29 |
| 384 | 112.00 | 363.00 | 20.00 | -16.29 |
| 385 | 112.00 | 364.00 | 20.00 | -15.29 |
| 386 | 113.00 | 365.00 | 21.00 | -14.29 |
| 387 | 114.00 | 366.00 | 22.00 | -13.29 |
| 388 | 114.00 | 367.00 | 22.00 | -12.29 |
| 389 | 115.00 | 368.00 | 23.00 | -11.29 |
| 390 | 116.00 | 369.00 | 24.00 | -10.29 |
| 391 | 117.00 | 370.00 | 25.00 | -9.29 |
| 392 | 117.00 | 371.00 | 25.00 | -8.29 |
| 393 | 118.00 | 372.00 | 26.00 | -7.29 |
| 394 | 119.00 | 373.00 | 27.00 | -6.29 |
| 395 | 120.00 | 374.00 | 28.00 | -5.29 |
| 396 | 120.00 | 375.00 | 28.00 | -4.29 |
| 397 | 120.00 | 376.00 | 28.00 | -3.29 |
| 398 | 121.00 | 376.00 | 29.00 | -3.29 |
| 399 | 122.00 | 376.00 | 30.00 | -3.29 |
| 400 | 123.00 | 376.00 | 31.00 | -3.29 |
| 401 | 124.00 | 376.00 | 32.00 | -3.29 |
| 402 | 125.00 | 376.00 | 33.00 | -3.29 |
| 403 | 126.00 | 376.00 | 34.00 | -3.29 |
| 404 | 127.00 | 376.00 | 35.00 | -3.29 |
| 405 | 128.00 | 376.00 | 36.00 | -3.29 |
| 406 | 129.00 | 376.00 | 37.00 | -3.29 |
| 407 | 130.00 | 376.00 | 38.00 | -3.29 |
| 408 | 131.00 | 376.00 | 39.00 | -3.29 |
| 409 | 132.00 | 376.00 | 40.00 | -3.29 |
| 410 | 133.00 | 376.00 | 41.00 | -3.29 |
| 411 | 134.00 | 376.00 | 42.00 | -3.29 |
| 412 | 135.00 | 376.00 | 43.00 | -3.29 |
| 413 | 136.00 | 376.00 | 44.00 | -3.29 |
| 414 | 137.00 | 376.00 | 45.00 | -3.29 |
| 415 | 138.00 | 376.00 | 46.00 | -3.29 |
| 416 | 139.00 | 376.00 | 47.00 | -3.29 |
| 417 | 140.00 | 376.00 | 48.00 | -3.29 |
| 418 | 141.00 | 376.00 | 49.00 | -3.29 |
| 419 | 142.00 | 376.00 | 50.00 | -3.29 |
| 420 | 143.00 | 376.00 | 51.00 | -3.29 |
| 421 | 144.00 | 376.00 | 52.00 | -3.29 |
| 422 | 145.00 | 376.00 | 53.00 | -3.29 |
| 423 | 146.00 | 376.00 | 54.00 | -3.29 |
| 424 | 147.00 | 376.00 | 55.00 | -3.29 |
| 425 | 148.00 | 376.00 | 56.00 | -3.29 |
| 426 | 149.00 | 376.00 | 57.00 | -3.29 |
| 427 | 150.00 | 376.00 | 58.00 | -3.29 |
| 428 | 151.00 | 376.00 | 59.00 | -3.29 |
| 429 | 152.00 | 376.00 | 60.00 | -3.29 |
| 430 | 153.00 | 376.00 | 61.00 | -3.29 |
| 431 | 154.00 | 376.00 | 62.00 | -3.29 |
| 432 | 155.00 | 376.00 | 63.00 | -3.29 |
| 433 | 156.00 | 376.00 | 64.00 | -3.29 |
| 434 | 157.00 | 376.00 | 65.00 | -3.29 |
| 435 | 158.00 | 376.00 | 66.00 | -3.29 |
| 436 | 159.00 | 376.00 | 67.00 | -3.29 |
| 437 | 160.00 | 376.00 | 68.00 | -3.29 |
| 438 | 161.00 | 376.00 | 69.00 | -3.29 |
| 439 | 162.00 | 376.00 | 70.00 | -3.29 |
| 440 | 163.00 | 376.00 | 71.00 | -3.29 |
| 441 | 164.00 | 376.00 | 72.00 | -3.29 |
| 442 | 165.00 | 376.00 | 73.00 | -3.29 |
| 443 | 166.00 | 376.00 | 74.00 | -3.29 |
| 444 | 167.00 | 376.00 | 75.00 | -3.29 |
| 445 | 168.00 | 376.00 | 76.00 | -3.29 |
| 446 | 169.00 | 376.00 | 77.00 | -3.29 |
| 447 | 170.00 | 376.00 | 78.00 | -3.29 |
| 448 | 171.00 | 376.00 | 79.00 | -3.29 |
| 449 | 172.00 | 376.00 | 80.00 | -3.29 |
| 450 | 173.00 | 376.00 | 81.00 | -3.29 |
| 451 | 174.00 | 376.00 | 82.00 | -3.29 |
| 452 | 175.00 | 376.00 | 83.00 | -3.29 |
| 453 | 176.00 | 376.00 | 84.00 | -3.29 |
| 454 | 177.00 | 376.00 | 85.00 | -3.29 |
| 455 | 178.00 | 376.00 | 86.00 | -3.29 |
| 456 | 179.00 | 376.00 | 87.00 | -3.29 |
| 457 | 180.00 | 376.00 | 88.00 | -3.29 |
| 458 | 181.00 | 376.00 | 89.00 | -3.29 |
| 459 | 182.00 | 376.00 | 90.00 | -3.29 |
| 460 | 183.00 | 376.00 | 91.00 | -3.29 |
| 461 | 184.00 | 376.00 | 92.00 | -3.29 |
| 462 | 185.00 | 376.00 | 93.00 | -3.29 |
| 463 | 186.00 | 376.00 | 94.00 | -3.29 |
| 464 | 187.00 | 376.00 | 95.00 | -3.29 |
| 465 | 188.00 | 376.00 | 96.00 | -3.29 |
| 466 | 189.00 | 376.00 | 97.00 | -3.29 |
| 467 | 190.00 | 376.00 | 98.00 | -3.29 |
| 468 | 191.00 | 376.00 | 99.00 | -3.29 |
| 469 | 192.00 | 376.00 | 100.00 | -3.29 |
| 470 | 193.00 | 376.00 | 101.00 | -3.29 |
| 471 | 194.00 | 376.00 | 102.00 | -3.29 |
| 472 | 195.00 | 376.00 | 103.00 | -3.29 |
| 473 | 196.00 | 376.00 | 104.00 | -3.29 |
| 474 | 197.00 | 376.00 | 105.00 | -3.29 |
| 475 | 198.00 | 376.00 | 106.00 | -3.29 |
| 476 | 199.00 | 376.00 | 107.00 | -3.29 |
| 477 | 200.00 | 376.00 | 108.00 | -3.29 |
| 478 | 201.00 | 376.00 | 109.00 | -3.29 |
| 479 | 202.00 | 376.00 | 110.00 | -3.29 |
| 480 | 203.00 | 376.00 | 111.00 | -3.29 |
| 481 | 204.00 | 376.00 | 112.00 | -3.29 |
| 482 | 205.00 | 376.00 | 113.00 | -3.29 |
| 483 | 206.00 | 376.00 | 114.00 | -3.29 |
| 484 | 207.00 | 376.00 | 115.00 | -3.29 |
| 485 | 208.00 | 376.00 | 116.00 | -3.29 |
| 486 | 209.00 | 376.00 | 117.00 | -3.29 |
| 487 | 210.00 | 376.00 | 118.00 | -3.29 |
| 488 | 211.00 | 376.00 | 119.00 | -3.29 |
| 489 | 212.00 | 376.00 | 120.00 | -3.29 |
| 490 | 213.00 | 376.00 | 121.00 | -3.29 |
| 491 | 214.00 | 376.00 | 122.00 | -3.29 |
| 492 | 215.00 | 376.00 | 123.00 | -3.29 |
| 493 | 216.00 | 376.00 | 124.00 | -3.29 |
| 494 | 217.00 | 376.00 | 125.00 | -3.29 |
| 495 | 218.00 | 376.00 | 126.00 | -3.29 |
| 496 | 219.00 | 376.00 | 127.00 | -3.29 |
| 497 | 220.00 | 376.00 | 128.00 | -3.29 |
| 498 | 221.00 | 376.00 | 129.00 | -3.29 |
| 499 | 222.00 | 376.00 | 130.00 | -3.29 |
| 500 | 223.00 | 376.00 | 131.00 | -3.29 |
| 501 | 224.00 | 376.00 | 132.00 | -3.29 |
| 502 | 225.00 | 376.00 | 133.00 | -3.29 |
| 503 | 226.00 | 376.00 | 134.00 | -3.29 |
| 504 | 227.00 | 376.00 | 135.00 | -3.29 |
| 505 | 228.00 | 376.00 | 136.00 | -3.29 |
| 506 | 229.00 | 376.00 | 137.00 | -3.29 |
| 507 | 230.00 | 376.00 | 138.00 | -3.29 |
| 508 | 231.00 | 376.00 | 139.00 | -3.29 |
| 509 | 232.00 | 376.00 | 140.00 | -3.29 |
| 510 | 233.00 | 376.00 | 141.00 | -3.29 |
| 511 | 234.00 | 376.00 | 142.00 | -3.29 |
| 512 | 235.00 | 376.00 | 143.00 | -3.29 |
| 513 | 236.00 | 376.00 | 144.00 | -3.29 |
| 514 | 237.00 | 376.00 | 145.00 | -3.29 |
| 515 | 238.00 | 376.00 | 146.00 | -3.29 |
| 516 | 239.00 | 376.00 | 147.00 | -3.29 |
| 517 | 240.00 | 376.00 | 148.00 | -3.29 |
| 518 | 241.00 | 376.00 | 149.00 | -3.29 |
| 519 | 242.00 | 376.00 | 150.00 | -3.29 |
| 520 | 243.00 | 376.00 | 151.00 | -3.29 |
| 521 | 244.00 | 376.00 | 152.00 | -3.29 |
| 522 | 245.00 | 376.00 | 153.00 | -3.29 |
| 523 | 246.00 | 376.00 | 154.00 | -3.29 |
| 524 | 247.00 | 376.00 | 155.00 | -3.29 |
| 525 | 248.00 | 376.00 | 156.00 | -3.29 |
| 526 | 249.00 | 376.00 | 157.00 | -3.29 |
| 527 | 250.00 | 376.00 | 158.00 | -3.29 |
| 528 | 251.00 | 376.00 | 159.00 | -3.29 |
| 529 | 252.00 | 376.00 | 160.00 | -3.29 |
| 530 | 253.00 | 376.00 | 161.00 | -3.29 |
| 531 | 254.00 | 376.00 | 162.00 | -3.29 |
| 532 | 255.00 | 376.00 | 163.00 | -3.29 |
| 533 | 256.00 | 376.00 | 164.00 | -3.29 |
| 534 | 257.00 | 376.00 | 165.00 | -3.29 |
| 535 | 258.00 | 376.00 | 166.00 | -3.29 |
| 536 | 259.00 | 376.00 | 167.00 | -3.29 |
| 537 | 260.00 | 376.00 | 168.00 | -3.29 |
| 538 | 261.00 | 376.00 | 169.00 | -3.29 |
| 539 | 262.00 | 376.00 | 170.00 | -3.29 |
| 540 | 263.00 | 376.00 | 171.00 | -3.29 |
| 541 | 264.00 | 376.00 | 172.00 | -3.29 |
| 542 | 265.00 | 376.00 | 173.00 | -3.29 |
| 543 | 266.00 | 376.00 | 174.00 | -3.29 |
| 544 | 267.00 | 376.00 | 175.00 | -3.29 |
| 545 | 268.00 | 376.00 | 176.00 | -3.29 |
| 546 | 269.00 | 376.00 | 177.00 | -3.29 |
| 547 | 270.00 | 376.00 | 178.00 | -3.29 |
| 548 | 271.00 | 376.00 | 179.00 | -3.29 |
| 549 | 272.00 | 376.00 | 180.00 | -3.29 |
| 550 | 273.00 | 376.00 | 181.00 | -3.29 |
| 551 | 274.00 | 376.00 | 182.00 | -3.29 |
| 552 | 275.00 | 376.00 | 183.00 | -3.29 |
| 553 | 276.00 | 376.00 | 184.00 | -3.29 |
| 554 | 277.00 | 376.00 | 185.00 | -3.29 |
| 555 | 278.00 | 376.00 | 186.00 | -3.29 |
| 556 | 279.00 | 376.00 | 187.00 | -3.29 |

- primeiro índice: 221
- último índice: 556
- quantidade: 336
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![50_geo esq](audit_outputs/75_geo_esq_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![50_geo esq polyfit](audit_outputs/75_geo_esq_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

### Lado: dir

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 1145
- ponto de contato recebido: [467.0, 376.0]
- baseline_y: 376.0
- baseline_ajustada: 379.29
- lado solicitado: dir
- largura da região: 180 px
- altura da gota: 329.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 264.00 | 47.00 | 386.59 | 332.29 | NÃO | fora da faixa vertical |
| 1 | 263.00 | 48.00 | 386.26 | 331.29 | NÃO | fora da faixa vertical |
| 2 | 262.00 | 48.00 | 386.79 | 331.29 | NÃO | fora da faixa vertical |
| 3 | 261.00 | 48.00 | 387.32 | 331.29 | NÃO | fora da faixa vertical |
| 4 | 260.00 | 48.00 | 387.86 | 331.29 | NÃO | fora da faixa vertical |
| 5 | 259.00 | 48.00 | 388.39 | 331.29 | NÃO | fora da faixa vertical |
| 6 | 258.00 | 48.00 | 388.93 | 331.29 | NÃO | fora da faixa vertical |
| 7 | 257.00 | 48.00 | 389.47 | 331.29 | NÃO | fora da faixa vertical |
| 8 | 256.00 | 48.00 | 390.01 | 331.29 | NÃO | fora da faixa vertical |
| 9 | 255.00 | 49.00 | 389.71 | 330.29 | NÃO | fora da faixa vertical |
| 10 | 254.00 | 49.00 | 390.25 | 330.29 | NÃO | fora da faixa vertical |
| 11 | 253.00 | 49.00 | 390.80 | 330.29 | NÃO | fora da faixa vertical |
| 12 | 252.00 | 49.00 | 391.35 | 330.29 | NÃO | fora da faixa vertical |
| 13 | 251.00 | 49.00 | 391.90 | 330.29 | NÃO | fora da faixa vertical |
| 14 | 250.00 | 49.00 | 392.45 | 330.29 | NÃO | fora da faixa vertical |
| 15 | 249.00 | 49.00 | 393.01 | 330.29 | NÃO | fora da faixa vertical |
| 16 | 248.00 | 49.00 | 393.56 | 330.29 | NÃO | fora da faixa vertical |
| 17 | 247.00 | 50.00 | 393.29 | 329.29 | NÃO | fora da faixa vertical |
| 18 | 246.00 | 50.00 | 393.85 | 329.29 | NÃO | fora da faixa vertical |
| 19 | 245.00 | 50.00 | 394.41 | 329.29 | NÃO | fora da faixa vertical |
| 20 | 244.00 | 50.00 | 394.97 | 329.29 | NÃO | fora da faixa vertical |
| 21 | 243.00 | 50.00 | 395.54 | 329.29 | NÃO | fora da faixa vertical |
| 22 | 242.00 | 51.00 | 395.28 | 328.29 | NÃO | fora da faixa vertical |
| 23 | 241.00 | 51.00 | 395.85 | 328.29 | NÃO | fora da faixa vertical |
| 24 | 240.00 | 51.00 | 396.43 | 328.29 | NÃO | fora da faixa vertical |
| 25 | 239.00 | 51.00 | 397.00 | 328.29 | NÃO | fora da faixa vertical |
| 26 | 238.00 | 51.00 | 397.58 | 328.29 | NÃO | fora da faixa vertical |
| 27 | 237.00 | 52.00 | 397.34 | 327.29 | NÃO | fora da faixa vertical |
| 28 | 236.00 | 52.00 | 397.92 | 327.29 | NÃO | fora da faixa vertical |
| 29 | 235.00 | 52.00 | 398.50 | 327.29 | NÃO | fora da faixa vertical |
| 30 | 234.00 | 52.00 | 399.08 | 327.29 | NÃO | fora da faixa vertical |
| 31 | 233.00 | 52.00 | 399.66 | 327.29 | NÃO | fora da faixa vertical |
| 32 | 232.00 | 53.00 | 399.44 | 326.29 | NÃO | fora da faixa vertical |
| 33 | 231.00 | 53.00 | 400.03 | 326.29 | NÃO | fora da faixa vertical |
| 34 | 230.00 | 53.00 | 400.62 | 326.29 | NÃO | fora da faixa vertical |
| 35 | 229.00 | 53.00 | 401.21 | 326.29 | NÃO | fora da faixa vertical |
| 36 | 228.00 | 54.00 | 401.00 | 325.29 | NÃO | fora da faixa vertical |
| 37 | 227.00 | 54.00 | 401.60 | 325.29 | NÃO | fora da faixa vertical |
| 38 | 226.00 | 54.00 | 402.20 | 325.29 | NÃO | fora da faixa vertical |
| 39 | 225.00 | 54.00 | 402.80 | 325.29 | NÃO | fora da faixa vertical |
| 40 | 224.00 | 55.00 | 402.60 | 324.29 | NÃO | fora da faixa vertical |
| 41 | 223.00 | 55.00 | 403.21 | 324.29 | NÃO | fora da faixa vertical |
| 42 | 222.00 | 55.00 | 403.81 | 324.29 | NÃO | fora da faixa vertical |
| 43 | 221.00 | 56.00 | 403.63 | 323.29 | NÃO | fora da faixa vertical |
| 44 | 220.00 | 56.00 | 404.24 | 323.29 | NÃO | fora da faixa vertical |
| 45 | 219.00 | 56.00 | 404.85 | 323.29 | NÃO | fora da faixa vertical |
| 46 | 218.00 | 56.00 | 405.46 | 323.29 | NÃO | fora da faixa vertical |
| 47 | 217.00 | 57.00 | 405.29 | 322.29 | NÃO | fora da faixa vertical |
| 48 | 216.00 | 57.00 | 405.91 | 322.29 | NÃO | fora da faixa vertical |
| 49 | 215.00 | 57.00 | 406.53 | 322.29 | NÃO | fora da faixa vertical |
| 50 | 214.00 | 58.00 | 406.37 | 321.29 | NÃO | fora da faixa vertical |
| 51 | 213.00 | 58.00 | 406.99 | 321.29 | NÃO | fora da faixa vertical |
| 52 | 212.00 | 58.00 | 407.61 | 321.29 | NÃO | fora da faixa vertical |
| 53 | 211.00 | 59.00 | 407.46 | 320.29 | NÃO | fora da faixa vertical |
| 54 | 210.00 | 59.00 | 408.09 | 320.29 | NÃO | fora da faixa vertical |
| 55 | 209.00 | 60.00 | 407.95 | 319.29 | NÃO | fora da faixa vertical |
| 56 | 208.00 | 60.00 | 408.58 | 319.29 | NÃO | fora da faixa vertical |
| 57 | 207.00 | 60.00 | 409.21 | 319.29 | NÃO | fora da faixa vertical |
| 58 | 206.00 | 61.00 | 409.08 | 318.29 | NÃO | fora da faixa vertical |
| 59 | 205.00 | 61.00 | 409.72 | 318.29 | NÃO | fora da faixa vertical |
| 60 | 204.00 | 61.00 | 410.36 | 318.29 | NÃO | fora da faixa vertical |
| 61 | 203.00 | 62.00 | 410.23 | 317.29 | NÃO | fora da faixa vertical |
| 62 | 202.00 | 62.00 | 410.88 | 317.29 | NÃO | fora da faixa vertical |
| 63 | 201.00 | 63.00 | 410.76 | 316.29 | NÃO | fora da faixa vertical |
| 64 | 200.00 | 63.00 | 411.41 | 316.29 | NÃO | fora da faixa vertical |
| 65 | 199.00 | 63.00 | 412.06 | 316.29 | NÃO | fora da faixa vertical |
| 66 | 198.00 | 64.00 | 411.95 | 315.29 | NÃO | fora da faixa vertical |
| 67 | 197.00 | 64.00 | 412.61 | 315.29 | NÃO | fora da faixa vertical |
| 68 | 196.00 | 65.00 | 412.51 | 314.29 | NÃO | fora da faixa vertical |
| 69 | 195.00 | 65.00 | 413.16 | 314.29 | NÃO | fora da faixa vertical |
| 70 | 194.00 | 66.00 | 413.07 | 313.29 | NÃO | fora da faixa vertical |
| 71 | 193.00 | 66.00 | 413.73 | 313.29 | NÃO | fora da faixa vertical |
| 72 | 192.00 | 67.00 | 413.65 | 312.29 | NÃO | fora da faixa vertical |
| 73 | 191.00 | 67.00 | 414.32 | 312.29 | NÃO | fora da faixa vertical |
| 74 | 190.00 | 68.00 | 414.24 | 311.29 | NÃO | fora da faixa vertical |
| 75 | 189.00 | 68.00 | 414.91 | 311.29 | NÃO | fora da faixa vertical |
| 76 | 188.00 | 69.00 | 414.84 | 310.29 | NÃO | fora da faixa vertical |
| 77 | 187.00 | 69.00 | 415.51 | 310.29 | NÃO | fora da faixa vertical |
| 78 | 186.00 | 70.00 | 415.45 | 309.29 | NÃO | fora da faixa vertical |
| 79 | 185.00 | 70.00 | 416.12 | 309.29 | NÃO | fora da faixa vertical |
| 80 | 184.00 | 71.00 | 416.07 | 308.29 | NÃO | fora da faixa vertical |
| 81 | 183.00 | 71.00 | 416.75 | 308.29 | NÃO | fora da faixa vertical |
| 82 | 182.00 | 72.00 | 416.70 | 307.29 | NÃO | fora da faixa vertical |
| 83 | 181.00 | 72.00 | 417.39 | 307.29 | NÃO | fora da faixa vertical |
| 84 | 180.00 | 73.00 | 417.35 | 306.29 | NÃO | fora da faixa vertical |
| 85 | 179.00 | 74.00 | 417.31 | 305.29 | NÃO | fora da faixa vertical |
| 86 | 178.00 | 74.00 | 418.00 | 305.29 | NÃO | fora da faixa vertical |
| 87 | 177.00 | 75.00 | 417.97 | 304.29 | NÃO | fora da faixa vertical |
| 88 | 176.00 | 75.00 | 418.67 | 304.29 | NÃO | fora da faixa vertical |
| 89 | 175.00 | 76.00 | 418.65 | 303.29 | NÃO | fora da faixa vertical |
| 90 | 174.00 | 77.00 | 418.63 | 302.29 | NÃO | fora da faixa vertical |
| 91 | 173.00 | 77.00 | 419.33 | 302.29 | NÃO | fora da faixa vertical |
| 92 | 172.00 | 78.00 | 419.32 | 301.29 | NÃO | fora da faixa vertical |
| 93 | 171.00 | 78.00 | 420.02 | 301.29 | NÃO | fora da faixa vertical |
| 94 | 170.00 | 79.00 | 420.02 | 300.29 | NÃO | fora da faixa vertical |
| 95 | 169.00 | 80.00 | 420.02 | 299.29 | NÃO | fora da faixa vertical |
| 96 | 168.00 | 80.00 | 420.73 | 299.29 | NÃO | fora da faixa vertical |
| 97 | 167.00 | 81.00 | 420.74 | 298.29 | NÃO | fora da faixa vertical |
| 98 | 166.00 | 82.00 | 420.76 | 297.29 | NÃO | fora da faixa vertical |
| 99 | 165.00 | 82.00 | 421.47 | 297.29 | NÃO | fora da faixa vertical |
| 100 | 164.00 | 83.00 | 421.49 | 296.29 | NÃO | fora da faixa vertical |
| 101 | 163.00 | 84.00 | 421.52 | 295.29 | NÃO | fora da faixa vertical |
| 102 | 162.00 | 85.00 | 421.55 | 294.29 | NÃO | fora da faixa vertical |
| 103 | 161.00 | 85.00 | 422.28 | 294.29 | NÃO | fora da faixa vertical |
| 104 | 160.00 | 86.00 | 422.31 | 293.29 | NÃO | fora da faixa vertical |
| 105 | 159.00 | 87.00 | 422.36 | 292.29 | NÃO | fora da faixa vertical |
| 106 | 158.00 | 88.00 | 422.40 | 291.29 | NÃO | fora da faixa vertical |
| 107 | 157.00 | 88.00 | 423.14 | 291.29 | NÃO | fora da faixa vertical |
| 108 | 156.00 | 89.00 | 423.19 | 290.29 | NÃO | fora da faixa vertical |
| 109 | 155.00 | 90.00 | 423.25 | 289.29 | NÃO | fora da faixa vertical |
| 110 | 154.00 | 91.00 | 423.31 | 288.29 | NÃO | fora da faixa vertical |
| 111 | 153.00 | 91.00 | 424.05 | 288.29 | NÃO | fora da faixa vertical |
| 112 | 152.00 | 92.00 | 424.12 | 287.29 | NÃO | fora da faixa vertical |
| 113 | 151.00 | 93.00 | 424.20 | 286.29 | NÃO | fora da faixa vertical |
| 114 | 150.00 | 94.00 | 424.28 | 285.29 | NÃO | fora da faixa vertical |
| 115 | 149.00 | 95.00 | 424.36 | 284.29 | NÃO | fora da faixa vertical |
| 116 | 148.00 | 95.00 | 425.11 | 284.29 | NÃO | fora da faixa vertical |
| 117 | 147.00 | 96.00 | 425.21 | 283.29 | NÃO | fora da faixa vertical |
| 118 | 146.00 | 97.00 | 425.30 | 282.29 | NÃO | fora da faixa vertical |
| 119 | 145.00 | 98.00 | 425.40 | 281.29 | NÃO | fora da faixa vertical |
| 120 | 144.00 | 99.00 | 425.51 | 280.29 | NÃO | fora da faixa vertical |
| 121 | 143.00 | 100.00 | 425.62 | 279.29 | NÃO | fora da faixa vertical |
| 122 | 142.00 | 101.00 | 425.73 | 278.29 | NÃO | fora da faixa vertical |
| 123 | 141.00 | 102.00 | 425.85 | 277.29 | NÃO | fora da faixa vertical |
| 124 | 140.00 | 103.00 | 425.98 | 276.29 | NÃO | fora da faixa vertical |
| 125 | 139.00 | 104.00 | 426.11 | 275.29 | NÃO | fora da faixa vertical |
| 126 | 138.00 | 105.00 | 426.24 | 274.29 | NÃO | fora da faixa vertical |
| 127 | 137.00 | 106.00 | 426.38 | 273.29 | NÃO | fora da faixa vertical |
| 128 | 136.00 | 107.00 | 426.52 | 272.29 | NÃO | fora da faixa vertical |
| 129 | 135.00 | 108.00 | 426.67 | 271.29 | NÃO | fora da faixa vertical |
| 130 | 134.00 | 109.00 | 426.82 | 270.29 | NÃO | fora da faixa vertical |
| 131 | 133.00 | 110.00 | 426.98 | 269.29 | NÃO | fora da faixa vertical |
| 132 | 132.00 | 111.00 | 427.14 | 268.29 | NÃO | fora da faixa vertical |
| 133 | 131.00 | 112.00 | 427.31 | 267.29 | NÃO | fora da faixa vertical |
| 134 | 130.00 | 113.00 | 427.48 | 266.29 | NÃO | fora da faixa vertical |
| 135 | 129.00 | 114.00 | 427.65 | 265.29 | NÃO | fora da faixa vertical |
| 136 | 128.00 | 115.00 | 427.83 | 264.29 | NÃO | fora da faixa vertical |
| 137 | 127.00 | 116.00 | 428.02 | 263.29 | NÃO | fora da faixa vertical |
| 138 | 126.00 | 117.00 | 428.21 | 262.29 | NÃO | fora da faixa vertical |
| 139 | 126.00 | 118.00 | 427.60 | 261.29 | NÃO | fora da faixa vertical |
| 140 | 125.00 | 119.00 | 427.80 | 260.29 | NÃO | fora da faixa vertical |
| 141 | 124.00 | 120.00 | 428.00 | 259.29 | NÃO | fora da faixa vertical |
| 142 | 123.00 | 121.00 | 428.21 | 258.29 | NÃO | fora da faixa vertical |
| 143 | 122.00 | 122.00 | 428.42 | 257.29 | NÃO | fora da faixa vertical |
| 144 | 121.00 | 123.00 | 428.63 | 256.29 | NÃO | fora da faixa vertical |
| 145 | 121.00 | 124.00 | 428.04 | 255.29 | NÃO | fora da faixa vertical |
| 146 | 120.00 | 125.00 | 428.26 | 254.29 | NÃO | fora da faixa vertical |
| 147 | 119.00 | 126.00 | 428.49 | 253.29 | NÃO | fora da faixa vertical |
| 148 | 118.00 | 127.00 | 428.72 | 252.29 | NÃO | fora da faixa vertical |
| 149 | 118.00 | 128.00 | 428.14 | 251.29 | NÃO | fora da faixa vertical |
| 150 | 117.00 | 129.00 | 428.38 | 250.29 | NÃO | fora da faixa vertical |
| 151 | 116.00 | 130.00 | 428.62 | 249.29 | NÃO | fora da faixa vertical |
| 152 | 115.00 | 131.00 | 428.87 | 248.29 | NÃO | fora da faixa vertical |
| 153 | 115.00 | 132.00 | 428.30 | 247.29 | NÃO | fora da faixa vertical |
| 154 | 114.00 | 133.00 | 428.55 | 246.29 | NÃO | fora da faixa vertical |
| 155 | 113.00 | 134.00 | 428.81 | 245.29 | NÃO | fora da faixa vertical |
| 156 | 112.00 | 135.00 | 429.08 | 244.29 | NÃO | fora da faixa vertical |
| 157 | 112.00 | 136.00 | 428.51 | 243.29 | NÃO | fora da faixa vertical |
| 158 | 111.00 | 137.00 | 428.79 | 242.29 | NÃO | fora da faixa vertical |
| 159 | 110.00 | 138.00 | 429.06 | 241.29 | NÃO | fora da faixa vertical |
| 160 | 110.00 | 139.00 | 428.51 | 240.29 | NÃO | fora da faixa vertical |
| 161 | 109.00 | 140.00 | 428.79 | 239.29 | NÃO | fora da faixa vertical |
| 162 | 109.00 | 141.00 | 428.24 | 238.29 | NÃO | fora da faixa vertical |
| 163 | 108.00 | 142.00 | 428.53 | 237.29 | NÃO | fora da faixa vertical |
| 164 | 107.00 | 143.00 | 428.82 | 236.29 | NÃO | fora da faixa vertical |
| 165 | 107.00 | 144.00 | 428.28 | 235.29 | NÃO | fora da faixa vertical |
| 166 | 106.00 | 145.00 | 428.58 | 234.29 | NÃO | fora da faixa vertical |
| 167 | 105.00 | 146.00 | 428.89 | 233.29 | NÃO | fora da faixa vertical |
| 168 | 105.00 | 147.00 | 428.35 | 232.29 | NÃO | fora da faixa vertical |
| 169 | 104.00 | 148.00 | 428.66 | 231.29 | NÃO | fora da faixa vertical |
| 170 | 104.00 | 149.00 | 428.13 | 230.29 | NÃO | fora da faixa vertical |
| 171 | 103.00 | 150.00 | 428.45 | 229.29 | NÃO | fora da faixa vertical |
| 172 | 102.00 | 151.00 | 428.78 | 228.29 | NÃO | fora da faixa vertical |
| 173 | 102.00 | 152.00 | 428.25 | 227.29 | NÃO | fora da faixa vertical |
| 174 | 101.00 | 153.00 | 428.58 | 226.29 | NÃO | fora da faixa vertical |
| 175 | 101.00 | 154.00 | 428.07 | 225.29 | NÃO | fora da faixa vertical |
| 176 | 100.00 | 155.00 | 428.40 | 224.29 | NÃO | fora da faixa vertical |
| 177 | 100.00 | 156.00 | 427.89 | 223.29 | NÃO | fora da faixa vertical |
| 178 | 99.00 | 157.00 | 428.23 | 222.29 | NÃO | fora da faixa vertical |
| 179 | 99.00 | 158.00 | 427.72 | 221.29 | NÃO | fora da faixa vertical |
| 180 | 98.00 | 159.00 | 428.08 | 220.29 | NÃO | fora da faixa vertical |
| 181 | 98.00 | 160.00 | 427.57 | 219.29 | NÃO | fora da faixa vertical |
| 182 | 97.00 | 161.00 | 427.93 | 218.29 | NÃO | fora da faixa vertical |
| 183 | 97.00 | 162.00 | 427.43 | 217.29 | NÃO | fora da faixa vertical |
| 184 | 96.00 | 163.00 | 427.80 | 216.29 | NÃO | fora da faixa vertical |
| 185 | 96.00 | 164.00 | 427.30 | 215.29 | NÃO | fora da faixa vertical |
| 186 | 95.00 | 165.00 | 427.67 | 214.29 | NÃO | fora da faixa vertical |
| 187 | 95.00 | 166.00 | 427.18 | 213.29 | NÃO | fora da faixa vertical |
| 188 | 94.00 | 167.00 | 427.56 | 212.29 | NÃO | fora da faixa vertical |
| 189 | 94.00 | 168.00 | 427.07 | 211.29 | NÃO | fora da faixa vertical |
| 190 | 93.00 | 169.00 | 427.46 | 210.29 | NÃO | fora da faixa vertical |
| 191 | 93.00 | 170.00 | 426.98 | 209.29 | NÃO | fora da faixa vertical |
| 192 | 93.00 | 171.00 | 426.50 | 208.29 | NÃO | fora da faixa vertical |
| 193 | 92.00 | 172.00 | 426.90 | 207.29 | NÃO | fora da faixa vertical |
| 194 | 92.00 | 173.00 | 426.42 | 206.29 | NÃO | fora da faixa vertical |
| 195 | 91.00 | 174.00 | 426.83 | 205.29 | NÃO | fora da faixa vertical |
| 196 | 91.00 | 175.00 | 426.35 | 204.29 | NÃO | fora da faixa vertical |
| 197 | 91.00 | 176.00 | 425.88 | 203.29 | NÃO | fora da faixa vertical |
| 198 | 90.00 | 177.00 | 426.30 | 202.29 | NÃO | fora da faixa vertical |
| 199 | 90.00 | 178.00 | 425.83 | 201.29 | NÃO | fora da faixa vertical |
| 200 | 90.00 | 179.00 | 425.37 | 200.29 | NÃO | fora da faixa vertical |
| 201 | 89.00 | 180.00 | 425.79 | 199.29 | NÃO | fora da faixa vertical |
| 202 | 89.00 | 181.00 | 425.33 | 198.29 | NÃO | fora da faixa vertical |
| 203 | 88.00 | 182.00 | 425.77 | 197.29 | NÃO | fora da faixa vertical |
| 204 | 88.00 | 183.00 | 425.31 | 196.29 | NÃO | fora da faixa vertical |
| 205 | 88.00 | 184.00 | 424.86 | 195.29 | NÃO | fora da faixa vertical |
| 206 | 87.00 | 185.00 | 425.30 | 194.29 | NÃO | fora da faixa vertical |
| 207 | 87.00 | 186.00 | 424.85 | 193.29 | NÃO | fora da faixa vertical |
| 208 | 87.00 | 187.00 | 424.41 | 192.29 | NÃO | fora da faixa vertical |
| 209 | 86.00 | 188.00 | 424.86 | 191.29 | NÃO | fora da faixa vertical |
| 210 | 86.00 | 189.00 | 424.42 | 190.29 | NÃO | fora da faixa vertical |
| 211 | 86.00 | 190.00 | 423.98 | 189.29 | NÃO | fora da faixa vertical |
| 212 | 86.00 | 191.00 | 423.54 | 188.29 | NÃO | fora da faixa vertical |
| 213 | 85.00 | 192.00 | 424.00 | 187.29 | NÃO | fora da faixa vertical |
| 214 | 85.00 | 193.00 | 423.57 | 186.29 | NÃO | fora da faixa vertical |
| 215 | 85.00 | 194.00 | 423.14 | 185.29 | NÃO | fora da faixa vertical |
| 216 | 84.00 | 195.00 | 423.62 | 184.29 | NÃO | fora da faixa vertical |
| 217 | 84.00 | 196.00 | 423.19 | 183.29 | NÃO | fora da faixa vertical |
| 218 | 84.00 | 197.00 | 422.76 | 182.29 | NÃO | fora da faixa vertical |
| 219 | 84.00 | 198.00 | 422.34 | 181.29 | NÃO | fora da faixa vertical |
| 220 | 83.00 | 199.00 | 422.83 | 180.29 | NÃO | fora da faixa vertical |
| 221 | 83.00 | 200.00 | 422.41 | 179.29 | NÃO | fora do lado solicitado |
| 222 | 83.00 | 201.00 | 422.00 | 178.29 | NÃO | fora do lado solicitado |
| 223 | 83.00 | 202.00 | 421.58 | 177.29 | NÃO | fora do lado solicitado |
| 224 | 82.00 | 203.00 | 422.08 | 176.29 | NÃO | fora do lado solicitado |
| 225 | 82.00 | 204.00 | 421.67 | 175.29 | NÃO | fora do lado solicitado |
| 226 | 82.00 | 205.00 | 421.27 | 174.29 | NÃO | fora do lado solicitado |
| 227 | 82.00 | 206.00 | 420.86 | 173.29 | NÃO | fora do lado solicitado |
| 228 | 82.00 | 207.00 | 420.46 | 172.29 | NÃO | fora do lado solicitado |
| 229 | 81.00 | 208.00 | 420.98 | 171.29 | NÃO | fora do lado solicitado |
| 230 | 81.00 | 209.00 | 420.58 | 170.29 | NÃO | fora do lado solicitado |
| 231 | 81.00 | 210.00 | 420.18 | 169.29 | NÃO | fora do lado solicitado |
| 232 | 81.00 | 211.00 | 419.79 | 168.29 | NÃO | fora do lado solicitado |
| 233 | 81.00 | 212.00 | 419.39 | 167.29 | NÃO | fora do lado solicitado |
| 234 | 80.00 | 213.00 | 419.93 | 166.29 | NÃO | fora do lado solicitado |
| 235 | 80.00 | 214.00 | 419.54 | 165.29 | NÃO | fora do lado solicitado |
| 236 | 80.00 | 215.00 | 419.15 | 164.29 | NÃO | fora do lado solicitado |
| 237 | 80.00 | 216.00 | 418.77 | 163.29 | NÃO | fora do lado solicitado |
| 238 | 80.00 | 217.00 | 418.39 | 162.29 | NÃO | fora do lado solicitado |
| 239 | 79.00 | 218.00 | 418.94 | 161.29 | NÃO | fora do lado solicitado |
| 240 | 79.00 | 219.00 | 418.56 | 160.29 | NÃO | fora do lado solicitado |
| 241 | 79.00 | 220.00 | 418.19 | 159.29 | NÃO | fora do lado solicitado |
| 242 | 79.00 | 221.00 | 417.81 | 158.29 | NÃO | fora do lado solicitado |
| 243 | 79.00 | 222.00 | 417.44 | 157.29 | NÃO | fora do lado solicitado |
| 244 | 79.00 | 223.00 | 417.08 | 156.29 | NÃO | fora do lado solicitado |
| 245 | 79.00 | 224.00 | 416.71 | 155.29 | NÃO | fora do lado solicitado |
| 246 | 79.00 | 225.00 | 416.35 | 154.29 | NÃO | fora do lado solicitado |
| 247 | 78.00 | 226.00 | 416.92 | 153.29 | NÃO | fora do lado solicitado |
| 248 | 78.00 | 227.00 | 416.56 | 152.29 | NÃO | fora do lado solicitado |
| 249 | 78.00 | 228.00 | 416.20 | 151.29 | NÃO | fora do lado solicitado |
| 250 | 78.00 | 229.00 | 415.85 | 150.29 | NÃO | fora do lado solicitado |
| 251 | 78.00 | 230.00 | 415.50 | 149.29 | NÃO | fora do lado solicitado |
| 252 | 78.00 | 231.00 | 415.15 | 148.29 | NÃO | fora do lado solicitado |
| 253 | 78.00 | 232.00 | 414.80 | 147.29 | NÃO | fora do lado solicitado |
| 254 | 78.00 | 233.00 | 414.45 | 146.29 | NÃO | fora do lado solicitado |
| 255 | 77.00 | 234.00 | 415.05 | 145.29 | NÃO | fora do lado solicitado |
| 256 | 77.00 | 235.00 | 414.71 | 144.29 | NÃO | fora do lado solicitado |
| 257 | 77.00 | 236.00 | 414.37 | 143.29 | NÃO | fora do lado solicitado |
| 258 | 77.00 | 237.00 | 414.03 | 142.29 | NÃO | fora do lado solicitado |
| 259 | 77.00 | 238.00 | 413.70 | 141.29 | NÃO | fora do lado solicitado |
| 260 | 77.00 | 239.00 | 413.36 | 140.29 | NÃO | fora do lado solicitado |
| 261 | 77.00 | 240.00 | 413.03 | 139.29 | NÃO | fora do lado solicitado |
| 262 | 77.00 | 241.00 | 412.70 | 138.29 | NÃO | fora do lado solicitado |
| 263 | 77.00 | 242.00 | 412.38 | 137.29 | NÃO | fora do lado solicitado |
| 264 | 77.00 | 243.00 | 412.05 | 136.29 | NÃO | fora do lado solicitado |
| 265 | 77.00 | 244.00 | 411.73 | 135.29 | NÃO | fora do lado solicitado |
| 266 | 77.00 | 245.00 | 411.41 | 134.29 | NÃO | fora do lado solicitado |
| 267 | 77.00 | 246.00 | 411.10 | 133.29 | NÃO | fora do lado solicitado |
| 268 | 77.00 | 247.00 | 410.78 | 132.29 | NÃO | fora do lado solicitado |
| 269 | 77.00 | 248.00 | 410.47 | 131.29 | NÃO | fora do lado solicitado |
| 270 | 77.00 | 249.00 | 410.16 | 130.29 | NÃO | fora do lado solicitado |
| 271 | 77.00 | 250.00 | 409.85 | 129.29 | NÃO | fora do lado solicitado |
| 272 | 77.00 | 251.00 | 409.54 | 128.29 | NÃO | fora do lado solicitado |
| 273 | 77.00 | 252.00 | 409.24 | 127.29 | NÃO | fora do lado solicitado |
| 274 | 77.00 | 253.00 | 408.94 | 126.29 | NÃO | fora do lado solicitado |
| 275 | 77.00 | 254.00 | 408.64 | 125.29 | NÃO | fora do lado solicitado |
| 276 | 77.00 | 255.00 | 408.34 | 124.29 | NÃO | fora do lado solicitado |
| 277 | 77.00 | 256.00 | 408.04 | 123.29 | NÃO | fora do lado solicitado |
| 278 | 77.00 | 257.00 | 407.75 | 122.29 | NÃO | fora do lado solicitado |
| 279 | 77.00 | 258.00 | 407.46 | 121.29 | NÃO | fora do lado solicitado |
| 280 | 77.00 | 259.00 | 407.17 | 120.29 | NÃO | fora do lado solicitado |
| 281 | 77.00 | 260.00 | 406.89 | 119.29 | NÃO | fora do lado solicitado |
| 282 | 77.00 | 261.00 | 406.60 | 118.29 | NÃO | fora do lado solicitado |
| 283 | 77.00 | 262.00 | 406.32 | 117.29 | NÃO | fora do lado solicitado |
| 284 | 77.00 | 263.00 | 406.04 | 116.29 | NÃO | fora do lado solicitado |
| 285 | 77.00 | 264.00 | 405.76 | 115.29 | NÃO | fora do lado solicitado |
| 286 | 77.00 | 265.00 | 405.49 | 114.29 | NÃO | fora do lado solicitado |
| 287 | 78.00 | 266.00 | 404.25 | 113.29 | NÃO | fora do lado solicitado |
| 288 | 78.00 | 267.00 | 403.98 | 112.29 | NÃO | fora do lado solicitado |
| 289 | 78.00 | 268.00 | 403.71 | 111.29 | NÃO | fora do lado solicitado |
| 290 | 78.00 | 269.00 | 403.45 | 110.29 | NÃO | fora do lado solicitado |
| 291 | 78.00 | 270.00 | 403.18 | 109.29 | NÃO | fora do lado solicitado |
| 292 | 78.00 | 271.00 | 402.92 | 108.29 | NÃO | fora do lado solicitado |
| 293 | 78.00 | 272.00 | 402.66 | 107.29 | NÃO | fora do lado solicitado |
| 294 | 78.00 | 273.00 | 402.41 | 106.29 | NÃO | fora do lado solicitado |
| 295 | 78.00 | 274.00 | 402.15 | 105.29 | NÃO | fora do lado solicitado |
| 296 | 79.00 | 275.00 | 400.93 | 104.29 | NÃO | fora do lado solicitado |
| 297 | 79.00 | 276.00 | 400.68 | 103.29 | NÃO | fora do lado solicitado |
| 298 | 79.00 | 277.00 | 400.43 | 102.29 | NÃO | fora do lado solicitado |
| 299 | 79.00 | 278.00 | 400.18 | 101.29 | NÃO | fora do lado solicitado |
| 300 | 79.00 | 279.00 | 399.94 | 100.29 | NÃO | fora do lado solicitado |
| 301 | 79.00 | 280.00 | 399.70 | 99.29 | NÃO | fora do lado solicitado |
| 302 | 79.00 | 281.00 | 399.46 | 98.29 | NÃO | fora do lado solicitado |
| 303 | 79.00 | 282.00 | 399.22 | 97.29 | NÃO | fora do lado solicitado |
| 304 | 80.00 | 283.00 | 398.02 | 96.29 | NÃO | fora do lado solicitado |
| 305 | 80.00 | 284.00 | 397.79 | 95.29 | NÃO | fora do lado solicitado |
| 306 | 80.00 | 285.00 | 397.56 | 94.29 | NÃO | fora do lado solicitado |
| 307 | 80.00 | 286.00 | 397.33 | 93.29 | NÃO | fora do lado solicitado |
| 308 | 80.00 | 287.00 | 397.10 | 92.29 | NÃO | fora do lado solicitado |
| 309 | 81.00 | 288.00 | 395.90 | 91.29 | NÃO | fora do lado solicitado |
| 310 | 81.00 | 289.00 | 395.68 | 90.29 | NÃO | fora do lado solicitado |
| 311 | 81.00 | 290.00 | 395.46 | 89.29 | NÃO | fora do lado solicitado |
| 312 | 81.00 | 291.00 | 395.25 | 88.29 | NÃO | fora do lado solicitado |
| 313 | 82.00 | 292.00 | 394.06 | 87.29 | NÃO | fora do lado solicitado |
| 314 | 82.00 | 293.00 | 393.85 | 86.29 | NÃO | fora do lado solicitado |
| 315 | 82.00 | 294.00 | 393.64 | 85.29 | NÃO | fora do lado solicitado |
| 316 | 82.00 | 295.00 | 393.43 | 84.29 | NÃO | fora do lado solicitado |
| 317 | 82.00 | 296.00 | 393.22 | 83.29 | NÃO | fora do lado solicitado |
| 318 | 83.00 | 297.00 | 392.04 | 82.29 | NÃO | fora do lado solicitado |
| 319 | 83.00 | 298.00 | 391.84 | 81.29 | NÃO | fora do lado solicitado |
| 320 | 83.00 | 299.00 | 391.64 | 80.29 | NÃO | fora do lado solicitado |
| 321 | 83.00 | 300.00 | 391.45 | 79.29 | NÃO | fora do lado solicitado |
| 322 | 84.00 | 301.00 | 390.27 | 78.29 | NÃO | fora do lado solicitado |
| 323 | 84.00 | 302.00 | 390.08 | 77.29 | NÃO | fora do lado solicitado |
| 324 | 84.00 | 303.00 | 389.89 | 76.29 | NÃO | fora do lado solicitado |
| 325 | 84.00 | 304.00 | 389.71 | 75.29 | NÃO | fora do lado solicitado |
| 326 | 85.00 | 305.00 | 388.54 | 74.29 | NÃO | fora do lado solicitado |
| 327 | 85.00 | 306.00 | 388.36 | 73.29 | NÃO | fora do lado solicitado |
| 328 | 85.00 | 307.00 | 388.18 | 72.29 | NÃO | fora do lado solicitado |
| 329 | 86.00 | 308.00 | 387.02 | 71.29 | NÃO | fora do lado solicitado |
| 330 | 86.00 | 309.00 | 386.85 | 70.29 | NÃO | fora do lado solicitado |
| 331 | 86.00 | 310.00 | 386.67 | 69.29 | NÃO | fora do lado solicitado |
| 332 | 86.00 | 311.00 | 386.50 | 68.29 | NÃO | fora do lado solicitado |
| 333 | 87.00 | 312.00 | 385.35 | 67.29 | NÃO | fora do lado solicitado |
| 334 | 87.00 | 313.00 | 385.19 | 66.29 | NÃO | fora do lado solicitado |
| 335 | 87.00 | 314.00 | 385.02 | 65.29 | NÃO | fora do lado solicitado |
| 336 | 88.00 | 315.00 | 383.88 | 64.29 | NÃO | fora do lado solicitado |
| 337 | 88.00 | 316.00 | 383.72 | 63.29 | NÃO | fora do lado solicitado |
| 338 | 88.00 | 317.00 | 383.56 | 62.29 | NÃO | fora do lado solicitado |
| 339 | 89.00 | 318.00 | 382.42 | 61.29 | NÃO | fora do lado solicitado |
| 340 | 89.00 | 319.00 | 382.27 | 60.29 | NÃO | fora do lado solicitado |
| 341 | 89.00 | 320.00 | 382.13 | 59.29 | NÃO | fora do lado solicitado |
| 342 | 90.00 | 321.00 | 380.99 | 58.29 | NÃO | fora do lado solicitado |
| 343 | 90.00 | 322.00 | 380.85 | 57.29 | NÃO | fora do lado solicitado |
| 344 | 91.00 | 323.00 | 379.72 | 56.29 | NÃO | fora do lado solicitado |
| 345 | 91.00 | 324.00 | 379.58 | 55.29 | NÃO | fora do lado solicitado |
| 346 | 91.00 | 325.00 | 379.44 | 54.29 | NÃO | fora do lado solicitado |
| 347 | 92.00 | 326.00 | 378.32 | 53.29 | NÃO | fora do lado solicitado |
| 348 | 92.00 | 327.00 | 378.19 | 52.29 | NÃO | fora do lado solicitado |
| 349 | 92.00 | 328.00 | 378.06 | 51.29 | NÃO | fora do lado solicitado |
| 350 | 93.00 | 329.00 | 376.94 | 50.29 | NÃO | fora do lado solicitado |
| 351 | 93.00 | 330.00 | 376.82 | 49.29 | NÃO | fora do lado solicitado |
| 352 | 94.00 | 331.00 | 375.70 | 48.29 | NÃO | fora do lado solicitado |
| 353 | 94.00 | 332.00 | 375.59 | 47.29 | NÃO | fora do lado solicitado |
| 354 | 95.00 | 333.00 | 374.48 | 46.29 | NÃO | fora do lado solicitado |
| 355 | 95.00 | 334.00 | 374.36 | 45.29 | NÃO | fora do lado solicitado |
| 356 | 96.00 | 335.00 | 373.26 | 44.29 | NÃO | fora do lado solicitado |
| 357 | 96.00 | 336.00 | 373.15 | 43.29 | NÃO | fora do lado solicitado |
| 358 | 97.00 | 337.00 | 372.05 | 42.29 | NÃO | fora do lado solicitado |
| 359 | 97.00 | 338.00 | 371.95 | 41.29 | NÃO | fora do lado solicitado |
| 360 | 98.00 | 339.00 | 370.85 | 40.29 | NÃO | fora do lado solicitado |
| 361 | 98.00 | 340.00 | 370.75 | 39.29 | NÃO | fora do lado solicitado |
| 362 | 99.00 | 341.00 | 369.66 | 38.29 | NÃO | fora do lado solicitado |
| 363 | 99.00 | 342.00 | 369.57 | 37.29 | NÃO | fora do lado solicitado |
| 364 | 100.00 | 343.00 | 368.48 | 36.29 | NÃO | fora do lado solicitado |
| 365 | 100.00 | 344.00 | 368.39 | 35.29 | NÃO | fora do lado solicitado |
| 366 | 101.00 | 345.00 | 367.31 | 34.29 | NÃO | fora do lado solicitado |
| 367 | 101.00 | 346.00 | 367.23 | 33.29 | NÃO | fora do lado solicitado |
| 368 | 102.00 | 347.00 | 366.15 | 32.29 | NÃO | fora do lado solicitado |
| 369 | 102.00 | 348.00 | 366.07 | 31.29 | NÃO | fora do lado solicitado |
| 370 | 103.00 | 349.00 | 365.00 | 30.29 | NÃO | fora do lado solicitado |
| 371 | 103.00 | 350.00 | 364.93 | 29.29 | NÃO | fora do lado solicitado |
| 372 | 104.00 | 351.00 | 363.86 | 28.29 | NÃO | fora do lado solicitado |
| 373 | 105.00 | 352.00 | 362.79 | 27.29 | NÃO | fora do lado solicitado |
| 374 | 105.00 | 353.00 | 362.73 | 26.29 | NÃO | fora do lado solicitado |
| 375 | 106.00 | 354.00 | 361.67 | 25.29 | NÃO | fora do lado solicitado |
| 376 | 107.00 | 355.00 | 360.61 | 24.29 | NÃO | fora do lado solicitado |
| 377 | 107.00 | 356.00 | 360.56 | 23.29 | NÃO | fora do lado solicitado |
| 378 | 108.00 | 357.00 | 359.50 | 22.29 | NÃO | fora do lado solicitado |
| 379 | 108.00 | 358.00 | 359.45 | 21.29 | NÃO | fora do lado solicitado |
| 380 | 109.00 | 359.00 | 358.40 | 20.29 | NÃO | fora do lado solicitado |
| 381 | 110.00 | 360.00 | 357.36 | 19.29 | NÃO | fora do lado solicitado |
| 382 | 110.00 | 361.00 | 357.31 | 18.29 | NÃO | fora do lado solicitado |
| 383 | 111.00 | 362.00 | 356.28 | 17.29 | NÃO | fora do lado solicitado |
| 384 | 112.00 | 363.00 | 355.24 | 16.29 | NÃO | fora do lado solicitado |
| 385 | 112.00 | 364.00 | 355.20 | 15.29 | NÃO | fora do lado solicitado |
| 386 | 113.00 | 365.00 | 354.17 | 14.29 | NÃO | fora do lado solicitado |
| 387 | 114.00 | 366.00 | 353.14 | 13.29 | NÃO | fora do lado solicitado |
| 388 | 114.00 | 367.00 | 353.11 | 12.29 | NÃO | fora do lado solicitado |
| 389 | 115.00 | 368.00 | 352.09 | 11.29 | NÃO | fora do lado solicitado |
| 390 | 116.00 | 369.00 | 351.07 | 10.29 | NÃO | fora do lado solicitado |
| 391 | 117.00 | 370.00 | 350.05 | 9.29 | NÃO | fora do lado solicitado |
| 392 | 117.00 | 371.00 | 350.04 | 8.29 | NÃO | fora do lado solicitado |
| 393 | 118.00 | 372.00 | 349.02 | 7.29 | NÃO | fora do lado solicitado |
| 394 | 119.00 | 373.00 | 348.01 | 6.29 | NÃO | fora do lado solicitado |
| 395 | 120.00 | 374.00 | 347.01 | 5.29 | NÃO | fora do lado solicitado |
| 396 | 120.00 | 375.00 | 347.00 | 4.29 | NÃO | fora do lado solicitado |
| 397 | 120.00 | 376.00 | 347.00 | 3.29 | NÃO | fora do lado solicitado |
| 398 | 121.00 | 376.00 | 346.00 | 3.29 | NÃO | fora do lado solicitado |
| 399 | 122.00 | 376.00 | 345.00 | 3.29 | NÃO | fora do lado solicitado |
| 400 | 123.00 | 376.00 | 344.00 | 3.29 | NÃO | fora do lado solicitado |
| 401 | 124.00 | 376.00 | 343.00 | 3.29 | NÃO | fora do lado solicitado |
| 402 | 125.00 | 376.00 | 342.00 | 3.29 | NÃO | fora do lado solicitado |
| 403 | 126.00 | 376.00 | 341.00 | 3.29 | NÃO | fora do lado solicitado |
| 404 | 127.00 | 376.00 | 340.00 | 3.29 | NÃO | fora do lado solicitado |
| 405 | 128.00 | 376.00 | 339.00 | 3.29 | NÃO | fora do lado solicitado |
| 406 | 129.00 | 376.00 | 338.00 | 3.29 | NÃO | fora do lado solicitado |
| 407 | 130.00 | 376.00 | 337.00 | 3.29 | NÃO | fora do lado solicitado |
| 408 | 131.00 | 376.00 | 336.00 | 3.29 | NÃO | fora do lado solicitado |
| 409 | 132.00 | 376.00 | 335.00 | 3.29 | NÃO | fora do lado solicitado |
| 410 | 133.00 | 376.00 | 334.00 | 3.29 | NÃO | fora do lado solicitado |
| 411 | 134.00 | 376.00 | 333.00 | 3.29 | NÃO | fora do lado solicitado |
| 412 | 135.00 | 376.00 | 332.00 | 3.29 | NÃO | fora do lado solicitado |
| 413 | 136.00 | 376.00 | 331.00 | 3.29 | NÃO | fora do lado solicitado |
| 414 | 137.00 | 376.00 | 330.00 | 3.29 | NÃO | fora do lado solicitado |
| 415 | 138.00 | 376.00 | 329.00 | 3.29 | NÃO | fora do lado solicitado |
| 416 | 139.00 | 376.00 | 328.00 | 3.29 | NÃO | fora do lado solicitado |
| 417 | 140.00 | 376.00 | 327.00 | 3.29 | NÃO | fora do lado solicitado |
| 418 | 141.00 | 376.00 | 326.00 | 3.29 | NÃO | fora do lado solicitado |
| 419 | 142.00 | 376.00 | 325.00 | 3.29 | NÃO | fora do lado solicitado |
| 420 | 143.00 | 376.00 | 324.00 | 3.29 | NÃO | fora do lado solicitado |
| 421 | 144.00 | 376.00 | 323.00 | 3.29 | NÃO | fora do lado solicitado |
| 422 | 145.00 | 376.00 | 322.00 | 3.29 | NÃO | fora do lado solicitado |
| 423 | 146.00 | 376.00 | 321.00 | 3.29 | NÃO | fora do lado solicitado |
| 424 | 147.00 | 376.00 | 320.00 | 3.29 | NÃO | fora do lado solicitado |
| 425 | 148.00 | 376.00 | 319.00 | 3.29 | NÃO | fora do lado solicitado |
| 426 | 149.00 | 376.00 | 318.00 | 3.29 | NÃO | fora do lado solicitado |
| 427 | 150.00 | 376.00 | 317.00 | 3.29 | NÃO | fora do lado solicitado |
| 428 | 151.00 | 376.00 | 316.00 | 3.29 | NÃO | fora do lado solicitado |
| 429 | 152.00 | 376.00 | 315.00 | 3.29 | NÃO | fora do lado solicitado |
| 430 | 153.00 | 376.00 | 314.00 | 3.29 | NÃO | fora do lado solicitado |
| 431 | 154.00 | 376.00 | 313.00 | 3.29 | NÃO | fora do lado solicitado |
| 432 | 155.00 | 376.00 | 312.00 | 3.29 | NÃO | fora do lado solicitado |
| 433 | 156.00 | 376.00 | 311.00 | 3.29 | NÃO | fora do lado solicitado |
| 434 | 157.00 | 376.00 | 310.00 | 3.29 | NÃO | fora do lado solicitado |
| 435 | 158.00 | 376.00 | 309.00 | 3.29 | NÃO | fora do lado solicitado |
| 436 | 159.00 | 376.00 | 308.00 | 3.29 | NÃO | fora do lado solicitado |
| 437 | 160.00 | 376.00 | 307.00 | 3.29 | NÃO | fora do lado solicitado |
| 438 | 161.00 | 376.00 | 306.00 | 3.29 | NÃO | fora do lado solicitado |
| 439 | 162.00 | 376.00 | 305.00 | 3.29 | NÃO | fora do lado solicitado |
| 440 | 163.00 | 376.00 | 304.00 | 3.29 | NÃO | fora do lado solicitado |
| 441 | 164.00 | 376.00 | 303.00 | 3.29 | NÃO | fora do lado solicitado |
| 442 | 165.00 | 376.00 | 302.00 | 3.29 | NÃO | fora do lado solicitado |
| 443 | 166.00 | 376.00 | 301.00 | 3.29 | NÃO | fora do lado solicitado |
| 444 | 167.00 | 376.00 | 300.00 | 3.29 | NÃO | fora do lado solicitado |
| 445 | 168.00 | 376.00 | 299.00 | 3.29 | NÃO | fora do lado solicitado |
| 446 | 169.00 | 376.00 | 298.00 | 3.29 | NÃO | fora do lado solicitado |
| 447 | 170.00 | 376.00 | 297.00 | 3.29 | NÃO | fora do lado solicitado |
| 448 | 171.00 | 376.00 | 296.00 | 3.29 | NÃO | fora do lado solicitado |
| 449 | 172.00 | 376.00 | 295.00 | 3.29 | NÃO | fora do lado solicitado |
| 450 | 173.00 | 376.00 | 294.00 | 3.29 | NÃO | fora do lado solicitado |
| 451 | 174.00 | 376.00 | 293.00 | 3.29 | NÃO | fora do lado solicitado |
| 452 | 175.00 | 376.00 | 292.00 | 3.29 | NÃO | fora do lado solicitado |
| 453 | 176.00 | 376.00 | 291.00 | 3.29 | NÃO | fora do lado solicitado |
| 454 | 177.00 | 376.00 | 290.00 | 3.29 | NÃO | fora do lado solicitado |
| 455 | 178.00 | 376.00 | 289.00 | 3.29 | NÃO | fora do lado solicitado |
| 456 | 179.00 | 376.00 | 288.00 | 3.29 | NÃO | fora do lado solicitado |
| 457 | 180.00 | 376.00 | 287.00 | 3.29 | NÃO | fora do lado solicitado |
| 458 | 181.00 | 376.00 | 286.00 | 3.29 | NÃO | fora do lado solicitado |
| 459 | 182.00 | 376.00 | 285.00 | 3.29 | NÃO | fora do lado solicitado |
| 460 | 183.00 | 376.00 | 284.00 | 3.29 | NÃO | fora do lado solicitado |
| 461 | 184.00 | 376.00 | 283.00 | 3.29 | NÃO | fora do lado solicitado |
| 462 | 185.00 | 376.00 | 282.00 | 3.29 | NÃO | fora do lado solicitado |
| 463 | 186.00 | 376.00 | 281.00 | 3.29 | NÃO | fora do lado solicitado |
| 464 | 187.00 | 376.00 | 280.00 | 3.29 | NÃO | fora do lado solicitado |
| 465 | 188.00 | 376.00 | 279.00 | 3.29 | NÃO | fora do lado solicitado |
| 466 | 189.00 | 376.00 | 278.00 | 3.29 | NÃO | fora do lado solicitado |
| 467 | 190.00 | 376.00 | 277.00 | 3.29 | NÃO | fora do lado solicitado |
| 468 | 191.00 | 376.00 | 276.00 | 3.29 | NÃO | fora do lado solicitado |
| 469 | 192.00 | 376.00 | 275.00 | 3.29 | NÃO | fora do lado solicitado |
| 470 | 193.00 | 376.00 | 274.00 | 3.29 | NÃO | fora do lado solicitado |
| 471 | 194.00 | 376.00 | 273.00 | 3.29 | NÃO | fora do lado solicitado |
| 472 | 195.00 | 376.00 | 272.00 | 3.29 | NÃO | fora do lado solicitado |
| 473 | 196.00 | 376.00 | 271.00 | 3.29 | NÃO | fora do lado solicitado |
| 474 | 197.00 | 376.00 | 270.00 | 3.29 | NÃO | fora do lado solicitado |
| 475 | 198.00 | 376.00 | 269.00 | 3.29 | NÃO | fora do lado solicitado |
| 476 | 199.00 | 376.00 | 268.00 | 3.29 | NÃO | fora do lado solicitado |
| 477 | 200.00 | 376.00 | 267.00 | 3.29 | NÃO | fora do lado solicitado |
| 478 | 201.00 | 376.00 | 266.00 | 3.29 | NÃO | fora do lado solicitado |
| 479 | 202.00 | 376.00 | 265.00 | 3.29 | NÃO | fora do lado solicitado |
| 480 | 203.00 | 376.00 | 264.00 | 3.29 | NÃO | fora do lado solicitado |
| 481 | 204.00 | 376.00 | 263.00 | 3.29 | NÃO | fora do lado solicitado |
| 482 | 205.00 | 376.00 | 262.00 | 3.29 | NÃO | fora do lado solicitado |
| 483 | 206.00 | 376.00 | 261.00 | 3.29 | NÃO | fora do lado solicitado |
| 484 | 207.00 | 376.00 | 260.00 | 3.29 | NÃO | fora do lado solicitado |
| 485 | 208.00 | 376.00 | 259.00 | 3.29 | NÃO | fora do lado solicitado |
| 486 | 209.00 | 376.00 | 258.00 | 3.29 | NÃO | fora do lado solicitado |
| 487 | 210.00 | 376.00 | 257.00 | 3.29 | NÃO | fora do lado solicitado |
| 488 | 211.00 | 376.00 | 256.00 | 3.29 | NÃO | fora do lado solicitado |
| 489 | 212.00 | 376.00 | 255.00 | 3.29 | NÃO | fora do lado solicitado |
| 490 | 213.00 | 376.00 | 254.00 | 3.29 | NÃO | fora do lado solicitado |
| 491 | 214.00 | 376.00 | 253.00 | 3.29 | NÃO | fora do lado solicitado |
| 492 | 215.00 | 376.00 | 252.00 | 3.29 | NÃO | fora do lado solicitado |
| 493 | 216.00 | 376.00 | 251.00 | 3.29 | NÃO | fora do lado solicitado |
| 494 | 217.00 | 376.00 | 250.00 | 3.29 | NÃO | fora do lado solicitado |
| 495 | 218.00 | 376.00 | 249.00 | 3.29 | NÃO | fora do lado solicitado |
| 496 | 219.00 | 376.00 | 248.00 | 3.29 | NÃO | fora do lado solicitado |
| 497 | 220.00 | 376.00 | 247.00 | 3.29 | NÃO | fora do lado solicitado |
| 498 | 221.00 | 376.00 | 246.00 | 3.29 | NÃO | fora do lado solicitado |
| 499 | 222.00 | 376.00 | 245.00 | 3.29 | NÃO | fora do lado solicitado |
| 500 | 223.00 | 376.00 | 244.00 | 3.29 | NÃO | fora do lado solicitado |
| 501 | 224.00 | 376.00 | 243.00 | 3.29 | NÃO | fora do lado solicitado |
| 502 | 225.00 | 376.00 | 242.00 | 3.29 | NÃO | fora do lado solicitado |
| 503 | 226.00 | 376.00 | 241.00 | 3.29 | NÃO | fora do lado solicitado |
| 504 | 227.00 | 376.00 | 240.00 | 3.29 | NÃO | fora do lado solicitado |
| 505 | 228.00 | 376.00 | 239.00 | 3.29 | NÃO | fora do lado solicitado |
| 506 | 229.00 | 376.00 | 238.00 | 3.29 | NÃO | fora do lado solicitado |
| 507 | 230.00 | 376.00 | 237.00 | 3.29 | NÃO | fora do lado solicitado |
| 508 | 231.00 | 376.00 | 236.00 | 3.29 | NÃO | fora do lado solicitado |
| 509 | 232.00 | 376.00 | 235.00 | 3.29 | NÃO | fora do lado solicitado |
| 510 | 233.00 | 376.00 | 234.00 | 3.29 | NÃO | fora do lado solicitado |
| 511 | 234.00 | 376.00 | 233.00 | 3.29 | NÃO | fora do lado solicitado |
| 512 | 235.00 | 376.00 | 232.00 | 3.29 | NÃO | fora do lado solicitado |
| 513 | 236.00 | 376.00 | 231.00 | 3.29 | NÃO | fora do lado solicitado |
| 514 | 237.00 | 376.00 | 230.00 | 3.29 | NÃO | fora do lado solicitado |
| 515 | 238.00 | 376.00 | 229.00 | 3.29 | NÃO | fora do lado solicitado |
| 516 | 239.00 | 376.00 | 228.00 | 3.29 | NÃO | fora do lado solicitado |
| 517 | 240.00 | 376.00 | 227.00 | 3.29 | NÃO | fora do lado solicitado |
| 518 | 241.00 | 376.00 | 226.00 | 3.29 | NÃO | fora do lado solicitado |
| 519 | 242.00 | 376.00 | 225.00 | 3.29 | NÃO | fora do lado solicitado |
| 520 | 243.00 | 376.00 | 224.00 | 3.29 | NÃO | fora do lado solicitado |
| 521 | 244.00 | 376.00 | 223.00 | 3.29 | NÃO | fora do lado solicitado |
| 522 | 245.00 | 376.00 | 222.00 | 3.29 | NÃO | fora do lado solicitado |
| 523 | 246.00 | 376.00 | 221.00 | 3.29 | NÃO | fora do lado solicitado |
| 524 | 247.00 | 376.00 | 220.00 | 3.29 | NÃO | fora do lado solicitado |
| 525 | 248.00 | 376.00 | 219.00 | 3.29 | NÃO | fora do lado solicitado |
| 526 | 249.00 | 376.00 | 218.00 | 3.29 | NÃO | fora do lado solicitado |
| 527 | 250.00 | 376.00 | 217.00 | 3.29 | NÃO | fora do lado solicitado |
| 528 | 251.00 | 376.00 | 216.00 | 3.29 | NÃO | fora do lado solicitado |
| 529 | 252.00 | 376.00 | 215.00 | 3.29 | NÃO | fora do lado solicitado |
| 530 | 253.00 | 376.00 | 214.00 | 3.29 | NÃO | fora do lado solicitado |
| 531 | 254.00 | 376.00 | 213.00 | 3.29 | NÃO | fora do lado solicitado |
| 532 | 255.00 | 376.00 | 212.00 | 3.29 | NÃO | fora do lado solicitado |
| 533 | 256.00 | 376.00 | 211.00 | 3.29 | NÃO | fora do lado solicitado |
| 534 | 257.00 | 376.00 | 210.00 | 3.29 | NÃO | fora do lado solicitado |
| 535 | 258.00 | 376.00 | 209.00 | 3.29 | NÃO | fora do lado solicitado |
| 536 | 259.00 | 376.00 | 208.00 | 3.29 | NÃO | fora do lado solicitado |
| 537 | 260.00 | 376.00 | 207.00 | 3.29 | NÃO | fora do lado solicitado |
| 538 | 261.00 | 376.00 | 206.00 | 3.29 | NÃO | fora do lado solicitado |
| 539 | 262.00 | 376.00 | 205.00 | 3.29 | NÃO | fora do lado solicitado |
| 540 | 263.00 | 376.00 | 204.00 | 3.29 | NÃO | fora do lado solicitado |
| 541 | 264.00 | 376.00 | 203.00 | 3.29 | NÃO | fora do lado solicitado |
| 542 | 265.00 | 376.00 | 202.00 | 3.29 | NÃO | fora do lado solicitado |
| 543 | 266.00 | 376.00 | 201.00 | 3.29 | NÃO | fora do lado solicitado |
| 544 | 267.00 | 376.00 | 200.00 | 3.29 | NÃO | fora do lado solicitado |
| 545 | 268.00 | 376.00 | 199.00 | 3.29 | NÃO | fora do lado solicitado |
| 546 | 269.00 | 376.00 | 198.00 | 3.29 | NÃO | fora do lado solicitado |
| 547 | 270.00 | 376.00 | 197.00 | 3.29 | NÃO | fora do lado solicitado |
| 548 | 271.00 | 376.00 | 196.00 | 3.29 | NÃO | fora do lado solicitado |
| 549 | 272.00 | 376.00 | 195.00 | 3.29 | NÃO | fora do lado solicitado |
| 550 | 273.00 | 376.00 | 194.00 | 3.29 | NÃO | fora do lado solicitado |
| 551 | 274.00 | 376.00 | 193.00 | 3.29 | NÃO | fora do lado solicitado |
| 552 | 275.00 | 376.00 | 192.00 | 3.29 | NÃO | fora do lado solicitado |
| 553 | 276.00 | 376.00 | 191.00 | 3.29 | NÃO | fora do lado solicitado |
| 554 | 277.00 | 376.00 | 190.00 | 3.29 | NÃO | fora do lado solicitado |
| 555 | 278.00 | 376.00 | 189.00 | 3.29 | NÃO | fora do lado solicitado |
| 556 | 279.00 | 376.00 | 188.00 | 3.29 | NÃO | fora do lado solicitado |
| 557 | 280.00 | 376.00 | 187.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 558 | 281.00 | 376.00 | 186.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 559 | 282.00 | 376.00 | 185.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 560 | 283.00 | 376.00 | 184.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 561 | 284.00 | 376.00 | 183.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 562 | 285.00 | 376.00 | 182.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 563 | 286.00 | 376.00 | 181.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 564 | 287.00 | 376.00 | 180.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 565 | 288.00 | 376.00 | 179.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 566 | 289.00 | 376.00 | 178.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 567 | 290.00 | 376.00 | 177.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 568 | 291.00 | 376.00 | 176.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 569 | 292.00 | 376.00 | 175.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 570 | 293.00 | 376.00 | 174.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 571 | 294.00 | 376.00 | 173.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 572 | 295.00 | 376.00 | 172.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 573 | 296.00 | 376.00 | 171.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 574 | 297.00 | 376.00 | 170.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 575 | 298.00 | 376.00 | 169.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 576 | 299.00 | 376.00 | 168.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 577 | 300.00 | 376.00 | 167.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 578 | 301.00 | 376.00 | 166.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 579 | 302.00 | 376.00 | 165.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 580 | 303.00 | 376.00 | 164.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 581 | 304.00 | 376.00 | 163.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 582 | 305.00 | 376.00 | 162.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 583 | 306.00 | 376.00 | 161.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 584 | 307.00 | 376.00 | 160.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 585 | 308.00 | 376.00 | 159.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 586 | 309.00 | 376.00 | 158.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 587 | 310.00 | 376.00 | 157.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 588 | 311.00 | 376.00 | 156.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 589 | 312.00 | 376.00 | 155.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 590 | 313.00 | 376.00 | 154.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 591 | 314.00 | 376.00 | 153.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 592 | 315.00 | 376.00 | 152.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 593 | 316.00 | 376.00 | 151.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 594 | 317.00 | 376.00 | 150.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 595 | 318.00 | 376.00 | 149.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 596 | 319.00 | 376.00 | 148.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 597 | 320.00 | 376.00 | 147.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 598 | 321.00 | 376.00 | 146.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 599 | 322.00 | 376.00 | 145.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 600 | 323.00 | 376.00 | 144.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 601 | 324.00 | 376.00 | 143.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 602 | 325.00 | 376.00 | 142.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 603 | 326.00 | 376.00 | 141.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 604 | 327.00 | 376.00 | 140.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 605 | 328.00 | 376.00 | 139.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 606 | 329.00 | 376.00 | 138.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 607 | 330.00 | 376.00 | 137.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 608 | 331.00 | 376.00 | 136.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 609 | 332.00 | 376.00 | 135.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 610 | 333.00 | 376.00 | 134.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 611 | 334.00 | 376.00 | 133.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 612 | 335.00 | 376.00 | 132.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 613 | 336.00 | 376.00 | 131.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 614 | 337.00 | 376.00 | 130.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 615 | 338.00 | 376.00 | 129.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 616 | 339.00 | 376.00 | 128.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 617 | 340.00 | 376.00 | 127.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 618 | 341.00 | 376.00 | 126.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 619 | 342.00 | 376.00 | 125.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 620 | 343.00 | 376.00 | 124.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 621 | 344.00 | 376.00 | 123.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 622 | 345.00 | 376.00 | 122.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 623 | 346.00 | 376.00 | 121.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 624 | 347.00 | 376.00 | 120.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 625 | 348.00 | 376.00 | 119.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 626 | 349.00 | 376.00 | 118.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 627 | 350.00 | 376.00 | 117.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 628 | 351.00 | 376.00 | 116.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 629 | 352.00 | 376.00 | 115.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 630 | 353.00 | 376.00 | 114.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 631 | 354.00 | 376.00 | 113.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 632 | 355.00 | 376.00 | 112.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 633 | 356.00 | 376.00 | 111.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 634 | 357.00 | 376.00 | 110.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 635 | 358.00 | 376.00 | 109.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 636 | 359.00 | 376.00 | 108.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 637 | 360.00 | 376.00 | 107.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 638 | 361.00 | 376.00 | 106.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 639 | 362.00 | 376.00 | 105.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 640 | 363.00 | 376.00 | 104.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 641 | 364.00 | 376.00 | 103.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 642 | 365.00 | 376.00 | 102.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 643 | 366.00 | 376.00 | 101.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 644 | 367.00 | 376.00 | 100.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 645 | 368.00 | 376.00 | 99.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 646 | 369.00 | 376.00 | 98.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 647 | 370.00 | 376.00 | 97.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 648 | 371.00 | 376.00 | 96.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 649 | 372.00 | 376.00 | 95.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 650 | 373.00 | 376.00 | 94.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 651 | 374.00 | 376.00 | 93.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 652 | 375.00 | 376.00 | 92.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 653 | 376.00 | 376.00 | 91.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 654 | 377.00 | 376.00 | 90.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 655 | 378.00 | 376.00 | 89.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 656 | 379.00 | 376.00 | 88.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 657 | 380.00 | 376.00 | 87.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 658 | 381.00 | 376.00 | 86.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 659 | 382.00 | 376.00 | 85.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 660 | 383.00 | 376.00 | 84.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 661 | 384.00 | 376.00 | 83.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 662 | 385.00 | 376.00 | 82.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 663 | 386.00 | 376.00 | 81.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 664 | 387.00 | 376.00 | 80.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 665 | 388.00 | 376.00 | 79.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 666 | 389.00 | 376.00 | 78.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 667 | 390.00 | 376.00 | 77.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 668 | 391.00 | 376.00 | 76.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 669 | 392.00 | 376.00 | 75.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 670 | 393.00 | 376.00 | 74.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 671 | 394.00 | 376.00 | 73.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 672 | 395.00 | 376.00 | 72.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 673 | 396.00 | 376.00 | 71.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 674 | 397.00 | 376.00 | 70.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 675 | 398.00 | 376.00 | 69.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 676 | 399.00 | 376.00 | 68.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 677 | 400.00 | 376.00 | 67.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 678 | 401.00 | 376.00 | 66.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 679 | 402.00 | 376.00 | 65.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 680 | 403.00 | 376.00 | 64.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 681 | 404.00 | 376.00 | 63.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 682 | 405.00 | 376.00 | 62.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 683 | 406.00 | 376.00 | 61.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 684 | 407.00 | 376.00 | 60.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 685 | 408.00 | 376.00 | 59.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 686 | 409.00 | 376.00 | 58.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 687 | 410.00 | 376.00 | 57.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 688 | 411.00 | 376.00 | 56.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 689 | 412.00 | 376.00 | 55.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 690 | 413.00 | 376.00 | 54.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 691 | 414.00 | 376.00 | 53.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 692 | 415.00 | 376.00 | 52.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 693 | 416.00 | 376.00 | 51.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 694 | 417.00 | 376.00 | 50.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 695 | 418.00 | 376.00 | 49.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 696 | 419.00 | 376.00 | 48.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 697 | 420.00 | 376.00 | 47.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 698 | 421.00 | 376.00 | 46.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 699 | 422.00 | 376.00 | 45.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 700 | 423.00 | 376.00 | 44.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 701 | 424.00 | 376.00 | 43.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 702 | 425.00 | 376.00 | 42.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 703 | 426.00 | 376.00 | 41.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 704 | 427.00 | 376.00 | 40.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 705 | 428.00 | 376.00 | 39.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 706 | 429.00 | 376.00 | 38.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 707 | 430.00 | 376.00 | 37.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 708 | 431.00 | 376.00 | 36.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 709 | 432.00 | 376.00 | 35.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 710 | 433.00 | 376.00 | 34.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 711 | 434.00 | 376.00 | 33.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 712 | 435.00 | 376.00 | 32.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 713 | 436.00 | 376.00 | 31.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 714 | 437.00 | 376.00 | 30.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 715 | 438.00 | 376.00 | 29.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 716 | 439.00 | 376.00 | 28.00 | 3.29 | SIM | dentro da janela vertical e do lado solicitado |
| 717 | 439.00 | 375.00 | 28.02 | 4.29 | SIM | dentro da janela vertical e do lado solicitado |
| 718 | 440.00 | 374.00 | 27.07 | 5.29 | SIM | dentro da janela vertical e do lado solicitado |
| 719 | 440.00 | 373.00 | 27.17 | 6.29 | SIM | dentro da janela vertical e do lado solicitado |
| 720 | 441.00 | 372.00 | 26.31 | 7.29 | SIM | dentro da janela vertical e do lado solicitado |
| 721 | 442.00 | 371.00 | 25.50 | 8.29 | SIM | dentro da janela vertical e do lado solicitado |
| 722 | 443.00 | 370.00 | 24.74 | 9.29 | SIM | dentro da janela vertical e do lado solicitado |
| 723 | 443.00 | 369.00 | 25.00 | 10.29 | SIM | dentro da janela vertical e do lado solicitado |
| 724 | 444.00 | 368.00 | 24.35 | 11.29 | SIM | dentro da janela vertical e do lado solicitado |
| 725 | 445.00 | 367.00 | 23.77 | 12.29 | SIM | dentro da janela vertical e do lado solicitado |
| 726 | 446.00 | 366.00 | 23.26 | 13.29 | SIM | dentro da janela vertical e do lado solicitado |
| 727 | 446.00 | 365.00 | 23.71 | 14.29 | SIM | dentro da janela vertical e do lado solicitado |
| 728 | 447.00 | 364.00 | 23.32 | 15.29 | SIM | dentro da janela vertical e do lado solicitado |
| 729 | 448.00 | 363.00 | 23.02 | 16.29 | SIM | dentro da janela vertical e do lado solicitado |
| 730 | 448.00 | 362.00 | 23.60 | 17.29 | SIM | dentro da janela vertical e do lado solicitado |
| 731 | 449.00 | 361.00 | 23.43 | 18.29 | SIM | dentro da janela vertical e do lado solicitado |
| 732 | 450.00 | 360.00 | 23.35 | 19.29 | SIM | dentro da janela vertical e do lado solicitado |
| 733 | 450.00 | 359.00 | 24.04 | 20.29 | SIM | dentro da janela vertical e do lado solicitado |
| 734 | 451.00 | 358.00 | 24.08 | 21.29 | SIM | dentro da janela vertical e do lado solicitado |
| 735 | 451.00 | 357.00 | 24.84 | 22.29 | SIM | dentro da janela vertical e do lado solicitado |
| 736 | 452.00 | 356.00 | 25.00 | 23.29 | SIM | dentro da janela vertical e do lado solicitado |
| 737 | 453.00 | 355.00 | 25.24 | 24.29 | SIM | dentro da janela vertical e do lado solicitado |
| 738 | 453.00 | 354.00 | 26.08 | 25.29 | SIM | dentro da janela vertical e do lado solicitado |
| 739 | 454.00 | 353.00 | 26.42 | 26.29 | SIM | dentro da janela vertical e do lado solicitado |
| 740 | 454.00 | 352.00 | 27.29 | 27.29 | SIM | dentro da janela vertical e do lado solicitado |
| 741 | 455.00 | 351.00 | 27.73 | 28.29 | SIM | dentro da janela vertical e do lado solicitado |
| 742 | 456.00 | 350.00 | 28.23 | 29.29 | SIM | dentro da janela vertical e do lado solicitado |
| 743 | 456.00 | 349.00 | 29.15 | 30.29 | SIM | dentro da janela vertical e do lado solicitado |
| 744 | 457.00 | 348.00 | 29.73 | 31.29 | SIM | dentro da janela vertical e do lado solicitado |
| 745 | 457.00 | 347.00 | 30.68 | 32.29 | SIM | dentro da janela vertical e do lado solicitado |
| 746 | 458.00 | 346.00 | 31.32 | 33.29 | SIM | dentro da janela vertical e do lado solicitado |
| 747 | 458.00 | 345.00 | 32.28 | 34.29 | SIM | dentro da janela vertical e do lado solicitado |
| 748 | 459.00 | 344.00 | 32.98 | 35.29 | SIM | dentro da janela vertical e do lado solicitado |
| 749 | 459.00 | 343.00 | 33.96 | 36.29 | SIM | dentro da janela vertical e do lado solicitado |
| 750 | 460.00 | 342.00 | 34.71 | 37.29 | SIM | dentro da janela vertical e do lado solicitado |
| 751 | 460.00 | 341.00 | 35.69 | 38.29 | SIM | dentro da janela vertical e do lado solicitado |
| 752 | 461.00 | 340.00 | 36.50 | 39.29 | SIM | dentro da janela vertical e do lado solicitado |
| 753 | 461.00 | 339.00 | 37.48 | 40.29 | SIM | dentro da janela vertical e do lado solicitado |
| 754 | 462.00 | 338.00 | 38.33 | 41.29 | SIM | dentro da janela vertical e do lado solicitado |
| 755 | 462.00 | 337.00 | 39.32 | 42.29 | SIM | dentro da janela vertical e do lado solicitado |
| 756 | 463.00 | 336.00 | 40.20 | 43.29 | SIM | dentro da janela vertical e do lado solicitado |
| 757 | 463.00 | 335.00 | 41.19 | 44.29 | SIM | dentro da janela vertical e do lado solicitado |
| 758 | 464.00 | 334.00 | 42.11 | 45.29 | SIM | dentro da janela vertical e do lado solicitado |
| 759 | 464.00 | 333.00 | 43.10 | 46.29 | SIM | dentro da janela vertical e do lado solicitado |
| 760 | 465.00 | 332.00 | 44.05 | 47.29 | SIM | dentro da janela vertical e do lado solicitado |
| 761 | 465.00 | 331.00 | 45.04 | 48.29 | SIM | dentro da janela vertical e do lado solicitado |
| 762 | 466.00 | 330.00 | 46.01 | 49.29 | SIM | dentro da janela vertical e do lado solicitado |
| 763 | 466.00 | 329.00 | 47.01 | 50.29 | SIM | dentro da janela vertical e do lado solicitado |
| 764 | 467.00 | 328.00 | 48.00 | 51.29 | SIM | dentro da janela vertical e do lado solicitado |
| 765 | 467.00 | 327.00 | 49.00 | 52.29 | SIM | dentro da janela vertical e do lado solicitado |
| 766 | 468.00 | 326.00 | 50.01 | 53.29 | SIM | dentro da janela vertical e do lado solicitado |
| 767 | 468.00 | 325.00 | 51.01 | 54.29 | SIM | dentro da janela vertical e do lado solicitado |
| 768 | 468.00 | 324.00 | 52.01 | 55.29 | SIM | dentro da janela vertical e do lado solicitado |
| 769 | 469.00 | 323.00 | 53.04 | 56.29 | SIM | dentro da janela vertical e do lado solicitado |
| 770 | 469.00 | 322.00 | 54.04 | 57.29 | SIM | dentro da janela vertical e do lado solicitado |
| 771 | 469.00 | 321.00 | 55.04 | 58.29 | SIM | dentro da janela vertical e do lado solicitado |
| 772 | 470.00 | 320.00 | 56.08 | 59.29 | SIM | dentro da janela vertical e do lado solicitado |
| 773 | 470.00 | 319.00 | 57.08 | 60.29 | SIM | dentro da janela vertical e do lado solicitado |
| 774 | 471.00 | 318.00 | 58.14 | 61.29 | SIM | dentro da janela vertical e do lado solicitado |
| 775 | 471.00 | 317.00 | 59.14 | 62.29 | SIM | dentro da janela vertical e do lado solicitado |
| 776 | 471.00 | 316.00 | 60.13 | 63.29 | SIM | dentro da janela vertical e do lado solicitado |
| 777 | 472.00 | 315.00 | 61.20 | 64.29 | SIM | dentro da janela vertical e do lado solicitado |
| 778 | 472.00 | 314.00 | 62.20 | 65.29 | SIM | dentro da janela vertical e do lado solicitado |
| 779 | 472.00 | 313.00 | 63.20 | 66.29 | SIM | dentro da janela vertical e do lado solicitado |
| 780 | 473.00 | 312.00 | 64.28 | 67.29 | SIM | dentro da janela vertical e do lado solicitado |
| 781 | 473.00 | 311.00 | 65.28 | 68.29 | SIM | dentro da janela vertical e do lado solicitado |
| 782 | 473.00 | 310.00 | 66.27 | 69.29 | SIM | dentro da janela vertical e do lado solicitado |
| 783 | 473.00 | 309.00 | 67.27 | 70.29 | SIM | dentro da janela vertical e do lado solicitado |
| 784 | 474.00 | 308.00 | 68.36 | 71.29 | SIM | dentro da janela vertical e do lado solicitado |
| 785 | 474.00 | 307.00 | 69.35 | 72.29 | SIM | dentro da janela vertical e do lado solicitado |
| 786 | 474.00 | 306.00 | 70.35 | 73.29 | SIM | dentro da janela vertical e do lado solicitado |
| 787 | 475.00 | 305.00 | 71.45 | 74.29 | SIM | dentro da janela vertical e do lado solicitado |
| 788 | 475.00 | 304.00 | 72.44 | 75.29 | SIM | dentro da janela vertical e do lado solicitado |
| 789 | 475.00 | 303.00 | 73.44 | 76.29 | SIM | dentro da janela vertical e do lado solicitado |
| 790 | 475.00 | 302.00 | 74.43 | 77.29 | SIM | dentro da janela vertical e do lado solicitado |
| 791 | 476.00 | 301.00 | 75.54 | 78.29 | SIM | dentro da janela vertical e do lado solicitado |
| 792 | 476.00 | 300.00 | 76.53 | 79.29 | SIM | dentro da janela vertical e do lado solicitado |
| 793 | 476.00 | 299.00 | 77.52 | 80.29 | SIM | dentro da janela vertical e do lado solicitado |
| 794 | 476.00 | 298.00 | 78.52 | 81.29 | SIM | dentro da janela vertical e do lado solicitado |
| 795 | 477.00 | 297.00 | 79.63 | 82.29 | SIM | dentro da janela vertical e do lado solicitado |
| 796 | 477.00 | 296.00 | 80.62 | 83.29 | SIM | dentro da janela vertical e do lado solicitado |
| 797 | 477.00 | 295.00 | 81.61 | 84.29 | SIM | dentro da janela vertical e do lado solicitado |
| 798 | 477.00 | 294.00 | 82.61 | 85.29 | SIM | dentro da janela vertical e do lado solicitado |
| 799 | 478.00 | 293.00 | 83.73 | 86.29 | SIM | dentro da janela vertical e do lado solicitado |
| 800 | 478.00 | 292.00 | 84.72 | 87.29 | SIM | dentro da janela vertical e do lado solicitado |
| 801 | 478.00 | 291.00 | 85.71 | 88.29 | SIM | dentro da janela vertical e do lado solicitado |
| 802 | 478.00 | 290.00 | 86.70 | 89.29 | SIM | dentro da janela vertical e do lado solicitado |
| 803 | 478.00 | 289.00 | 87.69 | 90.29 | SIM | dentro da janela vertical e do lado solicitado |
| 804 | 479.00 | 288.00 | 88.81 | 91.29 | SIM | dentro da janela vertical e do lado solicitado |
| 805 | 479.00 | 287.00 | 89.81 | 92.29 | SIM | dentro da janela vertical e do lado solicitado |
| 806 | 479.00 | 286.00 | 90.80 | 93.29 | SIM | dentro da janela vertical e do lado solicitado |
| 807 | 479.00 | 285.00 | 91.79 | 94.29 | SIM | dentro da janela vertical e do lado solicitado |
| 808 | 479.00 | 284.00 | 92.78 | 95.29 | SIM | dentro da janela vertical e do lado solicitado |
| 809 | 480.00 | 283.00 | 93.90 | 96.29 | SIM | dentro da janela vertical e do lado solicitado |
| 810 | 480.00 | 282.00 | 94.89 | 97.29 | SIM | dentro da janela vertical e do lado solicitado |
| 811 | 480.00 | 281.00 | 95.89 | 98.29 | SIM | dentro da janela vertical e do lado solicitado |
| 812 | 480.00 | 280.00 | 96.88 | 99.29 | SIM | dentro da janela vertical e do lado solicitado |
| 813 | 480.00 | 279.00 | 97.87 | 100.29 | SIM | dentro da janela vertical e do lado solicitado |
| 814 | 480.00 | 278.00 | 98.86 | 101.29 | SIM | dentro da janela vertical e do lado solicitado |
| 815 | 480.00 | 277.00 | 99.85 | 102.29 | SIM | dentro da janela vertical e do lado solicitado |
| 816 | 481.00 | 276.00 | 100.98 | 103.29 | SIM | dentro da janela vertical e do lado solicitado |
| 817 | 481.00 | 275.00 | 101.97 | 104.29 | SIM | dentro da janela vertical e do lado solicitado |
| 818 | 481.00 | 274.00 | 102.96 | 105.29 | SIM | dentro da janela vertical e do lado solicitado |
| 819 | 481.00 | 273.00 | 103.95 | 106.29 | SIM | dentro da janela vertical e do lado solicitado |
| 820 | 481.00 | 272.00 | 104.94 | 107.29 | SIM | dentro da janela vertical e do lado solicitado |
| 821 | 481.00 | 271.00 | 105.93 | 108.29 | SIM | dentro da janela vertical e do lado solicitado |
| 822 | 481.00 | 270.00 | 106.92 | 109.29 | SIM | dentro da janela vertical e do lado solicitado |
| 823 | 481.00 | 269.00 | 107.91 | 110.29 | SIM | dentro da janela vertical e do lado solicitado |
| 824 | 482.00 | 268.00 | 109.04 | 111.29 | SIM | dentro da janela vertical e do lado solicitado |
| 825 | 482.00 | 267.00 | 110.03 | 112.29 | SIM | dentro da janela vertical e do lado solicitado |
| 826 | 482.00 | 266.00 | 111.02 | 113.29 | SIM | dentro da janela vertical e do lado solicitado |
| 827 | 482.00 | 265.00 | 112.01 | 114.29 | SIM | dentro da janela vertical e do lado solicitado |
| 828 | 482.00 | 264.00 | 113.00 | 115.29 | SIM | dentro da janela vertical e do lado solicitado |
| 829 | 482.00 | 263.00 | 113.99 | 116.29 | SIM | dentro da janela vertical e do lado solicitado |
| 830 | 482.00 | 262.00 | 114.98 | 117.29 | SIM | dentro da janela vertical e do lado solicitado |
| 831 | 482.00 | 261.00 | 115.97 | 118.29 | SIM | dentro da janela vertical e do lado solicitado |
| 832 | 482.00 | 260.00 | 116.97 | 119.29 | SIM | dentro da janela vertical e do lado solicitado |
| 833 | 482.00 | 259.00 | 117.96 | 120.29 | SIM | dentro da janela vertical e do lado solicitado |
| 834 | 482.00 | 258.00 | 118.95 | 121.29 | SIM | dentro da janela vertical e do lado solicitado |
| 835 | 482.00 | 257.00 | 119.94 | 122.29 | SIM | dentro da janela vertical e do lado solicitado |
| 836 | 482.00 | 256.00 | 120.93 | 123.29 | SIM | dentro da janela vertical e do lado solicitado |
| 837 | 482.00 | 255.00 | 121.93 | 124.29 | SIM | dentro da janela vertical e do lado solicitado |
| 838 | 482.00 | 254.00 | 122.92 | 125.29 | SIM | dentro da janela vertical e do lado solicitado |
| 839 | 482.00 | 253.00 | 123.91 | 126.29 | SIM | dentro da janela vertical e do lado solicitado |
| 840 | 482.00 | 252.00 | 124.90 | 127.29 | SIM | dentro da janela vertical e do lado solicitado |
| 841 | 482.00 | 251.00 | 125.90 | 128.29 | SIM | dentro da janela vertical e do lado solicitado |
| 842 | 482.00 | 250.00 | 126.89 | 129.29 | SIM | dentro da janela vertical e do lado solicitado |
| 843 | 482.00 | 249.00 | 127.88 | 130.29 | SIM | dentro da janela vertical e do lado solicitado |
| 844 | 482.00 | 248.00 | 128.88 | 131.29 | SIM | dentro da janela vertical e do lado solicitado |
| 845 | 482.00 | 247.00 | 129.87 | 132.29 | SIM | dentro da janela vertical e do lado solicitado |
| 846 | 482.00 | 246.00 | 130.86 | 133.29 | SIM | dentro da janela vertical e do lado solicitado |
| 847 | 482.00 | 245.00 | 131.86 | 134.29 | SIM | dentro da janela vertical e do lado solicitado |
| 848 | 482.00 | 244.00 | 132.85 | 135.29 | SIM | dentro da janela vertical e do lado solicitado |
| 849 | 482.00 | 243.00 | 133.84 | 136.29 | SIM | dentro da janela vertical e do lado solicitado |
| 850 | 482.00 | 242.00 | 134.84 | 137.29 | SIM | dentro da janela vertical e do lado solicitado |
| 851 | 482.00 | 241.00 | 135.83 | 138.29 | SIM | dentro da janela vertical e do lado solicitado |
| 852 | 482.00 | 240.00 | 136.82 | 139.29 | SIM | dentro da janela vertical e do lado solicitado |
| 853 | 482.00 | 239.00 | 137.82 | 140.29 | SIM | dentro da janela vertical e do lado solicitado |
| 854 | 482.00 | 238.00 | 138.81 | 141.29 | SIM | dentro da janela vertical e do lado solicitado |
| 855 | 482.00 | 237.00 | 139.81 | 142.29 | SIM | dentro da janela vertical e do lado solicitado |
| 856 | 482.00 | 236.00 | 140.80 | 143.29 | SIM | dentro da janela vertical e do lado solicitado |
| 857 | 482.00 | 235.00 | 141.80 | 144.29 | SIM | dentro da janela vertical e do lado solicitado |
| 858 | 482.00 | 234.00 | 142.79 | 145.29 | SIM | dentro da janela vertical e do lado solicitado |
| 859 | 482.00 | 233.00 | 143.78 | 146.29 | SIM | dentro da janela vertical e do lado solicitado |
| 860 | 482.00 | 232.00 | 144.78 | 147.29 | SIM | dentro da janela vertical e do lado solicitado |
| 861 | 481.00 | 231.00 | 145.67 | 148.29 | SIM | dentro da janela vertical e do lado solicitado |
| 862 | 481.00 | 230.00 | 146.67 | 149.29 | SIM | dentro da janela vertical e do lado solicitado |
| 863 | 481.00 | 229.00 | 147.67 | 150.29 | SIM | dentro da janela vertical e do lado solicitado |
| 864 | 481.00 | 228.00 | 148.66 | 151.29 | SIM | dentro da janela vertical e do lado solicitado |
| 865 | 481.00 | 227.00 | 149.66 | 152.29 | SIM | dentro da janela vertical e do lado solicitado |
| 866 | 481.00 | 226.00 | 150.65 | 153.29 | SIM | dentro da janela vertical e do lado solicitado |
| 867 | 481.00 | 225.00 | 151.65 | 154.29 | SIM | dentro da janela vertical e do lado solicitado |
| 868 | 481.00 | 224.00 | 152.64 | 155.29 | SIM | dentro da janela vertical e do lado solicitado |
| 869 | 480.00 | 223.00 | 153.55 | 156.29 | SIM | dentro da janela vertical e do lado solicitado |
| 870 | 480.00 | 222.00 | 154.55 | 157.29 | SIM | dentro da janela vertical e do lado solicitado |
| 871 | 480.00 | 221.00 | 155.54 | 158.29 | SIM | dentro da janela vertical e do lado solicitado |
| 872 | 480.00 | 220.00 | 156.54 | 159.29 | SIM | dentro da janela vertical e do lado solicitado |
| 873 | 480.00 | 219.00 | 157.54 | 160.29 | SIM | dentro da janela vertical e do lado solicitado |
| 874 | 480.00 | 218.00 | 158.53 | 161.29 | SIM | dentro da janela vertical e do lado solicitado |
| 875 | 480.00 | 217.00 | 159.53 | 162.29 | SIM | dentro da janela vertical e do lado solicitado |
| 876 | 480.00 | 216.00 | 160.53 | 163.29 | SIM | dentro da janela vertical e do lado solicitado |
| 877 | 479.00 | 215.00 | 161.45 | 164.29 | SIM | dentro da janela vertical e do lado solicitado |
| 878 | 479.00 | 214.00 | 162.44 | 165.29 | SIM | dentro da janela vertical e do lado solicitado |
| 879 | 479.00 | 213.00 | 163.44 | 166.29 | SIM | dentro da janela vertical e do lado solicitado |
| 880 | 479.00 | 212.00 | 164.44 | 167.29 | SIM | dentro da janela vertical e do lado solicitado |
| 881 | 479.00 | 211.00 | 165.44 | 168.29 | SIM | dentro da janela vertical e do lado solicitado |
| 882 | 478.00 | 210.00 | 166.36 | 169.29 | SIM | dentro da janela vertical e do lado solicitado |
| 883 | 478.00 | 209.00 | 167.36 | 170.29 | SIM | dentro da janela vertical e do lado solicitado |
| 884 | 478.00 | 208.00 | 168.36 | 171.29 | SIM | dentro da janela vertical e do lado solicitado |
| 885 | 478.00 | 207.00 | 169.36 | 172.29 | SIM | dentro da janela vertical e do lado solicitado |
| 886 | 477.00 | 206.00 | 170.29 | 173.29 | SIM | dentro da janela vertical e do lado solicitado |
| 887 | 477.00 | 205.00 | 171.29 | 174.29 | SIM | dentro da janela vertical e do lado solicitado |
| 888 | 477.00 | 204.00 | 172.29 | 175.29 | SIM | dentro da janela vertical e do lado solicitado |
| 889 | 477.00 | 203.00 | 173.29 | 176.29 | SIM | dentro da janela vertical e do lado solicitado |
| 890 | 477.00 | 202.00 | 174.29 | 177.29 | SIM | dentro da janela vertical e do lado solicitado |
| 891 | 476.00 | 201.00 | 175.23 | 178.29 | SIM | dentro da janela vertical e do lado solicitado |
| 892 | 476.00 | 200.00 | 176.23 | 179.29 | SIM | dentro da janela vertical e do lado solicitado |
| 893 | 476.00 | 199.00 | 177.23 | 180.29 | NÃO | fora da faixa vertical |
| 894 | 476.00 | 198.00 | 178.23 | 181.29 | NÃO | fora da faixa vertical |
| 895 | 475.00 | 197.00 | 179.18 | 182.29 | NÃO | fora da faixa vertical |
| 896 | 475.00 | 196.00 | 180.18 | 183.29 | NÃO | fora da faixa vertical |
| 897 | 475.00 | 195.00 | 181.18 | 184.29 | NÃO | fora da faixa vertical |
| 898 | 475.00 | 194.00 | 182.18 | 185.29 | NÃO | fora da faixa vertical |
| 899 | 474.00 | 193.00 | 183.13 | 186.29 | NÃO | fora da faixa vertical |
| 900 | 474.00 | 192.00 | 184.13 | 187.29 | NÃO | fora da faixa vertical |
| 901 | 474.00 | 191.00 | 185.13 | 188.29 | NÃO | fora da faixa vertical |
| 902 | 473.00 | 190.00 | 186.10 | 189.29 | NÃO | fora da faixa vertical |
| 903 | 473.00 | 189.00 | 187.10 | 190.29 | NÃO | fora da faixa vertical |
| 904 | 473.00 | 188.00 | 188.10 | 191.29 | NÃO | fora da faixa vertical |
| 905 | 473.00 | 187.00 | 189.10 | 192.29 | NÃO | fora da faixa vertical |
| 906 | 472.00 | 186.00 | 190.07 | 193.29 | NÃO | fora da faixa vertical |
| 907 | 472.00 | 185.00 | 191.07 | 194.29 | NÃO | fora da faixa vertical |
| 908 | 472.00 | 184.00 | 192.07 | 195.29 | NÃO | fora da faixa vertical |
| 909 | 471.00 | 183.00 | 193.04 | 196.29 | NÃO | fora da faixa vertical |
| 910 | 471.00 | 182.00 | 194.04 | 197.29 | NÃO | fora da faixa vertical |
| 911 | 470.00 | 181.00 | 195.02 | 198.29 | NÃO | fora da faixa vertical |
| 912 | 470.00 | 180.00 | 196.02 | 199.29 | NÃO | fora da faixa vertical |
| 913 | 470.00 | 179.00 | 197.02 | 200.29 | NÃO | fora da faixa vertical |
| 914 | 469.00 | 178.00 | 198.01 | 201.29 | NÃO | fora da faixa vertical |
| 915 | 469.00 | 177.00 | 199.01 | 202.29 | NÃO | fora da faixa vertical |
| 916 | 469.00 | 176.00 | 200.01 | 203.29 | NÃO | fora da faixa vertical |
| 917 | 468.00 | 175.00 | 201.00 | 204.29 | NÃO | fora da faixa vertical |
| 918 | 468.00 | 174.00 | 202.00 | 205.29 | NÃO | fora da faixa vertical |
| 919 | 467.00 | 173.00 | 203.00 | 206.29 | NÃO | fora da faixa vertical |
| 920 | 467.00 | 172.00 | 204.00 | 207.29 | NÃO | fora da faixa vertical |
| 921 | 467.00 | 171.00 | 205.00 | 208.29 | NÃO | fora da faixa vertical |
| 922 | 466.00 | 170.00 | 206.00 | 209.29 | NÃO | fora da faixa vertical |
| 923 | 466.00 | 169.00 | 207.00 | 210.29 | NÃO | fora da faixa vertical |
| 924 | 465.00 | 168.00 | 208.01 | 211.29 | NÃO | fora da faixa vertical |
| 925 | 465.00 | 167.00 | 209.01 | 212.29 | NÃO | fora da faixa vertical |
| 926 | 464.00 | 166.00 | 210.02 | 213.29 | NÃO | fora da faixa vertical |
| 927 | 464.00 | 165.00 | 211.02 | 214.29 | NÃO | fora da faixa vertical |
| 928 | 463.00 | 164.00 | 212.04 | 215.29 | NÃO | fora da faixa vertical |
| 929 | 463.00 | 163.00 | 213.04 | 216.29 | NÃO | fora da faixa vertical |
| 930 | 462.00 | 162.00 | 214.06 | 217.29 | NÃO | fora da faixa vertical |
| 931 | 462.00 | 161.00 | 215.06 | 218.29 | NÃO | fora da faixa vertical |
| 932 | 461.00 | 160.00 | 216.08 | 219.29 | NÃO | fora da faixa vertical |
| 933 | 461.00 | 159.00 | 217.08 | 220.29 | NÃO | fora da faixa vertical |
| 934 | 460.00 | 158.00 | 218.11 | 221.29 | NÃO | fora da faixa vertical |
| 935 | 460.00 | 157.00 | 219.11 | 222.29 | NÃO | fora da faixa vertical |
| 936 | 459.00 | 156.00 | 220.15 | 223.29 | NÃO | fora da faixa vertical |
| 937 | 459.00 | 155.00 | 221.14 | 224.29 | NÃO | fora da faixa vertical |
| 938 | 458.00 | 154.00 | 222.18 | 225.29 | NÃO | fora da faixa vertical |
| 939 | 458.00 | 153.00 | 223.18 | 226.29 | NÃO | fora da faixa vertical |
| 940 | 457.00 | 152.00 | 224.22 | 227.29 | NÃO | fora da faixa vertical |
| 941 | 457.00 | 151.00 | 225.22 | 228.29 | NÃO | fora da faixa vertical |
| 942 | 456.00 | 150.00 | 226.27 | 229.29 | NÃO | fora da faixa vertical |
| 943 | 455.00 | 149.00 | 227.32 | 230.29 | NÃO | fora da faixa vertical |
| 944 | 455.00 | 148.00 | 228.32 | 231.29 | NÃO | fora da faixa vertical |
| 945 | 454.00 | 147.00 | 229.37 | 232.29 | NÃO | fora da faixa vertical |
| 946 | 454.00 | 146.00 | 230.37 | 233.29 | NÃO | fora da faixa vertical |
| 947 | 453.00 | 145.00 | 231.42 | 234.29 | NÃO | fora da faixa vertical |
| 948 | 452.00 | 144.00 | 232.48 | 235.29 | NÃO | fora da faixa vertical |
| 949 | 452.00 | 143.00 | 233.48 | 236.29 | NÃO | fora da faixa vertical |
| 950 | 451.00 | 142.00 | 234.55 | 237.29 | NÃO | fora da faixa vertical |
| 951 | 451.00 | 141.00 | 235.54 | 238.29 | NÃO | fora da faixa vertical |
| 952 | 450.00 | 140.00 | 236.61 | 239.29 | NÃO | fora da faixa vertical |
| 953 | 449.00 | 139.00 | 237.68 | 240.29 | NÃO | fora da faixa vertical |
| 954 | 449.00 | 138.00 | 238.68 | 241.29 | NÃO | fora da faixa vertical |
| 955 | 448.00 | 137.00 | 239.75 | 242.29 | NÃO | fora da faixa vertical |
| 956 | 448.00 | 136.00 | 240.75 | 243.29 | NÃO | fora da faixa vertical |
| 957 | 447.00 | 135.00 | 241.83 | 244.29 | NÃO | fora da faixa vertical |
| 958 | 446.00 | 134.00 | 242.91 | 245.29 | NÃO | fora da faixa vertical |
| 959 | 445.00 | 133.00 | 243.99 | 246.29 | NÃO | fora da faixa vertical |
| 960 | 445.00 | 132.00 | 244.99 | 247.29 | NÃO | fora da faixa vertical |
| 961 | 444.00 | 131.00 | 246.08 | 248.29 | NÃO | fora da faixa vertical |
| 962 | 443.00 | 130.00 | 247.17 | 249.29 | NÃO | fora da faixa vertical |
| 963 | 442.00 | 129.00 | 248.26 | 250.29 | NÃO | fora da faixa vertical |
| 964 | 442.00 | 128.00 | 249.26 | 251.29 | NÃO | fora da faixa vertical |
| 965 | 441.00 | 127.00 | 250.35 | 252.29 | NÃO | fora da faixa vertical |
| 966 | 440.00 | 126.00 | 251.45 | 253.29 | NÃO | fora da faixa vertical |
| 967 | 439.00 | 125.00 | 252.56 | 254.29 | NÃO | fora da faixa vertical |
| 968 | 439.00 | 124.00 | 253.55 | 255.29 | NÃO | fora da faixa vertical |
| 969 | 438.00 | 123.00 | 254.66 | 256.29 | NÃO | fora da faixa vertical |
| 970 | 437.00 | 122.00 | 255.77 | 257.29 | NÃO | fora da faixa vertical |
| 971 | 436.00 | 121.00 | 256.88 | 258.29 | NÃO | fora da faixa vertical |
| 972 | 436.00 | 120.00 | 257.87 | 259.29 | NÃO | fora da faixa vertical |
| 973 | 435.00 | 119.00 | 258.98 | 260.29 | NÃO | fora da faixa vertical |
| 974 | 434.00 | 118.00 | 260.10 | 261.29 | NÃO | fora da faixa vertical |
| 975 | 433.00 | 117.00 | 261.22 | 262.29 | NÃO | fora da faixa vertical |
| 976 | 432.00 | 116.00 | 262.35 | 263.29 | NÃO | fora da faixa vertical |
| 977 | 431.00 | 115.00 | 263.47 | 264.29 | NÃO | fora da faixa vertical |
| 978 | 430.00 | 114.00 | 264.60 | 265.29 | NÃO | fora da faixa vertical |
| 979 | 429.00 | 113.00 | 265.73 | 266.29 | NÃO | fora da faixa vertical |
| 980 | 428.00 | 112.00 | 266.87 | 267.29 | NÃO | fora da faixa vertical |
| 981 | 427.00 | 111.00 | 268.00 | 268.29 | NÃO | fora da faixa vertical |
| 982 | 426.00 | 110.00 | 269.14 | 269.29 | NÃO | fora da faixa vertical |
| 983 | 425.00 | 109.00 | 270.28 | 270.29 | NÃO | fora da faixa vertical |
| 984 | 425.00 | 108.00 | 271.27 | 271.29 | NÃO | fora da faixa vertical |
| 985 | 424.00 | 107.00 | 272.42 | 272.29 | NÃO | fora da faixa vertical |
| 986 | 423.00 | 106.00 | 273.56 | 273.29 | NÃO | fora da faixa vertical |
| 987 | 422.00 | 105.00 | 274.71 | 274.29 | NÃO | fora da faixa vertical |
| 988 | 421.00 | 104.00 | 275.86 | 275.29 | NÃO | fora da faixa vertical |
| 989 | 420.00 | 103.00 | 277.02 | 276.29 | NÃO | fora da faixa vertical |
| 990 | 419.00 | 103.00 | 277.19 | 276.29 | NÃO | fora da faixa vertical |
| 991 | 418.00 | 102.00 | 278.35 | 277.29 | NÃO | fora da faixa vertical |
| 992 | 417.00 | 101.00 | 279.51 | 278.29 | NÃO | fora da faixa vertical |
| 993 | 416.00 | 100.00 | 280.67 | 279.29 | NÃO | fora da faixa vertical |
| 994 | 415.00 | 99.00 | 281.84 | 280.29 | NÃO | fora da faixa vertical |
| 995 | 414.00 | 98.00 | 283.01 | 281.29 | NÃO | fora da faixa vertical |
| 996 | 413.00 | 97.00 | 284.18 | 282.29 | NÃO | fora da faixa vertical |
| 997 | 412.00 | 96.00 | 285.35 | 283.29 | NÃO | fora da faixa vertical |
| 998 | 411.00 | 95.00 | 286.53 | 284.29 | NÃO | fora da faixa vertical |
| 999 | 410.00 | 94.00 | 287.70 | 285.29 | NÃO | fora da faixa vertical |
| 1000 | 409.00 | 94.00 | 287.90 | 285.29 | NÃO | fora da faixa vertical |
| 1001 | 408.00 | 93.00 | 289.08 | 286.29 | NÃO | fora da faixa vertical |
| 1002 | 407.00 | 92.00 | 290.27 | 287.29 | NÃO | fora da faixa vertical |
| 1003 | 406.00 | 91.00 | 291.45 | 288.29 | NÃO | fora da faixa vertical |
| 1004 | 405.00 | 90.00 | 292.64 | 289.29 | NÃO | fora da faixa vertical |
| 1005 | 404.00 | 90.00 | 292.86 | 289.29 | NÃO | fora da faixa vertical |
| 1006 | 403.00 | 89.00 | 294.05 | 290.29 | NÃO | fora da faixa vertical |
| 1007 | 402.00 | 88.00 | 295.24 | 291.29 | NÃO | fora da faixa vertical |
| 1008 | 401.00 | 87.00 | 296.44 | 292.29 | NÃO | fora da faixa vertical |
| 1009 | 400.00 | 87.00 | 296.66 | 292.29 | NÃO | fora da faixa vertical |
| 1010 | 399.00 | 86.00 | 297.87 | 293.29 | NÃO | fora da faixa vertical |
| 1011 | 398.00 | 85.00 | 299.07 | 294.29 | NÃO | fora da faixa vertical |
| 1012 | 397.00 | 84.00 | 300.27 | 295.29 | NÃO | fora da faixa vertical |
| 1013 | 396.00 | 84.00 | 300.51 | 295.29 | NÃO | fora da faixa vertical |
| 1014 | 395.00 | 83.00 | 301.72 | 296.29 | NÃO | fora da faixa vertical |
| 1015 | 394.00 | 82.00 | 302.93 | 297.29 | NÃO | fora da faixa vertical |
| 1016 | 393.00 | 82.00 | 303.17 | 297.29 | NÃO | fora da faixa vertical |
| 1017 | 392.00 | 81.00 | 304.38 | 298.29 | NÃO | fora da faixa vertical |
| 1018 | 391.00 | 80.00 | 305.60 | 299.29 | NÃO | fora da faixa vertical |
| 1019 | 390.00 | 80.00 | 305.85 | 299.29 | NÃO | fora da faixa vertical |
| 1020 | 389.00 | 79.00 | 307.07 | 300.29 | NÃO | fora da faixa vertical |
| 1021 | 388.00 | 78.00 | 308.29 | 301.29 | NÃO | fora da faixa vertical |
| 1022 | 387.00 | 78.00 | 308.55 | 301.29 | NÃO | fora da faixa vertical |
| 1023 | 386.00 | 77.00 | 309.78 | 302.29 | NÃO | fora da faixa vertical |
| 1024 | 385.00 | 77.00 | 310.04 | 302.29 | NÃO | fora da faixa vertical |
| 1025 | 384.00 | 76.00 | 311.27 | 303.29 | NÃO | fora da faixa vertical |
| 1026 | 383.00 | 75.00 | 312.50 | 304.29 | NÃO | fora da faixa vertical |
| 1027 | 382.00 | 75.00 | 312.77 | 304.29 | NÃO | fora da faixa vertical |
| 1028 | 381.00 | 74.00 | 314.01 | 305.29 | NÃO | fora da faixa vertical |
| 1029 | 380.00 | 73.00 | 315.24 | 306.29 | NÃO | fora da faixa vertical |
| 1030 | 379.00 | 73.00 | 315.52 | 306.29 | NÃO | fora da faixa vertical |
| 1031 | 378.00 | 72.00 | 316.76 | 307.29 | NÃO | fora da faixa vertical |
| 1032 | 377.00 | 72.00 | 317.04 | 307.29 | NÃO | fora da faixa vertical |
| 1033 | 376.00 | 71.00 | 318.29 | 308.29 | NÃO | fora da faixa vertical |
| 1034 | 375.00 | 71.00 | 318.57 | 308.29 | NÃO | fora da faixa vertical |
| 1035 | 374.00 | 70.00 | 319.82 | 309.29 | NÃO | fora da faixa vertical |
| 1036 | 373.00 | 70.00 | 320.11 | 309.29 | NÃO | fora da faixa vertical |
| 1037 | 372.00 | 69.00 | 321.36 | 310.29 | NÃO | fora da faixa vertical |
| 1038 | 371.00 | 69.00 | 321.66 | 310.29 | NÃO | fora da faixa vertical |
| 1039 | 370.00 | 68.00 | 322.91 | 311.29 | NÃO | fora da faixa vertical |
| 1040 | 369.00 | 68.00 | 323.22 | 311.29 | NÃO | fora da faixa vertical |
| 1041 | 368.00 | 67.00 | 324.47 | 312.29 | NÃO | fora da faixa vertical |
| 1042 | 367.00 | 67.00 | 324.78 | 312.29 | NÃO | fora da faixa vertical |
| 1043 | 366.00 | 66.00 | 326.04 | 313.29 | NÃO | fora da faixa vertical |
| 1044 | 365.00 | 66.00 | 326.35 | 313.29 | NÃO | fora da faixa vertical |
| 1045 | 364.00 | 65.00 | 327.61 | 314.29 | NÃO | fora da faixa vertical |
| 1046 | 363.00 | 65.00 | 327.93 | 314.29 | NÃO | fora da faixa vertical |
| 1047 | 362.00 | 64.00 | 329.19 | 315.29 | NÃO | fora da faixa vertical |
| 1048 | 361.00 | 64.00 | 329.51 | 315.29 | NÃO | fora da faixa vertical |
| 1049 | 360.00 | 63.00 | 330.78 | 316.29 | NÃO | fora da faixa vertical |
| 1050 | 359.00 | 63.00 | 331.11 | 316.29 | NÃO | fora da faixa vertical |
| 1051 | 358.00 | 62.00 | 332.38 | 317.29 | NÃO | fora da faixa vertical |
| 1052 | 357.00 | 62.00 | 332.71 | 317.29 | NÃO | fora da faixa vertical |
| 1053 | 356.00 | 62.00 | 333.04 | 317.29 | NÃO | fora da faixa vertical |
| 1054 | 355.00 | 61.00 | 334.32 | 318.29 | NÃO | fora da faixa vertical |
| 1055 | 354.00 | 61.00 | 334.66 | 318.29 | NÃO | fora da faixa vertical |
| 1056 | 353.00 | 61.00 | 334.99 | 318.29 | NÃO | fora da faixa vertical |
| 1057 | 352.00 | 60.00 | 336.28 | 319.29 | NÃO | fora da faixa vertical |
| 1058 | 351.00 | 60.00 | 336.62 | 319.29 | NÃO | fora da faixa vertical |
| 1059 | 350.00 | 59.00 | 337.90 | 320.29 | NÃO | fora da faixa vertical |
| 1060 | 349.00 | 59.00 | 338.25 | 320.29 | NÃO | fora da faixa vertical |
| 1061 | 348.00 | 59.00 | 338.60 | 320.29 | NÃO | fora da faixa vertical |
| 1062 | 347.00 | 58.00 | 339.89 | 321.29 | NÃO | fora da faixa vertical |
| 1063 | 346.00 | 58.00 | 340.24 | 321.29 | NÃO | fora da faixa vertical |
| 1064 | 345.00 | 58.00 | 340.60 | 321.29 | NÃO | fora da faixa vertical |
| 1065 | 344.00 | 57.00 | 341.89 | 322.29 | NÃO | fora da faixa vertical |
| 1066 | 343.00 | 57.00 | 342.25 | 322.29 | NÃO | fora da faixa vertical |
| 1067 | 342.00 | 57.00 | 342.62 | 322.29 | NÃO | fora da faixa vertical |
| 1068 | 341.00 | 56.00 | 343.91 | 323.29 | NÃO | fora da faixa vertical |
| 1069 | 340.00 | 56.00 | 344.28 | 323.29 | NÃO | fora da faixa vertical |
| 1070 | 339.00 | 56.00 | 344.65 | 323.29 | NÃO | fora da faixa vertical |
| 1071 | 338.00 | 56.00 | 345.02 | 323.29 | NÃO | fora da faixa vertical |
| 1072 | 337.00 | 55.00 | 346.32 | 324.29 | NÃO | fora da faixa vertical |
| 1073 | 336.00 | 55.00 | 346.70 | 324.29 | NÃO | fora da faixa vertical |
| 1074 | 335.00 | 55.00 | 347.08 | 324.29 | NÃO | fora da faixa vertical |
| 1075 | 334.00 | 54.00 | 348.39 | 325.29 | NÃO | fora da faixa vertical |
| 1076 | 333.00 | 54.00 | 348.77 | 325.29 | NÃO | fora da faixa vertical |
| 1077 | 332.00 | 54.00 | 349.15 | 325.29 | NÃO | fora da faixa vertical |
| 1078 | 331.00 | 54.00 | 349.54 | 325.29 | NÃO | fora da faixa vertical |
| 1079 | 330.00 | 53.00 | 350.85 | 326.29 | NÃO | fora da faixa vertical |
| 1080 | 329.00 | 53.00 | 351.24 | 326.29 | NÃO | fora da faixa vertical |
| 1081 | 328.00 | 53.00 | 351.64 | 326.29 | NÃO | fora da faixa vertical |
| 1082 | 327.00 | 53.00 | 352.04 | 326.29 | NÃO | fora da faixa vertical |
| 1083 | 326.00 | 52.00 | 353.35 | 327.29 | NÃO | fora da faixa vertical |
| 1084 | 325.00 | 52.00 | 353.75 | 327.29 | NÃO | fora da faixa vertical |
| 1085 | 324.00 | 52.00 | 354.15 | 327.29 | NÃO | fora da faixa vertical |
| 1086 | 323.00 | 52.00 | 354.56 | 327.29 | NÃO | fora da faixa vertical |
| 1087 | 322.00 | 52.00 | 354.97 | 327.29 | NÃO | fora da faixa vertical |
| 1088 | 321.00 | 51.00 | 356.29 | 328.29 | NÃO | fora da faixa vertical |
| 1089 | 320.00 | 51.00 | 356.70 | 328.29 | NÃO | fora da faixa vertical |
| 1090 | 319.00 | 51.00 | 357.11 | 328.29 | NÃO | fora da faixa vertical |
| 1091 | 318.00 | 51.00 | 357.53 | 328.29 | NÃO | fora da faixa vertical |
| 1092 | 317.00 | 51.00 | 357.95 | 328.29 | NÃO | fora da faixa vertical |
| 1093 | 316.00 | 50.00 | 359.27 | 329.29 | NÃO | fora da faixa vertical |
| 1094 | 315.00 | 50.00 | 359.69 | 329.29 | NÃO | fora da faixa vertical |
| 1095 | 314.00 | 50.00 | 360.12 | 329.29 | NÃO | fora da faixa vertical |
| 1096 | 313.00 | 50.00 | 360.54 | 329.29 | NÃO | fora da faixa vertical |
| 1097 | 312.00 | 50.00 | 360.97 | 329.29 | NÃO | fora da faixa vertical |
| 1098 | 311.00 | 49.00 | 362.31 | 330.29 | NÃO | fora da faixa vertical |
| 1099 | 310.00 | 49.00 | 362.74 | 330.29 | NÃO | fora da faixa vertical |
| 1100 | 309.00 | 49.00 | 363.17 | 330.29 | NÃO | fora da faixa vertical |
| 1101 | 308.00 | 49.00 | 363.61 | 330.29 | NÃO | fora da faixa vertical |
| 1102 | 307.00 | 49.00 | 364.05 | 330.29 | NÃO | fora da faixa vertical |
| 1103 | 306.00 | 49.00 | 364.49 | 330.29 | NÃO | fora da faixa vertical |
| 1104 | 305.00 | 49.00 | 364.93 | 330.29 | NÃO | fora da faixa vertical |
| 1105 | 304.00 | 48.00 | 366.27 | 331.29 | NÃO | fora da faixa vertical |
| 1106 | 303.00 | 48.00 | 366.72 | 331.29 | NÃO | fora da faixa vertical |
| 1107 | 302.00 | 48.00 | 367.16 | 331.29 | NÃO | fora da faixa vertical |
| 1108 | 301.00 | 48.00 | 367.61 | 331.29 | NÃO | fora da faixa vertical |
| 1109 | 300.00 | 48.00 | 368.07 | 331.29 | NÃO | fora da faixa vertical |
| 1110 | 299.00 | 48.00 | 368.52 | 331.29 | NÃO | fora da faixa vertical |
| 1111 | 298.00 | 48.00 | 368.98 | 331.29 | NÃO | fora da faixa vertical |
| 1112 | 297.00 | 48.00 | 369.44 | 331.29 | NÃO | fora da faixa vertical |
| 1113 | 296.00 | 48.00 | 369.90 | 331.29 | NÃO | fora da faixa vertical |
| 1114 | 295.00 | 47.00 | 371.25 | 332.29 | NÃO | fora da faixa vertical |
| 1115 | 294.00 | 47.00 | 371.71 | 332.29 | NÃO | fora da faixa vertical |
| 1116 | 293.00 | 47.00 | 372.18 | 332.29 | NÃO | fora da faixa vertical |
| 1117 | 292.00 | 47.00 | 372.65 | 332.29 | NÃO | fora da faixa vertical |
| 1118 | 291.00 | 47.00 | 373.12 | 332.29 | NÃO | fora da faixa vertical |
| 1119 | 290.00 | 47.00 | 373.59 | 332.29 | NÃO | fora da faixa vertical |
| 1120 | 289.00 | 47.00 | 374.07 | 332.29 | NÃO | fora da faixa vertical |
| 1121 | 288.00 | 47.00 | 374.54 | 332.29 | NÃO | fora da faixa vertical |
| 1122 | 287.00 | 47.00 | 375.02 | 332.29 | NÃO | fora da faixa vertical |
| 1123 | 286.00 | 47.00 | 375.50 | 332.29 | NÃO | fora da faixa vertical |
| 1124 | 285.00 | 47.00 | 375.99 | 332.29 | NÃO | fora da faixa vertical |
| 1125 | 284.00 | 47.00 | 376.47 | 332.29 | NÃO | fora da faixa vertical |
| 1126 | 283.00 | 47.00 | 376.96 | 332.29 | NÃO | fora da faixa vertical |
| 1127 | 282.00 | 47.00 | 377.45 | 332.29 | NÃO | fora da faixa vertical |
| 1128 | 281.00 | 47.00 | 377.94 | 332.29 | NÃO | fora da faixa vertical |
| 1129 | 280.00 | 47.00 | 378.43 | 332.29 | NÃO | fora da faixa vertical |
| 1130 | 279.00 | 47.00 | 378.93 | 332.29 | NÃO | fora da faixa vertical |
| 1131 | 278.00 | 47.00 | 379.42 | 332.29 | NÃO | fora da faixa vertical |
| 1132 | 277.00 | 47.00 | 379.92 | 332.29 | NÃO | fora da faixa vertical |
| 1133 | 276.00 | 47.00 | 380.42 | 332.29 | NÃO | fora da faixa vertical |
| 1134 | 275.00 | 47.00 | 380.93 | 332.29 | NÃO | fora da faixa vertical |
| 1135 | 274.00 | 47.00 | 381.43 | 332.29 | NÃO | fora da faixa vertical |
| 1136 | 273.00 | 47.00 | 381.94 | 332.29 | NÃO | fora da faixa vertical |
| 1137 | 272.00 | 47.00 | 382.45 | 332.29 | NÃO | fora da faixa vertical |
| 1138 | 271.00 | 47.00 | 382.96 | 332.29 | NÃO | fora da faixa vertical |
| 1139 | 270.00 | 47.00 | 383.47 | 332.29 | NÃO | fora da faixa vertical |
| 1140 | 269.00 | 47.00 | 383.99 | 332.29 | NÃO | fora da faixa vertical |
| 1141 | 268.00 | 47.00 | 384.50 | 332.29 | NÃO | fora da faixa vertical |
| 1142 | 267.00 | 47.00 | 385.02 | 332.29 | NÃO | fora da faixa vertical |
| 1143 | 266.00 | 47.00 | 385.54 | 332.29 | NÃO | fora da faixa vertical |
| 1144 | 265.00 | 47.00 | 386.06 | 332.29 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 557 | 280.00 | 376.00 | -187.00 | -3.29 |
| 558 | 281.00 | 376.00 | -186.00 | -3.29 |
| 559 | 282.00 | 376.00 | -185.00 | -3.29 |
| 560 | 283.00 | 376.00 | -184.00 | -3.29 |
| 561 | 284.00 | 376.00 | -183.00 | -3.29 |
| 562 | 285.00 | 376.00 | -182.00 | -3.29 |
| 563 | 286.00 | 376.00 | -181.00 | -3.29 |
| 564 | 287.00 | 376.00 | -180.00 | -3.29 |
| 565 | 288.00 | 376.00 | -179.00 | -3.29 |
| 566 | 289.00 | 376.00 | -178.00 | -3.29 |
| 567 | 290.00 | 376.00 | -177.00 | -3.29 |
| 568 | 291.00 | 376.00 | -176.00 | -3.29 |
| 569 | 292.00 | 376.00 | -175.00 | -3.29 |
| 570 | 293.00 | 376.00 | -174.00 | -3.29 |
| 571 | 294.00 | 376.00 | -173.00 | -3.29 |
| 572 | 295.00 | 376.00 | -172.00 | -3.29 |
| 573 | 296.00 | 376.00 | -171.00 | -3.29 |
| 574 | 297.00 | 376.00 | -170.00 | -3.29 |
| 575 | 298.00 | 376.00 | -169.00 | -3.29 |
| 576 | 299.00 | 376.00 | -168.00 | -3.29 |
| 577 | 300.00 | 376.00 | -167.00 | -3.29 |
| 578 | 301.00 | 376.00 | -166.00 | -3.29 |
| 579 | 302.00 | 376.00 | -165.00 | -3.29 |
| 580 | 303.00 | 376.00 | -164.00 | -3.29 |
| 581 | 304.00 | 376.00 | -163.00 | -3.29 |
| 582 | 305.00 | 376.00 | -162.00 | -3.29 |
| 583 | 306.00 | 376.00 | -161.00 | -3.29 |
| 584 | 307.00 | 376.00 | -160.00 | -3.29 |
| 585 | 308.00 | 376.00 | -159.00 | -3.29 |
| 586 | 309.00 | 376.00 | -158.00 | -3.29 |
| 587 | 310.00 | 376.00 | -157.00 | -3.29 |
| 588 | 311.00 | 376.00 | -156.00 | -3.29 |
| 589 | 312.00 | 376.00 | -155.00 | -3.29 |
| 590 | 313.00 | 376.00 | -154.00 | -3.29 |
| 591 | 314.00 | 376.00 | -153.00 | -3.29 |
| 592 | 315.00 | 376.00 | -152.00 | -3.29 |
| 593 | 316.00 | 376.00 | -151.00 | -3.29 |
| 594 | 317.00 | 376.00 | -150.00 | -3.29 |
| 595 | 318.00 | 376.00 | -149.00 | -3.29 |
| 596 | 319.00 | 376.00 | -148.00 | -3.29 |
| 597 | 320.00 | 376.00 | -147.00 | -3.29 |
| 598 | 321.00 | 376.00 | -146.00 | -3.29 |
| 599 | 322.00 | 376.00 | -145.00 | -3.29 |
| 600 | 323.00 | 376.00 | -144.00 | -3.29 |
| 601 | 324.00 | 376.00 | -143.00 | -3.29 |
| 602 | 325.00 | 376.00 | -142.00 | -3.29 |
| 603 | 326.00 | 376.00 | -141.00 | -3.29 |
| 604 | 327.00 | 376.00 | -140.00 | -3.29 |
| 605 | 328.00 | 376.00 | -139.00 | -3.29 |
| 606 | 329.00 | 376.00 | -138.00 | -3.29 |
| 607 | 330.00 | 376.00 | -137.00 | -3.29 |
| 608 | 331.00 | 376.00 | -136.00 | -3.29 |
| 609 | 332.00 | 376.00 | -135.00 | -3.29 |
| 610 | 333.00 | 376.00 | -134.00 | -3.29 |
| 611 | 334.00 | 376.00 | -133.00 | -3.29 |
| 612 | 335.00 | 376.00 | -132.00 | -3.29 |
| 613 | 336.00 | 376.00 | -131.00 | -3.29 |
| 614 | 337.00 | 376.00 | -130.00 | -3.29 |
| 615 | 338.00 | 376.00 | -129.00 | -3.29 |
| 616 | 339.00 | 376.00 | -128.00 | -3.29 |
| 617 | 340.00 | 376.00 | -127.00 | -3.29 |
| 618 | 341.00 | 376.00 | -126.00 | -3.29 |
| 619 | 342.00 | 376.00 | -125.00 | -3.29 |
| 620 | 343.00 | 376.00 | -124.00 | -3.29 |
| 621 | 344.00 | 376.00 | -123.00 | -3.29 |
| 622 | 345.00 | 376.00 | -122.00 | -3.29 |
| 623 | 346.00 | 376.00 | -121.00 | -3.29 |
| 624 | 347.00 | 376.00 | -120.00 | -3.29 |
| 625 | 348.00 | 376.00 | -119.00 | -3.29 |
| 626 | 349.00 | 376.00 | -118.00 | -3.29 |
| 627 | 350.00 | 376.00 | -117.00 | -3.29 |
| 628 | 351.00 | 376.00 | -116.00 | -3.29 |
| 629 | 352.00 | 376.00 | -115.00 | -3.29 |
| 630 | 353.00 | 376.00 | -114.00 | -3.29 |
| 631 | 354.00 | 376.00 | -113.00 | -3.29 |
| 632 | 355.00 | 376.00 | -112.00 | -3.29 |
| 633 | 356.00 | 376.00 | -111.00 | -3.29 |
| 634 | 357.00 | 376.00 | -110.00 | -3.29 |
| 635 | 358.00 | 376.00 | -109.00 | -3.29 |
| 636 | 359.00 | 376.00 | -108.00 | -3.29 |
| 637 | 360.00 | 376.00 | -107.00 | -3.29 |
| 638 | 361.00 | 376.00 | -106.00 | -3.29 |
| 639 | 362.00 | 376.00 | -105.00 | -3.29 |
| 640 | 363.00 | 376.00 | -104.00 | -3.29 |
| 641 | 364.00 | 376.00 | -103.00 | -3.29 |
| 642 | 365.00 | 376.00 | -102.00 | -3.29 |
| 643 | 366.00 | 376.00 | -101.00 | -3.29 |
| 644 | 367.00 | 376.00 | -100.00 | -3.29 |
| 645 | 368.00 | 376.00 | -99.00 | -3.29 |
| 646 | 369.00 | 376.00 | -98.00 | -3.29 |
| 647 | 370.00 | 376.00 | -97.00 | -3.29 |
| 648 | 371.00 | 376.00 | -96.00 | -3.29 |
| 649 | 372.00 | 376.00 | -95.00 | -3.29 |
| 650 | 373.00 | 376.00 | -94.00 | -3.29 |
| 651 | 374.00 | 376.00 | -93.00 | -3.29 |
| 652 | 375.00 | 376.00 | -92.00 | -3.29 |
| 653 | 376.00 | 376.00 | -91.00 | -3.29 |
| 654 | 377.00 | 376.00 | -90.00 | -3.29 |
| 655 | 378.00 | 376.00 | -89.00 | -3.29 |
| 656 | 379.00 | 376.00 | -88.00 | -3.29 |
| 657 | 380.00 | 376.00 | -87.00 | -3.29 |
| 658 | 381.00 | 376.00 | -86.00 | -3.29 |
| 659 | 382.00 | 376.00 | -85.00 | -3.29 |
| 660 | 383.00 | 376.00 | -84.00 | -3.29 |
| 661 | 384.00 | 376.00 | -83.00 | -3.29 |
| 662 | 385.00 | 376.00 | -82.00 | -3.29 |
| 663 | 386.00 | 376.00 | -81.00 | -3.29 |
| 664 | 387.00 | 376.00 | -80.00 | -3.29 |
| 665 | 388.00 | 376.00 | -79.00 | -3.29 |
| 666 | 389.00 | 376.00 | -78.00 | -3.29 |
| 667 | 390.00 | 376.00 | -77.00 | -3.29 |
| 668 | 391.00 | 376.00 | -76.00 | -3.29 |
| 669 | 392.00 | 376.00 | -75.00 | -3.29 |
| 670 | 393.00 | 376.00 | -74.00 | -3.29 |
| 671 | 394.00 | 376.00 | -73.00 | -3.29 |
| 672 | 395.00 | 376.00 | -72.00 | -3.29 |
| 673 | 396.00 | 376.00 | -71.00 | -3.29 |
| 674 | 397.00 | 376.00 | -70.00 | -3.29 |
| 675 | 398.00 | 376.00 | -69.00 | -3.29 |
| 676 | 399.00 | 376.00 | -68.00 | -3.29 |
| 677 | 400.00 | 376.00 | -67.00 | -3.29 |
| 678 | 401.00 | 376.00 | -66.00 | -3.29 |
| 679 | 402.00 | 376.00 | -65.00 | -3.29 |
| 680 | 403.00 | 376.00 | -64.00 | -3.29 |
| 681 | 404.00 | 376.00 | -63.00 | -3.29 |
| 682 | 405.00 | 376.00 | -62.00 | -3.29 |
| 683 | 406.00 | 376.00 | -61.00 | -3.29 |
| 684 | 407.00 | 376.00 | -60.00 | -3.29 |
| 685 | 408.00 | 376.00 | -59.00 | -3.29 |
| 686 | 409.00 | 376.00 | -58.00 | -3.29 |
| 687 | 410.00 | 376.00 | -57.00 | -3.29 |
| 688 | 411.00 | 376.00 | -56.00 | -3.29 |
| 689 | 412.00 | 376.00 | -55.00 | -3.29 |
| 690 | 413.00 | 376.00 | -54.00 | -3.29 |
| 691 | 414.00 | 376.00 | -53.00 | -3.29 |
| 692 | 415.00 | 376.00 | -52.00 | -3.29 |
| 693 | 416.00 | 376.00 | -51.00 | -3.29 |
| 694 | 417.00 | 376.00 | -50.00 | -3.29 |
| 695 | 418.00 | 376.00 | -49.00 | -3.29 |
| 696 | 419.00 | 376.00 | -48.00 | -3.29 |
| 697 | 420.00 | 376.00 | -47.00 | -3.29 |
| 698 | 421.00 | 376.00 | -46.00 | -3.29 |
| 699 | 422.00 | 376.00 | -45.00 | -3.29 |
| 700 | 423.00 | 376.00 | -44.00 | -3.29 |
| 701 | 424.00 | 376.00 | -43.00 | -3.29 |
| 702 | 425.00 | 376.00 | -42.00 | -3.29 |
| 703 | 426.00 | 376.00 | -41.00 | -3.29 |
| 704 | 427.00 | 376.00 | -40.00 | -3.29 |
| 705 | 428.00 | 376.00 | -39.00 | -3.29 |
| 706 | 429.00 | 376.00 | -38.00 | -3.29 |
| 707 | 430.00 | 376.00 | -37.00 | -3.29 |
| 708 | 431.00 | 376.00 | -36.00 | -3.29 |
| 709 | 432.00 | 376.00 | -35.00 | -3.29 |
| 710 | 433.00 | 376.00 | -34.00 | -3.29 |
| 711 | 434.00 | 376.00 | -33.00 | -3.29 |
| 712 | 435.00 | 376.00 | -32.00 | -3.29 |
| 713 | 436.00 | 376.00 | -31.00 | -3.29 |
| 714 | 437.00 | 376.00 | -30.00 | -3.29 |
| 715 | 438.00 | 376.00 | -29.00 | -3.29 |
| 716 | 439.00 | 376.00 | -28.00 | -3.29 |
| 717 | 439.00 | 375.00 | -28.00 | -4.29 |
| 718 | 440.00 | 374.00 | -27.00 | -5.29 |
| 719 | 440.00 | 373.00 | -27.00 | -6.29 |
| 720 | 441.00 | 372.00 | -26.00 | -7.29 |
| 721 | 442.00 | 371.00 | -25.00 | -8.29 |
| 722 | 443.00 | 370.00 | -24.00 | -9.29 |
| 723 | 443.00 | 369.00 | -24.00 | -10.29 |
| 724 | 444.00 | 368.00 | -23.00 | -11.29 |
| 725 | 445.00 | 367.00 | -22.00 | -12.29 |
| 726 | 446.00 | 366.00 | -21.00 | -13.29 |
| 727 | 446.00 | 365.00 | -21.00 | -14.29 |
| 728 | 447.00 | 364.00 | -20.00 | -15.29 |
| 729 | 448.00 | 363.00 | -19.00 | -16.29 |
| 730 | 448.00 | 362.00 | -19.00 | -17.29 |
| 731 | 449.00 | 361.00 | -18.00 | -18.29 |
| 732 | 450.00 | 360.00 | -17.00 | -19.29 |
| 733 | 450.00 | 359.00 | -17.00 | -20.29 |
| 734 | 451.00 | 358.00 | -16.00 | -21.29 |
| 735 | 451.00 | 357.00 | -16.00 | -22.29 |
| 736 | 452.00 | 356.00 | -15.00 | -23.29 |
| 737 | 453.00 | 355.00 | -14.00 | -24.29 |
| 738 | 453.00 | 354.00 | -14.00 | -25.29 |
| 739 | 454.00 | 353.00 | -13.00 | -26.29 |
| 740 | 454.00 | 352.00 | -13.00 | -27.29 |
| 741 | 455.00 | 351.00 | -12.00 | -28.29 |
| 742 | 456.00 | 350.00 | -11.00 | -29.29 |
| 743 | 456.00 | 349.00 | -11.00 | -30.29 |
| 744 | 457.00 | 348.00 | -10.00 | -31.29 |
| 745 | 457.00 | 347.00 | -10.00 | -32.29 |
| 746 | 458.00 | 346.00 | -9.00 | -33.29 |
| 747 | 458.00 | 345.00 | -9.00 | -34.29 |
| 748 | 459.00 | 344.00 | -8.00 | -35.29 |
| 749 | 459.00 | 343.00 | -8.00 | -36.29 |
| 750 | 460.00 | 342.00 | -7.00 | -37.29 |
| 751 | 460.00 | 341.00 | -7.00 | -38.29 |
| 752 | 461.00 | 340.00 | -6.00 | -39.29 |
| 753 | 461.00 | 339.00 | -6.00 | -40.29 |
| 754 | 462.00 | 338.00 | -5.00 | -41.29 |
| 755 | 462.00 | 337.00 | -5.00 | -42.29 |
| 756 | 463.00 | 336.00 | -4.00 | -43.29 |
| 757 | 463.00 | 335.00 | -4.00 | -44.29 |
| 758 | 464.00 | 334.00 | -3.00 | -45.29 |
| 759 | 464.00 | 333.00 | -3.00 | -46.29 |
| 760 | 465.00 | 332.00 | -2.00 | -47.29 |
| 761 | 465.00 | 331.00 | -2.00 | -48.29 |
| 762 | 466.00 | 330.00 | -1.00 | -49.29 |
| 763 | 466.00 | 329.00 | -1.00 | -50.29 |
| 764 | 467.00 | 328.00 | 0.00 | -51.29 |
| 765 | 467.00 | 327.00 | 0.00 | -52.29 |
| 766 | 468.00 | 326.00 | 1.00 | -53.29 |
| 767 | 468.00 | 325.00 | 1.00 | -54.29 |
| 768 | 468.00 | 324.00 | 1.00 | -55.29 |
| 769 | 469.00 | 323.00 | 2.00 | -56.29 |
| 770 | 469.00 | 322.00 | 2.00 | -57.29 |
| 771 | 469.00 | 321.00 | 2.00 | -58.29 |
| 772 | 470.00 | 320.00 | 3.00 | -59.29 |
| 773 | 470.00 | 319.00 | 3.00 | -60.29 |
| 774 | 471.00 | 318.00 | 4.00 | -61.29 |
| 775 | 471.00 | 317.00 | 4.00 | -62.29 |
| 776 | 471.00 | 316.00 | 4.00 | -63.29 |
| 777 | 472.00 | 315.00 | 5.00 | -64.29 |
| 778 | 472.00 | 314.00 | 5.00 | -65.29 |
| 779 | 472.00 | 313.00 | 5.00 | -66.29 |
| 780 | 473.00 | 312.00 | 6.00 | -67.29 |
| 781 | 473.00 | 311.00 | 6.00 | -68.29 |
| 782 | 473.00 | 310.00 | 6.00 | -69.29 |
| 783 | 473.00 | 309.00 | 6.00 | -70.29 |
| 784 | 474.00 | 308.00 | 7.00 | -71.29 |
| 785 | 474.00 | 307.00 | 7.00 | -72.29 |
| 786 | 474.00 | 306.00 | 7.00 | -73.29 |
| 787 | 475.00 | 305.00 | 8.00 | -74.29 |
| 788 | 475.00 | 304.00 | 8.00 | -75.29 |
| 789 | 475.00 | 303.00 | 8.00 | -76.29 |
| 790 | 475.00 | 302.00 | 8.00 | -77.29 |
| 791 | 476.00 | 301.00 | 9.00 | -78.29 |
| 792 | 476.00 | 300.00 | 9.00 | -79.29 |
| 793 | 476.00 | 299.00 | 9.00 | -80.29 |
| 794 | 476.00 | 298.00 | 9.00 | -81.29 |
| 795 | 477.00 | 297.00 | 10.00 | -82.29 |
| 796 | 477.00 | 296.00 | 10.00 | -83.29 |
| 797 | 477.00 | 295.00 | 10.00 | -84.29 |
| 798 | 477.00 | 294.00 | 10.00 | -85.29 |
| 799 | 478.00 | 293.00 | 11.00 | -86.29 |
| 800 | 478.00 | 292.00 | 11.00 | -87.29 |
| 801 | 478.00 | 291.00 | 11.00 | -88.29 |
| 802 | 478.00 | 290.00 | 11.00 | -89.29 |
| 803 | 478.00 | 289.00 | 11.00 | -90.29 |
| 804 | 479.00 | 288.00 | 12.00 | -91.29 |
| 805 | 479.00 | 287.00 | 12.00 | -92.29 |
| 806 | 479.00 | 286.00 | 12.00 | -93.29 |
| 807 | 479.00 | 285.00 | 12.00 | -94.29 |
| 808 | 479.00 | 284.00 | 12.00 | -95.29 |
| 809 | 480.00 | 283.00 | 13.00 | -96.29 |
| 810 | 480.00 | 282.00 | 13.00 | -97.29 |
| 811 | 480.00 | 281.00 | 13.00 | -98.29 |
| 812 | 480.00 | 280.00 | 13.00 | -99.29 |
| 813 | 480.00 | 279.00 | 13.00 | -100.29 |
| 814 | 480.00 | 278.00 | 13.00 | -101.29 |
| 815 | 480.00 | 277.00 | 13.00 | -102.29 |
| 816 | 481.00 | 276.00 | 14.00 | -103.29 |
| 817 | 481.00 | 275.00 | 14.00 | -104.29 |
| 818 | 481.00 | 274.00 | 14.00 | -105.29 |
| 819 | 481.00 | 273.00 | 14.00 | -106.29 |
| 820 | 481.00 | 272.00 | 14.00 | -107.29 |
| 821 | 481.00 | 271.00 | 14.00 | -108.29 |
| 822 | 481.00 | 270.00 | 14.00 | -109.29 |
| 823 | 481.00 | 269.00 | 14.00 | -110.29 |
| 824 | 482.00 | 268.00 | 15.00 | -111.29 |
| 825 | 482.00 | 267.00 | 15.00 | -112.29 |
| 826 | 482.00 | 266.00 | 15.00 | -113.29 |
| 827 | 482.00 | 265.00 | 15.00 | -114.29 |
| 828 | 482.00 | 264.00 | 15.00 | -115.29 |
| 829 | 482.00 | 263.00 | 15.00 | -116.29 |
| 830 | 482.00 | 262.00 | 15.00 | -117.29 |
| 831 | 482.00 | 261.00 | 15.00 | -118.29 |
| 832 | 482.00 | 260.00 | 15.00 | -119.29 |
| 833 | 482.00 | 259.00 | 15.00 | -120.29 |
| 834 | 482.00 | 258.00 | 15.00 | -121.29 |
| 835 | 482.00 | 257.00 | 15.00 | -122.29 |
| 836 | 482.00 | 256.00 | 15.00 | -123.29 |
| 837 | 482.00 | 255.00 | 15.00 | -124.29 |
| 838 | 482.00 | 254.00 | 15.00 | -125.29 |
| 839 | 482.00 | 253.00 | 15.00 | -126.29 |
| 840 | 482.00 | 252.00 | 15.00 | -127.29 |
| 841 | 482.00 | 251.00 | 15.00 | -128.29 |
| 842 | 482.00 | 250.00 | 15.00 | -129.29 |
| 843 | 482.00 | 249.00 | 15.00 | -130.29 |
| 844 | 482.00 | 248.00 | 15.00 | -131.29 |
| 845 | 482.00 | 247.00 | 15.00 | -132.29 |
| 846 | 482.00 | 246.00 | 15.00 | -133.29 |
| 847 | 482.00 | 245.00 | 15.00 | -134.29 |
| 848 | 482.00 | 244.00 | 15.00 | -135.29 |
| 849 | 482.00 | 243.00 | 15.00 | -136.29 |
| 850 | 482.00 | 242.00 | 15.00 | -137.29 |
| 851 | 482.00 | 241.00 | 15.00 | -138.29 |
| 852 | 482.00 | 240.00 | 15.00 | -139.29 |
| 853 | 482.00 | 239.00 | 15.00 | -140.29 |
| 854 | 482.00 | 238.00 | 15.00 | -141.29 |
| 855 | 482.00 | 237.00 | 15.00 | -142.29 |
| 856 | 482.00 | 236.00 | 15.00 | -143.29 |
| 857 | 482.00 | 235.00 | 15.00 | -144.29 |
| 858 | 482.00 | 234.00 | 15.00 | -145.29 |
| 859 | 482.00 | 233.00 | 15.00 | -146.29 |
| 860 | 482.00 | 232.00 | 15.00 | -147.29 |
| 861 | 481.00 | 231.00 | 14.00 | -148.29 |
| 862 | 481.00 | 230.00 | 14.00 | -149.29 |
| 863 | 481.00 | 229.00 | 14.00 | -150.29 |
| 864 | 481.00 | 228.00 | 14.00 | -151.29 |
| 865 | 481.00 | 227.00 | 14.00 | -152.29 |
| 866 | 481.00 | 226.00 | 14.00 | -153.29 |
| 867 | 481.00 | 225.00 | 14.00 | -154.29 |
| 868 | 481.00 | 224.00 | 14.00 | -155.29 |
| 869 | 480.00 | 223.00 | 13.00 | -156.29 |
| 870 | 480.00 | 222.00 | 13.00 | -157.29 |
| 871 | 480.00 | 221.00 | 13.00 | -158.29 |
| 872 | 480.00 | 220.00 | 13.00 | -159.29 |
| 873 | 480.00 | 219.00 | 13.00 | -160.29 |
| 874 | 480.00 | 218.00 | 13.00 | -161.29 |
| 875 | 480.00 | 217.00 | 13.00 | -162.29 |
| 876 | 480.00 | 216.00 | 13.00 | -163.29 |
| 877 | 479.00 | 215.00 | 12.00 | -164.29 |
| 878 | 479.00 | 214.00 | 12.00 | -165.29 |
| 879 | 479.00 | 213.00 | 12.00 | -166.29 |
| 880 | 479.00 | 212.00 | 12.00 | -167.29 |
| 881 | 479.00 | 211.00 | 12.00 | -168.29 |
| 882 | 478.00 | 210.00 | 11.00 | -169.29 |
| 883 | 478.00 | 209.00 | 11.00 | -170.29 |
| 884 | 478.00 | 208.00 | 11.00 | -171.29 |
| 885 | 478.00 | 207.00 | 11.00 | -172.29 |
| 886 | 477.00 | 206.00 | 10.00 | -173.29 |
| 887 | 477.00 | 205.00 | 10.00 | -174.29 |
| 888 | 477.00 | 204.00 | 10.00 | -175.29 |
| 889 | 477.00 | 203.00 | 10.00 | -176.29 |
| 890 | 477.00 | 202.00 | 10.00 | -177.29 |
| 891 | 476.00 | 201.00 | 9.00 | -178.29 |
| 892 | 476.00 | 200.00 | 9.00 | -179.29 |

- primeiro índice: 557
- último índice: 892
- quantidade: 336
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![50_geo dir](audit_outputs/75_geo_dir_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![50_geo dir polyfit](audit_outputs/75_geo_dir_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

## Imagem: 75_geo

### Lado: esq

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 1063
- ponto de contato recebido: [114.0, 303.0]
- baseline_y: 303.0
- baseline_ajustada: 305.5
- lado solicitado: esq
- largura da região: 137 px
- altura da gota: 250.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 297.00 | 53.00 | 309.82 | 252.50 | NÃO | fora da faixa vertical |
| 1 | 296.00 | 54.00 | 308.42 | 251.50 | NÃO | fora da faixa vertical |
| 2 | 295.00 | 54.00 | 307.83 | 251.50 | NÃO | fora da faixa vertical |
| 3 | 294.00 | 54.00 | 307.25 | 251.50 | NÃO | fora da faixa vertical |
| 4 | 293.00 | 54.00 | 306.66 | 251.50 | NÃO | fora da faixa vertical |
| 5 | 292.00 | 54.00 | 306.08 | 251.50 | NÃO | fora da faixa vertical |
| 6 | 291.00 | 54.00 | 305.50 | 251.50 | NÃO | fora da faixa vertical |
| 7 | 290.00 | 54.00 | 304.92 | 251.50 | NÃO | fora da faixa vertical |
| 8 | 289.00 | 54.00 | 304.35 | 251.50 | NÃO | fora da faixa vertical |
| 9 | 288.00 | 55.00 | 302.95 | 250.50 | NÃO | fora da faixa vertical |
| 10 | 287.00 | 55.00 | 302.38 | 250.50 | NÃO | fora da faixa vertical |
| 11 | 286.00 | 55.00 | 301.81 | 250.50 | NÃO | fora da faixa vertical |
| 12 | 285.00 | 55.00 | 301.24 | 250.50 | NÃO | fora da faixa vertical |
| 13 | 284.00 | 55.00 | 300.67 | 250.50 | NÃO | fora da faixa vertical |
| 14 | 283.00 | 55.00 | 300.11 | 250.50 | NÃO | fora da faixa vertical |
| 15 | 282.00 | 55.00 | 299.55 | 250.50 | NÃO | fora da faixa vertical |
| 16 | 281.00 | 56.00 | 298.16 | 249.50 | NÃO | fora da faixa vertical |
| 17 | 280.00 | 56.00 | 297.60 | 249.50 | NÃO | fora da faixa vertical |
| 18 | 279.00 | 56.00 | 297.04 | 249.50 | NÃO | fora da faixa vertical |
| 19 | 278.00 | 56.00 | 296.49 | 249.50 | NÃO | fora da faixa vertical |
| 20 | 277.00 | 56.00 | 295.94 | 249.50 | NÃO | fora da faixa vertical |
| 21 | 276.00 | 57.00 | 294.55 | 248.50 | NÃO | fora da faixa vertical |
| 22 | 275.00 | 57.00 | 294.00 | 248.50 | NÃO | fora da faixa vertical |
| 23 | 274.00 | 57.00 | 293.46 | 248.50 | NÃO | fora da faixa vertical |
| 24 | 273.00 | 57.00 | 292.91 | 248.50 | NÃO | fora da faixa vertical |
| 25 | 272.00 | 57.00 | 292.37 | 248.50 | NÃO | fora da faixa vertical |
| 26 | 271.00 | 58.00 | 290.99 | 247.50 | NÃO | fora da faixa vertical |
| 27 | 270.00 | 58.00 | 290.45 | 247.50 | NÃO | fora da faixa vertical |
| 28 | 269.00 | 58.00 | 289.91 | 247.50 | NÃO | fora da faixa vertical |
| 29 | 268.00 | 58.00 | 289.38 | 247.50 | NÃO | fora da faixa vertical |
| 30 | 267.00 | 59.00 | 288.00 | 246.50 | NÃO | fora da faixa vertical |
| 31 | 266.00 | 59.00 | 287.47 | 246.50 | NÃO | fora da faixa vertical |
| 32 | 265.00 | 59.00 | 286.94 | 246.50 | NÃO | fora da faixa vertical |
| 33 | 264.00 | 59.00 | 286.42 | 246.50 | NÃO | fora da faixa vertical |
| 34 | 263.00 | 60.00 | 285.04 | 245.50 | NÃO | fora da faixa vertical |
| 35 | 262.00 | 60.00 | 284.52 | 245.50 | NÃO | fora da faixa vertical |
| 36 | 261.00 | 60.00 | 284.00 | 245.50 | NÃO | fora da faixa vertical |
| 37 | 260.00 | 61.00 | 282.63 | 244.50 | NÃO | fora da faixa vertical |
| 38 | 259.00 | 61.00 | 282.12 | 244.50 | NÃO | fora da faixa vertical |
| 39 | 258.00 | 61.00 | 281.60 | 244.50 | NÃO | fora da faixa vertical |
| 40 | 257.00 | 62.00 | 280.23 | 243.50 | NÃO | fora da faixa vertical |
| 41 | 256.00 | 62.00 | 279.72 | 243.50 | NÃO | fora da faixa vertical |
| 42 | 255.00 | 62.00 | 279.22 | 243.50 | NÃO | fora da faixa vertical |
| 43 | 254.00 | 62.00 | 278.71 | 243.50 | NÃO | fora da faixa vertical |
| 44 | 253.00 | 63.00 | 277.35 | 242.50 | NÃO | fora da faixa vertical |
| 45 | 252.00 | 63.00 | 276.85 | 242.50 | NÃO | fora da faixa vertical |
| 46 | 251.00 | 63.00 | 276.35 | 242.50 | NÃO | fora da faixa vertical |
| 47 | 250.00 | 64.00 | 274.99 | 241.50 | NÃO | fora da faixa vertical |
| 48 | 249.00 | 64.00 | 274.49 | 241.50 | NÃO | fora da faixa vertical |
| 49 | 248.00 | 65.00 | 273.13 | 240.50 | NÃO | fora da faixa vertical |
| 50 | 247.00 | 65.00 | 272.64 | 240.50 | NÃO | fora da faixa vertical |
| 51 | 246.00 | 65.00 | 272.15 | 240.50 | NÃO | fora da faixa vertical |
| 52 | 245.00 | 66.00 | 270.80 | 239.50 | NÃO | fora da faixa vertical |
| 53 | 244.00 | 66.00 | 270.31 | 239.50 | NÃO | fora da faixa vertical |
| 54 | 243.00 | 66.00 | 269.83 | 239.50 | NÃO | fora da faixa vertical |
| 55 | 242.00 | 67.00 | 268.48 | 238.50 | NÃO | fora da faixa vertical |
| 56 | 241.00 | 67.00 | 268.00 | 238.50 | NÃO | fora da faixa vertical |
| 57 | 240.00 | 68.00 | 266.65 | 237.50 | NÃO | fora da faixa vertical |
| 58 | 239.00 | 68.00 | 266.18 | 237.50 | NÃO | fora da faixa vertical |
| 59 | 238.00 | 68.00 | 265.71 | 237.50 | NÃO | fora da faixa vertical |
| 60 | 237.00 | 69.00 | 264.36 | 236.50 | NÃO | fora da faixa vertical |
| 61 | 236.00 | 69.00 | 263.89 | 236.50 | NÃO | fora da faixa vertical |
| 62 | 235.00 | 70.00 | 262.55 | 235.50 | NÃO | fora da faixa vertical |
| 63 | 234.00 | 70.00 | 262.09 | 235.50 | NÃO | fora da faixa vertical |
| 64 | 233.00 | 71.00 | 260.74 | 234.50 | NÃO | fora da faixa vertical |
| 65 | 232.00 | 71.00 | 260.28 | 234.50 | NÃO | fora da faixa vertical |
| 66 | 231.00 | 72.00 | 258.94 | 233.50 | NÃO | fora da faixa vertical |
| 67 | 230.00 | 72.00 | 258.49 | 233.50 | NÃO | fora da faixa vertical |
| 68 | 229.00 | 73.00 | 257.15 | 232.50 | NÃO | fora da faixa vertical |
| 69 | 228.00 | 73.00 | 256.70 | 232.50 | NÃO | fora da faixa vertical |
| 70 | 227.00 | 74.00 | 255.36 | 231.50 | NÃO | fora da faixa vertical |
| 71 | 226.00 | 74.00 | 254.92 | 231.50 | NÃO | fora da faixa vertical |
| 72 | 225.00 | 74.00 | 254.48 | 231.50 | NÃO | fora da faixa vertical |
| 73 | 224.00 | 75.00 | 253.15 | 230.50 | NÃO | fora da faixa vertical |
| 74 | 223.00 | 75.00 | 252.72 | 230.50 | NÃO | fora da faixa vertical |
| 75 | 222.00 | 76.00 | 251.38 | 229.50 | NÃO | fora da faixa vertical |
| 76 | 221.00 | 76.00 | 250.95 | 229.50 | NÃO | fora da faixa vertical |
| 77 | 220.00 | 77.00 | 249.62 | 228.50 | NÃO | fora da faixa vertical |
| 78 | 219.00 | 77.00 | 249.20 | 228.50 | NÃO | fora da faixa vertical |
| 79 | 218.00 | 78.00 | 247.87 | 227.50 | NÃO | fora da faixa vertical |
| 80 | 217.00 | 79.00 | 246.55 | 226.50 | NÃO | fora da faixa vertical |
| 81 | 216.00 | 79.00 | 246.13 | 226.50 | NÃO | fora da faixa vertical |
| 82 | 215.00 | 80.00 | 244.81 | 225.50 | NÃO | fora da faixa vertical |
| 83 | 214.00 | 80.00 | 244.40 | 225.50 | NÃO | fora da faixa vertical |
| 84 | 213.00 | 81.00 | 243.07 | 224.50 | NÃO | fora da faixa vertical |
| 85 | 212.00 | 82.00 | 241.75 | 223.50 | NÃO | fora da faixa vertical |
| 86 | 211.00 | 82.00 | 241.35 | 223.50 | NÃO | fora da faixa vertical |
| 87 | 210.00 | 83.00 | 240.03 | 222.50 | NÃO | fora da faixa vertical |
| 88 | 209.00 | 83.00 | 239.64 | 222.50 | NÃO | fora da faixa vertical |
| 89 | 208.00 | 84.00 | 238.32 | 221.50 | NÃO | fora da faixa vertical |
| 90 | 207.00 | 85.00 | 237.01 | 220.50 | NÃO | fora da faixa vertical |
| 91 | 206.00 | 85.00 | 236.62 | 220.50 | NÃO | fora da faixa vertical |
| 92 | 205.00 | 86.00 | 235.31 | 219.50 | NÃO | fora da faixa vertical |
| 93 | 204.00 | 86.00 | 234.92 | 219.50 | NÃO | fora da faixa vertical |
| 94 | 203.00 | 87.00 | 233.62 | 218.50 | NÃO | fora da faixa vertical |
| 95 | 202.00 | 88.00 | 232.31 | 217.50 | NÃO | fora da faixa vertical |
| 96 | 201.00 | 89.00 | 231.01 | 216.50 | NÃO | fora da faixa vertical |
| 97 | 200.00 | 89.00 | 230.63 | 216.50 | NÃO | fora da faixa vertical |
| 98 | 199.00 | 90.00 | 229.33 | 215.50 | NÃO | fora da faixa vertical |
| 99 | 198.00 | 91.00 | 228.04 | 214.50 | NÃO | fora da faixa vertical |
| 100 | 197.00 | 92.00 | 226.74 | 213.50 | NÃO | fora da faixa vertical |
| 101 | 196.00 | 92.00 | 226.37 | 213.50 | NÃO | fora da faixa vertical |
| 102 | 195.00 | 93.00 | 225.08 | 212.50 | NÃO | fora da faixa vertical |
| 103 | 194.00 | 94.00 | 223.79 | 211.50 | NÃO | fora da faixa vertical |
| 104 | 193.00 | 95.00 | 222.50 | 210.50 | NÃO | fora da faixa vertical |
| 105 | 192.00 | 95.00 | 222.14 | 210.50 | NÃO | fora da faixa vertical |
| 106 | 191.00 | 96.00 | 220.86 | 209.50 | NÃO | fora da faixa vertical |
| 107 | 190.00 | 97.00 | 219.57 | 208.50 | NÃO | fora da faixa vertical |
| 108 | 189.00 | 98.00 | 218.29 | 207.50 | NÃO | fora da faixa vertical |
| 109 | 188.00 | 98.00 | 217.95 | 207.50 | NÃO | fora da faixa vertical |
| 110 | 187.00 | 99.00 | 216.67 | 206.50 | NÃO | fora da faixa vertical |
| 111 | 186.00 | 100.00 | 215.39 | 205.50 | NÃO | fora da faixa vertical |
| 112 | 185.00 | 101.00 | 214.11 | 204.50 | NÃO | fora da faixa vertical |
| 113 | 184.00 | 102.00 | 212.84 | 203.50 | NÃO | fora da faixa vertical |
| 114 | 183.00 | 103.00 | 211.57 | 202.50 | NÃO | fora da faixa vertical |
| 115 | 182.00 | 104.00 | 210.30 | 201.50 | NÃO | fora da faixa vertical |
| 116 | 181.00 | 105.00 | 209.03 | 200.50 | NÃO | fora da faixa vertical |
| 117 | 180.00 | 105.00 | 208.71 | 200.50 | NÃO | fora da faixa vertical |
| 118 | 179.00 | 106.00 | 207.45 | 199.50 | NÃO | fora da faixa vertical |
| 119 | 178.00 | 107.00 | 206.18 | 198.50 | NÃO | fora da faixa vertical |
| 120 | 177.00 | 108.00 | 204.92 | 197.50 | NÃO | fora da faixa vertical |
| 121 | 176.00 | 109.00 | 203.67 | 196.50 | NÃO | fora da faixa vertical |
| 122 | 175.00 | 110.00 | 202.41 | 195.50 | NÃO | fora da faixa vertical |
| 123 | 174.00 | 111.00 | 201.16 | 194.50 | NÃO | fora da faixa vertical |
| 124 | 173.00 | 112.00 | 199.90 | 193.50 | NÃO | fora da faixa vertical |
| 125 | 172.00 | 113.00 | 198.66 | 192.50 | NÃO | fora da faixa vertical |
| 126 | 171.00 | 114.00 | 197.41 | 191.50 | NÃO | fora da faixa vertical |
| 127 | 170.00 | 115.00 | 196.16 | 190.50 | NÃO | fora da faixa vertical |
| 128 | 169.00 | 116.00 | 194.92 | 189.50 | NÃO | fora da faixa vertical |
| 129 | 169.00 | 117.00 | 193.96 | 188.50 | NÃO | fora da faixa vertical |
| 130 | 168.00 | 118.00 | 192.72 | 187.50 | NÃO | fora da faixa vertical |
| 131 | 167.00 | 119.00 | 191.48 | 186.50 | NÃO | fora da faixa vertical |
| 132 | 166.00 | 120.00 | 190.24 | 185.50 | NÃO | fora da faixa vertical |
| 133 | 165.00 | 121.00 | 189.01 | 184.50 | NÃO | fora da faixa vertical |
| 134 | 164.00 | 122.00 | 187.78 | 183.50 | NÃO | fora da faixa vertical |
| 135 | 163.00 | 123.00 | 186.55 | 182.50 | NÃO | fora da faixa vertical |
| 136 | 162.00 | 124.00 | 185.32 | 181.50 | NÃO | fora da faixa vertical |
| 137 | 161.00 | 125.00 | 184.10 | 180.50 | NÃO | fora da faixa vertical |
| 138 | 160.00 | 126.00 | 182.88 | 179.50 | NÃO | fora da faixa vertical |
| 139 | 160.00 | 127.00 | 181.91 | 178.50 | NÃO | fora da faixa vertical |
| 140 | 159.00 | 128.00 | 180.69 | 177.50 | NÃO | fora da faixa vertical |
| 141 | 158.00 | 129.00 | 179.48 | 176.50 | NÃO | fora da faixa vertical |
| 142 | 157.00 | 130.00 | 178.26 | 175.50 | NÃO | fora da faixa vertical |
| 143 | 157.00 | 131.00 | 177.29 | 174.50 | NÃO | fora da faixa vertical |
| 144 | 156.00 | 132.00 | 176.08 | 173.50 | NÃO | fora da faixa vertical |
| 145 | 155.00 | 133.00 | 174.87 | 172.50 | NÃO | fora da faixa vertical |
| 146 | 154.00 | 134.00 | 173.67 | 171.50 | NÃO | fora da faixa vertical |
| 147 | 154.00 | 135.00 | 172.70 | 170.50 | NÃO | fora da faixa vertical |
| 148 | 153.00 | 136.00 | 171.49 | 169.50 | NÃO | fora da faixa vertical |
| 149 | 152.00 | 137.00 | 170.29 | 168.50 | NÃO | fora da faixa vertical |
| 150 | 151.00 | 138.00 | 169.10 | 167.50 | NÃO | fora da faixa vertical |
| 151 | 151.00 | 139.00 | 168.12 | 166.50 | NÃO | fora da faixa vertical |
| 152 | 150.00 | 140.00 | 166.93 | 165.50 | NÃO | fora da faixa vertical |
| 153 | 149.00 | 141.00 | 165.74 | 164.50 | NÃO | fora da faixa vertical |
| 154 | 148.00 | 142.00 | 164.55 | 163.50 | NÃO | fora da faixa vertical |
| 155 | 148.00 | 143.00 | 163.57 | 162.50 | NÃO | fora da faixa vertical |
| 156 | 147.00 | 144.00 | 162.39 | 161.50 | NÃO | fora da faixa vertical |
| 157 | 146.00 | 145.00 | 161.21 | 160.50 | NÃO | fora da faixa vertical |
| 158 | 146.00 | 146.00 | 160.23 | 159.50 | NÃO | fora da faixa vertical |
| 159 | 145.00 | 147.00 | 159.05 | 158.50 | NÃO | fora da faixa vertical |
| 160 | 145.00 | 148.00 | 158.07 | 157.50 | NÃO | fora da faixa vertical |
| 161 | 144.00 | 149.00 | 156.89 | 156.50 | NÃO | fora da faixa vertical |
| 162 | 143.00 | 150.00 | 155.72 | 155.50 | NÃO | fora da faixa vertical |
| 163 | 143.00 | 151.00 | 154.74 | 154.50 | NÃO | fora da faixa vertical |
| 164 | 142.00 | 152.00 | 153.57 | 153.50 | NÃO | fora da faixa vertical |
| 165 | 141.00 | 153.00 | 152.41 | 152.50 | NÃO | fora da faixa vertical |
| 166 | 141.00 | 154.00 | 151.43 | 151.50 | NÃO | fora da faixa vertical |
| 167 | 140.00 | 155.00 | 150.27 | 150.50 | NÃO | fora da faixa vertical |
| 168 | 140.00 | 156.00 | 149.28 | 149.50 | NÃO | fora da faixa vertical |
| 169 | 139.00 | 157.00 | 148.12 | 148.50 | NÃO | fora da faixa vertical |
| 170 | 138.00 | 158.00 | 146.97 | 147.50 | NÃO | fora da faixa vertical |
| 171 | 138.00 | 159.00 | 145.99 | 146.50 | NÃO | fora da faixa vertical |
| 172 | 137.00 | 160.00 | 144.84 | 145.50 | NÃO | fora da faixa vertical |
| 173 | 137.00 | 161.00 | 143.85 | 144.50 | NÃO | fora da faixa vertical |
| 174 | 136.00 | 162.00 | 142.71 | 143.50 | NÃO | fora da faixa vertical |
| 175 | 136.00 | 163.00 | 141.72 | 142.50 | NÃO | fora da faixa vertical |
| 176 | 135.00 | 164.00 | 140.58 | 141.50 | NÃO | fora da faixa vertical |
| 177 | 135.00 | 165.00 | 139.59 | 140.50 | NÃO | fora da faixa vertical |
| 178 | 135.00 | 166.00 | 138.60 | 139.50 | NÃO | fora da faixa vertical |
| 179 | 134.00 | 167.00 | 137.46 | 138.50 | NÃO | fora da faixa vertical |
| 180 | 134.00 | 168.00 | 136.47 | 137.50 | NÃO | fora da faixa vertical |
| 181 | 133.00 | 169.00 | 135.34 | 136.50 | SIM | dentro da janela vertical e do lado solicitado |
| 182 | 133.00 | 170.00 | 134.35 | 135.50 | SIM | dentro da janela vertical e do lado solicitado |
| 183 | 132.00 | 171.00 | 133.22 | 134.50 | SIM | dentro da janela vertical e do lado solicitado |
| 184 | 132.00 | 172.00 | 132.23 | 133.50 | SIM | dentro da janela vertical e do lado solicitado |
| 185 | 131.00 | 173.00 | 131.11 | 132.50 | SIM | dentro da janela vertical e do lado solicitado |
| 186 | 131.00 | 174.00 | 130.12 | 131.50 | SIM | dentro da janela vertical e do lado solicitado |
| 187 | 130.00 | 175.00 | 129.00 | 130.50 | SIM | dentro da janela vertical e do lado solicitado |
| 188 | 130.00 | 176.00 | 128.00 | 129.50 | SIM | dentro da janela vertical e do lado solicitado |
| 189 | 129.00 | 177.00 | 126.89 | 128.50 | SIM | dentro da janela vertical e do lado solicitado |
| 190 | 129.00 | 178.00 | 125.90 | 127.50 | SIM | dentro da janela vertical e do lado solicitado |
| 191 | 129.00 | 179.00 | 124.90 | 126.50 | SIM | dentro da janela vertical e do lado solicitado |
| 192 | 128.00 | 180.00 | 123.79 | 125.50 | SIM | dentro da janela vertical e do lado solicitado |
| 193 | 128.00 | 181.00 | 122.80 | 124.50 | SIM | dentro da janela vertical e do lado solicitado |
| 194 | 127.00 | 182.00 | 121.70 | 123.50 | SIM | dentro da janela vertical e do lado solicitado |
| 195 | 127.00 | 183.00 | 120.70 | 122.50 | SIM | dentro da janela vertical e do lado solicitado |
| 196 | 127.00 | 184.00 | 119.71 | 121.50 | SIM | dentro da janela vertical e do lado solicitado |
| 197 | 126.00 | 185.00 | 118.61 | 120.50 | SIM | dentro da janela vertical e do lado solicitado |
| 198 | 126.00 | 186.00 | 117.61 | 119.50 | SIM | dentro da janela vertical e do lado solicitado |
| 199 | 126.00 | 187.00 | 116.62 | 118.50 | SIM | dentro da janela vertical e do lado solicitado |
| 200 | 125.00 | 188.00 | 115.52 | 117.50 | SIM | dentro da janela vertical e do lado solicitado |
| 201 | 125.00 | 189.00 | 114.53 | 116.50 | SIM | dentro da janela vertical e do lado solicitado |
| 202 | 124.00 | 190.00 | 113.44 | 115.50 | SIM | dentro da janela vertical e do lado solicitado |
| 203 | 124.00 | 191.00 | 112.45 | 114.50 | SIM | dentro da janela vertical e do lado solicitado |
| 204 | 124.00 | 192.00 | 111.45 | 113.50 | SIM | dentro da janela vertical e do lado solicitado |
| 205 | 124.00 | 193.00 | 110.45 | 112.50 | SIM | dentro da janela vertical e do lado solicitado |
| 206 | 123.00 | 194.00 | 109.37 | 111.50 | SIM | dentro da janela vertical e do lado solicitado |
| 207 | 123.00 | 195.00 | 108.37 | 110.50 | SIM | dentro da janela vertical e do lado solicitado |
| 208 | 123.00 | 196.00 | 107.38 | 109.50 | SIM | dentro da janela vertical e do lado solicitado |
| 209 | 122.00 | 197.00 | 106.30 | 108.50 | SIM | dentro da janela vertical e do lado solicitado |
| 210 | 122.00 | 198.00 | 105.30 | 107.50 | SIM | dentro da janela vertical e do lado solicitado |
| 211 | 122.00 | 199.00 | 104.31 | 106.50 | SIM | dentro da janela vertical e do lado solicitado |
| 212 | 122.00 | 200.00 | 103.31 | 105.50 | SIM | dentro da janela vertical e do lado solicitado |
| 213 | 121.00 | 201.00 | 102.24 | 104.50 | SIM | dentro da janela vertical e do lado solicitado |
| 214 | 121.00 | 202.00 | 101.24 | 103.50 | SIM | dentro da janela vertical e do lado solicitado |
| 215 | 121.00 | 203.00 | 100.24 | 102.50 | SIM | dentro da janela vertical e do lado solicitado |
| 216 | 120.00 | 204.00 | 99.18 | 101.50 | SIM | dentro da janela vertical e do lado solicitado |
| 217 | 120.00 | 205.00 | 98.18 | 100.50 | SIM | dentro da janela vertical e do lado solicitado |
| 218 | 120.00 | 206.00 | 97.19 | 99.50 | SIM | dentro da janela vertical e do lado solicitado |
| 219 | 120.00 | 207.00 | 96.19 | 98.50 | SIM | dentro da janela vertical e do lado solicitado |
| 220 | 119.00 | 208.00 | 95.13 | 97.50 | SIM | dentro da janela vertical e do lado solicitado |
| 221 | 119.00 | 209.00 | 94.13 | 96.50 | SIM | dentro da janela vertical e do lado solicitado |
| 222 | 119.00 | 210.00 | 93.13 | 95.50 | SIM | dentro da janela vertical e do lado solicitado |
| 223 | 119.00 | 211.00 | 92.14 | 94.50 | SIM | dentro da janela vertical e do lado solicitado |
| 224 | 119.00 | 212.00 | 91.14 | 93.50 | SIM | dentro da janela vertical e do lado solicitado |
| 225 | 118.00 | 213.00 | 90.09 | 92.50 | SIM | dentro da janela vertical e do lado solicitado |
| 226 | 118.00 | 214.00 | 89.09 | 91.50 | SIM | dentro da janela vertical e do lado solicitado |
| 227 | 118.00 | 215.00 | 88.09 | 90.50 | SIM | dentro da janela vertical e do lado solicitado |
| 228 | 118.00 | 216.00 | 87.09 | 89.50 | SIM | dentro da janela vertical e do lado solicitado |
| 229 | 118.00 | 217.00 | 86.09 | 88.50 | SIM | dentro da janela vertical e do lado solicitado |
| 230 | 117.00 | 218.00 | 85.05 | 87.50 | SIM | dentro da janela vertical e do lado solicitado |
| 231 | 117.00 | 219.00 | 84.05 | 86.50 | SIM | dentro da janela vertical e do lado solicitado |
| 232 | 117.00 | 220.00 | 83.05 | 85.50 | SIM | dentro da janela vertical e do lado solicitado |
| 233 | 117.00 | 221.00 | 82.05 | 84.50 | SIM | dentro da janela vertical e do lado solicitado |
| 234 | 117.00 | 222.00 | 81.06 | 83.50 | SIM | dentro da janela vertical e do lado solicitado |
| 235 | 116.00 | 223.00 | 80.02 | 82.50 | SIM | dentro da janela vertical e do lado solicitado |
| 236 | 116.00 | 224.00 | 79.03 | 81.50 | SIM | dentro da janela vertical e do lado solicitado |
| 237 | 116.00 | 225.00 | 78.03 | 80.50 | SIM | dentro da janela vertical e do lado solicitado |
| 238 | 116.00 | 226.00 | 77.03 | 79.50 | SIM | dentro da janela vertical e do lado solicitado |
| 239 | 116.00 | 227.00 | 76.03 | 78.50 | SIM | dentro da janela vertical e do lado solicitado |
| 240 | 116.00 | 228.00 | 75.03 | 77.50 | SIM | dentro da janela vertical e do lado solicitado |
| 241 | 116.00 | 229.00 | 74.03 | 76.50 | SIM | dentro da janela vertical e do lado solicitado |
| 242 | 116.00 | 230.00 | 73.03 | 75.50 | SIM | dentro da janela vertical e do lado solicitado |
| 243 | 115.00 | 231.00 | 72.01 | 74.50 | SIM | dentro da janela vertical e do lado solicitado |
| 244 | 115.00 | 232.00 | 71.01 | 73.50 | SIM | dentro da janela vertical e do lado solicitado |
| 245 | 115.00 | 233.00 | 70.01 | 72.50 | SIM | dentro da janela vertical e do lado solicitado |
| 246 | 115.00 | 234.00 | 69.01 | 71.50 | SIM | dentro da janela vertical e do lado solicitado |
| 247 | 115.00 | 235.00 | 68.01 | 70.50 | SIM | dentro da janela vertical e do lado solicitado |
| 248 | 115.00 | 236.00 | 67.01 | 69.50 | SIM | dentro da janela vertical e do lado solicitado |
| 249 | 115.00 | 237.00 | 66.01 | 68.50 | SIM | dentro da janela vertical e do lado solicitado |
| 250 | 115.00 | 238.00 | 65.01 | 67.50 | SIM | dentro da janela vertical e do lado solicitado |
| 251 | 115.00 | 239.00 | 64.01 | 66.50 | SIM | dentro da janela vertical e do lado solicitado |
| 252 | 114.00 | 240.00 | 63.00 | 65.50 | SIM | dentro da janela vertical e do lado solicitado |
| 253 | 114.00 | 241.00 | 62.00 | 64.50 | SIM | dentro da janela vertical e do lado solicitado |
| 254 | 114.00 | 242.00 | 61.00 | 63.50 | SIM | dentro da janela vertical e do lado solicitado |
| 255 | 114.00 | 243.00 | 60.00 | 62.50 | SIM | dentro da janela vertical e do lado solicitado |
| 256 | 114.00 | 244.00 | 59.00 | 61.50 | SIM | dentro da janela vertical e do lado solicitado |
| 257 | 114.00 | 245.00 | 58.00 | 60.50 | SIM | dentro da janela vertical e do lado solicitado |
| 258 | 114.00 | 246.00 | 57.00 | 59.50 | SIM | dentro da janela vertical e do lado solicitado |
| 259 | 114.00 | 247.00 | 56.00 | 58.50 | SIM | dentro da janela vertical e do lado solicitado |
| 260 | 114.00 | 248.00 | 55.00 | 57.50 | SIM | dentro da janela vertical e do lado solicitado |
| 261 | 114.00 | 249.00 | 54.00 | 56.50 | SIM | dentro da janela vertical e do lado solicitado |
| 262 | 114.00 | 250.00 | 53.00 | 55.50 | SIM | dentro da janela vertical e do lado solicitado |
| 263 | 114.00 | 251.00 | 52.00 | 54.50 | SIM | dentro da janela vertical e do lado solicitado |
| 264 | 114.00 | 252.00 | 51.00 | 53.50 | SIM | dentro da janela vertical e do lado solicitado |
| 265 | 114.00 | 253.00 | 50.00 | 52.50 | SIM | dentro da janela vertical e do lado solicitado |
| 266 | 114.00 | 254.00 | 49.00 | 51.50 | SIM | dentro da janela vertical e do lado solicitado |
| 267 | 114.00 | 255.00 | 48.00 | 50.50 | SIM | dentro da janela vertical e do lado solicitado |
| 268 | 114.00 | 256.00 | 47.00 | 49.50 | SIM | dentro da janela vertical e do lado solicitado |
| 269 | 114.00 | 257.00 | 46.00 | 48.50 | SIM | dentro da janela vertical e do lado solicitado |
| 270 | 114.00 | 258.00 | 45.00 | 47.50 | SIM | dentro da janela vertical e do lado solicitado |
| 271 | 114.00 | 259.00 | 44.00 | 46.50 | SIM | dentro da janela vertical e do lado solicitado |
| 272 | 114.00 | 260.00 | 43.00 | 45.50 | SIM | dentro da janela vertical e do lado solicitado |
| 273 | 114.00 | 261.00 | 42.00 | 44.50 | SIM | dentro da janela vertical e do lado solicitado |
| 274 | 114.00 | 262.00 | 41.00 | 43.50 | SIM | dentro da janela vertical e do lado solicitado |
| 275 | 114.00 | 263.00 | 40.00 | 42.50 | SIM | dentro da janela vertical e do lado solicitado |
| 276 | 114.00 | 264.00 | 39.00 | 41.50 | SIM | dentro da janela vertical e do lado solicitado |
| 277 | 114.00 | 265.00 | 38.00 | 40.50 | SIM | dentro da janela vertical e do lado solicitado |
| 278 | 114.00 | 266.00 | 37.00 | 39.50 | SIM | dentro da janela vertical e do lado solicitado |
| 279 | 114.00 | 267.00 | 36.00 | 38.50 | SIM | dentro da janela vertical e do lado solicitado |
| 280 | 114.00 | 268.00 | 35.00 | 37.50 | SIM | dentro da janela vertical e do lado solicitado |
| 281 | 114.00 | 269.00 | 34.00 | 36.50 | SIM | dentro da janela vertical e do lado solicitado |
| 282 | 114.00 | 270.00 | 33.00 | 35.50 | SIM | dentro da janela vertical e do lado solicitado |
| 283 | 114.00 | 271.00 | 32.00 | 34.50 | SIM | dentro da janela vertical e do lado solicitado |
| 284 | 115.00 | 272.00 | 31.02 | 33.50 | SIM | dentro da janela vertical e do lado solicitado |
| 285 | 115.00 | 273.00 | 30.02 | 32.50 | SIM | dentro da janela vertical e do lado solicitado |
| 286 | 115.00 | 274.00 | 29.02 | 31.50 | SIM | dentro da janela vertical e do lado solicitado |
| 287 | 115.00 | 275.00 | 28.02 | 30.50 | SIM | dentro da janela vertical e do lado solicitado |
| 288 | 115.00 | 276.00 | 27.02 | 29.50 | SIM | dentro da janela vertical e do lado solicitado |
| 289 | 115.00 | 277.00 | 26.02 | 28.50 | SIM | dentro da janela vertical e do lado solicitado |
| 290 | 115.00 | 278.00 | 25.02 | 27.50 | SIM | dentro da janela vertical e do lado solicitado |
| 291 | 115.00 | 279.00 | 24.02 | 26.50 | SIM | dentro da janela vertical e do lado solicitado |
| 292 | 116.00 | 280.00 | 23.09 | 25.50 | SIM | dentro da janela vertical e do lado solicitado |
| 293 | 116.00 | 281.00 | 22.09 | 24.50 | SIM | dentro da janela vertical e do lado solicitado |
| 294 | 116.00 | 282.00 | 21.10 | 23.50 | SIM | dentro da janela vertical e do lado solicitado |
| 295 | 116.00 | 283.00 | 20.10 | 22.50 | SIM | dentro da janela vertical e do lado solicitado |
| 296 | 116.00 | 284.00 | 19.10 | 21.50 | SIM | dentro da janela vertical e do lado solicitado |
| 297 | 116.00 | 285.00 | 18.11 | 20.50 | SIM | dentro da janela vertical e do lado solicitado |
| 298 | 116.00 | 286.00 | 17.12 | 19.50 | SIM | dentro da janela vertical e do lado solicitado |
| 299 | 116.00 | 287.00 | 16.12 | 18.50 | SIM | dentro da janela vertical e do lado solicitado |
| 300 | 117.00 | 288.00 | 15.30 | 17.50 | SIM | dentro da janela vertical e do lado solicitado |
| 301 | 117.00 | 289.00 | 14.32 | 16.50 | SIM | dentro da janela vertical e do lado solicitado |
| 302 | 117.00 | 290.00 | 13.34 | 15.50 | SIM | dentro da janela vertical e do lado solicitado |
| 303 | 117.00 | 291.00 | 12.37 | 14.50 | SIM | dentro da janela vertical e do lado solicitado |
| 304 | 117.00 | 292.00 | 11.40 | 13.50 | SIM | dentro da janela vertical e do lado solicitado |
| 305 | 118.00 | 293.00 | 10.77 | 12.50 | SIM | dentro da janela vertical e do lado solicitado |
| 306 | 118.00 | 294.00 | 9.85 | 11.50 | SIM | dentro da janela vertical e do lado solicitado |
| 307 | 118.00 | 295.00 | 8.94 | 10.50 | SIM | dentro da janela vertical e do lado solicitado |
| 308 | 118.00 | 296.00 | 8.06 | 9.50 | SIM | dentro da janela vertical e do lado solicitado |
| 309 | 118.00 | 297.00 | 7.21 | 8.50 | SIM | dentro da janela vertical e do lado solicitado |
| 310 | 119.00 | 298.00 | 7.07 | 7.50 | SIM | dentro da janela vertical e do lado solicitado |
| 311 | 119.00 | 299.00 | 6.40 | 6.50 | SIM | dentro da janela vertical e do lado solicitado |
| 312 | 119.00 | 300.00 | 5.83 | 5.50 | SIM | dentro da janela vertical e do lado solicitado |
| 313 | 119.00 | 301.00 | 5.39 | 4.50 | SIM | dentro da janela vertical e do lado solicitado |
| 314 | 119.00 | 302.00 | 5.10 | 3.50 | SIM | dentro da janela vertical e do lado solicitado |
| 315 | 120.00 | 303.00 | 6.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 316 | 121.00 | 303.00 | 7.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 317 | 122.00 | 303.00 | 8.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 318 | 123.00 | 303.00 | 9.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 319 | 124.00 | 303.00 | 10.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 320 | 125.00 | 303.00 | 11.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 321 | 126.00 | 303.00 | 12.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 322 | 127.00 | 303.00 | 13.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 323 | 128.00 | 303.00 | 14.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 324 | 129.00 | 303.00 | 15.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 325 | 130.00 | 303.00 | 16.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 326 | 131.00 | 303.00 | 17.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 327 | 132.00 | 303.00 | 18.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 328 | 133.00 | 303.00 | 19.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 329 | 134.00 | 303.00 | 20.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 330 | 135.00 | 303.00 | 21.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 331 | 136.00 | 303.00 | 22.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 332 | 137.00 | 303.00 | 23.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 333 | 138.00 | 303.00 | 24.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 334 | 139.00 | 303.00 | 25.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 335 | 140.00 | 303.00 | 26.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 336 | 141.00 | 303.00 | 27.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 337 | 142.00 | 303.00 | 28.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 338 | 143.00 | 303.00 | 29.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 339 | 144.00 | 303.00 | 30.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 340 | 145.00 | 303.00 | 31.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 341 | 146.00 | 303.00 | 32.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 342 | 147.00 | 303.00 | 33.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 343 | 148.00 | 303.00 | 34.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 344 | 149.00 | 303.00 | 35.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 345 | 150.00 | 303.00 | 36.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 346 | 151.00 | 303.00 | 37.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 347 | 152.00 | 303.00 | 38.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 348 | 153.00 | 303.00 | 39.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 349 | 154.00 | 303.00 | 40.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 350 | 155.00 | 303.00 | 41.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 351 | 156.00 | 303.00 | 42.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 352 | 157.00 | 303.00 | 43.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 353 | 158.00 | 303.00 | 44.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 354 | 159.00 | 303.00 | 45.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 355 | 160.00 | 303.00 | 46.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 356 | 161.00 | 303.00 | 47.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 357 | 162.00 | 303.00 | 48.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 358 | 163.00 | 303.00 | 49.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 359 | 164.00 | 303.00 | 50.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 360 | 165.00 | 303.00 | 51.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 361 | 166.00 | 303.00 | 52.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 362 | 167.00 | 303.00 | 53.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 363 | 168.00 | 303.00 | 54.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 364 | 169.00 | 303.00 | 55.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 365 | 170.00 | 303.00 | 56.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 366 | 171.00 | 303.00 | 57.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 367 | 172.00 | 303.00 | 58.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 368 | 173.00 | 303.00 | 59.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 369 | 174.00 | 303.00 | 60.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 370 | 175.00 | 303.00 | 61.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 371 | 176.00 | 303.00 | 62.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 372 | 177.00 | 303.00 | 63.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 373 | 178.00 | 303.00 | 64.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 374 | 179.00 | 303.00 | 65.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 375 | 180.00 | 303.00 | 66.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 376 | 181.00 | 303.00 | 67.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 377 | 182.00 | 303.00 | 68.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 378 | 183.00 | 303.00 | 69.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 379 | 184.00 | 303.00 | 70.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 380 | 185.00 | 303.00 | 71.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 381 | 186.00 | 303.00 | 72.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 382 | 187.00 | 303.00 | 73.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 383 | 188.00 | 303.00 | 74.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 384 | 189.00 | 303.00 | 75.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 385 | 190.00 | 303.00 | 76.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 386 | 191.00 | 303.00 | 77.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 387 | 192.00 | 303.00 | 78.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 388 | 193.00 | 303.00 | 79.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 389 | 194.00 | 303.00 | 80.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 390 | 195.00 | 303.00 | 81.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 391 | 196.00 | 303.00 | 82.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 392 | 197.00 | 303.00 | 83.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 393 | 198.00 | 303.00 | 84.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 394 | 199.00 | 303.00 | 85.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 395 | 200.00 | 303.00 | 86.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 396 | 201.00 | 303.00 | 87.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 397 | 202.00 | 303.00 | 88.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 398 | 203.00 | 303.00 | 89.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 399 | 204.00 | 303.00 | 90.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 400 | 205.00 | 303.00 | 91.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 401 | 206.00 | 303.00 | 92.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 402 | 207.00 | 303.00 | 93.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 403 | 208.00 | 303.00 | 94.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 404 | 209.00 | 303.00 | 95.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 405 | 210.00 | 303.00 | 96.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 406 | 211.00 | 303.00 | 97.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 407 | 212.00 | 303.00 | 98.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 408 | 213.00 | 303.00 | 99.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 409 | 214.00 | 303.00 | 100.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 410 | 215.00 | 303.00 | 101.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 411 | 216.00 | 303.00 | 102.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 412 | 217.00 | 303.00 | 103.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 413 | 218.00 | 303.00 | 104.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 414 | 219.00 | 303.00 | 105.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 415 | 220.00 | 303.00 | 106.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 416 | 221.00 | 303.00 | 107.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 417 | 222.00 | 303.00 | 108.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 418 | 223.00 | 303.00 | 109.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 419 | 224.00 | 303.00 | 110.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 420 | 225.00 | 303.00 | 111.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 421 | 226.00 | 303.00 | 112.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 422 | 227.00 | 303.00 | 113.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 423 | 228.00 | 303.00 | 114.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 424 | 229.00 | 303.00 | 115.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 425 | 230.00 | 303.00 | 116.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 426 | 231.00 | 303.00 | 117.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 427 | 232.00 | 303.00 | 118.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 428 | 233.00 | 303.00 | 119.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 429 | 234.00 | 303.00 | 120.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 430 | 235.00 | 303.00 | 121.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 431 | 236.00 | 303.00 | 122.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 432 | 237.00 | 303.00 | 123.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 433 | 238.00 | 303.00 | 124.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 434 | 239.00 | 303.00 | 125.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 435 | 240.00 | 303.00 | 126.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 436 | 241.00 | 303.00 | 127.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 437 | 242.00 | 303.00 | 128.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 438 | 243.00 | 303.00 | 129.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 439 | 244.00 | 303.00 | 130.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 440 | 245.00 | 303.00 | 131.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 441 | 246.00 | 303.00 | 132.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 442 | 247.00 | 303.00 | 133.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 443 | 248.00 | 303.00 | 134.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 444 | 249.00 | 303.00 | 135.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 445 | 250.00 | 303.00 | 136.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 446 | 251.00 | 303.00 | 137.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 447 | 252.00 | 303.00 | 138.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 448 | 253.00 | 303.00 | 139.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 449 | 254.00 | 303.00 | 140.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 450 | 255.00 | 303.00 | 141.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 451 | 256.00 | 303.00 | 142.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 452 | 257.00 | 303.00 | 143.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 453 | 258.00 | 303.00 | 144.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 454 | 259.00 | 303.00 | 145.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 455 | 260.00 | 303.00 | 146.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 456 | 261.00 | 303.00 | 147.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 457 | 262.00 | 303.00 | 148.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 458 | 263.00 | 303.00 | 149.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 459 | 264.00 | 303.00 | 150.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 460 | 265.00 | 303.00 | 151.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 461 | 266.00 | 303.00 | 152.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 462 | 267.00 | 303.00 | 153.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 463 | 268.00 | 303.00 | 154.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 464 | 269.00 | 303.00 | 155.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 465 | 270.00 | 303.00 | 156.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 466 | 271.00 | 303.00 | 157.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 467 | 272.00 | 303.00 | 158.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 468 | 273.00 | 303.00 | 159.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 469 | 274.00 | 303.00 | 160.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 470 | 275.00 | 303.00 | 161.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 471 | 276.00 | 303.00 | 162.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 472 | 277.00 | 303.00 | 163.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 473 | 278.00 | 303.00 | 164.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 474 | 279.00 | 303.00 | 165.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 475 | 280.00 | 303.00 | 166.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 476 | 281.00 | 303.00 | 167.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 477 | 282.00 | 303.00 | 168.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 478 | 283.00 | 303.00 | 169.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 479 | 284.00 | 303.00 | 170.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 480 | 285.00 | 303.00 | 171.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 481 | 286.00 | 303.00 | 172.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 482 | 287.00 | 303.00 | 173.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 483 | 288.00 | 303.00 | 174.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 484 | 289.00 | 303.00 | 175.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 485 | 290.00 | 303.00 | 176.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 486 | 291.00 | 303.00 | 177.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 487 | 292.00 | 303.00 | 178.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 488 | 293.00 | 303.00 | 179.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 489 | 294.00 | 303.00 | 180.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 490 | 295.00 | 303.00 | 181.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 491 | 296.00 | 303.00 | 182.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 492 | 297.00 | 303.00 | 183.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 493 | 298.00 | 303.00 | 184.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 494 | 299.00 | 303.00 | 185.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 495 | 300.00 | 303.00 | 186.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 496 | 301.00 | 303.00 | 187.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 497 | 302.00 | 303.00 | 188.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 498 | 303.00 | 303.00 | 189.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 499 | 304.00 | 303.00 | 190.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 500 | 305.00 | 303.00 | 191.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 501 | 306.00 | 303.00 | 192.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 502 | 307.00 | 303.00 | 193.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 503 | 308.00 | 303.00 | 194.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 504 | 309.00 | 303.00 | 195.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 505 | 310.00 | 303.00 | 196.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 506 | 311.00 | 303.00 | 197.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 507 | 312.00 | 303.00 | 198.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 508 | 313.00 | 303.00 | 199.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 509 | 314.00 | 303.00 | 200.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 510 | 315.00 | 303.00 | 201.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 511 | 316.00 | 303.00 | 202.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 512 | 317.00 | 303.00 | 203.00 | 2.50 | NÃO | fora do lado solicitado |
| 513 | 318.00 | 303.00 | 204.00 | 2.50 | NÃO | fora do lado solicitado |
| 514 | 319.00 | 303.00 | 205.00 | 2.50 | NÃO | fora do lado solicitado |
| 515 | 320.00 | 303.00 | 206.00 | 2.50 | NÃO | fora do lado solicitado |
| 516 | 321.00 | 303.00 | 207.00 | 2.50 | NÃO | fora do lado solicitado |
| 517 | 322.00 | 303.00 | 208.00 | 2.50 | NÃO | fora do lado solicitado |
| 518 | 323.00 | 303.00 | 209.00 | 2.50 | NÃO | fora do lado solicitado |
| 519 | 324.00 | 303.00 | 210.00 | 2.50 | NÃO | fora do lado solicitado |
| 520 | 325.00 | 303.00 | 211.00 | 2.50 | NÃO | fora do lado solicitado |
| 521 | 326.00 | 303.00 | 212.00 | 2.50 | NÃO | fora do lado solicitado |
| 522 | 327.00 | 303.00 | 213.00 | 2.50 | NÃO | fora do lado solicitado |
| 523 | 328.00 | 303.00 | 214.00 | 2.50 | NÃO | fora do lado solicitado |
| 524 | 329.00 | 303.00 | 215.00 | 2.50 | NÃO | fora do lado solicitado |
| 525 | 330.00 | 303.00 | 216.00 | 2.50 | NÃO | fora do lado solicitado |
| 526 | 331.00 | 303.00 | 217.00 | 2.50 | NÃO | fora do lado solicitado |
| 527 | 332.00 | 303.00 | 218.00 | 2.50 | NÃO | fora do lado solicitado |
| 528 | 333.00 | 303.00 | 219.00 | 2.50 | NÃO | fora do lado solicitado |
| 529 | 334.00 | 303.00 | 220.00 | 2.50 | NÃO | fora do lado solicitado |
| 530 | 335.00 | 303.00 | 221.00 | 2.50 | NÃO | fora do lado solicitado |
| 531 | 336.00 | 303.00 | 222.00 | 2.50 | NÃO | fora do lado solicitado |
| 532 | 337.00 | 303.00 | 223.00 | 2.50 | NÃO | fora do lado solicitado |
| 533 | 338.00 | 303.00 | 224.00 | 2.50 | NÃO | fora do lado solicitado |
| 534 | 339.00 | 303.00 | 225.00 | 2.50 | NÃO | fora do lado solicitado |
| 535 | 340.00 | 303.00 | 226.00 | 2.50 | NÃO | fora do lado solicitado |
| 536 | 341.00 | 303.00 | 227.00 | 2.50 | NÃO | fora do lado solicitado |
| 537 | 342.00 | 303.00 | 228.00 | 2.50 | NÃO | fora do lado solicitado |
| 538 | 343.00 | 303.00 | 229.00 | 2.50 | NÃO | fora do lado solicitado |
| 539 | 344.00 | 303.00 | 230.00 | 2.50 | NÃO | fora do lado solicitado |
| 540 | 345.00 | 303.00 | 231.00 | 2.50 | NÃO | fora do lado solicitado |
| 541 | 346.00 | 303.00 | 232.00 | 2.50 | NÃO | fora do lado solicitado |
| 542 | 347.00 | 303.00 | 233.00 | 2.50 | NÃO | fora do lado solicitado |
| 543 | 348.00 | 303.00 | 234.00 | 2.50 | NÃO | fora do lado solicitado |
| 544 | 349.00 | 303.00 | 235.00 | 2.50 | NÃO | fora do lado solicitado |
| 545 | 350.00 | 303.00 | 236.00 | 2.50 | NÃO | fora do lado solicitado |
| 546 | 351.00 | 303.00 | 237.00 | 2.50 | NÃO | fora do lado solicitado |
| 547 | 352.00 | 303.00 | 238.00 | 2.50 | NÃO | fora do lado solicitado |
| 548 | 353.00 | 303.00 | 239.00 | 2.50 | NÃO | fora do lado solicitado |
| 549 | 354.00 | 303.00 | 240.00 | 2.50 | NÃO | fora do lado solicitado |
| 550 | 355.00 | 303.00 | 241.00 | 2.50 | NÃO | fora do lado solicitado |
| 551 | 356.00 | 303.00 | 242.00 | 2.50 | NÃO | fora do lado solicitado |
| 552 | 357.00 | 303.00 | 243.00 | 2.50 | NÃO | fora do lado solicitado |
| 553 | 358.00 | 303.00 | 244.00 | 2.50 | NÃO | fora do lado solicitado |
| 554 | 359.00 | 303.00 | 245.00 | 2.50 | NÃO | fora do lado solicitado |
| 555 | 360.00 | 303.00 | 246.00 | 2.50 | NÃO | fora do lado solicitado |
| 556 | 361.00 | 303.00 | 247.00 | 2.50 | NÃO | fora do lado solicitado |
| 557 | 362.00 | 303.00 | 248.00 | 2.50 | NÃO | fora do lado solicitado |
| 558 | 363.00 | 303.00 | 249.00 | 2.50 | NÃO | fora do lado solicitado |
| 559 | 364.00 | 303.00 | 250.00 | 2.50 | NÃO | fora do lado solicitado |
| 560 | 365.00 | 303.00 | 251.00 | 2.50 | NÃO | fora do lado solicitado |
| 561 | 366.00 | 303.00 | 252.00 | 2.50 | NÃO | fora do lado solicitado |
| 562 | 367.00 | 303.00 | 253.00 | 2.50 | NÃO | fora do lado solicitado |
| 563 | 368.00 | 303.00 | 254.00 | 2.50 | NÃO | fora do lado solicitado |
| 564 | 369.00 | 303.00 | 255.00 | 2.50 | NÃO | fora do lado solicitado |
| 565 | 370.00 | 303.00 | 256.00 | 2.50 | NÃO | fora do lado solicitado |
| 566 | 371.00 | 303.00 | 257.00 | 2.50 | NÃO | fora do lado solicitado |
| 567 | 372.00 | 303.00 | 258.00 | 2.50 | NÃO | fora do lado solicitado |
| 568 | 373.00 | 303.00 | 259.00 | 2.50 | NÃO | fora do lado solicitado |
| 569 | 374.00 | 303.00 | 260.00 | 2.50 | NÃO | fora do lado solicitado |
| 570 | 375.00 | 303.00 | 261.00 | 2.50 | NÃO | fora do lado solicitado |
| 571 | 376.00 | 303.00 | 262.00 | 2.50 | NÃO | fora do lado solicitado |
| 572 | 377.00 | 303.00 | 263.00 | 2.50 | NÃO | fora do lado solicitado |
| 573 | 378.00 | 303.00 | 264.00 | 2.50 | NÃO | fora do lado solicitado |
| 574 | 379.00 | 303.00 | 265.00 | 2.50 | NÃO | fora do lado solicitado |
| 575 | 380.00 | 303.00 | 266.00 | 2.50 | NÃO | fora do lado solicitado |
| 576 | 381.00 | 303.00 | 267.00 | 2.50 | NÃO | fora do lado solicitado |
| 577 | 382.00 | 303.00 | 268.00 | 2.50 | NÃO | fora do lado solicitado |
| 578 | 383.00 | 303.00 | 269.00 | 2.50 | NÃO | fora do lado solicitado |
| 579 | 384.00 | 303.00 | 270.00 | 2.50 | NÃO | fora do lado solicitado |
| 580 | 385.00 | 303.00 | 271.00 | 2.50 | NÃO | fora do lado solicitado |
| 581 | 386.00 | 303.00 | 272.00 | 2.50 | NÃO | fora do lado solicitado |
| 582 | 387.00 | 303.00 | 273.00 | 2.50 | NÃO | fora do lado solicitado |
| 583 | 388.00 | 303.00 | 274.00 | 2.50 | NÃO | fora do lado solicitado |
| 584 | 389.00 | 303.00 | 275.00 | 2.50 | NÃO | fora do lado solicitado |
| 585 | 390.00 | 303.00 | 276.00 | 2.50 | NÃO | fora do lado solicitado |
| 586 | 391.00 | 303.00 | 277.00 | 2.50 | NÃO | fora do lado solicitado |
| 587 | 392.00 | 303.00 | 278.00 | 2.50 | NÃO | fora do lado solicitado |
| 588 | 393.00 | 303.00 | 279.00 | 2.50 | NÃO | fora do lado solicitado |
| 589 | 394.00 | 303.00 | 280.00 | 2.50 | NÃO | fora do lado solicitado |
| 590 | 395.00 | 303.00 | 281.00 | 2.50 | NÃO | fora do lado solicitado |
| 591 | 396.00 | 303.00 | 282.00 | 2.50 | NÃO | fora do lado solicitado |
| 592 | 397.00 | 303.00 | 283.00 | 2.50 | NÃO | fora do lado solicitado |
| 593 | 398.00 | 303.00 | 284.00 | 2.50 | NÃO | fora do lado solicitado |
| 594 | 399.00 | 303.00 | 285.00 | 2.50 | NÃO | fora do lado solicitado |
| 595 | 400.00 | 303.00 | 286.00 | 2.50 | NÃO | fora do lado solicitado |
| 596 | 401.00 | 303.00 | 287.00 | 2.50 | NÃO | fora do lado solicitado |
| 597 | 402.00 | 303.00 | 288.00 | 2.50 | NÃO | fora do lado solicitado |
| 598 | 403.00 | 303.00 | 289.00 | 2.50 | NÃO | fora do lado solicitado |
| 599 | 404.00 | 303.00 | 290.00 | 2.50 | NÃO | fora do lado solicitado |
| 600 | 405.00 | 303.00 | 291.00 | 2.50 | NÃO | fora do lado solicitado |
| 601 | 406.00 | 303.00 | 292.00 | 2.50 | NÃO | fora do lado solicitado |
| 602 | 407.00 | 303.00 | 293.00 | 2.50 | NÃO | fora do lado solicitado |
| 603 | 408.00 | 303.00 | 294.00 | 2.50 | NÃO | fora do lado solicitado |
| 604 | 409.00 | 303.00 | 295.00 | 2.50 | NÃO | fora do lado solicitado |
| 605 | 410.00 | 303.00 | 296.00 | 2.50 | NÃO | fora do lado solicitado |
| 606 | 411.00 | 303.00 | 297.00 | 2.50 | NÃO | fora do lado solicitado |
| 607 | 412.00 | 303.00 | 298.00 | 2.50 | NÃO | fora do lado solicitado |
| 608 | 413.00 | 303.00 | 299.00 | 2.50 | NÃO | fora do lado solicitado |
| 609 | 414.00 | 303.00 | 300.00 | 2.50 | NÃO | fora do lado solicitado |
| 610 | 415.00 | 303.00 | 301.00 | 2.50 | NÃO | fora do lado solicitado |
| 611 | 416.00 | 303.00 | 302.00 | 2.50 | NÃO | fora do lado solicitado |
| 612 | 417.00 | 303.00 | 303.00 | 2.50 | NÃO | fora do lado solicitado |
| 613 | 418.00 | 303.00 | 304.00 | 2.50 | NÃO | fora do lado solicitado |
| 614 | 419.00 | 303.00 | 305.00 | 2.50 | NÃO | fora do lado solicitado |
| 615 | 420.00 | 303.00 | 306.00 | 2.50 | NÃO | fora do lado solicitado |
| 616 | 421.00 | 303.00 | 307.00 | 2.50 | NÃO | fora do lado solicitado |
| 617 | 422.00 | 303.00 | 308.00 | 2.50 | NÃO | fora do lado solicitado |
| 618 | 423.00 | 303.00 | 309.00 | 2.50 | NÃO | fora do lado solicitado |
| 619 | 424.00 | 303.00 | 310.00 | 2.50 | NÃO | fora do lado solicitado |
| 620 | 425.00 | 303.00 | 311.00 | 2.50 | NÃO | fora do lado solicitado |
| 621 | 426.00 | 303.00 | 312.00 | 2.50 | NÃO | fora do lado solicitado |
| 622 | 427.00 | 303.00 | 313.00 | 2.50 | NÃO | fora do lado solicitado |
| 623 | 428.00 | 303.00 | 314.00 | 2.50 | NÃO | fora do lado solicitado |
| 624 | 429.00 | 303.00 | 315.00 | 2.50 | NÃO | fora do lado solicitado |
| 625 | 430.00 | 303.00 | 316.00 | 2.50 | NÃO | fora do lado solicitado |
| 626 | 431.00 | 303.00 | 317.00 | 2.50 | NÃO | fora do lado solicitado |
| 627 | 432.00 | 303.00 | 318.00 | 2.50 | NÃO | fora do lado solicitado |
| 628 | 433.00 | 303.00 | 319.00 | 2.50 | NÃO | fora do lado solicitado |
| 629 | 434.00 | 303.00 | 320.00 | 2.50 | NÃO | fora do lado solicitado |
| 630 | 435.00 | 303.00 | 321.00 | 2.50 | NÃO | fora do lado solicitado |
| 631 | 436.00 | 303.00 | 322.00 | 2.50 | NÃO | fora do lado solicitado |
| 632 | 437.00 | 303.00 | 323.00 | 2.50 | NÃO | fora do lado solicitado |
| 633 | 438.00 | 303.00 | 324.00 | 2.50 | NÃO | fora do lado solicitado |
| 634 | 439.00 | 303.00 | 325.00 | 2.50 | NÃO | fora do lado solicitado |
| 635 | 440.00 | 303.00 | 326.00 | 2.50 | NÃO | fora do lado solicitado |
| 636 | 441.00 | 303.00 | 327.00 | 2.50 | NÃO | fora do lado solicitado |
| 637 | 442.00 | 303.00 | 328.00 | 2.50 | NÃO | fora do lado solicitado |
| 638 | 443.00 | 303.00 | 329.00 | 2.50 | NÃO | fora do lado solicitado |
| 639 | 444.00 | 303.00 | 330.00 | 2.50 | NÃO | fora do lado solicitado |
| 640 | 445.00 | 303.00 | 331.00 | 2.50 | NÃO | fora do lado solicitado |
| 641 | 446.00 | 303.00 | 332.00 | 2.50 | NÃO | fora do lado solicitado |
| 642 | 447.00 | 303.00 | 333.00 | 2.50 | NÃO | fora do lado solicitado |
| 643 | 448.00 | 303.00 | 334.00 | 2.50 | NÃO | fora do lado solicitado |
| 644 | 449.00 | 303.00 | 335.00 | 2.50 | NÃO | fora do lado solicitado |
| 645 | 450.00 | 303.00 | 336.00 | 2.50 | NÃO | fora do lado solicitado |
| 646 | 451.00 | 303.00 | 337.00 | 2.50 | NÃO | fora do lado solicitado |
| 647 | 452.00 | 303.00 | 338.00 | 2.50 | NÃO | fora do lado solicitado |
| 648 | 453.00 | 303.00 | 339.00 | 2.50 | NÃO | fora do lado solicitado |
| 649 | 454.00 | 303.00 | 340.00 | 2.50 | NÃO | fora do lado solicitado |
| 650 | 455.00 | 303.00 | 341.00 | 2.50 | NÃO | fora do lado solicitado |
| 651 | 456.00 | 303.00 | 342.00 | 2.50 | NÃO | fora do lado solicitado |
| 652 | 457.00 | 303.00 | 343.00 | 2.50 | NÃO | fora do lado solicitado |
| 653 | 458.00 | 303.00 | 344.00 | 2.50 | NÃO | fora do lado solicitado |
| 654 | 459.00 | 303.00 | 345.00 | 2.50 | NÃO | fora do lado solicitado |
| 655 | 460.00 | 303.00 | 346.00 | 2.50 | NÃO | fora do lado solicitado |
| 656 | 461.00 | 303.00 | 347.00 | 2.50 | NÃO | fora do lado solicitado |
| 657 | 462.00 | 303.00 | 348.00 | 2.50 | NÃO | fora do lado solicitado |
| 658 | 463.00 | 303.00 | 349.00 | 2.50 | NÃO | fora do lado solicitado |
| 659 | 464.00 | 303.00 | 350.00 | 2.50 | NÃO | fora do lado solicitado |
| 660 | 465.00 | 303.00 | 351.00 | 2.50 | NÃO | fora do lado solicitado |
| 661 | 466.00 | 303.00 | 352.00 | 2.50 | NÃO | fora do lado solicitado |
| 662 | 467.00 | 303.00 | 353.00 | 2.50 | NÃO | fora do lado solicitado |
| 663 | 468.00 | 303.00 | 354.00 | 2.50 | NÃO | fora do lado solicitado |
| 664 | 469.00 | 303.00 | 355.00 | 2.50 | NÃO | fora do lado solicitado |
| 665 | 470.00 | 303.00 | 356.00 | 2.50 | NÃO | fora do lado solicitado |
| 666 | 471.00 | 303.00 | 357.00 | 2.50 | NÃO | fora do lado solicitado |
| 667 | 472.00 | 303.00 | 358.00 | 2.50 | NÃO | fora do lado solicitado |
| 668 | 473.00 | 303.00 | 359.00 | 2.50 | NÃO | fora do lado solicitado |
| 669 | 474.00 | 303.00 | 360.00 | 2.50 | NÃO | fora do lado solicitado |
| 670 | 475.00 | 303.00 | 361.00 | 2.50 | NÃO | fora do lado solicitado |
| 671 | 476.00 | 303.00 | 362.00 | 2.50 | NÃO | fora do lado solicitado |
| 672 | 477.00 | 303.00 | 363.00 | 2.50 | NÃO | fora do lado solicitado |
| 673 | 478.00 | 303.00 | 364.00 | 2.50 | NÃO | fora do lado solicitado |
| 674 | 479.00 | 303.00 | 365.00 | 2.50 | NÃO | fora do lado solicitado |
| 675 | 480.00 | 303.00 | 366.00 | 2.50 | NÃO | fora do lado solicitado |
| 676 | 481.00 | 303.00 | 367.00 | 2.50 | NÃO | fora do lado solicitado |
| 677 | 482.00 | 303.00 | 368.00 | 2.50 | NÃO | fora do lado solicitado |
| 678 | 483.00 | 303.00 | 369.00 | 2.50 | NÃO | fora do lado solicitado |
| 679 | 484.00 | 303.00 | 370.00 | 2.50 | NÃO | fora do lado solicitado |
| 680 | 485.00 | 303.00 | 371.00 | 2.50 | NÃO | fora do lado solicitado |
| 681 | 486.00 | 303.00 | 372.00 | 2.50 | NÃO | fora do lado solicitado |
| 682 | 487.00 | 303.00 | 373.00 | 2.50 | NÃO | fora do lado solicitado |
| 683 | 488.00 | 303.00 | 374.00 | 2.50 | NÃO | fora do lado solicitado |
| 684 | 489.00 | 303.00 | 375.00 | 2.50 | NÃO | fora do lado solicitado |
| 685 | 490.00 | 303.00 | 376.00 | 2.50 | NÃO | fora do lado solicitado |
| 686 | 491.00 | 303.00 | 377.00 | 2.50 | NÃO | fora do lado solicitado |
| 687 | 492.00 | 303.00 | 378.00 | 2.50 | NÃO | fora do lado solicitado |
| 688 | 493.00 | 303.00 | 379.00 | 2.50 | NÃO | fora do lado solicitado |
| 689 | 494.00 | 303.00 | 380.00 | 2.50 | NÃO | fora do lado solicitado |
| 690 | 495.00 | 303.00 | 381.00 | 2.50 | NÃO | fora do lado solicitado |
| 691 | 496.00 | 303.00 | 382.00 | 2.50 | NÃO | fora do lado solicitado |
| 692 | 497.00 | 303.00 | 383.00 | 2.50 | NÃO | fora do lado solicitado |
| 693 | 498.00 | 303.00 | 384.00 | 2.50 | NÃO | fora do lado solicitado |
| 694 | 499.00 | 303.00 | 385.00 | 2.50 | NÃO | fora do lado solicitado |
| 695 | 500.00 | 303.00 | 386.00 | 2.50 | NÃO | fora do lado solicitado |
| 696 | 501.00 | 303.00 | 387.00 | 2.50 | NÃO | fora do lado solicitado |
| 697 | 502.00 | 303.00 | 388.00 | 2.50 | NÃO | fora do lado solicitado |
| 698 | 503.00 | 303.00 | 389.00 | 2.50 | NÃO | fora do lado solicitado |
| 699 | 504.00 | 303.00 | 390.00 | 2.50 | NÃO | fora do lado solicitado |
| 700 | 505.00 | 303.00 | 391.00 | 2.50 | NÃO | fora do lado solicitado |
| 701 | 506.00 | 303.00 | 392.00 | 2.50 | NÃO | fora do lado solicitado |
| 702 | 507.00 | 303.00 | 393.00 | 2.50 | NÃO | fora do lado solicitado |
| 703 | 508.00 | 303.00 | 394.00 | 2.50 | NÃO | fora do lado solicitado |
| 704 | 509.00 | 303.00 | 395.00 | 2.50 | NÃO | fora do lado solicitado |
| 705 | 510.00 | 303.00 | 396.00 | 2.50 | NÃO | fora do lado solicitado |
| 706 | 511.00 | 303.00 | 397.00 | 2.50 | NÃO | fora do lado solicitado |
| 707 | 512.00 | 303.00 | 398.00 | 2.50 | NÃO | fora do lado solicitado |
| 708 | 513.00 | 303.00 | 399.00 | 2.50 | NÃO | fora do lado solicitado |
| 709 | 514.00 | 303.00 | 400.00 | 2.50 | NÃO | fora do lado solicitado |
| 710 | 514.00 | 302.00 | 400.00 | 3.50 | NÃO | fora do lado solicitado |
| 711 | 514.00 | 301.00 | 400.00 | 4.50 | NÃO | fora do lado solicitado |
| 712 | 514.00 | 300.00 | 400.01 | 5.50 | NÃO | fora do lado solicitado |
| 713 | 514.00 | 299.00 | 400.02 | 6.50 | NÃO | fora do lado solicitado |
| 714 | 515.00 | 298.00 | 401.03 | 7.50 | NÃO | fora do lado solicitado |
| 715 | 515.00 | 297.00 | 401.04 | 8.50 | NÃO | fora do lado solicitado |
| 716 | 515.00 | 296.00 | 401.06 | 9.50 | NÃO | fora do lado solicitado |
| 717 | 515.00 | 295.00 | 401.08 | 10.50 | NÃO | fora do lado solicitado |
| 718 | 515.00 | 294.00 | 401.10 | 11.50 | NÃO | fora do lado solicitado |
| 719 | 516.00 | 293.00 | 402.12 | 12.50 | NÃO | fora do lado solicitado |
| 720 | 516.00 | 292.00 | 402.15 | 13.50 | NÃO | fora do lado solicitado |
| 721 | 516.00 | 291.00 | 402.18 | 14.50 | NÃO | fora do lado solicitado |
| 722 | 516.00 | 290.00 | 402.21 | 15.50 | NÃO | fora do lado solicitado |
| 723 | 516.00 | 289.00 | 402.24 | 16.50 | NÃO | fora do lado solicitado |
| 724 | 517.00 | 288.00 | 403.28 | 17.50 | NÃO | fora do lado solicitado |
| 725 | 517.00 | 287.00 | 403.32 | 18.50 | NÃO | fora do lado solicitado |
| 726 | 517.00 | 286.00 | 403.36 | 19.50 | NÃO | fora do lado solicitado |
| 727 | 517.00 | 285.00 | 403.40 | 20.50 | NÃO | fora do lado solicitado |
| 728 | 517.00 | 284.00 | 403.45 | 21.50 | NÃO | fora do lado solicitado |
| 729 | 517.00 | 283.00 | 403.50 | 22.50 | NÃO | fora do lado solicitado |
| 730 | 517.00 | 282.00 | 403.55 | 23.50 | NÃO | fora do lado solicitado |
| 731 | 518.00 | 281.00 | 404.60 | 24.50 | NÃO | fora do lado solicitado |
| 732 | 518.00 | 280.00 | 404.65 | 25.50 | NÃO | fora do lado solicitado |
| 733 | 518.00 | 279.00 | 404.71 | 26.50 | NÃO | fora do lado solicitado |
| 734 | 518.00 | 278.00 | 404.77 | 27.50 | NÃO | fora do lado solicitado |
| 735 | 518.00 | 277.00 | 404.84 | 28.50 | NÃO | fora do lado solicitado |
| 736 | 518.00 | 276.00 | 404.90 | 29.50 | NÃO | fora do lado solicitado |
| 737 | 518.00 | 275.00 | 404.97 | 30.50 | NÃO | fora do lado solicitado |
| 738 | 518.00 | 274.00 | 405.04 | 31.50 | NÃO | fora do lado solicitado |
| 739 | 519.00 | 273.00 | 406.11 | 32.50 | NÃO | fora do lado solicitado |
| 740 | 519.00 | 272.00 | 406.18 | 33.50 | NÃO | fora do lado solicitado |
| 741 | 519.00 | 271.00 | 406.26 | 34.50 | NÃO | fora do lado solicitado |
| 742 | 519.00 | 270.00 | 406.34 | 35.50 | NÃO | fora do lado solicitado |
| 743 | 519.00 | 269.00 | 406.42 | 36.50 | NÃO | fora do lado solicitado |
| 744 | 519.00 | 268.00 | 406.51 | 37.50 | NÃO | fora do lado solicitado |
| 745 | 519.00 | 267.00 | 406.60 | 38.50 | NÃO | fora do lado solicitado |
| 746 | 519.00 | 266.00 | 406.69 | 39.50 | NÃO | fora do lado solicitado |
| 747 | 519.00 | 265.00 | 406.78 | 40.50 | NÃO | fora do lado solicitado |
| 748 | 519.00 | 264.00 | 406.87 | 41.50 | NÃO | fora do lado solicitado |
| 749 | 519.00 | 263.00 | 406.97 | 42.50 | NÃO | fora do lado solicitado |
| 750 | 519.00 | 262.00 | 407.07 | 43.50 | NÃO | fora do lado solicitado |
| 751 | 519.00 | 261.00 | 407.17 | 44.50 | NÃO | fora do lado solicitado |
| 752 | 519.00 | 260.00 | 407.28 | 45.50 | NÃO | fora do lado solicitado |
| 753 | 519.00 | 259.00 | 407.38 | 46.50 | NÃO | fora do lado solicitado |
| 754 | 519.00 | 258.00 | 407.49 | 47.50 | NÃO | fora do lado solicitado |
| 755 | 519.00 | 257.00 | 407.60 | 48.50 | NÃO | fora do lado solicitado |
| 756 | 519.00 | 256.00 | 407.72 | 49.50 | NÃO | fora do lado solicitado |
| 757 | 519.00 | 255.00 | 407.83 | 50.50 | NÃO | fora do lado solicitado |
| 758 | 519.00 | 254.00 | 407.95 | 51.50 | NÃO | fora do lado solicitado |
| 759 | 519.00 | 253.00 | 408.07 | 52.50 | NÃO | fora do lado solicitado |
| 760 | 519.00 | 252.00 | 408.20 | 53.50 | NÃO | fora do lado solicitado |
| 761 | 519.00 | 251.00 | 408.32 | 54.50 | NÃO | fora do lado solicitado |
| 762 | 519.00 | 250.00 | 408.45 | 55.50 | NÃO | fora do lado solicitado |
| 763 | 519.00 | 249.00 | 408.58 | 56.50 | NÃO | fora do lado solicitado |
| 764 | 519.00 | 248.00 | 408.72 | 57.50 | NÃO | fora do lado solicitado |
| 765 | 519.00 | 247.00 | 408.85 | 58.50 | NÃO | fora do lado solicitado |
| 766 | 519.00 | 246.00 | 408.99 | 59.50 | NÃO | fora do lado solicitado |
| 767 | 519.00 | 245.00 | 409.13 | 60.50 | NÃO | fora do lado solicitado |
| 768 | 519.00 | 244.00 | 409.27 | 61.50 | NÃO | fora do lado solicitado |
| 769 | 519.00 | 243.00 | 409.42 | 62.50 | NÃO | fora do lado solicitado |
| 770 | 519.00 | 242.00 | 409.57 | 63.50 | NÃO | fora do lado solicitado |
| 771 | 519.00 | 241.00 | 409.72 | 64.50 | NÃO | fora do lado solicitado |
| 772 | 519.00 | 240.00 | 409.87 | 65.50 | NÃO | fora do lado solicitado |
| 773 | 519.00 | 239.00 | 410.03 | 66.50 | NÃO | fora do lado solicitado |
| 774 | 519.00 | 238.00 | 410.18 | 67.50 | NÃO | fora do lado solicitado |
| 775 | 519.00 | 237.00 | 410.34 | 68.50 | NÃO | fora do lado solicitado |
| 776 | 518.00 | 236.00 | 409.52 | 69.50 | NÃO | fora do lado solicitado |
| 777 | 518.00 | 235.00 | 409.68 | 70.50 | NÃO | fora do lado solicitado |
| 778 | 518.00 | 234.00 | 409.85 | 71.50 | NÃO | fora do lado solicitado |
| 779 | 518.00 | 233.00 | 410.02 | 72.50 | NÃO | fora do lado solicitado |
| 780 | 518.00 | 232.00 | 410.19 | 73.50 | NÃO | fora do lado solicitado |
| 781 | 518.00 | 231.00 | 410.37 | 74.50 | NÃO | fora do lado solicitado |
| 782 | 518.00 | 230.00 | 410.54 | 75.50 | NÃO | fora do lado solicitado |
| 783 | 518.00 | 229.00 | 410.72 | 76.50 | NÃO | fora do lado solicitado |
| 784 | 517.00 | 228.00 | 409.92 | 77.50 | NÃO | fora do lado solicitado |
| 785 | 517.00 | 227.00 | 410.10 | 78.50 | NÃO | fora do lado solicitado |
| 786 | 517.00 | 226.00 | 410.29 | 79.50 | NÃO | fora do lado solicitado |
| 787 | 517.00 | 225.00 | 410.48 | 80.50 | NÃO | fora do lado solicitado |
| 788 | 517.00 | 224.00 | 410.67 | 81.50 | NÃO | fora do lado solicitado |
| 789 | 517.00 | 223.00 | 410.86 | 82.50 | NÃO | fora do lado solicitado |
| 790 | 517.00 | 222.00 | 411.06 | 83.50 | NÃO | fora do lado solicitado |
| 791 | 516.00 | 221.00 | 410.28 | 84.50 | NÃO | fora do lado solicitado |
| 792 | 516.00 | 220.00 | 410.48 | 85.50 | NÃO | fora do lado solicitado |
| 793 | 516.00 | 219.00 | 410.68 | 86.50 | NÃO | fora do lado solicitado |
| 794 | 516.00 | 218.00 | 410.89 | 87.50 | NÃO | fora do lado solicitado |
| 795 | 516.00 | 217.00 | 411.10 | 88.50 | NÃO | fora do lado solicitado |
| 796 | 515.00 | 216.00 | 410.33 | 89.50 | NÃO | fora do lado solicitado |
| 797 | 515.00 | 215.00 | 410.54 | 90.50 | NÃO | fora do lado solicitado |
| 798 | 515.00 | 214.00 | 410.76 | 91.50 | NÃO | fora do lado solicitado |
| 799 | 515.00 | 213.00 | 410.98 | 92.50 | NÃO | fora do lado solicitado |
| 800 | 515.00 | 212.00 | 411.20 | 93.50 | NÃO | fora do lado solicitado |
| 801 | 514.00 | 211.00 | 410.44 | 94.50 | NÃO | fora do lado solicitado |
| 802 | 514.00 | 210.00 | 410.67 | 95.50 | NÃO | fora do lado solicitado |
| 803 | 514.00 | 209.00 | 410.90 | 96.50 | NÃO | fora do lado solicitado |
| 804 | 514.00 | 208.00 | 411.13 | 97.50 | NÃO | fora do lado solicitado |
| 805 | 514.00 | 207.00 | 411.36 | 98.50 | NÃO | fora do lado solicitado |
| 806 | 513.00 | 206.00 | 410.62 | 99.50 | NÃO | fora do lado solicitado |
| 807 | 513.00 | 205.00 | 410.86 | 100.50 | NÃO | fora do lado solicitado |
| 808 | 513.00 | 204.00 | 411.10 | 101.50 | NÃO | fora do lado solicitado |
| 809 | 512.00 | 203.00 | 410.37 | 102.50 | NÃO | fora do lado solicitado |
| 810 | 512.00 | 202.00 | 410.62 | 103.50 | NÃO | fora do lado solicitado |
| 811 | 512.00 | 201.00 | 410.86 | 104.50 | NÃO | fora do lado solicitado |
| 812 | 512.00 | 200.00 | 411.11 | 105.50 | NÃO | fora do lado solicitado |
| 813 | 511.00 | 199.00 | 410.40 | 106.50 | NÃO | fora do lado solicitado |
| 814 | 511.00 | 198.00 | 410.65 | 107.50 | NÃO | fora do lado solicitado |
| 815 | 511.00 | 197.00 | 410.91 | 108.50 | NÃO | fora do lado solicitado |
| 816 | 511.00 | 196.00 | 411.17 | 109.50 | NÃO | fora do lado solicitado |
| 817 | 510.00 | 195.00 | 410.46 | 110.50 | NÃO | fora do lado solicitado |
| 818 | 510.00 | 194.00 | 410.73 | 111.50 | NÃO | fora do lado solicitado |
| 819 | 510.00 | 193.00 | 410.99 | 112.50 | NÃO | fora do lado solicitado |
| 820 | 509.00 | 192.00 | 410.30 | 113.50 | NÃO | fora do lado solicitado |
| 821 | 509.00 | 191.00 | 410.57 | 114.50 | NÃO | fora do lado solicitado |
| 822 | 509.00 | 190.00 | 410.85 | 115.50 | NÃO | fora do lado solicitado |
| 823 | 508.00 | 189.00 | 410.16 | 116.50 | NÃO | fora do lado solicitado |
| 824 | 508.00 | 188.00 | 410.44 | 117.50 | NÃO | fora do lado solicitado |
| 825 | 508.00 | 187.00 | 410.72 | 118.50 | NÃO | fora do lado solicitado |
| 826 | 507.00 | 186.00 | 410.05 | 119.50 | NÃO | fora do lado solicitado |
| 827 | 507.00 | 185.00 | 410.33 | 120.50 | NÃO | fora do lado solicitado |
| 828 | 507.00 | 184.00 | 410.62 | 121.50 | NÃO | fora do lado solicitado |
| 829 | 506.00 | 183.00 | 409.96 | 122.50 | NÃO | fora do lado solicitado |
| 830 | 506.00 | 182.00 | 410.25 | 123.50 | NÃO | fora do lado solicitado |
| 831 | 505.00 | 181.00 | 409.59 | 124.50 | NÃO | fora do lado solicitado |
| 832 | 505.00 | 180.00 | 409.89 | 125.50 | NÃO | fora do lado solicitado |
| 833 | 505.00 | 179.00 | 410.19 | 126.50 | NÃO | fora do lado solicitado |
| 834 | 504.00 | 178.00 | 409.54 | 127.50 | NÃO | fora do lado solicitado |
| 835 | 504.00 | 177.00 | 409.85 | 128.50 | NÃO | fora do lado solicitado |
| 836 | 503.00 | 176.00 | 409.21 | 129.50 | NÃO | fora do lado solicitado |
| 837 | 503.00 | 175.00 | 409.52 | 130.50 | NÃO | fora do lado solicitado |
| 838 | 503.00 | 174.00 | 409.83 | 131.50 | NÃO | fora do lado solicitado |
| 839 | 502.00 | 173.00 | 409.20 | 132.50 | NÃO | fora do lado solicitado |
| 840 | 502.00 | 172.00 | 409.52 | 133.50 | NÃO | fora do lado solicitado |
| 841 | 501.00 | 171.00 | 408.89 | 134.50 | NÃO | fora do lado solicitado |
| 842 | 501.00 | 170.00 | 409.22 | 135.50 | NÃO | fora do lado solicitado |
| 843 | 500.00 | 169.00 | 408.60 | 136.50 | NÃO | fora do lado solicitado |
| 844 | 500.00 | 168.00 | 408.93 | 137.50 | NÃO | fora da faixa vertical |
| 845 | 499.00 | 167.00 | 408.31 | 138.50 | NÃO | fora da faixa vertical |
| 846 | 499.00 | 166.00 | 408.65 | 139.50 | NÃO | fora da faixa vertical |
| 847 | 498.00 | 165.00 | 408.04 | 140.50 | NÃO | fora da faixa vertical |
| 848 | 498.00 | 164.00 | 408.38 | 141.50 | NÃO | fora da faixa vertical |
| 849 | 497.00 | 163.00 | 407.79 | 142.50 | NÃO | fora da faixa vertical |
| 850 | 497.00 | 162.00 | 408.13 | 143.50 | NÃO | fora da faixa vertical |
| 851 | 496.00 | 161.00 | 407.54 | 144.50 | NÃO | fora da faixa vertical |
| 852 | 496.00 | 160.00 | 407.89 | 145.50 | NÃO | fora da faixa vertical |
| 853 | 495.00 | 159.00 | 407.30 | 146.50 | NÃO | fora da faixa vertical |
| 854 | 495.00 | 158.00 | 407.66 | 147.50 | NÃO | fora da faixa vertical |
| 855 | 494.00 | 157.00 | 407.08 | 148.50 | NÃO | fora da faixa vertical |
| 856 | 493.00 | 156.00 | 406.51 | 149.50 | NÃO | fora da faixa vertical |
| 857 | 493.00 | 155.00 | 406.87 | 150.50 | NÃO | fora da faixa vertical |
| 858 | 492.00 | 154.00 | 406.31 | 151.50 | NÃO | fora da faixa vertical |
| 859 | 492.00 | 153.00 | 406.67 | 152.50 | NÃO | fora da faixa vertical |
| 860 | 491.00 | 152.00 | 406.12 | 153.50 | NÃO | fora da faixa vertical |
| 861 | 490.00 | 151.00 | 405.56 | 154.50 | NÃO | fora da faixa vertical |
| 862 | 490.00 | 150.00 | 405.94 | 155.50 | NÃO | fora da faixa vertical |
| 863 | 489.00 | 149.00 | 405.39 | 156.50 | NÃO | fora da faixa vertical |
| 864 | 489.00 | 148.00 | 405.77 | 157.50 | NÃO | fora da faixa vertical |
| 865 | 488.00 | 147.00 | 405.23 | 158.50 | NÃO | fora da faixa vertical |
| 866 | 487.00 | 146.00 | 404.69 | 159.50 | NÃO | fora da faixa vertical |
| 867 | 487.00 | 145.00 | 405.08 | 160.50 | NÃO | fora da faixa vertical |
| 868 | 486.00 | 144.00 | 404.56 | 161.50 | NÃO | fora da faixa vertical |
| 869 | 486.00 | 143.00 | 404.95 | 162.50 | NÃO | fora da faixa vertical |
| 870 | 485.00 | 142.00 | 404.43 | 163.50 | NÃO | fora da faixa vertical |
| 871 | 484.00 | 141.00 | 403.91 | 164.50 | NÃO | fora da faixa vertical |
| 872 | 483.00 | 140.00 | 403.40 | 165.50 | NÃO | fora da faixa vertical |
| 873 | 483.00 | 139.00 | 403.80 | 166.50 | NÃO | fora da faixa vertical |
| 874 | 482.00 | 138.00 | 403.30 | 167.50 | NÃO | fora da faixa vertical |
| 875 | 481.00 | 137.00 | 402.80 | 168.50 | NÃO | fora da faixa vertical |
| 876 | 480.00 | 136.00 | 402.30 | 169.50 | NÃO | fora da faixa vertical |
| 877 | 480.00 | 135.00 | 402.72 | 170.50 | NÃO | fora da faixa vertical |
| 878 | 479.00 | 134.00 | 402.23 | 171.50 | NÃO | fora da faixa vertical |
| 879 | 478.00 | 133.00 | 401.74 | 172.50 | NÃO | fora da faixa vertical |
| 880 | 477.00 | 132.00 | 401.26 | 173.50 | NÃO | fora da faixa vertical |
| 881 | 477.00 | 131.00 | 401.69 | 174.50 | NÃO | fora da faixa vertical |
| 882 | 476.00 | 130.00 | 401.21 | 175.50 | NÃO | fora da faixa vertical |
| 883 | 475.00 | 129.00 | 400.75 | 176.50 | NÃO | fora da faixa vertical |
| 884 | 475.00 | 128.00 | 401.18 | 177.50 | NÃO | fora da faixa vertical |
| 885 | 474.00 | 127.00 | 400.72 | 178.50 | NÃO | fora da faixa vertical |
| 886 | 473.00 | 126.00 | 400.26 | 179.50 | NÃO | fora da faixa vertical |
| 887 | 472.00 | 125.00 | 399.81 | 180.50 | NÃO | fora da faixa vertical |
| 888 | 471.00 | 124.00 | 399.36 | 181.50 | NÃO | fora da faixa vertical |
| 889 | 470.00 | 123.00 | 398.92 | 182.50 | NÃO | fora da faixa vertical |
| 890 | 469.00 | 122.00 | 398.48 | 183.50 | NÃO | fora da faixa vertical |
| 891 | 468.00 | 121.00 | 398.05 | 184.50 | NÃO | fora da faixa vertical |
| 892 | 467.00 | 120.00 | 397.62 | 185.50 | NÃO | fora da faixa vertical |
| 893 | 467.00 | 119.00 | 398.08 | 186.50 | NÃO | fora da faixa vertical |
| 894 | 466.00 | 118.00 | 397.65 | 187.50 | NÃO | fora da faixa vertical |
| 895 | 465.00 | 117.00 | 397.24 | 188.50 | NÃO | fora da faixa vertical |
| 896 | 464.00 | 116.00 | 396.82 | 189.50 | NÃO | fora da faixa vertical |
| 897 | 463.00 | 115.00 | 396.42 | 190.50 | NÃO | fora da faixa vertical |
| 898 | 462.00 | 114.00 | 396.01 | 191.50 | NÃO | fora da faixa vertical |
| 899 | 461.00 | 113.00 | 395.61 | 192.50 | NÃO | fora da faixa vertical |
| 900 | 460.00 | 112.00 | 395.22 | 193.50 | NÃO | fora da faixa vertical |
| 901 | 459.00 | 111.00 | 394.83 | 194.50 | NÃO | fora da faixa vertical |
| 902 | 458.00 | 110.00 | 394.44 | 195.50 | NÃO | fora da faixa vertical |
| 903 | 457.00 | 109.00 | 394.06 | 196.50 | NÃO | fora da faixa vertical |
| 904 | 456.00 | 108.00 | 393.69 | 197.50 | NÃO | fora da faixa vertical |
| 905 | 455.00 | 107.00 | 393.32 | 198.50 | NÃO | fora da faixa vertical |
| 906 | 454.00 | 106.00 | 392.95 | 199.50 | NÃO | fora da faixa vertical |
| 907 | 453.00 | 105.00 | 392.59 | 200.50 | NÃO | fora da faixa vertical |
| 908 | 452.00 | 104.00 | 392.23 | 201.50 | NÃO | fora da faixa vertical |
| 909 | 451.00 | 103.00 | 391.88 | 202.50 | NÃO | fora da faixa vertical |
| 910 | 450.00 | 103.00 | 391.02 | 202.50 | NÃO | fora da faixa vertical |
| 911 | 449.00 | 102.00 | 390.67 | 203.50 | NÃO | fora da faixa vertical |
| 912 | 448.00 | 101.00 | 390.33 | 204.50 | NÃO | fora da faixa vertical |
| 913 | 447.00 | 100.00 | 390.00 | 205.50 | NÃO | fora da faixa vertical |
| 914 | 446.00 | 99.00 | 389.67 | 206.50 | NÃO | fora da faixa vertical |
| 915 | 445.00 | 98.00 | 389.34 | 207.50 | NÃO | fora da faixa vertical |
| 916 | 444.00 | 97.00 | 389.02 | 208.50 | NÃO | fora da faixa vertical |
| 917 | 443.00 | 97.00 | 388.17 | 208.50 | NÃO | fora da faixa vertical |
| 918 | 442.00 | 96.00 | 387.86 | 209.50 | NÃO | fora da faixa vertical |
| 919 | 441.00 | 95.00 | 387.55 | 210.50 | NÃO | fora da faixa vertical |
| 920 | 440.00 | 94.00 | 387.24 | 211.50 | NÃO | fora da faixa vertical |
| 921 | 439.00 | 94.00 | 386.40 | 211.50 | NÃO | fora da faixa vertical |
| 922 | 438.00 | 93.00 | 386.10 | 212.50 | NÃO | fora da faixa vertical |
| 923 | 437.00 | 92.00 | 385.81 | 213.50 | NÃO | fora da faixa vertical |
| 924 | 436.00 | 91.00 | 385.52 | 214.50 | NÃO | fora da faixa vertical |
| 925 | 435.00 | 91.00 | 384.69 | 214.50 | NÃO | fora da faixa vertical |
| 926 | 434.00 | 90.00 | 384.41 | 215.50 | NÃO | fora da faixa vertical |
| 927 | 433.00 | 89.00 | 384.13 | 216.50 | NÃO | fora da faixa vertical |
| 928 | 432.00 | 88.00 | 383.86 | 217.50 | NÃO | fora da faixa vertical |
| 929 | 431.00 | 88.00 | 383.03 | 217.50 | NÃO | fora da faixa vertical |
| 930 | 430.00 | 87.00 | 382.77 | 218.50 | NÃO | fora da faixa vertical |
| 931 | 429.00 | 86.00 | 382.51 | 219.50 | NÃO | fora da faixa vertical |
| 932 | 428.00 | 86.00 | 381.69 | 219.50 | NÃO | fora da faixa vertical |
| 933 | 427.00 | 85.00 | 381.44 | 220.50 | NÃO | fora da faixa vertical |
| 934 | 426.00 | 85.00 | 380.62 | 220.50 | NÃO | fora da faixa vertical |
| 935 | 425.00 | 84.00 | 380.37 | 221.50 | NÃO | fora da faixa vertical |
| 936 | 424.00 | 83.00 | 380.13 | 222.50 | NÃO | fora da faixa vertical |
| 937 | 423.00 | 83.00 | 379.32 | 222.50 | NÃO | fora da faixa vertical |
| 938 | 422.00 | 82.00 | 379.08 | 223.50 | NÃO | fora da faixa vertical |
| 939 | 421.00 | 82.00 | 378.27 | 223.50 | NÃO | fora da faixa vertical |
| 940 | 420.00 | 81.00 | 378.05 | 224.50 | NÃO | fora da faixa vertical |
| 941 | 419.00 | 80.00 | 377.83 | 225.50 | NÃO | fora da faixa vertical |
| 942 | 418.00 | 80.00 | 377.02 | 225.50 | NÃO | fora da faixa vertical |
| 943 | 417.00 | 79.00 | 376.81 | 226.50 | NÃO | fora da faixa vertical |
| 944 | 416.00 | 79.00 | 376.01 | 226.50 | NÃO | fora da faixa vertical |
| 945 | 415.00 | 78.00 | 375.80 | 227.50 | NÃO | fora da faixa vertical |
| 946 | 414.00 | 77.00 | 375.60 | 228.50 | NÃO | fora da faixa vertical |
| 947 | 413.00 | 77.00 | 374.80 | 228.50 | NÃO | fora da faixa vertical |
| 948 | 412.00 | 76.00 | 374.61 | 229.50 | NÃO | fora da faixa vertical |
| 949 | 411.00 | 76.00 | 373.82 | 229.50 | NÃO | fora da faixa vertical |
| 950 | 410.00 | 75.00 | 373.63 | 230.50 | NÃO | fora da faixa vertical |
| 951 | 409.00 | 75.00 | 372.84 | 230.50 | NÃO | fora da faixa vertical |
| 952 | 408.00 | 74.00 | 372.66 | 231.50 | NÃO | fora da faixa vertical |
| 953 | 407.00 | 74.00 | 371.87 | 231.50 | NÃO | fora da faixa vertical |
| 954 | 406.00 | 73.00 | 371.70 | 232.50 | NÃO | fora da faixa vertical |
| 955 | 405.00 | 73.00 | 370.92 | 232.50 | NÃO | fora da faixa vertical |
| 956 | 404.00 | 72.00 | 370.76 | 233.50 | NÃO | fora da faixa vertical |
| 957 | 403.00 | 72.00 | 369.98 | 233.50 | NÃO | fora da faixa vertical |
| 958 | 402.00 | 71.00 | 369.82 | 234.50 | NÃO | fora da faixa vertical |
| 959 | 401.00 | 71.00 | 369.04 | 234.50 | NÃO | fora da faixa vertical |
| 960 | 400.00 | 71.00 | 368.27 | 234.50 | NÃO | fora da faixa vertical |
| 961 | 399.00 | 70.00 | 368.12 | 235.50 | NÃO | fora da faixa vertical |
| 962 | 398.00 | 70.00 | 367.35 | 235.50 | NÃO | fora da faixa vertical |
| 963 | 397.00 | 69.00 | 367.21 | 236.50 | NÃO | fora da faixa vertical |
| 964 | 396.00 | 69.00 | 366.44 | 236.50 | NÃO | fora da faixa vertical |
| 965 | 395.00 | 68.00 | 366.31 | 237.50 | NÃO | fora da faixa vertical |
| 966 | 394.00 | 68.00 | 365.55 | 237.50 | NÃO | fora da faixa vertical |
| 967 | 393.00 | 67.00 | 365.43 | 238.50 | NÃO | fora da faixa vertical |
| 968 | 392.00 | 67.00 | 364.66 | 238.50 | NÃO | fora da faixa vertical |
| 969 | 391.00 | 67.00 | 363.90 | 238.50 | NÃO | fora da faixa vertical |
| 970 | 390.00 | 66.00 | 363.79 | 239.50 | NÃO | fora da faixa vertical |
| 971 | 389.00 | 66.00 | 363.03 | 239.50 | NÃO | fora da faixa vertical |
| 972 | 388.00 | 66.00 | 362.28 | 239.50 | NÃO | fora da faixa vertical |
| 973 | 387.00 | 65.00 | 362.18 | 240.50 | NÃO | fora da faixa vertical |
| 974 | 386.00 | 65.00 | 361.42 | 240.50 | NÃO | fora da faixa vertical |
| 975 | 385.00 | 64.00 | 361.33 | 241.50 | NÃO | fora da faixa vertical |
| 976 | 384.00 | 64.00 | 360.58 | 241.50 | NÃO | fora da faixa vertical |
| 977 | 383.00 | 64.00 | 359.84 | 241.50 | NÃO | fora da faixa vertical |
| 978 | 382.00 | 63.00 | 359.76 | 242.50 | NÃO | fora da faixa vertical |
| 979 | 381.00 | 63.00 | 359.01 | 242.50 | NÃO | fora da faixa vertical |
| 980 | 380.00 | 63.00 | 358.27 | 242.50 | NÃO | fora da faixa vertical |
| 981 | 379.00 | 62.00 | 358.20 | 243.50 | NÃO | fora da faixa vertical |
| 982 | 378.00 | 62.00 | 357.46 | 243.50 | NÃO | fora da faixa vertical |
| 983 | 377.00 | 62.00 | 356.72 | 243.50 | NÃO | fora da faixa vertical |
| 984 | 376.00 | 61.00 | 356.66 | 244.50 | NÃO | fora da faixa vertical |
| 985 | 375.00 | 61.00 | 355.93 | 244.50 | NÃO | fora da faixa vertical |
| 986 | 374.00 | 61.00 | 355.20 | 244.50 | NÃO | fora da faixa vertical |
| 987 | 373.00 | 61.00 | 354.46 | 244.50 | NÃO | fora da faixa vertical |
| 988 | 372.00 | 60.00 | 354.42 | 245.50 | NÃO | fora da faixa vertical |
| 989 | 371.00 | 60.00 | 353.69 | 245.50 | NÃO | fora da faixa vertical |
| 990 | 370.00 | 60.00 | 352.97 | 245.50 | NÃO | fora da faixa vertical |
| 991 | 369.00 | 59.00 | 352.93 | 246.50 | NÃO | fora da faixa vertical |
| 992 | 368.00 | 59.00 | 352.21 | 246.50 | NÃO | fora da faixa vertical |
| 993 | 367.00 | 59.00 | 351.49 | 246.50 | NÃO | fora da faixa vertical |
| 994 | 366.00 | 59.00 | 350.77 | 246.50 | NÃO | fora da faixa vertical |
| 995 | 365.00 | 58.00 | 350.75 | 247.50 | NÃO | fora da faixa vertical |
| 996 | 364.00 | 58.00 | 350.04 | 247.50 | NÃO | fora da faixa vertical |
| 997 | 363.00 | 58.00 | 349.32 | 247.50 | NÃO | fora da faixa vertical |
| 998 | 362.00 | 58.00 | 348.61 | 247.50 | NÃO | fora da faixa vertical |
| 999 | 361.00 | 57.00 | 348.60 | 248.50 | NÃO | fora da faixa vertical |
| 1000 | 360.00 | 57.00 | 347.90 | 248.50 | NÃO | fora da faixa vertical |
| 1001 | 359.00 | 57.00 | 347.19 | 248.50 | NÃO | fora da faixa vertical |
| 1002 | 358.00 | 57.00 | 346.49 | 248.50 | NÃO | fora da faixa vertical |
| 1003 | 357.00 | 57.00 | 345.78 | 248.50 | NÃO | fora da faixa vertical |
| 1004 | 356.00 | 56.00 | 345.79 | 249.50 | NÃO | fora da faixa vertical |
| 1005 | 355.00 | 56.00 | 345.09 | 249.50 | NÃO | fora da faixa vertical |
| 1006 | 354.00 | 56.00 | 344.40 | 249.50 | NÃO | fora da faixa vertical |
| 1007 | 353.00 | 56.00 | 343.70 | 249.50 | NÃO | fora da faixa vertical |
| 1008 | 352.00 | 56.00 | 343.01 | 249.50 | NÃO | fora da faixa vertical |
| 1009 | 351.00 | 55.00 | 343.03 | 250.50 | NÃO | fora da faixa vertical |
| 1010 | 350.00 | 55.00 | 342.34 | 250.50 | NÃO | fora da faixa vertical |
| 1011 | 349.00 | 55.00 | 341.66 | 250.50 | NÃO | fora da faixa vertical |
| 1012 | 348.00 | 55.00 | 340.97 | 250.50 | NÃO | fora da faixa vertical |
| 1013 | 347.00 | 55.00 | 340.28 | 250.50 | NÃO | fora da faixa vertical |
| 1014 | 346.00 | 55.00 | 339.60 | 250.50 | NÃO | fora da faixa vertical |
| 1015 | 345.00 | 54.00 | 339.65 | 251.50 | NÃO | fora da faixa vertical |
| 1016 | 344.00 | 54.00 | 338.97 | 251.50 | NÃO | fora da faixa vertical |
| 1017 | 343.00 | 54.00 | 338.29 | 251.50 | NÃO | fora da faixa vertical |
| 1018 | 342.00 | 54.00 | 337.62 | 251.50 | NÃO | fora da faixa vertical |
| 1019 | 341.00 | 54.00 | 336.94 | 251.50 | NÃO | fora da faixa vertical |
| 1020 | 340.00 | 54.00 | 336.27 | 251.50 | NÃO | fora da faixa vertical |
| 1021 | 339.00 | 54.00 | 335.60 | 251.50 | NÃO | fora da faixa vertical |
| 1022 | 338.00 | 54.00 | 334.93 | 251.50 | NÃO | fora da faixa vertical |
| 1023 | 337.00 | 53.00 | 335.01 | 252.50 | NÃO | fora da faixa vertical |
| 1024 | 336.00 | 53.00 | 334.34 | 252.50 | NÃO | fora da faixa vertical |
| 1025 | 335.00 | 53.00 | 333.68 | 252.50 | NÃO | fora da faixa vertical |
| 1026 | 334.00 | 53.00 | 333.02 | 252.50 | NÃO | fora da faixa vertical |
| 1027 | 333.00 | 53.00 | 332.36 | 252.50 | NÃO | fora da faixa vertical |
| 1028 | 332.00 | 53.00 | 331.70 | 252.50 | NÃO | fora da faixa vertical |
| 1029 | 331.00 | 53.00 | 331.04 | 252.50 | NÃO | fora da faixa vertical |
| 1030 | 330.00 | 53.00 | 330.39 | 252.50 | NÃO | fora da faixa vertical |
| 1031 | 329.00 | 53.00 | 329.73 | 252.50 | NÃO | fora da faixa vertical |
| 1032 | 328.00 | 53.00 | 329.08 | 252.50 | NÃO | fora da faixa vertical |
| 1033 | 327.00 | 53.00 | 328.43 | 252.50 | NÃO | fora da faixa vertical |
| 1034 | 326.00 | 53.00 | 327.79 | 252.50 | NÃO | fora da faixa vertical |
| 1035 | 325.00 | 53.00 | 327.14 | 252.50 | NÃO | fora da faixa vertical |
| 1036 | 324.00 | 53.00 | 326.50 | 252.50 | NÃO | fora da faixa vertical |
| 1037 | 323.00 | 53.00 | 325.85 | 252.50 | NÃO | fora da faixa vertical |
| 1038 | 322.00 | 53.00 | 325.21 | 252.50 | NÃO | fora da faixa vertical |
| 1039 | 321.00 | 53.00 | 324.58 | 252.50 | NÃO | fora da faixa vertical |
| 1040 | 320.00 | 53.00 | 323.94 | 252.50 | NÃO | fora da faixa vertical |
| 1041 | 319.00 | 53.00 | 323.30 | 252.50 | NÃO | fora da faixa vertical |
| 1042 | 318.00 | 53.00 | 322.67 | 252.50 | NÃO | fora da faixa vertical |
| 1043 | 317.00 | 53.00 | 322.04 | 252.50 | NÃO | fora da faixa vertical |
| 1044 | 316.00 | 53.00 | 321.41 | 252.50 | NÃO | fora da faixa vertical |
| 1045 | 315.00 | 53.00 | 320.78 | 252.50 | NÃO | fora da faixa vertical |
| 1046 | 314.00 | 53.00 | 320.16 | 252.50 | NÃO | fora da faixa vertical |
| 1047 | 313.00 | 53.00 | 319.53 | 252.50 | NÃO | fora da faixa vertical |
| 1048 | 312.00 | 53.00 | 318.91 | 252.50 | NÃO | fora da faixa vertical |
| 1049 | 311.00 | 53.00 | 318.29 | 252.50 | NÃO | fora da faixa vertical |
| 1050 | 310.00 | 53.00 | 317.67 | 252.50 | NÃO | fora da faixa vertical |
| 1051 | 309.00 | 53.00 | 317.06 | 252.50 | NÃO | fora da faixa vertical |
| 1052 | 308.00 | 53.00 | 316.44 | 252.50 | NÃO | fora da faixa vertical |
| 1053 | 307.00 | 53.00 | 315.83 | 252.50 | NÃO | fora da faixa vertical |
| 1054 | 306.00 | 53.00 | 315.22 | 252.50 | NÃO | fora da faixa vertical |
| 1055 | 305.00 | 53.00 | 314.61 | 252.50 | NÃO | fora da faixa vertical |
| 1056 | 304.00 | 53.00 | 314.01 | 252.50 | NÃO | fora da faixa vertical |
| 1057 | 303.00 | 53.00 | 313.40 | 252.50 | NÃO | fora da faixa vertical |
| 1058 | 302.00 | 53.00 | 312.80 | 252.50 | NÃO | fora da faixa vertical |
| 1059 | 301.00 | 53.00 | 312.20 | 252.50 | NÃO | fora da faixa vertical |
| 1060 | 300.00 | 53.00 | 311.60 | 252.50 | NÃO | fora da faixa vertical |
| 1061 | 299.00 | 53.00 | 311.01 | 252.50 | NÃO | fora da faixa vertical |
| 1062 | 298.00 | 53.00 | 310.41 | 252.50 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 181 | 133.00 | 169.00 | 19.00 | -136.50 |
| 182 | 133.00 | 170.00 | 19.00 | -135.50 |
| 183 | 132.00 | 171.00 | 18.00 | -134.50 |
| 184 | 132.00 | 172.00 | 18.00 | -133.50 |
| 185 | 131.00 | 173.00 | 17.00 | -132.50 |
| 186 | 131.00 | 174.00 | 17.00 | -131.50 |
| 187 | 130.00 | 175.00 | 16.00 | -130.50 |
| 188 | 130.00 | 176.00 | 16.00 | -129.50 |
| 189 | 129.00 | 177.00 | 15.00 | -128.50 |
| 190 | 129.00 | 178.00 | 15.00 | -127.50 |
| 191 | 129.00 | 179.00 | 15.00 | -126.50 |
| 192 | 128.00 | 180.00 | 14.00 | -125.50 |
| 193 | 128.00 | 181.00 | 14.00 | -124.50 |
| 194 | 127.00 | 182.00 | 13.00 | -123.50 |
| 195 | 127.00 | 183.00 | 13.00 | -122.50 |
| 196 | 127.00 | 184.00 | 13.00 | -121.50 |
| 197 | 126.00 | 185.00 | 12.00 | -120.50 |
| 198 | 126.00 | 186.00 | 12.00 | -119.50 |
| 199 | 126.00 | 187.00 | 12.00 | -118.50 |
| 200 | 125.00 | 188.00 | 11.00 | -117.50 |
| 201 | 125.00 | 189.00 | 11.00 | -116.50 |
| 202 | 124.00 | 190.00 | 10.00 | -115.50 |
| 203 | 124.00 | 191.00 | 10.00 | -114.50 |
| 204 | 124.00 | 192.00 | 10.00 | -113.50 |
| 205 | 124.00 | 193.00 | 10.00 | -112.50 |
| 206 | 123.00 | 194.00 | 9.00 | -111.50 |
| 207 | 123.00 | 195.00 | 9.00 | -110.50 |
| 208 | 123.00 | 196.00 | 9.00 | -109.50 |
| 209 | 122.00 | 197.00 | 8.00 | -108.50 |
| 210 | 122.00 | 198.00 | 8.00 | -107.50 |
| 211 | 122.00 | 199.00 | 8.00 | -106.50 |
| 212 | 122.00 | 200.00 | 8.00 | -105.50 |
| 213 | 121.00 | 201.00 | 7.00 | -104.50 |
| 214 | 121.00 | 202.00 | 7.00 | -103.50 |
| 215 | 121.00 | 203.00 | 7.00 | -102.50 |
| 216 | 120.00 | 204.00 | 6.00 | -101.50 |
| 217 | 120.00 | 205.00 | 6.00 | -100.50 |
| 218 | 120.00 | 206.00 | 6.00 | -99.50 |
| 219 | 120.00 | 207.00 | 6.00 | -98.50 |
| 220 | 119.00 | 208.00 | 5.00 | -97.50 |
| 221 | 119.00 | 209.00 | 5.00 | -96.50 |
| 222 | 119.00 | 210.00 | 5.00 | -95.50 |
| 223 | 119.00 | 211.00 | 5.00 | -94.50 |
| 224 | 119.00 | 212.00 | 5.00 | -93.50 |
| 225 | 118.00 | 213.00 | 4.00 | -92.50 |
| 226 | 118.00 | 214.00 | 4.00 | -91.50 |
| 227 | 118.00 | 215.00 | 4.00 | -90.50 |
| 228 | 118.00 | 216.00 | 4.00 | -89.50 |
| 229 | 118.00 | 217.00 | 4.00 | -88.50 |
| 230 | 117.00 | 218.00 | 3.00 | -87.50 |
| 231 | 117.00 | 219.00 | 3.00 | -86.50 |
| 232 | 117.00 | 220.00 | 3.00 | -85.50 |
| 233 | 117.00 | 221.00 | 3.00 | -84.50 |
| 234 | 117.00 | 222.00 | 3.00 | -83.50 |
| 235 | 116.00 | 223.00 | 2.00 | -82.50 |
| 236 | 116.00 | 224.00 | 2.00 | -81.50 |
| 237 | 116.00 | 225.00 | 2.00 | -80.50 |
| 238 | 116.00 | 226.00 | 2.00 | -79.50 |
| 239 | 116.00 | 227.00 | 2.00 | -78.50 |
| 240 | 116.00 | 228.00 | 2.00 | -77.50 |
| 241 | 116.00 | 229.00 | 2.00 | -76.50 |
| 242 | 116.00 | 230.00 | 2.00 | -75.50 |
| 243 | 115.00 | 231.00 | 1.00 | -74.50 |
| 244 | 115.00 | 232.00 | 1.00 | -73.50 |
| 245 | 115.00 | 233.00 | 1.00 | -72.50 |
| 246 | 115.00 | 234.00 | 1.00 | -71.50 |
| 247 | 115.00 | 235.00 | 1.00 | -70.50 |
| 248 | 115.00 | 236.00 | 1.00 | -69.50 |
| 249 | 115.00 | 237.00 | 1.00 | -68.50 |
| 250 | 115.00 | 238.00 | 1.00 | -67.50 |
| 251 | 115.00 | 239.00 | 1.00 | -66.50 |
| 252 | 114.00 | 240.00 | 0.00 | -65.50 |
| 253 | 114.00 | 241.00 | 0.00 | -64.50 |
| 254 | 114.00 | 242.00 | 0.00 | -63.50 |
| 255 | 114.00 | 243.00 | 0.00 | -62.50 |
| 256 | 114.00 | 244.00 | 0.00 | -61.50 |
| 257 | 114.00 | 245.00 | 0.00 | -60.50 |
| 258 | 114.00 | 246.00 | 0.00 | -59.50 |
| 259 | 114.00 | 247.00 | 0.00 | -58.50 |
| 260 | 114.00 | 248.00 | 0.00 | -57.50 |
| 261 | 114.00 | 249.00 | 0.00 | -56.50 |
| 262 | 114.00 | 250.00 | 0.00 | -55.50 |
| 263 | 114.00 | 251.00 | 0.00 | -54.50 |
| 264 | 114.00 | 252.00 | 0.00 | -53.50 |
| 265 | 114.00 | 253.00 | 0.00 | -52.50 |
| 266 | 114.00 | 254.00 | 0.00 | -51.50 |
| 267 | 114.00 | 255.00 | 0.00 | -50.50 |
| 268 | 114.00 | 256.00 | 0.00 | -49.50 |
| 269 | 114.00 | 257.00 | 0.00 | -48.50 |
| 270 | 114.00 | 258.00 | 0.00 | -47.50 |
| 271 | 114.00 | 259.00 | 0.00 | -46.50 |
| 272 | 114.00 | 260.00 | 0.00 | -45.50 |
| 273 | 114.00 | 261.00 | 0.00 | -44.50 |
| 274 | 114.00 | 262.00 | 0.00 | -43.50 |
| 275 | 114.00 | 263.00 | 0.00 | -42.50 |
| 276 | 114.00 | 264.00 | 0.00 | -41.50 |
| 277 | 114.00 | 265.00 | 0.00 | -40.50 |
| 278 | 114.00 | 266.00 | 0.00 | -39.50 |
| 279 | 114.00 | 267.00 | 0.00 | -38.50 |
| 280 | 114.00 | 268.00 | 0.00 | -37.50 |
| 281 | 114.00 | 269.00 | 0.00 | -36.50 |
| 282 | 114.00 | 270.00 | 0.00 | -35.50 |
| 283 | 114.00 | 271.00 | 0.00 | -34.50 |
| 284 | 115.00 | 272.00 | 1.00 | -33.50 |
| 285 | 115.00 | 273.00 | 1.00 | -32.50 |
| 286 | 115.00 | 274.00 | 1.00 | -31.50 |
| 287 | 115.00 | 275.00 | 1.00 | -30.50 |
| 288 | 115.00 | 276.00 | 1.00 | -29.50 |
| 289 | 115.00 | 277.00 | 1.00 | -28.50 |
| 290 | 115.00 | 278.00 | 1.00 | -27.50 |
| 291 | 115.00 | 279.00 | 1.00 | -26.50 |
| 292 | 116.00 | 280.00 | 2.00 | -25.50 |
| 293 | 116.00 | 281.00 | 2.00 | -24.50 |
| 294 | 116.00 | 282.00 | 2.00 | -23.50 |
| 295 | 116.00 | 283.00 | 2.00 | -22.50 |
| 296 | 116.00 | 284.00 | 2.00 | -21.50 |
| 297 | 116.00 | 285.00 | 2.00 | -20.50 |
| 298 | 116.00 | 286.00 | 2.00 | -19.50 |
| 299 | 116.00 | 287.00 | 2.00 | -18.50 |
| 300 | 117.00 | 288.00 | 3.00 | -17.50 |
| 301 | 117.00 | 289.00 | 3.00 | -16.50 |
| 302 | 117.00 | 290.00 | 3.00 | -15.50 |
| 303 | 117.00 | 291.00 | 3.00 | -14.50 |
| 304 | 117.00 | 292.00 | 3.00 | -13.50 |
| 305 | 118.00 | 293.00 | 4.00 | -12.50 |
| 306 | 118.00 | 294.00 | 4.00 | -11.50 |
| 307 | 118.00 | 295.00 | 4.00 | -10.50 |
| 308 | 118.00 | 296.00 | 4.00 | -9.50 |
| 309 | 118.00 | 297.00 | 4.00 | -8.50 |
| 310 | 119.00 | 298.00 | 5.00 | -7.50 |
| 311 | 119.00 | 299.00 | 5.00 | -6.50 |
| 312 | 119.00 | 300.00 | 5.00 | -5.50 |
| 313 | 119.00 | 301.00 | 5.00 | -4.50 |
| 314 | 119.00 | 302.00 | 5.00 | -3.50 |
| 315 | 120.00 | 303.00 | 6.00 | -2.50 |
| 316 | 121.00 | 303.00 | 7.00 | -2.50 |
| 317 | 122.00 | 303.00 | 8.00 | -2.50 |
| 318 | 123.00 | 303.00 | 9.00 | -2.50 |
| 319 | 124.00 | 303.00 | 10.00 | -2.50 |
| 320 | 125.00 | 303.00 | 11.00 | -2.50 |
| 321 | 126.00 | 303.00 | 12.00 | -2.50 |
| 322 | 127.00 | 303.00 | 13.00 | -2.50 |
| 323 | 128.00 | 303.00 | 14.00 | -2.50 |
| 324 | 129.00 | 303.00 | 15.00 | -2.50 |
| 325 | 130.00 | 303.00 | 16.00 | -2.50 |
| 326 | 131.00 | 303.00 | 17.00 | -2.50 |
| 327 | 132.00 | 303.00 | 18.00 | -2.50 |
| 328 | 133.00 | 303.00 | 19.00 | -2.50 |
| 329 | 134.00 | 303.00 | 20.00 | -2.50 |
| 330 | 135.00 | 303.00 | 21.00 | -2.50 |
| 331 | 136.00 | 303.00 | 22.00 | -2.50 |
| 332 | 137.00 | 303.00 | 23.00 | -2.50 |
| 333 | 138.00 | 303.00 | 24.00 | -2.50 |
| 334 | 139.00 | 303.00 | 25.00 | -2.50 |
| 335 | 140.00 | 303.00 | 26.00 | -2.50 |
| 336 | 141.00 | 303.00 | 27.00 | -2.50 |
| 337 | 142.00 | 303.00 | 28.00 | -2.50 |
| 338 | 143.00 | 303.00 | 29.00 | -2.50 |
| 339 | 144.00 | 303.00 | 30.00 | -2.50 |
| 340 | 145.00 | 303.00 | 31.00 | -2.50 |
| 341 | 146.00 | 303.00 | 32.00 | -2.50 |
| 342 | 147.00 | 303.00 | 33.00 | -2.50 |
| 343 | 148.00 | 303.00 | 34.00 | -2.50 |
| 344 | 149.00 | 303.00 | 35.00 | -2.50 |
| 345 | 150.00 | 303.00 | 36.00 | -2.50 |
| 346 | 151.00 | 303.00 | 37.00 | -2.50 |
| 347 | 152.00 | 303.00 | 38.00 | -2.50 |
| 348 | 153.00 | 303.00 | 39.00 | -2.50 |
| 349 | 154.00 | 303.00 | 40.00 | -2.50 |
| 350 | 155.00 | 303.00 | 41.00 | -2.50 |
| 351 | 156.00 | 303.00 | 42.00 | -2.50 |
| 352 | 157.00 | 303.00 | 43.00 | -2.50 |
| 353 | 158.00 | 303.00 | 44.00 | -2.50 |
| 354 | 159.00 | 303.00 | 45.00 | -2.50 |
| 355 | 160.00 | 303.00 | 46.00 | -2.50 |
| 356 | 161.00 | 303.00 | 47.00 | -2.50 |
| 357 | 162.00 | 303.00 | 48.00 | -2.50 |
| 358 | 163.00 | 303.00 | 49.00 | -2.50 |
| 359 | 164.00 | 303.00 | 50.00 | -2.50 |
| 360 | 165.00 | 303.00 | 51.00 | -2.50 |
| 361 | 166.00 | 303.00 | 52.00 | -2.50 |
| 362 | 167.00 | 303.00 | 53.00 | -2.50 |
| 363 | 168.00 | 303.00 | 54.00 | -2.50 |
| 364 | 169.00 | 303.00 | 55.00 | -2.50 |
| 365 | 170.00 | 303.00 | 56.00 | -2.50 |
| 366 | 171.00 | 303.00 | 57.00 | -2.50 |
| 367 | 172.00 | 303.00 | 58.00 | -2.50 |
| 368 | 173.00 | 303.00 | 59.00 | -2.50 |
| 369 | 174.00 | 303.00 | 60.00 | -2.50 |
| 370 | 175.00 | 303.00 | 61.00 | -2.50 |
| 371 | 176.00 | 303.00 | 62.00 | -2.50 |
| 372 | 177.00 | 303.00 | 63.00 | -2.50 |
| 373 | 178.00 | 303.00 | 64.00 | -2.50 |
| 374 | 179.00 | 303.00 | 65.00 | -2.50 |
| 375 | 180.00 | 303.00 | 66.00 | -2.50 |
| 376 | 181.00 | 303.00 | 67.00 | -2.50 |
| 377 | 182.00 | 303.00 | 68.00 | -2.50 |
| 378 | 183.00 | 303.00 | 69.00 | -2.50 |
| 379 | 184.00 | 303.00 | 70.00 | -2.50 |
| 380 | 185.00 | 303.00 | 71.00 | -2.50 |
| 381 | 186.00 | 303.00 | 72.00 | -2.50 |
| 382 | 187.00 | 303.00 | 73.00 | -2.50 |
| 383 | 188.00 | 303.00 | 74.00 | -2.50 |
| 384 | 189.00 | 303.00 | 75.00 | -2.50 |
| 385 | 190.00 | 303.00 | 76.00 | -2.50 |
| 386 | 191.00 | 303.00 | 77.00 | -2.50 |
| 387 | 192.00 | 303.00 | 78.00 | -2.50 |
| 388 | 193.00 | 303.00 | 79.00 | -2.50 |
| 389 | 194.00 | 303.00 | 80.00 | -2.50 |
| 390 | 195.00 | 303.00 | 81.00 | -2.50 |
| 391 | 196.00 | 303.00 | 82.00 | -2.50 |
| 392 | 197.00 | 303.00 | 83.00 | -2.50 |
| 393 | 198.00 | 303.00 | 84.00 | -2.50 |
| 394 | 199.00 | 303.00 | 85.00 | -2.50 |
| 395 | 200.00 | 303.00 | 86.00 | -2.50 |
| 396 | 201.00 | 303.00 | 87.00 | -2.50 |
| 397 | 202.00 | 303.00 | 88.00 | -2.50 |
| 398 | 203.00 | 303.00 | 89.00 | -2.50 |
| 399 | 204.00 | 303.00 | 90.00 | -2.50 |
| 400 | 205.00 | 303.00 | 91.00 | -2.50 |
| 401 | 206.00 | 303.00 | 92.00 | -2.50 |
| 402 | 207.00 | 303.00 | 93.00 | -2.50 |
| 403 | 208.00 | 303.00 | 94.00 | -2.50 |
| 404 | 209.00 | 303.00 | 95.00 | -2.50 |
| 405 | 210.00 | 303.00 | 96.00 | -2.50 |
| 406 | 211.00 | 303.00 | 97.00 | -2.50 |
| 407 | 212.00 | 303.00 | 98.00 | -2.50 |
| 408 | 213.00 | 303.00 | 99.00 | -2.50 |
| 409 | 214.00 | 303.00 | 100.00 | -2.50 |
| 410 | 215.00 | 303.00 | 101.00 | -2.50 |
| 411 | 216.00 | 303.00 | 102.00 | -2.50 |
| 412 | 217.00 | 303.00 | 103.00 | -2.50 |
| 413 | 218.00 | 303.00 | 104.00 | -2.50 |
| 414 | 219.00 | 303.00 | 105.00 | -2.50 |
| 415 | 220.00 | 303.00 | 106.00 | -2.50 |
| 416 | 221.00 | 303.00 | 107.00 | -2.50 |
| 417 | 222.00 | 303.00 | 108.00 | -2.50 |
| 418 | 223.00 | 303.00 | 109.00 | -2.50 |
| 419 | 224.00 | 303.00 | 110.00 | -2.50 |
| 420 | 225.00 | 303.00 | 111.00 | -2.50 |
| 421 | 226.00 | 303.00 | 112.00 | -2.50 |
| 422 | 227.00 | 303.00 | 113.00 | -2.50 |
| 423 | 228.00 | 303.00 | 114.00 | -2.50 |
| 424 | 229.00 | 303.00 | 115.00 | -2.50 |
| 425 | 230.00 | 303.00 | 116.00 | -2.50 |
| 426 | 231.00 | 303.00 | 117.00 | -2.50 |
| 427 | 232.00 | 303.00 | 118.00 | -2.50 |
| 428 | 233.00 | 303.00 | 119.00 | -2.50 |
| 429 | 234.00 | 303.00 | 120.00 | -2.50 |
| 430 | 235.00 | 303.00 | 121.00 | -2.50 |
| 431 | 236.00 | 303.00 | 122.00 | -2.50 |
| 432 | 237.00 | 303.00 | 123.00 | -2.50 |
| 433 | 238.00 | 303.00 | 124.00 | -2.50 |
| 434 | 239.00 | 303.00 | 125.00 | -2.50 |
| 435 | 240.00 | 303.00 | 126.00 | -2.50 |
| 436 | 241.00 | 303.00 | 127.00 | -2.50 |
| 437 | 242.00 | 303.00 | 128.00 | -2.50 |
| 438 | 243.00 | 303.00 | 129.00 | -2.50 |
| 439 | 244.00 | 303.00 | 130.00 | -2.50 |
| 440 | 245.00 | 303.00 | 131.00 | -2.50 |
| 441 | 246.00 | 303.00 | 132.00 | -2.50 |
| 442 | 247.00 | 303.00 | 133.00 | -2.50 |
| 443 | 248.00 | 303.00 | 134.00 | -2.50 |
| 444 | 249.00 | 303.00 | 135.00 | -2.50 |
| 445 | 250.00 | 303.00 | 136.00 | -2.50 |
| 446 | 251.00 | 303.00 | 137.00 | -2.50 |
| 447 | 252.00 | 303.00 | 138.00 | -2.50 |
| 448 | 253.00 | 303.00 | 139.00 | -2.50 |
| 449 | 254.00 | 303.00 | 140.00 | -2.50 |
| 450 | 255.00 | 303.00 | 141.00 | -2.50 |
| 451 | 256.00 | 303.00 | 142.00 | -2.50 |
| 452 | 257.00 | 303.00 | 143.00 | -2.50 |
| 453 | 258.00 | 303.00 | 144.00 | -2.50 |
| 454 | 259.00 | 303.00 | 145.00 | -2.50 |
| 455 | 260.00 | 303.00 | 146.00 | -2.50 |
| 456 | 261.00 | 303.00 | 147.00 | -2.50 |
| 457 | 262.00 | 303.00 | 148.00 | -2.50 |
| 458 | 263.00 | 303.00 | 149.00 | -2.50 |
| 459 | 264.00 | 303.00 | 150.00 | -2.50 |
| 460 | 265.00 | 303.00 | 151.00 | -2.50 |
| 461 | 266.00 | 303.00 | 152.00 | -2.50 |
| 462 | 267.00 | 303.00 | 153.00 | -2.50 |
| 463 | 268.00 | 303.00 | 154.00 | -2.50 |
| 464 | 269.00 | 303.00 | 155.00 | -2.50 |
| 465 | 270.00 | 303.00 | 156.00 | -2.50 |
| 466 | 271.00 | 303.00 | 157.00 | -2.50 |
| 467 | 272.00 | 303.00 | 158.00 | -2.50 |
| 468 | 273.00 | 303.00 | 159.00 | -2.50 |
| 469 | 274.00 | 303.00 | 160.00 | -2.50 |
| 470 | 275.00 | 303.00 | 161.00 | -2.50 |
| 471 | 276.00 | 303.00 | 162.00 | -2.50 |
| 472 | 277.00 | 303.00 | 163.00 | -2.50 |
| 473 | 278.00 | 303.00 | 164.00 | -2.50 |
| 474 | 279.00 | 303.00 | 165.00 | -2.50 |
| 475 | 280.00 | 303.00 | 166.00 | -2.50 |
| 476 | 281.00 | 303.00 | 167.00 | -2.50 |
| 477 | 282.00 | 303.00 | 168.00 | -2.50 |
| 478 | 283.00 | 303.00 | 169.00 | -2.50 |
| 479 | 284.00 | 303.00 | 170.00 | -2.50 |
| 480 | 285.00 | 303.00 | 171.00 | -2.50 |
| 481 | 286.00 | 303.00 | 172.00 | -2.50 |
| 482 | 287.00 | 303.00 | 173.00 | -2.50 |
| 483 | 288.00 | 303.00 | 174.00 | -2.50 |
| 484 | 289.00 | 303.00 | 175.00 | -2.50 |
| 485 | 290.00 | 303.00 | 176.00 | -2.50 |
| 486 | 291.00 | 303.00 | 177.00 | -2.50 |
| 487 | 292.00 | 303.00 | 178.00 | -2.50 |
| 488 | 293.00 | 303.00 | 179.00 | -2.50 |
| 489 | 294.00 | 303.00 | 180.00 | -2.50 |
| 490 | 295.00 | 303.00 | 181.00 | -2.50 |
| 491 | 296.00 | 303.00 | 182.00 | -2.50 |
| 492 | 297.00 | 303.00 | 183.00 | -2.50 |
| 493 | 298.00 | 303.00 | 184.00 | -2.50 |
| 494 | 299.00 | 303.00 | 185.00 | -2.50 |
| 495 | 300.00 | 303.00 | 186.00 | -2.50 |
| 496 | 301.00 | 303.00 | 187.00 | -2.50 |
| 497 | 302.00 | 303.00 | 188.00 | -2.50 |
| 498 | 303.00 | 303.00 | 189.00 | -2.50 |
| 499 | 304.00 | 303.00 | 190.00 | -2.50 |
| 500 | 305.00 | 303.00 | 191.00 | -2.50 |
| 501 | 306.00 | 303.00 | 192.00 | -2.50 |
| 502 | 307.00 | 303.00 | 193.00 | -2.50 |
| 503 | 308.00 | 303.00 | 194.00 | -2.50 |
| 504 | 309.00 | 303.00 | 195.00 | -2.50 |
| 505 | 310.00 | 303.00 | 196.00 | -2.50 |
| 506 | 311.00 | 303.00 | 197.00 | -2.50 |
| 507 | 312.00 | 303.00 | 198.00 | -2.50 |
| 508 | 313.00 | 303.00 | 199.00 | -2.50 |
| 509 | 314.00 | 303.00 | 200.00 | -2.50 |
| 510 | 315.00 | 303.00 | 201.00 | -2.50 |
| 511 | 316.00 | 303.00 | 202.00 | -2.50 |

- primeiro índice: 181
- último índice: 511
- quantidade: 331
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![75_geo esq](audit_outputs/75_geo_esq_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![75_geo esq polyfit](audit_outputs/75_geo_esq_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.

### Lado: dir

#### Etapa 1 — Entrada de _selecionar_pontos_lado()

- quantidade total de pontos do contorno: 1063
- ponto de contato recebido: [519.0, 303.0]
- baseline_y: 303.0
- baseline_ajustada: 305.5
- lado solicitado: dir
- largura da região: 137 px
- altura da gota: 250.00 px

#### Etapa 2 — Processo interno de seleção

| índice | x | y | dist. contato | dist. baseline | aceito | motivo |
|---|---:|---:|---:|---:|---|---|
| 0 | 297.00 | 53.00 | 334.34 | 252.50 | NÃO | fora da faixa vertical |
| 1 | 296.00 | 54.00 | 334.26 | 251.50 | NÃO | fora da faixa vertical |
| 2 | 295.00 | 54.00 | 334.93 | 251.50 | NÃO | fora da faixa vertical |
| 3 | 294.00 | 54.00 | 335.60 | 251.50 | NÃO | fora da faixa vertical |
| 4 | 293.00 | 54.00 | 336.27 | 251.50 | NÃO | fora da faixa vertical |
| 5 | 292.00 | 54.00 | 336.94 | 251.50 | NÃO | fora da faixa vertical |
| 6 | 291.00 | 54.00 | 337.62 | 251.50 | NÃO | fora da faixa vertical |
| 7 | 290.00 | 54.00 | 338.29 | 251.50 | NÃO | fora da faixa vertical |
| 8 | 289.00 | 54.00 | 338.97 | 251.50 | NÃO | fora da faixa vertical |
| 9 | 288.00 | 55.00 | 338.92 | 250.50 | NÃO | fora da faixa vertical |
| 10 | 287.00 | 55.00 | 339.60 | 250.50 | NÃO | fora da faixa vertical |
| 11 | 286.00 | 55.00 | 340.28 | 250.50 | NÃO | fora da faixa vertical |
| 12 | 285.00 | 55.00 | 340.97 | 250.50 | NÃO | fora da faixa vertical |
| 13 | 284.00 | 55.00 | 341.66 | 250.50 | NÃO | fora da faixa vertical |
| 14 | 283.00 | 55.00 | 342.34 | 250.50 | NÃO | fora da faixa vertical |
| 15 | 282.00 | 55.00 | 343.03 | 250.50 | NÃO | fora da faixa vertical |
| 16 | 281.00 | 56.00 | 343.01 | 249.50 | NÃO | fora da faixa vertical |
| 17 | 280.00 | 56.00 | 343.70 | 249.50 | NÃO | fora da faixa vertical |
| 18 | 279.00 | 56.00 | 344.40 | 249.50 | NÃO | fora da faixa vertical |
| 19 | 278.00 | 56.00 | 345.09 | 249.50 | NÃO | fora da faixa vertical |
| 20 | 277.00 | 56.00 | 345.79 | 249.50 | NÃO | fora da faixa vertical |
| 21 | 276.00 | 57.00 | 345.78 | 248.50 | NÃO | fora da faixa vertical |
| 22 | 275.00 | 57.00 | 346.49 | 248.50 | NÃO | fora da faixa vertical |
| 23 | 274.00 | 57.00 | 347.19 | 248.50 | NÃO | fora da faixa vertical |
| 24 | 273.00 | 57.00 | 347.90 | 248.50 | NÃO | fora da faixa vertical |
| 25 | 272.00 | 57.00 | 348.60 | 248.50 | NÃO | fora da faixa vertical |
| 26 | 271.00 | 58.00 | 348.61 | 247.50 | NÃO | fora da faixa vertical |
| 27 | 270.00 | 58.00 | 349.32 | 247.50 | NÃO | fora da faixa vertical |
| 28 | 269.00 | 58.00 | 350.04 | 247.50 | NÃO | fora da faixa vertical |
| 29 | 268.00 | 58.00 | 350.75 | 247.50 | NÃO | fora da faixa vertical |
| 30 | 267.00 | 59.00 | 350.77 | 246.50 | NÃO | fora da faixa vertical |
| 31 | 266.00 | 59.00 | 351.49 | 246.50 | NÃO | fora da faixa vertical |
| 32 | 265.00 | 59.00 | 352.21 | 246.50 | NÃO | fora da faixa vertical |
| 33 | 264.00 | 59.00 | 352.93 | 246.50 | NÃO | fora da faixa vertical |
| 34 | 263.00 | 60.00 | 352.97 | 245.50 | NÃO | fora da faixa vertical |
| 35 | 262.00 | 60.00 | 353.69 | 245.50 | NÃO | fora da faixa vertical |
| 36 | 261.00 | 60.00 | 354.42 | 245.50 | NÃO | fora da faixa vertical |
| 37 | 260.00 | 61.00 | 354.46 | 244.50 | NÃO | fora da faixa vertical |
| 38 | 259.00 | 61.00 | 355.20 | 244.50 | NÃO | fora da faixa vertical |
| 39 | 258.00 | 61.00 | 355.93 | 244.50 | NÃO | fora da faixa vertical |
| 40 | 257.00 | 62.00 | 355.98 | 243.50 | NÃO | fora da faixa vertical |
| 41 | 256.00 | 62.00 | 356.72 | 243.50 | NÃO | fora da faixa vertical |
| 42 | 255.00 | 62.00 | 357.46 | 243.50 | NÃO | fora da faixa vertical |
| 43 | 254.00 | 62.00 | 358.20 | 243.50 | NÃO | fora da faixa vertical |
| 44 | 253.00 | 63.00 | 358.27 | 242.50 | NÃO | fora da faixa vertical |
| 45 | 252.00 | 63.00 | 359.01 | 242.50 | NÃO | fora da faixa vertical |
| 46 | 251.00 | 63.00 | 359.76 | 242.50 | NÃO | fora da faixa vertical |
| 47 | 250.00 | 64.00 | 359.84 | 241.50 | NÃO | fora da faixa vertical |
| 48 | 249.00 | 64.00 | 360.58 | 241.50 | NÃO | fora da faixa vertical |
| 49 | 248.00 | 65.00 | 360.67 | 240.50 | NÃO | fora da faixa vertical |
| 50 | 247.00 | 65.00 | 361.42 | 240.50 | NÃO | fora da faixa vertical |
| 51 | 246.00 | 65.00 | 362.18 | 240.50 | NÃO | fora da faixa vertical |
| 52 | 245.00 | 66.00 | 362.28 | 239.50 | NÃO | fora da faixa vertical |
| 53 | 244.00 | 66.00 | 363.03 | 239.50 | NÃO | fora da faixa vertical |
| 54 | 243.00 | 66.00 | 363.79 | 239.50 | NÃO | fora da faixa vertical |
| 55 | 242.00 | 67.00 | 363.90 | 238.50 | NÃO | fora da faixa vertical |
| 56 | 241.00 | 67.00 | 364.66 | 238.50 | NÃO | fora da faixa vertical |
| 57 | 240.00 | 68.00 | 364.78 | 237.50 | NÃO | fora da faixa vertical |
| 58 | 239.00 | 68.00 | 365.55 | 237.50 | NÃO | fora da faixa vertical |
| 59 | 238.00 | 68.00 | 366.31 | 237.50 | NÃO | fora da faixa vertical |
| 60 | 237.00 | 69.00 | 366.44 | 236.50 | NÃO | fora da faixa vertical |
| 61 | 236.00 | 69.00 | 367.21 | 236.50 | NÃO | fora da faixa vertical |
| 62 | 235.00 | 70.00 | 367.35 | 235.50 | NÃO | fora da faixa vertical |
| 63 | 234.00 | 70.00 | 368.12 | 235.50 | NÃO | fora da faixa vertical |
| 64 | 233.00 | 71.00 | 368.27 | 234.50 | NÃO | fora da faixa vertical |
| 65 | 232.00 | 71.00 | 369.04 | 234.50 | NÃO | fora da faixa vertical |
| 66 | 231.00 | 72.00 | 369.20 | 233.50 | NÃO | fora da faixa vertical |
| 67 | 230.00 | 72.00 | 369.98 | 233.50 | NÃO | fora da faixa vertical |
| 68 | 229.00 | 73.00 | 370.14 | 232.50 | NÃO | fora da faixa vertical |
| 69 | 228.00 | 73.00 | 370.92 | 232.50 | NÃO | fora da faixa vertical |
| 70 | 227.00 | 74.00 | 371.09 | 231.50 | NÃO | fora da faixa vertical |
| 71 | 226.00 | 74.00 | 371.87 | 231.50 | NÃO | fora da faixa vertical |
| 72 | 225.00 | 74.00 | 372.66 | 231.50 | NÃO | fora da faixa vertical |
| 73 | 224.00 | 75.00 | 372.84 | 230.50 | NÃO | fora da faixa vertical |
| 74 | 223.00 | 75.00 | 373.63 | 230.50 | NÃO | fora da faixa vertical |
| 75 | 222.00 | 76.00 | 373.82 | 229.50 | NÃO | fora da faixa vertical |
| 76 | 221.00 | 76.00 | 374.61 | 229.50 | NÃO | fora da faixa vertical |
| 77 | 220.00 | 77.00 | 374.80 | 228.50 | NÃO | fora da faixa vertical |
| 78 | 219.00 | 77.00 | 375.60 | 228.50 | NÃO | fora da faixa vertical |
| 79 | 218.00 | 78.00 | 375.80 | 227.50 | NÃO | fora da faixa vertical |
| 80 | 217.00 | 79.00 | 376.01 | 226.50 | NÃO | fora da faixa vertical |
| 81 | 216.00 | 79.00 | 376.81 | 226.50 | NÃO | fora da faixa vertical |
| 82 | 215.00 | 80.00 | 377.02 | 225.50 | NÃO | fora da faixa vertical |
| 83 | 214.00 | 80.00 | 377.83 | 225.50 | NÃO | fora da faixa vertical |
| 84 | 213.00 | 81.00 | 378.05 | 224.50 | NÃO | fora da faixa vertical |
| 85 | 212.00 | 82.00 | 378.27 | 223.50 | NÃO | fora da faixa vertical |
| 86 | 211.00 | 82.00 | 379.08 | 223.50 | NÃO | fora da faixa vertical |
| 87 | 210.00 | 83.00 | 379.32 | 222.50 | NÃO | fora da faixa vertical |
| 88 | 209.00 | 83.00 | 380.13 | 222.50 | NÃO | fora da faixa vertical |
| 89 | 208.00 | 84.00 | 380.37 | 221.50 | NÃO | fora da faixa vertical |
| 90 | 207.00 | 85.00 | 380.62 | 220.50 | NÃO | fora da faixa vertical |
| 91 | 206.00 | 85.00 | 381.44 | 220.50 | NÃO | fora da faixa vertical |
| 92 | 205.00 | 86.00 | 381.69 | 219.50 | NÃO | fora da faixa vertical |
| 93 | 204.00 | 86.00 | 382.51 | 219.50 | NÃO | fora da faixa vertical |
| 94 | 203.00 | 87.00 | 382.77 | 218.50 | NÃO | fora da faixa vertical |
| 95 | 202.00 | 88.00 | 383.03 | 217.50 | NÃO | fora da faixa vertical |
| 96 | 201.00 | 89.00 | 383.30 | 216.50 | NÃO | fora da faixa vertical |
| 97 | 200.00 | 89.00 | 384.13 | 216.50 | NÃO | fora da faixa vertical |
| 98 | 199.00 | 90.00 | 384.41 | 215.50 | NÃO | fora da faixa vertical |
| 99 | 198.00 | 91.00 | 384.69 | 214.50 | NÃO | fora da faixa vertical |
| 100 | 197.00 | 92.00 | 384.97 | 213.50 | NÃO | fora da faixa vertical |
| 101 | 196.00 | 92.00 | 385.81 | 213.50 | NÃO | fora da faixa vertical |
| 102 | 195.00 | 93.00 | 386.10 | 212.50 | NÃO | fora da faixa vertical |
| 103 | 194.00 | 94.00 | 386.40 | 211.50 | NÃO | fora da faixa vertical |
| 104 | 193.00 | 95.00 | 386.70 | 210.50 | NÃO | fora da faixa vertical |
| 105 | 192.00 | 95.00 | 387.55 | 210.50 | NÃO | fora da faixa vertical |
| 106 | 191.00 | 96.00 | 387.86 | 209.50 | NÃO | fora da faixa vertical |
| 107 | 190.00 | 97.00 | 388.17 | 208.50 | NÃO | fora da faixa vertical |
| 108 | 189.00 | 98.00 | 388.49 | 207.50 | NÃO | fora da faixa vertical |
| 109 | 188.00 | 98.00 | 389.34 | 207.50 | NÃO | fora da faixa vertical |
| 110 | 187.00 | 99.00 | 389.67 | 206.50 | NÃO | fora da faixa vertical |
| 111 | 186.00 | 100.00 | 390.00 | 205.50 | NÃO | fora da faixa vertical |
| 112 | 185.00 | 101.00 | 390.33 | 204.50 | NÃO | fora da faixa vertical |
| 113 | 184.00 | 102.00 | 390.67 | 203.50 | NÃO | fora da faixa vertical |
| 114 | 183.00 | 103.00 | 391.02 | 202.50 | NÃO | fora da faixa vertical |
| 115 | 182.00 | 104.00 | 391.37 | 201.50 | NÃO | fora da faixa vertical |
| 116 | 181.00 | 105.00 | 391.72 | 200.50 | NÃO | fora da faixa vertical |
| 117 | 180.00 | 105.00 | 392.59 | 200.50 | NÃO | fora da faixa vertical |
| 118 | 179.00 | 106.00 | 392.95 | 199.50 | NÃO | fora da faixa vertical |
| 119 | 178.00 | 107.00 | 393.32 | 198.50 | NÃO | fora da faixa vertical |
| 120 | 177.00 | 108.00 | 393.69 | 197.50 | NÃO | fora da faixa vertical |
| 121 | 176.00 | 109.00 | 394.06 | 196.50 | NÃO | fora da faixa vertical |
| 122 | 175.00 | 110.00 | 394.44 | 195.50 | NÃO | fora da faixa vertical |
| 123 | 174.00 | 111.00 | 394.83 | 194.50 | NÃO | fora da faixa vertical |
| 124 | 173.00 | 112.00 | 395.22 | 193.50 | NÃO | fora da faixa vertical |
| 125 | 172.00 | 113.00 | 395.61 | 192.50 | NÃO | fora da faixa vertical |
| 126 | 171.00 | 114.00 | 396.01 | 191.50 | NÃO | fora da faixa vertical |
| 127 | 170.00 | 115.00 | 396.42 | 190.50 | NÃO | fora da faixa vertical |
| 128 | 169.00 | 116.00 | 396.82 | 189.50 | NÃO | fora da faixa vertical |
| 129 | 169.00 | 117.00 | 396.35 | 188.50 | NÃO | fora da faixa vertical |
| 130 | 168.00 | 118.00 | 396.77 | 187.50 | NÃO | fora da faixa vertical |
| 131 | 167.00 | 119.00 | 397.19 | 186.50 | NÃO | fora da faixa vertical |
| 132 | 166.00 | 120.00 | 397.62 | 185.50 | NÃO | fora da faixa vertical |
| 133 | 165.00 | 121.00 | 398.05 | 184.50 | NÃO | fora da faixa vertical |
| 134 | 164.00 | 122.00 | 398.48 | 183.50 | NÃO | fora da faixa vertical |
| 135 | 163.00 | 123.00 | 398.92 | 182.50 | NÃO | fora da faixa vertical |
| 136 | 162.00 | 124.00 | 399.36 | 181.50 | NÃO | fora da faixa vertical |
| 137 | 161.00 | 125.00 | 399.81 | 180.50 | NÃO | fora da faixa vertical |
| 138 | 160.00 | 126.00 | 400.26 | 179.50 | NÃO | fora da faixa vertical |
| 139 | 160.00 | 127.00 | 399.82 | 178.50 | NÃO | fora da faixa vertical |
| 140 | 159.00 | 128.00 | 400.28 | 177.50 | NÃO | fora da faixa vertical |
| 141 | 158.00 | 129.00 | 400.75 | 176.50 | NÃO | fora da faixa vertical |
| 142 | 157.00 | 130.00 | 401.21 | 175.50 | NÃO | fora da faixa vertical |
| 143 | 157.00 | 131.00 | 400.78 | 174.50 | NÃO | fora da faixa vertical |
| 144 | 156.00 | 132.00 | 401.26 | 173.50 | NÃO | fora da faixa vertical |
| 145 | 155.00 | 133.00 | 401.74 | 172.50 | NÃO | fora da faixa vertical |
| 146 | 154.00 | 134.00 | 402.23 | 171.50 | NÃO | fora da faixa vertical |
| 147 | 154.00 | 135.00 | 401.81 | 170.50 | NÃO | fora da faixa vertical |
| 148 | 153.00 | 136.00 | 402.30 | 169.50 | NÃO | fora da faixa vertical |
| 149 | 152.00 | 137.00 | 402.80 | 168.50 | NÃO | fora da faixa vertical |
| 150 | 151.00 | 138.00 | 403.30 | 167.50 | NÃO | fora da faixa vertical |
| 151 | 151.00 | 139.00 | 402.89 | 166.50 | NÃO | fora da faixa vertical |
| 152 | 150.00 | 140.00 | 403.40 | 165.50 | NÃO | fora da faixa vertical |
| 153 | 149.00 | 141.00 | 403.91 | 164.50 | NÃO | fora da faixa vertical |
| 154 | 148.00 | 142.00 | 404.43 | 163.50 | NÃO | fora da faixa vertical |
| 155 | 148.00 | 143.00 | 404.03 | 162.50 | NÃO | fora da faixa vertical |
| 156 | 147.00 | 144.00 | 404.56 | 161.50 | NÃO | fora da faixa vertical |
| 157 | 146.00 | 145.00 | 405.08 | 160.50 | NÃO | fora da faixa vertical |
| 158 | 146.00 | 146.00 | 404.69 | 159.50 | NÃO | fora da faixa vertical |
| 159 | 145.00 | 147.00 | 405.23 | 158.50 | NÃO | fora da faixa vertical |
| 160 | 145.00 | 148.00 | 404.85 | 157.50 | NÃO | fora da faixa vertical |
| 161 | 144.00 | 149.00 | 405.39 | 156.50 | NÃO | fora da faixa vertical |
| 162 | 143.00 | 150.00 | 405.94 | 155.50 | NÃO | fora da faixa vertical |
| 163 | 143.00 | 151.00 | 405.56 | 154.50 | NÃO | fora da faixa vertical |
| 164 | 142.00 | 152.00 | 406.12 | 153.50 | NÃO | fora da faixa vertical |
| 165 | 141.00 | 153.00 | 406.67 | 152.50 | NÃO | fora da faixa vertical |
| 166 | 141.00 | 154.00 | 406.31 | 151.50 | NÃO | fora da faixa vertical |
| 167 | 140.00 | 155.00 | 406.87 | 150.50 | NÃO | fora da faixa vertical |
| 168 | 140.00 | 156.00 | 406.51 | 149.50 | NÃO | fora da faixa vertical |
| 169 | 139.00 | 157.00 | 407.08 | 148.50 | NÃO | fora da faixa vertical |
| 170 | 138.00 | 158.00 | 407.66 | 147.50 | NÃO | fora da faixa vertical |
| 171 | 138.00 | 159.00 | 407.30 | 146.50 | NÃO | fora da faixa vertical |
| 172 | 137.00 | 160.00 | 407.89 | 145.50 | NÃO | fora da faixa vertical |
| 173 | 137.00 | 161.00 | 407.54 | 144.50 | NÃO | fora da faixa vertical |
| 174 | 136.00 | 162.00 | 408.13 | 143.50 | NÃO | fora da faixa vertical |
| 175 | 136.00 | 163.00 | 407.79 | 142.50 | NÃO | fora da faixa vertical |
| 176 | 135.00 | 164.00 | 408.38 | 141.50 | NÃO | fora da faixa vertical |
| 177 | 135.00 | 165.00 | 408.04 | 140.50 | NÃO | fora da faixa vertical |
| 178 | 135.00 | 166.00 | 407.71 | 139.50 | NÃO | fora da faixa vertical |
| 179 | 134.00 | 167.00 | 408.31 | 138.50 | NÃO | fora da faixa vertical |
| 180 | 134.00 | 168.00 | 407.98 | 137.50 | NÃO | fora da faixa vertical |
| 181 | 133.00 | 169.00 | 408.60 | 136.50 | NÃO | fora do lado solicitado |
| 182 | 133.00 | 170.00 | 408.27 | 135.50 | NÃO | fora do lado solicitado |
| 183 | 132.00 | 171.00 | 408.89 | 134.50 | NÃO | fora do lado solicitado |
| 184 | 132.00 | 172.00 | 408.57 | 133.50 | NÃO | fora do lado solicitado |
| 185 | 131.00 | 173.00 | 409.20 | 132.50 | NÃO | fora do lado solicitado |
| 186 | 131.00 | 174.00 | 408.88 | 131.50 | NÃO | fora do lado solicitado |
| 187 | 130.00 | 175.00 | 409.52 | 130.50 | NÃO | fora do lado solicitado |
| 188 | 130.00 | 176.00 | 409.21 | 129.50 | NÃO | fora do lado solicitado |
| 189 | 129.00 | 177.00 | 409.85 | 128.50 | NÃO | fora do lado solicitado |
| 190 | 129.00 | 178.00 | 409.54 | 127.50 | NÃO | fora do lado solicitado |
| 191 | 129.00 | 179.00 | 409.24 | 126.50 | NÃO | fora do lado solicitado |
| 192 | 128.00 | 180.00 | 409.89 | 125.50 | NÃO | fora do lado solicitado |
| 193 | 128.00 | 181.00 | 409.59 | 124.50 | NÃO | fora do lado solicitado |
| 194 | 127.00 | 182.00 | 410.25 | 123.50 | NÃO | fora do lado solicitado |
| 195 | 127.00 | 183.00 | 409.96 | 122.50 | NÃO | fora do lado solicitado |
| 196 | 127.00 | 184.00 | 409.66 | 121.50 | NÃO | fora do lado solicitado |
| 197 | 126.00 | 185.00 | 410.33 | 120.50 | NÃO | fora do lado solicitado |
| 198 | 126.00 | 186.00 | 410.05 | 119.50 | NÃO | fora do lado solicitado |
| 199 | 126.00 | 187.00 | 409.76 | 118.50 | NÃO | fora do lado solicitado |
| 200 | 125.00 | 188.00 | 410.44 | 117.50 | NÃO | fora do lado solicitado |
| 201 | 125.00 | 189.00 | 410.16 | 116.50 | NÃO | fora do lado solicitado |
| 202 | 124.00 | 190.00 | 410.85 | 115.50 | NÃO | fora do lado solicitado |
| 203 | 124.00 | 191.00 | 410.57 | 114.50 | NÃO | fora do lado solicitado |
| 204 | 124.00 | 192.00 | 410.30 | 113.50 | NÃO | fora do lado solicitado |
| 205 | 124.00 | 193.00 | 410.03 | 112.50 | NÃO | fora do lado solicitado |
| 206 | 123.00 | 194.00 | 410.73 | 111.50 | NÃO | fora do lado solicitado |
| 207 | 123.00 | 195.00 | 410.46 | 110.50 | NÃO | fora do lado solicitado |
| 208 | 123.00 | 196.00 | 410.20 | 109.50 | NÃO | fora do lado solicitado |
| 209 | 122.00 | 197.00 | 410.91 | 108.50 | NÃO | fora do lado solicitado |
| 210 | 122.00 | 198.00 | 410.65 | 107.50 | NÃO | fora do lado solicitado |
| 211 | 122.00 | 199.00 | 410.40 | 106.50 | NÃO | fora do lado solicitado |
| 212 | 122.00 | 200.00 | 410.14 | 105.50 | NÃO | fora do lado solicitado |
| 213 | 121.00 | 201.00 | 410.86 | 104.50 | NÃO | fora do lado solicitado |
| 214 | 121.00 | 202.00 | 410.62 | 103.50 | NÃO | fora do lado solicitado |
| 215 | 121.00 | 203.00 | 410.37 | 102.50 | NÃO | fora do lado solicitado |
| 216 | 120.00 | 204.00 | 411.10 | 101.50 | NÃO | fora do lado solicitado |
| 217 | 120.00 | 205.00 | 410.86 | 100.50 | NÃO | fora do lado solicitado |
| 218 | 120.00 | 206.00 | 410.62 | 99.50 | NÃO | fora do lado solicitado |
| 219 | 120.00 | 207.00 | 410.39 | 98.50 | NÃO | fora do lado solicitado |
| 220 | 119.00 | 208.00 | 411.13 | 97.50 | NÃO | fora do lado solicitado |
| 221 | 119.00 | 209.00 | 410.90 | 96.50 | NÃO | fora do lado solicitado |
| 222 | 119.00 | 210.00 | 410.67 | 95.50 | NÃO | fora do lado solicitado |
| 223 | 119.00 | 211.00 | 410.44 | 94.50 | NÃO | fora do lado solicitado |
| 224 | 119.00 | 212.00 | 410.22 | 93.50 | NÃO | fora do lado solicitado |
| 225 | 118.00 | 213.00 | 410.98 | 92.50 | NÃO | fora do lado solicitado |
| 226 | 118.00 | 214.00 | 410.76 | 91.50 | NÃO | fora do lado solicitado |
| 227 | 118.00 | 215.00 | 410.54 | 90.50 | NÃO | fora do lado solicitado |
| 228 | 118.00 | 216.00 | 410.33 | 89.50 | NÃO | fora do lado solicitado |
| 229 | 118.00 | 217.00 | 410.12 | 88.50 | NÃO | fora do lado solicitado |
| 230 | 117.00 | 218.00 | 410.89 | 87.50 | NÃO | fora do lado solicitado |
| 231 | 117.00 | 219.00 | 410.68 | 86.50 | NÃO | fora do lado solicitado |
| 232 | 117.00 | 220.00 | 410.48 | 85.50 | NÃO | fora do lado solicitado |
| 233 | 117.00 | 221.00 | 410.28 | 84.50 | NÃO | fora do lado solicitado |
| 234 | 117.00 | 222.00 | 410.08 | 83.50 | NÃO | fora do lado solicitado |
| 235 | 116.00 | 223.00 | 410.86 | 82.50 | NÃO | fora do lado solicitado |
| 236 | 116.00 | 224.00 | 410.67 | 81.50 | NÃO | fora do lado solicitado |
| 237 | 116.00 | 225.00 | 410.48 | 80.50 | NÃO | fora do lado solicitado |
| 238 | 116.00 | 226.00 | 410.29 | 79.50 | NÃO | fora do lado solicitado |
| 239 | 116.00 | 227.00 | 410.10 | 78.50 | NÃO | fora do lado solicitado |
| 240 | 116.00 | 228.00 | 409.92 | 77.50 | NÃO | fora do lado solicitado |
| 241 | 116.00 | 229.00 | 409.74 | 76.50 | NÃO | fora do lado solicitado |
| 242 | 116.00 | 230.00 | 409.56 | 75.50 | NÃO | fora do lado solicitado |
| 243 | 115.00 | 231.00 | 410.37 | 74.50 | NÃO | fora do lado solicitado |
| 244 | 115.00 | 232.00 | 410.19 | 73.50 | NÃO | fora do lado solicitado |
| 245 | 115.00 | 233.00 | 410.02 | 72.50 | NÃO | fora do lado solicitado |
| 246 | 115.00 | 234.00 | 409.85 | 71.50 | NÃO | fora do lado solicitado |
| 247 | 115.00 | 235.00 | 409.68 | 70.50 | NÃO | fora do lado solicitado |
| 248 | 115.00 | 236.00 | 409.52 | 69.50 | NÃO | fora do lado solicitado |
| 249 | 115.00 | 237.00 | 409.36 | 68.50 | NÃO | fora do lado solicitado |
| 250 | 115.00 | 238.00 | 409.20 | 67.50 | NÃO | fora do lado solicitado |
| 251 | 115.00 | 239.00 | 409.04 | 66.50 | NÃO | fora do lado solicitado |
| 252 | 114.00 | 240.00 | 409.87 | 65.50 | NÃO | fora do lado solicitado |
| 253 | 114.00 | 241.00 | 409.72 | 64.50 | NÃO | fora do lado solicitado |
| 254 | 114.00 | 242.00 | 409.57 | 63.50 | NÃO | fora do lado solicitado |
| 255 | 114.00 | 243.00 | 409.42 | 62.50 | NÃO | fora do lado solicitado |
| 256 | 114.00 | 244.00 | 409.27 | 61.50 | NÃO | fora do lado solicitado |
| 257 | 114.00 | 245.00 | 409.13 | 60.50 | NÃO | fora do lado solicitado |
| 258 | 114.00 | 246.00 | 408.99 | 59.50 | NÃO | fora do lado solicitado |
| 259 | 114.00 | 247.00 | 408.85 | 58.50 | NÃO | fora do lado solicitado |
| 260 | 114.00 | 248.00 | 408.72 | 57.50 | NÃO | fora do lado solicitado |
| 261 | 114.00 | 249.00 | 408.58 | 56.50 | NÃO | fora do lado solicitado |
| 262 | 114.00 | 250.00 | 408.45 | 55.50 | NÃO | fora do lado solicitado |
| 263 | 114.00 | 251.00 | 408.32 | 54.50 | NÃO | fora do lado solicitado |
| 264 | 114.00 | 252.00 | 408.20 | 53.50 | NÃO | fora do lado solicitado |
| 265 | 114.00 | 253.00 | 408.07 | 52.50 | NÃO | fora do lado solicitado |
| 266 | 114.00 | 254.00 | 407.95 | 51.50 | NÃO | fora do lado solicitado |
| 267 | 114.00 | 255.00 | 407.83 | 50.50 | NÃO | fora do lado solicitado |
| 268 | 114.00 | 256.00 | 407.72 | 49.50 | NÃO | fora do lado solicitado |
| 269 | 114.00 | 257.00 | 407.60 | 48.50 | NÃO | fora do lado solicitado |
| 270 | 114.00 | 258.00 | 407.49 | 47.50 | NÃO | fora do lado solicitado |
| 271 | 114.00 | 259.00 | 407.38 | 46.50 | NÃO | fora do lado solicitado |
| 272 | 114.00 | 260.00 | 407.28 | 45.50 | NÃO | fora do lado solicitado |
| 273 | 114.00 | 261.00 | 407.17 | 44.50 | NÃO | fora do lado solicitado |
| 274 | 114.00 | 262.00 | 407.07 | 43.50 | NÃO | fora do lado solicitado |
| 275 | 114.00 | 263.00 | 406.97 | 42.50 | NÃO | fora do lado solicitado |
| 276 | 114.00 | 264.00 | 406.87 | 41.50 | NÃO | fora do lado solicitado |
| 277 | 114.00 | 265.00 | 406.78 | 40.50 | NÃO | fora do lado solicitado |
| 278 | 114.00 | 266.00 | 406.69 | 39.50 | NÃO | fora do lado solicitado |
| 279 | 114.00 | 267.00 | 406.60 | 38.50 | NÃO | fora do lado solicitado |
| 280 | 114.00 | 268.00 | 406.51 | 37.50 | NÃO | fora do lado solicitado |
| 281 | 114.00 | 269.00 | 406.42 | 36.50 | NÃO | fora do lado solicitado |
| 282 | 114.00 | 270.00 | 406.34 | 35.50 | NÃO | fora do lado solicitado |
| 283 | 114.00 | 271.00 | 406.26 | 34.50 | NÃO | fora do lado solicitado |
| 284 | 115.00 | 272.00 | 405.19 | 33.50 | NÃO | fora do lado solicitado |
| 285 | 115.00 | 273.00 | 405.11 | 32.50 | NÃO | fora do lado solicitado |
| 286 | 115.00 | 274.00 | 405.04 | 31.50 | NÃO | fora do lado solicitado |
| 287 | 115.00 | 275.00 | 404.97 | 30.50 | NÃO | fora do lado solicitado |
| 288 | 115.00 | 276.00 | 404.90 | 29.50 | NÃO | fora do lado solicitado |
| 289 | 115.00 | 277.00 | 404.84 | 28.50 | NÃO | fora do lado solicitado |
| 290 | 115.00 | 278.00 | 404.77 | 27.50 | NÃO | fora do lado solicitado |
| 291 | 115.00 | 279.00 | 404.71 | 26.50 | NÃO | fora do lado solicitado |
| 292 | 116.00 | 280.00 | 403.66 | 25.50 | NÃO | fora do lado solicitado |
| 293 | 116.00 | 281.00 | 403.60 | 24.50 | NÃO | fora do lado solicitado |
| 294 | 116.00 | 282.00 | 403.55 | 23.50 | NÃO | fora do lado solicitado |
| 295 | 116.00 | 283.00 | 403.50 | 22.50 | NÃO | fora do lado solicitado |
| 296 | 116.00 | 284.00 | 403.45 | 21.50 | NÃO | fora do lado solicitado |
| 297 | 116.00 | 285.00 | 403.40 | 20.50 | NÃO | fora do lado solicitado |
| 298 | 116.00 | 286.00 | 403.36 | 19.50 | NÃO | fora do lado solicitado |
| 299 | 116.00 | 287.00 | 403.32 | 18.50 | NÃO | fora do lado solicitado |
| 300 | 117.00 | 288.00 | 402.28 | 17.50 | NÃO | fora do lado solicitado |
| 301 | 117.00 | 289.00 | 402.24 | 16.50 | NÃO | fora do lado solicitado |
| 302 | 117.00 | 290.00 | 402.21 | 15.50 | NÃO | fora do lado solicitado |
| 303 | 117.00 | 291.00 | 402.18 | 14.50 | NÃO | fora do lado solicitado |
| 304 | 117.00 | 292.00 | 402.15 | 13.50 | NÃO | fora do lado solicitado |
| 305 | 118.00 | 293.00 | 401.12 | 12.50 | NÃO | fora do lado solicitado |
| 306 | 118.00 | 294.00 | 401.10 | 11.50 | NÃO | fora do lado solicitado |
| 307 | 118.00 | 295.00 | 401.08 | 10.50 | NÃO | fora do lado solicitado |
| 308 | 118.00 | 296.00 | 401.06 | 9.50 | NÃO | fora do lado solicitado |
| 309 | 118.00 | 297.00 | 401.04 | 8.50 | NÃO | fora do lado solicitado |
| 310 | 119.00 | 298.00 | 400.03 | 7.50 | NÃO | fora do lado solicitado |
| 311 | 119.00 | 299.00 | 400.02 | 6.50 | NÃO | fora do lado solicitado |
| 312 | 119.00 | 300.00 | 400.01 | 5.50 | NÃO | fora do lado solicitado |
| 313 | 119.00 | 301.00 | 400.00 | 4.50 | NÃO | fora do lado solicitado |
| 314 | 119.00 | 302.00 | 400.00 | 3.50 | NÃO | fora do lado solicitado |
| 315 | 120.00 | 303.00 | 399.00 | 2.50 | NÃO | fora do lado solicitado |
| 316 | 121.00 | 303.00 | 398.00 | 2.50 | NÃO | fora do lado solicitado |
| 317 | 122.00 | 303.00 | 397.00 | 2.50 | NÃO | fora do lado solicitado |
| 318 | 123.00 | 303.00 | 396.00 | 2.50 | NÃO | fora do lado solicitado |
| 319 | 124.00 | 303.00 | 395.00 | 2.50 | NÃO | fora do lado solicitado |
| 320 | 125.00 | 303.00 | 394.00 | 2.50 | NÃO | fora do lado solicitado |
| 321 | 126.00 | 303.00 | 393.00 | 2.50 | NÃO | fora do lado solicitado |
| 322 | 127.00 | 303.00 | 392.00 | 2.50 | NÃO | fora do lado solicitado |
| 323 | 128.00 | 303.00 | 391.00 | 2.50 | NÃO | fora do lado solicitado |
| 324 | 129.00 | 303.00 | 390.00 | 2.50 | NÃO | fora do lado solicitado |
| 325 | 130.00 | 303.00 | 389.00 | 2.50 | NÃO | fora do lado solicitado |
| 326 | 131.00 | 303.00 | 388.00 | 2.50 | NÃO | fora do lado solicitado |
| 327 | 132.00 | 303.00 | 387.00 | 2.50 | NÃO | fora do lado solicitado |
| 328 | 133.00 | 303.00 | 386.00 | 2.50 | NÃO | fora do lado solicitado |
| 329 | 134.00 | 303.00 | 385.00 | 2.50 | NÃO | fora do lado solicitado |
| 330 | 135.00 | 303.00 | 384.00 | 2.50 | NÃO | fora do lado solicitado |
| 331 | 136.00 | 303.00 | 383.00 | 2.50 | NÃO | fora do lado solicitado |
| 332 | 137.00 | 303.00 | 382.00 | 2.50 | NÃO | fora do lado solicitado |
| 333 | 138.00 | 303.00 | 381.00 | 2.50 | NÃO | fora do lado solicitado |
| 334 | 139.00 | 303.00 | 380.00 | 2.50 | NÃO | fora do lado solicitado |
| 335 | 140.00 | 303.00 | 379.00 | 2.50 | NÃO | fora do lado solicitado |
| 336 | 141.00 | 303.00 | 378.00 | 2.50 | NÃO | fora do lado solicitado |
| 337 | 142.00 | 303.00 | 377.00 | 2.50 | NÃO | fora do lado solicitado |
| 338 | 143.00 | 303.00 | 376.00 | 2.50 | NÃO | fora do lado solicitado |
| 339 | 144.00 | 303.00 | 375.00 | 2.50 | NÃO | fora do lado solicitado |
| 340 | 145.00 | 303.00 | 374.00 | 2.50 | NÃO | fora do lado solicitado |
| 341 | 146.00 | 303.00 | 373.00 | 2.50 | NÃO | fora do lado solicitado |
| 342 | 147.00 | 303.00 | 372.00 | 2.50 | NÃO | fora do lado solicitado |
| 343 | 148.00 | 303.00 | 371.00 | 2.50 | NÃO | fora do lado solicitado |
| 344 | 149.00 | 303.00 | 370.00 | 2.50 | NÃO | fora do lado solicitado |
| 345 | 150.00 | 303.00 | 369.00 | 2.50 | NÃO | fora do lado solicitado |
| 346 | 151.00 | 303.00 | 368.00 | 2.50 | NÃO | fora do lado solicitado |
| 347 | 152.00 | 303.00 | 367.00 | 2.50 | NÃO | fora do lado solicitado |
| 348 | 153.00 | 303.00 | 366.00 | 2.50 | NÃO | fora do lado solicitado |
| 349 | 154.00 | 303.00 | 365.00 | 2.50 | NÃO | fora do lado solicitado |
| 350 | 155.00 | 303.00 | 364.00 | 2.50 | NÃO | fora do lado solicitado |
| 351 | 156.00 | 303.00 | 363.00 | 2.50 | NÃO | fora do lado solicitado |
| 352 | 157.00 | 303.00 | 362.00 | 2.50 | NÃO | fora do lado solicitado |
| 353 | 158.00 | 303.00 | 361.00 | 2.50 | NÃO | fora do lado solicitado |
| 354 | 159.00 | 303.00 | 360.00 | 2.50 | NÃO | fora do lado solicitado |
| 355 | 160.00 | 303.00 | 359.00 | 2.50 | NÃO | fora do lado solicitado |
| 356 | 161.00 | 303.00 | 358.00 | 2.50 | NÃO | fora do lado solicitado |
| 357 | 162.00 | 303.00 | 357.00 | 2.50 | NÃO | fora do lado solicitado |
| 358 | 163.00 | 303.00 | 356.00 | 2.50 | NÃO | fora do lado solicitado |
| 359 | 164.00 | 303.00 | 355.00 | 2.50 | NÃO | fora do lado solicitado |
| 360 | 165.00 | 303.00 | 354.00 | 2.50 | NÃO | fora do lado solicitado |
| 361 | 166.00 | 303.00 | 353.00 | 2.50 | NÃO | fora do lado solicitado |
| 362 | 167.00 | 303.00 | 352.00 | 2.50 | NÃO | fora do lado solicitado |
| 363 | 168.00 | 303.00 | 351.00 | 2.50 | NÃO | fora do lado solicitado |
| 364 | 169.00 | 303.00 | 350.00 | 2.50 | NÃO | fora do lado solicitado |
| 365 | 170.00 | 303.00 | 349.00 | 2.50 | NÃO | fora do lado solicitado |
| 366 | 171.00 | 303.00 | 348.00 | 2.50 | NÃO | fora do lado solicitado |
| 367 | 172.00 | 303.00 | 347.00 | 2.50 | NÃO | fora do lado solicitado |
| 368 | 173.00 | 303.00 | 346.00 | 2.50 | NÃO | fora do lado solicitado |
| 369 | 174.00 | 303.00 | 345.00 | 2.50 | NÃO | fora do lado solicitado |
| 370 | 175.00 | 303.00 | 344.00 | 2.50 | NÃO | fora do lado solicitado |
| 371 | 176.00 | 303.00 | 343.00 | 2.50 | NÃO | fora do lado solicitado |
| 372 | 177.00 | 303.00 | 342.00 | 2.50 | NÃO | fora do lado solicitado |
| 373 | 178.00 | 303.00 | 341.00 | 2.50 | NÃO | fora do lado solicitado |
| 374 | 179.00 | 303.00 | 340.00 | 2.50 | NÃO | fora do lado solicitado |
| 375 | 180.00 | 303.00 | 339.00 | 2.50 | NÃO | fora do lado solicitado |
| 376 | 181.00 | 303.00 | 338.00 | 2.50 | NÃO | fora do lado solicitado |
| 377 | 182.00 | 303.00 | 337.00 | 2.50 | NÃO | fora do lado solicitado |
| 378 | 183.00 | 303.00 | 336.00 | 2.50 | NÃO | fora do lado solicitado |
| 379 | 184.00 | 303.00 | 335.00 | 2.50 | NÃO | fora do lado solicitado |
| 380 | 185.00 | 303.00 | 334.00 | 2.50 | NÃO | fora do lado solicitado |
| 381 | 186.00 | 303.00 | 333.00 | 2.50 | NÃO | fora do lado solicitado |
| 382 | 187.00 | 303.00 | 332.00 | 2.50 | NÃO | fora do lado solicitado |
| 383 | 188.00 | 303.00 | 331.00 | 2.50 | NÃO | fora do lado solicitado |
| 384 | 189.00 | 303.00 | 330.00 | 2.50 | NÃO | fora do lado solicitado |
| 385 | 190.00 | 303.00 | 329.00 | 2.50 | NÃO | fora do lado solicitado |
| 386 | 191.00 | 303.00 | 328.00 | 2.50 | NÃO | fora do lado solicitado |
| 387 | 192.00 | 303.00 | 327.00 | 2.50 | NÃO | fora do lado solicitado |
| 388 | 193.00 | 303.00 | 326.00 | 2.50 | NÃO | fora do lado solicitado |
| 389 | 194.00 | 303.00 | 325.00 | 2.50 | NÃO | fora do lado solicitado |
| 390 | 195.00 | 303.00 | 324.00 | 2.50 | NÃO | fora do lado solicitado |
| 391 | 196.00 | 303.00 | 323.00 | 2.50 | NÃO | fora do lado solicitado |
| 392 | 197.00 | 303.00 | 322.00 | 2.50 | NÃO | fora do lado solicitado |
| 393 | 198.00 | 303.00 | 321.00 | 2.50 | NÃO | fora do lado solicitado |
| 394 | 199.00 | 303.00 | 320.00 | 2.50 | NÃO | fora do lado solicitado |
| 395 | 200.00 | 303.00 | 319.00 | 2.50 | NÃO | fora do lado solicitado |
| 396 | 201.00 | 303.00 | 318.00 | 2.50 | NÃO | fora do lado solicitado |
| 397 | 202.00 | 303.00 | 317.00 | 2.50 | NÃO | fora do lado solicitado |
| 398 | 203.00 | 303.00 | 316.00 | 2.50 | NÃO | fora do lado solicitado |
| 399 | 204.00 | 303.00 | 315.00 | 2.50 | NÃO | fora do lado solicitado |
| 400 | 205.00 | 303.00 | 314.00 | 2.50 | NÃO | fora do lado solicitado |
| 401 | 206.00 | 303.00 | 313.00 | 2.50 | NÃO | fora do lado solicitado |
| 402 | 207.00 | 303.00 | 312.00 | 2.50 | NÃO | fora do lado solicitado |
| 403 | 208.00 | 303.00 | 311.00 | 2.50 | NÃO | fora do lado solicitado |
| 404 | 209.00 | 303.00 | 310.00 | 2.50 | NÃO | fora do lado solicitado |
| 405 | 210.00 | 303.00 | 309.00 | 2.50 | NÃO | fora do lado solicitado |
| 406 | 211.00 | 303.00 | 308.00 | 2.50 | NÃO | fora do lado solicitado |
| 407 | 212.00 | 303.00 | 307.00 | 2.50 | NÃO | fora do lado solicitado |
| 408 | 213.00 | 303.00 | 306.00 | 2.50 | NÃO | fora do lado solicitado |
| 409 | 214.00 | 303.00 | 305.00 | 2.50 | NÃO | fora do lado solicitado |
| 410 | 215.00 | 303.00 | 304.00 | 2.50 | NÃO | fora do lado solicitado |
| 411 | 216.00 | 303.00 | 303.00 | 2.50 | NÃO | fora do lado solicitado |
| 412 | 217.00 | 303.00 | 302.00 | 2.50 | NÃO | fora do lado solicitado |
| 413 | 218.00 | 303.00 | 301.00 | 2.50 | NÃO | fora do lado solicitado |
| 414 | 219.00 | 303.00 | 300.00 | 2.50 | NÃO | fora do lado solicitado |
| 415 | 220.00 | 303.00 | 299.00 | 2.50 | NÃO | fora do lado solicitado |
| 416 | 221.00 | 303.00 | 298.00 | 2.50 | NÃO | fora do lado solicitado |
| 417 | 222.00 | 303.00 | 297.00 | 2.50 | NÃO | fora do lado solicitado |
| 418 | 223.00 | 303.00 | 296.00 | 2.50 | NÃO | fora do lado solicitado |
| 419 | 224.00 | 303.00 | 295.00 | 2.50 | NÃO | fora do lado solicitado |
| 420 | 225.00 | 303.00 | 294.00 | 2.50 | NÃO | fora do lado solicitado |
| 421 | 226.00 | 303.00 | 293.00 | 2.50 | NÃO | fora do lado solicitado |
| 422 | 227.00 | 303.00 | 292.00 | 2.50 | NÃO | fora do lado solicitado |
| 423 | 228.00 | 303.00 | 291.00 | 2.50 | NÃO | fora do lado solicitado |
| 424 | 229.00 | 303.00 | 290.00 | 2.50 | NÃO | fora do lado solicitado |
| 425 | 230.00 | 303.00 | 289.00 | 2.50 | NÃO | fora do lado solicitado |
| 426 | 231.00 | 303.00 | 288.00 | 2.50 | NÃO | fora do lado solicitado |
| 427 | 232.00 | 303.00 | 287.00 | 2.50 | NÃO | fora do lado solicitado |
| 428 | 233.00 | 303.00 | 286.00 | 2.50 | NÃO | fora do lado solicitado |
| 429 | 234.00 | 303.00 | 285.00 | 2.50 | NÃO | fora do lado solicitado |
| 430 | 235.00 | 303.00 | 284.00 | 2.50 | NÃO | fora do lado solicitado |
| 431 | 236.00 | 303.00 | 283.00 | 2.50 | NÃO | fora do lado solicitado |
| 432 | 237.00 | 303.00 | 282.00 | 2.50 | NÃO | fora do lado solicitado |
| 433 | 238.00 | 303.00 | 281.00 | 2.50 | NÃO | fora do lado solicitado |
| 434 | 239.00 | 303.00 | 280.00 | 2.50 | NÃO | fora do lado solicitado |
| 435 | 240.00 | 303.00 | 279.00 | 2.50 | NÃO | fora do lado solicitado |
| 436 | 241.00 | 303.00 | 278.00 | 2.50 | NÃO | fora do lado solicitado |
| 437 | 242.00 | 303.00 | 277.00 | 2.50 | NÃO | fora do lado solicitado |
| 438 | 243.00 | 303.00 | 276.00 | 2.50 | NÃO | fora do lado solicitado |
| 439 | 244.00 | 303.00 | 275.00 | 2.50 | NÃO | fora do lado solicitado |
| 440 | 245.00 | 303.00 | 274.00 | 2.50 | NÃO | fora do lado solicitado |
| 441 | 246.00 | 303.00 | 273.00 | 2.50 | NÃO | fora do lado solicitado |
| 442 | 247.00 | 303.00 | 272.00 | 2.50 | NÃO | fora do lado solicitado |
| 443 | 248.00 | 303.00 | 271.00 | 2.50 | NÃO | fora do lado solicitado |
| 444 | 249.00 | 303.00 | 270.00 | 2.50 | NÃO | fora do lado solicitado |
| 445 | 250.00 | 303.00 | 269.00 | 2.50 | NÃO | fora do lado solicitado |
| 446 | 251.00 | 303.00 | 268.00 | 2.50 | NÃO | fora do lado solicitado |
| 447 | 252.00 | 303.00 | 267.00 | 2.50 | NÃO | fora do lado solicitado |
| 448 | 253.00 | 303.00 | 266.00 | 2.50 | NÃO | fora do lado solicitado |
| 449 | 254.00 | 303.00 | 265.00 | 2.50 | NÃO | fora do lado solicitado |
| 450 | 255.00 | 303.00 | 264.00 | 2.50 | NÃO | fora do lado solicitado |
| 451 | 256.00 | 303.00 | 263.00 | 2.50 | NÃO | fora do lado solicitado |
| 452 | 257.00 | 303.00 | 262.00 | 2.50 | NÃO | fora do lado solicitado |
| 453 | 258.00 | 303.00 | 261.00 | 2.50 | NÃO | fora do lado solicitado |
| 454 | 259.00 | 303.00 | 260.00 | 2.50 | NÃO | fora do lado solicitado |
| 455 | 260.00 | 303.00 | 259.00 | 2.50 | NÃO | fora do lado solicitado |
| 456 | 261.00 | 303.00 | 258.00 | 2.50 | NÃO | fora do lado solicitado |
| 457 | 262.00 | 303.00 | 257.00 | 2.50 | NÃO | fora do lado solicitado |
| 458 | 263.00 | 303.00 | 256.00 | 2.50 | NÃO | fora do lado solicitado |
| 459 | 264.00 | 303.00 | 255.00 | 2.50 | NÃO | fora do lado solicitado |
| 460 | 265.00 | 303.00 | 254.00 | 2.50 | NÃO | fora do lado solicitado |
| 461 | 266.00 | 303.00 | 253.00 | 2.50 | NÃO | fora do lado solicitado |
| 462 | 267.00 | 303.00 | 252.00 | 2.50 | NÃO | fora do lado solicitado |
| 463 | 268.00 | 303.00 | 251.00 | 2.50 | NÃO | fora do lado solicitado |
| 464 | 269.00 | 303.00 | 250.00 | 2.50 | NÃO | fora do lado solicitado |
| 465 | 270.00 | 303.00 | 249.00 | 2.50 | NÃO | fora do lado solicitado |
| 466 | 271.00 | 303.00 | 248.00 | 2.50 | NÃO | fora do lado solicitado |
| 467 | 272.00 | 303.00 | 247.00 | 2.50 | NÃO | fora do lado solicitado |
| 468 | 273.00 | 303.00 | 246.00 | 2.50 | NÃO | fora do lado solicitado |
| 469 | 274.00 | 303.00 | 245.00 | 2.50 | NÃO | fora do lado solicitado |
| 470 | 275.00 | 303.00 | 244.00 | 2.50 | NÃO | fora do lado solicitado |
| 471 | 276.00 | 303.00 | 243.00 | 2.50 | NÃO | fora do lado solicitado |
| 472 | 277.00 | 303.00 | 242.00 | 2.50 | NÃO | fora do lado solicitado |
| 473 | 278.00 | 303.00 | 241.00 | 2.50 | NÃO | fora do lado solicitado |
| 474 | 279.00 | 303.00 | 240.00 | 2.50 | NÃO | fora do lado solicitado |
| 475 | 280.00 | 303.00 | 239.00 | 2.50 | NÃO | fora do lado solicitado |
| 476 | 281.00 | 303.00 | 238.00 | 2.50 | NÃO | fora do lado solicitado |
| 477 | 282.00 | 303.00 | 237.00 | 2.50 | NÃO | fora do lado solicitado |
| 478 | 283.00 | 303.00 | 236.00 | 2.50 | NÃO | fora do lado solicitado |
| 479 | 284.00 | 303.00 | 235.00 | 2.50 | NÃO | fora do lado solicitado |
| 480 | 285.00 | 303.00 | 234.00 | 2.50 | NÃO | fora do lado solicitado |
| 481 | 286.00 | 303.00 | 233.00 | 2.50 | NÃO | fora do lado solicitado |
| 482 | 287.00 | 303.00 | 232.00 | 2.50 | NÃO | fora do lado solicitado |
| 483 | 288.00 | 303.00 | 231.00 | 2.50 | NÃO | fora do lado solicitado |
| 484 | 289.00 | 303.00 | 230.00 | 2.50 | NÃO | fora do lado solicitado |
| 485 | 290.00 | 303.00 | 229.00 | 2.50 | NÃO | fora do lado solicitado |
| 486 | 291.00 | 303.00 | 228.00 | 2.50 | NÃO | fora do lado solicitado |
| 487 | 292.00 | 303.00 | 227.00 | 2.50 | NÃO | fora do lado solicitado |
| 488 | 293.00 | 303.00 | 226.00 | 2.50 | NÃO | fora do lado solicitado |
| 489 | 294.00 | 303.00 | 225.00 | 2.50 | NÃO | fora do lado solicitado |
| 490 | 295.00 | 303.00 | 224.00 | 2.50 | NÃO | fora do lado solicitado |
| 491 | 296.00 | 303.00 | 223.00 | 2.50 | NÃO | fora do lado solicitado |
| 492 | 297.00 | 303.00 | 222.00 | 2.50 | NÃO | fora do lado solicitado |
| 493 | 298.00 | 303.00 | 221.00 | 2.50 | NÃO | fora do lado solicitado |
| 494 | 299.00 | 303.00 | 220.00 | 2.50 | NÃO | fora do lado solicitado |
| 495 | 300.00 | 303.00 | 219.00 | 2.50 | NÃO | fora do lado solicitado |
| 496 | 301.00 | 303.00 | 218.00 | 2.50 | NÃO | fora do lado solicitado |
| 497 | 302.00 | 303.00 | 217.00 | 2.50 | NÃO | fora do lado solicitado |
| 498 | 303.00 | 303.00 | 216.00 | 2.50 | NÃO | fora do lado solicitado |
| 499 | 304.00 | 303.00 | 215.00 | 2.50 | NÃO | fora do lado solicitado |
| 500 | 305.00 | 303.00 | 214.00 | 2.50 | NÃO | fora do lado solicitado |
| 501 | 306.00 | 303.00 | 213.00 | 2.50 | NÃO | fora do lado solicitado |
| 502 | 307.00 | 303.00 | 212.00 | 2.50 | NÃO | fora do lado solicitado |
| 503 | 308.00 | 303.00 | 211.00 | 2.50 | NÃO | fora do lado solicitado |
| 504 | 309.00 | 303.00 | 210.00 | 2.50 | NÃO | fora do lado solicitado |
| 505 | 310.00 | 303.00 | 209.00 | 2.50 | NÃO | fora do lado solicitado |
| 506 | 311.00 | 303.00 | 208.00 | 2.50 | NÃO | fora do lado solicitado |
| 507 | 312.00 | 303.00 | 207.00 | 2.50 | NÃO | fora do lado solicitado |
| 508 | 313.00 | 303.00 | 206.00 | 2.50 | NÃO | fora do lado solicitado |
| 509 | 314.00 | 303.00 | 205.00 | 2.50 | NÃO | fora do lado solicitado |
| 510 | 315.00 | 303.00 | 204.00 | 2.50 | NÃO | fora do lado solicitado |
| 511 | 316.00 | 303.00 | 203.00 | 2.50 | NÃO | fora do lado solicitado |
| 512 | 317.00 | 303.00 | 202.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 513 | 318.00 | 303.00 | 201.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 514 | 319.00 | 303.00 | 200.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 515 | 320.00 | 303.00 | 199.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 516 | 321.00 | 303.00 | 198.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 517 | 322.00 | 303.00 | 197.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 518 | 323.00 | 303.00 | 196.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 519 | 324.00 | 303.00 | 195.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 520 | 325.00 | 303.00 | 194.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 521 | 326.00 | 303.00 | 193.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 522 | 327.00 | 303.00 | 192.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 523 | 328.00 | 303.00 | 191.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 524 | 329.00 | 303.00 | 190.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 525 | 330.00 | 303.00 | 189.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 526 | 331.00 | 303.00 | 188.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 527 | 332.00 | 303.00 | 187.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 528 | 333.00 | 303.00 | 186.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 529 | 334.00 | 303.00 | 185.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 530 | 335.00 | 303.00 | 184.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 531 | 336.00 | 303.00 | 183.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 532 | 337.00 | 303.00 | 182.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 533 | 338.00 | 303.00 | 181.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 534 | 339.00 | 303.00 | 180.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 535 | 340.00 | 303.00 | 179.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 536 | 341.00 | 303.00 | 178.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 537 | 342.00 | 303.00 | 177.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 538 | 343.00 | 303.00 | 176.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 539 | 344.00 | 303.00 | 175.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 540 | 345.00 | 303.00 | 174.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 541 | 346.00 | 303.00 | 173.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 542 | 347.00 | 303.00 | 172.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 543 | 348.00 | 303.00 | 171.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 544 | 349.00 | 303.00 | 170.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 545 | 350.00 | 303.00 | 169.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 546 | 351.00 | 303.00 | 168.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 547 | 352.00 | 303.00 | 167.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 548 | 353.00 | 303.00 | 166.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 549 | 354.00 | 303.00 | 165.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 550 | 355.00 | 303.00 | 164.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 551 | 356.00 | 303.00 | 163.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 552 | 357.00 | 303.00 | 162.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 553 | 358.00 | 303.00 | 161.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 554 | 359.00 | 303.00 | 160.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 555 | 360.00 | 303.00 | 159.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 556 | 361.00 | 303.00 | 158.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 557 | 362.00 | 303.00 | 157.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 558 | 363.00 | 303.00 | 156.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 559 | 364.00 | 303.00 | 155.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 560 | 365.00 | 303.00 | 154.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 561 | 366.00 | 303.00 | 153.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 562 | 367.00 | 303.00 | 152.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 563 | 368.00 | 303.00 | 151.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 564 | 369.00 | 303.00 | 150.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 565 | 370.00 | 303.00 | 149.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 566 | 371.00 | 303.00 | 148.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 567 | 372.00 | 303.00 | 147.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 568 | 373.00 | 303.00 | 146.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 569 | 374.00 | 303.00 | 145.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 570 | 375.00 | 303.00 | 144.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 571 | 376.00 | 303.00 | 143.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 572 | 377.00 | 303.00 | 142.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 573 | 378.00 | 303.00 | 141.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 574 | 379.00 | 303.00 | 140.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 575 | 380.00 | 303.00 | 139.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 576 | 381.00 | 303.00 | 138.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 577 | 382.00 | 303.00 | 137.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 578 | 383.00 | 303.00 | 136.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 579 | 384.00 | 303.00 | 135.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 580 | 385.00 | 303.00 | 134.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 581 | 386.00 | 303.00 | 133.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 582 | 387.00 | 303.00 | 132.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 583 | 388.00 | 303.00 | 131.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 584 | 389.00 | 303.00 | 130.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 585 | 390.00 | 303.00 | 129.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 586 | 391.00 | 303.00 | 128.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 587 | 392.00 | 303.00 | 127.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 588 | 393.00 | 303.00 | 126.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 589 | 394.00 | 303.00 | 125.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 590 | 395.00 | 303.00 | 124.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 591 | 396.00 | 303.00 | 123.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 592 | 397.00 | 303.00 | 122.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 593 | 398.00 | 303.00 | 121.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 594 | 399.00 | 303.00 | 120.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 595 | 400.00 | 303.00 | 119.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 596 | 401.00 | 303.00 | 118.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 597 | 402.00 | 303.00 | 117.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 598 | 403.00 | 303.00 | 116.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 599 | 404.00 | 303.00 | 115.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 600 | 405.00 | 303.00 | 114.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 601 | 406.00 | 303.00 | 113.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 602 | 407.00 | 303.00 | 112.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 603 | 408.00 | 303.00 | 111.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 604 | 409.00 | 303.00 | 110.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 605 | 410.00 | 303.00 | 109.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 606 | 411.00 | 303.00 | 108.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 607 | 412.00 | 303.00 | 107.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 608 | 413.00 | 303.00 | 106.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 609 | 414.00 | 303.00 | 105.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 610 | 415.00 | 303.00 | 104.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 611 | 416.00 | 303.00 | 103.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 612 | 417.00 | 303.00 | 102.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 613 | 418.00 | 303.00 | 101.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 614 | 419.00 | 303.00 | 100.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 615 | 420.00 | 303.00 | 99.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 616 | 421.00 | 303.00 | 98.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 617 | 422.00 | 303.00 | 97.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 618 | 423.00 | 303.00 | 96.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 619 | 424.00 | 303.00 | 95.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 620 | 425.00 | 303.00 | 94.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 621 | 426.00 | 303.00 | 93.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 622 | 427.00 | 303.00 | 92.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 623 | 428.00 | 303.00 | 91.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 624 | 429.00 | 303.00 | 90.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 625 | 430.00 | 303.00 | 89.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 626 | 431.00 | 303.00 | 88.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 627 | 432.00 | 303.00 | 87.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 628 | 433.00 | 303.00 | 86.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 629 | 434.00 | 303.00 | 85.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 630 | 435.00 | 303.00 | 84.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 631 | 436.00 | 303.00 | 83.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 632 | 437.00 | 303.00 | 82.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 633 | 438.00 | 303.00 | 81.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 634 | 439.00 | 303.00 | 80.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 635 | 440.00 | 303.00 | 79.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 636 | 441.00 | 303.00 | 78.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 637 | 442.00 | 303.00 | 77.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 638 | 443.00 | 303.00 | 76.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 639 | 444.00 | 303.00 | 75.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 640 | 445.00 | 303.00 | 74.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 641 | 446.00 | 303.00 | 73.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 642 | 447.00 | 303.00 | 72.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 643 | 448.00 | 303.00 | 71.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 644 | 449.00 | 303.00 | 70.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 645 | 450.00 | 303.00 | 69.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 646 | 451.00 | 303.00 | 68.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 647 | 452.00 | 303.00 | 67.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 648 | 453.00 | 303.00 | 66.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 649 | 454.00 | 303.00 | 65.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 650 | 455.00 | 303.00 | 64.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 651 | 456.00 | 303.00 | 63.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 652 | 457.00 | 303.00 | 62.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 653 | 458.00 | 303.00 | 61.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 654 | 459.00 | 303.00 | 60.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 655 | 460.00 | 303.00 | 59.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 656 | 461.00 | 303.00 | 58.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 657 | 462.00 | 303.00 | 57.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 658 | 463.00 | 303.00 | 56.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 659 | 464.00 | 303.00 | 55.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 660 | 465.00 | 303.00 | 54.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 661 | 466.00 | 303.00 | 53.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 662 | 467.00 | 303.00 | 52.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 663 | 468.00 | 303.00 | 51.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 664 | 469.00 | 303.00 | 50.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 665 | 470.00 | 303.00 | 49.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 666 | 471.00 | 303.00 | 48.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 667 | 472.00 | 303.00 | 47.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 668 | 473.00 | 303.00 | 46.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 669 | 474.00 | 303.00 | 45.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 670 | 475.00 | 303.00 | 44.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 671 | 476.00 | 303.00 | 43.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 672 | 477.00 | 303.00 | 42.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 673 | 478.00 | 303.00 | 41.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 674 | 479.00 | 303.00 | 40.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 675 | 480.00 | 303.00 | 39.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 676 | 481.00 | 303.00 | 38.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 677 | 482.00 | 303.00 | 37.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 678 | 483.00 | 303.00 | 36.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 679 | 484.00 | 303.00 | 35.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 680 | 485.00 | 303.00 | 34.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 681 | 486.00 | 303.00 | 33.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 682 | 487.00 | 303.00 | 32.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 683 | 488.00 | 303.00 | 31.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 684 | 489.00 | 303.00 | 30.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 685 | 490.00 | 303.00 | 29.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 686 | 491.00 | 303.00 | 28.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 687 | 492.00 | 303.00 | 27.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 688 | 493.00 | 303.00 | 26.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 689 | 494.00 | 303.00 | 25.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 690 | 495.00 | 303.00 | 24.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 691 | 496.00 | 303.00 | 23.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 692 | 497.00 | 303.00 | 22.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 693 | 498.00 | 303.00 | 21.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 694 | 499.00 | 303.00 | 20.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 695 | 500.00 | 303.00 | 19.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 696 | 501.00 | 303.00 | 18.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 697 | 502.00 | 303.00 | 17.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 698 | 503.00 | 303.00 | 16.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 699 | 504.00 | 303.00 | 15.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 700 | 505.00 | 303.00 | 14.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 701 | 506.00 | 303.00 | 13.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 702 | 507.00 | 303.00 | 12.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 703 | 508.00 | 303.00 | 11.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 704 | 509.00 | 303.00 | 10.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 705 | 510.00 | 303.00 | 9.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 706 | 511.00 | 303.00 | 8.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 707 | 512.00 | 303.00 | 7.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 708 | 513.00 | 303.00 | 6.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 709 | 514.00 | 303.00 | 5.00 | 2.50 | SIM | dentro da janela vertical e do lado solicitado |
| 710 | 514.00 | 302.00 | 5.10 | 3.50 | SIM | dentro da janela vertical e do lado solicitado |
| 711 | 514.00 | 301.00 | 5.39 | 4.50 | SIM | dentro da janela vertical e do lado solicitado |
| 712 | 514.00 | 300.00 | 5.83 | 5.50 | SIM | dentro da janela vertical e do lado solicitado |
| 713 | 514.00 | 299.00 | 6.40 | 6.50 | SIM | dentro da janela vertical e do lado solicitado |
| 714 | 515.00 | 298.00 | 6.40 | 7.50 | SIM | dentro da janela vertical e do lado solicitado |
| 715 | 515.00 | 297.00 | 7.21 | 8.50 | SIM | dentro da janela vertical e do lado solicitado |
| 716 | 515.00 | 296.00 | 8.06 | 9.50 | SIM | dentro da janela vertical e do lado solicitado |
| 717 | 515.00 | 295.00 | 8.94 | 10.50 | SIM | dentro da janela vertical e do lado solicitado |
| 718 | 515.00 | 294.00 | 9.85 | 11.50 | SIM | dentro da janela vertical e do lado solicitado |
| 719 | 516.00 | 293.00 | 10.44 | 12.50 | SIM | dentro da janela vertical e do lado solicitado |
| 720 | 516.00 | 292.00 | 11.40 | 13.50 | SIM | dentro da janela vertical e do lado solicitado |
| 721 | 516.00 | 291.00 | 12.37 | 14.50 | SIM | dentro da janela vertical e do lado solicitado |
| 722 | 516.00 | 290.00 | 13.34 | 15.50 | SIM | dentro da janela vertical e do lado solicitado |
| 723 | 516.00 | 289.00 | 14.32 | 16.50 | SIM | dentro da janela vertical e do lado solicitado |
| 724 | 517.00 | 288.00 | 15.13 | 17.50 | SIM | dentro da janela vertical e do lado solicitado |
| 725 | 517.00 | 287.00 | 16.12 | 18.50 | SIM | dentro da janela vertical e do lado solicitado |
| 726 | 517.00 | 286.00 | 17.12 | 19.50 | SIM | dentro da janela vertical e do lado solicitado |
| 727 | 517.00 | 285.00 | 18.11 | 20.50 | SIM | dentro da janela vertical e do lado solicitado |
| 728 | 517.00 | 284.00 | 19.10 | 21.50 | SIM | dentro da janela vertical e do lado solicitado |
| 729 | 517.00 | 283.00 | 20.10 | 22.50 | SIM | dentro da janela vertical e do lado solicitado |
| 730 | 517.00 | 282.00 | 21.10 | 23.50 | SIM | dentro da janela vertical e do lado solicitado |
| 731 | 518.00 | 281.00 | 22.02 | 24.50 | SIM | dentro da janela vertical e do lado solicitado |
| 732 | 518.00 | 280.00 | 23.02 | 25.50 | SIM | dentro da janela vertical e do lado solicitado |
| 733 | 518.00 | 279.00 | 24.02 | 26.50 | SIM | dentro da janela vertical e do lado solicitado |
| 734 | 518.00 | 278.00 | 25.02 | 27.50 | SIM | dentro da janela vertical e do lado solicitado |
| 735 | 518.00 | 277.00 | 26.02 | 28.50 | SIM | dentro da janela vertical e do lado solicitado |
| 736 | 518.00 | 276.00 | 27.02 | 29.50 | SIM | dentro da janela vertical e do lado solicitado |
| 737 | 518.00 | 275.00 | 28.02 | 30.50 | SIM | dentro da janela vertical e do lado solicitado |
| 738 | 518.00 | 274.00 | 29.02 | 31.50 | SIM | dentro da janela vertical e do lado solicitado |
| 739 | 519.00 | 273.00 | 30.00 | 32.50 | SIM | dentro da janela vertical e do lado solicitado |
| 740 | 519.00 | 272.00 | 31.00 | 33.50 | SIM | dentro da janela vertical e do lado solicitado |
| 741 | 519.00 | 271.00 | 32.00 | 34.50 | SIM | dentro da janela vertical e do lado solicitado |
| 742 | 519.00 | 270.00 | 33.00 | 35.50 | SIM | dentro da janela vertical e do lado solicitado |
| 743 | 519.00 | 269.00 | 34.00 | 36.50 | SIM | dentro da janela vertical e do lado solicitado |
| 744 | 519.00 | 268.00 | 35.00 | 37.50 | SIM | dentro da janela vertical e do lado solicitado |
| 745 | 519.00 | 267.00 | 36.00 | 38.50 | SIM | dentro da janela vertical e do lado solicitado |
| 746 | 519.00 | 266.00 | 37.00 | 39.50 | SIM | dentro da janela vertical e do lado solicitado |
| 747 | 519.00 | 265.00 | 38.00 | 40.50 | SIM | dentro da janela vertical e do lado solicitado |
| 748 | 519.00 | 264.00 | 39.00 | 41.50 | SIM | dentro da janela vertical e do lado solicitado |
| 749 | 519.00 | 263.00 | 40.00 | 42.50 | SIM | dentro da janela vertical e do lado solicitado |
| 750 | 519.00 | 262.00 | 41.00 | 43.50 | SIM | dentro da janela vertical e do lado solicitado |
| 751 | 519.00 | 261.00 | 42.00 | 44.50 | SIM | dentro da janela vertical e do lado solicitado |
| 752 | 519.00 | 260.00 | 43.00 | 45.50 | SIM | dentro da janela vertical e do lado solicitado |
| 753 | 519.00 | 259.00 | 44.00 | 46.50 | SIM | dentro da janela vertical e do lado solicitado |
| 754 | 519.00 | 258.00 | 45.00 | 47.50 | SIM | dentro da janela vertical e do lado solicitado |
| 755 | 519.00 | 257.00 | 46.00 | 48.50 | SIM | dentro da janela vertical e do lado solicitado |
| 756 | 519.00 | 256.00 | 47.00 | 49.50 | SIM | dentro da janela vertical e do lado solicitado |
| 757 | 519.00 | 255.00 | 48.00 | 50.50 | SIM | dentro da janela vertical e do lado solicitado |
| 758 | 519.00 | 254.00 | 49.00 | 51.50 | SIM | dentro da janela vertical e do lado solicitado |
| 759 | 519.00 | 253.00 | 50.00 | 52.50 | SIM | dentro da janela vertical e do lado solicitado |
| 760 | 519.00 | 252.00 | 51.00 | 53.50 | SIM | dentro da janela vertical e do lado solicitado |
| 761 | 519.00 | 251.00 | 52.00 | 54.50 | SIM | dentro da janela vertical e do lado solicitado |
| 762 | 519.00 | 250.00 | 53.00 | 55.50 | SIM | dentro da janela vertical e do lado solicitado |
| 763 | 519.00 | 249.00 | 54.00 | 56.50 | SIM | dentro da janela vertical e do lado solicitado |
| 764 | 519.00 | 248.00 | 55.00 | 57.50 | SIM | dentro da janela vertical e do lado solicitado |
| 765 | 519.00 | 247.00 | 56.00 | 58.50 | SIM | dentro da janela vertical e do lado solicitado |
| 766 | 519.00 | 246.00 | 57.00 | 59.50 | SIM | dentro da janela vertical e do lado solicitado |
| 767 | 519.00 | 245.00 | 58.00 | 60.50 | SIM | dentro da janela vertical e do lado solicitado |
| 768 | 519.00 | 244.00 | 59.00 | 61.50 | SIM | dentro da janela vertical e do lado solicitado |
| 769 | 519.00 | 243.00 | 60.00 | 62.50 | SIM | dentro da janela vertical e do lado solicitado |
| 770 | 519.00 | 242.00 | 61.00 | 63.50 | SIM | dentro da janela vertical e do lado solicitado |
| 771 | 519.00 | 241.00 | 62.00 | 64.50 | SIM | dentro da janela vertical e do lado solicitado |
| 772 | 519.00 | 240.00 | 63.00 | 65.50 | SIM | dentro da janela vertical e do lado solicitado |
| 773 | 519.00 | 239.00 | 64.00 | 66.50 | SIM | dentro da janela vertical e do lado solicitado |
| 774 | 519.00 | 238.00 | 65.00 | 67.50 | SIM | dentro da janela vertical e do lado solicitado |
| 775 | 519.00 | 237.00 | 66.00 | 68.50 | SIM | dentro da janela vertical e do lado solicitado |
| 776 | 518.00 | 236.00 | 67.01 | 69.50 | SIM | dentro da janela vertical e do lado solicitado |
| 777 | 518.00 | 235.00 | 68.01 | 70.50 | SIM | dentro da janela vertical e do lado solicitado |
| 778 | 518.00 | 234.00 | 69.01 | 71.50 | SIM | dentro da janela vertical e do lado solicitado |
| 779 | 518.00 | 233.00 | 70.01 | 72.50 | SIM | dentro da janela vertical e do lado solicitado |
| 780 | 518.00 | 232.00 | 71.01 | 73.50 | SIM | dentro da janela vertical e do lado solicitado |
| 781 | 518.00 | 231.00 | 72.01 | 74.50 | SIM | dentro da janela vertical e do lado solicitado |
| 782 | 518.00 | 230.00 | 73.01 | 75.50 | SIM | dentro da janela vertical e do lado solicitado |
| 783 | 518.00 | 229.00 | 74.01 | 76.50 | SIM | dentro da janela vertical e do lado solicitado |
| 784 | 517.00 | 228.00 | 75.03 | 77.50 | SIM | dentro da janela vertical e do lado solicitado |
| 785 | 517.00 | 227.00 | 76.03 | 78.50 | SIM | dentro da janela vertical e do lado solicitado |
| 786 | 517.00 | 226.00 | 77.03 | 79.50 | SIM | dentro da janela vertical e do lado solicitado |
| 787 | 517.00 | 225.00 | 78.03 | 80.50 | SIM | dentro da janela vertical e do lado solicitado |
| 788 | 517.00 | 224.00 | 79.03 | 81.50 | SIM | dentro da janela vertical e do lado solicitado |
| 789 | 517.00 | 223.00 | 80.02 | 82.50 | SIM | dentro da janela vertical e do lado solicitado |
| 790 | 517.00 | 222.00 | 81.02 | 83.50 | SIM | dentro da janela vertical e do lado solicitado |
| 791 | 516.00 | 221.00 | 82.05 | 84.50 | SIM | dentro da janela vertical e do lado solicitado |
| 792 | 516.00 | 220.00 | 83.05 | 85.50 | SIM | dentro da janela vertical e do lado solicitado |
| 793 | 516.00 | 219.00 | 84.05 | 86.50 | SIM | dentro da janela vertical e do lado solicitado |
| 794 | 516.00 | 218.00 | 85.05 | 87.50 | SIM | dentro da janela vertical e do lado solicitado |
| 795 | 516.00 | 217.00 | 86.05 | 88.50 | SIM | dentro da janela vertical e do lado solicitado |
| 796 | 515.00 | 216.00 | 87.09 | 89.50 | SIM | dentro da janela vertical e do lado solicitado |
| 797 | 515.00 | 215.00 | 88.09 | 90.50 | SIM | dentro da janela vertical e do lado solicitado |
| 798 | 515.00 | 214.00 | 89.09 | 91.50 | SIM | dentro da janela vertical e do lado solicitado |
| 799 | 515.00 | 213.00 | 90.09 | 92.50 | SIM | dentro da janela vertical e do lado solicitado |
| 800 | 515.00 | 212.00 | 91.09 | 93.50 | SIM | dentro da janela vertical e do lado solicitado |
| 801 | 514.00 | 211.00 | 92.14 | 94.50 | SIM | dentro da janela vertical e do lado solicitado |
| 802 | 514.00 | 210.00 | 93.13 | 95.50 | SIM | dentro da janela vertical e do lado solicitado |
| 803 | 514.00 | 209.00 | 94.13 | 96.50 | SIM | dentro da janela vertical e do lado solicitado |
| 804 | 514.00 | 208.00 | 95.13 | 97.50 | SIM | dentro da janela vertical e do lado solicitado |
| 805 | 514.00 | 207.00 | 96.13 | 98.50 | SIM | dentro da janela vertical e do lado solicitado |
| 806 | 513.00 | 206.00 | 97.19 | 99.50 | SIM | dentro da janela vertical e do lado solicitado |
| 807 | 513.00 | 205.00 | 98.18 | 100.50 | SIM | dentro da janela vertical e do lado solicitado |
| 808 | 513.00 | 204.00 | 99.18 | 101.50 | SIM | dentro da janela vertical e do lado solicitado |
| 809 | 512.00 | 203.00 | 100.24 | 102.50 | SIM | dentro da janela vertical e do lado solicitado |
| 810 | 512.00 | 202.00 | 101.24 | 103.50 | SIM | dentro da janela vertical e do lado solicitado |
| 811 | 512.00 | 201.00 | 102.24 | 104.50 | SIM | dentro da janela vertical e do lado solicitado |
| 812 | 512.00 | 200.00 | 103.24 | 105.50 | SIM | dentro da janela vertical e do lado solicitado |
| 813 | 511.00 | 199.00 | 104.31 | 106.50 | SIM | dentro da janela vertical e do lado solicitado |
| 814 | 511.00 | 198.00 | 105.30 | 107.50 | SIM | dentro da janela vertical e do lado solicitado |
| 815 | 511.00 | 197.00 | 106.30 | 108.50 | SIM | dentro da janela vertical e do lado solicitado |
| 816 | 511.00 | 196.00 | 107.30 | 109.50 | SIM | dentro da janela vertical e do lado solicitado |
| 817 | 510.00 | 195.00 | 108.37 | 110.50 | SIM | dentro da janela vertical e do lado solicitado |
| 818 | 510.00 | 194.00 | 109.37 | 111.50 | SIM | dentro da janela vertical e do lado solicitado |
| 819 | 510.00 | 193.00 | 110.37 | 112.50 | SIM | dentro da janela vertical e do lado solicitado |
| 820 | 509.00 | 192.00 | 111.45 | 113.50 | SIM | dentro da janela vertical e do lado solicitado |
| 821 | 509.00 | 191.00 | 112.45 | 114.50 | SIM | dentro da janela vertical e do lado solicitado |
| 822 | 509.00 | 190.00 | 113.44 | 115.50 | SIM | dentro da janela vertical e do lado solicitado |
| 823 | 508.00 | 189.00 | 114.53 | 116.50 | SIM | dentro da janela vertical e do lado solicitado |
| 824 | 508.00 | 188.00 | 115.52 | 117.50 | SIM | dentro da janela vertical e do lado solicitado |
| 825 | 508.00 | 187.00 | 116.52 | 118.50 | SIM | dentro da janela vertical e do lado solicitado |
| 826 | 507.00 | 186.00 | 117.61 | 119.50 | SIM | dentro da janela vertical e do lado solicitado |
| 827 | 507.00 | 185.00 | 118.61 | 120.50 | SIM | dentro da janela vertical e do lado solicitado |
| 828 | 507.00 | 184.00 | 119.60 | 121.50 | SIM | dentro da janela vertical e do lado solicitado |
| 829 | 506.00 | 183.00 | 120.70 | 122.50 | SIM | dentro da janela vertical e do lado solicitado |
| 830 | 506.00 | 182.00 | 121.70 | 123.50 | SIM | dentro da janela vertical e do lado solicitado |
| 831 | 505.00 | 181.00 | 122.80 | 124.50 | SIM | dentro da janela vertical e do lado solicitado |
| 832 | 505.00 | 180.00 | 123.79 | 125.50 | SIM | dentro da janela vertical e do lado solicitado |
| 833 | 505.00 | 179.00 | 124.79 | 126.50 | SIM | dentro da janela vertical e do lado solicitado |
| 834 | 504.00 | 178.00 | 125.90 | 127.50 | SIM | dentro da janela vertical e do lado solicitado |
| 835 | 504.00 | 177.00 | 126.89 | 128.50 | SIM | dentro da janela vertical e do lado solicitado |
| 836 | 503.00 | 176.00 | 128.00 | 129.50 | SIM | dentro da janela vertical e do lado solicitado |
| 837 | 503.00 | 175.00 | 129.00 | 130.50 | SIM | dentro da janela vertical e do lado solicitado |
| 838 | 503.00 | 174.00 | 129.99 | 131.50 | SIM | dentro da janela vertical e do lado solicitado |
| 839 | 502.00 | 173.00 | 131.11 | 132.50 | SIM | dentro da janela vertical e do lado solicitado |
| 840 | 502.00 | 172.00 | 132.10 | 133.50 | SIM | dentro da janela vertical e do lado solicitado |
| 841 | 501.00 | 171.00 | 133.22 | 134.50 | SIM | dentro da janela vertical e do lado solicitado |
| 842 | 501.00 | 170.00 | 134.21 | 135.50 | SIM | dentro da janela vertical e do lado solicitado |
| 843 | 500.00 | 169.00 | 135.34 | 136.50 | SIM | dentro da janela vertical e do lado solicitado |
| 844 | 500.00 | 168.00 | 136.33 | 137.50 | NÃO | fora da faixa vertical |
| 845 | 499.00 | 167.00 | 137.46 | 138.50 | NÃO | fora da faixa vertical |
| 846 | 499.00 | 166.00 | 138.45 | 139.50 | NÃO | fora da faixa vertical |
| 847 | 498.00 | 165.00 | 139.59 | 140.50 | NÃO | fora da faixa vertical |
| 848 | 498.00 | 164.00 | 140.58 | 141.50 | NÃO | fora da faixa vertical |
| 849 | 497.00 | 163.00 | 141.72 | 142.50 | NÃO | fora da faixa vertical |
| 850 | 497.00 | 162.00 | 142.71 | 143.50 | NÃO | fora da faixa vertical |
| 851 | 496.00 | 161.00 | 143.85 | 144.50 | NÃO | fora da faixa vertical |
| 852 | 496.00 | 160.00 | 144.84 | 145.50 | NÃO | fora da faixa vertical |
| 853 | 495.00 | 159.00 | 145.99 | 146.50 | NÃO | fora da faixa vertical |
| 854 | 495.00 | 158.00 | 146.97 | 147.50 | NÃO | fora da faixa vertical |
| 855 | 494.00 | 157.00 | 148.12 | 148.50 | NÃO | fora da faixa vertical |
| 856 | 493.00 | 156.00 | 149.28 | 149.50 | NÃO | fora da faixa vertical |
| 857 | 493.00 | 155.00 | 150.27 | 150.50 | NÃO | fora da faixa vertical |
| 858 | 492.00 | 154.00 | 151.43 | 151.50 | NÃO | fora da faixa vertical |
| 859 | 492.00 | 153.00 | 152.41 | 152.50 | NÃO | fora da faixa vertical |
| 860 | 491.00 | 152.00 | 153.57 | 153.50 | NÃO | fora da faixa vertical |
| 861 | 490.00 | 151.00 | 154.74 | 154.50 | NÃO | fora da faixa vertical |
| 862 | 490.00 | 150.00 | 155.72 | 155.50 | NÃO | fora da faixa vertical |
| 863 | 489.00 | 149.00 | 156.89 | 156.50 | NÃO | fora da faixa vertical |
| 864 | 489.00 | 148.00 | 157.88 | 157.50 | NÃO | fora da faixa vertical |
| 865 | 488.00 | 147.00 | 159.05 | 158.50 | NÃO | fora da faixa vertical |
| 866 | 487.00 | 146.00 | 160.23 | 159.50 | NÃO | fora da faixa vertical |
| 867 | 487.00 | 145.00 | 161.21 | 160.50 | NÃO | fora da faixa vertical |
| 868 | 486.00 | 144.00 | 162.39 | 161.50 | NÃO | fora da faixa vertical |
| 869 | 486.00 | 143.00 | 163.37 | 162.50 | NÃO | fora da faixa vertical |
| 870 | 485.00 | 142.00 | 164.55 | 163.50 | NÃO | fora da faixa vertical |
| 871 | 484.00 | 141.00 | 165.74 | 164.50 | NÃO | fora da faixa vertical |
| 872 | 483.00 | 140.00 | 166.93 | 165.50 | NÃO | fora da faixa vertical |
| 873 | 483.00 | 139.00 | 167.90 | 166.50 | NÃO | fora da faixa vertical |
| 874 | 482.00 | 138.00 | 169.10 | 167.50 | NÃO | fora da faixa vertical |
| 875 | 481.00 | 137.00 | 170.29 | 168.50 | NÃO | fora da faixa vertical |
| 876 | 480.00 | 136.00 | 171.49 | 169.50 | NÃO | fora da faixa vertical |
| 877 | 480.00 | 135.00 | 172.47 | 170.50 | NÃO | fora da faixa vertical |
| 878 | 479.00 | 134.00 | 173.67 | 171.50 | NÃO | fora da faixa vertical |
| 879 | 478.00 | 133.00 | 174.87 | 172.50 | NÃO | fora da faixa vertical |
| 880 | 477.00 | 132.00 | 176.08 | 173.50 | NÃO | fora da faixa vertical |
| 881 | 477.00 | 131.00 | 177.05 | 174.50 | NÃO | fora da faixa vertical |
| 882 | 476.00 | 130.00 | 178.26 | 175.50 | NÃO | fora da faixa vertical |
| 883 | 475.00 | 129.00 | 179.48 | 176.50 | NÃO | fora da faixa vertical |
| 884 | 475.00 | 128.00 | 180.45 | 177.50 | NÃO | fora da faixa vertical |
| 885 | 474.00 | 127.00 | 181.66 | 178.50 | NÃO | fora da faixa vertical |
| 886 | 473.00 | 126.00 | 182.88 | 179.50 | NÃO | fora da faixa vertical |
| 887 | 472.00 | 125.00 | 184.10 | 180.50 | NÃO | fora da faixa vertical |
| 888 | 471.00 | 124.00 | 185.32 | 181.50 | NÃO | fora da faixa vertical |
| 889 | 470.00 | 123.00 | 186.55 | 182.50 | NÃO | fora da faixa vertical |
| 890 | 469.00 | 122.00 | 187.78 | 183.50 | NÃO | fora da faixa vertical |
| 891 | 468.00 | 121.00 | 189.01 | 184.50 | NÃO | fora da faixa vertical |
| 892 | 467.00 | 120.00 | 190.24 | 185.50 | NÃO | fora da faixa vertical |
| 893 | 467.00 | 119.00 | 191.21 | 186.50 | NÃO | fora da faixa vertical |
| 894 | 466.00 | 118.00 | 192.44 | 187.50 | NÃO | fora da faixa vertical |
| 895 | 465.00 | 117.00 | 193.68 | 188.50 | NÃO | fora da faixa vertical |
| 896 | 464.00 | 116.00 | 194.92 | 189.50 | NÃO | fora da faixa vertical |
| 897 | 463.00 | 115.00 | 196.16 | 190.50 | NÃO | fora da faixa vertical |
| 898 | 462.00 | 114.00 | 197.41 | 191.50 | NÃO | fora da faixa vertical |
| 899 | 461.00 | 113.00 | 198.66 | 192.50 | NÃO | fora da faixa vertical |
| 900 | 460.00 | 112.00 | 199.90 | 193.50 | NÃO | fora da faixa vertical |
| 901 | 459.00 | 111.00 | 201.16 | 194.50 | NÃO | fora da faixa vertical |
| 902 | 458.00 | 110.00 | 202.41 | 195.50 | NÃO | fora da faixa vertical |
| 903 | 457.00 | 109.00 | 203.67 | 196.50 | NÃO | fora da faixa vertical |
| 904 | 456.00 | 108.00 | 204.92 | 197.50 | NÃO | fora da faixa vertical |
| 905 | 455.00 | 107.00 | 206.18 | 198.50 | NÃO | fora da faixa vertical |
| 906 | 454.00 | 106.00 | 207.45 | 199.50 | NÃO | fora da faixa vertical |
| 907 | 453.00 | 105.00 | 208.71 | 200.50 | NÃO | fora da faixa vertical |
| 908 | 452.00 | 104.00 | 209.98 | 201.50 | NÃO | fora da faixa vertical |
| 909 | 451.00 | 103.00 | 211.24 | 202.50 | NÃO | fora da faixa vertical |
| 910 | 450.00 | 103.00 | 211.57 | 202.50 | NÃO | fora da faixa vertical |
| 911 | 449.00 | 102.00 | 212.84 | 203.50 | NÃO | fora da faixa vertical |
| 912 | 448.00 | 101.00 | 214.11 | 204.50 | NÃO | fora da faixa vertical |
| 913 | 447.00 | 100.00 | 215.39 | 205.50 | NÃO | fora da faixa vertical |
| 914 | 446.00 | 99.00 | 216.67 | 206.50 | NÃO | fora da faixa vertical |
| 915 | 445.00 | 98.00 | 217.95 | 207.50 | NÃO | fora da faixa vertical |
| 916 | 444.00 | 97.00 | 219.23 | 208.50 | NÃO | fora da faixa vertical |
| 917 | 443.00 | 97.00 | 219.57 | 208.50 | NÃO | fora da faixa vertical |
| 918 | 442.00 | 96.00 | 220.86 | 209.50 | NÃO | fora da faixa vertical |
| 919 | 441.00 | 95.00 | 222.14 | 210.50 | NÃO | fora da faixa vertical |
| 920 | 440.00 | 94.00 | 223.43 | 211.50 | NÃO | fora da faixa vertical |
| 921 | 439.00 | 94.00 | 223.79 | 211.50 | NÃO | fora da faixa vertical |
| 922 | 438.00 | 93.00 | 225.08 | 212.50 | NÃO | fora da faixa vertical |
| 923 | 437.00 | 92.00 | 226.37 | 213.50 | NÃO | fora da faixa vertical |
| 924 | 436.00 | 91.00 | 227.67 | 214.50 | NÃO | fora da faixa vertical |
| 925 | 435.00 | 91.00 | 228.04 | 214.50 | NÃO | fora da faixa vertical |
| 926 | 434.00 | 90.00 | 229.33 | 215.50 | NÃO | fora da faixa vertical |
| 927 | 433.00 | 89.00 | 230.63 | 216.50 | NÃO | fora da faixa vertical |
| 928 | 432.00 | 88.00 | 231.94 | 217.50 | NÃO | fora da faixa vertical |
| 929 | 431.00 | 88.00 | 232.31 | 217.50 | NÃO | fora da faixa vertical |
| 930 | 430.00 | 87.00 | 233.62 | 218.50 | NÃO | fora da faixa vertical |
| 931 | 429.00 | 86.00 | 234.92 | 219.50 | NÃO | fora da faixa vertical |
| 932 | 428.00 | 86.00 | 235.31 | 219.50 | NÃO | fora da faixa vertical |
| 933 | 427.00 | 85.00 | 236.62 | 220.50 | NÃO | fora da faixa vertical |
| 934 | 426.00 | 85.00 | 237.01 | 220.50 | NÃO | fora da faixa vertical |
| 935 | 425.00 | 84.00 | 238.32 | 221.50 | NÃO | fora da faixa vertical |
| 936 | 424.00 | 83.00 | 239.64 | 222.50 | NÃO | fora da faixa vertical |
| 937 | 423.00 | 83.00 | 240.03 | 222.50 | NÃO | fora da faixa vertical |
| 938 | 422.00 | 82.00 | 241.35 | 223.50 | NÃO | fora da faixa vertical |
| 939 | 421.00 | 82.00 | 241.75 | 223.50 | NÃO | fora da faixa vertical |
| 940 | 420.00 | 81.00 | 243.07 | 224.50 | NÃO | fora da faixa vertical |
| 941 | 419.00 | 80.00 | 244.40 | 225.50 | NÃO | fora da faixa vertical |
| 942 | 418.00 | 80.00 | 244.81 | 225.50 | NÃO | fora da faixa vertical |
| 943 | 417.00 | 79.00 | 246.13 | 226.50 | NÃO | fora da faixa vertical |
| 944 | 416.00 | 79.00 | 246.55 | 226.50 | NÃO | fora da faixa vertical |
| 945 | 415.00 | 78.00 | 247.87 | 227.50 | NÃO | fora da faixa vertical |
| 946 | 414.00 | 77.00 | 249.20 | 228.50 | NÃO | fora da faixa vertical |
| 947 | 413.00 | 77.00 | 249.62 | 228.50 | NÃO | fora da faixa vertical |
| 948 | 412.00 | 76.00 | 250.95 | 229.50 | NÃO | fora da faixa vertical |
| 949 | 411.00 | 76.00 | 251.38 | 229.50 | NÃO | fora da faixa vertical |
| 950 | 410.00 | 75.00 | 252.72 | 230.50 | NÃO | fora da faixa vertical |
| 951 | 409.00 | 75.00 | 253.15 | 230.50 | NÃO | fora da faixa vertical |
| 952 | 408.00 | 74.00 | 254.48 | 231.50 | NÃO | fora da faixa vertical |
| 953 | 407.00 | 74.00 | 254.92 | 231.50 | NÃO | fora da faixa vertical |
| 954 | 406.00 | 73.00 | 256.26 | 232.50 | NÃO | fora da faixa vertical |
| 955 | 405.00 | 73.00 | 256.70 | 232.50 | NÃO | fora da faixa vertical |
| 956 | 404.00 | 72.00 | 258.04 | 233.50 | NÃO | fora da faixa vertical |
| 957 | 403.00 | 72.00 | 258.49 | 233.50 | NÃO | fora da faixa vertical |
| 958 | 402.00 | 71.00 | 259.83 | 234.50 | NÃO | fora da faixa vertical |
| 959 | 401.00 | 71.00 | 260.28 | 234.50 | NÃO | fora da faixa vertical |
| 960 | 400.00 | 71.00 | 260.74 | 234.50 | NÃO | fora da faixa vertical |
| 961 | 399.00 | 70.00 | 262.09 | 235.50 | NÃO | fora da faixa vertical |
| 962 | 398.00 | 70.00 | 262.55 | 235.50 | NÃO | fora da faixa vertical |
| 963 | 397.00 | 69.00 | 263.89 | 236.50 | NÃO | fora da faixa vertical |
| 964 | 396.00 | 69.00 | 264.36 | 236.50 | NÃO | fora da faixa vertical |
| 965 | 395.00 | 68.00 | 265.71 | 237.50 | NÃO | fora da faixa vertical |
| 966 | 394.00 | 68.00 | 266.18 | 237.50 | NÃO | fora da faixa vertical |
| 967 | 393.00 | 67.00 | 267.53 | 238.50 | NÃO | fora da faixa vertical |
| 968 | 392.00 | 67.00 | 268.00 | 238.50 | NÃO | fora da faixa vertical |
| 969 | 391.00 | 67.00 | 268.48 | 238.50 | NÃO | fora da faixa vertical |
| 970 | 390.00 | 66.00 | 269.83 | 239.50 | NÃO | fora da faixa vertical |
| 971 | 389.00 | 66.00 | 270.31 | 239.50 | NÃO | fora da faixa vertical |
| 972 | 388.00 | 66.00 | 270.80 | 239.50 | NÃO | fora da faixa vertical |
| 973 | 387.00 | 65.00 | 272.15 | 240.50 | NÃO | fora da faixa vertical |
| 974 | 386.00 | 65.00 | 272.64 | 240.50 | NÃO | fora da faixa vertical |
| 975 | 385.00 | 64.00 | 274.00 | 241.50 | NÃO | fora da faixa vertical |
| 976 | 384.00 | 64.00 | 274.49 | 241.50 | NÃO | fora da faixa vertical |
| 977 | 383.00 | 64.00 | 274.99 | 241.50 | NÃO | fora da faixa vertical |
| 978 | 382.00 | 63.00 | 276.35 | 242.50 | NÃO | fora da faixa vertical |
| 979 | 381.00 | 63.00 | 276.85 | 242.50 | NÃO | fora da faixa vertical |
| 980 | 380.00 | 63.00 | 277.35 | 242.50 | NÃO | fora da faixa vertical |
| 981 | 379.00 | 62.00 | 278.71 | 243.50 | NÃO | fora da faixa vertical |
| 982 | 378.00 | 62.00 | 279.22 | 243.50 | NÃO | fora da faixa vertical |
| 983 | 377.00 | 62.00 | 279.72 | 243.50 | NÃO | fora da faixa vertical |
| 984 | 376.00 | 61.00 | 281.09 | 244.50 | NÃO | fora da faixa vertical |
| 985 | 375.00 | 61.00 | 281.60 | 244.50 | NÃO | fora da faixa vertical |
| 986 | 374.00 | 61.00 | 282.12 | 244.50 | NÃO | fora da faixa vertical |
| 987 | 373.00 | 61.00 | 282.63 | 244.50 | NÃO | fora da faixa vertical |
| 988 | 372.00 | 60.00 | 284.00 | 245.50 | NÃO | fora da faixa vertical |
| 989 | 371.00 | 60.00 | 284.52 | 245.50 | NÃO | fora da faixa vertical |
| 990 | 370.00 | 60.00 | 285.04 | 245.50 | NÃO | fora da faixa vertical |
| 991 | 369.00 | 59.00 | 286.42 | 246.50 | NÃO | fora da faixa vertical |
| 992 | 368.00 | 59.00 | 286.94 | 246.50 | NÃO | fora da faixa vertical |
| 993 | 367.00 | 59.00 | 287.47 | 246.50 | NÃO | fora da faixa vertical |
| 994 | 366.00 | 59.00 | 288.00 | 246.50 | NÃO | fora da faixa vertical |
| 995 | 365.00 | 58.00 | 289.38 | 247.50 | NÃO | fora da faixa vertical |
| 996 | 364.00 | 58.00 | 289.91 | 247.50 | NÃO | fora da faixa vertical |
| 997 | 363.00 | 58.00 | 290.45 | 247.50 | NÃO | fora da faixa vertical |
| 998 | 362.00 | 58.00 | 290.99 | 247.50 | NÃO | fora da faixa vertical |
| 999 | 361.00 | 57.00 | 292.37 | 248.50 | NÃO | fora da faixa vertical |
| 1000 | 360.00 | 57.00 | 292.91 | 248.50 | NÃO | fora da faixa vertical |
| 1001 | 359.00 | 57.00 | 293.46 | 248.50 | NÃO | fora da faixa vertical |
| 1002 | 358.00 | 57.00 | 294.00 | 248.50 | NÃO | fora da faixa vertical |
| 1003 | 357.00 | 57.00 | 294.55 | 248.50 | NÃO | fora da faixa vertical |
| 1004 | 356.00 | 56.00 | 295.94 | 249.50 | NÃO | fora da faixa vertical |
| 1005 | 355.00 | 56.00 | 296.49 | 249.50 | NÃO | fora da faixa vertical |
| 1006 | 354.00 | 56.00 | 297.04 | 249.50 | NÃO | fora da faixa vertical |
| 1007 | 353.00 | 56.00 | 297.60 | 249.50 | NÃO | fora da faixa vertical |
| 1008 | 352.00 | 56.00 | 298.16 | 249.50 | NÃO | fora da faixa vertical |
| 1009 | 351.00 | 55.00 | 299.55 | 250.50 | NÃO | fora da faixa vertical |
| 1010 | 350.00 | 55.00 | 300.11 | 250.50 | NÃO | fora da faixa vertical |
| 1011 | 349.00 | 55.00 | 300.67 | 250.50 | NÃO | fora da faixa vertical |
| 1012 | 348.00 | 55.00 | 301.24 | 250.50 | NÃO | fora da faixa vertical |
| 1013 | 347.00 | 55.00 | 301.81 | 250.50 | NÃO | fora da faixa vertical |
| 1014 | 346.00 | 55.00 | 302.38 | 250.50 | NÃO | fora da faixa vertical |
| 1015 | 345.00 | 54.00 | 303.77 | 251.50 | NÃO | fora da faixa vertical |
| 1016 | 344.00 | 54.00 | 304.35 | 251.50 | NÃO | fora da faixa vertical |
| 1017 | 343.00 | 54.00 | 304.92 | 251.50 | NÃO | fora da faixa vertical |
| 1018 | 342.00 | 54.00 | 305.50 | 251.50 | NÃO | fora da faixa vertical |
| 1019 | 341.00 | 54.00 | 306.08 | 251.50 | NÃO | fora da faixa vertical |
| 1020 | 340.00 | 54.00 | 306.66 | 251.50 | NÃO | fora da faixa vertical |
| 1021 | 339.00 | 54.00 | 307.25 | 251.50 | NÃO | fora da faixa vertical |
| 1022 | 338.00 | 54.00 | 307.83 | 251.50 | NÃO | fora da faixa vertical |
| 1023 | 337.00 | 53.00 | 309.23 | 252.50 | NÃO | fora da faixa vertical |
| 1024 | 336.00 | 53.00 | 309.82 | 252.50 | NÃO | fora da faixa vertical |
| 1025 | 335.00 | 53.00 | 310.41 | 252.50 | NÃO | fora da faixa vertical |
| 1026 | 334.00 | 53.00 | 311.01 | 252.50 | NÃO | fora da faixa vertical |
| 1027 | 333.00 | 53.00 | 311.60 | 252.50 | NÃO | fora da faixa vertical |
| 1028 | 332.00 | 53.00 | 312.20 | 252.50 | NÃO | fora da faixa vertical |
| 1029 | 331.00 | 53.00 | 312.80 | 252.50 | NÃO | fora da faixa vertical |
| 1030 | 330.00 | 53.00 | 313.40 | 252.50 | NÃO | fora da faixa vertical |
| 1031 | 329.00 | 53.00 | 314.01 | 252.50 | NÃO | fora da faixa vertical |
| 1032 | 328.00 | 53.00 | 314.61 | 252.50 | NÃO | fora da faixa vertical |
| 1033 | 327.00 | 53.00 | 315.22 | 252.50 | NÃO | fora da faixa vertical |
| 1034 | 326.00 | 53.00 | 315.83 | 252.50 | NÃO | fora da faixa vertical |
| 1035 | 325.00 | 53.00 | 316.44 | 252.50 | NÃO | fora da faixa vertical |
| 1036 | 324.00 | 53.00 | 317.06 | 252.50 | NÃO | fora da faixa vertical |
| 1037 | 323.00 | 53.00 | 317.67 | 252.50 | NÃO | fora da faixa vertical |
| 1038 | 322.00 | 53.00 | 318.29 | 252.50 | NÃO | fora da faixa vertical |
| 1039 | 321.00 | 53.00 | 318.91 | 252.50 | NÃO | fora da faixa vertical |
| 1040 | 320.00 | 53.00 | 319.53 | 252.50 | NÃO | fora da faixa vertical |
| 1041 | 319.00 | 53.00 | 320.16 | 252.50 | NÃO | fora da faixa vertical |
| 1042 | 318.00 | 53.00 | 320.78 | 252.50 | NÃO | fora da faixa vertical |
| 1043 | 317.00 | 53.00 | 321.41 | 252.50 | NÃO | fora da faixa vertical |
| 1044 | 316.00 | 53.00 | 322.04 | 252.50 | NÃO | fora da faixa vertical |
| 1045 | 315.00 | 53.00 | 322.67 | 252.50 | NÃO | fora da faixa vertical |
| 1046 | 314.00 | 53.00 | 323.30 | 252.50 | NÃO | fora da faixa vertical |
| 1047 | 313.00 | 53.00 | 323.94 | 252.50 | NÃO | fora da faixa vertical |
| 1048 | 312.00 | 53.00 | 324.58 | 252.50 | NÃO | fora da faixa vertical |
| 1049 | 311.00 | 53.00 | 325.21 | 252.50 | NÃO | fora da faixa vertical |
| 1050 | 310.00 | 53.00 | 325.85 | 252.50 | NÃO | fora da faixa vertical |
| 1051 | 309.00 | 53.00 | 326.50 | 252.50 | NÃO | fora da faixa vertical |
| 1052 | 308.00 | 53.00 | 327.14 | 252.50 | NÃO | fora da faixa vertical |
| 1053 | 307.00 | 53.00 | 327.79 | 252.50 | NÃO | fora da faixa vertical |
| 1054 | 306.00 | 53.00 | 328.43 | 252.50 | NÃO | fora da faixa vertical |
| 1055 | 305.00 | 53.00 | 329.08 | 252.50 | NÃO | fora da faixa vertical |
| 1056 | 304.00 | 53.00 | 329.73 | 252.50 | NÃO | fora da faixa vertical |
| 1057 | 303.00 | 53.00 | 330.39 | 252.50 | NÃO | fora da faixa vertical |
| 1058 | 302.00 | 53.00 | 331.04 | 252.50 | NÃO | fora da faixa vertical |
| 1059 | 301.00 | 53.00 | 331.70 | 252.50 | NÃO | fora da faixa vertical |
| 1060 | 300.00 | 53.00 | 332.36 | 252.50 | NÃO | fora da faixa vertical |
| 1061 | 299.00 | 53.00 | 333.02 | 252.50 | NÃO | fora da faixa vertical |
| 1062 | 298.00 | 53.00 | 333.68 | 252.50 | NÃO | fora da faixa vertical |

#### Etapa 3 — Resultado final da seleção

| índice | x | y | dist. contato | dist. baseline |
|---|---:|---:|---:|---:|
| 512 | 317.00 | 303.00 | -202.00 | -2.50 |
| 513 | 318.00 | 303.00 | -201.00 | -2.50 |
| 514 | 319.00 | 303.00 | -200.00 | -2.50 |
| 515 | 320.00 | 303.00 | -199.00 | -2.50 |
| 516 | 321.00 | 303.00 | -198.00 | -2.50 |
| 517 | 322.00 | 303.00 | -197.00 | -2.50 |
| 518 | 323.00 | 303.00 | -196.00 | -2.50 |
| 519 | 324.00 | 303.00 | -195.00 | -2.50 |
| 520 | 325.00 | 303.00 | -194.00 | -2.50 |
| 521 | 326.00 | 303.00 | -193.00 | -2.50 |
| 522 | 327.00 | 303.00 | -192.00 | -2.50 |
| 523 | 328.00 | 303.00 | -191.00 | -2.50 |
| 524 | 329.00 | 303.00 | -190.00 | -2.50 |
| 525 | 330.00 | 303.00 | -189.00 | -2.50 |
| 526 | 331.00 | 303.00 | -188.00 | -2.50 |
| 527 | 332.00 | 303.00 | -187.00 | -2.50 |
| 528 | 333.00 | 303.00 | -186.00 | -2.50 |
| 529 | 334.00 | 303.00 | -185.00 | -2.50 |
| 530 | 335.00 | 303.00 | -184.00 | -2.50 |
| 531 | 336.00 | 303.00 | -183.00 | -2.50 |
| 532 | 337.00 | 303.00 | -182.00 | -2.50 |
| 533 | 338.00 | 303.00 | -181.00 | -2.50 |
| 534 | 339.00 | 303.00 | -180.00 | -2.50 |
| 535 | 340.00 | 303.00 | -179.00 | -2.50 |
| 536 | 341.00 | 303.00 | -178.00 | -2.50 |
| 537 | 342.00 | 303.00 | -177.00 | -2.50 |
| 538 | 343.00 | 303.00 | -176.00 | -2.50 |
| 539 | 344.00 | 303.00 | -175.00 | -2.50 |
| 540 | 345.00 | 303.00 | -174.00 | -2.50 |
| 541 | 346.00 | 303.00 | -173.00 | -2.50 |
| 542 | 347.00 | 303.00 | -172.00 | -2.50 |
| 543 | 348.00 | 303.00 | -171.00 | -2.50 |
| 544 | 349.00 | 303.00 | -170.00 | -2.50 |
| 545 | 350.00 | 303.00 | -169.00 | -2.50 |
| 546 | 351.00 | 303.00 | -168.00 | -2.50 |
| 547 | 352.00 | 303.00 | -167.00 | -2.50 |
| 548 | 353.00 | 303.00 | -166.00 | -2.50 |
| 549 | 354.00 | 303.00 | -165.00 | -2.50 |
| 550 | 355.00 | 303.00 | -164.00 | -2.50 |
| 551 | 356.00 | 303.00 | -163.00 | -2.50 |
| 552 | 357.00 | 303.00 | -162.00 | -2.50 |
| 553 | 358.00 | 303.00 | -161.00 | -2.50 |
| 554 | 359.00 | 303.00 | -160.00 | -2.50 |
| 555 | 360.00 | 303.00 | -159.00 | -2.50 |
| 556 | 361.00 | 303.00 | -158.00 | -2.50 |
| 557 | 362.00 | 303.00 | -157.00 | -2.50 |
| 558 | 363.00 | 303.00 | -156.00 | -2.50 |
| 559 | 364.00 | 303.00 | -155.00 | -2.50 |
| 560 | 365.00 | 303.00 | -154.00 | -2.50 |
| 561 | 366.00 | 303.00 | -153.00 | -2.50 |
| 562 | 367.00 | 303.00 | -152.00 | -2.50 |
| 563 | 368.00 | 303.00 | -151.00 | -2.50 |
| 564 | 369.00 | 303.00 | -150.00 | -2.50 |
| 565 | 370.00 | 303.00 | -149.00 | -2.50 |
| 566 | 371.00 | 303.00 | -148.00 | -2.50 |
| 567 | 372.00 | 303.00 | -147.00 | -2.50 |
| 568 | 373.00 | 303.00 | -146.00 | -2.50 |
| 569 | 374.00 | 303.00 | -145.00 | -2.50 |
| 570 | 375.00 | 303.00 | -144.00 | -2.50 |
| 571 | 376.00 | 303.00 | -143.00 | -2.50 |
| 572 | 377.00 | 303.00 | -142.00 | -2.50 |
| 573 | 378.00 | 303.00 | -141.00 | -2.50 |
| 574 | 379.00 | 303.00 | -140.00 | -2.50 |
| 575 | 380.00 | 303.00 | -139.00 | -2.50 |
| 576 | 381.00 | 303.00 | -138.00 | -2.50 |
| 577 | 382.00 | 303.00 | -137.00 | -2.50 |
| 578 | 383.00 | 303.00 | -136.00 | -2.50 |
| 579 | 384.00 | 303.00 | -135.00 | -2.50 |
| 580 | 385.00 | 303.00 | -134.00 | -2.50 |
| 581 | 386.00 | 303.00 | -133.00 | -2.50 |
| 582 | 387.00 | 303.00 | -132.00 | -2.50 |
| 583 | 388.00 | 303.00 | -131.00 | -2.50 |
| 584 | 389.00 | 303.00 | -130.00 | -2.50 |
| 585 | 390.00 | 303.00 | -129.00 | -2.50 |
| 586 | 391.00 | 303.00 | -128.00 | -2.50 |
| 587 | 392.00 | 303.00 | -127.00 | -2.50 |
| 588 | 393.00 | 303.00 | -126.00 | -2.50 |
| 589 | 394.00 | 303.00 | -125.00 | -2.50 |
| 590 | 395.00 | 303.00 | -124.00 | -2.50 |
| 591 | 396.00 | 303.00 | -123.00 | -2.50 |
| 592 | 397.00 | 303.00 | -122.00 | -2.50 |
| 593 | 398.00 | 303.00 | -121.00 | -2.50 |
| 594 | 399.00 | 303.00 | -120.00 | -2.50 |
| 595 | 400.00 | 303.00 | -119.00 | -2.50 |
| 596 | 401.00 | 303.00 | -118.00 | -2.50 |
| 597 | 402.00 | 303.00 | -117.00 | -2.50 |
| 598 | 403.00 | 303.00 | -116.00 | -2.50 |
| 599 | 404.00 | 303.00 | -115.00 | -2.50 |
| 600 | 405.00 | 303.00 | -114.00 | -2.50 |
| 601 | 406.00 | 303.00 | -113.00 | -2.50 |
| 602 | 407.00 | 303.00 | -112.00 | -2.50 |
| 603 | 408.00 | 303.00 | -111.00 | -2.50 |
| 604 | 409.00 | 303.00 | -110.00 | -2.50 |
| 605 | 410.00 | 303.00 | -109.00 | -2.50 |
| 606 | 411.00 | 303.00 | -108.00 | -2.50 |
| 607 | 412.00 | 303.00 | -107.00 | -2.50 |
| 608 | 413.00 | 303.00 | -106.00 | -2.50 |
| 609 | 414.00 | 303.00 | -105.00 | -2.50 |
| 610 | 415.00 | 303.00 | -104.00 | -2.50 |
| 611 | 416.00 | 303.00 | -103.00 | -2.50 |
| 612 | 417.00 | 303.00 | -102.00 | -2.50 |
| 613 | 418.00 | 303.00 | -101.00 | -2.50 |
| 614 | 419.00 | 303.00 | -100.00 | -2.50 |
| 615 | 420.00 | 303.00 | -99.00 | -2.50 |
| 616 | 421.00 | 303.00 | -98.00 | -2.50 |
| 617 | 422.00 | 303.00 | -97.00 | -2.50 |
| 618 | 423.00 | 303.00 | -96.00 | -2.50 |
| 619 | 424.00 | 303.00 | -95.00 | -2.50 |
| 620 | 425.00 | 303.00 | -94.00 | -2.50 |
| 621 | 426.00 | 303.00 | -93.00 | -2.50 |
| 622 | 427.00 | 303.00 | -92.00 | -2.50 |
| 623 | 428.00 | 303.00 | -91.00 | -2.50 |
| 624 | 429.00 | 303.00 | -90.00 | -2.50 |
| 625 | 430.00 | 303.00 | -89.00 | -2.50 |
| 626 | 431.00 | 303.00 | -88.00 | -2.50 |
| 627 | 432.00 | 303.00 | -87.00 | -2.50 |
| 628 | 433.00 | 303.00 | -86.00 | -2.50 |
| 629 | 434.00 | 303.00 | -85.00 | -2.50 |
| 630 | 435.00 | 303.00 | -84.00 | -2.50 |
| 631 | 436.00 | 303.00 | -83.00 | -2.50 |
| 632 | 437.00 | 303.00 | -82.00 | -2.50 |
| 633 | 438.00 | 303.00 | -81.00 | -2.50 |
| 634 | 439.00 | 303.00 | -80.00 | -2.50 |
| 635 | 440.00 | 303.00 | -79.00 | -2.50 |
| 636 | 441.00 | 303.00 | -78.00 | -2.50 |
| 637 | 442.00 | 303.00 | -77.00 | -2.50 |
| 638 | 443.00 | 303.00 | -76.00 | -2.50 |
| 639 | 444.00 | 303.00 | -75.00 | -2.50 |
| 640 | 445.00 | 303.00 | -74.00 | -2.50 |
| 641 | 446.00 | 303.00 | -73.00 | -2.50 |
| 642 | 447.00 | 303.00 | -72.00 | -2.50 |
| 643 | 448.00 | 303.00 | -71.00 | -2.50 |
| 644 | 449.00 | 303.00 | -70.00 | -2.50 |
| 645 | 450.00 | 303.00 | -69.00 | -2.50 |
| 646 | 451.00 | 303.00 | -68.00 | -2.50 |
| 647 | 452.00 | 303.00 | -67.00 | -2.50 |
| 648 | 453.00 | 303.00 | -66.00 | -2.50 |
| 649 | 454.00 | 303.00 | -65.00 | -2.50 |
| 650 | 455.00 | 303.00 | -64.00 | -2.50 |
| 651 | 456.00 | 303.00 | -63.00 | -2.50 |
| 652 | 457.00 | 303.00 | -62.00 | -2.50 |
| 653 | 458.00 | 303.00 | -61.00 | -2.50 |
| 654 | 459.00 | 303.00 | -60.00 | -2.50 |
| 655 | 460.00 | 303.00 | -59.00 | -2.50 |
| 656 | 461.00 | 303.00 | -58.00 | -2.50 |
| 657 | 462.00 | 303.00 | -57.00 | -2.50 |
| 658 | 463.00 | 303.00 | -56.00 | -2.50 |
| 659 | 464.00 | 303.00 | -55.00 | -2.50 |
| 660 | 465.00 | 303.00 | -54.00 | -2.50 |
| 661 | 466.00 | 303.00 | -53.00 | -2.50 |
| 662 | 467.00 | 303.00 | -52.00 | -2.50 |
| 663 | 468.00 | 303.00 | -51.00 | -2.50 |
| 664 | 469.00 | 303.00 | -50.00 | -2.50 |
| 665 | 470.00 | 303.00 | -49.00 | -2.50 |
| 666 | 471.00 | 303.00 | -48.00 | -2.50 |
| 667 | 472.00 | 303.00 | -47.00 | -2.50 |
| 668 | 473.00 | 303.00 | -46.00 | -2.50 |
| 669 | 474.00 | 303.00 | -45.00 | -2.50 |
| 670 | 475.00 | 303.00 | -44.00 | -2.50 |
| 671 | 476.00 | 303.00 | -43.00 | -2.50 |
| 672 | 477.00 | 303.00 | -42.00 | -2.50 |
| 673 | 478.00 | 303.00 | -41.00 | -2.50 |
| 674 | 479.00 | 303.00 | -40.00 | -2.50 |
| 675 | 480.00 | 303.00 | -39.00 | -2.50 |
| 676 | 481.00 | 303.00 | -38.00 | -2.50 |
| 677 | 482.00 | 303.00 | -37.00 | -2.50 |
| 678 | 483.00 | 303.00 | -36.00 | -2.50 |
| 679 | 484.00 | 303.00 | -35.00 | -2.50 |
| 680 | 485.00 | 303.00 | -34.00 | -2.50 |
| 681 | 486.00 | 303.00 | -33.00 | -2.50 |
| 682 | 487.00 | 303.00 | -32.00 | -2.50 |
| 683 | 488.00 | 303.00 | -31.00 | -2.50 |
| 684 | 489.00 | 303.00 | -30.00 | -2.50 |
| 685 | 490.00 | 303.00 | -29.00 | -2.50 |
| 686 | 491.00 | 303.00 | -28.00 | -2.50 |
| 687 | 492.00 | 303.00 | -27.00 | -2.50 |
| 688 | 493.00 | 303.00 | -26.00 | -2.50 |
| 689 | 494.00 | 303.00 | -25.00 | -2.50 |
| 690 | 495.00 | 303.00 | -24.00 | -2.50 |
| 691 | 496.00 | 303.00 | -23.00 | -2.50 |
| 692 | 497.00 | 303.00 | -22.00 | -2.50 |
| 693 | 498.00 | 303.00 | -21.00 | -2.50 |
| 694 | 499.00 | 303.00 | -20.00 | -2.50 |
| 695 | 500.00 | 303.00 | -19.00 | -2.50 |
| 696 | 501.00 | 303.00 | -18.00 | -2.50 |
| 697 | 502.00 | 303.00 | -17.00 | -2.50 |
| 698 | 503.00 | 303.00 | -16.00 | -2.50 |
| 699 | 504.00 | 303.00 | -15.00 | -2.50 |
| 700 | 505.00 | 303.00 | -14.00 | -2.50 |
| 701 | 506.00 | 303.00 | -13.00 | -2.50 |
| 702 | 507.00 | 303.00 | -12.00 | -2.50 |
| 703 | 508.00 | 303.00 | -11.00 | -2.50 |
| 704 | 509.00 | 303.00 | -10.00 | -2.50 |
| 705 | 510.00 | 303.00 | -9.00 | -2.50 |
| 706 | 511.00 | 303.00 | -8.00 | -2.50 |
| 707 | 512.00 | 303.00 | -7.00 | -2.50 |
| 708 | 513.00 | 303.00 | -6.00 | -2.50 |
| 709 | 514.00 | 303.00 | -5.00 | -2.50 |
| 710 | 514.00 | 302.00 | -5.00 | -3.50 |
| 711 | 514.00 | 301.00 | -5.00 | -4.50 |
| 712 | 514.00 | 300.00 | -5.00 | -5.50 |
| 713 | 514.00 | 299.00 | -5.00 | -6.50 |
| 714 | 515.00 | 298.00 | -4.00 | -7.50 |
| 715 | 515.00 | 297.00 | -4.00 | -8.50 |
| 716 | 515.00 | 296.00 | -4.00 | -9.50 |
| 717 | 515.00 | 295.00 | -4.00 | -10.50 |
| 718 | 515.00 | 294.00 | -4.00 | -11.50 |
| 719 | 516.00 | 293.00 | -3.00 | -12.50 |
| 720 | 516.00 | 292.00 | -3.00 | -13.50 |
| 721 | 516.00 | 291.00 | -3.00 | -14.50 |
| 722 | 516.00 | 290.00 | -3.00 | -15.50 |
| 723 | 516.00 | 289.00 | -3.00 | -16.50 |
| 724 | 517.00 | 288.00 | -2.00 | -17.50 |
| 725 | 517.00 | 287.00 | -2.00 | -18.50 |
| 726 | 517.00 | 286.00 | -2.00 | -19.50 |
| 727 | 517.00 | 285.00 | -2.00 | -20.50 |
| 728 | 517.00 | 284.00 | -2.00 | -21.50 |
| 729 | 517.00 | 283.00 | -2.00 | -22.50 |
| 730 | 517.00 | 282.00 | -2.00 | -23.50 |
| 731 | 518.00 | 281.00 | -1.00 | -24.50 |
| 732 | 518.00 | 280.00 | -1.00 | -25.50 |
| 733 | 518.00 | 279.00 | -1.00 | -26.50 |
| 734 | 518.00 | 278.00 | -1.00 | -27.50 |
| 735 | 518.00 | 277.00 | -1.00 | -28.50 |
| 736 | 518.00 | 276.00 | -1.00 | -29.50 |
| 737 | 518.00 | 275.00 | -1.00 | -30.50 |
| 738 | 518.00 | 274.00 | -1.00 | -31.50 |
| 739 | 519.00 | 273.00 | 0.00 | -32.50 |
| 740 | 519.00 | 272.00 | 0.00 | -33.50 |
| 741 | 519.00 | 271.00 | 0.00 | -34.50 |
| 742 | 519.00 | 270.00 | 0.00 | -35.50 |
| 743 | 519.00 | 269.00 | 0.00 | -36.50 |
| 744 | 519.00 | 268.00 | 0.00 | -37.50 |
| 745 | 519.00 | 267.00 | 0.00 | -38.50 |
| 746 | 519.00 | 266.00 | 0.00 | -39.50 |
| 747 | 519.00 | 265.00 | 0.00 | -40.50 |
| 748 | 519.00 | 264.00 | 0.00 | -41.50 |
| 749 | 519.00 | 263.00 | 0.00 | -42.50 |
| 750 | 519.00 | 262.00 | 0.00 | -43.50 |
| 751 | 519.00 | 261.00 | 0.00 | -44.50 |
| 752 | 519.00 | 260.00 | 0.00 | -45.50 |
| 753 | 519.00 | 259.00 | 0.00 | -46.50 |
| 754 | 519.00 | 258.00 | 0.00 | -47.50 |
| 755 | 519.00 | 257.00 | 0.00 | -48.50 |
| 756 | 519.00 | 256.00 | 0.00 | -49.50 |
| 757 | 519.00 | 255.00 | 0.00 | -50.50 |
| 758 | 519.00 | 254.00 | 0.00 | -51.50 |
| 759 | 519.00 | 253.00 | 0.00 | -52.50 |
| 760 | 519.00 | 252.00 | 0.00 | -53.50 |
| 761 | 519.00 | 251.00 | 0.00 | -54.50 |
| 762 | 519.00 | 250.00 | 0.00 | -55.50 |
| 763 | 519.00 | 249.00 | 0.00 | -56.50 |
| 764 | 519.00 | 248.00 | 0.00 | -57.50 |
| 765 | 519.00 | 247.00 | 0.00 | -58.50 |
| 766 | 519.00 | 246.00 | 0.00 | -59.50 |
| 767 | 519.00 | 245.00 | 0.00 | -60.50 |
| 768 | 519.00 | 244.00 | 0.00 | -61.50 |
| 769 | 519.00 | 243.00 | 0.00 | -62.50 |
| 770 | 519.00 | 242.00 | 0.00 | -63.50 |
| 771 | 519.00 | 241.00 | 0.00 | -64.50 |
| 772 | 519.00 | 240.00 | 0.00 | -65.50 |
| 773 | 519.00 | 239.00 | 0.00 | -66.50 |
| 774 | 519.00 | 238.00 | 0.00 | -67.50 |
| 775 | 519.00 | 237.00 | 0.00 | -68.50 |
| 776 | 518.00 | 236.00 | -1.00 | -69.50 |
| 777 | 518.00 | 235.00 | -1.00 | -70.50 |
| 778 | 518.00 | 234.00 | -1.00 | -71.50 |
| 779 | 518.00 | 233.00 | -1.00 | -72.50 |
| 780 | 518.00 | 232.00 | -1.00 | -73.50 |
| 781 | 518.00 | 231.00 | -1.00 | -74.50 |
| 782 | 518.00 | 230.00 | -1.00 | -75.50 |
| 783 | 518.00 | 229.00 | -1.00 | -76.50 |
| 784 | 517.00 | 228.00 | -2.00 | -77.50 |
| 785 | 517.00 | 227.00 | -2.00 | -78.50 |
| 786 | 517.00 | 226.00 | -2.00 | -79.50 |
| 787 | 517.00 | 225.00 | -2.00 | -80.50 |
| 788 | 517.00 | 224.00 | -2.00 | -81.50 |
| 789 | 517.00 | 223.00 | -2.00 | -82.50 |
| 790 | 517.00 | 222.00 | -2.00 | -83.50 |
| 791 | 516.00 | 221.00 | -3.00 | -84.50 |
| 792 | 516.00 | 220.00 | -3.00 | -85.50 |
| 793 | 516.00 | 219.00 | -3.00 | -86.50 |
| 794 | 516.00 | 218.00 | -3.00 | -87.50 |
| 795 | 516.00 | 217.00 | -3.00 | -88.50 |
| 796 | 515.00 | 216.00 | -4.00 | -89.50 |
| 797 | 515.00 | 215.00 | -4.00 | -90.50 |
| 798 | 515.00 | 214.00 | -4.00 | -91.50 |
| 799 | 515.00 | 213.00 | -4.00 | -92.50 |
| 800 | 515.00 | 212.00 | -4.00 | -93.50 |
| 801 | 514.00 | 211.00 | -5.00 | -94.50 |
| 802 | 514.00 | 210.00 | -5.00 | -95.50 |
| 803 | 514.00 | 209.00 | -5.00 | -96.50 |
| 804 | 514.00 | 208.00 | -5.00 | -97.50 |
| 805 | 514.00 | 207.00 | -5.00 | -98.50 |
| 806 | 513.00 | 206.00 | -6.00 | -99.50 |
| 807 | 513.00 | 205.00 | -6.00 | -100.50 |
| 808 | 513.00 | 204.00 | -6.00 | -101.50 |
| 809 | 512.00 | 203.00 | -7.00 | -102.50 |
| 810 | 512.00 | 202.00 | -7.00 | -103.50 |
| 811 | 512.00 | 201.00 | -7.00 | -104.50 |
| 812 | 512.00 | 200.00 | -7.00 | -105.50 |
| 813 | 511.00 | 199.00 | -8.00 | -106.50 |
| 814 | 511.00 | 198.00 | -8.00 | -107.50 |
| 815 | 511.00 | 197.00 | -8.00 | -108.50 |
| 816 | 511.00 | 196.00 | -8.00 | -109.50 |
| 817 | 510.00 | 195.00 | -9.00 | -110.50 |
| 818 | 510.00 | 194.00 | -9.00 | -111.50 |
| 819 | 510.00 | 193.00 | -9.00 | -112.50 |
| 820 | 509.00 | 192.00 | -10.00 | -113.50 |
| 821 | 509.00 | 191.00 | -10.00 | -114.50 |
| 822 | 509.00 | 190.00 | -10.00 | -115.50 |
| 823 | 508.00 | 189.00 | -11.00 | -116.50 |
| 824 | 508.00 | 188.00 | -11.00 | -117.50 |
| 825 | 508.00 | 187.00 | -11.00 | -118.50 |
| 826 | 507.00 | 186.00 | -12.00 | -119.50 |
| 827 | 507.00 | 185.00 | -12.00 | -120.50 |
| 828 | 507.00 | 184.00 | -12.00 | -121.50 |
| 829 | 506.00 | 183.00 | -13.00 | -122.50 |
| 830 | 506.00 | 182.00 | -13.00 | -123.50 |
| 831 | 505.00 | 181.00 | -14.00 | -124.50 |
| 832 | 505.00 | 180.00 | -14.00 | -125.50 |
| 833 | 505.00 | 179.00 | -14.00 | -126.50 |
| 834 | 504.00 | 178.00 | -15.00 | -127.50 |
| 835 | 504.00 | 177.00 | -15.00 | -128.50 |
| 836 | 503.00 | 176.00 | -16.00 | -129.50 |
| 837 | 503.00 | 175.00 | -16.00 | -130.50 |
| 838 | 503.00 | 174.00 | -16.00 | -131.50 |
| 839 | 502.00 | 173.00 | -17.00 | -132.50 |
| 840 | 502.00 | 172.00 | -17.00 | -133.50 |
| 841 | 501.00 | 171.00 | -18.00 | -134.50 |
| 842 | 501.00 | 170.00 | -18.00 | -135.50 |
| 843 | 500.00 | 169.00 | -19.00 | -136.50 |

- primeiro índice: 512
- último índice: 843
- quantidade: 332
- contorno totalmente contínuo

#### Etapa 4 — Visualização

![75_geo dir](audit_outputs/75_geo_dir_audit.png)

#### Etapa 5 — Entrada de _calcular_slope_tangente_polynomial()


#### Etapa 6 — Verificação da ordem

NÃO
A ordem foi modificada.

#### Etapa 7 — Polyfit


#### Etapa 8 — Derivada


#### Etapa 9 — Comparação geométrica

![75_geo dir polyfit](audit_outputs/75_geo_dir_polyfit.png)

#### Etapa 10 — Consistência

- Existe salto nos índices? NÃO
- Existe inversão da ordem? NÃO
- Existe ponto duplicado? NÃO
- Existe ponto fora da região? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto abaixo da baseline? VERIFICAR NOS REGISTROS DE SELEÇÃO
- Existe ponto muito distante do contato? VERIFICAR NOS REGISTROS DE SELEÇÃO
- O polyfit usa exatamente os pontos selecionados? NÃO
- A derivada foi calculada exatamente no ponto de contato? VERIFICAR NO CÓDIGO E NO REGISTRO
- O ponto onde a derivada foi calculada pertence ao polinômio? VERIFICAR NO CÓDIGO E NO REGISTRO

#### Etapa 11 — Diagnóstico automático

- A seleção de pontos parece correta? NÃO
- O problema parece estar na seleção? SIM
- O problema parece estar no polyfit? NÃO
- O problema parece estar na derivada? NÃO
- Existe alguma inconsistência detectada?
  - A ordem de seleção e a ordem usada no polyfit não é consistente ou há salto nos índices.
