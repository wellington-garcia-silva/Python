import random
import time
numeros = list()
def sorteia(numeros):
    print('Sorteando 5 valores da lista: ',end=' ')
    for c in range(0,5):
        numeros.append(random.randint(0,10))
        print(numeros[c],end=' ')
        time.sleep(0.2)
    print('PRONTO!')


def somaPar(numeros):
    soma = 0
    print('Somando os valores pares de',end=' ')
    print(numeros, end=' ')
    for c in range(0,5):
        if numeros[c] % 2 == 0:
            soma+=numeros[c]
    print(',temos {}'.format(soma))


#Programa Principal
sorteia(numeros)
somaPar(numeros)

