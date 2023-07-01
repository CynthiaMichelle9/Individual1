from django.urls import path
from .views import IndexView, IngresoView, TareasView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name='home'),
    path('tareas', TareasView.as_view(template_name='tareas.html'), name='tareas'),
    path('login/', IngresoView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
