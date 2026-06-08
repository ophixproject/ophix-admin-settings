from django.db import migrations


class Migration(migrations.Migration):
    """Remove env_visible_in_favicon — favicon badge is always disabled."""

    dependencies = [
        ("ophix_admin_settings", "0002_serversettings_env_colors"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="serversettings",
            name="env_visible_in_favicon",
        ),
    ]
