from unicodedata import name
from django.urls import path

from app import admin
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("home", views.home, name='home'), 
    path("tracks", views.tracks, name='minor tracks'),
    path("apply", views.login, name='apply'),
    path("details", views.details, name="details"),
    path("BigPP", views.team, name="BigPP"),
    ]