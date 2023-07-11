from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='animalitos_activation')
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
class Subseccion(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    subseccion = models.ForeignKey(Subseccion, on_delete=models.CASCADE)