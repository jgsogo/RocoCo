from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices

from walls.models.route import Route

# TODO: Terminology
REPETITION1_TYPE = Choices((0, 'pie_libre', _('Pie libre')),
                           (1, 'pie_mano', _('Pie mano')),)

REPETITION2_TYPE = Choices((0, 'vista', _('A vista')),
                           (1, 'flash', _('Flash')),)


class Repetition(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    route = models.ForeignKey(Route, on_delete=models.PROTECT)
    rep1 = models.IntegerField(REPETITION1_TYPE, blank=True)
    rep2 = models.IntegerField(REPETITION2_TYPE, blank=True)

    class Meta:
        ordering = ['-datetime', '-timestamp']
