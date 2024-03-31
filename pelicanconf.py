#!/usr/bin/env python

from __future__ import unicode_literals
import json
import os
import logging
import markdown.util

AUTHOR = 'Eklavya Sharma'
SITENAME = "Eklavya's Blog"
DESCRIPTION = "Eklavya Sharma's blog where he writes about juggling and computer science."

PATH = 'content'
STATIC_PATHS = ['img', 'css']
MENUITEMS = (
    ('About me', 'https://sharmaeklavya2.github.io'),
)
TIMEZONE = 'Asia/Kolkata'
PUBLISH = ('PELICAN_PUBLISH' in os.environ)
RELATIVE_URLS = not PUBLISH
if PUBLISH:
    SITEURL = 'https://sharmaeklavya2.github.io/blog'
else:
    SITEURL = ''
NUMBER_HEADINGS = True

# Plugins

PLUGIN_PATHS = ['plugins', 'official-plugins']
# Order is important: plugins in `plugins` override plugins in `official-plugins`.
PLUGINS = ['sitemap', 'my_plugin', 'pelican_katex']

SITEMAP = {'format': 'txt'}

MARKDOWN = {
    'output_format': 'html5',
    'extension_configs': {
        'codehilite': {'guess_lang': False, 'use_pygments': True},
        'toc': {
            'title': 'Table of Contents',
            'permalink': True,
            'toc_depth': "2-3",
        },
        'md_in_html': {},
    }
}

for tag in ('figure', 'figcaption'):
    markdown.util.BLOCK_LEVEL_ELEMENTS.remove(tag)

MATH_JAX = {
    'auto_insert': False,
    'url': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js',
    'hub_config': {
        "jax": ["input/TeX", "output/CommonHTML"],
        "extensions": ["tex2jax.js"],
        "TeX": {
            "extensions": ["AMSmath.js", "AMSsymbols.js", "noErrors.js", "noUndefined.js"]
        },
    },
}

with open('package.json') as fp:
    NPM_DEP_VERSIONS = json.load(fp)['dependencies']

KATEX_VERSION = NPM_DEP_VERSIONS['katex']
KATEX_COMMON = {
    'version': KATEX_VERSION,
    'prefix': 'https://cdn.jsdelivr.net/npm/katex@' + KATEX_VERSION + '/dist',
    'defer_css': False,
    'options': {
        "output": "html",
        "fleqn": True,
        "macros": {
            "\\eps": "\\varepsilon",
            "\\E": "\\operatorname{\\mathbb{E}}",
            "\\defeq": ":=",
            "\\vecone": "\\mathbf{1}",
            "\\xhat": "\\widehat{x}",
            "\\yhat": "\\widehat{y}",
        }
    },
    'preload_fonts': [
        'KaTeX_Main-Regular.woff2',
        'KaTeX_Math-Italic.woff2',
        'KaTeX_Size1-Regular.woff2',
        'KaTeX_AMS-Regular.woff2',
        'KaTeX_Typewriter-Regular.woff2',
    ],
}
KATEX_PATH = "katex"
KATEX = KATEX_COMMON['options']

# Show tags but not categories and authors

SHOW_AUTHORS = False
USE_CATEGORIES = False
DISPLAY_CATEGORIES_ON_MENU = USE_CATEGORIES
USE_TAGS = True
DISPLAY_TAGS_ON_MENU = USE_TAGS

CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Feed

CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feed/all.atom.xml'
FEED_ALL_RSS = 'feed/all.rss.xml'
TAG_FEED_ATOM = 'feed/{slug}.atom.xml'
TAG_FEED_RSS = 'feed/{slug}.rss.xml'


# Prevent logging useless warnings

def filter_dotsvg(record):
    msg_match = record.msg == 'Cannot get modification stamp for %s\n\t%s'
    ext_match = record.args[0].endswith('.dot.svg') or record.args[0].endswith('.gif.mp4')
    return 0 if msg_match and ext_match else 1


cache_logger = logging.getLogger('pelican.cache')
cache_logger.addFilter(filter_dotsvg)
