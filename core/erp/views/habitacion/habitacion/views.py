from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.erp.forms import HabitacionForm
from core.erp.mixin import ValidatePermissionRequiredMixin
from core.erp.models import Habitacion


class HabitacionListView(ValidatePermissionRequiredMixin,ListView):
    permission_required = ("view_habitacion", "change_habitacion", "add_habitacion", "delete_habitacion")
    model = Habitacion
    template_name = 'habitacion/habitacion/list.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "searchdata":
                data = []
                for i in Habitacion.objects.all():
                    data.append(i.toJSON())
            else:
                data["error"] = "Ha ocurrido un error"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Habitaciones"
        context['entity'] = "Habitaciones"
        context['icon'] = "fas fa-bed"
        context['create_url'] = reverse_lazy('erp:habitacion_create')
        context['list_url'] = reverse_lazy('erp:habitacion_list')
        return context


class HabitacionCreateView(CreateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = "habitacion/habitacion/create.html"
    success_url = reverse_lazy('erp:habitacion_list')

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
        context['title'] = "Creacion de una Habitacion"
        context['entity'] = "Habitaciones"
        context['icon'] = "fas fa-bed"
        context['list_url'] = reverse_lazy('erp:habitacion_list')
        context['action'] = "add"
        return context


class HabitacionUpdateView(UpdateView):
    model = Habitacion
    form_class = HabitacionForm
    template_name = "habitacion/habitacion/create.html"
    success_url = reverse_lazy('erp:habitacion_list')

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
        context['title'] = "Edicion de una Habitacion"
        context['entity'] = "Habitaciones"
        context['icon'] = "fas fa-bed"
        context['list_url'] = reverse_lazy('erp:habitacion_list')
        context['action'] = "edit"
        return context


class HabitacionDeleteView(DeleteView):
    model = Habitacion
    template_name = "habitacion/habitacion/delete.html"
    success_url = reverse_lazy('erp:habitacion_list')

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
        context['title'] = "Eliminacion de una Habitacion"
        context['entity'] = "Habitaciones"
        context['icon'] = "fas fa-bed"
        context['list_url'] = reverse_lazy('erp:habitacion_list')
        return context
