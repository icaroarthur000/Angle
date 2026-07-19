# Relatório de Continuidade da Investigação - Projeto Angle

## Objetivo

Este documento consolida as conclusões já obtidas durante a investigação matemática e geométrica do algoritmo de cálculo de ângulo de contato. O propósito é permitir a continuidade da análise sem repetir auditorias já concluídas.

## Etapas já investigadas

As seguintes etapas do pipeline foram auditadas com o pipeline real do projeto, sem modificações no código-fonte:

- Extração do contorno (`contorno.py`)
- Detecção da baseline (`linha_base.py`)
- Determinação dos pontos de contato
- Seleção da região (`_selecionar_pontos_lado()`)
- Seleção dos pontos para a tangente (`_selecionar_pontos_tangente()`)
- Ajuste polinomial (`_calcular_slope_tangente_polynomial()`)
- Ajuste circular
- Conversão final do ângulo

A investigação utilizou:

- imagens de auditoria;
- CSVs dos pontos;
- relatórios automáticos;
- inspeção visual;
- comparação com gotas sintéticas de 30°, 50°, 75°, 100° e 130°.

## Conclusões validadas

### 1. Contorno

O contorno extraído representa corretamente a geometria da gota.

Não foram observados:

- saltos;
- descontinuidades;
- perda significativa de pontos.

Esta etapa não é considerada a origem do erro.

### 2. Baseline

A baseline acompanha corretamente o substrato.

Não foram encontrados indícios de que a baseline seja a causa principal dos erros de ângulo.

### 3. Pontos de contato

Os pontos de contato apresentam comportamento consistente na maioria dos casos analisados.

Não existem evidências de que esta etapa seja a origem principal da divergência.

### 4. Ajuste polinomial

O algoritmo de ajuste polinomial (`polyfit`) executa corretamente o ajuste sobre os pontos que recebe.

Até o momento não há evidências de erro matemático no algoritmo de ajuste em si.

## Principal resultado da investigação

A primeira perda significativa de representatividade geométrica ocorre antes do cálculo da tangente.

Os pontos enviados ao ajuste polinomial deixam de representar exclusivamente a vizinhança do ponto de contato.

Em diversos casos, o conjunto utilizado mistura regiões da gota com comportamentos geométricos diferentes, como:

- arco local próximo ao contato;
- região inferior achatada;
- base horizontal, quando existente;
- regiões superiores do arco em gotas obtusas.

Como consequência:

- a parábola ajustada deixa de representar a curvatura local;
- a derivada calculada deixa de representar a tangente física;
- o ângulo final torna-se incorreto.

## Situação atual da investigação

A investigação da origem do erro é considerada concluída.

O foco agora deixa de ser identificar onde o erro nasce e passa a ser compreender por que o conjunto de pontos utilizado para estimar a tangente não representa adequadamente a geometria local da gota.

## Próxima etapa

Antes de implementar qualquer correção, é necessário responder às seguintes questões:

1. Como `_selecionar_pontos_lado()` define a região candidata?
2. Como `_selecionar_pontos_tangente()` escolhe os pontos finais?
3. Esses critérios realmente representam apenas a vizinhança local do ponto de contato?
4. Existe algum critério geométrico mais adequado para selecionar os pontos da tangente?
5. O problema está:
   - na altura da janela?
   - na forma de ordenação dos pontos?
   - no critério de escolha dos 12 pontos?
   - ou na combinação desses fatores?

## Instruções para a nova etapa

Nesta fase não devem ser propostas correções imediatamente.

O objetivo é realizar uma investigação exclusivamente sobre o processo de seleção dos pontos da tangente.

A análise deve responder, com base em evidências matemáticas e geométricas:

- quais pontos entram em cada etapa;
- quais pontos são descartados;
- por que são descartados;
- quais critérios matemáticos estão sendo utilizados;
- se esses critérios representam corretamente a geometria local do ponto de contato.

Somente após essa análise será definida a estratégia de correção.

## Observação final

Não se deve assumir que a solução é apenas reduzir a altura da janela ou alterar parâmetros numéricos. A investigação precisa identificar a causa matemática do problema. Alterações no algoritmo só devem ser propostas após a causa estar comprovada por evidências.