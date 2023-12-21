from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import Attraction
from .serializers import AttractionSerializer
from rest_framework.response import Response


class AttractionViewSet(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    def get_queryset(self):
        return super().get_queryset().filter(approved=True)

    # Auxiliary methods:

    # middeleware method GET:
    # def list(self, request, *args, **kwargs):
    #     pass

    # middeleware method POST:
    # def create(self, request, *args, **kwargs):
    #     pass

    # middeleware method DELETE:
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # middeleware method GET DETAIL:
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # middeleware method PUT:
    # def update(self, request, *args, **kwargs):
    #     pass

    # middeleware method PATCH:
    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # Custom action:
    """"
    Usage example:
    http://localhost:8000/api/attractions/1/report/
    """

    @action(methods=["get"], detail=True)
    def report(self, request, pk=None):
        print("Custom action triggered")
        return Response({"Hello": "World"})
