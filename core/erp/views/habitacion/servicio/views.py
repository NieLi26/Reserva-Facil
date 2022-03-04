from turtle import position
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.erp.forms import ServicioHabitacionForm
from core.erp.models import ServicioHabitacion


class ServicioHabitacionListView(ListView):
    model = ServicioHabitacion
    template_name = 'habitacion/servicio/list.html'

    @method_decorator(csrf_exempt)
    # @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "searchdata":
                data = []
                # position = 1
                for i in ServicioHabitacion.objects.all():
                    item = i.toJSON()
                    # item["position"] = position
                    # data.append(item)
                    # position += 1
                    data.append(i.toJSON())
            else:
                data["error"] = "Ha ocurrido un error"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Servicios"
        context['entity'] = "Servicios"
        context['icon'] = "fas fa-thumbs-up"
        context['create_url'] = reverse_lazy('erp:servicio_habitacion_create')
        context['list_url'] = reverse_lazy('erp:servicio_habitacion_list')
        return context


class ServicioHabitacionCreateView(CreateView):
    model = ServicioHabitacion
    form_class = ServicioHabitacionForm
    template_name = "habitacion/servicio/create.html"
    success_url = reverse_lazy('erp:servicio_habitacion_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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
        context['title'] = "Creacion de un Servicio"
        context['entity'] = "Servicios"
        context['icon'] = "fas fa-thumbs-up"
        context['list_url'] = reverse_lazy('erp:servicio_habitacion_list')
        context['action'] = "add"
        return context


class ServicioHabitacionUpdateView(UpdateView):
    model = ServicioHabitacion
    form_class = ServicioHabitacionForm
    template_name = "habitacion/servicio/create.html"
    success_url = reverse_lazy('erp:servicio_habitacion_list')

    @method_decorator(login_required)
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
        context['title'] = "Edicion de un Servicio"
        context['entity'] = "Servicios"
        context['icon'] = "fas fa-thumbs-up"
        context['list_url'] = reverse_lazy('erp:servicio_habitacion_list')
        context['action'] = "edit"
        return context


class ServicioHabitacionDeleteView(DeleteView):
    model = ServicioHabitacion
    template_name = "habitacion/servicio/delete.html"
    success_url = reverse_lazy('erp:servicio_habitacion_list')

    @method_decorator(login_required)
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
        context['title'] = "Eliminacion de un Servicio"
        context['entity'] = "Servicios"
        context['icon'] = "fas fa-thumbs-up"
        context['list_url'] = reverse_lazy('erp:servicio_habitacion_list')
        return context
