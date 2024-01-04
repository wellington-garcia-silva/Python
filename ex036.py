valorCasa = input(float('Qual o valor da casa: '))
salario = input(float('Qual o salário: '))
anos =  input(float('Em quantos anos ele vai pagar: '))
prestacaoMensal = valorCasa/(anos*12)
if prestacaoMensal < 0.3*salario:
    print('Você pode comprar a casa!')
else:
    print('Você não pode comprar a casa pois seu salario é superior a 30 da sua renda!')