tupla = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']
n1 = -1
while(n1<0 or n1>20):
    n1 = int(input('Digite um número entre 0 e 20: '))
    for c in range(0,21):
        if(c == n1):
            num = n1
print('Você digitou o número {}.'.format(tupla[num]))