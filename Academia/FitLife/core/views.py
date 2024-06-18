from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Aulas
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def loginSubmit(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/main/perfil')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return render(request, 'login.html')


def telaPrincipal(request):
    return render(request ,'main.html')

@login_required(login_url='/login/')
def telaPerfil(request):
    return render(request,'perfil.html')

def logoutUser(request):
    logout(request)
    return redirect('/main')

def adicionarUser(request):
    return render(request,'novo_user.html')

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
    

