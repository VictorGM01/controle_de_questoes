from django.db import models
from datetime import datetime
from .materias import Materia


class Lista(models.Model):
    materia = models.TextField(max_length=15, choices=Materia.choices)
    nome_da_lista = models.CharField(max_length=100)
    quantidade_questoes = models.IntegerField()
    tipo = models.CharField(max_length=60)
    acertos = models.IntegerField()
    erros = models.IntegerField()
    descricao_erros = models.CharField(max_length=300, blank=True, null=True)
    tempo_realizacao = models.IntegerField()
    data_realizacao = models.DateField(default=datetime.today)
