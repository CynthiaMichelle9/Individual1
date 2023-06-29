from django.contrib import admin
from django import forms
from .models import CategoriaTarea, Tarea, EstadoTarea
from . import models
from django.db import models

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre_categoria']
    list_filter = ['nombre_categoria']
    search_fields = ['nombre_categoria']

formfield_overrides = {
        models.CharField: {'widget': forms.Select(choices=CategoriaTarea.CATEGORIA_CHOICES)},
    }
admin.site.register(CategoriaTarea, CategoriaAdmin)

#class TareaAdmin(admin.ModelAdmin):
#    list_display = ['titulo', 'descripcion', 'fecha_vencimiento', 'estado_tarea', 'etiqueta_tarea', 'user']
#    list_filter = ['estado_tarea', 'etiqueta_tarea']
#    search_fields = ['titulo', 'descripcion', 'user__username']
#
#    def usuario(self, obj):
#        return obj.user.username
#    usuario.short_description = 'Usuario'   
#    
#    def titulo(self, obj):
#        return obj.titulo
#    titulo.short_description = 'Título'
#
#    def descripcion(self, obj):
#        return obj.descripcion
#    descripcion.short_description = 'Descripción'
#
#    def fecha_vencimiento(self, obj):
#        return obj.fecha_vencimiento
#    fecha_vencimiento.short_description = 'Fecha de Vencimiento'
#
#    def estado(self, obj):
#        return obj.estado_tarea.estado_tarea
#    estado.short_description = 'Estado'
#
#    def etiqueta(self, obj):
#        return obj.etiqueta_tarea.nombre_categoria
#    etiqueta.short_description = 'Etiqueta'
#
#
#admin.site.register(Tarea, TareaAdmin)
#
#class EstadoTareaAdmin(admin.ModelAdmin):
#    list_display = ['estado_tarea']
#    list_filter = ['estado_tarea']
#    search_fields = ['estado_tarea']
#
#formfield_overrides = {
#        models.CharField: {'widget': forms.Select(choices=EstadoTarea.ESTADO_CHOICES)},
#    }
#admin.site.register(EstadoTarea, EstadoTareaAdmin)
#
