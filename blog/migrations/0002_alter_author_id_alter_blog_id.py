# Generated by Django 4.1.7 on 2023-10-03 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="id",
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="blog",
            name="id",
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
