# Generated by Django 4.0.1 on 2022-03-27 05:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_alter_reserva_check_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='check_out',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Salida'),
        ),
    ]