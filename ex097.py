def escreva(palavra):
    a = len(palavra)
    a = a + 4
    print(f'{a*'~'}  ')
    print(f'  {palavra}  ')
    print(f'{a * '~'}')


palavra = str(input('Digite uma palavra: ')).upper()
escreva(palavra)