from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'cinemas', CinemaMenuView.as_view(), name='cinema_menu'),
    url(r'cinema/(?P<pk>\d+)', CinemaInfoView.as_view(), name='cinema_detail'),
    url(r'', IndexView.as_view(), name='index'),
]
