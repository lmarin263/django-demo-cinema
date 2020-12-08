from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'about-us', AboutUsView.as_view(), name='about_us'),
    url(r'cinemas', CinemaMenuView.as_view(), name='cinema_menu'),
    url(r'cinema/(?P<pk>\d+)', CinemaInfoView.as_view(), name='cinema_detail'),
    url(r'films', FilmMenuView.as_view(), name='film_menu'),
    url(r'film/(?P<pk>\d+)', FilmInfoView.as_view(), name='film_detail'),
    url(r'offers', OfferMenuView.as_view(), name='offer_menu'),
    url(r'offer/(?P<pk>\d+)', OfferInfoView.as_view(), name='offer_detail'),
    url(r'', IndexView.as_view(), name='index'),
]
