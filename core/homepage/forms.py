from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from core.user.models import User

# Formulario de Login


class AFWithEmail(AuthenticationForm):
    # Ahora el campo username es de tipo email y cambiamos su texto
    username = forms.Field(label="Nombre usuario")

    class Meta:
        model = User
        fields = ["username", "password"]

# Formulario de Registro


class UCFWithEmail(UserCreationForm):
    # Establecemos que el campo username es tipo email y el nombre
    username = forms.Field(label="Nombre usuario")

    class Meta:
        model = User
        fields = ["username", "password1", "password2",
                  "first_name", "last_name", "email", "telefono"]

