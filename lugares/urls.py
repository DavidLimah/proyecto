from django.urls import path
from .views import LugaresListView, LugaresDetailView

urlpatterns = [
	path('', LugaresListView.as_view(), name='lugares_list'),
	path('<int:pk>', LugaresDetailView.as_view(), name='lugares_detail'),
]