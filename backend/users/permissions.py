from rest_framework.permissions import IsAuthenticated
from users import models as users_models


class IsManagerPermission(IsAuthenticated):
    message = "User should be a Manager type."

    def has_permission(self, request, view):
        user = request.user

        return user.user_type == users_models.BaseUser.UserType.MANAGER


class IsOwnerOfUserPermission(IsAuthenticated):
    message = "Caller must be the owner of User."

    def has_object_permission(self, request, view, obj: users_models.BaseUser):
        user = request.user

        return obj.id == user.id
