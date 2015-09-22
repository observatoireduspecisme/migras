import os

from bs4 import BeautifulSoup
from jinja2 import Template
from pelican import signals


current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, 'gallery.html'), 'r') as f:
    template = Template(f.read())


def test(sender):
    global template

    if not sender._content:
        return

    html = BeautifulSoup(sender._content, 'html.parser')
    galleries = html.select('a[href^="{gallery}"]')

    for gallery in galleries:
        gallery_name = gallery['href'].replace('{gallery}', '')
        rendered_gallery = template.render({
            'photos': sender.settings['GALLERIES'][gallery_name]
        })

        p = gallery.parent
        p.replace_with(BeautifulSoup(rendered_gallery, 'html.parser'))

    sender._content = unicode(html)
    #print(html.encode())
    #print(foo)


def register():
    signals.content_object_init.connect(test)
