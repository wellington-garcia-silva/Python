velCar = input(float('Digite qual é a velocidade do carro: '))
if velCar > 80:
    print('O carro vai ser multado:')
    n2 = velCar - 80
    print('A multa a ser paga é {}', n2*7)
else:
    print('O carro está numa velocidade aceit´cavel permitida!')