from django.urls import path
from core.homepage.views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf.urls import url


urlpatterns = [
    # path('', index, name="index"),
    # path('register', register, name="register"),
    path('', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout),
    path('reset/password_reset', PasswordResetView.as_view(template_name='departamento/registration/password_reset_forms.html', email_template_name="departamento/registration/password_reset_email.html"), name = 'password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='departamento/registration/password_reset_done.html'), name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='departamento/registration/password_reset_confirms.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='departamento/registration/password_reset_complete.html') , name = 'password_reset_complete'),
    
]


