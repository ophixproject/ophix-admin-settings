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
                help_text="Automatically hide success and info banners after the timeout. Errors and warnings are never auto-hidden.",
                verbose_name="auto-hide enabled",
            ),
        ),
        migrations.AddField(
            model_name="serversettings",
            name="message_autohide_delay",
            field=models.PositiveSmallIntegerField(
                default=4000,
                help_text="Milliseconds before success and info banners are hidden.",
                verbose_name="auto-hide delay (ms)",
            ),
        ),
    ]
