from django.shortcuts import render


def index(request):
    return render(request, 'acertos_e_erros/index.html')
