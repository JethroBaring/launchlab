from rest_framework import routers
from users import views

router = routers.SimpleRouter()
router.register(r"", views.UserViewSet)

urlpatterns = router.urls
