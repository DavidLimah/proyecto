from django.db import models
from django.urls import reverse

# Tablas
class Evento(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=250)
	cover = models.ImageField(upload_to='covers/', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'evento'
		verbose_name_plural = 'eventos'

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('evento_detail', args=[str(self.id)])
