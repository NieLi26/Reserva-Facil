# Generated by Django 4.0.1 on 2022-03-01 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_rename_name_tipohospedaje_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avance', models.IntegerField(default=0, verbose_name='Adelanto')),
                ('total', models.IntegerField(default=0, verbose_name='Valor total')),
                ('resto', models.IntegerField(default=0, verbose_name='Restante')),
                ('obs', models.TextField(blank=True, max_length=200, null=True, verbose_name='Observacion')),
                ('paid_out', models.BooleanField(default=True, verbose_name='Pagado')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.reserva', verbose_name='Reserva')),
            ],
            options={
                'verbose_name': 'Pago Reserva',
                'verbose_name_plural': 'Pagos Reserva',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Pagos',
        ),
    ]