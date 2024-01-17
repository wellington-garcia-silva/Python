lista = ['Pão',1.0,'Macarrão',3.5,'Bolacha',5.7,'Sabão',6.7,'detergente',2.0]
print('-----------------------------------')
print('--------LISTAGEM DE PREÇOS---------')
print('-----------------------------------')
produto = ' '
preco = 0
for c in range(0,len(lista)):
    if c % 2 == 0:
        produto = lista[c]
    else:
        preco = lista[c]
        print('{}...................R$  {}.'.format(produto,preco))
