"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from startups.urls import urlpatterns as startups_urlpatterns
from users.urls import urlpatterns as users_urlpatterns
from readinesslevel.urls import urlpatterns as readinesslevels_urlpatterns
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from .settings import (
    STATIC_ROOT,
    STATIC_URL,
)
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(startups_urlpatterns)),
    path("user/", include(users_urlpatterns)),
    path("readinesslevel/", include(readinesslevels_urlpatterns)),
    path("tokens/acquire/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("tokens/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


schema_view = get_schema_view(
    openapi.Info(
        title="LaunchLab API",
        default_version="v1",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns.append(
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
)
urlpatterns.append(
    path(
        "docs/",
        TemplateView.as_view(
            template_name="redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="redoc",
    )
)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
