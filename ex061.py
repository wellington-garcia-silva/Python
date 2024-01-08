primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
for c in range (1,11):
    n1 = primeiroTermo + (c - 1) * razao
    print('{}° termo da PA é: {}'.format(c,n1))
v = 1
while v!=11:
    n1 = primeiroTermo + (v - 1) * razao
    print('{}° termo da PA é: {}'.format(v, n1))
    v+=1