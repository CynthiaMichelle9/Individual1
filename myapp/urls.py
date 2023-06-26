from django.urls import path
from .views import IndexView, IngresoView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name='Home'),
    path('login/', IngresoView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
]
