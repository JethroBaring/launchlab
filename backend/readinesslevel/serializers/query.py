from rest_framework import serializers
from readinesslevel import models as readinesslevel_models


class ReadinessLevelQuerySerializer(serializers.Serializer):
    readiness_type = serializers.ChoiceField(
        required=False, choices=readinesslevel_models.ReadinessType.RLType.choices
    )
