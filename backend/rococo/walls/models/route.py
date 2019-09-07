import uuid

import jsonfield
from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices

from walls.models import Degree

ROUTE_TYPE = Choices((0, 'route', _('route')),
                     (1, 'boulder', _('boulder')),
                     (2, 'crossing', _('crossing')))


class Route(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    sector = models.ForeignKey("walls.Sector", on_delete=models.PROTECT,
                               help_text=_("Sector where the route is. If it crosses several"
                                           " sectors, then this is where the the route starts"))
    type = models.IntegerField(choices=ROUTE_TYPE, default=ROUTE_TYPE.route)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT)

    presas = jsonfield.JSONField(blank=True, help_text=_("List of coordinates"))  # TODO: translate
    seguros = jsonfield.JSONField(blank=True, help_text=_("List of coordinates"))  # TODO: translate

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    # TODO: Validate 'sector' is inside 'sector_set'
