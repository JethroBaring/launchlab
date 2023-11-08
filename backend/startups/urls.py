from rest_framework import routers
from startups import views

router = routers.SimpleRouter()
router.register(r"applicants", views.ApplicantViewSet)

urlpatterns = router.urls
