from generic.views import BaseViewSet
from rest_framework import mixins
from readinesslevel import models as readinesslevel_models
from readinesslevel import serializers as readinesslevel_serializers


class UratQuestionViewSet(
    mixins.ListModelMixin,
    BaseViewSet,
):
    queryset = readinesslevel_models.URATQuestion.objects
    serializer_class = readinesslevel_serializers.base.UratQuestionBaseSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ReadinessLevelViewSet(
    mixins.ListModelMixin,
    BaseViewSet,
):
    queryset = readinesslevel_models.ReadinessLevel.objects
    serializer_class = readinesslevel_serializers.base.ReadinessLevelBaseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        serializer = readinesslevel_serializers.query.ReadinessLevelQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)

        readiness_type = serializer.validated_data.get("readiness_type")
        if readiness_type:
            queryset = queryset.filter(readiness_type__rl_type=readiness_type)

        return queryset.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
