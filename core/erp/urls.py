from django.urls import path

from core.erp.views.dashboard.views import DashboardView

from core.erp.views.habitacion.habitacion.views import *
from core.erp.views.habitacion.piso.views import *
from core.erp.views.habitacion.servicio.views import *
from core.erp.views.habitacion.tipo.views import *

from core.erp.views.recepcion.views import *
from core.erp.views.pago.views import *

app_name = "erp"

urlpatterns = [
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    ########################## HABITACION ##############################
    # habitacion
    path('habitacion/list/', HabitacionListView.as_view(), name='habitacion_list'),
    path('habitacion/add/', HabitacionCreateView.as_view(), name='habitacion_create'),
    path('habitacion/update/<int:pk>/', HabitacionUpdateView.as_view(), name='habitacion_update'),
    path('habitacion/delete/<int:pk>/', HabitacionDeleteView.as_view(), name='habitacion_delete'),
    # piso
    path('habitacion/piso/list/', PisoListView.as_view(), name='piso_list'),
    path('habitacion/piso/add/', PisoCreateView.as_view(), name='piso_create'),
    path('habitacion/piso/update/<int:pk>/', PisoUpdateView.as_view(), name='piso_update'),
    path('habitacion/piso/delete/<int:pk>/', PisoDeleteView.as_view(), name='piso_delete'),
    # servicio habitacion
    path('habitacion/servicio/list/', ServicioHabitacionListView.as_view(), name='servicio_habitacion_list'),
    path('habitacion/servicio/add/', ServicioHabitacionCreateView.as_view(), name='servicio_habitacion_create'),
    path('habitacion/servicio/update/<int:pk>/', ServicioHabitacionUpdateView.as_view(), name='servicio_habitacion_update'),
    path('habitacion/servicio/delete/<int:pk>/', ServicioHabitacionDeleteView.as_view(), name='servicio_habitacion_delete'),
    # tipo habitacion
    path('habitacion/tipo/list/', TipoHabitacionListView.as_view(), name='tipo_habitacion_list'),
    path('habitacion/tipo/add/', TipoHabitacionCreateView.as_view(), name='tipo_habitacion_create'),
    path('habitacion/tipo/update/<int:pk>/', TipoHabitacionUpdateView.as_view(), name='tipo_habitacion_update'),
    path('habitacion/tipo/delete/<int:pk>/', TipoHabitacionDeleteView.as_view(), name='tipo_habitacion_delete'),
    ########################## RESERVAS ##############################
    # reception
    path('recepcion/', RecepcionView.as_view(), name='recepcion'),
    path('check_out/', CheckOutView.as_view(), name='check_out'),
    path('check_out/pago/<int:pk>/', PagoReservaCreateView.as_view(), name='pago_reserva'),
    path('reserva/info/<int:pk>/', InfoReservaView.as_view(), name='info_reserva'),
    path('recepcion/list/', ReservaListView.as_view(), name='recepcion_list'),
    path('recepcion/add/<int:pk>/', ReservaCreateView.as_view(), name='recepcion_create'),
    path('recepcion/update/<int:pk>/', ReservaUpdateView.as_view(), name='recepcion_update'),
    path('recepcion/delete/<int:pk>/', ReservaDeleteView.as_view(), name='recepcion_delete'),

    ########################## PAGO RESERVA ##############################
    # pago reserva
    path('reserva/pago/list/', PagoReservaListView.as_view(), name='pago_reserva_list'),
    # path('guest/add/', GuestCreateView.as_view(), name='guest_create'),
    path('reserva/pago/update/<int:pk>/', PagoReservaUpdateView.as_view(), name='pago_reserva_update'),
    path('reserva/pago/delete/<int:pk>/', PagoReservaDeleteView.as_view(), name='pago_reserva_delete'),
]

