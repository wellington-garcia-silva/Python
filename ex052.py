n1 = int(input('Digite um número e saiba se ele é primo: '))
n2 = 0
for c in range (1,n1+1):
    if (n1 % c) == 0:
        n2 += 1
if n2 == 2:
    print('{} é um número primo.'.format(n1))
else:
    print('{} não é um número primo.'.format(n1))