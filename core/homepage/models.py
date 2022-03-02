from crum import get_current_request
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict
from core.homepage.choices import tipo_documento_choices

from config.settings import MEDIA_URL, STATIC_URL

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users/%y/%m/%d", null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    tipo_documento = models.CharField(
        max_length=25, choices=tipo_documento_choices, default="DNI", verbose_name="Tipo de Documento", blank=True, null=True)
    numero_documento = models.CharField(max_length=20, verbose_name="Numero de Documento", blank=True, null=True)

    def get_search_user(self):
        return "{} {} / {}".format(self.first_name, self.last_name, self.numero_documento)

    def get_image(self):
        if self.image:
            return "{}{}".format(MEDIA_URL, self.image)
        return "{}{}".format(STATIC_URL, "img/empty.png")

    def toJSON(self):
        item = model_to_dict(
            self, exclude=["user_permissions", "last_login"])
        if self.last_login:
            item['last_login'] = self.last_login.strftime("%Y-%m-%d")
        item['date_joined'] = self.date_joined.strftime("%Y-%m-%d")
        item['image'] = self.get_image()
        item['full_name'] = self.get_search_user()
        item['numero_documento'] = self.numero_documento
        item['groups'] = [{"id": g.id, "name": g.name}
                          for g in self.groups.all()]
        return item

    def get_group_session(self):
        try:
            request = get_current_request() 
            groups = self.groups.all()
            if groups.exists():
                if "group" not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass