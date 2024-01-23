def leiaInt():
    n1 = 1
    n2 = True
    while n2:
        n1 = input('Digite um número: ')
        if n1.isnumeric() == False:
            print('EROO, digite um número inteiro válido.')
            n2 = True
        else:
            n2=False
    print('Você digitou o número {}'.format(n1))


#Programa Principal
leiaInt()
