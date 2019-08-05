from django.urls import path
from django.urls import include
from .views import home_visit

urlpatterns = [
    path('', home_visit),
]
