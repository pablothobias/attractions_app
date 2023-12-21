from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from address.models import Address

from .serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    # Sets the model of authentication 👇🏻:
    authentication_classes = (TokenAuthentication,)
    # Sets the model of permission 👇🏻:
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
