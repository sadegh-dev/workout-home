from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=300,unique=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=500, unique=True)
    the_body = RichTextUploadingField(blank=True, null=True)
    release_datetime = models.DateTimeField(default=timezone.now) 
    image_cover = models.ImageField(upload_to="blog/")        
    the_url = models.SlugField(max_length=500 ,unique=True) #En {Ex: whats-is-django} 

    def __str__(self):
        return self.title
