from rest_framework import views, status
from rest_framework.response import Response

from c3pAPP.serializers.pacienteSerializer import GETpacienteSerializer
from c3pAPP.models.paciente import paciente

class PacienteListView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = paciente.objects.all()
        serializer = GETpacienteSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)