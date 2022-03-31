from datetime import date, datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.db.models import Q

from core.erp.forms import ReservaForm
from core.erp.models import Reserva, Habitacion
from core.user.models import User


class CalendarioListView(ListView):
    model = Reserva
    template_name = "calendario/calendario.html"

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "searchdata":
                data = []
                for i in Reserva.objects.all():
                    data.append(i.toJSON())
            elif action == "search_guest":
                data = []
                term = request.POST['term']
                users = User.objects.filter(Q(first_name__icontains=term) | Q(
                    last_name__icontains=term) | Q(numero_documento__icontains=term))[0:10]
                for i in users:
                    item = i.toJSON()
                    item['text'] = i.get_search_user()
                    data.append(item)
            elif action == "create_reserva":
                frmReserva = ReservaForm(request.POST)
                data = frmReserva.save()
            elif action == 'complete':
                habitacion = request.POST
                data = Habitacion.objects.get(id=habitacion['id']).toJSON()
            else:
                data["error"] = "Ha ocurrido un error"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Calendario de Reserva"
        context['entity'] = "Calendario"
        # context['create_url'] = reverse_lazy('erp:reception_create')
        context['list_url'] = reverse_lazy('erp:calendario')
        context['frmReserva'] = ReservaForm()
        context['datetimenow'] = datetime.now().strftime("%Y-%m-%d")
        return context



def page_not_found404(request, exception):
    return render(request, '404.html')