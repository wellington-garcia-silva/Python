salario = input(float('Qual é seu salário: '))
if salario > 1250:
    salario = salario*1.1
    printf('Seu novo salário é de {} R$'.format(salario))
else:
    salario =  salario*1.15
    printf('Seu novo salário é de {} R$'.format(salario))
    