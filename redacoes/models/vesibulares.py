from django.db import models


class Vestibular(models.TextChoices):
    ENEM = 'ENEM'
    UNICAMP = 'Unicamp'
    FUVEST = 'Fuvest'
    UNESP = 'Unesp'
    UERJ = 'UERJ'
    OUTROS = 'Outros'
