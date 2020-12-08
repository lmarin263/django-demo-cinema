from django.db import models
from django.urls import reverse
from django.conf import settings

from enum import Enum
from decimal import Decimal


class OfferChoice(Enum):
    PERCENTAGE = "Percentage"
    REDUCTION = "Reduction"

class Offer(models.Model):
    name = models.CharField(max_length=200)
    offer = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in OfferChoice])
    value = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.0'))
    description = models.TextField(max_length=500, blank=True)
    # TODO Fecha de caducidad

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('offer_detail', args=[str(self.id)])
