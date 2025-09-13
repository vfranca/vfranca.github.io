Title: Como Criei um Plugin OBV com Python e MetaTrader 5
Date: 2025-09-03 14:00
Modified: 2025-09-03 14:30
Status: draft
Category: Programação
Tags: python, metatrader5, trading, cli, obv, mtcli
Slug: plugin-obv-python-mt5
Author: Valmir França da Silva
Summary: Neste post, compartilho como desenvolvi um plugin CLI em Python para calcular o indicador OBV usando a API do MetaTrader 5.

---

Introdução

O indicador *On Balance Volume (OBV)* é uma ferramenta clássica de análise técnica que relaciona volume com variação de preço. Neste post, mostro como criei um *plugin para o projeto [mtcli](https://github.com/vfranca/mtcli)* que calcula o OBV diretamente via linha de comando, usando dados obtidos do MetaTrader 5.

Etapas

1. Conectei ao MetaTrader 5 com `MetaTrader5` Python API.
2. Recuperei os candles com `copy_rates_from_pos`.
3. Apliquei a fórmula do OBV com `numpy`.
4. Criei uma opção para exportar os dados para CSV.
5. Adicionei testes automatizados com `pytest` e `monkeypatch`.

Exemplo de uso

bash
mt obv --symbol WINV25 --periods 100 --csv
```

Resultado
O resultado é um arquivo obv_WINV25.csv contendo:

csv
Data,OBV
2025-09-03 09:00,0
2025-09-03 09:01,1000
...


Conclusão

Com esse plugin, posso visualizar o OBV de qualquer ativo diretamente no terminal — ideal para acessibilidade e automações. O código está disponível em:

[https://github.com/vfranca/mtcli](https://github.com/vfranca/mtcli)
