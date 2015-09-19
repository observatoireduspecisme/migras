#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Association Migros sans foie gras'
SITENAME = u'Migras'
SITEURL = ''
PAGE_URL = '{slug}/'
PAGE_LANG_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_SAVE_AS = '{slug}/index.html'
PAGE_ORDER_BY = 'position'

PATH = 'content'

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

LANGUAGES = (
    ('de', 'Deutsch'),
    ('fr', 'Français'),
    ('it', 'Italiano'),
)

I18N_SUBSITES = {
    'fr': {
        'SITENAME': 'Migras - Pour une Migros sans foie gras',
    },
    'it': {
        'SITENAME': 'Migras - Per une Migros senza foie gras',
    },
    'de': {
        'SITENAME': 'Migras - Für eine Migros ohne foie gras',
    },
}
I18N_UNTRANSLATED_PAGES = 'remove'

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
STATIC_PATHS = ['extra/CNAME']
