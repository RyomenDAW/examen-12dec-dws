from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

# Create your models here.



class Usuario(models.Model):    
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    puede_tener_promociones = models.BooleanField()

    def __str__(self):
        return self.nombre
    
class Promocion(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100)
    descripcion_promocion = models.TextField()
    
    #Relacion --> (1 Producto puede tener Varias promociones)
    #Producto de la promoción: El producto debe permitir que tenga promociones (0.75)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,related_name='producto')
    #Usuarios a los que se le aplica la promoción: Los usuarios tienen que ser mayor de edad(0.75)
    #Relacion --> (V)
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuarios')
    descuento = models.PositiveIntegerField()
    fecha_inicio_promocion = models.DateTimeField(default=timezone.now)
    fecha_fin_promocion = models.DateTimeField()
    esta_activa = models.BooleanField(default=True)
    

    

