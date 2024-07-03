#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Valmir França'
SITENAME = 'Price Action Acessível'
SITEURL = 'https://vfranca.github.io'
RELATIVE_URLS = True

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt-BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds.atom"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
     ('mtcli', 'https://pypi.org/project/mtcli/'),
     ('MetaTrader 5', 'https://www.metatrader5.com/pt'),
     ('Portal Price Action', 'https://www.priceaction.com.br')
)

# Social widget
SOCIAL = (
    ('Telegram', 'https://t.me/operandonoescuro'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
