# apps.py
"""Django app."""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """CoreConfig class."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
