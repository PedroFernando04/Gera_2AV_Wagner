import os

#Validação de Emails
def emailValido(users, conn):
    while True:
        email = input('\nDigite um email Válido: ')
        if '@' in email:
            usuario, dominio = email.split('@', 1)
            if usuario and dominio and '.' in dominio:
                email_existente = email_bd(conn, email)
                if email_existente:
                    print('\nEsse email já foi cadastrado.')
                else:
                    return email
                """#verificar se o email ja está cadastrado na lista(no proprio gera)
                    email_ja_cadastrado = False
                    for user in users:
                        if email == user.email:
                            print('\nEsse email já foi cadastrado.')
                            email_ja_cadastrado = True
                            break
                    if not email_ja_cadastrado:
                        return email"""
            else:
                os.system('cls' or 'clear')
                print('\n[ CADASTRO ]\n')
                print('\nDigite um email válido!')
        else:
            os.system('cls' or 'clear')
            print('\n[ CADASTRO ]\n')
            print('\nDigite um email válido!')

#Validação da senha
def senhaValida():
    while True:
        senha = input ('Digite a sua senha: ')
        senha2 = input ('Digite a sua senha novamente:')
        if senha == senha2:
            return senha
        else:
            print('Senhas não correspondentes, digite novamente\n')

#Validação do login
def loginValido(email, senha, conn):
    try:
        if email_bd(conn, email) and senha_bd(conn, senha, email):
            print('Usuário válido\n')
            return True
        else:
            pass
    except Exception as e:
        print(e)
        print ('Usuário e senha não encontrado')
        input()
        return False


#Email presente no banco

def email_bd(conn, email):
    cursor = conn.cursor()
    query = f"SELECT email FROM gera.usuarios WHERE email = '{email}'"
    cursor.execute(query)
    conn.commit()
    email_existente = cursor.fetchall()
    
    return email_existente


def senha_bd(conn, senha, email):
    cursor = conn.cursor()
    query = f"SELECT senha FROM gera.usuarios WHERE senha = '{senha}' and email = '{email}'"
    cursor.execute(query)
    conn.commit()
    senha_existente = cursor.fetchall()

    return senha_existente
