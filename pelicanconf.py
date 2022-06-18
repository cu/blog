AUTHOR = 'Charles'
SITENAME = 'Das Bityard'
SITEURL = ''
PATH = 'content'
THEME = 'themes/cpto'

TIMEZONE = 'America/Detroit'
DEFAULT_DATE = 'fs'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

#DIRECT_TEMPLATES = ('index', 'archives')
TEMPLATE_EXTENSIONS = ['.html', '.html.j2']

#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.do']}

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'articles/{date:%Y}/{date:%B}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%B}/{slug}.html'

ARCHIVES_SAVE_AS = 'articles/index.html'
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%B}/index.html'

USE_FOLDER_AS_CATEGORY = False

# Provides document-relative URLs when developing
RELATIVE_URLS = True

