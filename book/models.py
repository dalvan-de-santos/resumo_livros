from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    choice_cargo = (('A', 'ADM'),
                    ('E', 'Editor'))
    cargo = models.CharField(max_length=1, choices=choice_cargo)


class Generos(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Livros(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    resumo = models.TextField()
    ano = models.IntegerField()
    empresa_publicada = models.CharField(max_length=150)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    publicado_por = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)
    publicado_em = models.DateTimeField(auto_now_add=True)
    genero = models.ForeignKey(Generos, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

