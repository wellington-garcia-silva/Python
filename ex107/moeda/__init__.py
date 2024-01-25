def metade(num):
    return num/2

def dobro(num):
    return num*2


def aumentar(num,n2):
    return num*(1 +(n2/10))
def diminuir(num,n2):
    return num -  (n2/100)


def resumo(p,a,b):
    print(20*'-')
    print('  Resumo do Valor  ')
    print(20 * '-')
    print(f'Preço analizado: {p}')
    print(f'Dobro do preço:  {p*2}')
    print(f'Metade do preço é: {p/2}')
    print(f'{a}% de aumento é: {((a/100)+1)*p}')
    print(f'{b}% de redução é: {(b / 100) * p}')


