from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class EtiquetaTarea(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Tarea(models.Model):

    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ]

    idtarea = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateTimeField()
    deleted = models.BooleanField(default=False)
    estado_tarea = models.CharField(choices=ESTADO_CHOICES, default='Pendiente')
    etiqueta_tarea = models.ForeignKey(EtiquetaTarea, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Tareas'