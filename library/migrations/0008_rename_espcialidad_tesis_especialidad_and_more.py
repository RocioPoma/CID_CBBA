# Generated by Django 5.1.2 on 2024-11-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_rename_carrera_especialidad_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tesis',
            old_name='espcialidad',
            new_name='especialidad',
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='especialidadName',
            field=models.TextField(max_length=100, verbose_name='especialidad'),
        ),
    ]
