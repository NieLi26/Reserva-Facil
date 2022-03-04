from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView, RedirectView
from django.utils.decorators import method_decorator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from core.user.forms import UserForm, UserProfileForm
from core.user.models import User


class UserListView(ListView):
    model = User
    template_name = 'user/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "searchdata":
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data["error"] = "Ha ocurrido un error"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Usuarios"
        context['entity'] = "Usuarios"
        context['icon'] = "fas fa-user-friends"
        context['create_url'] = reverse_lazy('user:user_create')
        context['list_url'] = reverse_lazy('user:user_list')
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "user/create.html"
    success_url = reverse_lazy('user:user_list')

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
        context['title'] = "Creacion de un Usuario"
        context['entity'] = "Usuarios"
        context['icon'] = "fas fa-user-friends"
        context['list_url'] = self.success_url
        context['action'] = "add"
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "user/create.html"
    success_url = reverse_lazy('user:user_list')
    url_redirect = success_url

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
        context['title'] = "Edición de un Usuario"
        context['entity'] = "Usuarios"
        context['icon'] = "fas fa-user-friends"
        context['list_url'] = self.success_url
        context['action'] = "edit"
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = "user/delete.html"
    success_url = reverse_lazy('user:user_list')
    url_redirect = success_url

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
        context['title'] = "Eliminacion de un Usuario"
        context['entity'] = "Usuarios"
        context['icon'] = "fas fa-user-friends"
        context['list_url'] = self.success_url
        return context


class UserChangeGroup(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:dashboard'))


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "user/profile.html"
    success_url = reverse_lazy('erp:dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

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
        context['title'] = "Edición de un Perfil"
        context['entity'] = "Perfil"
        context['icon'] = "fas fa-user"
        context['list_url'] = self.success_url
        context['action'] = "edit"
        return context


class UserChangePasswordView(LoginRequiredMixin, FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = "user/change_password.html"
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        form.fields["old_password"].widget.attrs["placeholder"] = "Ingrese su contraseña actual"
        form.fields["new_password1"].widget.attrs["placeholder"] = "Ingrese su nueva contraseña"
        form.fields["new_password2"].widget.attrs["placeholder"] = "Repita su contraseña"
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST["action"]
            if action == "edit":
                form = PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                    # para que nose deslogee
                    update_session_auth_hash(request, form.user)
                else:
                    data['error'] = form.errors
            else:
                data["error"] = "No ha ingresado a ninguna opcion"
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edición de un Password"
        context['entity'] = "Password"
        context['icon'] = "fas fa-key"
        context['list_url'] = reverse_lazy("erp:dashboard")
        context['action'] = "edit"
        return context


class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
