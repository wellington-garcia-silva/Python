n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
opcao = int(input('Selhecione uma opção a seguir para proceder com o programa: 1 - Soma; 2 - multiplicr; 3 - Maior; 4 - Novos números; 5 - Sair.'))
while opcao != 5:
    if opcao == 1:
        print('A soma dos valores é {}.'.format(n1+n2))
    elif opcao == 2:
        print('A multiplicação dos números é: {}.'.format(n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O número 1 é maior que o número 2.')
        elif n2 > n1:
            print('O  número 2 é maior que o número 1.')
        else:
            print('Os números são iguais.')

    elif opcao == 4:
        n1 = float(input('Digite um novo número: '))
        n2 = float(input('Digite outro novo número: '))
    else:
        print('Opção incorreta, tente outra.')
    opcao = int(input('Selhecione uma opção a seguir para proceder com o programa: 1 - Soma; 2 - multiplicr; 3 - Maior; 4 - Novos números; 5 - Sair.'))
print('Fim do programa.')