# Generated by Django 3.0.7 on 2020-12-20 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201219_2055'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='covidcase',
            index_together={('carga_provincia_nombre', 'clasificacion_resumen', 'fecha_diagnostico')},
        ),
    ]