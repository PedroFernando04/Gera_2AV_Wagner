from FUNCTIONS.Login.Validacao.validacao import emailValido, senhaValida, loginValido
import os
from gera_wagner_3av.FUNCTIONS.Conexao.conexao import conexao


class Cadastro:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

usuarios = []

def cadastrar ():
    os.system("cls" or "clear")

    print('\n[ CADASTRO ]\n')
    email = emailValido(usuarios)
    senha = senhaValida()
    usuarios.append(Cadastro(email,senha))

    #Cadastrar no banco

    conn = conexao()
    cursor = conn.cursor()
    query = f"INSERT INTO usuarios(email, senha) VALUES ('{email}', '{senha}')"
    conn.commit(query)
    cursor.execute()
    cursor.close()
    conn.close()


    print("Cadastro realizado com sucesso!")
    input('\n[Pressione qualquer botão para voltar ao menu]\n')
    return usuarios


def logar (users):
    os.system("cls" or "clear")
    
    print('\n[ LOGIN ]\n')
    nome_login = input ('Digite seu Email: ')
    senha_login = input ('Digite sua senha: ')

    if loginValido(nome_login, senha_login, users):
        return True
    else:
        print('\nUsuário e senha inválida!')
        return False

