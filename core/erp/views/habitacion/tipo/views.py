from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.erp.forms import TipoHabitacionForm
from core.erp.models import TipoHabitacion


class TipoHabitacionListView(ListView):
    model = TipoHabitacion
    template_name = 'habitacion/tipo/list.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "searchdata":
                data = []
                for i in TipoHabitacion.objects.all():
                    data.append(i.toJSON())
            else:
                data["error"] = "Ha ocurrido un error"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Tipos Habitacion"
        context['entity'] = "Tipos de Habitacion"
        context['icon'] = "fas fa-procedures"
        context['create_url'] = reverse_lazy('erp:tipo_habitacion_create')
        context['list_url'] = reverse_lazy('erp:tipo_habitacion_list')
        return context


class TipoHabitacionCreateView(CreateView):
    model = TipoHabitacion
    form_class = TipoHabitacionForm
    template_name = "habitacion/tipo/create.html"
    success_url = reverse_lazy('erp:tipo_habitacion_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "add":
                form = self.get_form()
                data = form.save()
            else:
                data["error"] = "No ha ingresado a ninguna opcion"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Creacion de tipo Habitacion"
        context['entity'] = "Tipos de Habitacion"
        context['icon'] = "fas fa-procedures"
        context['list_url'] = reverse_lazy('erp:tipo_habitacion_list')
        context['action'] = "add"
        return context


class TipoHabitacionUpdateView(UpdateView):
    model = TipoHabitacion
    form_class = TipoHabitacionForm
    template_name = "habitacion/tipo/create.html"
    success_url = reverse_lazy('erp:tipo_habitacion_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "edit":
                form = self.get_form()
                data = form.save()
            else:
                data["error"] = "No ha ingresado a ninguna opcion"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de tipo Habitacion"
        context['entity'] = "Tipos de Habitacion"
        context['icon'] = "fas fa-procedures"
        context['list_url'] = reverse_lazy('erp:tipo_habitacion_list')
        context['action'] = "edit"
        return context


class TipoHabitacionDeleteView(DeleteView):
    model = TipoHabitacion
    template_name = "habitacion/tipo/delete.html"
    success_url = reverse_lazy('erp:tipo_habitacion_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminacion de tipo Habitacion"
        context['entity'] = "Tipos de Habitacion"
        context['icon'] = "fas fa-procedures"
        context['list_url'] = reverse_lazy('erp:tipo_habitacion_list')
        return context
