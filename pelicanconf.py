#!/usr/bin/env python

from __future__ import unicode_literals

AUTHOR = 'Eklavya Sharma'
SITENAME = "Eklavya's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['img']

MENUITEMS = (
    ('About me', 'https://sharmaeklavya2.github.io'),
)

# Social widget
SOCIAL = (
    ('Github', 'sharmaeklavya2'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SHOW_AUTHORS = False
USE_CATEGORIES = False
DISPLAY_CATEGORIES_ON_MENU = USE_CATEGORIES
USE_TAGS = True
DISPLAY_TAGS_ON_MENU = USE_TAGS
