# Generated by Django 4.0.1 on 2022-03-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_remove_habitacion_imagen_tipohabitacion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='check_out',
            field=models.DateField(verbose_name='Fecha de Salida'),
        ),
    ]
