from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OphixAdminSettingsConfig(AppConfig):
    name = "ophix_admin_settings"
    verbose_name = _("Settings")
    admin_order = 810
    default_auto_field = "django.db.models.AutoField"

    def ready(self):
        from django.db.models.signals import post_migrate
        post_migrate.connect(_init_server_settings, sender=self)


def _init_server_settings(sender, **kwargs):
    from django.apps import apps
    from django.conf import settings

    ServerSettings = apps.get_model("ophix_admin_settings", "ServerSettings")
    obj = ServerSettings.load()
    if not obj.title:
        server_name = getattr(settings, "SERVER_NAME", "").strip()
        obj.title = ("Ophix " + server_name).strip() if server_name else "Ophix"
        obj.save(update_fields=["title"])
