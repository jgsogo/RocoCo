from django.db import models

from walls.models.area import Area


class Sector(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
