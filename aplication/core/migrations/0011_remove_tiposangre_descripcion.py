# Generated by Django 5.1.2 on 2024-11-01 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_paciente_tipo_sangre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tiposangre',
            name='descripcion',
        ),
    ]