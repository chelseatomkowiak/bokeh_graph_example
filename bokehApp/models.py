from django.db import models
from django.conf import settings
from django.utils import timezone

class Products(models.Model):

    COLOR =(
        ("WHITE", 'White'),
        ("BLUE", 'Blue'),
        ("BLACK", 'Black'),
        ("GREEN", 'Green'),
    )
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, choices=COLOR)
    price = models.IntegerField()

    def __str__(self):
        return '{}: - {}: - {}:'.format(self.name, self.color, self.price)

class CurrentStats(models.Model):
    waterIn = models.IntegerField(null=True)
    waterOut = models.IntegerField(null=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return '{}: - {}: - {}:'.format(self.waterIn, self.waterOut, self.updated_at)