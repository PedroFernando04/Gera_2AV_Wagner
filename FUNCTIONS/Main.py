from Cadastro_login.CadLog import usuarios, cadastrar,logar
from Validacao.validacao import loginValido
from menu.Menu import menu

# Menu principal do Gera Fichar
while True:
    resposta = menu()
    match resposta:
        case 1:
            usuarios = cadastrar()
        case 2:
            if logar(usuarios):
                print ('Feito')
        case 3:
            print('obrigado por testar')
            break
