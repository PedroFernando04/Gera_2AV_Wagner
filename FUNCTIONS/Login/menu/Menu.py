#Validação da opçao do menu
def intinput():
    while True:
        try:
            resp = int(input('Digite a opção no qual deseja realizar: '))
            if 1 <= resp <= 3:
                return resp
            else:
                print("Digite um número válido entre 1 e 3.")
                print('1 - Realizar Cadastro')
                print('2 - Login')
                print('3 - Sair')

        except ValueError:
            print("Digite um número inteiro válido.")



#menu padrao do Gera
def menu():
    while True:
        print("\nSeu organizador e gerenciador de Ficha do personagem\n")
        print('1 - Realizar Cadastro')
        print('2 - Login')
        print('3 - Sair')
        resp = intinput()
        break
    return resp


