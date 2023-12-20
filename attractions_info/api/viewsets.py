from rest_framework.viewsets import ModelViewSet
from attractions_info.models import AttractionsInfo
from .serializers import AttractionInfoSerializer


class AttractionInfoViewSet(ModelViewSet):
    queryset = AttractionsInfo.objects.all()
    serializer_class = AttractionInfoSerializer
