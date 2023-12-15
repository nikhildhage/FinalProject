from django.urls import path
from . import views

# Pacific Trails Resort Urls
urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.yurts, name="menu"),
    path("reservations", views.yurts, name="menu"),
    path("giftCards", views.reservations, name="giftcard"),
    path("contact", views.details, name="contact"),
]