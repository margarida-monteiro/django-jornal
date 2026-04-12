from django.db import models
from django.utils import timezone

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_publicacao']


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_comentario = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentário em {self.artigo.titulo}"