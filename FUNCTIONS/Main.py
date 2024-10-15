from Cadastro_login.CadLog import usuarios, cadastrar,logar
from Validacao.validacao import loginValido
from menu.Menu import menu

# Menu principal do Gera Fichar
while True:
    resposta = menu()
    if resposta == 1:
        usuarios = cadastrar()
    elif resposta == 2:
        if logar(usuarios):
            print ('Feito')
    else:
        print ('obrigado por testar')