from django.shortcuts import render
from rest_framework import status, mixins
from generic.views import BaseViewSet
from users import models
from users import serializers
# Create your views here.
class UserViewSet(mixins.RetrieveModelMixin, BaseViewSet):
    queryset = models.User.objects
    serializer_class = serializers.UserSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
