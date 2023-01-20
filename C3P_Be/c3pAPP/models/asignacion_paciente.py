from django.db import models
from .paciente import paciente
from .familiar import familiar
from .personal_salud import personal_salud


class asignacion_paciente(models.Model):
    id = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(paciente, null=True, blank=True, on_delete=models.CASCADE)
    id_familiar = models.ForeignKey(familiar, null=True, blank=True, on_delete=models.CASCADE)
    id_personal = models.ForeignKey(personal_salud, null=True, blank=True, on_delete=models.CASCADE)
