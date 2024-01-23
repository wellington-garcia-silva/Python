def area(l,c):
    a = l*c
    print(f'A área de um terreno de {l} x {c} é de {a}m².')


#Programa principal
print('--------------------------------')
print('------CONTROLE DE TERRENOS------')
print('--------------------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)