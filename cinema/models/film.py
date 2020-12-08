from django.db import models
from django.urls import reverse


class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    length_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', args=[str(self.id)])
