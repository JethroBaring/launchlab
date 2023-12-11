from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
from readinesslevel import models as readinesslevel_models


class UratQuestionBaseSerializer(serializers.ModelSerializer):
    readiness_type_id = serializers.PrimaryKeyRelatedField(
        source="readiness_type", queryset=readinesslevel_models.ReadinessType.objects
    )

    readiness_type_verbose = serializers.CharField(source="get_readiness_type_display")

    class Meta:
        model = readinesslevel_models.URATQuestion
        fields = ["id", "question", "readiness_type_id", "readiness_type_verbose"]


class LevelCriterionBaseSerializer(serializers.ModelSerializer):
    readiness_level_id = serializers.PrimaryKeyRelatedField(
        source="readiness_level", read_only=True
    )

    class Meta:
        model = readinesslevel_models.LevelCriterion
        fields = [
            "id",
            "readiness_level_id",
            "criteria",
            "excellent_description",
            "good_description",
            "fair_description",
            "poor_description",
            "very_poor_description",
        ]


class ScoringGuideBaseSerializer(serializers.ModelSerializer):
    level_criteria_id = serializers.PrimaryKeyRelatedField(
        source="level_criteria", read_only=True
    )

    class Meta:
        model = readinesslevel_models.ScoringGuide
        fields = [
            "id",
            "level_criteria_id",
            "start_range",
            "end_range",
            "description",
        ]


class ReadinessLevelBaseSerializer(serializers.ModelSerializer):
    readiness_type_id = serializers.PrimaryKeyRelatedField(
        source="readiness_type", queryset=readinesslevel_models.ReadinessType.objects
    )
    criteria = LevelCriterionBaseSerializer(many=True)
    scoring_guide = ScoringGuideBaseSerializer(many=True)

    readiness_type_verbose = serializers.CharField(source="get_readiness_type_display")

    class Meta:
        model = readinesslevel_models.ReadinessLevel
        fields = [
            "id",
            "level",
            "name",
            "readiness_type_id",
            "readiness_type_verbose",
            "criteria",
            "scoring_guide",
        ]
