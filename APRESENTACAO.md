# Apresentação Profissional - Desafios de PDI

## Identidade e Valor

Coleção de experimentos científicos e computacionais voltados aos fundamentos do Processamento Digital de Imagens (PDI). O projeto investiga a transição entre imagens sintéticas ideais e fotografias do mundo real, abordando alinhamento geométrico, quantificação de diferenças espectrais, modelagem estatística de ruído de sensor e estimativa de desfoque óptico via Edge Spread Function (ESF) e Line Spread Function (LSF).

## Texto para Publicação

> Como modelar matematicamente a diferença entre o que um computador desenha e o que uma câmera fotografa? Neste projeto de fundamentos de Processamento Digital de Imagens, estruturei um pipeline experimental que alinha imagens sintéticas a capturas reais, mede o erro pixel a pixel e modela a degradação física: ruído gaussiano aditivo de sensor e espalhamento de borda (desfoque óptico via ESF e LSF). O trabalho demonstra como conceitos teóricos de Fourier, amostragem e resposta ao impulso se traduzem em diagnósticos numéricos práticos para calibração de visão computacional.

## Evidências Visuais Recomendadas

1. Mapa de diferenças absolutas com mapa de calor jet (`evidencias/exp1_diferenca_alinhamento.png`).
2. Perfil de intensidade comparando degrau ideal e borda real suavizada (`evidencias/exp2_perfil_borda.png`).
3. Histograma de ruído e ajuste de distribuição (`evidencias/exp3_histograma_ruido.png`).
4. Simulação de degradação com injeção de ruído Gaussiano e PSNR (`evidencias/exp4_simulacao_ruido.png`).
5. Modelagem de desfoque óptico com curvas ESF e LSF (`evidencias/exp5_desfoque_esf_lsf.png`).
6. Relatório Executivo Word diagramado (`PID_Fundamentos_Relatorio_Publicacao.docx`).

## Prompt para Imagem Complementar

```text
Diagrama científico de processamento digital de imagens: uma imagem geométrica digital perfeita passa por uma lente de câmera real, gerando ruído e desfoque; gráficos de perfil de intensidade de borda (ESF/LSF) e mapa de calor de erro conectam os dois mundos, estilo paper acadêmico, paleta azul marinho e ciano, fundo claro, sem logotipos.
```
