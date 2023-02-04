AUTHOR = 'Charles'
SITENAME = 'Das Bityard'
SITEURL = ''
PATH = 'content'
THEME = 'themes/cpto'

TIMEZONE = 'America/Detroit'
DEFAULT_DATE = 'fs'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/{slug}.rss.xml'
TAG_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = None
AUTHOR_FEED_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index', 'tags', 'archives']
TEMPLATE_EXTENSIONS = ['.html.j2', '.html']

#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.do']}

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'articles/{date:%Y}/{date:%B}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%B}/{slug}.html'

ARCHIVES_SAVE_AS = 'articles/index.html'
YEAR_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'articles/{date:%Y}/{date:%B}/index.html'

STATIC_PATHS = [
    'extra/headers',
]
EXTRA_PATH_METADATA = {
    'extra/headers': {'path': '_headers'},
}

USE_FOLDER_AS_CATEGORY = False

# Provides document-relative URLs when developing
RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'guess_lang': False,
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
