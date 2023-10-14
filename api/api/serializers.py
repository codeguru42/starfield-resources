from rest_framework import serializers

from api import models


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resource
        fields = "__all__"


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Star
        fields = "__all__"


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Planet
        fields = "__all__"


class MoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Moon
        fields = "__all__"
