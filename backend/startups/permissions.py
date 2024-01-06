from rest_framework.permissions import IsAuthenticated
from users import models as users_models
from startups import models as startups_models


class IsManagerPermission(IsAuthenticated):
    message = "User should be a Manager type."

    def has_object_permission(self, request, obj: users_models.BaseUser):
        return obj.user_type == users_models.BaseUser.UserType.MANAGER


class IsManagerOrOwnerOfStartUpPermission(IsAuthenticated):
    message = "User must be a Manager or Owner of StatUp Instance."

    def has_object_permission(self, request, obj: startups_models.Startup):
        user = request.user

        return (
            obj.user.user_type == users_models.BaseUser.UserType.MANAGER
            or obj.user_id == user.id
        )
