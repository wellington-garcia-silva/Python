n1 = int(input('Digite um número para saber a fatorial deste número: '))
n2 = 1
while n1 !=0:
    n2 = n1*n2
    n1 = n1 - 1
print('A soma fatorial deste número é: {}'.format(n2))