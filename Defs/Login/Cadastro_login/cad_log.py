from Defs.Login.Validacao.validacao import emailValido, senhaValida, loginValido
import os


class Cadastro:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

usuarios = []

def cadastrar (conn):
    os.system('cls' or 'clear')

    print('\n[ CADASTRO ]\n')
    email = emailValido(usuarios, conn)
    senha = senhaValida()
    
    #colocar na lista do gera
    usuarios.append(Cadastro(email,senha))

    #colocar no bd
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO gera.usuarios(email, senha, mod) VALUES ('{email}', '{senha}', 'false')"
        cursor.execute(query)
        conn.commit()
        return usuarios
    except Exception as e:
        print(e)
        input()


def logar (conn):
    os.system('cls' or 'clear')
    
    print('\n[ LOGIN ]\n')
    nome_login = input ('Digite seu Email: ')
    senha_login = input ('Digite sua senha: ')

    id_usuario = loginValido(nome_login, senha_login, conn)
    
    if id_usuario:
        return id_usuario
    else:
        print('\nUsuário ou senha inválido!')
        return False



