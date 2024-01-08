from rest_framework.permissions import IsAuthenticated
from users import models as users_models
from startups import models as startups_models


class IsManagerOrMemberOrMentorOfStartUpPermission(IsAuthenticated):
    message = "User must be a Manager, Owner, member, or mentor of Startup instance."

    def has_object_permission(self, request, view, obj: startups_models.Startup):
        user = request.user
        user_id = user.id

        return (
            user.user_type == users_models.BaseUser.UserType.MANAGER
            or obj.user_id == user_id
            or obj.members.filter(user_id=user_id).exists()
            or obj.mentors.filter(id=user_id).exists()
        )


class IsMentorPermission(IsAuthenticated):
    message = "User must be a Mentor of the startup."

    def has_object_permission(self, request, view, obj: startups_models.Startup):
        user = request.user
        user_id = user.id

        return obj.mentors.filter(id=user_id).exists()


class IsMentorThroughReadinessLevelCriterionAnswerPermission(IsMentorPermission):
    def has_object_permission(
        self, request, view, obj: startups_models.ReadinessLevelCriterionAnswer
    ):
        return super().has_object_permission(request, view, obj.startup)
