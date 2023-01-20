from rest_framework import views, status
from rest_framework.response import Response

from c3pAPP.serializers.familiarSerializer import GETfamiliarSerializer
from c3pAPP.models.familiar import familiar

class FamiliarListView(views.APIView):
    def get(self, request, *args, **kwargs):
        queryset = familiar.objects.all()
        serializer = GETfamiliarSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)