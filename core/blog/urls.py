from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<slug:catname>/', views.category_list_view, name='category'),
    path('tag/<slug:catname>/<slug:tagname>/', views.tag_list_view, name='tag'),
    path('<slug:myurl>/', views.post_details_view, name='post-details'),
] 