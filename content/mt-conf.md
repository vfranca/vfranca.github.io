Title: Editando Configurações com `mt conf` no MTCLI
Date: 2025-09-10
Category: mtcli
Tags: mtcli, config, cli
Slug: mtcli-conf
Author: Valmir França da Silva
Summary: Aprenda a gerenciar suas configurações no MTCLI com o comando `mt conf`, de forma simples e eficiente.

O MTCLI permite gerenciar o arquivo `mtcli.ini` diretamente pela linha de comando com o subcomando `conf`.
  
O que é `mtcli.ini`?
  
É o arquivo onde ficam armazenadas configurações que o MTCLI utiliza, como timeframe, número de dígitos, etc. Ele deve estar na mesma pasta onde o comando é executado.
  
---
  
## Usando `mt conf`
  
Ver todas as configurações:
  
```bash
mt conf --list
```
  
Obter o valor de uma configuração:
  
```bash
mt conf --get CHAVE
```
  
Definir/alterar o valor de uma configuração:
  
```bash
mt conf --set CHAVE VALOR
```
  
Restaurar as configurações padrão:
  
```bash
mt conf --reset
```
  
---
  
Exemplo:
  
```bash
mt conf --set period D1
mt conf --get period
```
  
---
  
## Dica
  
Evite editar o arquivo `mtcli.ini` manualmente. O comando `mt conf` valida e organiza tudo para você.  
  
