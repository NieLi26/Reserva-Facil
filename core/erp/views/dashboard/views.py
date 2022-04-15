from datetime import datetime
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from core.erp.models import Reserva, PagoReserva

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    # def get(self, request, *args, **kwargs):
    #     request.user.get_group_session()
    #     return super().get(request, *args, **kwargs)

    def get_reservas_mensual(self):
        data = []
        try:
            uno = Reserva.objects.filter(estado_reserva='alojamiento terminado').count()
            dos = Reserva.objects.filter(estado_reserva='cancelada').count()
            tres = Reserva.objects.filter(estado_reserva='no ingreso').count()
            cuatro = Reserva.objects.filter(estado_reserva='confirmada').count()
            cinco = Reserva.objects.filter(estado_reserva='sin confirmar').count()
            data.append({'name': 'alojamiento terminado', 'y': uno, 'color': 'green'})
            data.append({'name': 'cancelada', 'y': dos, 'color': 'dark'})
            data.append({'name': 'no ingreso', 'y': tres, 'color': 'blue'})
            data.append({'name': 'confirmada', 'y': cuatro, 'color': 'red'})
            data.append({'name': 'sin confirmar', 'y': cinco, 'color': 'yellow'})
        except:
        # except Exception as e:
            pass
        # print(data)
        return data


    def get_pagos_mensual(self):
        data = []
        m = datetime.now().month
        # cancelado = PagoReserva.objects.filter(estado_pago='cancelado', fecha_creacion__month = m).count()
        # nocancelado = PagoReserva.objects.filter(estado_pago='sin cancelar', fecha_creacion__month = m).count()
        valor1 = 0
        valor2 = 0
        cancelado = PagoReserva.objects.filter(estado_pago='cancelado', fecha_creacion__month = m)
        for can in cancelado:
            valor1 += can.total
        nocancelado = PagoReserva.objects.filter(estado_pago='sin cancelar', fecha_creacion__month = m)
        for nocan in nocancelado:
            valor2 += nocan.total
        print(valor1)
        print(valor2)
        data.append({ 'name': 'Cancelado', 'y': valor1, 'color': '#00CB03' })
        data.append({ 'name': 'Sin cancelar', 'y': valor2, 'color': '#F00505' })
        return data


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = "Panel de adminstrador"
        context['entity'] = "Dashboard"
        context['icon'] = "fas fa-chart-line"
        context['reservas'] = self.get_reservas_mensual()
        context['pagos'] = self.get_pagos_mensual()
        return context
