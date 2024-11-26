from servico.moderador import *
from servico.menu_login import *
from servico.exclusao import exluir_mod
import os


def verifmod(conn, id_usuario):
    try:
       
        with conn.cursor() as cursor:
            query = """SELECT mod FROM gera.usuarios WHERE id_usuario = %s"""
            cursor.execute(query, (id_usuario,))
            resultado = cursor.fetchone()  
            
            if resultado:
                mod = resultado[0] 
                return mod 
            else:
                print("Usuário não encontrado!")
                return False  
    except Exception as e:
        print(f"Erro ao verificar o moderador: {e}")
        return False
    
def menumod (conn):
        try:
             with conn.cursor() as cursor:
                os.system ("cls" or "clear")
                print("Bem-vindo, moderador do Gera Ficha!\n")
                while True:
                    print("O que você deseja?")
                    print("1 - Visualizar itens")
                    print("2 - Inserir itens")
                    print("3 - Alterar itens")
                    print("4 - Deletar personagem")
                    print("5 - Buscar personagem")
                    print("6 - Sair")

                    opc = int(input("O que gostaria de fazer: "))
                    os.system("cls" or "clear")
                    match opc:
                        case 1:
                            visualizar_dados(conn)
                            voltar_menu()
                        case 2:
                            inserir_dados(conn)
                            voltar_menu()
                        case 3:
                            alterar_dados(conn)
                            voltar_menu()
                        case 4:
                            exluir_mod(conn) 
                            voltar_menu()
                        case 5:
                            buscarperso(conn)
                            voltar_menu()
                        case 6:
                            break
                        case _:
                            print("Opção inválida. Tente novamente.")
        except Exception as e:
            print (e)
