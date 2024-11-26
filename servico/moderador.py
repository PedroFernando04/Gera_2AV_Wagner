from servico.finalprint import print_final
import os
from servico.menu_login import *

def visualizar_itens(conn):

    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM gera.itens"
            cursor.execute(query)
            registros = cursor.fetchall()
            if registros:
                print("\nTipo: Itens")
                print("-" * 120)
                for id_item, nome, id_class_item, quantidade, valor, peso in registros:
                    print(f"ID: {id_item}, NOME: {nome}, CLASSIFICAÇÃO: {id_class_item}, QUANTIDADE: {quantidade}, VALOR: {valor}, PESO: {peso}")
                print("-" * 120)
            else:
                print("Nenhum item encontrado.")
    except Exception as e:
        print(e)

def visualizar_armaduras(conn):
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM gera.armaduras"
            cursor.execute(query)
            registros = cursor.fetchall()
            if registros:
                print("\nTipo: Armaduras")
                print("-" * 120)
                for id_armadura, nome, tipo_armadura, bonus, defesa_base, valor, peso in registros:
                    print(f"ID: {id_armadura}, NOME: {nome}, TIPO: {tipo_armadura}, BÔNUS: {bonus}, DEFESA BASE: {defesa_base}, VALOR: {valor}, PESO: {peso}")
                print("-" * 120)
            else:
                print("Nenhuma armadura encontrada.")
    except Exception as e:
        print(e)

def visualizar_armas(conn):
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM gera.armas"
            cursor.execute(query)
            registros = cursor.fetchall()
            if registros:
                print("\nTipo: Armas")
                print("-" * 120)
                for id_arma, nome, tipo_arma, bonus, ataque_base, valor, peso in registros:
                    print(f"ID: {id_arma}, NOME: {nome}, TIPO: {tipo_arma}, BÔNUS: {bonus}, ATAQUE BASE: {ataque_base}, VALOR: {valor}, PESO: {peso}")
                print("-" * 120)
            else:
                print("Nenhuma arma encontrada.")
    except Exception as e:
        print(e)

def classifcacao_itens(conn):
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM gera.class_itens"
            cursor.execute(query)
            resultados = cursor.fetchall()
            if resultados:
                print("\nTipo: Classificação de Itens")
                print("-" * 120)
                for id_class_item, categoria, tipo, efeito in resultados:
                    print(f"ID: {id_class_item}, CATEGORIA: {categoria}, TIPO: {tipo}, EFEITO: {efeito}")
                print("-" * 120)
            else:
                print("nenhuma ")
    except Exception as e:
        print(e)


def visualizar_dados(conn):
    while True:
        print("\nVisualizar:")
        print("1 - Itens")
        print("2 - Armaduras")
        print("3 - Armas")
        print("4 - Classificação de itens")
        print("5 - Sair")
        opc = int(input("Escolha uma tabela: "))
        os.system("cls" or "clear")
        match opc:
            case 1:
                visualizar_itens(conn)
                voltar_menu()
            case 2:
                visualizar_armaduras(conn)
                voltar_menu()
            case 3:
                visualizar_armas(conn)
                voltar_menu()
            case 4:
                classifcacao_itens(conn)
                voltar_menu()
            case 5:
                print("\nSaindo do menu de Visualização...\n")
                break
            case _:
                print("Opção inválida.")
                continue


def inserir_dados(conn):
    while True:
        print("\nInserir em:")
        print("1 - Itens")
        print("2 - Armaduras")
        print("3 - Armas")
        print("4 - Sair...")
        opc = int(input("Escolha uma tabela: "))
        os.system("cls" or "clear")
        match opc:
            case 1:
                classifcacao_itens(conn)
                tabela = 'itens'
                nome = input("Nome do novo item: ")
                id_class_item = int(input("ID da classificação do item:"))
                quantidade = int(input("Quantidade: "))
                valor = float(input("Valor: "))
                peso = float(input("Peso: "))
                valores = (nome, id_class_item, quantidade, valor, peso)
                query = f"INSERT INTO gera.{tabela} (nome, id_class_item, quantidade, valor, peso) VALUES (%s, %s, %s, %s, %s)"
                
            case 2:
                tabela = "armaduras"
                nome = input("Nome da nova armadura: ")
                tipo = input("Tipo: ")
                bonus = input("Bônus: ")
                defesa_base = int(input("Defesa base: "))
                valor = float(input("Valor: "))
                peso = float(input("Peso: "))
                valores = (nome, tipo, bonus, defesa_base, valor, peso)
                query = f"INSERT INTO gera.{tabela} (nome, tipo, bonus, defesa_base, valor, peso) VALUES (%s, %s, %s, %s, %s, %s)"

            case 3:
                tabela = "armas"
                nome = input("Nome da nova arma: ")
                tipo = input("Tipo: ")
                bonus = input("Bônus: ")
                ataque_base = int(input("Ataque base: "))
                valor = float(input("Valor: "))
                peso = float(input("Peso: "))
                valores = (nome, tipo, bonus, ataque_base, valor, peso)
                query = f"INSERT INTO gera.{tabela} (nome, tipo, bonus, ataque_base, valor, peso) VALUES (%s, %s, %s, %s, %s, %s)"
            case 4:
                print("Saindo do menu de Inserção...\n")
                break

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, valores)
                conn.commit()
                print(f"{nome} inserido com sucesso na tabela {tabela}!")
        except Exception as e:
            print(e)

def alterar_dados(conn):
    while True:
        print("\nAlterar em:")
        print("1 - Itens")
        print("2 - Armaduras")
        print("3 - Armas")
        print("4 - Sair...")
        opc = int(input("Escolha uma tabela: "))
        os.system("cls" or "clear")
        match opc:
            case 1:
                visualizar_itens(conn)
                classifcacao_itens(conn)
                tabela = "Itens"
                item_id = int(input(f"Informe o ID do item que deseja alterar na tabela itens: "))
                nome = input("Novo nome do item: ")
                id_class_item = int(input("Nova classificação do item (ID): "))
                quantidade = int(input("Nova quantidade: "))
                valor = float(input("Novo valor: "))
                peso = float(input("Novo peso: "))
                query = f"UPDATE gera.itens SET nome = %s, id_class_item = %s, quantidade = %s, valor = %s, peso = %s WHERE id_item = %s"
                valores = (nome, id_class_item, quantidade, valor, peso, item_id)
            case 2:
                visualizar_armaduras(conn)
                tabela = "Armaduras"
                item_id = int(input(f"Informe o ID do item que deseja alterar na tabela Armaduras: "))
                nome = input("Novo nome do item: ")
                id_class_item = int(input("Nova classificação do item (ID): "))
                quantidade = int(input("Nova quantidade: "))
                valor = float(input("Novo valor: "))
                peso = float(input("Novo peso: "))
                query = f"UPDATE gera.armaduras SET nome = %s, id_class_item = %s, quantidade = %s, valor = %s, peso = %s WHERE id_armadura = %s"
                valores = (nome, id_class_item, quantidade, valor, peso, item_id)
            case 3:
                visualizar_armas(conn)
                tabela = "Armas"
                item_id = int(input(f"Informe o ID do item que deseja alterar na tabela Armas: "))
                nome = input("Novo nome da arma: ")
                tipo = input("Novo tipo: ")
                bonus = input("Novo bônus: ")
                ataque_base = int(input("Novo ataque base: "))
                valor = float(input("Novo valor: "))
                peso = float(input("Novo peso: "))
                query = f"UPDATE gera.armas SET nome = %s, tipo = %s, bonus = %s, ataque_base = %s, valor = %s, peso = %s WHERE id_arma = %s"
                valores = (nome, tipo, bonus, ataque_base, valor, peso, item_id)
            case 4:
                print("Saindo do menu de alteração...\n")
                break
            case _:
                print("Opção inválida.")
                continue   
        try:       
            with conn.cursor() as cursor:
                cursor.execute(query, valores)
                conn.commit()
                print(f"{nome} atualizado com sucesso na tabela {tabela}!")
        
        except Exception as e:
            print(e)

def buscarperso(conn):
    try:
        with conn.cursor() as cursor:
            print("Seus Personagens:")
            print("-" * 120)
            
            query = "SELECT nome, classe FROM gera.personagens"
            cursor.execute(query)
            personagens = cursor.fetchall()
            
            if personagens:
                for nome, classe in personagens:
                    print(f"Nome: {nome} | Classe: {classe}")
                print("-" * 120)

            nome_personagem = input("Digite o nome do personagem que deseja visualizar (ou parte do nome): ").lower()
            queryid = """Select id_personagem from gera.personagens p WHERE nome ILIKE %s """
            cursor.execute(queryid, ('%' + nome_personagem + '%',))
            idperso = cursor.fetchall()
            if idperso:
                id_personagem = idperso[0][0]  
                print_final(conn, id_personagem) 
            else:
                print("Nenhum personagem encontrado com esse nome.")
           
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
