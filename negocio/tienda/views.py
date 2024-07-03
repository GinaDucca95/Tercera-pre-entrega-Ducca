from django.shortcuts import render
from tienda.models import *

def home(request):
    return render(request, "tienda/index.html")

def about(request):
    contexto = {"about": About.objects.all()}
    return render(request, "tienda/about.html", contexto)

def chairs(request):
    return render(request, "tienda/chairs.html")

def tables(request):
    return render(request, "tienda/tables.html")

def deco(request):
    return render(request, "tienda/deco.html")