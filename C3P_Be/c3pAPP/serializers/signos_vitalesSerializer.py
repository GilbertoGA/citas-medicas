from c3pAPP.models.signos_vitales import signos_vitales
from rest_framework import serializers

class signos_vitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = signos_vitales
        fields = ['id', 'presion_sistolica', 'presion_diastolica', 
                  'frecuencia_respiratoria', 'glicemia', 'oximetria', 'temperatura', 
                  'frecuencia_cardiaca']
        
class signos_vitalesSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = signos_vitales
        fields = ['presion_sistolica', 'presion_diastolica', 
                  'frecuencia_respiratoria', 'glicemia', 'oximetria', 'temperatura', 
                  'frecuencia_cardiaca']