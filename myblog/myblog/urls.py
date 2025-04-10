
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views import home
 
urlpatterns = [
     path('admin/', admin.site.urls),
     path('blog/', include('blog.urls')),
     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), 
     path('itinerarios/', include('itinerarios.urls')),
     path('', home), 
 ]
