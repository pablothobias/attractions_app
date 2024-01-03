from rest_framework.serializers import (
    ModelSerializer,
    ModelSerializer,
    SerializerMethodField,
)
from core.models import Attraction
from address.api.serializers import AddressSerializer
from reviews.api.serializers import ReviewSerializer


class AttractionSerializer(ModelSerializer):
    address = AddressSerializer(many=False)
    reviews = ReviewSerializer(many=True)
    name_id = SerializerMethodField()

    class Meta:
        model = Attraction
        fields = (
            "id",
            "name_id",
            "name",
            "description",
            "image",
            "address",
            "reviews",
        )

    def get_name_id(self, obj):
        return obj.name + " - " + str(obj.id)
