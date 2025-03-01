
from django.urls import path
from . import views


# localhost
urlpatterns = [
    path('', views.all_superhero, name='all_superhero'),

]