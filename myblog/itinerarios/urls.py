from django.urls import path
from . import views

app_name = 'itinerarios' 

urlpatterns = [
    path('', views.lista_itinerarios, name='lista'),  # Esta ya funciona como página principal
    path('nuevo/', views.crear_itinerario, name='nuevo'),
    path('<int:pk>/', views.detalle_itinerario, name='detalle_itinerario'),
    path('<int:pk>/editar/', views.editar_itinerario, name='editar_itinerario'),
    path('<int:pk>/eliminar/', views.eliminar_itinerario, name='eliminar_itinerario'),
]