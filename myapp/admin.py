from django.contrib import admin
from .models import EtiquetaTarea, Prioridad


class EtiquetaTareaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(EtiquetaTarea, EtiquetaTareaAdmin)
admin.site.register(Prioridad)