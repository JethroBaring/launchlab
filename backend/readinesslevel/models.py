from django.db import models
from generic.models import BaseModel

from django.utils.translation import gettext_lazy as _


class ReadinessType(BaseModel):
    class RLType(models.TextChoices):
        TECHNOLOGY = "T", _("Technology")
        MARKET = "M", _("Market")
        ACCEPTANCE = "A", _("Acceptance")
        ORGANIZATIONAL = "O", _("Organizational")
        REGULATORY = "R", _("Regulatory")
        INVESTMENT = "I", _("Investment")

    rl_type = models.CharField(choices=RLType.choices, max_length=1)


class ReadinessLevel(BaseModel):
    readiness_type = models.ForeignKey(
        ReadinessType, on_delete=models.CASCADE, related_name="readiness_levels"
    )
    level = models.SmallIntegerField()
    name = models.CharField(max_length=200)


class LevelCriterion(BaseModel):
    readiness_level = models.ForeignKey(
        ReadinessLevel, on_delete=models.CASCADE, related_name="level_criteria"
    )
    criteria = models.CharField(max_length=100)
    excellent_description = models.CharField(max_length=200)
    good_description = models.CharField(max_length=200)
    fair_description = models.CharField(max_length=200)
    poor_description = models.CharField(max_length=200)
    very_poor_description = models.CharField(max_length=200)


class ScoringGuide(BaseModel):
    level_criteria = models.ForeignKey(
        LevelCriterion, on_delete=models.CASCADE, related_name="scoring_guides"
    )
    start_range = models.SmallIntegerField()
    end_range = models.SmallIntegerField()
    description = models.CharField(max_length=200)


class URATQuestion(BaseModel):
    question = models.CharField(max_length=500)
    readiness_type = models.ForeignKey(
        ReadinessType, on_delete=models.CASCADE, related_name="urat_questions"
    )
