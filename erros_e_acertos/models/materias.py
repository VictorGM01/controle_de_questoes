from django.db import models


class Materia(models.TextChoices):
    MATEMATICA = 'Matemática'
    FISICA = 'Física'
    PORTUGUES = 'Português'
    HISTORIA = 'História'
    FILOSOFIA = 'Filosofia'
    SOCIOLOGIA = 'Sociologia'
    BIOLOGIA = 'Biologia'
    QUIMICA = 'Química'
    LITERATURA = 'Literatura'
    GEOGRAFIA = 'Geografia'
