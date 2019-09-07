from django.db import models


class Degree(models.Model):
    # Degrees according to
    #  https://www.desnivel.com/escalada-roca/conversion-de-grados-y-tablas-de-graduacion/
    # TODO: Decide the pivotal one
    # TODO: Create fixture with the table

    french = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.french
