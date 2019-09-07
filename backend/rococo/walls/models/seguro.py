from django.db import models

from walls.models.sector import Sector


class Seguro(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    type = models.IntegerField(blank=True, null=True)  # Cómo conseguir una librería de seguros
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()
