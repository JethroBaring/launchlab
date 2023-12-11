from django.db import models
from generic.models import BaseModel
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from users import managers


class BaseUser(AbstractBaseUser, BaseModel):
    class UserType(models.TextChoices):
        MANAGER = "M", _("Manager")
        STARTUP = "S", _("Startup")
        MENTOR = "ME", _("Mentor")

    username = None
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    profile_pic = models.ImageField(
        "Profile Picture", upload_to="users/", blank=True, null=True
    )
    user_type = models.CharField(
        "User Type",
        max_length=2,
        choices=UserType.choices,
    )

    objects = managers.CustomBaseUserManager()

    USERNAME_FIELD = "email"


class ManagerUser(BaseUser):
    objects = managers.ManagerUserManager()


class StartupUser(BaseUser):
    objects = managers.StartupUserManager()


class MentorUser(BaseUser):
    objects = managers.MentorUserManager()
