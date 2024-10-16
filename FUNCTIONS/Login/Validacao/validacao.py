#Validação de Emails
def emailValido(users):
    while True:
        email = input('\nDigite um email Válido: ')
        if '@' in email:
            usuario, dominio = email.split('@', 1)
            if usuario and dominio and '.' in dominio:
            #verificar se o email ja está cadastrado
                email_ja_cadastrado = False
                for user in users:
                    if email == user.email:
                        print('\nEsse email já foi cadastrado.')
                        email_ja_cadastrado = True
                        break
                if not email_ja_cadastrado:
                    return email
            else:
                print('\nDigite um email válido!')
        else:
            print ('\nDigite um email válido!')

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
def loginValido(email, senha, usuarios):
    validacao = 0
    for i in range(0, len(usuarios)):
        if email == usuarios[i].email and senha == usuarios[i].senha:
            validacao += 1
        if validacao > 0:
            print('Usuário válido\n')
            return True
        else:
            return False
