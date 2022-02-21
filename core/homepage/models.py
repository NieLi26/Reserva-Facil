from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users/%y/%m/%d", null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    def get_image(self):
        if self.image:
            return "{}{}".format(MEDIA_URL, self.image)
        return "{}{}".format(STATIC_URL, "img/empty.png")

    def toJSON(self):
        # no se puede convetir campos de imagen, fecha, relaciones,etc.
        # se puede ever lo que traen llamando al metodo para saber que excluir.
        item = model_to_dict(
            self, exclude=["user_permissions", "last_login"])
        if self.last_login:
            item['last_login'] = self.last_login.strftime("%Y-%m-%d")
        item['date_joined'] = self.date_joined.strftime("%Y-%m-%d")
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        # para traer todos los grupos del usuario e iterarlos, luego insertarlos en diccionario
        item['groups'] = [{"id": g.id, "name": g.name}
                          for g in self.groups.all()]
        return item
