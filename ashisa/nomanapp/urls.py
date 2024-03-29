
from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("contact.html/", views.contact, name="contact"),
    path("about.html/", views.about, name="about"),
    path("services.html/", views.services, name="services"),
    path("appointment.html/", views.appointment, name="appointment"),
    path("thank_you.html/", views.thank_you, name="thank_you"),
]
