from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from core.homepage.models import Huesped
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

# Formulario de Modificación de Perfil

class profileModifyForm(forms.ModelForm):

    class Meta:
        model = Huesped
        fields = ["nombre","apellido","tipo_documento",
                "numero_documento", "email", "telefono"]
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class' : 'form-control'}),
            'apellido': forms.TextInput(attrs={'class' : 'form-control'}),
            'tipo_documento': forms.TextInput(attrs={'class' : 'form-control'}),
            'numero_documento': forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.TextInput(attrs={'class' : 'form-control'}),
            'telefono': forms.TextInput(attrs={'class' : 'form-control'}),

        }

    

