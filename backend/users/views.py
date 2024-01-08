from rest_framework import mixins
from generic.views import BaseViewSet
from users import models
from users import serializers as users_serializers
from users import permissions as users_permissions


class UserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, BaseViewSet):
    queryset = models.BaseUser.objects
    serializer_class = users_serializers.base.UserBaseSerializer

    def get_permissions(self):
        viewset_action = self.action

        if viewset_action == "list":
            return [users_permissions.IsManagerPermission()]

        if viewset_action == "retrieve":
            return [users_permissions.IsOwnerOfUserPermission()]

        return super().get_permissions()

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        serializer = users_serializers.query.UserQuerySerializer(
            data=request.query_params
        )

        serializer.is_valid(raise_exception=True)

        user_type = serializer.validated_data.get("user_type")
        if user_type:
            queryset = queryset.filter(user_type=user_type)

        return queryset.all()

    def retrieve(self, request, *args, **kwargs):
        """Retrieve User

        Gets a User Instance.
        """
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """List Users

        Gets a collection of Users instances.
        """
        return super().list(request, *args, **kwargs)
