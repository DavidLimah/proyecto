from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Lugares

# Registro de vistas
class LugaresListView(ListView):
	model = Lugares
	context_object_name = 'lugares_list'
	template_name = 'lugares/lugares_list.html'

class LugaresDetailView(DetailView):
	model = Lugares
	context_object_name = 'lugares'
	template_name = 'lugares/lugares_detail.html'