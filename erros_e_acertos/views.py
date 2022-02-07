from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .models import Lista, Materia
from django.contrib.auth.models import User


def index(request):
    return render(request, 'acertos_e_erros/index.html')


def adicionar_registro(request):
    if request.method == 'POST':
        materia = request.POST['materia']
        nome_lista = request.POST['nome_lista']
        quantidade_questoes = request.POST['quantidade_questoes']
        tipo = request.POST['tipo']
        acertos = request.POST['acertos']
        erros = request.POST['erros']
        descricao = request.POST['descricao']
        time = request.POST['time']
        data = request.POST['data']

        user = get_object_or_404(User, pk=request.user.id)

        nova_lista = Lista.objects.create(usuario=user, nome_da_lista=nome_lista, materia=materia,
                                          quantidade_questoes=quantidade_questoes,
                                          tipo=tipo, acertos=acertos, erros=erros, descricao_erros=descricao,
                                          tempo_realizacao=time, data_realizacao=data)

        nova_lista.save()

        return redirect('dashboard')

    contexto = {"materias": sorted(Materia.values)}

    return render(request, 'acertos_e_erros/adicionar_registros.html', contexto)


def detalhar_lista(request, id_lista):
    lista_a_exibir = get_object_or_404(Lista, pk=id_lista)

    contexto = {
        'lista': lista_a_exibir
    }

    return render(request, 'acertos_e_erros/detalhes_lista.html', contexto)


def editar_lista(request, id_lista):
    pass
