from rest_framework import serializers
from startups import models as startups_models
from startups.serializers import base as startups_base_serializers


class StartupRequestSerializer(startups_base_serializers.StartupBaseSerializer):
    qualification_status = serializers.IntegerField(read_only=True)
    set_members = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = startups_models.Startup
        fields = [
            "id",
            "name",
            "user_id",
            "qualification_status",
            "data_privacy",
            "capsule_proposal",
            "links",
            "group_name",
            "member_1_name",
            "member_1_number",
            "member_1_email",
            "university_name",
            "eligibility",
            "set_members",
        ]


class UpdateStartupRequestSerializer(startups_base_serializers.StartupBaseSerializer):
    class Meta:
        model = startups_models.Startup
        fields = ["qualification_status"]


class UpdateUratQuestionAnswerRequestSerializer(serializers.Serializer):
    score = serializers.IntegerField()


class ReadinessLevelCriterionAnswerRequestSerializer(serializers.Serializer):
    score = serializers.IntegerField()
    remake = serializers.CharField(required=False)
