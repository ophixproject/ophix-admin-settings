from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ophix_admin_settings", "0004_serversettings_env_name_remove_help_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="serversettings",
            name="message_autohide_enabled",
            field=models.BooleanField(
                default=False,
                help_text="Automatically dismiss success and info banners after the timeout. Errors and warnings remain until page reload or user dismissal.",
                verbose_name="auto-dismiss enabled",
            ),
        ),
        migrations.AddField(
            model_name="serversettings",
            name="message_autohide_delay",
            field=models.PositiveSmallIntegerField(
                default=4000,
                help_text="Milliseconds before success and info banners are dismissed.",
                verbose_name="auto-dismiss delay (ms)",
            ),
        ),
    ]
