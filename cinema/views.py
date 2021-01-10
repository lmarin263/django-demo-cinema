from django.views.generic import TemplateView, DetailView

from .models import Cinema, Film, Offer


class IndexView(TemplateView):
    template_name = 'index.html'

class AboutUsView(TemplateView):
    template_name = 'about_us.html'

class CinemaMenuView(TemplateView):
    template_name = 'cinema_menu.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CinemaMenuView, self).get_context_data(*args, **kwargs)
        context['cinemas'] = Cinema.objects.all()
        return context

class CinemaInfoView(DetailView):
    model = Cinema
    paginate_by = 10

class FilmMenuView(TemplateView):
    template_name = 'film_menu.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FilmMenuView, self).get_context_data(*args, **kwargs)
        context['films'] = Film.objects.all()
        return context

class FilmInfoView(DetailView):
    model = Film
    paginate_by = 10

class OfferMenuView(TemplateView):
    template_name = 'offer_menu.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OfferMenuView, self).get_context_data(*args, **kwargs)
        context['offers'] = Offer.objects.all()
        return context

class OfferInfoView(DetailView):
    model = Offer
    paginate_by = 10
