from django.contrib import admin
from .models import Empresa

# Registro de modelos
class EmpresaAdmin(admin.ModelAdmin):
	list_display = ("nombre","descripcion")

admin.site.register(Empresa, EmpresaAdmin)
