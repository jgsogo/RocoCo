import uuid

from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices

from walls.models.degree import Degree
from walls.models.presa import Presa, PresaCatch
from walls.models.sector import Sector
from walls.models.seguro import Seguro

ROUTE_TYPE = Choices((0, 'route', _('route')),
                     (1, 'boulder', _('boulder')),
                     (2, 'crossing', _('crossing')))


class Route(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, related_name="route_start_set",
                               help_text=_("Sector where the route is. If it crosses several"
                                           " sectors, then this is where the the route starts"))
    sectors_by = models.ManyToManyField(Sector, related_name="route_all")  # Crossings can traverse several sectors

    type = models.IntegerField(choices=ROUTE_TYPE, default=ROUTE_TYPE.route)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)

    presas = models.ManyToManyField(Presa, through=PresaCatch)
    seguros = models.ManyToManyField(Seguro)

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    # TODO: Validate 'sector' is inside 'sectors_by'
