from rest_framework import serializers
from startups import models as startups_models
from users import models as users_models

class ApplicantBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = startups_models.Applicant
        fields = "__all__"


class StartupBaseSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True, source="user")
    applicant_id = serializers.PrimaryKeyRelatedField(
        read_only=True, source="applicant"
    )

    class Meta:
        model = startups_models.Startup
        fields = ["name", "user_id", "applicant_id"]

class ReadinessLevelBaseSerializer(serializers.ModelSerializer):
    startup_id = serializers.PrimaryKeyRelatedField(
        source="startup", queryset=startups_models.Startup.objects
    )
    irl = serializers.IntegerField(read_only=True)

    class Meta:
        model = startups_models.ReadinessLevel
        fields = [
            "id",
            "startup_id",
            "trl",
            "orl",
            "mrl",
            "rrl",
            "arl",
            "irl",
            "datetime_created",
        ]
class UserSerializer(serializers.ModelSerializer):
    startup_id = serializers.SerializerMethodField(read_only=True)
    startup_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = users_models.User
        fields = ["user_type", "email", "startup_id", "startup_name", "first_name", "last_name"]

    def get_startup_id(self, obj):
        if obj.user_type == 'S':
            return obj.startup.id
        return None

    def get_startup_name(self, obj):
        if obj.user_type == 'S':
            return obj.startup.name
        return None
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user_type = data.get("user_type")

        if user_type != "S":
            # Exclude startup_id and startup_name if user_type is not 'S'
            data.pop("startup_id", None)
            data.pop("startup_name", None)
        else:
            data.pop("first_name", None)
            data.pop("last_name", None)
        
        return data
