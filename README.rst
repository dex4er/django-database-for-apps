.. image:: https://img.shields.io/pypi/v/django-database-for-apps.svg
   :target: https://pypi.python.org/pypi/django-database-for-apps
.. image:: https://travis-ci.org/dex4er/django-database-for-apps.svg?branch=master
   :target: https://travis-ci.org/dex4er/django-database-for-apps
.. image:: https://readthedocs.org/projects/django-database-for-apps/badge/?version=latest
   :target: http://django-database-for-apps.readthedocs.org/en/latest/
.. image:: https://img.shields.io/pypi/pyversions/django-database-for-apps.svg
   :target: https://www.python.org/
.. image:: https://img.shields.io/pypi/djversions/django-database-for-apps.svg
   :target: https://www.djangoproject.com/

django-database-for-apps
========================

``django-database-for-apps`` is a package that provides a router which chooses
a database based on app name.


Installation
------------

Install with ``pip`` or ``pipenv``:

.. code:: python

  pip install django-database-for-apps

Add ``django_database_for_apps`` to your installed apps in your
settings.py file:

.. code:: python

  INSTALLED_APPS = [
      'django_database_for_apps',
      ...
  ]


Configuration
-------------

.. code:: python

  # list of apps and theirs database
  DATABASE_FOR_APPS = {
      'test_project': 'default',
      '*': 'django',
  }

``*`` matches all applications so the default database might be redefined from
``'default'`` to something else.

Optional
^^^^^^^^

.. code:: python

  # allows relations between databases (default: None)
  DATABASE_FOR_APPS_RELATIONS = True


Documentation
-------------

See http://django-database-for-apps.readthedocs.org/


License
-------

Copyright © 2019, Piotr Roszatycki

This software is distributed under the GNU Lesser General Public License (LGPL
3 or greater).
