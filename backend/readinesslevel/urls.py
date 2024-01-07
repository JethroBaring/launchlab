from rest_framework import routers
from readinesslevel import views

router = routers.SimpleRouter()
router.register(r"readiness-levels", views.ReadinessLevelViewSet)
router.register(r"urat-questions", views.UratQuestionViewSet)
router.register(r"calculator-categories", views.CalculatorCategoryViewSet)

urlpatterns = router.urls
