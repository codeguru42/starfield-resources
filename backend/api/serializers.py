from rest_framework import serializers

from api import models


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        fields = "__all__"


class MoonSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)

    class Meta:
        model = models.Moon
        fields = "__all__"


class PlanetSerializer(serializers.ModelSerializer):
    moons = MoonSerializer(many=True)
    resources = ResourceSerializer(many=True)

    class Meta:
        model = models.Planet
        fields = "__all__"


class StarSerializer(serializers.ModelSerializer):
    planets = PlanetSerializer(many=True)

    class Meta:
        model = models.Star
        fields = "__all__"
