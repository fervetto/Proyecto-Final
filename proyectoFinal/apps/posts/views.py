from django.shortcuts import render
from .models import Post, Categoria
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy

# Vista basada en funciones

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts' : posts})

#----------------------------------- Vista basada en modelos
#-------------------------------------- CRUD CATEGORIAS
class CrearCategoria(CreateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'posts/agregar_categoria.html'
    success_url = reverse_lazy('index')
    
class ActualizarCategoria(UpdateView):
    model = Categoria
    fields = ['nombre']
    template_name = 'posts/agregar_categoria.html'
    success_url = reverse_lazy('index')
    
class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

#------------------------------------------ CRUD POSTS
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()
    
class CrearPost(CreateView):
    model = Post
    fields = ['titulo','subtitulo', 'texto','categoria','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class ActualizarPost(UpdateView):
    model = Post
    fields = ['titulo','subtitulo','texto','categoria','imagen']
    template_name = 'posts/agregar_post.html'
    success_url = reverse_lazy('index')

class EliminarPost(DeleteView):
    model = Post
    template_name = 'genericos/confirma_eliminar.html'
    success_url = reverse_lazy('index')

class ListarPosts(ListView):
    model = Post
    template_name = 'posts/listar_posts.html'
    context_object_name = 'post'
    
