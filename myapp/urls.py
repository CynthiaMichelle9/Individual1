from django.urls import path
from .views import IndexView, IngresoView, TareaList, TareaDetalle, TareaCrear, TareaEditar, TareaEliminar, CompletarTarea
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name='home'),
    path('tareas', TareaList.as_view(), name='tareas'),
    path('tarea/<int:pk>/', TareaDetalle.as_view(), name='tarea'),
    path('crear-tarea/', TareaCrear.as_view(template_name='tarea_form.html'), name = 'crear-tarea'),
    path('editar-tarea/<int:pk>/', TareaEditar.as_view(), name= 'editar-tarea'),
    path('eliminar-tarea/<int:pk>/', TareaEliminar.as_view(), name= 'eliminar-tarea'),
    path('completar-tarea/<int:pk>/', CompletarTarea.as_view(), name='completar-tarea'),
    path('login/', IngresoView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
