from django.contrib import admin
from .models import EtiquetaTarea

class EtiquetaTareaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(EtiquetaTarea, EtiquetaTareaAdmin)

