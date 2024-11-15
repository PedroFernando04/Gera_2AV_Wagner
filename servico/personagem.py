from servicos.finalprint import print_final
import random, os

def criacao (conn):
    print ("Agora para a criação do seu persongem vamos precisar de alguas informações: ")
    nome = input("Qual o nome deseja colocar: ")
    id_raca = escolha_raca(conn)
    classe, opc = escolha_classe(conn)
    id_inventario = opc
    escolha_inventario(conn,id_inventario)
    id_atributo = 1 #Falta vincular
    vida = calculo_vida(conn, id_atributo,id_inventario)

    valores = (nome, id_raca, classe, id_inventario, id_atributo, vida)
    try:
        with conn.cursor() as cursor:
            query = """insert into gera.personagens (nome,  id_raca, classe, id_inventario, id_atributo, vida) 
            values (%s, %s, %s, %s, %s, %s);""" 
            cursor.execute(query, valores)
            conn.commit()

    except Exception as e:
        print(e)
    else:
        print

def escolha_raca(conn):
    print("-" * 120)
    print("Escolha sua Raça:")
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM gera.racas"
            cursor.execute(query)
            racas = cursor.fetchall()
            
            if racas:
                for linha in racas:
                    print(f"{linha[0]} - {linha[1]} || Passiva: {linha[2]}")
                opc = int(input("Digite o número da Raça que você deseja: "))
                return opc
    except Exception as e:
        print(e)

def escolha_classe(conn):
    
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
                print(f"Classe {classe_nome} foi selecionada!")
                print(f"Seu atributo principal é {atributo_principal}!")
                print("-" * 120)
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("\nValor inválido! Informe um dos valores presentes na tabela.\n")
    return classe_nome, opc

def escolha_inventario(conn, id_inventario):
    try:
        with conn.cursor() as cursor:
            query = """select
	                    atq.nome as Arma,
	                    atq.ataque_base as Dano,
                        def.nome as Armadura,
                        def.defesa_base as Defesa,
                        itn.nome as Item,
                        itn.quantidade as Quantidade
                        from
                        gera.inventarios inv
                    join gera.armas atq on inv.id_arma = atq.id_arma 
                    join gera.armaduras def on inv.id_armadura = def.id_armadura 
                    join gera.itens itn on inv.id_item = itn.id_item
                    where inv.id_inventario = %s"""
            cursor.execute(query,(id_inventario,))
            lista_iventario= ["Nome", "Dano", "Armadura", "Defesa", "Item", "Qauntidade"]
            valores = cursor.fetchall ()
            print("-" * 120)
            print("Seus Itens básicos dessa classe são: ")
            for linha in valores:
                for i in range(0,len(lista_iventario)):
                    print(f"{lista_iventario[i]}: {linha[i]}")
                print("-" * 120)

    except Exception as e:
        print(e)


def calculo_vida(conn, id_atributo, opc):
    print("\nAgora vamos calcular a vida do personagem")
    print("(A vida é definida por um dado de vida + Constituição do personagem)\n")
    print("A quantidade de lados do dado de vida é definida pela classe do personagem, sendo: \n")
    print("1 - Guerreiro  |  10 lados")
    print("2 - Ladino     |  8 lados")
    print("3 - Curandeiro |  8 lados")
    print("4 - Mago       |  6 lados")
    print("5 - Bardo      |  8 lados")
    print("6 - Druida     |  8 lados\n")
    
   
    dados_por_classe = {
        1: 10,  
        2: 8,   
        3: 8,   
        4: 6,   
        5: 8,  
        6: 8    
    }
    dvariavel = dados_por_classe.get(opc, 6)  

    dadovida = random.randint(1, dvariavel)

    try:
        with conn.cursor() as cursor:
         
            query = "SELECT constituicao FROM gera.atributos WHERE id_atributo = %s"
            cursor.execute(query, (id_atributo,))
            resultado = cursor.fetchone()  

            const = resultado[0] 
    except Exception as e:
        print(e)
        return None

    vida = dadovida + const

    print(f"Baseado na classe do seu personagem, você tem direito a um dado de {dvariavel} lados.")
    print(f"Sua rolagem de um d{dvariavel} resultou em {dadovida}.")
    print(f"{dadovida} (dado de vida) + {const} (Constituição)")
    print(f"Logo, o PV do personagem é de: {vida}\n")
    return vida
