from django.db import models


class Screening(models.Model):
    film = models.ForeignKey('Film', on_delete=models.PROTECT)
    auditorium = models.ForeignKey('Auditorium', on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)

    # TODO Ver como validar el tiempo en la sesion
    # Si la pelicula dura dos horas y empieza a las cinco, entonces puedo poner una a partir de las siete
    # En el caso anterior, si la pongo a las seis, no me deberia dejar...

    def __str__(self):
        return ' - '.join([self.film.title, self.start_time.strftime('%H:%M')])
