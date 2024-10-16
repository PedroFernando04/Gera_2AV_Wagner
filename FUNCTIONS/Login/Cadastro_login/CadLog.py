from FUNCTIONS.Login.Validacao.validacao import emailValido, senhaValida, loginValido
import os


class Cadastro:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

usuarios = []

def cadastrar ():
    os.system('cls')

    print('\n[ CADASTRO ]\n')
    email = emailValido(usuarios)
    senha = senhaValida()
    usuarios.append(Cadastro(email,senha))
    return usuarios


def logar (users):
    os.system('cls')
    
    print('\n[ LOGIN ]\n')
    nome_login = input ('Digite seu Email: ')
    senha_login = input ('Digite sua senha: ')

    if loginValido(nome_login, senha_login, users):
        return True
    else:
        print('\nUsuário e senha inválida!')
        return False
