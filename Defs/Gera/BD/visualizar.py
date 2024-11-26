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



