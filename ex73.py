tupla = ['América Mineiro', 'Atlético Mineiro', 'Atlético Paranaense', 'Botafogo', 'Chapecoense', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Figueirense', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional', 'Palmeiras', 'Ponte Preta', 'Santa Cruz', 'Santos', 'São Paulo', 'Sport', 'Vitória']
print(tupla[0:5])
print(tupla[16:])
print(sorted(tupla))
for c in range(0,20):
    if tupla[c] == 'Chapecoense':
        print('O time da Chapecoense estava na {}° posição do Campeonato Brasileiro em 2016.'.format(c))