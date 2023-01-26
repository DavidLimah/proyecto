from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Empresa

# Registro de vistas
class EmpresaListView(ListView):
	model = Empresa
	context_object_name = 'empresa_list'
	template_name = 'empresa/empresa_list.html'

class EmpresaDetailView(DetailView):
	model = Empresa
	context_object_name = 'empresa'
	template_name = 'empresa/empresa_detail.html'
