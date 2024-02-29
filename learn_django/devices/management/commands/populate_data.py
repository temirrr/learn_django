from django.core.management.base import BaseCommand
from devices import models


class Command(BaseCommand):
    help = "Populate tables with dummy data"

    def handle(self, *args, **kwargs):
        cheap = models.Tag.objects.create(
            name="cheap", description="Price below USD1000"
        )
        expensive = models.Tag.objects.create(
            name="expensive", description="Price above or equal USD1000"
        )
        korea = models.Tag.objects.create(name="Korea", description="Produced in Korea")
        us = models.Tag.objects.create(name="US", description="Produced in US")

        samsung_a5 = models.Device.objects.create(
            name="Samsung Galaxy A5", category="phone"
        )
        samsung_a5.tags.add(cheap, korea)

        iphone_15 = models.Device.objects.create(name="iPhone 15", category="phone")
        iphone_15.tags.add(expensive, us)

        dell_2720 = models.Device.objects.create(name="Dell U2720Q", category="monitor")
        dell_2720.tags.add(cheap, us)
