dicionario = dict()
for c in range(0,1):
    dicionario['nome'] = str(input('Nome: '))
    dicionario['media'] = float(input('Media:'))
if dicionario['media'] >= 5:
    print('O nome é igual a: {}'.format(dicionario['nome']))
    print('A média é igual a: {}'.format(dicionario['media']))
    print('A situação é igual a aprovado.')
else:
    print('O nome é igual a: {}'.format(dicionario['nome']))
    print('A média é igual a: {}'.format(dicionario['media']))
    print('A situação é igual a reprovado.')
