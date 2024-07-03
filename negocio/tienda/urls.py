
from django.urls import path, include
from tienda.views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('chairs/', chairs, name="chairs"),
    path('tables/', tables, name="tables"),
    path('deco/', deco, name="deco"),
]
