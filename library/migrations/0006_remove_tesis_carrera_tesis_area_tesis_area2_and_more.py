# Generated by Django 5.1.2 on 2024-11-07 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_carrera_tesis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesis',
            name='carrera',
        ),
        migrations.AddField(
            model_name='tesis',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='library_primary', to='library.area'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='area2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='library_secondary', to='library.area'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='espcialidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='speciality_name', to='library.carrera'),
        ),
    ]
