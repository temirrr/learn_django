from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_devices, name="get_devices"),
]
