from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from reviews.models import Review

from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    # Sets the model of authentication 👇🏻:
    authentication_classes = (TokenAuthentication,)
    # Sets the model of permission 👇🏻:
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
