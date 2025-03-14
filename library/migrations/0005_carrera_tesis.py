# Generated by Django 5.1.2 on 2024-11-07 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_area2_alter_book_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carreraName', models.TextField(max_length=100, verbose_name='carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Tesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, verbose_name='title')),
                ('author', models.TextField(max_length=100, verbose_name='author')),
                ('publish_date', models.DateField(null=True, verbose_name='publish_date')),
                ('universidad', models.TextField(max_length=100, verbose_name='editorial')),
                ('pages', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='pages')),
                ('description', models.TextField(max_length=800, verbose_name='description')),
                ('kword', models.CharField(max_length=10, null=True, verbose_name='kword')),
                ('files', models.FileField(upload_to='pdfs', verbose_name='files')),
                ('images', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='images')),
                ('carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carreraname', to='library.carrera')),
            ],
        ),
    ]
