from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class TipoMaterial(models.Model):
	nombre = models.CharField(max_length = 20)

	def __str__(self):
		return self.nombre

class Bodega(models.Model):
	nombre = models.CharField(max_length = 30)
	user = models.OneToOneField(User, null = True, blank = True)
	direccion = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre

class BodegaMaterial(models.Model):
	material = models.ForeignKey(TipoMaterial)
	precio = models.DecimalField(max_digits = 11, decimal_places = 2, blank = True, null = True)
	bodega = models.ForeignKey(Bodega)

	def __str__(self):
		return self.bodega.nombre

class SolicitudUser(models.Model):
	user = models.ForeignKey(User)
	bodega_material = models.ForeignKey(BodegaMaterial)
	peso_aprox = models.DecimalField(max_digits = 11, decimal_places = 2)
	fecha = models.DateField(default = datetime.now)