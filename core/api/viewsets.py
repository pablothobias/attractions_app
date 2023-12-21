from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Attraction

from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    # Sets the model of authentication 👇🏻:
    authentication_classes = (TokenAuthentication,)
    # Sets the model of permission 👇🏻:
    permission_classes = (IsAuthenticated,)
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filterset_fields = ("id", "name", "description", "approved")

    # def get_queryset(self):
    #     return super().get_queryset().filter(approved=True)

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

    @action(methods=["get"], detail=True)
    def get_by_param(self, request, pk=None):
        id = self.request.query_params.get("id", None)
        name = self.request.query_params.get("name", None)
        if not id and not name:
            return Response({"error": "You need to pass id or name param"})
        else:
            if id:
                queryset = Attraction.objects.filter(id=id)
            else:
                queryset = Attraction.objects.filter(name__iexact=name)
        return Response(self.serializer_class(queryset, many=True).data)
