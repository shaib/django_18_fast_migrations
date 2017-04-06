"""
A migrate command which does some monkeypatching on the migration executor
to use a backporting of the migration performance-improvement fixes
introduced in later versions of Django
"""
import django
from django.core.management.commands import migrate
from django.core.exceptions import ImproperlyConfigured

from django_18_fast_migrations.migration_executor_patched import monkeypatch


class Command(migrate.Command):

    def handle(self, **options):
        if django.VERSION >= (1,9):
            raise ImproperlyConfigured("Please remove the django_18_fast_migrations package\n"
                                       "It is intended for use with Django 1.8.x only")
        # Monkeypatch
        monkeypatch(migrate)
        # Invoke original
        return super(Command, self).handle(**options)
