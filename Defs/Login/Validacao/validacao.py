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
                print('\nFormato inválido!')
        else:
            os.system('cls' or 'clear')
            print('\n[ CADASTRO ]\n')
            print('\nFormato inválido!')

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

    id_usuario = email_bd(conn, email)

    try:
        if id_usuario and senha_bd(conn, senha, email):
            print('Usuário válido\n')
            return id_usuario
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
    query = f"SELECT * FROM gera.usuarios WHERE email = '{email}'"
    cursor.execute(query)
    conn.commit()
    usuario = cursor.fetchall()
    
    #retorna o id do usuario
    if usuario:
        return usuario[0][0]
    else:
        return False

def senha_bd(conn, senha, email):
    cursor = conn.cursor()
    query = f"SELECT senha FROM gera.usuarios WHERE senha = '{senha}' and email = '{email}'"
    cursor.execute(query)
    conn.commit()
    senha_existente = cursor.fetchall()

    return senha_existente

