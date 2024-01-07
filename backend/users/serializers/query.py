from rest_framework import serializers
from users import models as users_models


class UserQuerySerializer(serializers.Serializer):
    user_type = serializers.ChoiceField(
        choices=users_models.BaseUser.UserType.choices, required=False
    )
