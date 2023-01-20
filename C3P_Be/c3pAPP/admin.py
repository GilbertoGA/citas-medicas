from django.contrib import admin
from .models.usuario import User
from .models.rol import rol
from .models.personal_salud import personal_salud
from .models.paciente import paciente
from .models.familiar import familiar
from .models.asignacion_paciente import asignacion_paciente
from .models.signos_vitales import signos_vitales
from .models.historial_signos import historial_signos
from .models.sugerencia import sugerencia

# Register your models here.

admin.site.register(User)
admin.site.register(rol)
admin.site.register(personal_salud)
admin.site.register(paciente)
admin.site.register(familiar)
admin.site.register(asignacion_paciente)
admin.site.register(signos_vitales)
admin.site.register(historial_signos)
admin.site.register(sugerencia)
