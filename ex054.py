n1 = 0
n2 = 0
for c in range(1,8):
    p1 = int(input('Digite o ano de nascimento da pessoa: '))
    if (2024 - p1) > 21:
        n1 =+ 1
    else:
        n2 += 1
print('{} são maiores de idade e {} são menores de idade.'.format(n1,n2))

