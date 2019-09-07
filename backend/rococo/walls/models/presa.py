from django.db import models

from walls.models.sector import Sector


class Presa(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    type = models.IntegerField(blank=True, null=True)  # Cómo conseguir una librería de presas
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()

    def __str__(self):
        return "{} | ({}, {})".format(self.sector, self.x_coord, self.y_coord)


class PresaCatch(models.Model):
    presa = models.ForeignKey(Presa, on_delete=models.CASCADE)
    route = models.ForeignKey("walls.Route", on_delete=models.CASCADE)

    # Agarre: lugar en la presa, ángulo, "bidedo/cazo"?
    x_rel = models.IntegerField()
    y_rel = models.IntegerField()
    angle = models.IntegerField()
