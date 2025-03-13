# Generated by Django 5.1.2 on 2024-11-29 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0016_alter_favorite_book_alter_favorite_thesis_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='articleDescription',
            field=models.TextField(max_length=1200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='articleFiles',
            field=models.FileField(max_length=1000, upload_to='pdfs', verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='article',
            name='articleKword',
            field=models.CharField(max_length=100, null=True, verbose_name='kword'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=1200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='files',
            field=models.FileField(max_length=1000, upload_to='pdfs', verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='book',
            name='images',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='logos', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='book',
            name='kword',
            field=models.CharField(max_length=100, null=True, verbose_name='kword'),
        ),
        migrations.AlterField(
            model_name='campo',
            name='campoName',
            field=models.TextField(max_length=200, verbose_name='campo'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='description',
            field=models.TextField(max_length=1200, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='files',
            field=models.FileField(max_length=1000, upload_to='pdfs', verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='kword',
            field=models.CharField(max_length=100, null=True, verbose_name='kword'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='universidad',
            field=models.ForeignKey(blank=True, max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='library_university', to='library.universidad'),
        ),
        migrations.AlterField(
            model_name='universidad',
            name='universityName',
            field=models.TextField(max_length=200, verbose_name='university'),
        ),
    ]
