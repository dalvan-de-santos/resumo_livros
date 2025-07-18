from django.contrib import admin
from django.contrib import admin
from .models import Users, Livros, Generos
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm


@admin.register(Users)
class UserAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Cargo', {'fields': ('cargo',)}),
    )


@admin.register(Livros)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'resumo', 'ano', 'empresa_publicada', 'picture', 'publicado_por', 'publicado_em', 'genero')

@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ('name',)