continuar = 'S'
pos = 0
lista= [1]
while(continuar == 'S'):
    n1 = int(input('Digite um valor: '))
    if pos == 0:
        lista[0] = n1
        print('Valor adicionado com sucesso!')
    else:
        if n1 in lista:
            print('Valor duplicado, não vou adicionar!')
        else:
            lista.append(n1)
            print('Valor adicionado com sucesso!')
    continuar = input('Você deseja continuar? [S/N]')
    pos+=1
lista.sort()
print('Você acionou os valores {}'.format(lista))
