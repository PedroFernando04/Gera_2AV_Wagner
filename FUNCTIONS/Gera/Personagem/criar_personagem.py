import os

class Personagem:
    def __init__(self, nome, classe, atributo):
        self.nome = nome
        self.classe = classe
        self.atributo =  atributo


def criar_personagem():
    personagens = []

    #Atribuir nome a ficha
    nome = input("Qual o nome do seu personagem? ")

    #Limpar o tutorial e manter o nome
    os.system("cls" or "clear")
    print(f"Nome: {nome}")
    
    #Escolha da classe
    print("\nVamos selecionar a classe do seu personagem.")
    print("(Classe || Atributo principal)")
    print("1 - Guerreiro || Força")
    print("2 - Ladino    || Destreza")
    print("3 - Curandeiro|| Constituição")
    print("4 - Mago      || Inteligência")
    print("5 - Bardo     || Carisma")
    print("6 - Druida    || Sabedoria\n")

    while True:
        try:
            classe = int(input("Informe o número referente a classe do seu personagem: "))
            if classe < 1 or classe > 6:
                raise ValueError("Fora do intervalo")     
        except(ValueError):
            print("\nValor inválido!")
            print("informe um dos valores presentes na tabela\n")
        else:
            os.system("cls" or "clear")
            break

    match(classe):
        case 1:
            nome_classe = "Guerreiro"
            atributo_classe = "Força"
        case 2: 
            nome_classe = "Ladino"
            atributo_classe = "Destreza"
        case 3: 
            nome_classe = "Curandeiro"
            atributo_classe = "Constituição"
        case 4: 
            nome_classe = "Mago"
            atributo_classe = "Inteligência"
        case 5: 
            nome_classe = "Bardo"
            atributo_classe = "Carisma"
        case 6: 
            nome_classe = "Druida"
            atributo_classe = "Sabedoria"

    print(f"Nome: {nome}")
    print(f"Classe selecionada: {nome_classe}")
    print(f"Atributo preferível: {atributo_classe}")

    personagens.append(Personagem(nome, nome_classe, atributo_classe))

    return personagens

#USO DA FUNÇÃO
"""personagens = (criar_personagem())

print(personagens[0].nome)"""
