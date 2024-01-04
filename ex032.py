n1 = input(int('Digite o primeiro número: '))
n2 = input(int('Digite o segundo número: '))
n3 = input(int('Digite o terceiro número: '))
if (n1 > n2 and n1 > n3):
    printf('O maior número é o primeiro {}'.format(n1))
elif(n2 > n1 and n2 > n3):
    printf('O maior número é o segundo {}'.format(n2))
else:
    print('O maior número é o terceiro {}'.format(n3))
if (n1 < n2 and n1 < n3):
    printf('O menor número é o primeiro {}'.format(n1))
elif(n2 < n1 and n2 < n3):
    printf('O menor número é o segundo {}'.format(n2))
else:
    print('O menor número é o terceiro {}'.format(n3))


