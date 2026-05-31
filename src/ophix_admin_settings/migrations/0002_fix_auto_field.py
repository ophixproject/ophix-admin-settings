from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Corrects the id field definition in the migration state to match what
    Django generates for auto-created primary keys. No database changes.
    """

    dependencies = [
        ("ophix_admin_settings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serversettings",
            name="id",
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]
