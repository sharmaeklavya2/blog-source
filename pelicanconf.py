#!/usr/bin/env python

from __future__ import unicode_literals
import os

PUBLISH = ('PELICAN_PUBLISH' in os.environ)

AUTHOR = 'Eklavya Sharma'
SITENAME = "Eklavya's Blog"
if PUBLISH:
    SITEURL = 'https://sharmaeklavya2.github.io/blog'
else:
    SITEURL = ''
DESCRIPTION = "Eklavya Sharma's blog where he writes about juggling and computer science."

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = False
TIMEZONE = 'Asia/Kolkata'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

SITEMAP = {'format': 'txt'}

MARKDOWN = {
    'extensions': ['codehilite(guess_lang=False, use_pygments=True)'],
}

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

STATIC_PATHS = ['img', 'css']

MENUITEMS = (
    ('About me', 'https://sharmaeklavya2.github.io'),
)

# Social widget
SOCIAL = (
    ('Github', 'sharmaeklavya2'),
)

DEFAULT_PAGINATION = False

RELATIVE_URLS = not PUBLISH

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
