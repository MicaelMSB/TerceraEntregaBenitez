from django.db import models

class Producto(models.Model):
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    def __str__(self):
        return self.producto
