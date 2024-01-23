import random
import time
lista = list()
def maior(lista,n1):
    maior = 1
    for c in range(0,n1):
        if lista[c] >= maior:
            maior = lista[c]
    print('O maior valor informado foi {}.'.format(maior))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


#Programa Principal
n1 = random.randint(0,10)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Analisando os valores passados...')
for c in range(0,n1):
    n2 = random.randint(0,10)
    lista.append(n2)
    print(n2,end=' ')
    time.sleep(0.2)
print('Foram informados {} valores ao todo. '.format(n1))

maior(lista,n1)