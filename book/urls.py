from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('criar_editor/', views.criar_editor, name='criar_editor'),
    path('login/', views.loginn, name='login'),
    path('logout/', views.logoutt, name='logout'),
    path('adm/', views.adm, name='adm'),
    path('criar_post/', views.criar_post, name='criar_post'),
]