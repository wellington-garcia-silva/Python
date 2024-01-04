import math
cat_adjacente = float(input('Digite o comprimente do cateto adjacente: '))
cat_oposto = float(input('Digite o comprimente do cateto oposto: '))
cat_adjacente = math.pow(cat_adjacente,2)
cat_oposto = math.pow(cat_oposto,2)
hipotenusa = math.sqrt(cat_oposto+cat_adjacente)
print('A hipotenusa deste número é: {}'.format(hipotenusa))
