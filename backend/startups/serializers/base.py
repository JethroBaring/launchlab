from rest_framework import serializers
from startups import models as startups_models


class ApplicantBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = startups_models.Applicant
        fields = "__all__"
