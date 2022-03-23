from django.contrib import admin
from core.erp.models import *

# Register your models here.

######## INTERFAZ ADMIN ########
admin.site.register(Reserva)
admin.site.register(TipoHabitacion)
admin.site.register(ServicioHabitacion)
admin.site.register(Habitacion)
admin.site.register(ImagenHabitacion)
admin.site.register(Piso)

