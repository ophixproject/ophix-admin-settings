import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ophix_admin_settings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="serversettings",
            name="env_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#ddab52",
                help_text="Background colour of the environment badge.",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="badge color",
            ),
        ),
        migrations.AddField(
            model_name="serversettings",
            name="env_color_dark_use",
            field=models.BooleanField(default=False, verbose_name="dark?"),
        ),
        migrations.AddField(
            model_name="serversettings",
            name="env_color_dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default="",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="dark",
            ),
        ),
        migrations.AddField(
            model_name="serversettings",
            name="env_text_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#1a1a1a",
                help_text="Text colour of the environment badge.",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="badge text color",
            ),
        ),
        migrations.AddField(
            model_name="serversettings",
            name="env_text_color_dark_use",
            field=models.BooleanField(default=False, verbose_name="dark?"),
        ),
        migrations.AddField(
            model_name="serversettings",
            name="env_text_color_dark",
            field=colorfield.fields.ColorField(
                blank=True,
                default="",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="dark",
            ),
        ),
    ]
