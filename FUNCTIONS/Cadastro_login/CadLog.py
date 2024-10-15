from Validacao.validacao import emailValido, senhaValida,loginValido


class Cadastro:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

usuarios = []

def cadastrar ():

    print('\n[ CADASTRO ]\n')
    email = emailValido()
    senha = senhaValida()
    usuarios.append(Cadastro(email,senha))
    return usuarios


def logar (users):
    print('\n[ LOGIN ]\n')
    nome_login = input ('Digite seu Email: ')
    senha_login = input ('Digite sua senha: ')

    if loginValido(nome_login, senha_login, users):
        return True
    else:
        print('Usuário e senha inválida!')
        return False

