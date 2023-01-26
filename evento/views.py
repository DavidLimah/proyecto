from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Evento

# Registro de vistas
class EventoListView(ListView):
	model = Evento
	context_object_name = 'evento_list'
	template_name = 'evento/evento_list.html'


class EventoDetailView(DetailView):
	model = Evento
	context_object_name = 'evento'
	template_name = 'evento/evento_detail.html'
