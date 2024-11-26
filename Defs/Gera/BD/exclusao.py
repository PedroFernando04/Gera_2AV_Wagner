import os
def excluir_perso(conn, id_usuario):
    try:
        with conn.cursor() as cursor:
            # Listar os personagens do usuário
            query = """
                SELECT p.nome AS Nome, p.classe AS Classe
                FROM gera.personagens p
                WHERE p.id_usuario = %s
            """
            cursor.execute(query, (id_usuario,))
            registros = cursor.fetchall()

            if registros:
                print("\nSeus Personagens:")
                print("-" * 120)
                for nome, classe in registros:
                    print(f"Nome: {nome} | Classe: {classe}")
                print("-" * 120)
                nome_perso = input("Digite o nome do personagem que deseja excluir (ou parte do nome): ")

                
                query = """
                    SELECT p.id_personagem, p.nome AS Nome, p.classe AS Classe
                    FROM gera.personagens p
                    WHERE p.id_usuario = %s AND p.nome ILIKE %s
                """
                cursor.execute(query, (id_usuario, f"%{nome_perso}%"))
                personagens = cursor.fetchall()
                os.system("cls" or "clear")
                if personagens:
                    print("\nPersonagens encontrados:")
                    print("-" * 120)
                    for id_personagem, nome, classe in personagens:
                        print(f"Nome: {nome} | Classe: {classe}")
                    print("-" * 120)

                    if len(personagens) == 1:
                        
                        id_personagem = personagens[0][0]
                        confirmacao = input(f"Tem certeza que deseja excluir o personagem '{personagens[0][1]}'? (S/N): ").strip().lower()

                        if confirmacao == 's':
                            query = "DELETE FROM gera.personagens WHERE id_personagem = %s"
                            cursor.execute(query, (id_personagem,))
                            conn.commit()
                            print(f"Personagem '{personagens[0][1]}' excluído com sucesso.")
                        else:
                            print("Exclusão cancelada.")
                    else:
                       
                        print("Mais de um personagem corresponde ao nome informado. Especifique melhor o nome.")
                else:
                    print("Nenhum personagem encontrado com esse nome.")
            else:
                print("Você não possui personagens para excluir.")

    except Exception as e:
        print("Ocorreu um erro:", e)

def exluir_mod(conn):
    try:
        with conn.cursor() as cursor:
            print("Seus Personagens:")
            print("-" * 120)
            
            # Exibir personagens
            query = "SELECT nome, classe FROM gera.personagens"
            cursor.execute(query)
            personagens = cursor.fetchall()
            os.system("cls" or "clear")
            if personagens:
                for nome, classe in personagens:
                    print(f"Nome: {nome} | Classe: {classe}")
                print("-" * 120)

            # Solicitar o nome do personagem para excluir
            nome_personagem = input("Digite o nome do personagem que deseja excluir (ou parte do nome): ").lower()

            # Consulta SQL usando ILIKE para não diferenciar maiúsculas/minúsculas
            query_excluir = """
                DELETE FROM gera.personagens 
                WHERE nome ILIKE %s
                RETURNING nome, classe;
            """
            cursor.execute(query_excluir, ('%' + nome_personagem + '%',))

            # Verificar se algum personagem foi excluído
            registros_excluidos = cursor.fetchall()
            if registros_excluidos:
                print("\nPersonagem excluído com sucesso!")
                for nome, classe in registros_excluidos:
                    print(f"Nome: {nome} | Classe: {classe}")
            else:
                print("\nNenhum personagem encontrado com esse nome.")

            conn.commit()  # Garantir que a exclusão seja salva no banco de dados
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
