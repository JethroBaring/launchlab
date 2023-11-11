from rest_framework import routers
from startups import views

router = routers.SimpleRouter()
router.register(r"applicants", views.ApplicantViewSet)
router.register(r"startups", views.StartupViewSet)
router.register(r"readiness-levels", views.ReadinessLevelViewSet)

urlpatterns = router.urls
