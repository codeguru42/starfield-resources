from django.db import models


class Star(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField
