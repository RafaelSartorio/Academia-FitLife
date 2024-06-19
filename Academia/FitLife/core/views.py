from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Aulas
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def loginSubmit(request):
    context = {
        'title': 'Login'
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/main/perfil')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return render(request, 'login.html', context)


def telaPrincipal(request):
    context = {
        'title': 'Home'
    }
    return render(request ,'main.html', context)

# *COMENTEI PARA USOS FUTUROS*
@login_required(login_url='/login/')
def telaPerfil(request):

    # Obtém o usuário logado atualmente
    usuario = request.user

    # Filtra as aulas para o usuário logado
    aulas = Aulas.objects.filter(aluno=usuario)
    
    # Prepara o dicionário de contexto
    context = {
        'title': 'Perfil',
        'aulas': aulas,  # Passa o queryset filtrado de Aulas para o template
    }

    # Renderiza o template 'perfil.html' com o contexto
    return render(request, 'perfil.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/main')

def adicionarUser(request):
    context = { 
        'title': 'Cadastro' 
    }
    return render(request,'novo_user.html', context)

def cadastroSubmit(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
        User.objects.create_user(email=email,password=password,username=username)
        return redirect('/login') 

def atualizarSenha():
    user = User.get_username('')
    User.set_password
    

