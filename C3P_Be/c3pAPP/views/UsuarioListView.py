from rest_framework import views, status
from rest_framework.response import Response

from c3pAPP.serializers.usuarioSerializer import usuarioSerializer
from c3pAPP.models.usuario import User

class UsuarioListView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = usuarioSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)