from django.db import models

# Create your models here.

class Rubro(models.Model):
	nombre = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 100, null = False)

	def __str__(self):
		return self.nombre


class Producto(models.Model):
	nombre = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 100, null = False)
	precio = models.DecimalField(max_digits=5, decimal_places=2)
	stock = models.IntegerField()
	rubro = models.ForeignKey(Rubro, on_delete = models.CASCADE )
	imagen = models.ImageField(upload_to = 'imagenes_productos', null = True)

	def __str__(self):
		return self.nombre