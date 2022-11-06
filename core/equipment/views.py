from django.shortcuts import render
from .forms import SearchEquipForm


from .models import Tool

def show_tools(request):
    form = SearchEquipForm()
    tools = Tool.objects.all()
    tools_s = None
    if 'search' in request.GET:
        cd = request.GET['search']
        tools_s = Tool.objects.filter(name__icontains = cd)
    if tools_s :
        tools = tools_s
    context = {
        'tools': tools ,
        'form': form ,
    }
    return render(request,'equipment/equi.html', context)




