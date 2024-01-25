def leiaDinheiro():
    n1 = input('Digite um número: ')
    while n1.isnumeric() == False:
        n1 = input('Digite um número: ')
    return n1

