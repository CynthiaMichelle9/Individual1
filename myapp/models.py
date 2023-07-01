from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class EstadoTarea(models.Model):

    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ]

    idestado_tarea = models.IntegerField(primary_key=True)
    estado_tarea = models.CharField(max_length=25, choices=ESTADO_CHOICES, default='Pendiente')

class CategoriaTarea(models.Model):

    CATEGORIA_CHOICES = [
    ('Trabajo', 'Trabajo'),
    ('Hogar', 'Hogar'),
    ('Estudios', 'Estudios'),
    ('Otros', 'Otros')
]
    idetiqueta_tarea = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=25, choices=CATEGORIA_CHOICES, default='Trabajo')
    

class Tarea(models.Model):
    idtarea = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha_vencimiento = models.DateTimeField()
    deleted = models.BooleanField(default=False)
    estado_tarea = models.ForeignKey(EstadoTarea, on_delete=models.CASCADE)
    etiqueta_tarea = models.ForeignKey(CategoriaTarea, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()
