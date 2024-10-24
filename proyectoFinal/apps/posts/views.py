from django.shortcuts import render, redirect
from .models import Post, Categoria
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from mixins.custom_test_mixin import CustomTestMixin
from apps.comentarios.models import Comentario
from apps.comentarios.forms import ComentarioForm
from django.http.response import HttpResponseRedirect
from django.db.models.query import QuerySet
# Vista basada en funciones

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts' : posts})

#----------------------------------- Vista basada en modelos
#-------------------------------------- CRUD CATEGORIAS
class CrearCategoria(LoginRequiredMixin, CustomTestMixin, CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'posts/agregar_categoria.html'
    success_url = reverse_lazy('index')
    
class ActualizarCategoria(UpdateView, CustomTestMixin):
    model = Categoria
    fields = ['nombre']
    template_name = 'posts/agregar_categoria.html'
    success_url = reverse_lazy('index')
    
class EliminarCategoria(DeleteView, CustomTestMixin):
    model = Categoria
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

#------------------------------------------ CRUD POSTS
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'posts/post_individual.html'
#     context_object_name = 'posts'
#     pk_url_kwarg = 'id'
#     queryset = Post.objects.all()
    
class CrearPost(CreateView, CustomTestMixin):
    model = Post
    fields = ['titulo','subtitulo', 'texto','categoria','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class ActualizarPost(UpdateView, CustomTestMixin):
    model = Post
    fields = ['titulo','subtitulo','texto','categoria','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class EliminarPost(DeleteView, CustomTestMixin):
    model = Post
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

class ListarPosts(ListView):
    model = Post
    template_name = 'posts/listar_posts.html'
    context_object_name = 'post'
    
def detalle_post(request,id):
    post = Post.objects.get(id = id)
    comentarios = Comentario.objects.filter(post = id)
    form = ComentarioForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.post = post
            aux.usuario = request.user
            aux.save()
            form = ComentarioForm()
        else:
            return redirect('apps.blog_auth:iniciar_sesion')

    context= {
        "post": post,
        "form" : form, 
        "comentarios" : comentarios
    }
    template_name = "posts/post_individual.html"

    return render(request, template_name=template_name,context=context)
