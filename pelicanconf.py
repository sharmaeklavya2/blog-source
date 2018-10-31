#!/usr/bin/env python

from __future__ import unicode_literals

AUTHOR = 'Eklavya Sharma'
SITENAME = "Eklavya's Blog"
SITEURL = ''
DESCRIPTION = "Eklavya Sharma's blog where he writes about juggling and computer science."

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

SITEMAP = {'format': 'txt'}

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

CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''
