# Generated by Django 5.1.2 on 2024-11-01 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_tiposangre_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='tipo_sangre',
            field=models.ForeignKey(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tipos_sangre', to='core.tiposangre', verbose_name='Tipo de Sangre'),
        ),
        migrations.AlterField(
            model_name='tiposangre',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='tiposangre',
            name='tipo',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=15, unique=True, verbose_name='Tipo de Sangre'),
        ),
    ]