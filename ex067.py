print('-----------------------------------')
n1 = int(input('Você quer ver a tabuada de qual valor: '))
print('-----------------------------------')
while(n1 > 0):
    for c in range(1,11):
        print('{} x {} = {}'.format(c,n1,n1*c))
    print('-----------------------------------')
    n1 = int(input('Você quer ver a tabuada de qual valor: '))
    print('-----------------------------------')
print('Programa tabuada encerrado.')