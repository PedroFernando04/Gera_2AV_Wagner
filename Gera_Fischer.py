from FUNCTIONS.Gera.Tutorial.tutoriais import inicio

from FUNCTIONS.Login.Cadastro_login import CadLog
from FUNCTIONS.Login.menu.Menu import menu

from FUNCTIONS.Conexao.conexao import conexao

from servico.personagem import criacao
from servico.finalprint import print_final

conn = conexao()

usuarios = None
# Menu principal do Gera Fichar
while True:
    resposta = menu()
    match resposta:
        case 1:
            usuarios = CadLog.cadastrar(conn)
            if usuarios:
                print("E-mail cadastrado com sucesso!")
        case 2:
            id_usuario = CadLog.logar(conn) 
            if id_usuario:
                break
            else:
                input('\n[Pressione qualquer botão para voltar ao menu]\n[Tente fazer o login novamente]\n')
        case 3:
            print('\nEncerrando o programa...\n\nFim\n')
            exit()

#Login realizado com sucesso

#iniciando o Gera
inicio()

#Criação do personagem
personagem = criacao(conn)

#Print final
#print_final(conn, id_personagem)
#id_personagem: criar uma função pra conseguir esse id e chamar a função dentro do print_final
print("PRINT FINAL")
