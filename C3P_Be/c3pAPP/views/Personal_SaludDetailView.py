from rest_framework import status, generics
from rest_framework.response import Response
from c3pAPP.models.personal_salud import personal_salud
from c3pAPP.serializers.personal_saludSerializer import GETpersonal_saludSerializer


class Personal_SaludDetailView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        try:
            user = personal_salud.objects.get(id=kwargs['pk'])
            serializer = GETpersonal_saludSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except personal_salud.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
