from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import CadastroForms
from .models import Lista


def index(request):
    return render(request, 'acertos_e_erros/index.html')


