import random
import os

def rolar_dados(qnt_dados, nome_classe, atributo_classe):
    dados_matriz = []  # Armazenar os resultados finais
    
    print(f"Classe: {nome_classe}\nAtributo: {atributo_classe}")
    
    for re_rolagens in range(3):  # Permite até 3 rerrolagens
        ultima_rolagem = [random.randint(1, 20) for _ in range(qnt_dados)]
        
        print("\nResultado dos dados:\n")
        for i, valor in enumerate(ultima_rolagem, start=1):
            print(f"Dado {i}: {valor}")
        
        # Atualiza os dados_matriz com o último resultado
        dados_matriz = ultima_rolagem[:]
        
        # Se for a última tentativa de rerolar, avisa o usuário e não pergunta mais
        if re_rolagens == 2:  
            print("\nVocê atingiu o limite de rerrolagens.")
            break

        print(f"\nDeseja rerolar? Você tem {2 - re_rolagens} chance(s) restante(s).")
        print("1 - Sim\n2 - Não")
        
        while True:
            try:
                rerolar = int(input("Escolha uma opção: "))
                if rerolar not in [1, 2]:
                    raise ValueError
            except ValueError:
                print("\nOpção inválida! Tente novamente.")
            else:
                break
        
        if rerolar == 2:  # Se o usuário escolher "Não", interrompe o laço
            break
        os.system('cls' or 'clear')
    print(f"Resultado final dos dados para a classe {nome_classe}:")
    for i, valor in enumerate(dados_matriz, start=1):
        print(f"Dado {i}: {valor}")
    pausa = input("Digite qualque coisa para continuar")
    return dados_matriz
