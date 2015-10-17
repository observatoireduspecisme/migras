Migras site
===========

This is the content for migras.ch. It uses
`Pelican <http://docs.getpelican.com/en/>`_ as a site generator.

Installation
------------

You'll most likely want to create a virtual environment first. Once this is
done, install the project requirements::

    pip install -r requirements.txt

Site generation
---------------

Run the following command to generate the content::

    pelican content

If you want to see the result, run::

    fab serve

And point your browser to http://localhost:8000/.

Deploying
---------

Run the following::

    make github
