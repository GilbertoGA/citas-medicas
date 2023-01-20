from django.db import models
from .personal_salud import personal_salud
from .historial_signos import historial_signos

class sugerencia (models.Model):
    id = models.AutoField(primary_key=True)
    id_personal = models.ForeignKey(personal_salud, null=True, blank=True, on_delete=models.CASCADE)
    id_historial_signos = models.ForeignKey(historial_signos, null=True, blank=True, on_delete=models.CASCADE)
    fecha_sugerencia = models.DateTimeField(verbose_name='Fecha de la sugerencia')
    recomendacion_medica = models.CharField('Recomendacion medica', max_length=1000)