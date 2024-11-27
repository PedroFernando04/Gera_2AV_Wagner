import os
import bcrypt
from getpass import getpass

# Validação de Emails
def emailValido(users, conn):
    while True:
        email = input('\nDigite um email válido: ')
        if '@' in email:
            usuario, dominio = email.split('@', 1)
            if usuario and dominio and '.' in dominio:
                email_existente = email_bd(conn, email)
                if email_existente:
                    print('\nEsse email já foi cadastrado.')
                else:
                    return email
            else:
                os.system('cls' or 'clear')
                print('\n[ CADASTRO ]\nFormato inválido!')
        else:
            os.system('cls' or 'clear')
            print('\n[ CADASTRO ]\nFormato inválido!')

# Validação da senha
def senhaValida():
    while True:
        senha = getpass('Digite a sua senha: ')
        senha2 = getpass('Digite a sua senha novamente: ')
        if senha == senha2:
            # Garantindo que a senha seja convertida para bytes antes de gerar o hash
            hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
            return hashed.decode('utf-8')  # Convertendo o hash para string
        else:
            print('Senhas não correspondentes, digite novamente\n')

# Validação do login
def loginValido(email, senha, conn):
    id_usuario = email_bd(conn, email)
    try:
        if id_usuario and senha_bd(conn, senha, email):
            print('Usuário válido\n')
            return id_usuario
        else:
            print('E-mail ou senha inválidos.\n')
            return False
    except Exception as e:
        print(f"Erro: {e}")
        return False

# Email presente no banco
def email_bd(conn, email):
    cursor = conn.cursor()
    query = "SELECT id_usuario FROM gera.usuarios WHERE email = %s"
    cursor.execute(query, (email,))
    usuario = cursor.fetchone()
    
    # Retorna o id do usuário
    if usuario:
        return usuario[0]
    else:
        return False

# Verificação da senha no banco
def senha_bd(conn, senha, email):
    cursor = conn.cursor()
    query = "SELECT senha FROM gera.usuarios WHERE email = %s"
    cursor.execute(query, (email,))
    resultado = cursor.fetchone()

    if resultado:
        senha_hash = resultado[0]
        if isinstance(senha_hash, memoryview):  # Tratar retorno como memoryview
            senha_hash = senha_hash.tobytes()
        # Verificando senha com bcrypt
        return bcrypt.checkpw(senha.encode('utf-8'), senha_hash)
    return False
