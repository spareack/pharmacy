# Generated by Django 4.1.5 on 2023-01-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Medicine",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("price", models.IntegerField()),
                ("link", models.CharField(max_length=200)),
                ("company", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
    ]
