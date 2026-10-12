# Desafios de Processamento Digital de Imagens

## Visao geral

Colecao de exercicios e scripts academicos de Processamento Digital de Imagens (PDI). O nucleo do projeto compara imagens sinteticas e capturadas, realiza alinhamento, mede diferencas e explora efeitos de borda, ruido e desfoque.

O repositorio e voltado a estudantes e docentes que desejam acompanhar uma implementacao procedural e visual dos conceitos.

## Tecnologias e organizacao

- Python
- OpenCV
- NumPy
- Matplotlib

| Arquivo | Responsabilidade |
|---|---|
| `codigo_desafio_2.py` | carrega, alinha, compara imagens e produz metricas/graficos |
| `recorte.py` | gera imagens sinteticas no formato PPM |
| `DesafiosPDI.pdf` | enunciados de referencia |
| `imgs/`, `temporario/` e `img4.ppm` | entradas e artefatos locais do exercicio |

## Instalacao e execucao

Requer Python e as bibliotecas registradas em `requirements.txt`.

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python codigo_desafio_2.py
```

Para executar a etapa de geracao de imagens:

```bash
python recorte.py
```

Os scripts dependem dos arquivos locais esperados pelos desafios. Caso uma entrada esteja ausente, revise os caminhos definidos no codigo antes de executar.

## Escopo e maturidade

Trata-se de material academico experimental, sem suite automatizada de testes ou dataset formal. Os graficos e metricas devem ser lidos no contexto das imagens fornecidas, e nao como uma avaliacao generalizavel de algoritmos de visao.

## Material para publicacao

**Texto sugerido**

> Neste conjunto de desafios de Processamento Digital de Imagens, transformei conceitos de alinhamento, diferenca entre imagens, bordas, ruido e desfoque em experimentos executaveis. O foco foi tornar cada etapa observavel: da geracao de uma entrada sintetica ao pareamento com uma imagem capturada e a leitura de metricas e graficos. O projeto valoriza o raciocinio experimental e a interpretacao visual, que sao essenciais para compreender os efeitos de pequenas variacoes na aquisicao e no processamento de imagens.

**Capturas recomendadas:** imagem sintetica e capturada lado a lado, mapa de diferenca, histograma de ruido e perfil de intensidade em uma borda.

**Prompt para imagem complementar**

```text
Infografico didatico de processamento digital de imagens, quatro etapas conectadas: imagem sintetica, imagem fotografada desalinhada, alinhamento geometrico, mapa de diferencas e grafico de perfil de borda; estilo universitario limpo, fundo claro, detalhes em azul e laranja, sem marcas e sem texto pequeno.
```
