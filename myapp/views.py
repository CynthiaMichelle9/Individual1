from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Tarea
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

    def get(self, request, *args, **kwargs):
       result = []
       if not result:
          pass
       context = {}
       return render(request, self.template_name, context=context)
    
class IngresoView(TemplateView):
  template_name = 'registration/login.html'

  def get(self, request, *args, **kwargs):
    form = LoginForm()
    return render(request, self.template_name, { "form": form })
  
  def post(self, request, *args, **kwargs):
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect('tareas')
      form.add_error('password', 'Nombre de usuario o contraseña incorrectos. Porfavor ingrese nuevamente')
      return render(request, self.template_name, { "form": form })
    else:
      return render(request, self.template_name, { "form": form })
  
class TareasView(TemplateView):
    template_name='tareas.html'

    def get(self, request, *args, **kwargs):
       result = []
       if not result:
          pass
       context = {}
       return render(request, self.template_name, context=context)
  


def login_success(request):
    # Obtén el usuario autenticado
    user = request.user
    
    # Crea un mensaje de bienvenida
    mensaje_bienvenida = f"Bienvenido/a, {user.username}!"
    
    # Redirige a la página deseada con el mensaje de bienvenida como parámetro
    return HttpResponseRedirect('/tareas.html/?mensaje={}'.format(mensaje_bienvenida))


class TareaList(ListView):
   model = Tarea
   context_object_name = "tareas"

class TareaDetalle(DetailView):
   model = Tarea 
   context_object_name = "tarea"
   template_name = "myspp/tarea.html"

class TareaCrear(CreateView):
   model = Tarea
   fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'estado_tarea', 'etiqueta_tarea']
  
   success_url = reverse_lazy("tareas")

class TareaModificar(UpdateView):
   model = Tarea
   fields = "__all__"
   success_url = reverse_lazy("tareas")
