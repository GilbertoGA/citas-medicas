from rest_framework import views, status
from rest_framework.response import Response

from c3pAPP.serializers.personal_saludSerializer import GETpersonal_saludSerializer
from c3pAPP.models.personal_salud import personal_salud

class Personal_SaludListView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = personal_salud.objects.all()
        serializer = GETpersonal_saludSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)