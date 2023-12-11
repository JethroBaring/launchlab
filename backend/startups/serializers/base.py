from rest_framework import serializers
from startups import models as startups_models
from drf_yasg.utils import swagger_serializer_method
from readinesslevel import models as readinesslevel_models


class StartupMemberBaseSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)
    startup_id = serializers.PrimaryKeyRelatedField(source="startup", read_only=True)

    class Meta:
        model = startups_models.StartupMember
        fields = ["id", "email", "user_id", "startup_id"]


class StartupBaseSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source="user", read_only=True)
    members = serializers.SerializerMethodField(method_name="_members")
    initial_readiness_level_id = serializers.PrimaryKeyRelatedField(
        source="initial_readiness_level", read_only=True, allow_null=True
    )

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
            "members",
            "initial_readiness_level_id",
        ]

    @swagger_serializer_method(StartupMemberBaseSerializer())
    def _members(self, startup):
        return StartupMemberBaseSerializer(startup.members.all(), many=True).data


class UratQuestionAnswerBaseSerializer(serializers.ModelSerializer):
    startup_id = serializers.PrimaryKeyRelatedField(
        source="startup", queryset=startups_models.Startup.objects
    )
    urat_question_id = serializers.PrimaryKeyRelatedField(
        source="urat_question", queryset=readinesslevel_models.URATQuestion.objects
    )
    score = serializers.IntegerField(read_only=True)

    class Meta:
        model = startups_models.URATQuestionAnswer
        fields = [
            "id",
            "startup_id",
            "urat_question_id",
            "response",
            "score",
        ]


class ReadinessLevelCriterionAnswerBaseSerializer(serializers.ModelSerializer):
    startup_id = serializers.PrimaryKeyRelatedField(
        source="startup", queryset=startups_models.Startup.objects
    )
    criterion_id = serializers.PrimaryKeyRelatedField(
        source="criterion", queryset=readinesslevel_models.LevelCriterion.objects
    )
    remark = serializers.CharField(required=False)

    class Meta:
        model = startups_models.ReadinessLevelCriterionAnswer
        fields = [
            "id",
            "startup_id",
            "criterion_id",
            "score",
            "remark",
        ]


# class ReadinessLevelBaseSerializer(serializers.ModelSerializer):
#     startup_id = serializers.PrimaryKeyRelatedField(
#         source="startup", queryset=startups_models.Startup.objects
#     )
#     irl = serializers.IntegerField(read_only=True)

#     class Meta:
#         model = startups_models.ReadinessLevel
#         fields = [
#             "id",
#             "startup_id",
#             "trl",
#             "orl",
#             "mrl",
#             "rrl",
#             "arl",
#             "irl",
#             "datetime_created",
#         ]


# class InitialReadinessLevelBaseSerializer(serializers.ModelSerializer):
#     startup_id = serializers.PrimaryKeyRelatedField(source="startup", read_only=True)

#     class Meta:
#         model = startups_models.InitialReadinessLevel
#         fields = [
#             "id",
#             "startup_id",
#             "trl_response",
#             "orl_response",
#             "mrl_response",
#             "rrl_response",
#             "arl_response",
#             "irl_response",
#             "trl",
#             "orl",
#             "mrl",
#             "rrl",
#             "arl",
#             "irl",
#         ]
