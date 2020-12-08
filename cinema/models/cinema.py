from django.db import models
from django.urls import reverse
from django.conf import settings


class Cinema(models.Model):
    name = models.CharField(max_length=200)
    city_name = models.CharField(max_length=200)
    city_address = models.CharField(max_length=250)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to=settings.MEDIA_URL, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cinema_detail', args=[str(self.id)])
