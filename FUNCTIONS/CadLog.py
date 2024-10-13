from validacao import *


class cadastro:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha


usuarios = []
print('[ CADASTRO ]\n')
email = emailValido()
senha = senhaValida()
usuarios.append(cadastro(email,senha))

def logar ():
    print('[ LOGIN ]\n')
    nome_login = input ('Digite seu Email: ')
    senha_login = input ('Digite sua senha: ')
    lista_user = usuarios

    if loginValido(nome_login, senha_login, lista_user):
        print ('TUDO CERTO')
    else:
        print ('TUDO ERRAAAAAAADO!')