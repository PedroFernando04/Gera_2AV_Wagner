import os
def print_final (conn, id_personagem):
    try:
        with conn.cursor () as cursor:
            query = f"""select p.nome, p.vida, p.dinheiro, p.classe,r.nome as raca,it.nome as item,def.nome as armadura, atc.nome as arma,forca,destreza, constituicao,inteligencia,sabedoria,carisma
                        from gera.personagens p 
                        join gera.atributos atb on atb.id_atributo = p.id_atributo
                        join gera.racas r on r.id_raca = p.id_raca
                        left join gera.inventarios inv on inv.id_inventario = p.id_inventario
                        left join gera.itens it on it.id_item  = inv.id_item
                        left join gera.armaduras def on def.id_armadura = inv.id_armadura
                        left join gera.armas atc on atc.id_arma = inv.id_arma
                        where id_personagem = {id_personagem}
                        """
            cursor.execute(query)
            lista_perso= ["Nome", "Vida", "Dinheiro", "Classe", "Raça", "Item", "Armadura", "Arma"]
            lista_atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
            valores = cursor.fetchall ()

           
            print("-" * 120)

            for linha in valores:
                
                for i in range(0,len(lista_perso)):
                    print(f"{lista_perso[i]}: {linha[i]}")
                
                print("\n")
                print("Atributos:")
                for k in range(len(lista_atributos)):
                    print(f"{lista_atributos[k]}: {linha[8 + k]}")
                print("-" * 120)
                print("\n")
                
    
    except Exception as e:
        print (e)
