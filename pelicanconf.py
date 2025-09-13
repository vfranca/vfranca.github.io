THEME = 'C:/Users/Administrador/pelican-themes/Flex'
DEFAULT_CATEGORY = "Geral"

SITENAME = 'Blog mtcli'
SITEDESCRIPTION = 'Ferramentas, ideias e métricas para traders'
SITEURL = ''

AUTHOR = 'Valmir França'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'pt-BR'

PATH = 'content'
OUTPUT_PATH = 'docs'

# Social
SOCIAL = (
    ('telegram', 'https://t.me/operandonoescuro'),
    ('github', 'https://github.com/vfranca'),
)

# Links úteis
LINKS = (
    ('mtcli', 'https://pypi.org/project/mtcli/'),
    ('MetaTrader 5', 'https://www.metatrader5.com/pt'),
)

# Flex-specific
SITELOGO = 'images/logo-mtcli.jpg'  # coloque uma imagem em content/images/
# FAVICON = 'images/favicon.ico'
BROWSER_COLOR = '#333'
PYGMENTS_STYLE = 'monokai'

DEFAULT_PAGINATION = 10
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# Outros
MAIN_MENU = True

MENUITEMS = (
    ('Início', '/'),
    ('Contato', '/pages/contato.html'),
)

COPYRIGHT_YEAR = 2025

