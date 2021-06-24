from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "forest_inventory.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import forest_inventory.users.signals  # noqa F401
        except ImportError:
            pass
