from rest_framework import generics, status
from rest_framework.response import Response

from c3pAPP.serializers.historial_signosSerializer import GEThistorial_signosSerializer
from c3pAPP.models.historial_signos import historial_signos


# get asignacion by id_paciente
class Historial_SignosDetailView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        try:
            user = historial_signos.objects.get(id_paciente=kwargs["id_paciente"])
            serializer = GEThistorial_signosSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except historial_signos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)