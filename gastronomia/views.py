from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Gastronomia

# Registro de vistas
class GastronomiaListView(ListView):
	model = Gastronomia
	context_object_name = 'gastronomia_list'
	template_name = 'gastronomia/gastronomia_list.html'


class GastronomiaDetailView(DetailView):
	model = Gastronomia
	context_object_name = 'gastronomia'
	template_name = 'gastronomia/gastronomia_detail.html'
