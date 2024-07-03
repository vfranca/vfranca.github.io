Title: Tutorial
Slug: tutorial
Date: 2024-07-02
Tags: price action, metatrader 5, mtcli, price action
Status: draft

1. METATRADER 5

1.1 Atalhos de teclado.

| Atalho | Descrição |
| ---- | --- |
| CTRL+O | Abre a janela de opções do MetaTrader |
| CTRL+U | Abre a janela de ativos |
| CTRL+I | Abre a janela de indicadores |
| F9 | Abre a janela da boleta |
| CTRL+F9 | Abre a caixa de informações da conta |
| F10 | Abre a janela de preços |

1.2 Opções básicas

Acessar a janela de opções do MT5 (CTRL + O) e a guia Negociação.  
Alterar:  
* Selecionar o ativo padrão.  
* Selecionar o lote padrão.  
* Marcar a opção negociar a um click.  


1.3 Perfis

Recurso do MT5 para salvar um conjunto de gráficos.  
  
| Caminho | Descrição |
| --- | ---- |
| Menu arquivo >> Perfiss >> Salvar perfil como |Cria novo perfil |
| Menu arquivo >> Perfis >> <nome do perfil> | Abre um perfil existente |


1.4 Templates

Recurso do MT5 para salvar um conjunto de configurações aplicadas a um gráfico

| Caminho | Descrição |
| --- | ---- |
| Menu de contexto >> Templates > salvar template como | Salva um novo template |
| Menu de contexto >> Templates >> <nome do template> | Abre um template existente |

1.5 Boleta

Recurso do MT5 para rotear órdens.  
  
Tipos de Ordens:

* a mercado	Envia uma órden para ser executada no melhor preço do momento
* Buy limit	Compra limitada
* Sell limite	Venda limitada
* Buy stop	Compra stop
* Sell stop	Venda stop
* Buy stop limit	Compra stop limitada
* Sell stop limit	Venda stop limitada

2. MTCLI


2.1 Comandos

* mt bars - exibe os candles de diversas formas.  
* mt mm - exibe a média móvel simples.  
* mt rm - exibe o range médio do candle.  

2.2 Os componentes de uma barra

Cada linha do mt bars exibida no prompt de comando representa uma barra (candle) e exibe as seguintes informações:  
* Direção: asc, desc, ob, ou ib;  
* Corpo: range, percentual e tendência;  
* gap: gap de rompimento da barra anterior;  
* Sombra: percentual da maior sombra;  
* Máxima, mínima e fechamento;  
* Range - tamanho do candle em pontos;  
* oscilação: variação percentual do fechamento;  

2.3 As diferentes exibições do gráfico

* padrão - gráfico cheio
* ch - gráfico de máximas e mínimas
* r - gráfico de ranges
* c - gráfico de fechamentos
* h - gráfico de máximas
* l - gráfico de mínimas
* var - gráfico de variações percentuais
* vol - gráfico de volume de negócios

2.5 Medias móveis

mt mm <ativo> - exibe a média móvel aritmética.  

2.6 Ranges

mt rm <ativo> - exibe o range médio de 14 candles.  

	