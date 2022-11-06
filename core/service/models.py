from django.db import models
from django.urls import reverse


class Service(models.Model):
    logo = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    descriptions = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


