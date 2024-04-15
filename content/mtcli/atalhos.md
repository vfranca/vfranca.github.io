Title: Atalhos de comandos
Date: 2021-10-17
Modified: 2024-04-15
Tags: mtcli, atalhos de comandos, workspace
Status: published

| Atalho | Comando | Descrição | Indicado para |
| ---- | ---- | ----- | --- |
| dd1 | mt bars <ticker> -p daily | gráfico cheio com todas as informações do candle do diário | ler força de barras e outras leituras |
| d1 | mt bars <ticker> -p daily -v ch | gráfico de máximas e mínimas do diário | ler canais |
| d1r | mt bars <ticker> -p daily -v r | gráfico de ranges do diário | identificar rompimentos ou clímax |
| d1o | mt bars <ticker> -p daily -v var | gráfico com as oscilações percentuais fechamento contra fechamento do diário | ler somente as variações percentuais |
| d1c | mt bars <ticker> -p daily -v c | gráfico com os fechamentos do diário | ler somente os fechamentos como no gráfico de linhas |
| d1v | mt bars <ticker> -p daily -v vol | gráfico com os volumes de negociação em ticks  do diário | ler somente o volume de negócios |

  
Para os demais tempos gráficos substitua o d1:  

* mn1 para mensal (monthly)
* w1 para semanal (weekly)
* h4 para 4 horas
* h1 para 1 hora
* m15 para 15min
* m5 para 5min
  
Os atalhos para variação percentual, volume e fechamento estão disponíveis apenas a partir do diário

