from .models import Producto
from django.shortcuts import render


# Create your views here.

def inicio(req):
    return render(req, 'inicio.html')

def lista_productos(req):
    productos = Producto.objects.all()
    return render(req, 'productos.html', {'Producto': productos})



