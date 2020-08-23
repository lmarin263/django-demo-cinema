from django.views.generic import TemplateView, DetailView

from .models import Cinema


class IndexView(TemplateView):
    template_name = 'index.html'


class CinemaMenuView(TemplateView):
    template_name = 'cinema_menu.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CinemaMenuView, self).get_context_data(*args, **kwargs)
        context['cinemas'] = Cinema.objects.all()
        return context

class CinemaInfoView(DetailView):
    model = Cinema
    paginate_by = 10

class UnderConstructionView(TemplateView):
    template_name = 'under_construction.html'
