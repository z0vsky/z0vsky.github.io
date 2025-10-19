from datetime import datetime
NOW = datetime.now()

AUTHOR = 'z0vsky'
SITENAME = 'z0vsky'
SITEURL = ''

PATH = 'content'
THEME = 'themes/pelican-mofo-solarized'

TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGINS = [
    #'plugins.minify',
    'sitemap',
]

STATIC_PATHS = ['assets', 'extra']

EXTRA_PATH_METADATA = {
    'extra/apple-icon-57x57.png': {'path': 'apple-icon-57x57.png'},
    'extra/apple-icon-60x60.png': {'path': 'apple-icon-60x60.png'},
    'extra/apple-icon-72x72.png': {'path': 'apple-icon-72x72.png'},
    'extra/apple-icon-76x76.png': {'path': 'apple-icon-76x76.png'},
    'extra/apple-icon-114x114.png': {'path': 'apple-icon-114x114.png'},
    'extra/apple-icon-120x120.png': {'path': 'apple-icon-120x120.png'},
    'extra/apple-icon-144x144.png': {'path': 'apple-icon-144x144.png'},
    'extra/apple-icon-152x152.png': {'path': 'apple-icon-152x152.png'},
    'extra/apple-icon-180x180.png': {'path': 'apple-icon-180x180.png'},
    'extra/android-icon-192x192.png': {'path': 'android-icon-192x192.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/manifest.json': {'path': 'manifest.json'},
    'extra/ms-icon-144x144.png': {'path': 'ms-icon-144x144.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_PAGINATION = False

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'guess_lang':False,},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = '{slug}.html'
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
PAGE_SAVE_AS = '{slug}.html'
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
