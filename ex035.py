r1 = input(int('Digite o comprimento da primeira reta: '))
r2 = input(int('Digite o comprimento da segunda reta: '))
r3 = input(int('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3:
    print('Os segmentos de retas formam um triângulo. ')
elif r1 + r3 > r2:
    print('Os segmentos de retas formam um triângulo. ')
elif r2 + r3 > r1:
    print('Os segmentos de retas formam um triângulo. ')
else:
    print('Os segmentos de reta não formam um triângulo.')