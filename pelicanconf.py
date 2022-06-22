#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Valmir'
SITENAME = 'mtcli MetaTrader 5 para cegos'
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
     ('MetaTrader 5', 'https://www.metatrader5.com/pt'),
     ('Manual de price action', 'https://www.priceaction.com.br/conteudo-livre/manual-de-price-action/'),
)

# Social widget
SOCIAL = (
    ('Telegram', 'https://t.me/operandonoescuro'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
