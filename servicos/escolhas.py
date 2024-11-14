def criar_perso(conn):
    print("Agora você vai criar o personagem")

    try:
        with conn.cursor() as cursor:
            nome = input("Digite o nome do seu Personagem: ")
            query = "INSERT INTO gera.personagens (nome) VALUES (%s) RETURNING id_personagem"
            cursor.execute(query, (nome,))
            id_personagem = cursor.fetchone()[0]
            print(f"Personagem criado com o ID: {id_personagem}")
            
            escolha_raca(conn, id_personagem)
            escolha_classe(conn, id_personagem)
    except Exception as e:
        print(f"Erro ao criar personagem: {e}")

def escolha_raca(conn, id_personagem):
    print("Escolha de Raças:")
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM gera.racas"
            cursor.execute(query)
            racas = cursor.fetchall()
            
            if racas:
                for linha in racas:
                    print(f"{linha[0]} - Raça: {linha[1]} Passiva: {linha[2]}")
                opc = int(input("Digite o número da Raça que você deseja: "))
                
                if 1 <= opc <= len(racas):
                    raca_id = racas[opc - 1][0]
                    update_query = "UPDATE gera.personagens SET id_raca = %s WHERE id_personagem = %s"
                    cursor.execute(update_query, (raca_id, id_personagem))
                    conn.commit()
                    print(f"Raça {racas[opc - 1][1]} foi selecionada!")
                else:
                    print("Opção inválida!")
            else:
                print("Opa! Não há raças disponíveis.")
    except Exception as e:
        print(e)

def escolha_classe(conn, id_personagem):
    print("\nVamos selecionar a classe do seu personagem.")
    print("(Classe || Atributo principal)")
    print("1 - Guerreiro || Força")
    print("2 - Ladino    || Destreza")
    print("3 - Curandeiro|| Constituição")
    print("4 - Mago      || Inteligência")
    print("5 - Bardo     || Carisma")
    print("6 - Druida    || Sabedoria\n")

    classes = [
        ("Guerreiro", "Força"),
        ("Ladino", "Destreza"),
        ("Curandeiro", "Constituição"),
        ("Mago", "Inteligência"),
        ("Bardo", "Carisma"),
        ("Druida", "Sabedoria")
    ]

    while True:
        try:
            opc = int(input("Digite o número da classe que você deseja: "))
            if 1 <= opc <= len(classes):
                classe_nome, atributo_principal = classes[opc - 1]
                with conn.cursor() as cursor:
                    update_query = "UPDATE gera.personagens SET classe = %s WHERE id_personagem = %s"
                    cursor.execute(update_query, (opc, id_personagem))  
                    conn.commit()
                    print(f"Classe {classe_nome} foi selecionada!")
                    print(f"Seu atributo principal é {atributo_principal}!\n")
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("\nValor inválido! Informe um dos valores presentes na tabela.\n")
