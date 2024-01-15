import random
n1 = random.randint(0,10)
print('=-=-=-=-=-=-=-=-=-=-=')
print('VAMOS JOGAR PAR OU IMPAR')
print('=-=-=-=-=-=-=-=-=-=-=')
n2 = int(input('Diga um valor: '))
num = input('Par ou impar? [P/I]')
soma = n1+n2
cont = 1
if (num=='P') and (soma%2==0):
    opcao = True
elif (num=='I'):
    opcao = False

while(opcao == False):
    n1 = random.randint(0, 10)
    print('VAMOS JOGAR NOVAMENTE')
    n2 = int(input('Diga um valor: '))
    num = input('Par ou impar? [P/I]')
    soma = n1 + n2
    if (num == 'P') and (soma % 2 == 0):
        opcao = True
    elif (num == 'I'):
        opcao = False
    cont+=1
    print('Você venceu.')
print('Você perdeu. Você tentou {} vezes. '.format(cont))
