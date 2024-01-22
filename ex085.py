lista = list()
dado = list()
for c in range(0,7):
    n1 = int(input('Digite o {} valor.').format(c))
    if n1 % 2 == 0:
        dado.append(n1)
        lista[0].append(dado[:])
    else:
        dado.append(n1)
        lista[1].append(dado[:])
print(lista)