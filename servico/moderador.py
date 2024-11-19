from servico.visualizar import *

def visualizar_dados(conn):
    while True:
        print("\nVisualizar:")
        print("1 - Itens")
        print("2 - Armaduras")
        print("3 - Armas")
        print("4 - Classificação de itens")
        print("5 - Sair")
        opc = int(input("Escolha uma tabela: "))
        
        match opc:
            case 1:
                visualizar_itens(conn)
            case 2:
                visualizar_armaduras(conn)
            case 3:
                visualizar_armas(conn)
            case 4:
                classifcacao_itens(conn)
                continue
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


    
