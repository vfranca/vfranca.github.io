from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *

# URL do site em produção
SITEURL = 'https://vfranca.github.io'
RELATIVE_URLS = False

# Feeds para produção
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Limpa a saída antes de gerar novamente
DELETE_OUTPUT_DIRECTORY = True

# Recursos extras (opcionais)
GOOGLE_ANALYTICS = 'UA-XXXXXXX-X'
DISQUS_SITENAME = 'seudisqus'
