from django.db import models
from django.urls import reverse
import requests
from bs4 import BeautifulSoup


class Store(models.Model):
    name = models.CharField(max_length=200)
    func = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tool(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50,unique=True)
    descriptions = models.TextField(max_length=3000)
    the_link = models.URLField(null=True, blank=True, max_length=5000)
    pic = models.ImageField(null=True, blank=True, upload_to='equipments/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    #############################
    ## Crwaling #################
    #############################

    def get_onlineprice(self):
        # iransporter function
        def iransporter(mylink):
            result = requests.get(mylink)
            content = BeautifulSoup(result.text, 'html.parser')
            price = content.find('span', class_='price')
            return(price.contents[0])

        if self.store.func == 'iransporter' :
            return iransporter(self.the_link)



