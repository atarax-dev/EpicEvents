from django.conf import settings
from django.db import models

from contract.models import Contract


class Event(models.Model):
    contract = models.ForeignKey(to=Contract, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=12, choices=[("Coming", "Coming"), ("Ended", "Ended")])
    assignee = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True)
    notes = models.TextField(max_length=500, blank=True)
    attendees = models.IntegerField
    date = models.DateTimeField

    def __str__(self):
        return self.contract
