peso = input(float('Qual é o peso da pessoa: '))
altura = input(float('Qaul é a alura da pessoa: '))
imc = peso/(altura*altura)
if imc < 18.5:
    print('Esta pessoa está abaixo do peso')
elif imc >=18.5 and imc <=25:
    print('Esta pessoa está com o peso normal!')
elif imc <= 30:
    print('Esta pessoa está obesa')
else:
    print('Esta pessoa está com obsidade mórbida!')