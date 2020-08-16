from django.db import models
from django.db.models import Max


class Auditorium(models.Model):
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE)
    local_id = models.PositiveIntegerField(blank=True)
    description = models.TextField(max_length=500, blank=True)
    seat_number = models.PositiveIntegerField(default=50)

    def save(self, *args, **kwargs):
        if self.local_id == None:
            max_id = Auditorium.objects.filter(cinema=self.cinema).aggregate(max_id=Max('local_id'))['max_id']
            self.local_id = (max_id if max_id else 0) + 1
        super().save(*args, **kwargs)

    def display_auditorium(self):
        return self.__str__()

    def __str__(self):
        return ' - '.join([self.cinema.name, 'Sala ' + str(self.local_id)])
