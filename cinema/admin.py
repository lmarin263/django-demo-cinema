from django.contrib import admin
from .models import Cinema, Auditorium, Film, Screening, Offer


# Register your models here.
@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city_name', 'city_address', 'description')

@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = ('display_auditorium', 'seat_number', 'description')

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('film', 'auditorium', 'start_time')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'offer', 'value')
