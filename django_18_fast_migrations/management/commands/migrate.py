"""
A migrate command which does some monkeypatching on the migration executor
to use a backporting of the migration performance-improvement fixes
introduced in later versions of Django
"""
import warnings

import django
from django.core.management.commands import migrate
from django.core.exceptions import ImproperlyConfigured

from django_18_fast_migrations.migration_executor_patched import monkeypatch


class Command(migrate.Command):

    def handle(self, **options):
        if django.VERSION >= (1, 10):
            raise ImproperlyConfigured("Please remove the django_18_fast_migrations package\n"
                                       "Its improvements are already included in Django itself")
        elif django.VERSION >= (1, 9):
            warnings.warn("Django 1.9 is no longer supported", DeprecationWarning)
        # Monkeypatch
        monkeypatch(migrate)
        # Invoke original
        return super(Command, self).handle(**options)
