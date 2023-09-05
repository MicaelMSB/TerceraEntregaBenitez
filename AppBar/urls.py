from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', lista_productos, name="productos"),    
    path('login/', loginView, name="Login"),
    path('registrar/', registrar, name="Registro"),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name="Logout"),
]
