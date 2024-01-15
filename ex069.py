idade = int(input('Digite a idade de uma pessoa: '))
sexo = input('Digite o sexo dessa mesma pessoa: [M/F]')
continuar = input('Você deseja continuar: [S/N]')

maior18 = 0
numHomens = 0
numMulheres = 0

if(idade > 18):
    maior18+=1
if(sexo == 'M'):
    numHomens+=1
if(sexo == 'F' and idade < 20):
     numMulheres+=1

if(continuar=='S'):
    while(continuar=='S'):
        idade = int(input('Digite a idade de uma pessoa: '))
        sexo = input('Digite o sexo dessa mesma pessoa: [M/F]')
        if(idade > 18):
            maior18+=1
        if(sexo == 'M'):
            numHomens+=1
        if(sexo == 'F' and idade < 20):
            numMulheres+=1
        continuar = input('Você deseja continuar: [S/N]')
print('{} pessoas tem mais de 18 anos, {} pessoas são homens e {} mulheres tem menos de 20 anos.'.format(maior18,numHomens,numMulheres))
