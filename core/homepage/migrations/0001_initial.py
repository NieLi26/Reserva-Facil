# Generated by Django 4.0.1 on 2022-04-15 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apellido')),
                ('tipo_documento', models.CharField(blank=True, choices=[('pasaporte', 'Pasaporte'), ('DNI', 'DNI'), ('carnet extranjeria', 'Carnet Extranjeria')], default='DNI', max_length=25, null=True, verbose_name='Tipo de Documento')),
                ('numero_documento', models.IntegerField(blank=True, null=True, verbose_name='Numero de Documento')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('telefono', models.IntegerField(blank=True, null=True, verbose_name='telefono')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
