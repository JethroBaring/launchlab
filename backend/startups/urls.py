from rest_framework import routers
from startups import views

router = routers.SimpleRouter()
router.register(r"startups", views.StartupViewSet)
router.register(r"startup-readiness-levels", views.StartupReadinessLevelViewSet)
router.register(
    r"readiness-level-criterion-answer", views.ReadinessLevelCriterionAnswerViewSet
)
router.register(r"urat-question-answer", views.UratQuestionAnswerViewSet)

urlpatterns = router.urls
