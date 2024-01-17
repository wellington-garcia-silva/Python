lista = [0]
cont = 1
continuar = 'S'
pos = 0
while continuar == 'S':
    n1 = int(input('Digite um valor: '))
    if pos == 0:
        lista[0] = n1
    else:
        lista.append(n1)
    cont+=1
    pos+=1
    continuar = input('Você deseja continuar? [S/N]').upper()
lista.sort(reverse=True)
print('Você digitou {}'.format(cont))
print('Os valores em ordem decrescente são {}'.format(lista))
if 5 in lista:
    print('O valor cinco foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')

