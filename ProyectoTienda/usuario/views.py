from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from usuario.forms import RegistroForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

# Create your views here.

from django.shortcuts import render, redirect


class RegistroUsuario(CreateView):
	model = User
	template_name = "register.html"
	form_class = UserCreationForm
	success_url = reverse_lazy('Home')