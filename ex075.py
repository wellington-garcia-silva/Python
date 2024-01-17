n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro núemero: '))
n3 = int(input('Digite mais um núemro: '))
n4 = int(input('Digite o último número: '))
tupla = [n1,n2,n3,n4]
nove = 0
posicaoTres = 0
t1 = 0
for c in range(0,4):
    if tupla[c]==9:
        nove+=1
    if tupla[c] == 3:
        posicaoTres = c
    if tupla[c] % 2 == 0:
        print('{} é um valor par.'.format(tupla[c]))
print(tupla)
print('O valor 9 apareceu {} vezes.'.format(nove))
if posicaoTres != 0:
    print('O valor 3 apareceu na posição {}°.'.format(posicaoTres))
else:
    print('O valor 3 não apareceu nenhuma vez.')
