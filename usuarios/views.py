from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from erros_e_acertos.models import Lista, Materia
from django.core.paginator import Paginator
from django.db.models import Q


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip() or not senha.strip() or not senha2.strip():
            return redirect('cadastro')

        if senha != senha2:
            return redirect('cadastro')

        elif User.objects.filter(email=email).exists():
            return redirect('cadastro')

        elif User.objects.filter(username=nome).exists():
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return redirect('login')

    elif request.method == 'GET':

        if request.user.is_authenticated:
            return redirect('index')

        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']

        if not senha.strip() or not email.strip():
            return redirect('login')

        elif User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()

            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

            else:
                return redirect('login')

        else:
            return redirect('login')

    if request.method == 'GET':

        if request.user.is_authenticated:
            return redirect('index')

        return render(request, 'usuarios/login.html')


def dashboard(request):
    materia = request.GET.get('materia')
    tipo = request.GET.get('tipo')
    nome = request.GET.get('nome')

    if request.user.is_authenticated and not request.user.is_superuser:
        id_user = request.user.id

        if nome:
            listas = Lista.objects.filter(
                Q(nome_da_lista__icontains=nome) | Q(tipo__icontains=nome)).filter(usuario=id_user)

        elif materia or tipo:

            if not tipo and materia != 'todas':
                listas = Lista.objects.filter(materia=materia).filter(usuario=id_user)

            elif materia == 'todas':
                listas = Lista.objects.filter(tipo__icontains=tipo).filter(usuario=id_user)

            else:
                listas = Lista.objects.filter(materia=materia).filter(tipo__icontains=tipo).filter(usuario=id_user)

        else:
            listas = Lista.objects.order_by('data_realizacao').filter(usuario=id_user)

        materias = sorted(Materia.values)

        paginator = Paginator(listas, 3)

        pagina = request.GET.get('page')

        listas_por_pagina = paginator.get_page(pagina)

        dados = {
            'listas': listas_por_pagina,
            'materias': materias
        }
        return render(request, 'usuarios/dashboard.html', dados)

    elif request.user.is_superuser:
        if nome:
            listas = Lista.objects.filter(
                Q(nome_da_lista__icontains=nome) | Q(tipo__icontains=nome))

        elif materia or tipo:

            if not tipo and materia != 'todas':
                listas = Lista.objects.filter(materia=materia)

            elif materia == 'todas':
                listas = Lista.objects.filter(tipo__icontains=tipo)

            else:
                listas = Lista.objects.filter(materia=materia).filter(tipo__icontains=tipo)

        else:
            listas = Lista.objects.order_by('data_realizacao')

        materias = sorted(Materia.values)

        paginator = Paginator(listas, 3)

        pagina = request.GET.get('page')

        listas_por_pagina = paginator.get_page(pagina)

        usuario_admin = request.user

        dados = {
            'listas': listas_por_pagina,
            'materias': materias,
            'admin': usuario_admin
        }
        return render(request, 'usuarios/dashboard.html', dados)

    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')
