from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/<int:id>/', views.dashboard, name='dashboard'),
    path('details/<int:id>/', views.details, name='details'),
]

