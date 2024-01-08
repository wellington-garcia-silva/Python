maisVelho = 0
cont = 0
mediaIdade = 0
for c in range(0,4):
    nome = input('Qual o nome da pessoa: ')
    idade = int(input('Qual a idade desta pessao: '))
    sexo = input('Qual o sexo dessa pessoa: ')
    mediaIdade = idade + mediaIdade
    if (maisVelho < idade) and (sexo == 'masculino'):
        maisVelho = idade
        nomeMaisVelho = nome
    if (sexo == 'feminino') and (idade < 20):
        cont = cont + 1
print('A média de idade é {}. O homem mais velho é {}. {} mulheres tem menos de 20 anos.'.format(mediaIdade/4,nomeMaisVelho,cont))




