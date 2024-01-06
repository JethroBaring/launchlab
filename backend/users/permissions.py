from rest_framework.permissions import IsAuthenticated
from users import models as users_models


class IsManagerPermission(IsAuthenticated):
    message = "User should be a Manager type."

    def has_permission(self, request, view):
        user = request.user

        return user.user_type == users_models.BaseUser.UserType.MANAGER
