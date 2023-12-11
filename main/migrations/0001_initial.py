# Generated by Django 3.1.5 on 2021-01-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Do_list",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=50)),
                ("information", models.TextField()),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("check", models.BooleanField(default=False)),
                ("state", models.BooleanField(default=True)),
            ],
        ),
    ]