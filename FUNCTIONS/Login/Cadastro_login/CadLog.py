from FUNCTIONS.Login.Validacao.validacao import emailValido, senhaValida, loginValido
import os


class Cadastro:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

usuarios = []

def cadastrar (conn):
    os.system('cls' or 'clear')

    print('\n[ CADASTRO ]\n')
    email = emailValido(usuarios)
    senha = senhaValida()
    
    #colocar na lista do gera
    usuarios.append(Cadastro(email,senha))

    #colocar no bd
    cursor = conn.cursor()
    query = f"INSERT INTO gera.usuarios(email, senha) VALUES (\'{email}\', \'{senha}\')"
    cursor.execute(query)
    return usuarios


def logar (users):
    os.system('cls' or 'clear')
    
    print('\n[ LOGIN ]\n')
    nome_login = input ('Digite seu Email: ')
    senha_login = input ('Digite sua senha: ')

    if loginValido(nome_login, senha_login, users):
        return True
    else:
        print('\nUsuário e senha inválida!')
        return False

