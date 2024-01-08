from generic.views import BaseViewSet
from rest_framework import mixins
from readinesslevel import models as readinesslevel_models
from readinesslevel import serializers as readinesslevel_serializers
from drf_yasg.utils import swagger_auto_schema


class UratQuestionViewSet(
    mixins.ListModelMixin,
    BaseViewSet,
):
    queryset = readinesslevel_models.URATQuestion.objects
    serializer_class = readinesslevel_serializers.base.UratQuestionBaseSerializer

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action in ["list"]:
            return []

        return super().get_permissions()

    def get_queryset(self):
        queryset = self.queryset
        request = self.request

        serializer = readinesslevel_serializers.query.UratQuestionQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)

        readiness_type = serializer.validated_data.get("readiness_type")
        if readiness_type:
            queryset = queryset.filter(readiness_type__rl_type=readiness_type)

        return queryset.all()

    @swagger_auto_schema(
        query_serializer=readinesslevel_serializers.query.UratQuestionQuerySerializer,
        responses={
            200: readinesslevel_serializers.base.UratQuestionBaseSerializer(many=True)
        },
    )
    def list(self, request, *args, **kwargs):
        """List Urat Questions

        Gets a collection of Urat Question instances.
        """
        return super().list(request, *args, **kwargs)


class ReadinessLevelViewSet(
    mixins.ListModelMixin,
    BaseViewSet,
):
    queryset = readinesslevel_models.ReadinessLevel.objects
    serializer_class = readinesslevel_serializers.base.ReadinessLevelBaseSerializer

    def get_queryset(self):
        queryset = self.queryset
        request = self.request

        serializer = readinesslevel_serializers.query.ReadinessLevelQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)

        readiness_type = serializer.validated_data.get("readiness_type")
        if readiness_type:
            queryset = queryset.filter(readiness_type__rl_type=readiness_type)

        return queryset.all()

    @swagger_auto_schema(
        query_serializer=readinesslevel_serializers.query.ReadinessLevelQuerySerializer,
        responses={
            200: readinesslevel_serializers.base.ReadinessLevelBaseSerializer(many=True)
        },
    )
    def list(self, request, *args, **kwargs):
        """List Readiness Levels

        Gets a collection of Readiness Level instances.
        """
        return super().list(request, *args, **kwargs)


class CalculatorCategoryViewSet(
    mixins.ListModelMixin,
    BaseViewSet,
):
    queryset = readinesslevel_models.CalculatorCategory.objects
    serializer_class = readinesslevel_serializers.base.CalculatorCategoryBaseSerializer

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action in ["list"]:
            return []

        return super().get_permissions()

    def get_queryset(self):
        queryset = self.queryset
        request = self.request

        serializer = readinesslevel_serializers.query.CalculatorCatgoryQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)

        readiness_type = serializer.validated_data.get("readiness_type")
        if readiness_type:
            queryset = queryset.filter(readiness_type__rl_type=readiness_type)

        return queryset.all()

    @swagger_auto_schema(
        query_serializer=readinesslevel_serializers.query.CalculatorCatgoryQuerySerializer,
        responses={
            200: readinesslevel_serializers.base.CalculatorCategoryBaseSerializer(
                many=True
            )
        },
    )
    def list(self, request, *args, **kwargs):
        """List Calculator Categories

        Gets a collection of Calculator Category instances.
        """
        return super().list(request, *args, **kwargs)
