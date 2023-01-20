from rest_framework import generics, status
from rest_framework.response import Response

from c3pAPP.serializers.pacienteSerializer import GETpacienteSerializer
from c3pAPP.models.paciente import paciente


class PacienteDetailView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        try:
            user = paciente.objects.get(id=kwargs['pk'])
            serializer = GETpacienteSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except paciente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
