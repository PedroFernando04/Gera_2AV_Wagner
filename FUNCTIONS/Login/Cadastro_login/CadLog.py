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
    email = emailValido(usuarios, conn)
    senha = senhaValida()
    
    #colocar na lista do gera
    usuarios.append(Cadastro(email,senha))

    #colocar no bd
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO gera.usuarios(email, senha, mod, id_personagem) VALUES ('{email}', '{senha}', 'false' , '1')"
        cursor.execute(query)
        conn.commit()
        return usuarios
    except Exception as e:
        print(e)
        input()


def logar (users, conn):
    os.system('cls' or 'clear')
    
    print('\n[ LOGIN ]\n')
    nome_login = input ('Digite seu Email: ')
    senha_login = input ('Digite sua senha: ')

    if loginValido(nome_login, senha_login, users, conn):
        return True
    else:
        print('\nUsuário e senha inválida!')
        return False

