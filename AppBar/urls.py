from django.urls import path
from AppBar.views import *
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='productos'),

]
