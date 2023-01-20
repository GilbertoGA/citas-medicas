from rest_framework import serializers
from c3pAPP.models.personal_salud import personal_salud
from c3pAPP.serializers.usuarioSerializer import usuarioSerializerDetail
from c3pAPP.serializers.rolSerializer import rolSerializerDetail


class GETpersonal_saludSerializer(serializers.ModelSerializer):
    id_usuario = usuarioSerializerDetail()
    id_rol = rolSerializerDetail()
    class Meta:
        model = personal_salud
        fields = ['id', 'id_usuario', 'id_rol']
        
class POSTpersonal_saludSerializer(serializers.ModelSerializer):
    class Meta:
        model = personal_salud
        fields = ['id', 'id_usuario', 'id_rol']
