from django.db import models
from django.contrib.auth.models import User

from apps.posts.models import Post

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Comentario')
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.texto
    
    class Meta:
        ordering = ['-fecha']
