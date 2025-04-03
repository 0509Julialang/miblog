from . import views
from django.urls import path
 
urlpatterns = [
     path('', views.home, name='home'),
     path('agregar_transporte/', views.agregar_transporte, name='agregar_transporte'),
     path('agregar_alojamiento/', views.agregar_alojamiento, name='agregar_alojamiento'),
     path('agregar_actividades/', views.agregar_actividades, name='agregar_actividades'),
     path('buscar/', views.buscar, name='buscar'),
 ]