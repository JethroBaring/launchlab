from rest_framework import routers
from readinesslevel import views

router = routers.SimpleRouter()
router.register(r"readiness-level", views.ReadinessLevelViewSet)
router.register(r"urat-questions", views.UratQuestionViewSet)

urlpatterns = router.urls
