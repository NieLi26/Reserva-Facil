from django.urls import reverse_lazy
from .forms import AFWithEmail, UCFWithEmail
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse, response
from django.contrib import messages
from core.erp.models import Configuration, Hospedaje
from django.core.paginator import Paginator
from django.http import Http404

from django.views.generic import RedirectView
from django.contrib.auth import login, logout
import config.settings as setting


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
                if user.is_superuser:
                  return redirect(setting.LOGIN_REDIRECT_URL)
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
    departamentos = Hospedaje.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(departamentos, 2)
        departamentos = paginator.page(page)
    except:
        raise response.Http404
    data = {
        'configuracion': configuracion,
        'entity': departamentos,
        'paginator': paginator,
    }
    return render(request, 'departamento/inicio.html', data)

# Vista página de nosotros.


def nosotros(request):
    configuracion = Configuration.objects.last()
    data = {
        'configuracion': configuracion,
    }
    return render(request, 'departamento/nosotros.html', data)
