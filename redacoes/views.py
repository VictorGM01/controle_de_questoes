from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Vestibular, Genero, Redaction


def dashboard_redacoes(request):
    if request.user.is_authenticated:
        id_user = request.user.id

        tema = request.GET.get('tema')

        if tema:
            redacoes = Redaction.objects.order_by(
                'data_realizacao').filter(usuario=id_user).filter(tema__icontains=tema)

        else:
            redacoes = Redaction.objects.order_by('data_realizacao').filter(usuario=id_user)

        generos = sorted(Genero.values)

        vestibulares = sorted(Vestibular.values)

        paginator = Paginator(redacoes, 3)

        pagina = request.GET.get('page')

        redacoes_por_pagina = paginator.get_page(pagina)

        contexto = {
            'redacoes': redacoes_por_pagina,
            'generos': generos,
            'vestibulares': vestibulares
        }
        return render(request, 'redacoes/dashboard_redacoes.html', contexto)

    else:
        return redirect('index')
