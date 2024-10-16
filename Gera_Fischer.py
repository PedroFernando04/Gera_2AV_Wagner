from FUNCTIONS.Gera.Atributos import atribuir_atributo, modificadores
from FUNCTIONS.Gera.Dados import rolar_dados
from FUNCTIONS.Gera.Personagem import criar_personagem
from FUNCTIONS.Gera.Tutorial import tutoriais
from FUNCTIONS.Gera.Vida import pv

from FUNCTIONS.Login.Cadastro_login import CadLog
from FUNCTIONS.Login.menu import Menu

# Menu principal do Gera Fichar
while True:
    resposta = Menu.menu()
    match resposta:
        case 1:
            usuarios = CadLog.cadastrar()
            if usuarios:
                print("E-mail cadastrado com sucesso!")
        case 2:
            if CadLog.logar(usuarios):
                break
            else:
                input('\n[Pressione qualquer botão para voltar ao menu]\n[Tente fazer o login novamente]\n')
                resposta
                
        case 3:
            print('\nEncerrando o programa...\n\nFim\n')
            break

#Login realizado com sucesso
#iniciando o Gera

