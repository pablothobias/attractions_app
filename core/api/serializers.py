from rest_framework.serializers import ModelSerializer, SerializerMethodField

from address.api.serializers import AddressSerializer
from address.models import Address
from core.models import Attraction
from attractions_info.models import AttractionsInfo
from reviews.api.serializers import ReviewSerializer
from attractions_info.api.serializers import AttractionInfoSerializer


class AttractionSerializer(ModelSerializer):
    address = AddressSerializer(many=False)
    reviews = ReviewSerializer(many=True, read_only=True)
    attractions_info = AttractionInfoSerializer(many=True)
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
            "attractions_info",
            "reviews",
        )

    def insert_address(self, attraction, address):
        address = Address.objects.create(**address)
        attraction.address = address
        return attraction

    def insert_attractions_info(self, attraction, attractions_info):
        for attraction_info in attractions_info:
            new_attraction_info = AttractionsInfo.objects.create(**attraction_info)
            attraction.attractions_info.add(new_attraction_info)
        return attraction

    def create(self, validated_data):
        address = validated_data["address"]
        del validated_data["address"]

        attractions_info = validated_data["attractions_info"]
        del validated_data["attractions_info"]

        attraction = Attraction.objects.create(**validated_data)
        update_attraction_with_address = self.insert_address(attraction, address)

        update_attraction = self.insert_attractions_info(
            update_attraction_with_address, attractions_info
        )

        update_attraction.save()
        return update_attraction

    def get_name_id(self, obj):
        return obj.name + " - " + str(obj.id)
