# Generated by Django 5.1.2 on 2024-12-12 14:48

import library.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0023_alter_book_author_alter_book_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='codLib',
            field=models.CharField(max_length=200, null=True, unique=True, validators=[library.models.validate_unique_title], verbose_name='codLib'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='título'),
        ),
    ]
