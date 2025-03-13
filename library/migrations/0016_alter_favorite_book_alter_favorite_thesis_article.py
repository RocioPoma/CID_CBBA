# Generated by Django 5.1.2 on 2024-11-27 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_favorite_thesis_alter_favorite_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='thesis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.tesis'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleTitle', models.TextField(max_length=200, verbose_name='articleTitle')),
                ('articleAuthor', models.TextField(max_length=100, verbose_name='articleAuthor')),
                ('articlePublish_date', models.DateField(null=True, verbose_name='publish_date')),
                ('articlePages', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='pages')),
                ('articleDescription', models.TextField(max_length=800, verbose_name='description')),
                ('articleKword', models.CharField(max_length=10, null=True, verbose_name='kword')),
                ('articleFiles', models.FileField(upload_to='pdfs', verbose_name='files')),
                ('articleImages', models.ImageField(blank=True, max_length=1000, null=True, upload_to='logos', verbose_name='images')),
                ('articleArea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_primary', to='library.area')),
                ('articleArea2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_secondary', to='library.area')),
                ('articleCampo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='library.campo')),
                ('articleUniversidad', models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='article_university', to='library.universidad')),
            ],
        ),
    ]
