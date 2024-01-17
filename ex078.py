n0 = int(input('Digite um valor para a Posição 0.'))
n1 = int(input('Digite um valor para a Posição 1.'))
n2 = int(input('Digite um valor para a Posição 2.'))
n3 = int(input('Digite um valor para a Posição 3.'))
n4 = int(input('Digite um valor para a Posição 4.'))
lista = [n0,n1,n2,n3,n4]
maior = 0
menor = 0
posMaior = 0
posMenor = 0
for c in range(0,5):
    if maior <= lista[c]:
        maior = lista[c]
        posMaior = c
    if menor >= lista[c]:
        menor = lista[c]
        posMenor = c
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-=-=-=-=-=-=-=')
print('Você digitou os valores {}.'.format(lista))
print('O maior valor digitado foi o {} na posição {}.'.format(maior,posMaior))
print('O menor valor digitado foi o {} na posição {}.'.format(menor,posMenor))

