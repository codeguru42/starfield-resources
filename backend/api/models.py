from django.db import models


class Resource(models.Model):
    RARITY = (
        (0, "common"),
        (1, "uncommon"),
        (2, "rare"),
        (3, "exotic"),
        (4, "unique"),
    )
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
    rarity = models.IntegerField(choices=RARITY)


class Star(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField()


class Planet(models.Model):
    name = models.CharField(max_length=255)
    star = models.ForeignKey(
        Star, on_delete=models.PROTECT, null=False, related_name="planets"
    )
    extreme_environment = models.BooleanField()
    resources = models.ManyToManyField(Resource)


class Moon(models.Model):
    name = models.CharField(max_length=255)
    planet = models.ForeignKey(
        Planet, on_delete=models.PROTECT, null=False, related_name="moons"
    )
    extreme_environment = models.BooleanField()
    resources = models.ManyToManyField(Resource)
