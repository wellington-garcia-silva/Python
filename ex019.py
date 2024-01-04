import random
nome1 = input('Digite o nome do primero aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
sorteado = random.choice(nome4,nome3,nome2,nome1)
print('O aluno sorteado foi: {}' .format(sorteado))
