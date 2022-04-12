from django.forms import *
from core.erp.models import *


######################### HABITACION ######################


class TipoHabitacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = "true"

    class Meta:
        model = TipoHabitacion
        fields = '__all__'
        exclude = ["user_update", "user_creation"]
        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "ingrese un nombre",
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data


class ServicioHabitacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = "true"

    class Meta:
        model = ServicioHabitacion
        fields = '__all__'
        exclude = ["user_update", "user_creation"]
        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "ingrese un nombre",
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data


class PisoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = "true"

    class Meta:
        model = Piso
        fields = '__all__'
        exclude = ["user_update", "user_creation"]
        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "ingrese numero de piso",
                }
            ),
            'activo': CheckboxInput(
                attrs={
                    'style': 'width: 5%'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data


class HabitacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tipo_habitacion"].widget.attrs["autofocus"] = "true"

    class Meta:
        model = Habitacion
        fields = '__all__'
        exclude = ["user_update", "user_creation"]
        widgets = {
            "servicio_habitacion": Select(attrs={
                "class": "form-control select2",
                "style": "width: 100%"
            }),
            "piso": Select(attrs={
                "class": "form-control select2",
                "style": "width: 100%"
            }),
            "tipo_habitacion": Select(attrs={
                "class": "form-control select2",
                "style": "width: 100%"
            }),
            "numero_habitacion": TextInput(
                attrs={
                    "placeholder": "ingrese un numero de habitación",
                }
            ),
            "desc": Textarea(
                attrs={
                    "placeholder": "ingrese una descripción",
                    "rows": 3,
                    "cols": 3,
                }
            ),
            'activo': CheckboxInput(
                attrs={
                    'style': 'width: 5%'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data

######################### RESERVA ######################


class ReservaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields["avance"].widget.attrs = {
            "class": "form-control",
        }

    class Meta:
        model = Reserva
        fields = '__all__'
        exclude = ["user_update", "user_creation"]
        widgets = {
            "user": Select(attrs={
                "class": "form-select select2",
            }),
            "estado_reserva": Select(attrs={
                "class": "form-control",
                "style": "width: 100%"
            }),
            "check_in": DateInput(
                format="%Y-%m-%d",
                attrs={
                    # "value": datetime.now().strftime("%y-%m-%d")
                    "autocomplete": "off",
                    "class": "form-control datetimepicker-input",
                    "id": "check_in",
                    "data-target": "#check_in",
                    "data-toggle": "datetimepicker"
                }
            ),
            "check_out": DateInput(
                format="%Y-%m-%d",
                attrs={
                    # "value": datetime.now().strftime("%y-%m-%d")
                    "autocomplete": "off",
                    "class": "form-control datetimepicker-input",
                    "id": "check_out",
                    "data-target": "#check_out",
                    "data-toggle": "datetimepicker"
                }
            ),
            "iva": TextInput(),
            # "advance": TextInput(attrs={
            #     "class": "form-control",
            # }),
            "subtotal": TextInput(attrs={
                "readonly": True,
                # "disabled": True,
                "class": "form-control",
            }),
            "total": TextInput(attrs={
                "readonly": True,
                # "disabled": True,
                "class": "form-control",
            }),
            "obs": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ingrese su observación",
                "rows": 3,
                "cols": 3
            })
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save() # me devuelve la instancia del objeto creado( el que se guardo)
                habitacion = Habitacion.objects.filter(id=instance.habitacion_id)
                if instance.estado_reserva == "alojamiento terminado":
                    habitacion.update(estado_habitacion="limpieza")
                else:
                    habitacion.update(estado_habitacion="ocupada")
                
                if not PagoReserva.objects.filter(reserva=instance.id):
                    pago = PagoReserva()
                    pago.reserva  = instance
                    pago.avance = instance.avance
                    pago.total = instance.total + pago.avance
                    pago.resto =  pago.total - pago.avance
                    pago.save()         
            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data

######################### PAGO RESERVA ######################


class PagoReservaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["avance"].widget.attrs = {
            "readonly": True,
            "class": "form-control",
        }

        self.fields["reserva"].widget.attrs = {
            # "style": "visibility:hidden"
            "style": "display:none"

        }


    class Meta:
        model = PagoReserva
        fields = '__all__'
        exclude = ["user_update", "user_creation"]
        widgets = {
            "resto": TextInput(attrs={
                "readonly": True,
                # "disabled": True,
                "class": "form-control",
            }),
            "total": TextInput(attrs={
                "readonly": True,
                # "disabled": True,
                "class": "form-control",
            }),

            "obs": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Ingrese su observación",
                "rows": 3,
                "cols": 3
            }),
            'paid_out': CheckboxInput(
                attrs={
                    'style': 'width: 5%'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                pago = PagoReserva.objects.filter(id=instance.id)
                pago.update(paid_out = True)
                # cambiar estado de reserva
                reserva = Reserva.objects.get(id=instance.reserva.id)
                reserva.estado_reserva = "alojamiento terminado"
                reserva.save()
                #cambiar estado de habitacion
                habitacion = Habitacion.objects.filter(id=reserva.habitacion.id)
                if reserva.estado_reserva == "alojamiento terminado":
                    habitacion.update(estado_habitacion="limpieza")


            else:
                data["error"] = form.errors
        except Exception as e:
            data["error"] = str(e)
        return data
