from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)


class Device(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    tags = models.ManyToManyField(Tag)
