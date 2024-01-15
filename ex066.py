n1 = float(input('Digite um número até que este número seja igual a 999: '))
soma = n1
cont = 1
if(n1==999):
    cont=0
    soma = 0
while(n1!=999):
    n1 = float(input('Digite um número até que este número seja igual a 999: '))
    soma = n1 + soma
    cont = cont + 1
print('A soma dos {} números é:{} '.format(cont,soma))
