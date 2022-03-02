from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from django.db import transaction
from django.db.models import Q

from core.erp.mixin import ValidatePermissionRequiredMixin
from core.erp.models import Reserva, Habitacion, PagoReserva
from core.erp.forms import ReservaForm, PagoReservaForm
from core.homepage.forms import UserForm, UserReservaForm
from core.homepage.models import User


class RecepcionView(LoginRequiredMixin, TemplateView):
    template_name = 'recepcion/recepcion.html'

    def get_habitaciones(self):
        data = []
        try:
            for i in Habitacion.objects.all().order_by("numero_habitacion"):
                data.append(i)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Panel de Recepcion"
        context['entity'] = "Recepcion"
        context['habitaciones'] = self.get_habitaciones()
        return context


class CheckOutView(LoginRequiredMixin, TemplateView):
    template_name = 'recepcion/check_out.html'

    def get_reservas(self):
        data = []
        try:
            for i in Reserva.objects.all().order_by("habitacion"):
                data.append(i)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Panel de Salida"
        context['entity'] = "Salida"
        context['reservas'] = self.get_reservas()
        return context

##pendiente
class PagoReservaCreateView(CreateView):
    model = PagoReserva
    form_class = PagoReservaForm
    template_name = "recepcion/pago.html"
    success_url = reverse_lazy('erp:check_out')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == 'add':
                form = self.get_form()
                data = form.save()

            elif action == 'complete':
                data = Reserva.objects.get(id=self.kwargs['pk']).toJSON()
            else:
                data["error"] = "No ha ingresado a ninguna opcion"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registro pago de Reserva"
        context['entity'] = "Pago de Reservas"
        context['list_url'] = self.success_url
        context['action'] = "add"
        context['reserva'] = Reserva.objects.get(id=self.kwargs['pk'])
        return context


class InfoReservaView(LoginRequiredMixin, TemplateView):
    template_name = 'recepcion/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Panel de informacion Reserva"
        context['entity'] = "Informacion"
        context['reserva'] = Reserva.objects.get(habitacion_id=self.kwargs['pk'])
        context['list_url'] = reverse_lazy('erp:recepcion')
        return context


class ReservaListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Reserva
    template_name = "recepcion/list.html"

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
                for i in Reserva.objects.all():
                    data.append(i.toJSON())
            else:
                data["error"] = "Ha ocurrido un error"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Reservas"
        context['entity'] = "Reservas"
        context['list_url'] = reverse_lazy('erp:recepcion_list')
        context['form'] = ReservaForm()
        return context


class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = "recepcion/create.html"
    success_url = reverse_lazy('erp:recepcion')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == 'add':
                form = self.get_form()
                data = form.save()
            elif action == "search_user":
                data = []
                term = request.POST['term']
                users = User.objects.filter(Q(first_name__icontains=term) | Q(
                    last_name__icontains=term) | Q(numero_documento__icontains=term))[0:10]
                for i in users:
                    item = i.toJSON()
                    item['text'] = i.get_search_user()
                    data.append(item)
            elif action == "create_user":
                with transaction.atomic():
                    print(request.POST)
                    frmUser = UserReservaForm(request.POST)
                    data = frmUser.save()
                    # insertamos los datos del formulario que enviamos en una varianble
                    # frmGuest = request.POST
                    # guest = Guest()  # creamos un objecto(instancia) del modelo Guest
                    # guest.doc_type = frmGuest['doc_type']
                    # guest.doc_number = frmGuest['doc_number']
                    # guest.firstname = frmGuest['firstname']
                    # guest.lastname = frmGuest['lastname']
                    # guest.cell = frmGuest['cell']
                    # guest.mail = frmGuest['mail']
                    # if frmGuest.get('active'):
                    #     guest.active = True
                    print(data)
            elif action == 'complete':
                data = Habitacion.objects.get(id=self.kwargs['pk']).toJSON()
            else:
                data["error"] = "No ha ingresado a ninguna opcion"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registro de Reserva"
        context['entity'] = "Reservas"
        context['list_url'] = reverse_lazy('erp:recepcion')
        context['action'] = "add"
        context['habitacion'] = Habitacion.objects.get(id=self.kwargs['pk'])
        context['frmUser'] = UserReservaForm()
        return context


class ReservaUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = "recepcion/create.html"
    success_url = reverse_lazy('erp:recepcion_list')

    @method_decorator(csrf_exempt)
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
            elif action == "search_user":
                data = []
                term = request.POST['term']
                users = User.objects.filter(Q(first_name__icontains=term) | Q(
                    last_name__icontains=term) | Q(numero_documento__icontains=term))[0:10]
                for i in users:
                    item = i.toJSON()
                    item['text'] = i.get_search_user()
                    data.append(item)
            elif action == "create_user":
                with transaction.atomic():  
                    frmUser = UserReservaForm(request.POST)
                    data = frmUser.save()  
            elif action == 'complete':
                data = Habitacion.objects.get(id=self.object.habitacion.id).toJSON()
            else:
                data["error"] = "No ha ingresado a ninguna opcion"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de una Reserva"
        context['entity'] = "Reservas"
        context['list_url'] = self.success_url
        context['action'] = "edit"
        context['habitacion'] = Habitacion.objects.get(id=self.object.habitacion.id)
        context['frmUser'] = UserReservaForm()
        return context


class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = "recepcion/delete.html"
    success_url = reverse_lazy('erp:recepcion_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
            habitacion = Habitacion.objects.filter(id=self.object.habitacion_id)
            habitacion.update(estado_habitacion="disponible")
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminacion de una Reserva"
        context['entity'] = "Reservas"
        context['list_url'] = reverse_lazy('erp:recepcion_list')
        return context
