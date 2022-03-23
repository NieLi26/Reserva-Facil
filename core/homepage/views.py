from django.urls import reverse_lazy
from .forms import AFWithEmail, UCFWithEmail
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse, response
from django.contrib import messages
from core.erp.models import Configuration, Habitacion,ImagenHabitacion,Reserva
from django.core.paginator import Paginator
from django.http import Http404

import config.settings as setting

from .filters import *
from django.db.models import Q
from datetime import datetime

# Vista principal y login.


def login(request):
  # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe el usuario
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                for group in request.user.groups.all():
                    if  user.is_superuser or group.name == "Gestor":
                        return redirect('erp:dashboard')
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')

        else:
            messages.error(request, 'Los datos no son válidos')

    # Si llegamos al final renderizamos el formulario
    return render(request, 'departamento/login.html', {'form': form})

# Vista registro de usuarios.


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UCFWithEmail()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UCFWithEmail(data=request.POST)

        # Si el formulario es válido...
        if form.is_valid():


            # Creamos la nueva cuenta de usuario
            user = form.save()
            messages.success(
                request, f'Bienvenid@ {user.username}, ya eres parte de Reserva Fácil')

            # Si existe el usuario
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('inicio')
        else:
          messages.error(request, 'Usuario ya existente')

    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None

    # Si llegamos al final renderizamos el formulario
    return render(request, "departamento/registro.html", {'form': form})

#Cierre de sesión para los usuarios.


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


# class LogoutRedirectView(RedirectView):
#     pattern_name = 'inicio'

#     def dispatch(self, request, *args, **kwargs):
#         logout(self.request)
#         return super().dispatch(request, *args, **kwargs)


# Vista página de inicio.


def inicio(request):
    configuracion = Configuration.objects.last()
    filtro = FiltroHabitacion(request.GET,queryset=Habitacion.objects.filter(activo=True).order_by('numero_habitacion'))
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(filtro.qs, 6)
        qs = paginator.get_page(page) 
    except:
        raise response.Http404
    #Elementos Filtro Fecha
    reservas = Reserva.objects.filter(check_in__gte=datetime.now()).order_by('habitacion__numero_habitacion')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')
    if  valid_param(checkin):
        if valid_param(checkout):
            if(checkout >= checkin):
                reservas = reservas.filter(Q(check_in__lte=checkin) & Q(check_out__gt=checkin) | 
                Q(check_in__lt=checkout) & Q(check_out__gte=checkout) | 
                Q(check_in__gt=checkin) & Q(check_out__lt=checkout))
            else:
                reservas = reservas.filter(Q(check_in__lte=checkin) & Q(check_out__gt=checkin))
        else:
            reservas = reservas.filter(Q(check_in__lte=checkin) & Q(check_out__gt=checkin))
    else:
        reservas=reservas.none()

    data = {
        'configuracion': configuracion,
        'filtro': filtro,
        'entity': qs,
        'paginator': paginator,
        'reservas': reservas,
        'checkin':checkin,
    }
    return render(request, 'departamento/inicio.html', data)

# Vista página de nosotros.


def nosotros(request):
    configuracion = Configuration.objects.last()
    data = {
        'configuracion': configuracion,
    }
    return render(request, 'departamento/nosotros.html', data)

def valid_param(param):
    return param != '' and param is not None

