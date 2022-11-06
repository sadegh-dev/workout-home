from django.db import models
from django.urls import reverse


class doctor(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    the_link = models.URLField(null=True, blank=True)
    pic = models.ImageField(null=True, blank=True, upload_to='doctors/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


