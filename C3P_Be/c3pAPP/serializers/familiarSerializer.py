from rest_framework import serializers
from c3pAPP.models.familiar import familiar
from c3pAPP.serializers.usuarioSerializer import usuarioSerializerDetail

class GETfamiliarSerializer(serializers.ModelSerializer):
    id_usuario = usuarioSerializerDetail()
    class Meta:
        model = familiar
        fields = ['id', 'id_usuario', 'parentesco']
        
class POSTfamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = familiar
        fields = ['id', 'id_usuario', 'parentesco']