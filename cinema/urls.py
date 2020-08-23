from django.conf.urls import url

from .views import *


urlpatterns = [
    url(r'index', IndexView.as_view(), name='index'),
    url(r'cinemas', CinemaMenuView.as_view(), name='cinema_menu'),
    url(r'cinema/(?P<pk>\d+)', CinemaInfoView.as_view(), name='cinema_detail'),
    url('', UnderConstructionView.as_view(), name='under_construction'),
]
