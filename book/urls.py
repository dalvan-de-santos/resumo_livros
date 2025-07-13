from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('criar_editor/', views.criar_editor, name='criar_editor'),
    path('login/', views.loginn, name='login'),
    path('adm/', views.adm, name='adm'),
]