# Generated by Django 4.1.7 on 2023-10-03 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_author_id_alter_blog_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="blog",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
