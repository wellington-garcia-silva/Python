print('================================')
print('            Banco CEV           ')
print('================================')
valor = int(input('Digite o valor a ser sacado: '))
notasCinquenta = 0
notasVinte = 0
notasDez = 0
notasCinco = 0
notasDois = 0
notasUm = 0
while(valor > 0):
    if(valor>=50):
        valor=valor-50
        notasCinquenta+=1
    elif(valor >= 20):
        valor = valor - 20
        notasVinte+=1
    elif(valor >= 10):
        valor = valor-10
        notasDez+=1
    elif(valor>=5):
        valor=valor-5
        notasCinco+=1
    elif(valor>=2):
        valor=valor-2
        notasDois+=1
    else:
        valor=valor-1
        notasUm+=1
print('Total de {} notas de R$50,00.'.format(notasCinquenta))
print('Total de {} notas de  R$20,00.'.format(notasVinte))
print('Total de {} notas de  R$10,00.'.format(notasDez))
print('Total de {} notas de  R$5,00.n'.format(notasCinco))
print('Total de {} notas de  R$2,00.'.format(notasDois))
print('Total de {} notas de  R$1,00.'.format(notasUm))
print('================================')
print('Volte sempre ao Banco CEV!')


