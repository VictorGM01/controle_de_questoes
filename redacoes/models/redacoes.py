from django.db import models
from datetime import datetime
from .generos import Genero
from django.contrib.auth.models import User


class Redaction(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    genero = models.TextField(max_length=30, choices=Genero.choices)
    tema = models.CharField(max_length=100)
    vestibular = models.CharField(max_length=40)
    data_realizacao = models.DateField(default=datetime.today)
    nota = models.IntegerField(blank=True, null=True)
    correcao = models.CharField(max_length=400, blank=True, null=True)
    tempo_de_realizacao = models.IntegerField()
    data_da_correcao = models.DateField(null=True, blank=True)
