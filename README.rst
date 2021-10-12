=============================
django_18_fast_migrations
=============================

.. commented-out .. image:: https://badge.fury.io/py/django_18_fast_migrations.svg
    :target: https://badge.fury.io/py/django_18_fast_migrations

.. commented-out .. image:: https://travis-ci.org/shaib/django_18_fast_migrations.svg?branch=master
    :target: https://travis-ci.org/shaib/django_18_fast_migrations

.. commented-out .. image:: https://codecov.io/gh/shaib/django_18_fast_migrations/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/shaib/django_18_fast_migrations

Fast migrations from Django 1.10 backported into Django 1.8

Archived
--------
This library became obsolete when Django 1.8 reached EOL, in April 2018. No further changes are expected.


.. commented-out Documentation
   -------------

   The full documentation is at https://django_18_fast_migrations.readthedocs.io.

Usage
-----

Install django_18_fast_migrations::

    pip install django_18_fast_migrations

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_18_fast_migrations',
        ...
    )

Done. Your migrations will now run faster.

Features
--------

* Nothing visible, except the time it takes migrations to run.

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Or::

    (myenv) $ cd $SOURCE_ROOT
    (myenv) $ python tests/django_runtests.py
  
Credits
-------

The changes in Django's migrations code which made this happen were mostly
made by Markus Holtermann and Simon Charette, of the Django project. Of
course, the Django project and in particular migrations have enjoyed many
contributors over the years.

Our contribution here is just to package this code for use in Django 1.8.

This work was partly supported by Matific_.

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Matific: https://matific.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
