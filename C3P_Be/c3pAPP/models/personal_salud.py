from django.db import models
from .usuario import User
from .rol import rol

class personal_salud (models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(rol, null=True, blank=True, on_delete=models.CASCADE)