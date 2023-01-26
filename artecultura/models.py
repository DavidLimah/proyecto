from django.db import models
from django.urls import reverse

# Tablas Arte y cultura
class Artecultura(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=250)
	# cover = models.ImageField(upload_to='covers/')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'arte y cultura'
		verbose_name_plural = 'artes y cultura'

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('artecultura_detail', kwargs={'pk': str(self.pk)})
