from django.contrib import admin
from .models import Lugares

# Registro de tablas
class LugaresAdmin(admin.ModelAdmin):
	list_display = ("nombre", "descripcion",)

admin.site.register(Lugares, LugaresAdmin)
