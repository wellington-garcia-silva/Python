primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

v = 1
termos = 10
while v!=0:
    while v!=termos:
        n1 = primeiroTermo + (v - 1) * razao
        print('{}° termo da PA é: {}'.format(v, n1))
        v+=1
    v = 1
    termos = int(input('Quantos termos você ainda quer ver: '))
