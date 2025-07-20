from django.test import TestCase
from .models import Users

name = 'Dalvan'
sobrenome = 'Santos'
email = 'dalvan14@gmail.com'
cargo = 'A'
senha = '123456'

user = Users.objects.create_user(username=email, first_name=name, last_name=sobrenome, password=senha, cargo=cargo)
print('usuario criado')