from django.urls import path
from .views import IndexView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name='Home'),
    path('login/', LoginView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
]
