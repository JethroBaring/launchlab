from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from users import models as users_models
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = users_models.BaseUser
        fields = [
            "id",
            "user_type",
            "email",
            "first_name",
            "last_name",
        ]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type
        return token