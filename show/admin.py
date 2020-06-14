from django.contrib import admin
from .models import Film, FilmScreening


# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(FilmScreening)
class FilmScreeningAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'screening')
