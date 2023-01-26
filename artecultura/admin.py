from django.contrib import admin
from .models import Artecultura

# Registro de modelos Arte cultura
class ArteculturaAdmin(admin.ModelAdmin):
	list_display = ("nombre","descripcion",)


admin.site.register(Artecultura, ArteculturaAdmin)
