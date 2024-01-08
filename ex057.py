sexo = input('Digite o sexo de uma pessoa (F ou M): ')
while sexo != ('F' or 'M'):
    sexo = input('Você digitou de forma incorreta. Digite (F ou M): ')
print('O sexo da pessoa digitado é {}.'.format(sexo))
