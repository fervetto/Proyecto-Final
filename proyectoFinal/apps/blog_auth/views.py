from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib import messages

from .forms import RegistrarseForm

class RegistrarseView(FormView):
    template_name = 'users/registrarse.html'
    form_class = RegistrarseForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class IniciarSesionView(LoginView):
    template_name = 'users/iniciar_sesion.html'
    success_url = reverse_lazy('index')

    
# Create your views here.
