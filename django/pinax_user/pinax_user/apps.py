from django.apps import AppConfig as BaseAppConfig
from django.utils.importlib import import_module


class AppConfig(BaseAppConfig):

    name = "pinax_user"

    def ready(self):
        import_module("pinax_user.receivers")
