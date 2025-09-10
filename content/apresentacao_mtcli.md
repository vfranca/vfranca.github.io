Title: mtcli — Acessibilidade e Análise Técnica no Terminal
Date: 2025-09-03 15:00
Category: Projetos
Tags: mtcli, metatrader5, acessibilidade, cli, python, trading
Slug: apresentando-mtcli
Author: Valmir França da Silva
Summary: Conheça o mtcli, uma interface de linha de comando para o MetaTrader 5, desenvolvida com foco em acessibilidade para pessoas cegas ou com baixa visão.

---

O que é o mtcli?

O mtcli é um aplicativo CLI (Command-Line Interface) desenvolvido em Python para interação acessível com dados de mercado do MetaTrader 5. Seu principal objetivo é permitir que traders com deficiência visual possam acessar gráficos, indicadores técnicos e informações da conta de forma navegável e textual, totalmente compatível com leitores de tela.

---

A quem se destina?

- Pessoas cegas ou com baixa visão, que enfrentam dificuldades com interfaces gráficas complexas.
- Traders que preferem o terminal ou querem integrar dados do MetaTrader em scripts automatizados.
- Desenvolvedores e entusiastas que buscam uma forma leve e extensível de interagir com o MetaTrader 5.

---

Recursos principais
- ✅ Acesso aos candles do MetaTrader 5 com navegação tecla por tecla.
- ✅ Exibição de padrões de velas com descrição acessível.
- ✅ Indicadores embutidos e plugins opcionais:
  - Médias móveis
  - Volume médio
  - Range médio
  - OBV (On Balance Volume)
- ✅ Exportação para CSV.
- ✅ Plugins extensíveis via arquitetura modular.
- ✅ Suporte a ambientes virtuais com poetry.
- ✅ Compatibilidade com leitores de tela como NVDA e JAWS.

---

Como obter e instalar

Você pode instalar o mtcli diretamente do PyPI:

bash
pip install mtcli


Ou clonando o repositório:

bash
git clone https://github.com/vfranca/mtcli.git
cd mtcli
poetry install


Para executar:

bash
mt grafico --symbol WINV25 --periods 100


---

Documentação

A documentação está disponível em:

*[https://vfranca.github.io/mtcli](https://vfranca.github.io/mtcli)*

---

Contribua!

O projeto é livre (GPLv3) e aberto a contribuições. Seja para desenvolvimento, testes ou sugestões de usabilidade acessível.

Repositório:  
*[https://github.com/vfranca/mtcli](https://github.com/vfranca/mtcli)*

---

Se você é uma pessoa cega ou conhece alguém que busca mais autonomia no mercado financeiro, o mtcli foi feito com esse propósito.

```
Se quiser, posso gerar também um index.rst ou conteúdo de docs/README.md com base nesse texto.
