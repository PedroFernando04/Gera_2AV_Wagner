import os
def print_atributos(dados_matriz, atributos):
    print(f"|D1 = [{dados_matriz[0]}] | D2 = [{dados_matriz[1]}] | D3 = [{dados_matriz[2]}] |")
    print(f"|D4 = [{dados_matriz[3]}] | D5 = [{dados_matriz[4]}] | D6 = [{dados_matriz[5]}] |")

    print(f"\nOs atributos são:")
    print(f"Força:        {atributos[0]}", )
    print(f"Destreza:     {atributos[1]}", )
    print(f"Constituição: {atributos[2]}", )
    print(f"Inteligência: {atributos[3]}", )
    print(f"Carisma:      {atributos[4]}", )
    print(f"Sabedoria:    {atributos[5]}")

def atribuir_atributo(dados_matriz, nome_classe, atributo_classe):
    For = Des = Const = Int = Car = Sab = 0
    atributos = [For, Des, Const, Int, Car, Sab]

    #Mostra os atributos atuais
    for i in range (6):
        
        print_atributos(dados_matriz, atributos)

        print(f"Sua classe ({nome_classe}) prioriza ({atributo_classe})")
        
        nome_atributo = ["FORÇA", "DESTREZA", "CONSTITUIÇÃO", "INTELIGÊNCIA", "CARISMA", "SABEDORIA"]
        
        #Valida o dado selecionado
        while True:
            try:
                dado_selecionado = int(input(f"\nPara o atributo {nome_atributo[i]}, qual número do dado você deseja vincular: "))
                if dado_selecionado > 6 or dado_selecionado < 1:
                    raise ValueError("Fora do intervalo")
                elif dados_matriz[dado_selecionado - 1] == "Utilizado":
                    raise ValueError("Dado já utilizado!")
            except ValueError:
                os.system('cls')
                print("Valor inválido ou dado já utilizado!")
                print("Informe um dos dados presentes na tabela e que já não tenha sido utilizado!\n")

                print_atributos(dados_matriz, atributos)

                print(f"\nSua classe ({nome_classe}) prioriza ({atributo_classe})")  
            
            else: 
                break
            
        #Atribui o dado ao atributo
        atributos[i] = dados_matriz[dado_selecionado - 1]
        dados_matriz[dado_selecionado - 1] = "Utilizado"
        os.system('cls')


    print_atributos(dados_matriz, atributos)
    return atributos
        
#TESTE DA FUNÇÃO
#Ordem do resultado --> atributos = [For, Des, Const, Int, Car, Sab]
#print(atribuir_atributo([1,2,3,4,5,6], 'guerreiro', 'força'))
