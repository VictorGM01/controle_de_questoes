from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .models import Lista


def index(request):
    return render(request, 'acertos_e_erros/index.html')


def adicionar_registro(request):
    return render(request, 'acertos_e_erros/adicionar_registros.html')
