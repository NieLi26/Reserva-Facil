from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from core.erp.forms import PisoForm
from core.erp.models import Piso


class PisoListView(ListView):
    model = Piso
    template_name = 'habitacion/piso/list.html'

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
                for i in Piso.objects.all():
                    data.append(i.toJSON())
            else:
                data["error"] = "Ha ocurrido un error"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Pisos"
        context['entity'] = "Pisos"
        context['create_url'] = reverse_lazy('erp:piso_create')
        context['list_url'] = reverse_lazy('erp:piso_list')
        return context


class PisoCreateView(CreateView):
    model = Piso
    form_class = PisoForm
    template_name = "habitacion/piso/create.html"
    success_url = reverse_lazy('erp:piso_list')

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
        context['title'] = "Creacion de un piso"
        context['entity'] = "Pisos"
        context['list_url'] = reverse_lazy('erp:piso_list')
        context['action'] = "add"
        return context


class PisoUpdateView(UpdateView):
    model = Piso
    form_class = PisoForm
    template_name = "habitacion/piso/create.html"
    success_url = reverse_lazy('erp:room_floor_list')

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
        context['title'] = "Edicion de un Piso"
        context['entity'] = "Pisos"
        context['list_url'] = reverse_lazy('erp:piso_list')
        context['action'] = "edit"
        return context


class PisoDeleteView(DeleteView):
    model = Piso
    template_name = "habitacion/piso/delete.html"
    success_url = reverse_lazy('erp:room_floor_list')

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
        context['title'] = "Eliminacion de un Piso"
        context['entity'] = "Pisos"
        context['list_url'] = reverse_lazy('erp:piso_list')
        return context
