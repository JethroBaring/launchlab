from rest_framework import serializers
from startups import models as startups_models
from startups.serializers import base as startups_base_serializers
from users import models as users_models


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


class BulkCreateReadinessLevelCriterionAnswerRequestSerializer(serializers.Serializer):
    criterion_answers = (
        startups_base_serializers.ReadinessLevelCriterionAnswerBaseSerializer(many=True)
    )


class BulkCreateUratQuestionAnswerRequestSerializer(serializers.Serializer):
    urat_question_answers = startups_base_serializers.UratQuestionAnswerBaseSerializer(
        many=True
    )


class BulkCreateStartupReadinessLevelRequestSerializer(serializers.Serializer):
    startup_readiness_levels = (
        startups_base_serializers.StartupReadinessLevelBaseSerializer(many=True)
    )


class AssignMentorsRequestSerializer(serializers.Serializer):
    mentor_ids = serializers.ListField(
        child=(
            serializers.PrimaryKeyRelatedField(queryset=users_models.MentorUser.objects)
        ),
        write_only=True,
    )


class BulkCreateCalculatorQuestionAnswerRequestSerializer(serializers.Serializer):
    calculator_question_answers = (
        startups_base_serializers.CalculatorQuestionAnswerBaseSerializer(many=True)
    )
