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
                print("Não foi possível encontrar resultados para sua busca.")
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
        tabela = int(input("Escolha uma tabela: "))
        
        match tabela:
            case 1:
                tabela = "itens"
                tipo = "Itens"
            case 2:
                tabela = "armaduras"
                tipo = "Armaduras"
            case 3:
                tabela = "armas"
                tipo = "Armas"
            case 4:
                classifcacao_itens(conn)
                continue
            case 5:
                print("\nSaindo do menu Visualizar...\n")
                break
            case _:
                print("Opção inválida.")
                continue

        try:
            with conn.cursor() as cursor:
                query = f"SELECT * FROM gera.{tabela};"
                cursor.execute(query)
                registros = cursor.fetchall()
                if registros:
                    print(f"\nTipo: {tipo}")
                    print("-" * 120)

                    if tipo == "Itens":
                        for id_item, nome, id_class_item, quantidade, valor, peso in registros:
                            print(f"ID: {id_item}, NOME: {nome}, CLASSIFICAÇÃO: {id_class_item}, QUANTIDADE: {quantidade}, VALOR: {valor}, PESO: {peso}")

                    elif tipo == "Armaduras":
                        for id_armadura, nome, tipo_armadura, bonus, defesa_base, valor, peso in registros:
                            print(f"ID: {id_armadura}, NOME: {nome}, TIPO: {tipo_armadura}, BÔNUS: {bonus}, DEFESA BASE: {defesa_base}, VALOR: {valor}, PESO: {peso}")

                    elif tipo == "Armas":
                        for id_arma, nome, tipo_arma, bonus, ataque_base, valor, peso in registros:
                            print(f"ID: {id_arma}, NOME: {nome}, TIPO: {tipo_arma}, BÔNUS: {bonus}, ATAQUE BASE: {ataque_base}, VALOR: {valor}, PESO: {peso}")
                else:
                    print("Nenhum registro encontrado.")
            print("-" * 120)
        except Exception as e:
            print(e)


def inserir_dados(conn):
    while True:
        print("\nInserir em:")
        print("1 - Itens")
        print("2 - Armaduras")
        print("3 - Armas")
        print("4 - Sair...")
        tabela = int(input("Escolha uma tabela: "))
        
        match tabela:
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
                print("Saindo...")
                break

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, valores)
                conn.commit()
                print(f"{nome} inserido com sucesso na tabela {tabela}!")
        except Exception as e:
            print(e)
