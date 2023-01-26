from django.urls import path
from .views import EventoListView, EventoDetailView

urlpatterns = [
	path('', EventoListView.as_view(), name='evento_list'),
	path('<int:pk>', EventoDetailView.as_view(), name='evento_detail'),
]