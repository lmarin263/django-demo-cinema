from django.shortcuts import render

from .models import Cinema, Auditorium, Film, Screening


# Create your views here.
def index(request):
    # Genera contadores de algunos de los objetos principales
    num_cinemas = Cinema.objects.all().count()
    num_auditoriums = Auditorium.objects.all().count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_cinemas': num_cinemas, 'num_auditoriums': num_auditoriums},
    )
