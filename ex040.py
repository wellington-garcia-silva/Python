n1 = input(float('Digite a primeira nota:'))
n2 = input(float('Digite a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('O aluno foi reprovado!')
elif (media >= 5 and media <= 6.9):
    print('O aluno está de recuperação!')
else:
    print('O aluno está aprovado!')