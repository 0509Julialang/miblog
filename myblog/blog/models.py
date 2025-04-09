from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Transporte(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Actividades(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()  # Duración en horas
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'my_custom_blog_actividades'

    def __str__(self):
        return self.nombre
    
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(default='default.jpg', upload_to='perfil_pics')
    bio = models.TextField(max_length=500, blank=True)
    ubicacion = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

# Crear/actualizar el perfil automáticamente
#@receiver(post_save, sender=User)
#def crear_perfil_usuario(sender, instance, created, **kwargs):
#    if created:
#       Perfil.objects.create(usuario=instance)

#@receiver(post_save, sender=User)
#def guardar_perfil_usuario(sender, instance, **kwargs):
#    instance.perfil.save()    