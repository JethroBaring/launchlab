from rest_framework import routers
from startups import views

router = routers.SimpleRouter()
router.register(r"startups", views.StartupViewSet)
router.register(r"startup-readiness-levels", views.StartupReadinessLevelViewSet)
router.register(
    r"readiness-level-criterion-answers", views.ReadinessLevelCriterionAnswerViewSet
)
router.register(r"urat-question-answers", views.UratQuestionAnswerViewSet)
router.register(r"calculator-question-answers", views.CalculatorQuestionAnswerViewSet)

urlpatterns = router.urls
