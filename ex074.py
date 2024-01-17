import random
tupla = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
print(f'Os números sorteados são {tupla}')
maior = tupla[0]
menor = tupla[0]
for c in range(0,5):
    if maior < tupla[c]:
        maior=tupla[c]
    if menor > tupla[c]:
        menor=tupla[c]
print('O maior elemento da tupla é {}. O menor elemento da tupla é {}.'.format(maior,menor))