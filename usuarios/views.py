from django.shortcuts import render, redirect

from usuarios.forms import LoginForm, CadastroForms
from django.contrib.auth.models import User 

from django.contrib import auth , messages

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            print(f'Nome: {nome} - Senha: {senha}')
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                print('Usuário logado com sucesso')
                messages.success(request, f'Bem vindo {nome}!')
                return redirect('index')
            else:
                print('Senha incorreta')
                messages.error(request, 'Senha incorreta')
                return redirect('login')
        else:
                print('Usuário não existe')
                messages.error(request, 'Usuário não existe')
                return redirect('login')
    return render(request, 'usuarios/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('login')

def cadastro(request):
    form = CadastroForms()
    if request.method == "POST":
        form = CadastroForms(request.POST)
        print(request.POST)
        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, 'As senhas não coincidem.')
                return redirect('cadastro')
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existe')
                return redirect('cadastro')

            usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
            )
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})