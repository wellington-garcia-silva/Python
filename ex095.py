import random
dicionario = dict()
var = 0
dicionario['jogador1'] = random.randint(1,6)
dicionario['jogador2'] = random.randint(1,6)
dicionario['jogador3'] = random.randint(1,6)
dicionario['jogador4'] = random.randint(1,6)

dicionario_ordenado = dict(sorted(dicionario.items()))
print(dicionario_ordenado)
