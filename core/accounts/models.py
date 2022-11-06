from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager
from django.conf import settings


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    full_name = models.CharField(max_length=200)
    weight = models.PositiveSmallIntegerField(null=True, blank=True) 
    height = models.PositiveSmallIntegerField(null=True, blank=True) 
    birth_year = models.PositiveSmallIntegerField(null=True, blank=True)
    type_gender = (
        ('m','مرد'),
        ('f','زن')
    )
    gender = models.CharField(null=True, blank=True, max_length=1, choices=type_gender, default='m')
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',]
    objects = MyUserManager()

    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse('accounts:dashboard', args=[self.id,])


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

