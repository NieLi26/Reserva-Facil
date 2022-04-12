from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class DashboardTemplateView(TemplateView):
    template_name = 'crm/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['test'] = 'k pazaaaaaa'
        return context