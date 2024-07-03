Title: 2 - mtcli
Date: 2024-04-15
Tags: price action, metatrader 5
Status: hidden

## Comandos

* mt bars - exibe os candles de diversas formas.  
* mt mm - exibe a média móvel simples.  
* mt rm - exibe o range médio do candle.  

## Os componentes de uma barra

Cada linha do mt bars exibida no prompt de comando representa uma barra (candle) e exibe as seguintes informações:  
* Direção: asc, desc, ob, ou ib;  
* Corpo: range, percentual e tendência;  
* gap: gap de rompimento da barra anterior;  
* Sombra: percentual da maior sombra;  
* Máxima, mínima e fechamento;  
* Range - tamanho do candle em pontos;  
* oscilação: variação percentual do fechamento;  

## As diferentes exibições do gráfico

* padrão - gráfico cheio
* ch - gráfico de máximas e mínimas
* r - gráfico de ranges
* c - gráfico de fechamentos
* h - gráfico de máximas
* l - gráfico de mínimas
* var - gráfico de variações percentuais
* vol - gráfico de volume de negócios

## Medias móveis

mt mm <ativo> - exibe a média móvel aritmética.  

## Ranges

mt rm <ativo> - exibe o range médio de 14 candles.  
