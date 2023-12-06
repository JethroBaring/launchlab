from django.db import models
from generic.models import BaseModel
from users import models as users_models


class Startup(BaseModel):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(
        users_models.StartupUser,
        on_delete=models.SET_NULL,
        related_name="startups",
        null=True,
        default=None,
    )
    is_qualified = models.BooleanField(default=False)
    data_privacy = models.BooleanField(default=False)
    capsule_proposal = models.FileField(upload_to="capsule_proposals")
    links = models.TextField(null=True, blank=True)
    group_name = models.CharField(max_length=100)
    member_1_name = models.CharField(max_length=100)
    member_1_number = models.CharField(max_length=20, null=True, default=None)
    member_1_email = models.EmailField()

    university_name = models.CharField(max_length=200, null=True, blank=True)
    eligibility = models.BooleanField(default=False)


class StartupMember(BaseModel):
    email = models.EmailField()
    startup = models.ForeignKey(
        Startup, on_delete=models.CASCADE, related_name="members"
    )
    user = models.ForeignKey(
        users_models.BaseUser,
        on_delete=models.SET_NULL,
        related_name="startup_members",
        null=True,
        default=None,
    )


class ReadinessLevel(BaseModel):
    startup = models.ForeignKey(
        Startup, on_delete=models.CASCADE, related_name="readiness_levels"
    )
    trl = models.IntegerField(default=0)
    orl = models.IntegerField(default=0)
    mrl = models.IntegerField(default=0)
    rrl = models.IntegerField(default=0)
    arl = models.IntegerField(default=0)
    irl = models.IntegerField(default=0)


class InitialReadinessLevel(BaseModel):
    startup = models.OneToOneField(
        Startup, on_delete=models.CASCADE, related_name="initial_readiness_level"
    )
    trl_response = models.JSONField(blank=True, null=True)
    orl_response = models.JSONField(blank=True, null=True)
    mrl_response = models.JSONField(blank=True, null=True)
    rrl_response = models.JSONField(blank=True, null=True)
    arl_response = models.JSONField(blank=True, null=True)
    irl_response = models.JSONField(blank=True, null=True)
    trl = models.CharField(max_length=10, blank=True, null=True)
    orl = models.CharField(max_length=10, blank=True, null=True)
    mrl = models.CharField(max_length=10, blank=True, null=True)
    rrl = models.CharField(max_length=10, blank=True, null=True)
    arl = models.CharField(max_length=10, blank=True, null=True)
    irl = models.CharField(max_length=10, blank=True, null=True)
