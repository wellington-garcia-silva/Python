import random

# Gera um número inteiro aleatório entre 1 e 100

n1 = random.randint(0, 5)
n2 = input(int('digite um número entre 0 e 5: '))
if n1 == n2:
 print('Você acertou o núemro!')
else:
 print('Você errou o número')