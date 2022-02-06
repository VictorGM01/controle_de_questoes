from django.contrib import admin
from .models import Lista


@admin.register(Lista)
class ListaAdmin(admin.ModelAdmin):
    list_display = ['materia', 'nome_da_lista', 'quantidade_questoes', 'acertos', 'erros']
