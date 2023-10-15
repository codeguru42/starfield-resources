from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register("resources", views.ResourceViewSet)
router.register("stars", views.StarViewSet)
router.register("planets", views.PlanetViewSet)
router.register("moons", views.MoonViewSet)

urlpatterns = [path("", include(router.urls))]
