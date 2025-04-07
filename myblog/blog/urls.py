from . import views
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views 
 
urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.home, name='home'),
     path('login/', views.login_view, name='login'),
     path('logout/', views.logout_view, name='logout'),
     path('registro/', views.registro_view, name='registro'),
     path('perfil/', views.perfil_view, name='perfil'),
     path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
     path('agregar_transporte/', views.agregar_transporte, name='agregar_transporte'),
     path('agregar_alojamiento/', views.agregar_alojamiento, name='agregar_alojamiento'),
     path('agregar_actividades/', views.agregar_actividades, name='agregar_actividades'),
     path('buscar/', views.buscar, name='buscar'),
     path('about/', views.about, name='about'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
