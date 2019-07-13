from django.db import models
from django.conf import settings
from django.utils import timezone

class CurrentStats(models.Model):
    waterIn = models.IntegerField(null=True)
    waterOut = models.IntegerField(null=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.waterIn