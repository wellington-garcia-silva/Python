n1 = input(int('Digite o distancia da viagem:'))
if n1 < 200:
    print('A distancia é menor que 200, portanto você irá pagar 0.5R$ por KM, assim o total a ser pago é: {}',n1*0.5)
else:
    print('A distancia é maior que 200, portanto você irá pagar 0.45R$ por KM, assim o total a ser pago é: {}',n1*0.45)