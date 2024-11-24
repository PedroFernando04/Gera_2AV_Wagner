import os
#INICIO
def inicio():
    nome = "Gera Fischar"

    #Apresentação
    os.system("cls" or "clear")
    print(f"Bem vindo(a) ao {nome}!")
    print("Aqui vamos te ajudar a montar a ficha para o seu personagem de RPG!")
    print("\nNa sua ficha de RPG você irá escolher o nome, a classe e os atributos do seu personagem.")

    while True:
        print("Deseja ver algum tutorial?")
        print(f"1 - Tutorial de classes\n2 - Tutorial de atributos\n3 - Tutorial do {nome}\n4 - Nenhum tutorial\n")
        tutorial = input()
        print("\n")
        match(tutorial):
            case '1':
                tutorial_classe()
                
            case '2':
                tutorial_atributo()
                
            case '3':
                tutorial_gera(nome)
                
            case '4':
                os.system("cls" or "clear")
                break
                
            case _:
                os.system("cls" or "clear")
                print("Deseja ver algum tutorial?")
                print(f"1 - Tutorial de classes\n2 - Tutorial de atributos\n3 - Tutorial do {nome}\n4 - Nenhum tutorial\n")
                tutorial = input()
                os.system("cls" or "clear")


#CLASSES
def tutorial_classe():
    os.system("cls" or "clear")

    #Tutorial
    print("\nClasse é o que definirá o seu papel no jogo.\n(Determina as habilidades, aptidões e estilo de jogo do personagem.)")
    print("\nCada classe tem habilidades e limitações específicas, então escolha com atenção, pois isso influenciará como o personagem se desenvolverá")

    #As Classes
    print("\nAs classes são:\n")

    #Guerreiro
    print("Guerreiro:\n Focados no combate corpo a corpo, eles são mestres no uso de armas e armaduras pesadas, e sua principal função é proteger o grupo e enfrentar os inimigos diretamente.")
    print(" Os guerreiros são conhecidos por sua resistência e capacidade de infligir dano físico significativo aos oponentes.")
    print(" Eles são ideais para jogadores que preferem um estilo de jogo direto e focado em combate.\n")
    
    #Ladino
    print("Ladino:\n Especialistas em furtividade, astúcia e habilidades sociais. Eles são mestres em movimento silencioso, ")
    print("arrombamento de fechaduras, furtos e emboscadas.\n Além disso, possuem grande habilidade em detectar armadilhas e desarmá-las.")
    print(" Os ladinos são frequentemente usados para explorar, sabotar ou se infiltrar em áreas inimigas, bem como para desvendar mistérios e segredos.\n")
    
    
    #Curandeiro
    print("Curandeiro:\n Também conhecidos como clérigos ou sacerdotes, os curandeiros são especialistas em magia de cura e apoio.")
    print(" Eles têm o poder de curar ferimentos, remover doenças e restaurar energia vital aos aliados.")
    print(" Além disso, os curandeiros podem possuir habilidades para proteger o grupo contra efeitos negativos, banir mortos-vivos e até ")
    print("mesmo invocar\npoderes divinos para derrotar inimigos.\n Eles desempenham um papel crucial na manutenção da saúde e na sobrevivência do grupo.\n\n")
    
    
    #Mago
    print("Mago:\n Usuários de magia arcana, estudiosos do oculto e manipuladores das energias místicas do universo.")
    print(" Eles lançam feitiços poderosos que podem causar dano devastador, controlar as mentes dos inimigos,")
    print(" alterar a realidade e até mesmo\ninvocar criaturas mágicas para auxiliá-los.")
    print(" Os magos são especialistas em conhecimento arcano e são mais limitados em combate físico, mas compensam isso com sua vasta gama de habilidades mágicas.\n\n")
    
    #Bardo
    print("Bardo:\n Artistas versáteis e contadores de histórias talentosos.")
    print(" Eles possuem habilidades musicais, poéticas e teatrais que os permitem encantar, inspirar e manipular as emoções dos outros.")
    print(" Além disso, os bardos são capazes de utilizar magias arcanas e habilidades de combate para apoiar o grupo de diversas maneiras,")
    print("seja através de cura, buffs, debuffs ou até mesmo ataques diretos.\n Sua versatilidade os torna valiosos tanto em combate quanto em situações sociais e de exploração.\n\n")
    
    #Druida
    print("Druida:\n Guardiões da natureza e praticantes de magia druídica.")
    print(" Eles têm uma forte conexão com os elementos naturais, podendo invocar a fúria dos elementos, transformar-se em animais e manipular a flora e fauna ao seu redor.")
    print(" Os druidas são especialistas em cura natural, bem como em controlar ou convocar criaturas da natureza para lutar ao seu lado.")
    print(" Sua ligação com a natureza os torna defensores do equilíbrio e protetores das terras selvagens.\n\n")
            
#ATRIBUTOS
def tutorial_atributo():
    os.system("cls" or "clear")
    #Atributos
    print("\nAtributos são valores numéricos que representam as habilidades e as capacidades do personagem.\n")
    print("Valores esses que servem como base para determinar a eficácia do personagem em diversas habilidades e ações.")
    print("Sendo levados em consideração, em uma jogada, os atributos básicos, da ficha do personagem, somados com o dado lançado no momento.\n")
    print("Os atributos são:\n")
    
    #Força
    print("Força:\n A força é um atributo que representa a capacidade física do personagem.")
    print("Significando que o personagem é mais capaz em atividades que exigem força física, como combate corpo a corpo,")
    print("levantamento de objetos pesados e resistência a efeitos que demandam vigor físico, como ser empurrado ou derrubado.\n")
    
    #Destreza
    print("Destreza:\n A destreza está relacionada à agilidade, coordenação e reflexos do personagem.")
    print(" Resultando em maior precisão em ataques à distância, capacidade de esquiva a ataques inimigos, ")
    print("habilidades furtivas e capacidade de realizar acrobacias ou manobras de evasão.\n")
    
    #Constituição
    print("Constituição:\n A constituição ou vigor representa a saúde e a resistência do personagem.")
    print(" Significando que o personagem pode suportar mais dano, resistir a efeitos adversos, como veneno ou doenças, e manter sua resistência física por mais tempo.\n")
    
    #Inteligência
    print("Inteligência:\n A inteligência representa a capacidade mental, conhecimento e habilidades mágicas do personagem.")
    print(" Resultando em maior eficácia em habilidades mágicas, capacidade de resolver problemas complexos, conhecimento em áreas acadêmicas e aptidão para\n identificar e utilizar artefatos mágicos.\n")
    
    #Carisma
    print("Carisma:\n O carisma mede a presença, confiança e habilidades sociais do personagem.")
    print(" Uma alta pontuação de carisma pode influenciar a capacidade do personagem de persuadir outros, liderar grupos, negociar com NPCs e influenciar\n as interações sociais de maneira geral.\n")
    
    #Sabedoria
    print("Sabedoria:\n A sabedoria reflete a percepção, intuição e experiência do personagem.")
    print(" Resultando em maior resistência a efeitos mentais, como encantamentos ou ilusões, capacidade de perceber ameaças e armadilhas ocultas\n e sabedoria prática em situações do dia a dia.\n")

 #GERA   
def tutorial_gera(nome):
    os.system("cls" or "clear")
            
    print(f"\nNo {nome} você vai, primeiramente, escolher o nome do seu personagem.\n(Basta Colocar o nome que desejar, simples ou composto, e teclar 'Enter' para registrá-lo)\n")
    print("Após isso será escolhida a classe(em caso de dúvida, consultar o tutorial de classes), teclando o número equivalente à classe desejada.\n")
    print("Em seguida será a sessão dos dados. Nela serão sorteados 6 valores que você deverá atribui-los aos seus atributos de personagem.")
    print("\nAssim que os dados forem sorteados você poderá escolher se deseja um novo sorteio ou seguir com os dados atuais(Terá 3 oportunidades para fazer isso)\n")
    print("Após selecionar os dados, como dito anteriormente, você deverá atribuir seus valores aos atributos de persongaem (em caso de dúvida, consultar o tutorial de atributos).")
    print("\nUm atributo por vez, você irá teclar o número referente ao dado desejado\n(Ex: Caso deseje atribuir o D1 = 20, você irá teclar apenas o número 1), lembrado que cada dado pode ser selecionado apenas uma vez.\n")
    print("Por fim você verá a sua ficha completa, com Nome, Classe e todos os atributos.\n")
    print("Agora que já está por dentro, pode seguir em frente e criar sua ficha!")
    print("\n")

