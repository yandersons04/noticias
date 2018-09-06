from django.db import models
from django.utils import timezone

class Artigo(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    texto = models.TextField()
    data_criado = models.DateTimeField(
            default=timezone.now)
    data_publicado = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.data_publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo