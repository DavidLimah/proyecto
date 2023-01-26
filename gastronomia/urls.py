from django.urls import path

from .views import GastronomiaListView, GastronomiaDetailView

# Registrar urls
urlpatterns = [
	path('', GastronomiaListView.as_view(), name='gastronomia_list'),
	path('<int:pk>', GastronomiaDetailView.as_view(), name='gastronomia_detail'),
]