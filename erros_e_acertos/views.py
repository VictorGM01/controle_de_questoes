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

    if lista_a_exibir.usuario.id == request.user.id:

        contexto = {
            'lista': lista_a_exibir
        }

        return render(request, 'acertos_e_erros/detalhes_lista.html', contexto)

    else:
        return redirect('dashboard')


def editar_lista(request, id_lista):
    lista_a_editar = get_object_or_404(Lista, pk=id_lista)
    materias = sorted(Materia.values)
    contexto = {
        'lista': lista_a_editar,
        'materias': materias
    }

    return render(request, 'acertos_e_erros/editar_lista.html', contexto)


def atualizar_lista(request):
    if request.method == 'POST':
        lista_id = request.POST['lista_id']

        lista_a_atualizar = get_object_or_404(Lista, pk=lista_id)

        lista_a_atualizar.materia = request.POST['materia']
        lista_a_atualizar.nome_da_lista = request.POST['nome_lista']
        lista_a_atualizar.quantidade_questoes = request.POST['quantidade_questoes']
        lista_a_atualizar.tipo = request.POST['tipo']
        lista_a_atualizar.acertos = request.POST['acertos']
        lista_a_atualizar.erros = request.POST['erros']
        lista_a_atualizar.descricao_erros = request.POST['descricao']
        lista_a_atualizar.tempo_realizacao = request.POST['time']
        lista_a_atualizar.data_realizacao = lista_a_atualizar.data_realizacao
        lista_a_atualizar.usuario = lista_a_atualizar.usuario
        data_revisao = request.POST['data_revisao']

        if data_revisao != '':
            lista_a_atualizar.data_revisao = request.POST['data_revisao']

        else:
            lista_a_atualizar.data_revisao = lista_a_atualizar.data_revisao

        lista_a_atualizar.save()

        return redirect(f'detalhes/{lista_id}')

    else:
        return redirect('index')
