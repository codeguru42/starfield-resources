from rest_framework import viewsets

from api import models, serializers


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.ResourceSerializer


class StarViewSet(viewsets.ModelViewSet):
    queryset = models.Star.objects.all()
    serializer_class = serializers.StarSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = models.Planet.objects.all()
    serializer_class = serializers.PlanetSerializer


class MoonViewSet(viewsets.ModelViewSet):
    queryset = models.Moon.objects.all()
    serializer_class = serializers.MoonSerializer
