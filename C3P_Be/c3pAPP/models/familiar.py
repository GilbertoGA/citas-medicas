from django.db import models
from .usuario import User

class familiar(models.Model):
    id = models.AutoField(primary_key = True)
    id_usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    parentesco = models.CharField('Parentesco', max_length = 50)