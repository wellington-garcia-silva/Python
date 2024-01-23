def ficha(nome,gols):
    if nome == '' and gols != '':
        print(f'O jogador <desconhecido> fez {gols} gols.')
    elif nome == '' and gols == '':
        print(f'O jogador <desconhecido> fez 0 gols.')
    else:
        print(f'O jogador <{nome}> fez {gols} gols.')


#Programa Principal
print('-----------------------------------------')
nome = str(input('Nome do Jogador: '))
gols = str(input('Quantos gols o Jogador fez: '))
ficha(nome,gols)