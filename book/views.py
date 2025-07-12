from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

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
