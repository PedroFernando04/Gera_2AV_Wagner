#verificar opçao valida no menu
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

 #Menu basico de Cadastro/login
def menu():
    while True:
        print("\nSeu organizador e gerenciador de Ficha do personagem\n")
        print('1 - Realizar Cadastro')
        print('2 - Login')
        print('3 - Sair')

        opc = intinput()

        if opc == 1:
            print("Cadastro realizado!") #vai entrar a função de Cadastro()
            return 1
        elif opc == 2:
            print("Login efetuado!")  #vai entrar a função de login()
            return 2
        elif opc == 3:
            print("Saindo...")
            break 
