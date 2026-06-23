from django.conf import settings
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .models import ServerSettings


@admin.register(ServerSettings)
class ServerSettingsAdmin(admin.ModelAdmin):

    def response_change(self, request, obj):
        if "_save" in request.POST:
            self.message_user(request, _("Server Settings saved successfully."), messages.SUCCESS)
            return HttpResponseRedirect(reverse("admin:index"))
        if "_continue" in request.POST:
            self.message_user(request, _("Server Settings saved successfully."), messages.SUCCESS)
            return HttpResponseRedirect(request.path)
        return super().response_change(request, obj)
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
                "fields": (
                    "env_name",
                    "env_visible_in_header",
                    ("env_color", "env_color_dark_use", "env_color_dark"),
                    ("env_text_color", "env_text_color_dark_use", "env_text_color_dark"),
                ),
                "description": _(
                    "Small badge displayed in the header to identify the deployment environment "
                    "(e.g. PROD, DEV, TEST)."
                ),
            },
        ),
        (
            _("Notifications"),
            {
                "classes": ("wide",),
                "fields": ("message_autohide_enabled", "message_autohide_delay"),
                "description": _(
                    "Configure automatic dismissal of system notifications. "
                    "Only success and info notifications are auto-dismissed; errors and warnings remain until page reload or user dismissal."
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

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        from django.conf import settings as django_settings
        if getattr(django_settings, "SHOW_THEME_MODEL", True):
            try:
                from admin_interface.models import Theme
                extra_context["active_theme"] = Theme.objects.get_active()
            except Exception:
                extra_context["active_theme"] = None
        else:
            extra_context["active_theme"] = None
        return super().change_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = ServerSettings.load()
        return HttpResponseRedirect(
            reverse("admin:ophix_admin_settings_serversettings_change", args=[obj.pk])
        )


if not getattr(settings, "SHOW_SETTINGS_MODEL", False):
    try:
        admin.site.unregister(ServerSettings)
    except admin.sites.NotRegistered:
        pass
