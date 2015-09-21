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
PLUGINS = ['assets', 'i18n_subsites', 'image_process']
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
THEME = 'themes/migras'
ASSET_SOURCE_PATHS = [
    'static',
]

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
STATIC_PATHS = ['images', 'extra/CNAME']
IMAGE_PROCESS = {
    'thumb': ["scale_out 150 120 false", "crop 0 0 150 120"],
}
IMAGE_PROCESS_FORCE = True

SUPPORTERS = (
    ('pea', "https://www.asso-pea.ch/", "PEA - Pour l'Égalité Animale"),
    ('agstg', "http://www.agstg.ch/", "AGSTG - Aktionsgemeinschaft Schweizer Tierversuchgegner"),
    ('atra', "http://www.atra.info/", "ATRA - Associazione svizzera per l'abolizione della vivisezione"),
    ('borta', "http://www.borta.org/", "BORTA"),
    ('chatsdesrues', "http://www.chatsdesrues.ch/", "Chats des rues"),
    ('hall', "http://www.al-hallmarks.net/", "Animal Liberation Hallmarks"),
    ('jv_neuchatel', "http://www.jvne.ch/", "Jeunes vert-e-s Neuchâtel"),
    ('l214', "http://www.l214.com/", "L214"),
    ('ligue_vaudoise_defense_animaux', "http://www.defense-animaux.ch/", "Ligue vaudoise de défense des animaux"),
    ('lscv', "http://www.lscv.ch/", "LSCV - Ligue suisse contre la vivisection"),
    ('mart', "http://www.mart.ch/", "MART - Mouvement pour les Animaux et le Respect de la Terre"),
    ('stopgavage', "http://www.stopgavage.com/", "Stop gavage"),
)
