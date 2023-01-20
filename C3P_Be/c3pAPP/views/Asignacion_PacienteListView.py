from rest_framework import views, status
from rest_framework.response import Response

from c3pAPP.serializers.asignacion_pacienteSerializer import GETasignacion_pacienteSerializer
from c3pAPP.models.asignacion_paciente import asignacion_paciente

class Asignacion_PacienteListView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = asignacion_paciente.objects.all()
        serializer = GETasignacion_pacienteSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)