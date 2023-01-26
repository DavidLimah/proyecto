from django.contrib import admin
from .models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
	list_display = ("nombre","descripcion",)

admin.site.register(Evento, EventoAdmin)