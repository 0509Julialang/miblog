from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from itinerarios import views as itinerarios_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('agregar_transporte/', views.agregar_transporte, name='agregar_transporte'),
    path('agregar_alojamiento/', views.agregar_alojamiento, name='agregar_alojamiento'),
    path('agregar_actividades/', views.agregar_actividades, name='agregar_actividades'),
    path('buscar/', views.buscar, name='buscar'),
    path('about/', views.about, name='about'),
    ] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     
