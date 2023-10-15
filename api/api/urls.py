from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from api import views

router = routers.DefaultRouter()
router.register("resources", views.ResourceViewSet)
router.register("stars", views.StarViewSet)
router.register("planets", views.PlanetViewSet)
router.register("moons", views.MoonViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "schema",
        get_schema_view(
            title="Starfield Resources",
            description="REST API to search for resources in Starfield",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "docs",
        TemplateView.as_view(
            template_name="swagger.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="docs",
    ),
]
