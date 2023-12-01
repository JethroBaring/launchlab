from rest_framework import serializers
from startups import models as startups_models
from startups.serializers import base as startups_base_serializers


class StartupRequestSerializer(startups_base_serializers.StartupBaseSerializer):
    is_qualified = serializers.BooleanField(read_only=True)
    set_members = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = startups_models.Startup
        fields = [
            "id",
            "name",
            "user_id",
            "is_qualified",
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
