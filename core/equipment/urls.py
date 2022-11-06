from django.urls import path
from .views import show_tools

app_name = 'equipments'

urlpatterns = [
    path('',show_tools, name='equipments')
]
