"""while (rerolagens >= 0) {
        AtD20(dados, 6);
        
        printf("O resultado dos seus atributos foram:\n");
        for (int j = 0; j < 6; j++) {
            printf("Dado %d: %.2d\n", j + 1, dados[j]);
        }
        
        printf("Deseja rerolar? Você tem %d rerolagens restantes (digite S ou N): ", rerolagens);
        scanf(" %c", &reRolar);
    
        if (reRolar == 'S' || reRolar == 's') {
            rerolagens--;
            system("cls || clear");
            printf("Classe selecionada: %s\n", nomeClasse);
			printf("Atributo preferível: %s\n", atributoClasse);
			printf("\n");
            
        } else {
            break;
        }"""

import random
import os

def rolar_dados(qntDados, nome_classe, atributo_classe):
    dadosMatriz = []

    for re_rolagens in range(0, 3):
        
        if re_rolagens > 0:
            soma_re_rolagens = 6 * re_rolagens
        else:
            soma_re_rolagens = 0

        print("\nResultado dos dados: \n")
        for j in range(0, qntDados):
            dadosMatriz.append(random.randint(0, 20))
            print(f"Dado {j + 1}: {dadosMatriz[j + soma_re_rolagens]}")
        
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
        
        if re_rolagens == 2:
            print("Resultado final")
            print(f"|D1 = [{dadosMatriz[0]}] | D2 = [{dadosMatriz[1]}] | D3 = [{dadosMatriz[2]}] |")
            print(f"|D4 = [{dadosMatriz[3]}] | D5 = [{dadosMatriz[4]}] | D6 = [{dadosMatriz[5]}] |")
            break

        if rerolar == 1:
            os.system('cls')
            print(f"Classe selecionada: {nome_classe}")
            print(f"Atributo preferível: {atributo_classe}\n")

        else:  
            print("Resultado final")
            print(f"|D1 = [{dadosMatriz[0]}] | D2 = [{dadosMatriz[1]}] | D3 = [{dadosMatriz[2]}] |")
            print(f"|D4 = [{dadosMatriz[3]}] | D5 = [{dadosMatriz[4]}] | D6 = [{dadosMatriz[5]}] |")
            break

    return dadosMatriz
#TESTE DA FUNÇÃO
#print(rolar_dados(6, 'Guerreiro', 'Força'))
