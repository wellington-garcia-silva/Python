anoNascimento = input(int('Digite o ano de nascimento do atleta: '))
if anoNascimento <=9:
    print('O atleta é MIRIM')
elif anoNascimento <= 14:
    print('O atleta é INFANTIL')
elif anoNascimento <= 19:
    print('O atleta é JUNIOR')
elif anoNascimento <= 20:
    print('O atleta é SENIOR')
else:
    print('O atleta é MASTER')