from Defs.Gera.Tutorial.tutoriais import inicio
from Defs.Login.Cadastro_login import CadLog
from Defs.Login.Menus.Menu import menu
from Defs.Conexao.conexao import conexao
from Defs.Login.Menus.menu_login import menu_login
from Defs.Login.Menus.menumod import verifmod,menumod


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
                if verifmod(conn,id_usuario):
                    menumod(conn)
                else:
                    inicio()
                    menu_login(conn, id_usuario)
                    continue
            else:
                input('\n[Pressione qualquer botão para voltar ao menu]\n[Tente fazer o login novamente]\n')
        case 3:
            print('\nEncerrando o programa...\n\nFim\n')
            break

conn.close()
