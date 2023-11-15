from rest_framework import serializers
from users import models

class UserSerializer(serializers.ModelSerializer):
    startup_id = serializers.SerializerMethodField(read_only=True)
    startup_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.User
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
