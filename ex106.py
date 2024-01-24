def ajuda(palavra):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Acessando o manual ou comando {palavra}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return help(palavra)


#Programa Principal
fim = ''
while fim != 'fim':
    fim = str(input('Função ou biblioteca: '))
    print(ajuda(fim))


