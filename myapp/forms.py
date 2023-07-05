from django import forms
from .models import Tarea
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', required=True, max_length=20, min_length=5,
                           error_messages={
                               'required': 'El nombre de usuario es obligatorio',
                               'max_length': 'El nombre de usuario no puede superar los 20 caracteres',
                               'min_length': 'La contraseña debe tener al menos 5 caracteres'
                           },
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Ingrese su nombre de usuario',
                               'class': 'form-control'
                           }))
    password = forms.CharField(label="Contraseña", required=True, max_length=20, min_length=5,
                               error_messages={
                                   'required': 'La contraseña es obligatoria',
                                   'max_length': 'La contraseña no puede superar los 20 caracteres',
                                   'min_length': 'La contraseña debe tener al menos 5 caracteres'
                               },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Ingrese su contraseña', 
                                    'class':'form-control'
                                }), strip=False)
    
class TareaForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'estado_tarea', 'etiqueta_tarea', 'prioridad', 'destinatario']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'})
        }

class ObservacionesForm(forms.Form):
    observaciones = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class': 'form-control observaciones-field', 'rows': 2})
    )