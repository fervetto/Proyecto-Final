from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Vista basada en funciones

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts' : posts})

class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
# Create your views here.

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_individual.html'
    context_object_name = 'posts'
    pk_url_kwarg = 'id'
    queryset = Post.objects.all()