from FUNCTIONS.Gera.Atributos import atribuir_atributo, modificadores
from FUNCTIONS.Gera.Dados import rolar_dados
from FUNCTIONS.Gera.Personagem import criar_personagem
from FUNCTIONS.Gera.Tutorial import tutoriais
from FUNCTIONS.Gera.Vida import pv

from FUNCTIONS.Login.Cadastro_login import CadLog
from FUNCTIONS.Login.menu import Menu
from FUNCTIONS.Login.Validacao import validacao

# Menu principal do Gera Fichar
while True:
    resposta = Menu.menu()
    match resposta:
        case 1:
            usuarios = CadLog.cadastrar()
        case 2:
            if CadLog.logar(usuarios):
                print ('Feito')
        case 3:
            print('obrigado por testar')
            break