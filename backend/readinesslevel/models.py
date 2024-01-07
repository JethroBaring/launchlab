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
        COMMERCIALIZATION = "C", _("Commercialization")

    rl_type = models.CharField(choices=RLType.choices, max_length=1)


class ReadinessLevel(BaseModel):
    readiness_type = models.ForeignKey(
        ReadinessType, on_delete=models.CASCADE, related_name="readiness_levels"
    )
    level = models.SmallIntegerField()
    name = models.CharField(max_length=500)


class LevelCriterion(BaseModel):
    readiness_level = models.ForeignKey(
        ReadinessLevel, on_delete=models.CASCADE, related_name="level_criteria"
    )
    criteria = models.CharField(max_length=100)
    excellent_description = models.CharField(max_length=500)
    good_description = models.CharField(max_length=500)
    fair_description = models.CharField(max_length=500)
    poor_description = models.CharField(max_length=500)
    very_poor_description = models.CharField(max_length=500)


class ScoringGuide(BaseModel):
    readiness_level = models.ForeignKey(
        ReadinessLevel, on_delete=models.CASCADE, related_name="scoring_guides"
    )
    start_range = models.SmallIntegerField()
    end_range = models.SmallIntegerField()
    description = models.CharField(max_length=700)


class URATQuestion(BaseModel):
    question = models.CharField(max_length=500)
    readiness_type = models.ForeignKey(
        ReadinessType, on_delete=models.CASCADE, related_name="urat_questions"
    )


class CalculatorCategory(BaseModel):
    category = models.CharField(max_length=200)
    readiness_type = models.ForeignKey(
        ReadinessType, on_delete=models.CASCADE, related_name="calculator_categories"
    )


class CalculatorQuestion(BaseModel):
    question = models.CharField(max_length=500)
    score = models.SmallIntegerField()
    category = models.ForeignKey(
        CalculatorCategory, on_delete=models.CASCADE, related_name="questions"
    )
