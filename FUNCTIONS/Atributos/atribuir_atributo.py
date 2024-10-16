"""int atribuirAtributo(int numerodoDado, int *dadosatb, int *dadosUtilizados) {
    if (dadosUtilizados[numerodoDado - 1]) {

        return -1;
    }
    dadosUtilizados[numerodoDado - 1] = 1;// Marcar o dado como utilizado
    return dadosatb[numerodoDado - 1];
}"""

def atribuir_atributo(numero_dado, dados_atb, dados_utilizados):
    if dados_utilizados[numero_dado - 1]:
        return -1
    dados_utilizados[numero_dado - 1] = 1

    return dados_atb[numero_dado - 1]

#NOVA VERSÃO

"""import os

def atribuir_atributo(dados_matriz, nome_classe, atributo_classe):
    For = Des = Const = Int = Car = Sab = 0
    for i in range (0, 6):
        print(f"\nOs atributos são:")
        print(f"Força:        {For}", )
        print(f"Destreza:     {Des}", )
        print(f"Constituição: {Const}", )
        print(f"Inteligência: {Int}", )
        print(f"Carisma:      {Car}", )
        print(f"Sabedoria:    {Sab}")

        print(f"Sua classe ({nome_classe}) prioriza ({atributo_classe})")

        nome_atributo = {"FORÇA", "DESTREZA", "CONSTITUIÇÃO", "INTELIGÊNCIA", "CARISMA", "SABEDORIA"}
        while True:
            try:
                atributo = int(input(f"\nPara o atributo {nome_atributo[i]}, qual número do dado você deseja vincular: "))
                if atributo > 6 or atributo < 1:
                    raise ValueError("Fora do intervalo")
            except ValueError:
                os.system('cls')
                print("Valor inválido!")

                print("Resultado final")
                print(f"|D1 = [{dados_matriz[0]}] | D2 = [{dados_matriz[1]}] | D3 = [{dados_matriz[2]}] |")
                print(f"|D4 = [{dados_matriz[3]}] | D5 = [{dados_matriz[4]}] | D6 = [{dados_matriz[5]}] |")

                print(f"\nOs atributos são:")
                print(f"Força:        {For}", )
                print(f"Destreza:     {Des}", )
                print(f"Constituição: {Const}", )
                print(f"Inteligência: {Int}", )
                print(f"Carisma:      {Car}", )
                print(f"Sabedoria:    {Sab}")

                print(f"\nSua classe ({nome_classe}) prioriza ({atributo_classe})")  
            
            else: 
                break
#TESTE DA FUNÇÃO
atribuir_atributo([1,2,3,4,5,6], 'guerreiro', 'força')"""
