from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth

def homepage(request):
    return render(request, 'pages/index.html')


def criar_editor(request):

    if request.method == "GET":
        return render(request, 'pages/criar_editor.html')
    
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)
        if user.exists():
            return HttpResponse('email ja existe')
        
        user = Users.objects.create_user(username=email, email=email, password=senha, cargo="E" )


        return HttpResponse('ok')



def loginn(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('homepage'))
    
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')
        user = auth.authenticate(username=login, password=senha)

        if not user:
            return HttpResponse('usuario não existe')
        auth.login(request, user)
        return redirect(reverse('adm'))
    return render(request, 'pages/loginn.html')


def adm(request):
    return render(request, 'pages/adm.html')
