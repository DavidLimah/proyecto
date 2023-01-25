from django.test import Client, TestCase
from django.urls import reverse

from .models import Lugares

# Unit Test
class LugaresTests(TestCase):

	def setUp(self):
		self.lugares = Lugares.objects.create(
			nombre='Toro Toro',
			descripcion='Frontera Cochabamba - Potosi',
			)

	def test_lugares_listing(self):
		self.assertEqual(f'{self.lugares.nombre}', 'Toro Toro')
		self.assertEqual(f'{self.lugares.descripcion}', 'Frontera Cochabamba - Potosi')

	def test_lugares_list_view(self):
		response = self.client.get(reverse('lugares_list'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Toro Toro')
		self.assertTemplateUsed(response, 'lugares/lugares_list.html')

	def test_lugares_detail_view(self):
		response = self.client.get(self.lugares.get_absolute_url())
		no_response = self.client.get('/lugares/12345/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'Toro Toro')
		self.assertTemplateUsed(response, 'lugares/lugares_detail.html')