from colorfield.fields import ColorField
from django.db import models
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

    message_autohide_enabled = models.BooleanField(
        default=False,
        verbose_name=_("auto-dismiss enabled"),
        help_text=_("Automatically dismiss success and info banners after the timeout. Errors and warnings remain until page reload or user dismissal."),
    )
    message_autohide_delay = models.PositiveSmallIntegerField(
        default=4000,
        verbose_name=_("auto-dismiss delay (ms)"),
        help_text=_("Milliseconds before success and info banners are dismissed."),
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

    def clean(self):
        from django.core.exceptions import ValidationError

        from .validators import (
            SETTINGS_COLOR_FIELDS,
            validate_env_name,
            validate_server_title,
        )

        errors = {}

        def _check(field_name, validator):
            try:
                validator(getattr(self, field_name) or "")
            except ValidationError as exc:
                errors[field_name] = exc

        for field_name in SETTINGS_COLOR_FIELDS:
            value = (getattr(self, field_name) or "").strip()
            setattr(self, field_name, value)

        _check("title", validate_server_title)
        _check("env_name", validate_env_name)

        if errors:
            raise ValidationError(errors)

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
