from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BaseUser
        fields = [
            "user_type",
            "email",
            "first_name",
            "last_name",
        ]
