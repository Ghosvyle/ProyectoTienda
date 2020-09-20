from django.contrib import admin
from django.urls import path
from usuario import views
from usuario.views import RegistroUsuario

urlpatterns = [
    path('register', RegistroUsuario.as_view(), name="Register"),
]