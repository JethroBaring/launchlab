from generic.views import BaseViewSet
from rest_framework import status, mixins
from rest_framework.response import Response
from startups import models as startups_models
from startups import serializers as startups_serializers
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import action
from users import models as users_models
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone
from django.db.models import Q
from startups import utils as startups_utils


class StartupViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    BaseViewSet,
):
    queryset = startups_models.Startup.objects
    serializer_class = startups_serializers.base.StartupBaseSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action in ["create", "create_initial_readiness_level"]:
            return []

        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request
        user = request.user

        serializer = startups_serializers.query.StartupQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)

        qualification_status = serializer.validated_data.get(
            "qualification_status", None
        )
        if qualification_status is not None:
            queryset = queryset.filter(qualification_status=qualification_status)

        if (
            not user.is_anonymous
            and user.user_type == users_models.BaseUser.UserType.STARTUP
        ):
            queryset = queryset.filter(Q(user_id=user.id) | Q(members__user_id=user.id))

        if not user.is_anonymous and user.user_type == users_models.BaseUser.UserType.MENTOR:
            # Filter startups associated with the mentor
            queryset = queryset.filter(mentors=user)
        
        return queryset.filter(datetime_deleted__isnull=True).all()

    @swagger_auto_schema(
        request_body=startups_serializers.request.StartupRequestSerializer,
        responses={200: startups_serializers.base.StartupBaseSerializer},
    )
    def create(self, request):
        serializer = startups_serializers.request.StartupRequestSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        members_email = serializer.validated_data.pop("set_members", [])

        startup = startups_models.Startup.objects.create(**serializer.validated_data)

        for member_email in members_email:
            startups_models.StartupMember.objects.create(
                email=member_email, startup=startup
            )

        return Response(self.serializer_class(startup).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            200: "sent email successfully",
        },
    )
    @transaction.atomic
    @action(url_path="approve-applicant", detail=True, methods=["POST"])
    def approve_applicant(self, request, pk):
        startup = self.get_object()

        member_1_email = startup.member_1_email
        members = startup.members.all()

        for member in members:
            user = startups_utils.send_approval_email(member.email)
            member.user = user
            member.save(update_fields=["user"])

        user = startups_utils.send_approval_email(
            member_1_email, first_name=startup.member_1_name
        )
        startup.user = user
        startup.qualification_status = 3
        startup.save(update_fields=["qualification_status", "user"])

        return Response("sent email successfully", status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            200: "sent email successfully",
        },
    )
    @transaction.atomic
    @action(url_path="reject-applicant", detail=True, methods=["POST"])
    def reject_applicant(self, request, pk):
        startup = self.get_object()
        startup.datetime_deleted = timezone.now()
        startup.save(update_fields=["datetime_deleted"])

        email = startup.member_1_email
        startups_utils.send_rejection_email(email)

        return Response("sent email successfully", status=status.HTTP_200_OK)

    @swagger_auto_schema(
        query_serializer=startups_serializers.query.StartupQuerySerializer(),
        responses={
            200: startups_serializers.base.StartupBaseSerializer(many=True),
        },
    )
    @transaction.atomic
    @action(url_path="rate-applicant", detail=True, methods=["POST"])
    def rate_applicant(self, request, pk):
        startup = self.get_object()
        startup.qualification_status = 2
        startup.save(update_fields=["qualification_status"])

        return Response("startup rated successfully", status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        query_serializer=startups_serializers.query.StartupQuerySerializer(),
        responses={
            200: startups_serializers.base.StartupBaseSerializer(),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        startup = self.get_object()

        request_serializer = (
            startups_serializers.request.UpdateStartupRequestSerializer(
                data=request.data
            )
        )
        request_serializer.is_valid(raise_exception=True)

        qualification_status = request_serializer.validated_data.get(
            "qualification_status"
        )

        startup.qualification_status = qualification_status
        startup.save(update_fields=["qualification_status"])

        return Response(self.serializer_class(startup).data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=startups_serializers.request.AssignMentorsRequestSerializer,
        responses={204: ""},
    )
    @action(url_path="appoint-mentors", detail=True, methods=["POST"])
    def appoint_mentors(self, request, pk):
        startup = self.get_object()

        request_seralizer = startups_serializers.request.AssignMentorsRequestSerializer(
            data=request.data
        )
        request_seralizer.is_valid(raise_exception=True)

        mentor_ids = request_seralizer.validated_data.get("mentor_ids")

        startup.mentors.set(mentor_ids)

        return Response(status=status.HTTP_204_NO_CONTENT)


class UratQuestionAnswerViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, BaseViewSet, mixins.UpdateModelMixin
):
    queryset = startups_models.URATQuestionAnswer.objects
    serializer_class = startups_serializers.base.UratQuestionAnswerBaseSerializer

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action in ["create","bulk_create"]:
            return []

        return super().get_permissions()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        serializer = startups_serializers.query.UratQuestionAnswerQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)
        startup_id = serializer.validated_data.get("startup_id")
        if startup_id:
            queryset = queryset.filter(startup_id=startup_id)

        return queryset.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=startups_serializers.request.BulkCreateUratQuestionAnswerRequestSerializer,
        responses={204: ""},
    )
    @action(url_path="bulk-create", detail=False, methods=["POST"])
    def bulk_create(self, request):
        request_serializer = (
            startups_serializers.request.BulkCreateUratQuestionAnswerRequestSerializer(
                data=request.data
            )
        )

        request_serializer.is_valid(raise_exception=True)

        urat_question_answers = request_serializer.validated_data.get(
            "urat_question_answers"
        )

        urat_question_answers_object = []
        for urat_question_answer in urat_question_answers:
            startup = urat_question_answer.get("startup")

            # if not (startup.user.id == request.user.id):
            #     continue

            urat_question_answers_object.append(
                startups_models.URATQuestionAnswer(**urat_question_answer)
            )

        startups_models.URATQuestionAnswer.objects.bulk_create(
            urat_question_answers_object
        )

        return Response(status=status.HTTP_204_NO_CONTENT)


class ReadinessLevelCriterionAnswerViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, BaseViewSet
):
    queryset = startups_models.ReadinessLevelCriterionAnswer.objects
    serializer_class = (
        startups_serializers.base.ReadinessLevelCriterionAnswerBaseSerializer
    )

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        serializer = (
            startups_serializers.query.ReadinessLevelCriterionAnswerQuerySerializer(
                data=request.query_params
            )
        )

        serializer.is_valid(raise_exception=True)

        startup_id = serializer.validated_data.get("startup_id")
        if startup_id:
            queryset = queryset.filter(startup_id=startup_id)

        criterion_id = serializer.validated_data.get("criterion_id")
        if criterion_id:
            queryset = queryset.filter(criterion_id=criterion_id)

        return queryset.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=startups_serializers.request.BulkCreateReadinessLevelCriterionAnswerRequestSerializer,
        responses={204: ""},
    )
    @action(url_path="bulk-create", detail=False, methods=["POST"])
    def bulk_create(self, request):
        request_serializer = startups_serializers.request.BulkCreateReadinessLevelCriterionAnswerRequestSerializer(
            data=request.data
        )

        request_serializer.is_valid(raise_exception=True)

        criterion_answers = request_serializer.validated_data.get("criterion_answers")

        criterion_answers_object = []
        for criterion_answer in criterion_answers:
            startup = criterion_answer.get("startup")

            # if not (startup.user.id == request.user.id):
            #     continue

            criterion_answers_object.append(
                startups_models.ReadinessLevelCriterionAnswer(**criterion_answer)
            )

        startups_models.ReadinessLevelCriterionAnswer.objects.bulk_create(
            criterion_answers_object
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        readinesslevel_criterion_answer = self.get_object()

        request_serializer = (
            startups_serializers.request.ReadinessLevelCriterionAnswerRequestSerializer(
                data=request.data
            )
        )
        request_serializer.is_valid(raise_exception=True)

        score = request_serializer.validated_data.get("score")
        remark = request_serializer.validated_data.get("remark")

        readinesslevel_criterion_answer.score = score
        readinesslevel_criterion_answer.remark = remark

        readinesslevel_criterion_answer.save(update_fields=["score", "remark"])

        return Response(
            self.serializer_class(readinesslevel_criterion_answer).data,
            status=status.HTTP_200_OK,
        )


class StartupReadinessLevelViewSet(mixins.CreateModelMixin, BaseViewSet):
    queryset = startups_models.StartupReadinessLevel.objects
    serializer_class = startups_serializers.base.StartupReadinessLevelBaseSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=startups_serializers.request.BulkCreateStartupReadinessLevelRequestSerializer,
        responses={204: ""},
    )
    @action(url_path="bulk-create", detail=False, methods=["POST"])
    def bulk_create(self, request):
        request_serializer = startups_serializers.request.BulkCreateStartupReadinessLevelRequestSerializer(
            data=request.data
        )

        request_serializer.is_valid(raise_exception=True)

        startup_readiness_levels = request_serializer.validated_data.get(
            "startup_readiness_levels"
        )

        startup_readiness_levels_object = []
        for startup_readiness_level in startup_readiness_levels:
            startup = startup_readiness_level.get("startup")

            # if not (startup.user.id == request.user.id):
            #     continue

            startup_readiness_levels_object.append(
                startups_models.StartupReadinessLevel(**startup_readiness_level)
            )

        startups_models.StartupReadinessLevel.objects.bulk_create(
            startup_readiness_levels_object
        )

        return Response(status=status.HTTP_204_NO_CONTENT)


class CalculatorQuestionAnswerViewSet(BaseViewSet):
    queryset = startups_models.CalculatorQuestionAnswer.objects
    serializer_class = startups_serializers.base.CalculatorQuestionAnswerBaseSerializer

    @swagger_auto_schema(
        request_body=startups_serializers.request.BulkCreateCalculatorQuestionAnswerRequestSerializer,
        responses={204: ""},
    )
    @action(url_path="bulk-create", detail=False, methods=["POST"])
    def bulk_create(self, request):
        request_serializer = startups_serializers.request.BulkCreateCalculatorQuestionAnswerRequestSerializer(
            data=request.data
        )

        request_serializer.is_valid(raise_exception=True)

        calculator_question_answers = request_serializer.validated_data.get(
            "calculator_question_answers"
        )

        calculator_question_answers_object = []
        for calculator_question_answer in calculator_question_answers:
            startup = calculator_question_answer.get("startup")

            # if not (startup.user.id == request.user.id):
            #     continue

            calculator_question_answers_object.append(
                startups_models.CalculatorQuestionAnswer(**calculator_question_answer)
            )

        startups_models.CalculatorQuestionAnswer.objects.bulk_create(
            calculator_question_answers_object
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
