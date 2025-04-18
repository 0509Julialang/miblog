from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Perfil

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False

class UserAdminConPerfil(UserAdmin):
    inlines = [PerfilInline]

admin.site.unregister(User)
admin.site.register(User, UserAdminConPerfil)
# Register your models here.
