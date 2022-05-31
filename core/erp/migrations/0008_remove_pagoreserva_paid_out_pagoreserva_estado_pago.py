# Generated by Django 4.0.1 on 2022-04-13 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_habitacion_obs_alter_pagoreserva_paid_out_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagoreserva',
            name='paid_out',
        ),
        migrations.AddField(
            model_name='pagoreserva',
            name='estado_pago',
            field=models.CharField(choices=[('cancelado', 'Cancelado'), ('pendiente', 'Pendiente'), ('sin cancelar', 'Sin Cancelar')], default='Pendiente', max_length=25, verbose_name='Estado de Pago'),
        ),
    ]