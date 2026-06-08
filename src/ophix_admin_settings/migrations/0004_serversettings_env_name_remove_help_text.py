from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ophix_admin_settings", "0003_remove_env_visible_in_favicon"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name="serversettings",
                    name="env_name",
                    field=models.CharField(
                        blank=True,
                        default="",
                        max_length=50,
                        verbose_name="environment name",
                    ),
                ),
            ],
        ),
    ]
