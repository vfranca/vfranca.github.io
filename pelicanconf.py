#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Valmir'
SITENAME = 'Operando no Escuro'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds.atom"
CATEGORY_FEED_ATOM = "feeds/%s.atom"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
     ('mtcli', 'https://pypi.org/project/mtcli/'),
     ('kt-line', 'https://pypi.org/project/kt-line/'),
     ('kt-tr', 'https://pypi.org/project/kt-tr/'),
     ('kt-pullback', 'https://pypi.org/project/kt-pullback/'),
     ('MetaTrader 5', 'https://www.metatrader5.com/pt'),
     ('Manual de price action', 'https://www.priceaction.com.br/conteudo-livre/manual-de-price-action/'),
)

# Social widget
SOCIAL = (
    ('Telegram', 'https://t.me/operandonoescuro'),
    ('Twitter', 'https://twitter.com/vfranca3'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
