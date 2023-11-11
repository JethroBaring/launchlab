from rest_framework import serializers
from startups import models as startups_models


class ApplicantBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = startups_models.Applicant
        fields = "__all__"


class StartupBaseSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True, source="user")
    applicant_id = serializers.PrimaryKeyRelatedField(
        read_only=True, source="applicant"
    )

    class Meta:
        model = startups_models.Startup
        fields = ["name", "user_id", "applicant_id"]


class ReadinessLevelBaseSerializer(serializers.ModelSerializer):
    startup_id = serializers.PrimaryKeyRelatedField(
        source="startup", queryset=startups_models.Startup.objects
    )
    irl = serializers.IntegerField(read_only=True)

    class Meta:
        model = startups_models.ReadinessLevel
        fields = [
            "id",
            "startup_id",
            "trl",
            "orl",
            "mrl",
            "rrl",
            "arl",
            "irl",
            "datetime_created",
        ]
