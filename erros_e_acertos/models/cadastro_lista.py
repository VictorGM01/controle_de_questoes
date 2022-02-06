from django.db import models
from datetime import datetime
from .materias import Materia
from django.contrib.auth.models import User


class Lista(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    materia = models.TextField(max_length=15, choices=Materia.choices)
    nome_da_lista = models.CharField(max_length=100)
    quantidade_questoes = models.IntegerField()
    tipo = models.CharField(max_length=60)
    acertos = models.IntegerField()
    erros = models.IntegerField()
    descricao_erros = models.CharField(max_length=300, blank=True, null=True)
    tempo_realizacao = models.IntegerField()
    data_realizacao = models.DateField(default=datetime.today)
