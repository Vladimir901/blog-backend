# Generated by Django 4.1.7 on 2023-09-27 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fio', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('theme', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('datetimecreate', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.author')),
            ],
        ),
    ]
