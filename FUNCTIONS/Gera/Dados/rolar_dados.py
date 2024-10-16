import random
import os

def rolar_dados(qnt_dados, nome_classe, atributo_classe):
    dados_matriz = []

    for re_rolagens in range(0, 3):
        
        if re_rolagens > 0:
            soma_re_rolagens = 6 * re_rolagens
        else:
            soma_re_rolagens = 0

        print("\nResultado dos dados: \n")
        for j in range(0, qnt_dados):
            dados_matriz.append(random.randint(0, 20))
            print(f"Dado {j + 1}: {dados_matriz[j + soma_re_rolagens]}")
        
        print(f"\nDeseja rerolar? você tem {3 - re_rolagens} chances")
        print("1 - Sim\n2 - Não")
        
        while True:
            try:
                rerolar = int(input())
                if rerolar != 1 and rerolar != 2:
                    raise ValueError
            except(ValueError):
                print("Valor inválido!")
                print(f"Deseja rerolar? você tem {3 - re_rolagens}")
                print("1 - Sim\n2 - Não")
            else:
                os.system('cls')
                break
        
        if re_rolagens == 2 or rerolar == 2:
            break

        else:
            os.system('cls')
            print(f"Classe selecionada: {nome_classe}")
            print(f"Atributo preferível: {atributo_classe}\n")


    return dados_matriz
