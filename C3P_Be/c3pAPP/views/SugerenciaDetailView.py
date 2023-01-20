from rest_framework import generics, status
from rest_framework.response import Response

from c3pAPP.serializers.sugerenciaSerializer import GETsugerenciaSerializer
from c3pAPP.models.sugerencia import sugerencia


# get asignacion by id_paciente
class SugerenciaDetailView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        try:
            user = sugerencia.objects.get(id_historial_signos=kwargs["id_historial_signos"])
            serializer = GETsugerenciaSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except sugerencia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)