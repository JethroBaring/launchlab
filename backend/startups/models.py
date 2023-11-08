from django.db import models
from generic.models import BaseModel
from users import models as users_models


class Applicant(BaseModel):
    data_privacy = models.BooleanField()
    starup_name = models.CharField(max_length=300)
    capsule_proposal = models.FileField(upload_to="capsule_proposals")
    links = models.TextField(null=True, blank=True)
    group_name = models.CharField(max_length=100)
    member_1_name = models.CharField(max_length=100)
    member_1_number = models.CharField(max_length=20)
    member_1_email = models.EmailField()
    member_2_name = models.CharField(max_length=100)
    member_3_name = models.CharField(max_length=100)
    member_4_name = models.CharField(max_length=100, null=True, blank=True)
    member_5_name = models.CharField(max_length=100, null=True, blank=True)
    university_name = models.CharField(max_length=200, null=True, blank=True)
    eligibility = models.BooleanField()


class Startup(BaseModel):
    name = models.CharField(max_length=300)
    user = models.OneToOneField(
        users_models.User, on_delete=models.SET_NULL, related_name="startup", null=True
    )
    applicant = models.OneToOneField(
        Applicant, on_delete=models.SET_NULL, related_name="startup", null=True
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
