
def visualizar_dados(conn):
    while True:
        print("\nVisualizar:")
        print("1 - Itens")
        print("2 - Armaduras")
        print("3 - Armas")
        Print("4 - Sair")
        tabela = input("Escolha uma tabela: ")
        
        match tabela:
            case "1":
                tabela = "itens"
                tipo = "Itens"
            case "2":
                tabela = "armaduras"
                tipo = "Armaduras"
            case "3":
                tabela = "armas"
                tipo = "Armas"
            case "4":
                print("Saindo...")
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
                    print("-" * 80)

                    
                    if tipo == "Itens":
                        for id_item, nome, id_class_item, quantidade, valor, peso in registros:
                            print(f"ID: {id_item}, NOME: {nome}, CLASSIFICAÇÃO: {id_class_item}, QUANTIDADE: {quantidade}, VALOR: {valor}, PESO: {peso}")

                    elif tipo == "Armaduras":
                        for id_armadura, nome, tipo_armadura, bonus, defesa_base, valor, peso in registros:
                            print(f"ID: {id_armadura}, NOME: {nome}, TIPO: {tipo_armadura}, BÔNUS: {bonus}, DEFESA BASE: {defesa_base}, VALOR: {valor}, PESO: {peso}")

                    elif tipo == "Armas":
                        for id_arma, nome, tipo_arma, bonus, ataque_base, valor, peso in registros:
                            print(f"ID: {id_arma}, NOME: {nome}, TIPO: {tipo_arma},BÔNUS: {bonus}, ATAQUE BASE: {ataque_base}, VALOR: {valor}, PESO: {peso}")
                else:
                    print("Inválido.")
        except Exception as e:
            print(e)
