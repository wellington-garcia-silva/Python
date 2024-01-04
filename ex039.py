anoNascimento = input(int('Qual o ano de nascimento: '))
if (2024 - anoNascimento) < 18:
    printf('Ainda não está na hora de se alistar. Faltam {} anos'.format(18-(2024-anoNascimento))
elif (2024 - anoNascimento) > 18:
    printf('Você já passou {} anos do tempo de se alistar.'.format(2024-anoNascimento)-18)
else:
    print('Está na hora de se alistar: ')