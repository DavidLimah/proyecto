from django.urls import path

from .views import ArteculturaListView, ArteculturaDetailView

# Registrar urls
urlpatterns = [
	path('', ArteculturaListView.as_view(), name='artecultura_list'),
	path('<int:pk>', ArteculturaDetailView.as_view(), name='artecultura_detail'),
]