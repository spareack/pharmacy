# Generated by Django 4.1.5 on 2023-01-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicine",
            name="address",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="medicine",
            name="company",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="medicine",
            name="link",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="medicine",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="medicine",
            name="price",
            field=models.IntegerField(null=True),
        ),
    ]
