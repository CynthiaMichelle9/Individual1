from django.contrib import admin
from django import forms
from .models import CategoriaTarea
from . import models

# Register your models here.
class CategoriaTareaAdmin(admin.ModelAdmin):
    list_display = ['idetiqueta_tarea', 'nombre_categoria']
    list_filter = ['nombre_categoria']
    search_fields = ['nombre_categoria']

formfield_overrides = {
        models.CharField: {'widget': forms.Select(choices=CategoriaTarea.CATEGORIA_CHOICES)},
    }
admin.site.register(CategoriaTarea, CategoriaTareaAdmin)