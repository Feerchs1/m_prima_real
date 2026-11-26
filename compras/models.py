from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.CharField(max_length=100, default='default.jpg')

    def __str__(self):
        return f"{self.nombre} (Stock: {self.stock})"

# Create your models here.
