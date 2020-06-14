from django.contrib import admin
from .models import Cinema, Auditorium, Screening


# Register your models here.
@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    # list_display = ('start_hour',)
    pass

# admin.site.register(Cinema)
@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# admin.site.register(Auditorium)
@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = ('display_auditorium', 'seat_number', 'description')
