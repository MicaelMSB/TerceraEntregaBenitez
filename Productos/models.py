from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='imagenproducto', blank=True, null=True)
   
    def __str__(self):
        return f"{self.descripcion} - ${self.precio}"