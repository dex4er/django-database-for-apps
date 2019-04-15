Configuration
=============

.. code:: python

  # list of apps and theirs database
  DATABASE_FOR_APPS = {
      'test_project': 'default',
      '*': 'django',
  }

``*`` matches all applications so the default database might be redefined from
``'default'`` to something else.

Optional
--------

.. code:: python

  # allows relations between databases (default: None)
  DATABASE_FOR_APPS_RELATIONS = True
