from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blog import views as blog_views
from itinerarios import views as itinerarios_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal
    path('', blog_views.home, name='home'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Cierra sesión y redirige

    path('registro/', blog_views.registro_view, name='registro'),

    # Perfil
    path('perfil/', blog_views.perfil, name='perfil'),
    path('perfil/editar/', blog_views.editar_perfil, name='editar_perfil'),
    path('detalle_perfil/', blog_views.detalle_perfil, name='detalle_perfil'),

    # Funcionalidades del blog
    path('agregar_transporte/', blog_views.agregar_transporte, name='agregar_transporte'),
    path('agregar_alojamiento/', blog_views.agregar_alojamiento, name='agregar_alojamiento'),
    path('agregar_actividades/', blog_views.agregar_actividades, name='agregar_actividades'),
    path('buscar/', blog_views.buscar, name='buscar'),
    path('about/', blog_views.about, name='about'),

    # Itinerarios
    path('itinerarios/', include('itinerarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

