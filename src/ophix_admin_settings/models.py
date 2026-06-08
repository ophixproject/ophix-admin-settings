from colorfield.fields import ColorField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class ServerSettings(models.Model):
    title = models.CharField(
        max_length=50,
        default="",
        blank=True,
        verbose_name=_("title"),
        help_text=_("Displayed in the browser tab and admin header (e.g. TaskServer, CredServer)."),
    )
    title_visible = models.BooleanField(
        default=True,
        verbose_name=_("title visible"),
    )

    env_name = models.CharField(
        blank=True,
        default="",
        max_length=50,
        verbose_name=_("environment name"),
        help_text=_("Short label shown in the header and favicon (e.g. Production, Staging, Dev)."),
    )
    env_visible_in_header = models.BooleanField(
        default=False,
        verbose_name=_("visible in header"),
    )
    env_color = ColorField(
        blank=True,
        default="#ddab52",
        max_length=10,
        verbose_name=_("badge color"),
        help_text=_("Background colour of the environment badge."),
    )
    env_color_dark_use = models.BooleanField(
        default=False,
        verbose_name=_("dark?"),
    )
    env_color_dark = ColorField(
        blank=True,
        default="",
        max_length=10,
        verbose_name=_("dark"),
    )
    env_text_color = ColorField(
        blank=True,
        default="#1a1a1a",
        max_length=10,
        verbose_name=_("badge text color"),
        help_text=_("Text colour of the environment badge."),
    )
    env_text_color_dark_use = models.BooleanField(
        default=False,
        verbose_name=_("dark?"),
    )
    env_text_color_dark = ColorField(
        blank=True,
        default="",
        max_length=10,
        verbose_name=_("dark"),
    )

    language_chooser_control_choices = (
        ("default-select", _("Default Select")),
        ("minimal-select", _("Minimal Select")),
    )
    language_chooser_active = models.BooleanField(
        default=True,
        verbose_name=_("language chooser active"),
    )
    language_chooser_control = models.CharField(
        max_length=20,
        choices=language_chooser_control_choices,
        default="default-select",
        verbose_name=_("language chooser control"),
    )
    language_chooser_display_choices = (
        ("code", _("code")),
        ("name", _("name")),
    )
    language_chooser_display = models.CharField(
        max_length=10,
        choices=language_chooser_display_choices,
        default="code",
        verbose_name=_("language chooser display"),
    )

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    class Meta:
        verbose_name = _("Server Settings")
        verbose_name_plural = _("Server Settings")

    def __str__(self):
        return self.title or "Server Settings"


@receiver(post_save, sender=ServerSettings)
def server_settings_post_save(sender, instance, **kwargs):
    from .context_processors import del_cached_settings
    del_cached_settings()
