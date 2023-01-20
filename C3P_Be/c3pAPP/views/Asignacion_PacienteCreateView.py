from rest_framework import views, status
from rest_framework.response import Response
from c3pAPP.serializers.asignacion_pacienteSerializer import POSTasignacion_pacienteSerializer


class Asignacion_PacienteCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = POSTasignacion_pacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
