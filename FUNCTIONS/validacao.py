from CadLog import Usuario

#Validação de Emails
def emailValido():
    while True:
        email = input('Digite um email Válido: ')
        if '@' in email:
            usuario, dominio = email.split('@', 1)
            if usuario and dominio and '.' in dominio:
                return email
        else:
            print ('Digite um email válido!')

#Validação da senha
def senhaValida():
    while True:
        senha = input ('Digite a sua senha: ')
        senha2 = input ('Digite a sua senha novamente:')
        if senha == senha2:
            return senha
        else:
            print('Senhas não são igual, digite novamente elas\n')

#Validação do login
def loginValido(email, senha, usuarios):
    validacao = 0
    for i in range(0, len(usuarios)):
        if email == usuarios[i].email and senha == usuarios[i].senha:
            validacao += 1
        if validacao > 0:
            print('Usuário válido')
            return True
        else:
            print('Usuário e senha inválida!')