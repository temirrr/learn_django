from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseNotAllowed
from . import models


# Create your views here.
def get_devices(request: HttpRequest) -> HttpResponse:
    if request.method != "GET":
        # Return 405 Method Not Allowed for unsupported methods
        return HttpResponseNotAllowed(["GET"])

    name = request.GET.get("name")
    category = request.GET.get("category")
    tags = request.GET.get("tags")

    devices = models.Device.objects

    if name:
        devices = devices.filter(name__icontains=name)

    if category:
        devices = devices.filter(category__iexact=category)

    if tags:
        tags_arr = [tag.strip() for tag in tags.split(",")]
        for tag in tags_arr:
            devices = devices.filter(tags__name__iexact=tag)

    # Using "all" to ensure execution of the queryset
    devices = devices.all()

    return render(request, "get_devices.html", {"devices": devices})
