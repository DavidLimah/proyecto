from django.contrib import admin
from .models import Gastronomia

# Registro de modelos Gastronomía
class GastronomiaAdmin(admin.ModelAdmin):
	list_display = ("nombre","descripcion",)

admin.site.register(Gastronomia, GastronomiaAdmin)
