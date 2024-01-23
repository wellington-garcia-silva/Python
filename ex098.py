import time
def contagem(inicio,fim,passo):
    print(f'A contagem de {inicio} até {fim} com passo de {passo}: ')
    for c in range(inicio,fim,passo):
        print(c, end=' ')
        time.sleep(0.2)

#Programa Principal
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Contagem de 1 até 10 de 1 em 1: ')
for c in range(1,10):
    print(c, end=' ')
    time.sleep(0.2)
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Contagem de 10 até 1 de 1 em 1: ')
for c in range(10,1,-2):
    print(c, end=' ')
    time.sleep(0.2)
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contagem(inicio,fim,passo)