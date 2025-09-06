from django.db import models

# Create your models here.
class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=True, blank=True)
    imagem_url = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"Fotografia: {self.nome}"