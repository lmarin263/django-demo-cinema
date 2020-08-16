from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    length_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
