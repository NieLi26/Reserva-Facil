import imp
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms

User = get_user_model()

class Huesped(models.Model):
    tipo_documento_choices = {
    ('DNI', 'DNI'),
    ('pasaporte', 'Pasaporte'),
    ('carnet extranjeria', 'Carnet Extranjeria')
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', blank=True, null=True)
    apellido = models.CharField(max_length=50, verbose_name='Apellido', blank=True, null=True)
    tipo_documento = models.CharField(max_length=25, choices=tipo_documento_choices, default="DNI", verbose_name="Tipo de Documento", blank=True, null=True)
    numero_documento = models.IntegerField(verbose_name="Numero de Documento", blank=True, null=True)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    telefono = models.IntegerField(verbose_name="telefono", blank=True, null=True)
    
    def __str__(self):
        if self.nombre and self.apellido:
            return '%s %s' % (self.nombre, self.apellido)
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse('perfil_cliente', args=[str(self.id)])