from Defs.Gera.Personagem.personagem import criacao
import os
from Defs.Gera.BD.finalprint import print_final
from Defs.Gera.BD.exclusao import excluir_perso

def voltar_menu():
    input('\n[Pressione qualquer botão para voltar ao menu]\n')
    os.system('cls' or 'clear')

def menu_login(conn, id_usuario):
    while True:
        print("Selecione o que deseja fazer:\n")
        print("1 - Criar personagem")
        print("2 - Visualizar personagem")
        print("3 - Deletar personagem")
        print("4 - Sair\n")
        opc = input()
        os.system("cls" or "clear")
        match(opc):
            case '1':
                id_personagem = criacao(conn, id_usuario)
                print_final(conn, id_personagem)
                voltar_menu()
            case '2':
                cursor = conn.cursor()
                query = "SELECT * FROM gera.personagens where id_usuario = %s"
                cursor.execute(query,(id_usuario,)
                row = cursor.fetchall()
                conn.commit()

                if row:
                    os.system ("cls" or "clear")
                    for i in range(0, len(row)):
                        print_final(conn, row[i][0])
                    voltar_menu()

                else:
                    print("Nenhum personagem encontrado!")
                    voltar_menu()

            case '3':
                excluir_perso(conn,id_usuario)
                voltar_menu()
            case '4':
                print("Finalizando")
                break
            case _:
                os.system('cls' or 'clear')
                print("Valor inválido!")
