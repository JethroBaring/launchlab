from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method
from readinesslevel import models as readinesslevel_models


class UratQuestionBaseSerializer(serializers.ModelSerializer):
    readiness_type_id = serializers.PrimaryKeyRelatedField(
        source="readiness_type", queryset=readinesslevel_models.ReadinessType.objects
    )
    readiness_type = serializers.CharField(
        source="readiness_type.get_rl_type_display", read_only=True
    )

    class Meta:
        model = readinesslevel_models.URATQuestion
        fields = ["id", "question", "readiness_type_id", "readiness_type"]


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
    readiness_level_id = serializers.PrimaryKeyRelatedField(
        source="readiness_level", read_only=True
    )

    class Meta:
        model = readinesslevel_models.ScoringGuide
        fields = [
            "id",
            "readiness_level_id",
            "start_range",
            "end_range",
            "description",
        ]


class ReadinessLevelBaseSerializer(serializers.ModelSerializer):
    readiness_type_id = serializers.PrimaryKeyRelatedField(
        source="readiness_type", queryset=readinesslevel_models.ReadinessType.objects
    )
    level_criteria = LevelCriterionBaseSerializer(many=True)
    scoring_guides = ScoringGuideBaseSerializer(many=True)
    readiness_type = serializers.CharField(
        source="readiness_type.get_rl_type_display", read_only=True
    )

    class Meta:
        model = readinesslevel_models.ReadinessLevel
        fields = [
            "id",
            "level",
            "name",
            "readiness_type_id",
            "readiness_type",
            "level_criteria",
            "scoring_guides",
        ]


class CalculatorQuestionBaseSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        source="category", queryset=readinesslevel_models.CalculatorCategory.objects
    )

    class Meta:
        model = readinesslevel_models.CalculatorQuestion
        fields = ["id", "question", "score", "category_id"]


class CalculatorCategoryBaseSerializer(serializers.ModelSerializer):
    readiness_type_id = serializers.PrimaryKeyRelatedField(
        source="readiness_type", queryset=readinesslevel_models.ReadinessType.objects
    )
    questions = CalculatorQuestionBaseSerializer(many=True)

    class Meta:
        model = readinesslevel_models.CalculatorCategory
        fields = ["id", "category", "readiness_type_id", "questions"]
