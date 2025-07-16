from django import forms as formes
from django.contrib.auth import forms
from .models import Users, Livros

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users



class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users


class LivrosForm(formes.ModelForm):
    class Meta:
        model = Livros
        fields = [
            'title',
            'author',
            'resumo',
            'ano',
            'empresa_publicada',
            'picture',
            'publicado_por',
            'genero',
        ]
        widgets = {
            'resumo': formes.Textarea(attrs={'rows': 4}),
            'publicado_por': formes.HiddenInput(), 
        }