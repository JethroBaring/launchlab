from django.shortcuts import render
from generic.views import BaseViewSet
from rest_framework import filters, status
from rest_framework.response import Response
from startups import models as startups_models
from startups import serializers as startups_serializers


class ApplicantViewSet(BaseViewSet):
    queryset = startups_models.Applicant.objects
    serializer_class = startups_serializers.base.ApplicantBaseSerializer

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action == "create":
            return []

        return super().get_permissions()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        applicant = startups_models.Applicant.objects.create(
            **serializer.validated_data
        )

        return Response(
            self.serializer_class(applicant).data, status=status.HTTP_200_OK
        )
