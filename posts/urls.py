from django.urls import path

from home.views import AboutPageView
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
]

