from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

menu = ["Abou site", "All tours", "Help"]

def index(request):
    tours = Tour.objects.all()
    return render(request,'tour/index.html',{'tours':tours,'menu': menu, 'title': 'Main Page'})

def about(request):
    return render(request, 'tour/about.html', {'menu': menu, 'title': 'About Page'})

def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Categories of tours</h1><p>{catid}</p>")