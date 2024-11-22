from servico.personagem import criacao
import os
from servico.finalprint import print_final

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
        
        match(opc):
            case '1':
                id_personagem = criacao(conn, id_usuario)
                print_final(conn, id_personagem)
                voltar_menu()
            case '2':
                cursor = conn.cursor()
                query = f"SELECT * FROM gera.personagens where id_usuario = {id_usuario}"
                cursor.execute(query)
                row = cursor.fetchall()
                conn.commit()

                if row:
                    os.system('cls' or 'clear')
                    for i in range(0, len(row)):
                        print_final(conn, row[i][0])
                    voltar_menu()

                else:
                    print("Nenhum usuário encontrado!")
                    voltar_menu()

            case '3':
                cursor = conn.cursor()
                query = f"SELECT * FROM gera.personagens where id_usuario = {id_usuario}"
                cursor.execute(query)
                row = cursor.fetchall()
                conn.commit()
        
                if row:
                    lista_print = ["ID", "Nome"]
                    os.system('cls' or 'clear')
                    print("-" * 120)
                    for coluna in range(0, len(row)):
                        for linha in range(0, 2):
                            print(f"{lista_print[linha]}: {row[coluna][linha]}")
                        print("-" * 120)
                else:
                    print("Nenhum usuário encontrado!")
                try:
                    personagem_deletado = input("\nInforme o ID do personagem que deseja deletar: ")
                    query2 = f"DELETE FROM gera.personagens where id_personagem = {personagem_deletado}"
                    cursor.execute(query2)
                    conn.commit()
                except Exception as e:
                    print(f"Erro ao deletar o personagem: {e}")
                    voltar_menu()
                else:
                    print("Personagem deletado com sucesso!")
                    voltar_menu()
            case '4':
                print("Finalizando")
                break
            case _:
                print("Valor inválido!")
                voltar_menu()
