from Defs.Conexao.conexao import conexao
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
                os.system("cls" or "clear")
                print("Valor inválido ou dado já utilizado!")
                print("Informe um dos dados presentes na tabela e que já não tenha sido utilizado!\n")

                print_atributos(dados_matriz, atributos)

                print(f"\nSua classe ({nome_classe}) prioriza ({atributo_classe})")  
            
            else: 
                break
            
        #Atribui o dado ao atributo
        atributos[i] = dados_matriz[dado_selecionado - 1]
        dados_matriz[dado_selecionado - 1] = "Utilizado"
        os.system("cls" or "clear")
       

    print_atributos(dados_matriz, atributos)
    return atributos
        
#TESTE DA FUNÇÃO
#Ordem do resultado --> atributos = [For, Des, Const, Int, Car, Sab]
#print(atribuir_atributo([1,2,3,4,5,6], 'guerreiro', 'força'))

def atribuir_atributo_BD(conn,atributos):
    
    #atribui os atributos ao banco
    try:
        cursor = conn.cursor()
        query = "INSERT INTO gera.atributos(forca, destreza, constituicao, inteligencia, carisma, sabedoria) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, atributos)
        conn.commit()
        
    except Exception as e:
        print(f"ERRO INSERT ATRIBUTO: {e}")
    

    #retorna o id_atributo para vincular ao personagem
    try:
        cursor = conn.cursor()
        query2 = "SELECT id_atributo from gera.atributos ORDER BY id_atributo DESC LIMIT 1"
        cursor.execute(query2)
        conn.commit()
        id_atributo = cursor.fetchone()
        return id_atributo[0]
    
    except Exception as e:
        print(f"ERRO SELECT ATRIBUTOS: {e}")
    
