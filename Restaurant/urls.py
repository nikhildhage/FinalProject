from django.urls import path
from . import views

# Restaurant Urls
urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("locations", views.locations, name="locations"),
    path("reservations", views.reservations, name="reservations"),
    path("giftcards", views.giftcards, name="giftcards"),
    path("contact", views.contact, name="contact"),
]