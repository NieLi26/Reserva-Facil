# Generated by Django 4.0.1 on 2022-03-03 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reservaservicioextra',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Huesped'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='habitacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erp.habitacion', verbose_name='Habitacion'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Huesped'),
        ),
        migrations.AddField(
            model_name='region',
            name='user_creation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='region',
            name='user_update',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_update', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='plan',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.cliente', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='plan',
            name='tipo_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.tipoplan', verbose_name='Tipo de Plan'),
        ),
        migrations.AddField(
            model_name='pagoreserva',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.reserva', verbose_name='Reserva'),
        ),
        migrations.AddField(
            model_name='imagenhabitacion',
            name='tipo_habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.tipohabitacion', verbose_name=' Tipo de Habitacion'),
        ),
        migrations.AddField(
            model_name='hospedaje',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.comuna', verbose_name='Comuna'),
        ),
        migrations.AddField(
            model_name='hospedaje',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.plan', verbose_name='Plan'),
        ),
        migrations.AddField(
            model_name='hospedaje',
            name='tipo_hospedaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.tipohospedaje', verbose_name='Tipo de hospedaje'),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='piso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.piso', verbose_name='Piso'),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='servicio_habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.serviciohabitacion', verbose_name='Servicio de Habitacion'),
        ),
        migrations.AddField(
            model_name='habitacion',
            name='tipo_habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.tipohabitacion', verbose_name='Tipo de Habitacion'),
        ),
        migrations.AddField(
            model_name='gestor',
            name='hospedaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.hospedaje', verbose_name='Hospedaje'),
        ),
        migrations.AddField(
            model_name='gestor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='detallereserva',
            name='reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.reserva', verbose_name='Reserva'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.region', verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='calification',
            name='habitacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.habitacion', verbose_name='Habitacion'),
        ),
    ]