from django.shortcuts import render
from doctor.models import doctor
from equipment.models import Tool
from service.models import Service
from blog.models import Post


def home(request):
    posts = Post.objects.all()
    services = Service.objects.all()
    doctors = doctor.objects.all()[::-1][:3]
    tools = Tool.objects.all()[::-1][:6]
    context = {
        'doctors' : doctors ,
        'tools' : tools ,
        'services' : services ,
        'posts':posts ,
    }
    return render(request, 'home/index.html', context)

