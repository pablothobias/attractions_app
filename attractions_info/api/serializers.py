from rest_framework.serializers import ModelSerializer
from attractions_info.models import AttractionsInfo


class AttractionInfoSerializer(ModelSerializer):
    class Meta:
        model = AttractionsInfo
        fields = (
            "id",
            "name",
            "descriptions",
            "open_days",
            "open_hour",
            "close_hour",
            "min_age_enter",
        )
