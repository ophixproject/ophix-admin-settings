from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .models import ServerSettings


@admin.register(ServerSettings)
class ServerSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("Server Identity"),
            {
                "classes": ("wide",),
                "fields": ("title", "title_visible"),
            },
        ),
        (
            _("Environment"),
            {
                "classes": ("wide",),
                "fields": ("env_name", "env_visible_in_header", "env_visible_in_favicon"),
                "description": _(
                    "Short label displayed in the header and favicon to identify the "
                    "deployment environment (e.g. Production, Staging, Dev)."
                ),
            },
        ),
        (
            _("Language Chooser"),
            {
                "classes": ("wide",),
                "fields": (
                    "language_chooser_active",
                    "language_chooser_control",
                    "language_chooser_display",
                ),
            },
        ),
    )

    save_on_top = True

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = ServerSettings.load()
        return HttpResponseRedirect(
            reverse("admin:ophix_admin_settings_serversettings_change", args=[obj.pk])
        )
