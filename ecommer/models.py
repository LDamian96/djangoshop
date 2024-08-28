from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    precio=models.DecimalField(max_digits=9,decimal_places=2)
    fecha_Registro=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to="productos",blank=True)
    
    def __str__(self):
        return self.nombre