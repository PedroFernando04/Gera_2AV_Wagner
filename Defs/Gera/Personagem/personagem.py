from Defs.Gera.Atributos.atribuir_atributo import atribuir_atributo_BD, atribuir_atributo
from Defs.Gera.Dados.rolar_dados import rolar_dados

import random, os

def criacao (conn, id_usuario):
    os.system('cls' or 'clear')
    print ("Agora para a criação do seu persongem vamos precisar de alguas informações: ")
    
    nome = input("Qual o nome deseja colocar: ")
    
    id_raca = escolha_raca(conn)
    
    classe, opc, atributo_principal = escolha_classe(conn)
    
    dados_matriz = rolar_dados_personagem(classe, atributo_principal)

    id_inventario = opc
    escolha_inventario(conn,id_inventario)

    atributos = atribuir_atributo(dados_matriz, classe, atributo_principal)
    id_atributo = atribuir_atributo_BD(conn,atributos)
    
    vida = calculo_vida(conn, id_atributo, id_inventario)

    valores = (nome, id_raca, classe, id_inventario, id_atributo, vida, id_usuario)
    try:
        with conn.cursor() as cursor:
            query = """insert into gera.personagens (nome, id_raca, classe, id_inventario, id_atributo, vida, id_usuario) 
            values (%s, %s, %s, %s, %s, %s, %s);""" 
            cursor.execute(query, valores)
            conn.commit()

    except Exception as e:
        print(e)
    else:
        return id_personagem(conn)

def escolha_raca(conn):
    os.system('cls' or 'clear')
    while True:
        try:
            print("-" * 120)
            print("Escolha sua Raça:")
            with conn.cursor() as cursor:
                query = "SELECT * FROM gera.racas"
                cursor.execute(query)
                racas = cursor.fetchall()
                
                if racas:
                    for linha in racas:
                        print(f"{linha[0]} - {linha[1]} || Passiva: {linha[2]}")
                    print("-" * 120)
                    opc = int(input("\nDigite o número da Raça que você deseja: "))
                    if 1 <= opc <= 10:
                        return opc
                    else:
                        raise Exception ("Raça inexistente")
        except Exception as e:
            os.system('cls' or 'clear')
            print(e)

def escolha_classe(conn):
    
    os.system('cls' or 'clear')
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
                os.system('cls' or 'clear')
                classe_nome, atributo_principal = classes[opc - 1]
                print("-" * 120)
                print(f"Classe {classe_nome} foi selecionada!")
                print(f"Seu atributo principal é {atributo_principal}!")
                print("-" * 120)
                break
            else:
                os.system('cls' or 'clear')
                print("Opção inválida!")
                print("-" * 120)
                print(f"Classe {classe_nome} foi selecionada!")
                print(f"Seu atributo principal é {atributo_principal}!")
                print("-" * 120)
        except ValueError:
            os.system('cls' or 'clear')
            print("\nValor inválido! Informe um dos valores presentes na tabela.\n")
    return classe_nome, opc, atributo_principal

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
            os.system('cls' or 'clear')
            print("-" * 120)
            print("Seus Itens básicos dessa classe são: ")
            for linha in valores:
                for i in range(0,len(lista_iventario)):
                    print(f"{lista_iventario[i]}: {linha[i]}")
                print("-" * 120)
                input()
                os.system('cls' or 'clear')
                

    except Exception as e:
        print(e)


def calculo_vida(conn, id_atributo, opc):
    os.system('cls' or 'clear')
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
         
            query = f"SELECT constituicao FROM gera.atributos WHERE id_atributo = '{id_atributo}'"
            cursor.execute(query)
            resultado = cursor.fetchone()  

            const = resultado[0] 
            print(const)
    except Exception as e:
        print(f"ERRO SELECT constituicao: {e}")

    vida = dadovida + const

    os.system('cls' or 'clear')
    print(f"Baseado na classe do seu personagem, você tem direito a um dado de {dvariavel} lados.")
    print(f"Sua rolagem de um d{dvariavel} resultou em {dadovida}.")
    print(f"{dadovida} (dado de vida) + {const} (Constituição)")
    print(f"Logo, o PV do personagem é de: {vida}\n")
    input()
    os.system('cls' or 'clear')
    return vida

def rolar_dados_personagem(nome_classe, nome_atributo):
    input("\nAgora está na hora de rolar os dados!\n[pressione qualquer tecla para seguir]\n")
    os.system('cls' or 'clear')
    dados_matriz = rolar_dados(6, nome_classe, nome_atributo)
    return dados_matriz

def id_personagem(conn):
    cursor = conn.cursor()
    query = "SELECT id_personagem from gera.personagens ORDER BY id_personagem DESC LIMIT 1"
    cursor.execute(query)
    conn.commit()
    row = cursor.fetchone()
    return row[0]
