from rest_framework import serializers


class StartupQuerySerializer(serializers.Serializer):
    is_qualified = serializers.BooleanField(
        required=False, allow_null=True, default=None
    )


class UratQuestionAnswerQuerySerializer(serializers.Serializer):
    startup_id = serializers.IntegerField(required=False)


class ReadinessLevelCriterionAnswerQuerySerializer(serializers.Serializer):
    startup_id = serializers.IntegerField(required=False)
    criterion_id = serializers.IntegerField(required=False)
