
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('agregar_transporte/', views.agregar_transporte, name='agregar_transporte'),
    path('agregar_alojamiento/', views.agregar_alojamiento, name='agregar_alojamiento'),
    path('agregar_actividades/', views.agregar_actividades, name='agregar_actividades'),
    path('buscar/', views.buscar, name='buscar'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]



