n1 = int(input('Digite um número: '))
soma = 0
cont = 0
while n1 != 999:
    soma +=n1
    n1 = int(input('Digite outro número: '))
    cont += 1
print('A soma dos números digitados é {} e foram digitadas {} vezes antes de ser digitado 999.'.format(soma,cont))
