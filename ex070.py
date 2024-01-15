print('--------------------')
print('Loja Super Baratão')
print('--------------------')
continuar = 'S'
totalGasto = 0
maior1000 = 0
maisBarato = 10
nomeMaisBarato = 'nulo'
while(continuar=='S'):
    preco = float(input('Preço: '))
    nome = input('Nome do produto: ')
    totalGasto +=preco
    if(preco>1000):
        maior1000+=1
    if(preco<maisBarato):
        maisBarato=preco
        nomeMaisBarato=nome
    continuar = input('Quer continuar? [S/N]')
print('------------Fim do Programa------------\n')
print('Temos {} produtos custando mais de R$1000,00 .\n'.format(maior1000))
print('O produto mais barato foi {} que custa R${},00.'.format(nomeMaisBarato,maisBarato))

