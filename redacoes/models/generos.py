from django.db import models


class Genero(models.TextChoices):
    DISSERTACAO = 'Dissertação'
    ARTIGO_DE_OPINIAO = 'Artigo de Opinião'
    CARTA_ABERTA = 'Carta Aberta'
    RESENHA = 'Resenha'
    CRONICA_REFLEXIVA = 'Crõnica Reflexiva'
    NARRACAO = 'Narração'
    DESCRICAO = 'Descrição'
    JORNALISTICO = 'Estilo Jornalístico'
    COMENTARIO = 'Comentário'
