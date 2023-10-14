from django.db import models


class Star(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField


class Planet(models.Model):
    name = models.CharField(max_length=255)
    star = models.ForeignKey(Star, on_delete=models.PROTECT, null=False)
    extreme_environment = models.BooleanField()


class Moon(models.Model):
    name = models.CharField(max_length=255)
    planet = models.ForeignKey(Planet, on_delete=models.PROTECT, null=False)
    extreme_environment = models.BooleanField()


class Resource(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
