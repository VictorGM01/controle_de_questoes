from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Vestibular, Genero, Redaction


def adicionar(request):
    if request.method == 'POST':
        tema = request.POST['tema']
        genero = request.POST['genero']
        vestibular = request.POST['vestibular']
        nota = request.POST['nota']
        data_realizacao = request.POST['data']
        tempo = request.POST['tempo']
        correcao = request.POST.get('correção')
        data_correcao = request.POST.get('data_correcao')

        if data_correcao == '':
            data_correcao = None

        user = get_object_or_404(User, pk=request.user.id)

        nova_redacao = Redaction.objects.create(usuario=user, tema=tema, genero=genero, vestibular=vestibular,
                                                nota=nota, data_realizacao=data_realizacao, tempo_de_realizacao=tempo,
                                                correcao=correcao, data_da_correcao=data_correcao)

        nova_redacao.save()

        return redirect('dashboard-redacoes')

    contexto = {
        'generos': sorted(Genero.values),
        'vestibulares': sorted(Vestibular.values)
    }

    return render(request, 'redacoes/adicionar_redacao.html', contexto)


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


def detalhar(request, id_redacao):
    redacao_a_editar = get_object_or_404(Redaction, pk=id_redacao)

    if redacao_a_editar.usuario.id == request.user.id:
        contexto = {
            'redacao': redacao_a_editar
        }

        return render(request, 'redacoes/detalhes.html', contexto)
    else:
        return redirect('index')


def editar(request, id_redacao):
    redacao_a_editar = get_object_or_404(Redaction, pk=id_redacao)

    if redacao_a_editar.usuario.id == request.user.id:
        generos = sorted(Genero.values)
        vestibulares = sorted(Vestibular.values)

        data_realizacao = redacao_a_editar.data_realizacao.strftime('%Y-%m-%d')

        if redacao_a_editar.data_da_correcao:
            data_correcao = redacao_a_editar.data_da_correcao.strftime('%Y-%m-%d')
        else:
            data_correcao = None

        contexto = {
            'generos': generos,
            'vestibulares': vestibulares,
            'data_realizacao': data_realizacao,
            'redacao': redacao_a_editar,
            'data_correcao': data_correcao
        }

        return render(request, 'redacoes/editar_redacao.html', contexto)

    else:
        return redirect('index')
