from django.urls import path
from core.homepage.views import *


urlpatterns = [
    # path('', index, name="index"),
    # path('register', register, name="register"),
    path('', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout),
]


