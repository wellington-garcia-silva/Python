n1 = float(input('Digite um número: '))
continuar = 'S'
cont = 1
soma = 0
maior = menor = 0
while continuar == 'S':
    soma = n1 + soma
    continuar = input('Deseja continua? S/N: ')
    if continuar == 'S':
        n1 = float(input('Digite um número: '))
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    cont+=1
print('A média dos valores digitados é {}. O maior númeor é {}  e o menor é {}'.format(soma/cont,maior,menor))
