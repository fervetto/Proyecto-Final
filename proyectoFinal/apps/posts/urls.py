from django.urls import path
from .views import CrearCategoria, ActualizarCategoria, EliminarCategoria, PostListView, detalle_post, CrearPost, ActualizarPost, EliminarPost, ListarPosts
from . import views

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:id>', detalle_post, name= 'post'),
    # path('posts/post_detalle/<int:id>/', PostDetailView.as_view(), name= 'Post_detalle'),
    

    
    
    path("agregar_categoria/", CrearCategoria.as_view(), name= 'agregar_categoria'),
    path("actualizar_categoria/<int:pk>", ActualizarCategoria.as_view(), name = 'actualizar_categoria'),
    path("eliminar_categoria/<int:pk>", EliminarCategoria.as_view(), name= 'eliminar_categoria'),
    
    
    path("agregar_post/", CrearPost.as_view(), name= 'agregar_post'),    
    path("actualizar_post/<int:pk>", ActualizarPost.as_view(), name = 'actualizar_post'),
    path("eliminar_post/<int:pk>", EliminarPost.as_view(), name= 'eliminar_post'),
    path("listar_posts/", ListarPosts.as_view(), name='listar_posts')
    
    
]
