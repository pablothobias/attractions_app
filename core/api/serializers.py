from rest_framework.serializers import (
    ModelSerializer,
    ModelSerializer,
    SerializerMethodField,
)
from core.models import Attraction
from address.api.serializers import AddressSerializer
from address.models import Address
from reviews.api.serializers import ReviewSerializer


class AttractionSerializer(ModelSerializer):
    address = AddressSerializer(many=False)
    reviews = ReviewSerializer(many=True, read_only=True)
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

    def insert_address(self, attraction, address):
        address = Address.objects.create(**address)
        attraction.address = address
        return attraction

    def create(self, validated_data):
        address = validated_data["address"]
        del validated_data["address"]
        attraction = Attraction.objects.create(**validated_data)
        update_attraction = self.insert_address(attraction, address)
        update_attraction.save()
        return update_attraction

    def get_name_id(self, obj):
        return obj.name + " - " + str(obj.id)
