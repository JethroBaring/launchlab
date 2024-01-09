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
from django.db.models import Q, Sum, Subquery, OuterRef
from startups import utils as startups_utils
from drf_yasg import openapi
from users import permissions as users_permissions
from startups import permissions as startups_permissions


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

        if viewset_action == "create":
            return []

        if viewset_action in [
            "approve_applicant",
            "rate_applicant",
            "reject_applicant",
            "appoint_mentors",
            "ranking_by_urat",
            "ranking_by_rubrics",
            "calculator_final_scores",
        ]:
            return [users_permissions.IsManagerPermission()]

        if viewset_action in ["retrieve", "get_mentors"]:
            return [startups_permissions.IsManagerOrMemberOrMentorOfStartUpPermission()]

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

        if (
            not user.is_anonymous
            and user.user_type == users_models.BaseUser.UserType.MENTOR
        ):
            queryset = queryset.filter(mentors=user)

        return queryset.filter(datetime_deleted__isnull=True).distinct().all()

    @swagger_auto_schema(
        request_body=startups_serializers.request.StartupRequestSerializer,
        responses={200: startups_serializers.base.StartupBaseSerializer},
    )
    def create(self, request):
        """Create Startup

        Creates a new Startup Instance with its members.
        """
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
        request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties={}),
        responses={
            200: "sent email successfully",
            403: users_permissions.IsManagerPermission.message,
        },
    )
    @transaction.atomic
    @action(url_path="approve-applicant", detail=True, methods=["POST"])
    def approve_applicant(self, request, pk):
        """Approve Applicant

        Updates the startup qualifacation status to qualified.
        And send approval emails to leader and members.
        """
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
        request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties={}),
        responses={
            200: "sent email successfully",
            403: users_permissions.IsManagerPermission.message,
        },
    )
    @transaction.atomic
    @action(url_path="reject-applicant", detail=True, methods=["POST"])
    def reject_applicant(self, request, pk):
        """Reject Applicant

        Soft delete startup and
        send rejection email to leader.
        """
        startup = self.get_object()
        startup.datetime_deleted = timezone.now()
        startup.save(update_fields=["datetime_deleted"])

        email = startup.member_1_email
        startups_utils.send_rejection_email(email)

        return Response("sent email successfully", status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties={}),
        responses={
            200: "startup rated successfully",
            403: users_permissions.IsManagerPermission.message,
        },
    )
    @transaction.atomic
    @action(url_path="rate-applicant", detail=True, methods=["POST"])
    def rate_applicant(self, request, pk):
        """Rate Applicant

        Updates the startup qualifacation status to rated.
        """
        startup = self.get_object()
        startup.qualification_status = 2
        startup.save(update_fields=["qualification_status"])

        return Response("startup rated successfully", status=status.HTTP_200_OK)

    @swagger_auto_schema(
        query_serializer=startups_serializers.query.StartupQuerySerializer(),
        responses={
            200: startups_serializers.base.StartupBaseSerializer(),
        },
    )
    def list(self, request, *args, **kwargs):
        """List Startups

        lists startups objects with different filters.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        query_serializer=startups_serializers.query.StartupQuerySerializer(),
        responses={
            200: startups_serializers.base.StartupBaseSerializer(),
            403: startups_permissions.IsManagerOrMemberOrMentorOfStartUpPermission.message,
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """Retrieve Startup

        Retrieves a startup given the id in path.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=startups_serializers.request.AssignMentorsRequestSerializer(),
        responses={
            204: "",
            403: users_permissions.IsManagerPermission.message,
        },
    )
    @action(url_path="appoint-mentors", detail=True, methods=["POST"])
    def appoint_mentors(self, request, pk):
        """Appoint Mentors

        Set mentor/s to the the specified startup.
        """
        startup = self.get_object()

        request_seralizer = startups_serializers.request.AssignMentorsRequestSerializer(
            data=request.data
        )
        request_seralizer.is_valid(raise_exception=True)

        mentor_ids = request_seralizer.validated_data.get("mentor_ids")

        startup.mentors.set(mentor_ids)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        query_serializer=None,
        responses={
            200: startups_serializers.base.StartupBaseSerializer(many=True),
            403: users_permissions.IsManagerPermission.message,
        },
    )
    @action(url_path="ranking-by-urat", detail=False, methods=["GET"])
    def ranking_by_urat(self, request):
        """Ranking By URAT

        Ranking startups based on their URAT scores.
        """
        urat_rankings = startups_models.URATQuestionAnswer.objects.values(
            "startup"
        ).annotate(urat_score=Sum("score"))

        final_scores = []
        for urat_ranking in urat_rankings:
            startup_id = urat_ranking.get("startup")
            technology_level, *_ = startups_utils.calculate_levels(startup_id)

            if technology_level < 4:
                continue

            final_scores.append(
                {
                    "startup_id": startup_id,
                    "score": urat_ranking.get("urat_score") + technology_level,
                }
            )

        final_scores.sort(key=lambda x: x.get("score", 0), reverse=True)

        startup_ids = [ranking["startup_id"] for ranking in final_scores]

        startups = startups_models.Startup.objects.filter(pk__in=startup_ids)
        startups_map = {}
        for startup in startups:
            startups_map[startup.id] = startup

        ordered_startups = []
        for final_score in final_scores:
            ordered_startups.append(startups_map[final_score.get("startup_id")])

        return Response(
            startups_serializers.base.StartupBaseSerializer(
                ordered_startups, many=True
            ).data
        )

    @swagger_auto_schema(
        query_serializer=None,
        responses={
            200: startups_serializers.base.StartupBaseSerializer(many=True),
            403: users_permissions.IsManagerPermission.message,
        },
    )
    @action(url_path="ranking-by-rubrics", detail=False, methods=["GET"])
    def ranking_by_rubrics(self, request):
        """Ranking By Rubrics

        Ranking startups based on their rubrics scores.
        """
        readiness_type_weights = {
            "T": 4,
            "M": 3,
            "R": 2,
            "A": 2,
            "O": 2,
            "I": 2,
        }

        subquery = Subquery(
            startups_models.StartupReadinessLevel.objects.filter(
                startup_id=OuterRef("startup_id"),
                readiness_level__readiness_type_id=OuterRef(
                    "readiness_level__readiness_type_id"
                ),
                readiness_level__readiness_type__rl_type__in=readiness_type_weights.keys(),
            )
            .order_by("datetime_created")
            .values("id")[:1]
        )

        levels = startups_models.StartupReadinessLevel.objects.filter(id=subquery)

        startup_scores = []
        for level in levels:
            startup_score = {
                "startup_id": level.startup_id,
                "weighted_score": level.readiness_level.level
                * readiness_type_weights[level.readiness_level.readiness_type.rl_type],
            }
            startup_scores.append(startup_score)

        total_weighted_scores = {}
        for startup_score in startup_scores:
            startup_id = startup_score["startup_id"]
            if startup_id not in total_weighted_scores:
                total_weighted_scores[startup_id] = 0
            total_weighted_scores[startup_id] += startup_score["weighted_score"]

        ranked_startups = sorted(
            [
                {"startup_id": k, "total_weighted_score": v}
                for k, v in total_weighted_scores.items()
            ],
            key=lambda x: x["total_weighted_score"],
            reverse=True,
        )

        startup_ids = [ranking["startup_id"] for ranking in ranked_startups]

        startups = startups_models.Startup.objects.filter(pk__in=startup_ids)

        startups_map = {}
        for startup in startups:
            startups_map[startup.id] = startup

        ordered_startups = []
        for ranked_startup in ranked_startups:
            ordered_startups.append(startups_map[ranked_startup.get("startup_id")])

        return Response(
            startups_serializers.base.StartupBaseSerializer(
                ordered_startups, many=True
            ).data
        )

    @swagger_auto_schema(
        query_serializer=None,
        responses={
            200: startups_serializers.response.CalculatorFinalScoresResponseSerializer,
            403: users_permissions.IsManagerPermission.message,
        },
    )
    @action(url_path="calculator-final-scores", detail=True, methods=["GET"])
    def calculator_final_scores(self, request, pk):
        """Calculator Final Scores

        Gets the scores using the
        NYSERDA Technology and Commercialization Readiness Level
        Calculator.
        """
        calculator_values = startups_utils.calculate_levels(pk)

        return Response(
            startups_serializers.response.CalculatorFinalScoresResponseSerializer(
                {
                    "technology_level": calculator_values[0],
                    "commercialization_level": calculator_values[1],
                    "technology_score": calculator_values[2],
                    "product_development": calculator_values[3],
                    "product_definition": calculator_values[4],
                    "competitive_landscape": calculator_values[5],
                    "team": calculator_values[6],
                    "go_to_market": calculator_values[7],
                    "supply_chain": calculator_values[8]
                }
            ).data
        )

    @swagger_auto_schema(
        query_serializer=None,
        responses={
            200: startups_serializers.response.GetMentorsResponseSerializer(many=True),
            403: startups_permissions.IsManagerOrMemberOrMentorOfStartUpPermission.message,
        },
    )
    @action(url_path="mentors", detail=True, methods=["GET"])
    def get_mentors(self, request, pk):
        """Get Mentors

        Gets the mentors of the startup.
        """
        startup = self.get_object()

        mentors = startup.mentors.all()

        return Response(
            startups_serializers.response.GetMentorsResponseSerializer(
                mentors, many=True
            ).data
        )


class UratQuestionAnswerViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, BaseViewSet, mixins.UpdateModelMixin
):
    queryset = startups_models.URATQuestionAnswer.objects
    serializer_class = startups_serializers.base.UratQuestionAnswerBaseSerializer

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action in ["create", "bulk_create"]:
            return []

        if viewset_action in ["partial_update", "list"]:
            return [users_permissions.IsManagerPermission()]

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

    @swagger_auto_schema(
        request_body=startups_serializers.base.UratQuestionAnswerBaseSerializer,
        responses={204: startups_serializers.base.UratQuestionAnswerBaseSerializer},
    )
    def create(self, request, *args, **kwargs):
        """Create URAT Question Answer

        Creates a new URAT Question Answer Instance.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        query_serializer=startups_serializers.query.UratQuestionAnswerQuerySerializer,
        responses={
            200: startups_serializers.base.UratQuestionAnswerBaseSerializer,
            403: users_permissions.IsManagerPermission.message,
        },
    )
    def list(self, request, *args, **kwargs):
        """List URAT Question Answers

        Lists a collection of URAT Question Answers.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=startups_serializers.base.UratQuestionAnswerBaseSerializer,
        responses={
            200: startups_serializers.base.UratQuestionAnswerBaseSerializer,
            403: users_permissions.IsManagerPermission.message,
        },
    )
    def partial_update(self, request, *args, **kwargs):
        urat_question_answer = self.get_object()

        request_serializer = (
            startups_serializers.request.UpdateUratQuestionAnswerRequestSerializer(
                data=request.data
            )
        )
        request_serializer.is_valid(raise_exception=True)

        score = request_serializer.validated_data.get("score")

        urat_question_answer.score = score
        urat_question_answer.save(update_fields=["score"])

        return Response(
            self.serializer_class(urat_question_answer).data, status=status.HTTP_200_OK
        )


    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(
        request_body=startups_serializers.request.BulkCreateUratQuestionAnswerRequestSerializer,
        responses={204: ""},
    )
    @action(url_path="bulk-create", detail=False, methods=["POST"])
    def bulk_create(self, request):
        """Bulk Create URAT Question Answers

        Creates multiple URAT Question Answer Instances.
        """
        request_serializer = (
            startups_serializers.request.BulkCreateUratQuestionAnswerRequestSerializer(
                data=request.data
            )
        )

        request_serializer.is_valid(raise_exception=True)

        urat_question_answers = request_serializer.validated_data.get(
            "urat_question_answers"
        )

        urat_question_answers_object = [
            startups_models.URATQuestionAnswer(**urat_question_answer)
            for urat_question_answer in urat_question_answers
        ]

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

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action == "partial_updated":
            return [startups_permissions.IsMentorPermission()]

        return super().get_permissions()

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

    @swagger_auto_schema(
        request_body=startups_serializers.base.ReadinessLevelCriterionAnswerBaseSerializer,
        responses={
            201: startups_serializers.base.ReadinessLevelCriterionAnswerBaseSerializer,
        },
    )
    def create(self, request, *args, **kwargs):
        """Create Readiness Level Criterion Answer

        Creates a new Readiness Level Crtierion Answer instance.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=startups_serializers.request.BulkCreateReadinessLevelCriterionAnswerRequestSerializer,
        responses={
            204: "",
        },
    )
    @action(url_path="bulk-create", detail=False, methods=["POST"])
    def bulk_create(self, request):
        """Bulk Create Readiness Level Criterion Answers

        Creates multiple Readiness Level Criterion Answer Instances.
        """
        request_serializer = startups_serializers.request.BulkCreateReadinessLevelCriterionAnswerRequestSerializer(
            data=request.data
        )

        request_serializer.is_valid(raise_exception=True)

        criterion_answers = request_serializer.validated_data.get("criterion_answers")

        criterion_answers_object = [
            startups_models.ReadinessLevelCriterionAnswer(**criterion_answer)
            for criterion_answer in criterion_answers
        ]

        startups_models.ReadinessLevelCriterionAnswer.objects.bulk_create(
            criterion_answers_object
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        query_serializer=startups_serializers.query.ReadinessLevelCriterionAnswerQuerySerializer,
        responses={
            200: startups_serializers.base.ReadinessLevelCriterionAnswerBaseSerializer(
                many=True
            )
        },
    )
    def list(self, request, *args, **kwargs):
        """List Readiness Level Criterion Answers

        Gets a collection of Readiness Level Criterion Answer Instances.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=startups_serializers.request.ReadinessLevelCriterionAnswerRequestSerializer,
        responses={
            200: startups_serializers.base.ReadinessLevelCriterionAnswerBaseSerializer(),
            403: startups_permissions.IsMentorThroughReadinessLevelCriterionAnswerPermission.message,
        },
    )
    def partial_update(self, request, *args, **kwargs):
        """Partial Update Readiness Level Criterion Answers

        Updates a Readiness Level Criterion Answer field/s.
        """
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


class StartupReadinessLevelViewSet(
    mixins.CreateModelMixin,
    BaseViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = startups_models.StartupReadinessLevel.objects
    serializer_class = startups_serializers.base.StartupReadinessLevelBaseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        serializer = startups_serializers.query.StartupReadinessLevelQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)

        startup_id = serializer.validated_data.get("startup_id")
        if startup_id:
            queryset = queryset.filter(startup_id=startup_id)

        return queryset.all()

    def list(self, request, *args, **kwargs):
        """List Startup Readiness Levels

        List collections of Startup Readiness Level instances.
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Get Startup Readiness Level

        Gets a Startup Readiness Level instance.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Update Startup Readiness Level

        Updates a startup Readiness Level instance.
        """
        return super().partial_update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Create Startup Readiness Level

        Creates a new Startup Readiness Level instance.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=startups_serializers.request.BulkCreateStartupReadinessLevelRequestSerializer,
        responses={204: ""},
    )
    @action(url_path="bulk-create", detail=False, methods=["POST"])
    def bulk_create(self, request):
        """Bulk Create Readiness Levels

        Creates multiple Readiness Level Instances.
        """
        request_serializer = startups_serializers.request.BulkCreateStartupReadinessLevelRequestSerializer(
            data=request.data
        )

        request_serializer.is_valid(raise_exception=True)

        startup_readiness_levels = request_serializer.validated_data.get(
            "startup_readiness_levels"
        )

        startup_readiness_levels_object = [
            startups_models.StartupReadinessLevel(**startup_readiness_level)
            for startup_readiness_level in startup_readiness_levels
        ]

        startups_models.StartupReadinessLevel.objects.bulk_create(
            startup_readiness_levels_object
        )

        return Response(status=status.HTTP_204_NO_CONTENT)


class CalculatorQuestionAnswerViewSet(BaseViewSet):
    queryset = startups_models.CalculatorQuestionAnswer.objects
    serializer_class = startups_serializers.base.CalculatorQuestionAnswerBaseSerializer

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action in ["bulk_create"]:
            return []

        return super().get_permissions()

    @swagger_auto_schema(
        request_body=startups_serializers.request.BulkCreateCalculatorQuestionAnswerRequestSerializer,
        responses={204: ""},
    )
    @action(url_path="bulk-create", detail=False, methods=["POST"])
    def bulk_create(self, request):
        """Bulk Create Calculator Question Answers

        Creates multiple Calculator Question Answer Instances.
        """
        request_serializer = startups_serializers.request.BulkCreateCalculatorQuestionAnswerRequestSerializer(
            data=request.data
        )

        request_serializer.is_valid(raise_exception=True)

        calculator_question_answers = request_serializer.validated_data.get(
            "calculator_question_answers"
        )

        calculator_question_answers_object = [
            startups_models.CalculatorQuestionAnswer(**calculator_question_answer)
            for calculator_question_answer in calculator_question_answers
        ]

        startups_models.CalculatorQuestionAnswer.objects.bulk_create(
            calculator_question_answers_object
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
