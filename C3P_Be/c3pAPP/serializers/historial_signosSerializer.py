from c3pAPP.models.historial_signos import historial_signos
from rest_framework import serializers
from c3pAPP.serializers.pacienteSerializer import GETpacienteSerializer
from c3pAPP.serializers.familiarSerializer import GETfamiliarSerializer
from c3pAPP.serializers.signos_vitalesSerializer import signos_vitalesSerializerDetail

class GEThistorial_signosSerializer(serializers.ModelSerializer):
    id_paciente = GETpacienteSerializer()
    id_familiar = GETfamiliarSerializer()
    id_signos_vitales = signos_vitalesSerializerDetail()
    class Meta:
        model = historial_signos
        fields = ['id', 'id_paciente', 'id_familiar', 'id_signos_vitales',
                  'fecha_historial', 'observaciones']
        
class POSThistorial_signosSerializer(serializers.ModelSerializer):
    class Meta:
        model = historial_signos
        fields = ['id', 'id_paciente', 'id_familiar', 'id_signos_vitales',
                  'fecha_historial', 'observaciones']