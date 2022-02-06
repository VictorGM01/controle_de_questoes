from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


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

        return redirect('index')

    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    pass


def dashboard(request):
    pass


def logout(request):
    pass
