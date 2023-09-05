from django.db import models

class Producto(models.Model):
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()

class Inicio(models.Model):
    "inicio"

