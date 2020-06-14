import uuid # Requerida para las instancias de libros únicos

from django.db import models


# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class FilmScreening(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para esta sesión particular")
    screening = models.ForeignKey('cinema.Screening', on_delete=models.PROTECT)
    film = models.ForeignKey('Film', on_delete=models.PROTECT)

    def __str__(self):
        return ' - '.join([self.film.title, self.screening.start_hour.strftime('%H:%M')])
