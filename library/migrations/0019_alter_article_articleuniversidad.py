# Generated by Django 5.1.2 on 2024-12-05 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_campo_area_alter_campo_camponame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='articleUniversidad',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_university', to='library.universidad'),
        ),
    ]
