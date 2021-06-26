from django.db import models

# Create your models here.
CATEGORIA = [
            ('autos', 'AUTOS'),
            ('celulares', 'CELULARES'),
            ('electrodomesticos', 'ELECTRODOMESTICOS'),
            ('muebles', 'MUEBLES'),
]


class Productos(models.Model):

    Titulo = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50, choices=CATEGORIA, default='default')
    Descripcion = models.TextField()
    Imagen = models.ImageField(upload_to="productos", null = True)
    Precio = models.IntegerField()

    def __str__(self) :
        return self.Titulo

class Contacto(models.Model):

    Mail = models.EmailField()
    Mensaje = models.TextField()

    def __str__(self):
        return self.Mail