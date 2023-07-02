from typing import Any, Dict
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import LoginForm, TareaForm, ObservacionesForm
from .models import Tarea, EtiquetaTarea
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import View
from django.db.models import Q
from datetime import datetime
from django.views.generic.edit import FormMixin


# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

    def get(self, request, *args, **kwargs):
       result = []
       if not result:
          pass
       context = {}
       return render(request, self.template_name, context=context)
    
class IngresoView(LoginView, LoginRequiredMixin):
  template_name = 'registration/login.html'
  fields = "__all__"
  redirect_authenticated_user = True


  def get_success_url(self):
    return reverse_lazy('tareas')
  
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


class TareaList(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'
    ordering = ['-fecha_vencimiento']
    template_name = 'tarea_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user, deleted=False)

        fecha_vencimiento = self.request.GET.get('fecha_vencimiento')
        estado_tarea = self.request.GET.get('estado_tarea')
        titulo = self.request.GET.get('titulo')
        etiqueta_tarea = self.request.GET.get('etiqueta_tarea')

        if fecha_vencimiento:
          try:
            fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%B %d, %Y").strftime("%Y-%m-%d")
            queryset = queryset.filter(fecha_vencimiento=fecha_vencimiento)
          except ValueError:
            pass
        if estado_tarea:
            queryset = queryset.filter(estado_tarea=estado_tarea)
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        if etiqueta_tarea:
            queryset = queryset.filter(etiqueta_tarea=etiqueta_tarea)

        return queryset
       
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tareas"] = context["tareas"].filter(user = self.request.user)
        context["count"] = context["tareas"].count()
        context['fechas_vencimiento'] = Tarea.objects.filter(user=self.request.user).values_list('fecha_vencimiento', flat=True).distinct()
        context['estados_tarea'] = Tarea.objects.filter(user=self.request.user).values_list('estado_tarea', flat=True).distinct()
        context['titulos'] = Tarea.objects.filter(user=self.request.user).values_list('titulo', flat=True).distinct()
        context['etiquetas_tarea'] = EtiquetaTarea.objects.all()
        return context
    

class TareaDetalle(LoginRequiredMixin, FormMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'tarea.html'
    form_class = ObservacionesForm

    def get_success_url(self):
        return reverse_lazy('tareas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tarea = self.object
        observaciones = tarea.observaciones
        form = self.get_form()
        form.initial['observaciones'] = observaciones
        context['observaciones_form'] = form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            self.object.observaciones = form.cleaned_data['observaciones']
            self.object.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

class TareaCrear(CreateView, LoginRequiredMixin):
   model = Tarea
   form_class = TareaForm
   success_url = reverse_lazy("tareas")

   def form_valid(self, form):
    form.instance.user = self.request.user
    return super(TareaCrear, self).form_valid(form)    
    
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['form'] = self.get_form()
      return context
   
class TareaEditar(UpdateView, LoginRequiredMixin):
   model = Tarea
   form_class = TareaForm
   success_url = reverse_lazy("tareas")

class TareaEliminar(DeleteView, LoginRequiredMixin):
   model = Tarea
   success_url = reverse_lazy("tareas")
   context_object_name = 'tarea' 

   def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class CompletarTarea(LoginRequiredMixin, View):
    def post(self, request, pk):
        tarea = Tarea.objects.get(pk=pk)
        tarea.estado_tarea = 'Completada'
        tarea.save()
        return redirect('tareas')