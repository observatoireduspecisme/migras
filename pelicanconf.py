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
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGIN_PATHS = ['pelican-plugins', 'custom_plugins/pelican-jinja2content', 'custom_plugins']
PLUGINS = ['assets', 'i18n_subsites', 'image_process', 'jinja2content']
JINJA_EXTENSIONS = ['jinja2.ext.i18n', 'jinja2.ext.with_']
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
    'it': {
        'SITENAME': 'Migras - Per una Migros senza foie gras',
    },
    'de': {
        'SITENAME': 'Migras - Für eine Migros ohne foie gras',
    },
}
I18N_UNTRANSLATED_PAGES = 'remove'

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
STATIC_PATHS = ['images', 'extra/CNAME', 'pdfs']
IMAGE_PROCESS = {
    'thumb': ["scale_out 150 120 false", "crop 0 0 150 120"],
}
IMAGE_PROCESS_FORCE = True

MENU = (
    ({
        'fr': "Le foie gras",
        'de': "Die Foie Gras",
        'it': "Il foie gras",
    }, ('gavage', 'suisse')),
    ({
        'fr': "La campagne",
        'de': "Die Kampagne",
        'it': "La campagna",
    }, ('migros', 'soutien', 'materiel')),
    ({
        'fr': "Contact",
        'de': "Kontakt",
        'it': "Contatti",
    }, 'contact')
)

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

GALLERIES = {
    'gavage': [
        ('pleinair.jpg', {
            'fr': "Les canards sont en semi-liberté de leur 40e au 80e jour",
            'de': "Die Enten leben vom 40. bis 80. Tag ihres Lebens in Halbfreiheit",
            'it': "",
        }),
        ('hangar.jpg', {
            'fr': "Puis ils sont enfermés, pour 87% d'entre eux en cages de batterie",
            'de': "Danach werden sie zu 87 % in Batterie-Käfige eingesperrt",
            'it': "",
        }),
        ('cages.jpg', {
            'fr': "Ils ne peuvent ni se lever, ni se retourner, ni étendre leurs ailes",
            'de': "Sie können sich weder aufrichten, noch sich kehren, noch die Flügel ausbreiten",
            'it': "",
        }),
        ('gavage.jpg', {
            'fr': "Pendant 12 jours, ils sont gavés au moyen d'un tube de métal de 25 cm",
            'de': "Während 12 Tagen werden sie mit Hilfe eines 25 cm langen Rohrs gemästet",
            'it': "",
        }),
        ('gavagegrosplan.jpg', {
            'fr': "La suralimentation forcée provoque des blessures et des maladies",
            'de': "Diese Ueberernährung hat Wunden und Krankheiten zur Folge",
            'it': "",
        }),
    ],
    'canetons': [
        ('carroussel2.jpg', {
            'fr': "Chaque année en France, 80 millions de canetons naissent pour le foie gras",
            'de': "Frankreich rechnet jedes Jahr mit 80 Millionen Enten für ihre Leber",
            'it': "",
        }),
        ('sexage.jpg', {
            'fr': "Leur orifice génital est retourné pour différencier les mâles des femelles",
            'de': "Der Genitalbereich der Tiere wird umgestülpt, um die Männchen von den Weibchen zu unterscheiden",
            'it': "",
        }),
        ('chute3.jpg', {
            'fr': "Seuls les mâles sont gavés. Les femelles sont généralement gazées ou broyées",
            'de': "Ausschliesslich die männlichen Enten werden gemästet. Die Weibchen werden vergast oder zerhäckselt",
            'it': "",
        }),
    ],
    'mort': [
        ('mortcage.jpg', {
            'fr': "1 million de canards meurent chaque année en période de gavage",
            'de': "Jedes Jahr sterben 1 Million Enten während der Mästung",
            'it': "",
        }),
        ('egorge.jpg', {
            'fr': "À l'abattoir, ils sont étourdis par électrochoc puis égorgés",
            'de': "Im Schlachthaus betäubt sie ein Elektroschock, bevor ihnen die Kehle durchgeschnitten wird",
            'it': "",
        }),
        ('morts.jpg', {
            'fr': "On extrait de leur cadavre un foie stéatosé de 6 à 10 fois sa taille normale",
            'de': "Ihrem Kadaver entnimmt man eine verfettete Leber, 6 bis 10 Mal  grösser als normal",
            'it': "",
        }),
        ('foie.jpg', {
            'fr': "Le foie de canard gavé à gauche (500g) et le foie de canard normal à droite (75g)",
            'de': "Links eine verfettete Leber (500g), rechts eine normale Leber (75g)",
            'it': "",
        }),
    ],
}
