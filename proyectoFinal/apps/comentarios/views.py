from django.shortcuts import render
from django.db.models.query import QuerySet
from typing import Any
from django.urls import reverse_lazy
from apps.comentarios.forms import ComentarioForm
from .models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView

def agregar_comentario(request):
    form = ComentarioForm(request.POST)
    if form.is_valid():
        form.save()
        form = ComentarioForm()
        
    template_name = 'comentarios/agregar_comentario.html'
    context = {
        'form' : form,
    }
    
    return render(request, template_name, context)

def comentarios(request):
    comentarios = Comentario.object.all()
    template_name = 'comentarios/listar_comentarios.html'
    context = {
        'comentarios' : comentarios,
        }
    return render (request, template_name, context)
    
    
class ModificarComentario(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields = ['texto',]
    template_name = 'comentarios/agregar_comentario.html'
    success_url = reverse_lazy('posts')
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return queryset.filter(usuario = self.request.user)
    
class EliminarComentario(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('posts')
    
    
    
    