from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Artecultura

# Registrar vistas
class ArteculturaListView(ListView):
	model = Artecultura
	context_object_name = 'artecultura_list'
	template_name = 'artecultura/artecultura_list.html'

class ArteculturaDetailView(DetailView):
	model = Artecultura
	context_object_name = 'artecultura'
	template_name = 'artecultura/artecultura_detail.html'