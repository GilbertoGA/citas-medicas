from django.db import models
from .paciente import paciente
from .familiar import familiar
from .signos_vitales import signos_vitales

class historial_signos (models.Model):
    id = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(paciente, null=True, blank=True, on_delete=models.CASCADE)
    id_familiar = models.ForeignKey(familiar, null=True, blank=True, on_delete=models.CASCADE)
    id_signos_vitales = models.ForeignKey(signos_vitales, null=True, blank=True, on_delete=models.CASCADE)
    fecha_historial = models.DateTimeField(verbose_name='Fecha Historial')
    observaciones = models.CharField('Observaciones', max_length=500)