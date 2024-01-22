continuar = 'S'
lista = list()
dado = list()
lista = list()
cont = 0
while continuar == 'S':
    dado.append(str(input('Digite o nome da pessoa: ')))
    dado.append(str(input('Digite o peso da pessoa: ')))
    lista.append(dado[:])
    dado.clear()
    continuar=input('Você deseja continuar? [S/N]').upper()
    cont+=1
print('Foram cadastradas {} pessoas.'.format(cont))
c = 0
for p in lista:
    print(p[c][0])
print(lista)
