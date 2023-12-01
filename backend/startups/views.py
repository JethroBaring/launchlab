from generic.views import BaseViewSet
from rest_framework import status, mixins
from rest_framework.response import Response
from startups import models as startups_models
from startups import serializers as startups_serializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from users import models as users_models
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone
from django.db.models import Q
from startups import utils as startups_utils


# TODO:
# add permissions
class StartupViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, BaseViewSet):
    queryset = startups_models.Startup.objects
    serializer_class = startups_serializers.base.StartupBaseSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action == "create":
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

        is_qualified = serializer.validated_data.get("is_qualified", None)
        if is_qualified is not None:
            queryset = queryset.filter(is_qualified=is_qualified)

        if (
            not user.is_anonymous
            and user.user_type == users_models.BaseUser.UserType.STARTUP
        ):
            queryset = queryset.filter(Q(user_id=user.id) | Q(members__user_id=user.id))

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
        startup.is_qualified = True
        startup.save(update_fields=["is_qualified", "user"])

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


class ReadinessLevelViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, BaseViewSet
):
    queryset = startups_models.ReadinessLevel.objects
    serializer_class = startups_serializers.base.ReadinessLevelBaseSerializer

    @swagger_auto_schema(
        request_body=serializer_class(),
        responses={
            200: serializer_class(),
        },
    )
    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        serializer = startups_serializers.query.ReadinessLevelQuerySerializer(
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
