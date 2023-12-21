from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from attractions_info.models import AttractionsInfo

from .serializers import AttractionInfoSerializer


class AttractionInfoViewSet(ModelViewSet):
    # Sets the model of authentication 👇🏻:
    authentication_classes = (TokenAuthentication,)
    # Sets the model of permission 👇🏻:
    permission_classes = (IsAuthenticated,)
    queryset = AttractionsInfo.objects.all()
    serializer_class = AttractionInfoSerializer
