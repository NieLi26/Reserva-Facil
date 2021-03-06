# Generated by Django 4.0.1 on 2022-03-03 02:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(default=0, verbose_name='Nota')),
            ],
            options={
                'verbose_name': 'Calificacion',
                'verbose_name_plural': 'Calificaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('rut', models.CharField(max_length=10, verbose_name='Rut')),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('mail', models.EmailField(max_length=30, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25, null=True)),
                ('color1', models.CharField(max_length=20)),
                ('color2', models.CharField(max_length=20)),
                ('logo', models.ImageField(upload_to='logotipos')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_adultos', models.IntegerField(blank=True, default=0, verbose_name='Numero de Adultos')),
                ('numero_niños', models.IntegerField(blank=True, default=0, verbose_name='Numero de Niños')),
                ('numero_mascotas', models.IntegerField(blank=True, default=0, verbose_name='Numero de Mascotas')),
                ('desc', models.TextField(verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Detalle de reserva',
                'verbose_name_plural': 'Detalle de reservas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='gestores/%Y/%m/%d')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Gestor',
                'verbose_name_plural': 'Gestores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_habitacion', models.CharField(choices=[('disponible', 'Disponible'), ('ocupada', 'Ocupada'), ('limpieza', 'Limpieza'), ('mantenimiento', 'Mantenimiento')], default='disponible', max_length=15, verbose_name='Estado Habitacion')),
                ('numero_habitacion', models.CharField(max_length=3, verbose_name='Numero de Habitacion')),
                ('capacidad', models.IntegerField(default=0, verbose_name='Capacidad')),
                ('desc', models.TextField(verbose_name='Descripcion')),
                ('activo', models.BooleanField(default=False, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Hospedaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Hospedaje',
                'verbose_name_plural': 'Hospedajes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ImagenHabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='habitaciones/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Imagen de Habitacion',
                'verbose_name_plural': 'Imagenes de Habitaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('porcentaje', models.IntegerField(default=0, verbose_name='Porcentaje')),
            ],
            options={
                'verbose_name': 'Porcentaje',
                'verbose_name_plural': 'Porcentajes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PagoReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avance', models.IntegerField(default=0, verbose_name='Adelanto')),
                ('total', models.IntegerField(default=0, verbose_name='Valor total')),
                ('resto', models.IntegerField(default=0, verbose_name='Restante')),
                ('obs', models.TextField(blank=True, max_length=200, null=True, verbose_name='Observacion')),
                ('paid_out', models.BooleanField(default=True, verbose_name='Pagado')),
            ],
            options={
                'verbose_name': 'Pago Reserva',
                'verbose_name_plural': 'Pagos Reserva',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('activo', models.BooleanField(default=False, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Piso',
                'verbose_name_plural': 'Pisos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('meses_contratados', models.IntegerField(default=0, verbose_name='Meses Contratados')),
                ('fecha_inicio', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de inicio')),
                ('valor', models.IntegerField(blank=True, default=0, null=True, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Planes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now=True, null=True)),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_reserva', models.CharField(choices=[('sin confirmar', 'Sin Confirmar'), ('confirmada', 'Confirmada'), ('no ingreso', 'No Ingreso'), ('alojamiento terminado', 'Alojamiento Terminado')], default='sin confirmar', max_length=25, verbose_name='Estado de Reserva')),
                ('subtotal', models.IntegerField(default=0, verbose_name='Subtotal')),
                ('total', models.IntegerField(default=0, verbose_name='Total a pagar')),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='IVA')),
                ('avance', models.IntegerField(blank=True, default=0, null=True, verbose_name='Adelanto')),
                ('check_in', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Entrada')),
                ('check_out', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Salida')),
                ('obs', models.TextField(blank=True, null=True, verbose_name='Observacion')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ServicioExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('desc', models.TextField(verbose_name='Descripcion')),
                ('tarifa', models.FloatField(default=0, verbose_name='Tarifa')),
                ('activo', models.BooleanField(default=False, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Servicio extra ',
                'verbose_name_plural': 'Servicios extras',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ServicioHabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de Habitacion',
                'verbose_name_plural': 'Tipos de Habitaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('tarifa', models.IntegerField(default=0, verbose_name='Tarifa')),
            ],
            options={
                'verbose_name': 'Tipo de Habitacion',
                'verbose_name_plural': 'Tipos de Habitaciones',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoHospedaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Categoria de Sucursal',
                'verbose_name_plural': 'Categorias de sucursal',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('valor_mensual', models.IntegerField(blank=True, default=0, null=True, verbose_name='Valor mensual')),
                ('desc', models.TextField(max_length=100, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de plan',
                'verbose_name_plural': 'Tipos de plan',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ReservaServicioExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_realizacion', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Realizacion')),
                ('servicio_extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.servicioextra', verbose_name='Servicio Extra')),
            ],
            options={
                'verbose_name': 'Reserva de servicio extra',
                'verbose_name_plural': 'Reserva de servicios extras',
                'ordering': ['id'],
            },
        ),
    ]
