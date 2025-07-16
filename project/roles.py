from rolepermissions.roles import AbstractUserRole



class Adm(AbstractUserRole):
    available_permissions = {
        'criar_usuario': True,
        'criar_post': True,
        'acessar_adm': True,
        'deletar_user': True,
        
    }


class Editor(AbstractUserRole):
    available_permissions = {
        'criar_post': True,
        'acessar_adm': True,
        
    }