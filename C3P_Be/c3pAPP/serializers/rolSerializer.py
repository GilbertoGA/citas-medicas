from rest_framework import serializers
from c3pAPP.models.rol import rol


class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = ['id', 'nombre']


class rolSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = ['nombre']
