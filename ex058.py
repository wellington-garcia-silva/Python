import random

# Gera um número inteiro aleatório entre 1 e 100
n3 = 1
n1 = random.randint(0, 10)
n2 = int(input('Digite um número entre 0 e 10: '))
while n1!=n2:
    n2 = int(input('Você não acertou. Digite outro número entre 0 e 10: '))
    n3 = n3 + 1
print('Parabéns, você acertou! O número que o computador escolheu foi {} e você tentou {} vezes.'.format(n2,n3))