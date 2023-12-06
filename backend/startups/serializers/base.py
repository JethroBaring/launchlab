from rest_framework import serializers
from startups import models as startups_models
from drf_yasg.utils import swagger_serializer_method


class StartupMemberBaseSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)
    startup_id = serializers.PrimaryKeyRelatedField(source="startup", read_only=True)

    class Meta:
        model = startups_models.StartupMember
        fields = ["id", "email", "user_id", "startup_id"]


class StartupBaseSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)
    members = serializers.SerializerMethodField(method_name="_members")

    class Meta:
        model = startups_models.Startup
        fields = [
            "id",
            "name",
            "user_id",
            "is_qualified",
            "data_privacy",
            "capsule_proposal",
            "links",
            "group_name",
            "member_1_name",
            "member_1_number",
            "member_1_email",
            "university_name",
            "eligibility",
            "members",
        ]

    @swagger_serializer_method(StartupMemberBaseSerializer())
    def _members(self, startup):
        return StartupMemberBaseSerializer(startup.members.all(), many=True).data


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


class InitialReadinessLevelBaseSerializer(serializers.ModelSerializer):
    startup_id = serializers.PrimaryKeyRelatedField(source="startup", read_only=True)

    class Meta:
        model = startups_models.InitialReadinessLevel
        fields = [
            "id",
            "startup_id",
            "trl_response",
            "orl_response",
            "mrl_response",
            "rrl_response",
            "arl_response",
            "irl_response",
            "trl",
            "orl",
            "mrl",
            "rrl",
            "arl",
            "irl",
        ]
