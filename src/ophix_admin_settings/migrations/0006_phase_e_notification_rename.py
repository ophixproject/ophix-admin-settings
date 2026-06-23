from django.db import migrations, models


class Migration(migrations.Migration):
    """Update help_text: 'banners' → 'notifications' (Phase E naming #9)."""

    dependencies = [
        ("ophix_admin_settings", "0005_serversettings_message_autohide"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serversettings",
            name="message_autohide_enabled",
            field=models.BooleanField(
                default=False,
                help_text="Automatically dismiss success and info notifications after the timeout. Errors and warnings remain until page reload or user dismissal.",
                verbose_name="auto-dismiss enabled",
            ),
        ),
        migrations.AlterField(
            model_name="serversettings",
            name="message_autohide_delay",
            field=models.PositiveSmallIntegerField(
                default=4000,
                help_text="Milliseconds before success and info notifications are dismissed.",
                verbose_name="auto-dismiss delay (ms)",
            ),
        ),
    ]
