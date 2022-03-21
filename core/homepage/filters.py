import django_filters as filters
from datetime import datetime
from django import forms
from core.erp.models import *

class FiltroHabitacion(filters.FilterSet):
    tipo_habitacion = filters.ModelChoiceFilter(queryset=TipoHabitacion.objects.all(),label='Tipo de Habitacion',empty_label="Todos",widget=forms.Select(attrs={'class': 'form-control'}))
    servicio_habitacion = filters.ModelChoiceFilter(queryset=ServicioHabitacion.objects.all(),label='Servicios',empty_label="Todos",widget=forms.Select(attrs={'class': 'form-control'}))
    #Tarifa exacta
    #tipo_habitacion__tarifa = filters.NumberFilter(label='Tarifa',widget=forms.NumberInput(attrs={'class': 'form-control'}))
    #Tarifa Mayor que
    #tipo_habitacion__tarifa__gt = filters.NumberFilter(field_name='tipo_habitacion__tarifa', lookup_expr='gt',label='Tarifa',widget=forms.NumberInput(attrs={'class': 'form-control'}))
    #Tarifa Menor que
    #tipo_habitacion__tarifa__lt = filters.NumberFilter(field_name='tipo_habitacion__tarifa', lookup_expr='lt',label='Tarifa',widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Habitacion
        fields = ['tipo_habitacion','servicio_habitacion']