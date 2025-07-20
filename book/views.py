from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Users, Livros
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import logout
from .forms import LivrosForm
from django.contrib.auth.decorators import login_required
from rolepermissions.decorators import has_permission_decorator
import requests

def homepage(request):
    livros = Livros.objects.all()
    return render(request, 'pages/index.html', {'livros': livros})

@has_permission_decorator('criar_usuario')
def criar_editor(request):

    if request.method == "GET":
        editor = Users.objects.filter(cargo="E")
        return render(request, 'pages/criar_editor.html', {'editores': editor})
    
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        first_name = request.POST.get('name')
        last_name = request.POST.get('sobrenome')

        user = Users.objects.filter(email=email)
        if user.exists():
            return HttpResponse('email ja existe')
        
        user = Users.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name, password=senha, cargo="E" )


        return redirect('criar_editor')



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

@login_required
def logoutt(request):
    logout(request)
    return redirect('login')


@login_required
@has_permission_decorator('acessar_adm')
def adm(request):
    return render(request, 'pages/adm.html')


@login_required
@has_permission_decorator('criar_post')
def criar_post(request):

    if request.method == "POST":
        form = LivrosForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.publicado_por = request.user
            livro.save()
            return redirect('adm')
    else:
        form = LivrosForm()


    return render(request, 'pages/criar_post.html', {'form': form})

@has_permission_decorator('criar_usuario')
def delete_editor(request, id):
    user = get_object_or_404(Users, id=id)
    user.delete()
    
    return redirect('criar_editor')


def detalhe_livro(request, id):
    livro = Livros.objects.filter(id=id)
    print(livro)
    return render(request, 'pages/detalhe_livro.html', {'livros': livro})


def buscar_livro(request):
    termo = request.GET.get("q", "")
    livros = []

    if termo:
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {"q": termo, "maxResults": 10}
        resp = requests.get(url, params=params).json()
        
        for item in resp.get("items", []):
            info = item.get("volumeInfo", {})
            livros.append({
                "titulo": info.get("title"),
                "autores": info.get("authors", []),
                "resumo": info.get("description", ""),
                "ano": info.get("publishedDate", ""),
                "editora": info.get("publisher", ""),
                "capa": info.get("imageLinks", {}).get("thumbnail"),
                "generos": info.get("categories", []),
            })

            return render(request, 'pages/book_list.html', {'livros': livros, 'termo': termo})
    return render(request, 'pages/book_list.html')
