# Generated by Django 5.1.2 on 2024-11-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_tiposangre_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiposangre',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripcion'),
        ),
    ]