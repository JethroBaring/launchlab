from rest_framework import serializers
from users import models as users_models


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = users_models.BaseUser
        fields = [
            "user_type",
            "email",
            "first_name",
            "last_name",
        ]
