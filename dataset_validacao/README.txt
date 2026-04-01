Pasta reservada para imagens de validação de regressão.

Sugestão de estrutura:
- sinteticas/: imagens com ângulos conhecidos (GeoGebra)
- reais/: fotos calibradas com gabarito
- labels.csv: nome_arquivo,angulo_esq_ref,angulo_dir_ref,tolerancia_deg

A suíte atual usa testes sintéticos gerados em memória.
Ao adicionar imagens reais, crie testes parametrizados em tests/.
