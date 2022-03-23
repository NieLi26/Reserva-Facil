from datetime import datetime
from crum import get_current_user
from django.db import models

from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from django.contrib.auth import get_user_model
from core.erp.choices import *

from core.models import BaseModel

User = get_user_model()

# Create your models here.

########################################################################## INTERFAZ ADMIN #############################################################################


# ---------------------- CLIENTE ------------------------

class Cliente(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    rut = models.CharField(max_length=10, verbose_name="Rut")
    direccion = models.CharField(
        max_length=150, verbose_name='Dirección')
    telefono = models.CharField(max_length=9, verbose_name="Telefono")
    mail = models.EmailField(max_length=30, verbose_name="Correo")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class TipoPlan(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    valor_mensual = models.IntegerField(
        default=0, verbose_name="Valor mensual", blank=True, null=True)
    desc = models.TextField(max_length=100, verbose_name="Descripcion")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Tipo de plan'
        verbose_name_plural = 'Tipos de plan'
        ordering = ['id']


class Plan(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    tipo_plan = models.ForeignKey(
        TipoPlan, on_delete=models.CASCADE, verbose_name="Tipo de Plan")
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    meses_contratados = models.IntegerField(
        default=0, verbose_name="Meses Contratados")
    fecha_inicio = models.DateField(
        default=datetime.now, verbose_name="Fecha de inicio")
    valor = models.IntegerField(
        default=0, verbose_name="Valor", blank=True, null=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
        ordering = ['id']

# ---------------------- DIRECCION ------------------------


class Region(BaseModel):
    nombre = models.CharField(
        max_length=150, verbose_name="Nombre", unique=True)

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_update = user
        super(Region, self).save()

    def toJSON(self):
        # item = model_to_dict(self, exclude=["algo"])
        item = model_to_dict(self)
        return item

    # def toJSON(self):
    #     item = {"id": self.id, "name": self.name}
    #     return item

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
        # db_table = "region"
        ordering = ["id"]


class Comuna(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, verbose_name="Region")
    nombre = models.CharField(max_length=150, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Comuna"
        verbose_name_plural = "Comunas"
        ordering = ["id"]

#---------------------- HABITACIONES( interfaz gestor ) -------------------------#


class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tarifa = models.IntegerField(default=0, verbose_name="Tarifa")
    imagen = models.ImageField(upload_to='habitaciones/%Y/%m/%d',blank=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['nombre'] = self.nombre
        item['tarifa'] = self.tarifa
        item["imagen"] = self.get_image()
        return item

    def get_image(self):
        if self.imagen:
            return "{}{}".format(MEDIA_URL, self.imagen)
        return "{}{}".format(STATIC_URL, "img/empty.png")
    class Meta:
        verbose_name = "Tipo de Habitacion"
        verbose_name_plural = "Tipos de Habitaciones"
        ordering = ["id"]


class ServicioHabitacion(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Servicio de Habitacion"
        verbose_name_plural = "Servicios de Habitaciones"
        ordering = ["id"]


class Piso(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    activo = models.BooleanField(default=False, verbose_name="Activo")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Piso"
        verbose_name_plural = "Pisos"
        ordering = ["id"]


class Habitacion(models.Model):
    estado_habitacion = models.CharField(
        max_length=15, choices=estado_habitacion_choices, default="disponible", verbose_name="Estado Habitacion")
    servicio_habitacion = models.ForeignKey(
        ServicioHabitacion, on_delete=models.CASCADE, verbose_name="Servicio de Habitacion")
    tipo_habitacion = models.ForeignKey(
        TipoHabitacion, on_delete=models.CASCADE, verbose_name="Tipo de Habitacion")
    piso = models.ForeignKey(
        Piso, on_delete=models.CASCADE, verbose_name="Piso")
    numero_habitacion = models.CharField(
        max_length=3, verbose_name="Numero de Habitacion")
    capacidad = models.IntegerField(default=0, verbose_name="Capacidad")
    desc = models.TextField(verbose_name="Descripcion")
    activo = models.BooleanField(default=False, verbose_name="Activo")


    def __str__(self):
        return self.numero_habitacion

    def toJSON(self):
        item = model_to_dict(self)
        item["servicio_habitacion"] = self.servicio_habitacion.toJSON()
        item["tipo_habitacion"] = self.tipo_habitacion.toJSON()
        item["piso"] = self.piso.toJSON()
        # item["book"] = [i.toJSON() for i in self.booking_set.all()]
        return item
    
    class Meta:
        verbose_name = "Habitacion"
        verbose_name_plural = "Habitaciones"
        ordering = ["id"]


class Calification(models.Model):
    habitacion = models.ForeignKey(
        Habitacion, on_delete=models.CASCADE, verbose_name="Habitacion")
    nota = models.IntegerField(default=0, verbose_name="Nota")

    def __str__(self):
        pass

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Calificacion"
        verbose_name_plural = "Calificaciones"
        ordering = ["id"]


class ImagenHabitacion(models.Model):
    imagen = models.ImageField(upload_to='habitaciones/%Y/%m/%d')
    tipo_habitacion = models.ForeignKey(
        TipoHabitacion, on_delete=models.CASCADE, verbose_name=" Tipo de Habitacion")

    # def __str__(self):
    #    pass

    def toJSON(self):
        item = model_to_dict(self)
        # item['tipo_habitacion'] = self.tipo_habitacion.toJSON()
        return item

    def get_image(self):
        if self.imagen:
            return "{}{}".format(MEDIA_URL, self.imagen)
        return "{}{}".format(STATIC_URL, "img/empty.png")

    class Meta:
        verbose_name = "Imagen de Habitacion"
        verbose_name_plural = "Imagenes de Habitaciones"
        ordering = ["id"]


#---------------------- SUCURSAL -------------------------#


class TipoHospedaje(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    desc = models.TextField(verbose_name="Descripcion", null=True, blank=True)

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Categoria de Sucursal"
        verbose_name_plural = "Categorias de sucursal"
        ordering = ["id"]


class Hospedaje(models.Model):
    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE, verbose_name="Plan")
    tipo_hospedaje = models.ForeignKey(
        TipoHospedaje, on_delete=models.CASCADE, verbose_name="Tipo de hospedaje")
    comuna = models.ForeignKey(
        Comuna, on_delete=models.CASCADE, verbose_name="Comuna")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    direccion = models.CharField(max_length=50, verbose_name="Direccion")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Hospedaje"
        verbose_name_plural = "Hospedajes"
        ordering = ["id"]


class Gestor(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuario")
    hospedaje = models.ForeignKey(
        Hospedaje, on_delete=models.CASCADE, verbose_name="Hospedaje")
    imagen = models.ImageField(
        upload_to='gestores/%Y/%m/%d', null=True, blank=True)
    telefono = models.CharField(max_length=9, verbose_name="Telefono")
    direccion = models.CharField(max_length=50, verbose_name="Direccion")

    def __str__(self):
        return self.user.username

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def get_image(self):
        if self.imagen:
            return "{}{}".format(MEDIA_URL, self.imagen)
        return "{}{}".format(STATIC_URL, "img/empty.png")

    class Meta:
        verbose_name = "Gestor"
        verbose_name_plural = "Gestores"
        ordering = ["id"]

########################################################################## INTERFAZ GESTOR #############################################################################


class Configuration(models.Model):
    titulo = models.CharField(max_length=25, null=True)
    color1 = models.CharField(max_length=20)
    color2 = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="logotipos")

    def __str__(self):
        return f"Configuracion - {self.titulo}"

#---------------------- RESERVA -------------------------#


class Impuesto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    porcentaje = models.IntegerField(default=0, verbose_name="Porcentaje")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Porcentaje"
        verbose_name_plural = "Porcentajes"
        ordering = ["id"]


class Reserva(models.Model):    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Huesped")
    habitacion = models.ForeignKey(
        Habitacion, on_delete=models.CASCADE, verbose_name="Habitacion", null=True, blank=True)
    estado_reserva = models.CharField(
        max_length=25, choices=estado_reserva_choices, default="sin confirmar", verbose_name="Estado de Reserva")
    subtotal = models.IntegerField(
        default=0, verbose_name="Subtotal")
    total = models.IntegerField(
        default=0, verbose_name="Total a pagar")
    iva = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2, verbose_name="IVA")
    avance = models.IntegerField(
        default=0, verbose_name="Adelanto", blank=True, null=True)
    check_in = models.DateField(
        default=datetime.now, verbose_name="Fecha de Entrada")
    check_out = models.DateField(
        default=datetime.now, verbose_name="Fecha de Salida")
    obs = models.TextField(verbose_name="Observacion", null=True, blank=True)

    def __str__(self):
        return self.user.get_search_user()

    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.toJSON()
        item['habitacion'] = self.habitacion.toJSON()
        item['iva'] = format(self.iva, '.2f')
        item['check_in'] = self.check_in.strftime('%Y-%m-%d')
        item['check_out'] = self.check_out.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["id"]


class DetalleReserva(models.Model):
    reserva = models.ForeignKey(
        Reserva, on_delete=models.CASCADE, verbose_name="Reserva")
    numero_adultos = models.IntegerField(
        default=0, verbose_name="Numero de Adultos", blank=True)
    numero_niños = models.IntegerField(
        default=0, verbose_name="Numero de Niños", blank=True)
    numero_mascotas = models.IntegerField(
        default=0, verbose_name="Numero de Mascotas", blank=True)
    desc = models.TextField(verbose_name="Descripcion")

    # def __str__(self):
    #     pass

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Detalle de reserva"
        verbose_name_plural = "Detalle de reservas"
        ordering = ["id"]


#---------------------- SERVICIO EXTRA -------------------------#

class ServicioExtra(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    desc = models.TextField(verbose_name="Descripcion")
    tarifa = models.FloatField(default=0, verbose_name="Tarifa")
    activo = models.BooleanField(default=False, verbose_name="Activo")

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Servicio extra "
        verbose_name_plural = "Servicios extras"
        ordering = ["id"]


class ReservaServicioExtra(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Huesped")
    servicio_extra = models.ForeignKey(
        ServicioExtra, on_delete=models.CASCADE, verbose_name="Servicio Extra")
    fecha_realizacion = models.DateField(
        default=datetime.now, verbose_name="Fecha de Realizacion")

    def __str__(self):
        pass

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = "Reserva de servicio extra"
        verbose_name_plural = "Reserva de servicios extras"
        ordering = ["id"]

#---------------------- PAGOS -------------------------#


class PagoReserva(models.Model):
    reserva = models.ForeignKey(
        Reserva, on_delete=models.CASCADE, verbose_name="Reserva")
    avance = models.IntegerField(default=0, verbose_name="Adelanto")
    total = models.IntegerField(default=0, verbose_name="Valor total")
    resto = models.IntegerField(default=0, verbose_name="Restante")
    obs = models.TextField(max_length=200, verbose_name="Observacion", blank=True, null=True)
    paid_out = models.BooleanField(default=True, verbose_name="Pagado")

    def __str__(self):
        return self.reserva

    def toJSON(self):
        item = model_to_dict(self)
        item['reserva'] = self.reserva.toJSON()
        return item

    class Meta:
        verbose_name = "Pago Reserva"
        verbose_name_plural = "Pagos Reserva"
        ordering = ["id"]
