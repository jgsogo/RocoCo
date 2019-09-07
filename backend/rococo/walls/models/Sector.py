from django.db import models

from walls.models import Area
from walls.models import Route


class Sector(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT)

    name = models.CharField(max_length=200)
    routes = models.ManyToManyField(Route, related_name="routes_all")  # Crossings can traverse several sectors

    def __str__(self):
        return self.name
