from django.db import models

class signos_vitales (models.Model):
    id = models.AutoField(primary_key=True)
    presion_sistolica = models.IntegerField(default=0)
    presion_diastolica = models.IntegerField(default=0)
    frecuencia_respiratoria = models.IntegerField(default=0)
    glicemia = models.FloatField(default=0)
    oximetria = models.FloatField(default=0)
    temperatura = models.FloatField(default=0)
    frecuencia_cardiaca = models.IntegerField(default=0)