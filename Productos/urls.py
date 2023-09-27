from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    path('cargar_producto/', views.cargar_producto, name='cargar_producto'),
    path('actualizar_producto/<int:id_producto>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('', views.lista_productos, name='lista_productos'),
]