from FUNCTIONS.Gera.Atributos import atribuir_atributo, modificadores
from FUNCTIONS.Gera.Dados import rolar_dados
from FUNCTIONS.Gera.Personagem import criar_personagem
from FUNCTIONS.Gera.Tutorial import tutoriais
from FUNCTIONS.Gera.Vida import pv

from FUNCTIONS.Login.Cadastro_login import CadLog
from FUNCTIONS.Login.menu import Menu

import os

# Menu principal do Gera Fichar
while True:
    resposta = Menu.menu()
    match resposta:
        case 1:
            usuarios = CadLog.cadastrar()
            if usuarios:
                print("E-mail cadastrado com sucesso!")
        case 2:
            if CadLog.logar(usuarios):
                break
            else:
                input('\n[Pressione qualquer botão para voltar ao menu]\n[Tente fazer o login novamente]\n')
                resposta
                
        case 3:
            print('\nEncerrando o programa...\n\nFim\n')
            break

#Login realizado com sucesso

#iniciando o Gera
tutoriais.inicio()

#Criação do personagem
personagem = criar_personagem.criar_personagem()[0]

#Rolar os dados
input("\nAgora está na hora de rolar os dados!\n[pressione qualquer tecla para seguir]\n")
os.system('cls')
dados_matriz = rolar_dados.rolar_dados(6, personagem.classe, personagem.atributo)

#Utilização do Personagem
"""print(personagem.nome)
print(personagem.classe)
print(personagem.atributo)"""

print(f"\nAgora vamos definir os atributos de {personagem.nome}\n")

#Atributos
atributos = atribuir_atributo.atribuir_atributo(dados_matriz, personagem.classe, personagem.atributo)

#PV
input("\nÉ hora dos pontos de vida\n[pressione qualquer tecla para seguir]\n")
os.system('cls')
vida = pv.pv(personagem.classe, atributos[2])

#limpar tela para deixar a apenas a ficha
input("\n[Pressione qualquer tecla para ver sua ficha finalizada]\n")
os.system('cls')

#Ficha final
print(f"Nome: {personagem.nome}")
print(f"Classe: {personagem.classe}")
print("\nAtributos: ")
print(f"Vida: {vida}")
print(f"Força: {atributos[0]}", )
print(f"Destreza: {atributos[1]}", )
print(f"Constituição: {atributos[2]}", )
print(f"Inteligência: {atributos[3]}", )
print(f"Carisma: {atributos[4]}", )
print(f"Sabedoria: {atributos[5]}")
