from django.urls import path
from .views import *

app_name = 'crm'

urlpatterns = [
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard')
]