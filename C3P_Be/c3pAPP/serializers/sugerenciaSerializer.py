from c3pAPP.models.sugerencia import sugerencia
from rest_framework import serializers
from c3pAPP.serializers.personal_saludSerializer import GETpersonal_saludSerializer
from c3pAPP.serializers.historial_signosSerializer import GEThistorial_signosSerializer

class GETsugerenciaSerializer(serializers.ModelSerializer):
    id_personal = GETpersonal_saludSerializer()
    id_historial_signos = GEThistorial_signosSerializer()
    class Meta:
        model = sugerencia
        fields = ['id', 'id_personal', 'id_historial_signos', 
                  'fecha_sugerencia', 'recomendacion_medica']

class POSTsugerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = sugerencia
        fields = ['id', 'id_personal', 'id_historial_signos', 
                  'fecha_sugerencia', 'recomendacion_medica']
        
