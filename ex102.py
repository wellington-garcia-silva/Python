def fatorial(n1,show=''):
    if show == '':
        soma = 1
        for c in range(0,n1):
            soma+=soma
        return soma
    else:
        soma = 1
        for c in range(0, n1):
            soma += soma
            print(c,end=' ')
            print('x',end=' ')
        print('=',end=' ')
        return soma


#Programa Principal
n1 = int(input('Digite um número para mostrar o seu fatorial: '))
show = str(input('Mostrar:'))
print(fatorial(n1,show))