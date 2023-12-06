from rest_framework import routers
from startups import views

router = routers.SimpleRouter()
router.register(r"startups", views.StartupViewSet)
router.register(r"readiness-levels", views.ReadinessLevelViewSet)
router.register(r"initial-readiness-levels", views.InitialReadinessLevelViewSet)

urlpatterns = router.urls
