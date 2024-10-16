import random

def pv(classe, Const):
    print("\nAgora vamos calcular a vida do personagem")
    print("(A vida é definida por um dado de vida + Constituição do personagem)\n")
    print("A quantidade de lados do dado de vida é definido pela classe do personagem, sendo: \n")
    print("Guerreiro  |  10")
    print("Ladino     |  8")
    print("Curandeiro |  8")
    print("Mago       |  6")
    print("Bardo      |  8")
    print("Druida     |  8")
    
    if classe == 1:
        dvariavel = 10

    elif classe == 4:
        dvariavel = 6

    else:
        dvariavel = 8

    dadovida = random.randint(0, dvariavel)

    vida = dadovida + dvariavel

    print(f"\n\nBaseado na classe de seu personagem, você tem direito a um dado de {dvariavel} lados\n")

       
    print(f"Sua rolagem de um d{dvariavel} resultou em {dadovida}\n")
    
    print(f"{dadovida}(dado de vida) + {Const} (Constituição)\n")
    print(f"Logo o PV do personagem é de: {vida}\n")

    return vida
#Teste da Função
#pv(1 , 8)
