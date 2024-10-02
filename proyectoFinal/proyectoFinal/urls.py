"""
URL configuration for proyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import index
from apps.posts.views import PostListView, PostDetailView
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    #path('posts/', posts, name = 'posts')
    #path('posts/', PostListView.as_view(), name='posts'),
    #path('posts/<int:id>/', PostDetailView.as_view(), name= 'Post_individual'),
    path('', include('apps.posts.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
