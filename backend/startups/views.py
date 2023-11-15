from generic.views import BaseViewSet
from rest_framework import status, mixins
from rest_framework.response import Response
from startups import models as startups_models
from startups import serializers as startups_serializers
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from users import models as users_models
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema


# TODO:
# login
# Add send email chuchu
# generate random password
class ApplicantViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, BaseViewSet):
    queryset = startups_models.Applicant.objects
    serializer_class = startups_serializers.base.ApplicantBaseSerializer
    parser_classes = (MultiPartParser,)

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action == "create":
            return []

        return super().get_permissions()

    def get_queryset(self):
        """Get Queryset

        Gets the queryset based on the `query_params` from the request.
        Only the fields found in `SectionModelQuerySerializer` will be read
        from the query parameters.
        """
        queryset = super().get_queryset()
        request = self.request

        serializer = startups_serializers.query.ApplicantQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)

        is_qualified = serializer.validated_data.get("is_qualified", None)
        if is_qualified is not None:
            queryset = queryset.filter(startup__isnull=not is_qualified)

        return queryset.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        applicant = startups_models.Applicant.objects.create(
            **serializer.validated_data
        )

        return Response(
            self.serializer_class(applicant).data, status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        responses={
            200: "sent email successfully",
        },
    )
    @transaction.atomic
    @action(url_path="approve-applicant", detail=True, methods=["POST"])
    def approve_applicant(self, request, pk):
        applicant = self.get_object()

        # TODO: generate random password
        password = "123"
        user = users_models.User.objects.create_user(
            email=applicant.member_1_email,
            password=password,
            user_type=users_models.User.UserType.STARTUP,
        )
        startup = startups_models.Startup.objects.create(
            applicant=applicant, user=user, name=applicant.starup_name
        )

        # Send email
        #
        return Response("sent email successfully", status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={
            200: "sent email successfully",
        },
    )
    @transaction.atomic
    @action(url_path="reject-applicant", detail=True, methods=["POST"])
    def reject_applicant(self, request, pk):
        applicant = self.get_object()
    
        # Send email
        #
        return Response("sent email successfully", status=status.HTTP_200_OK)

    @swagger_auto_schema(
        query_serializer=startups_serializers.query.ApplicantQuerySerializer(),
        responses={
            200: startups_serializers.base.ApplicantBaseSerializer(many=True),
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class StartupViewSet(mixins.RetrieveModelMixin, BaseViewSet):
    queryset = startups_models.Startup.objects
    serializer_class = startups_serializers.base.StartupBaseSerializer

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = startups_serializers.response.StartupResponseSerializer
        return super().retrieve(request, *args, **kwargs)


class ReadinessLevelViewSet(mixins.CreateModelMixin, BaseViewSet):
    queryset = startups_models.ReadinessLevel.objects
    serializer_class = startups_serializers.base.ReadinessLevelBaseSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class UserViewSet(mixins.RetrieveModelMixin, BaseViewSet):
    queryset = users_models.User.objects
    serializer_class = startups_serializers.base.UserSerializer
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)