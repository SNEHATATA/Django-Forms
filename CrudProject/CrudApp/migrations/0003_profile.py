# Generated by Django 5.2.1 on 2025-06-19 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CrudApp", "0002_register"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("image", models.ImageField(upload_to="profiles/")),
            ],
        ),
    ]
