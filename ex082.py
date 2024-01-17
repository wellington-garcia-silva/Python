lista = [0]
listaPar = [0]
listaImpar = [0]
continuar = 'S'
pos = 0
while continuar == 'S':
    n1 = int(input('Digite um valor: '))
    if pos == 0:
        lista[0] = n1
    else:
        lista.append(n1)
    continuar = input('Você deseja continuar? [S/N]').upper()
    pos+=1
for c in range(0,len(lista)):
    n1 = lista
    if lista[c] % 2 == 0:
        if c == 0:
            listaPar[0]=lista[0]
        else:
            listaPar.append(lista[c])
    else:
        if c == 0:
            listaImpar[0] = lista[0]
        else:
            listaImpar.append(lista[c])
print('A lista completa é :{}.'.format(lista))
print('A lista de pares é :{}.'.format(listaPar))
print('A lista de ímpares é: {}.'.format(listaImpar))
