from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ophix_admin_settings", "0002_fix_auto_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serversettings",
            name="env_name",
            field=models.CharField(
                blank=True,
                default="",
                max_length=50,
                verbose_name="environment name",
                help_text="Short label shown in the header and favicon (e.g. Production, Staging, Dev).",
            ),
        ),
        migrations.AlterField(
            model_name="serversettings",
            name="env_visible_in_header",
            field=models.BooleanField(
                default=False,
                verbose_name="visible in header",
            ),
        ),
        migrations.AlterField(
            model_name="serversettings",
            name="env_visible_in_favicon",
            field=models.BooleanField(
                default=False,
                verbose_name="visible in favicon",
            ),
        ),
    ]
