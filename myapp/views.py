from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
          return redirect('Home')
      form.add_error('password', 'Nombre de usuario o contraseña incorrectos. Porfavor ingrese nuevamente')
      return render(request, self.template_name, { "form": form })
    else:
      return render(request, self.template_name, { "form": form })
    