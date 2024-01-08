def eh_palindromo(frase):
    # Removendo os espaços da frase e convertendo para letras minúsculas
    frase = frase.replace(" ", "").lower()

    # Verificando se a frase é igual à sua inversa
    return frase == frase[::-1]


# Leitura da frase do usuário
frase = input("Digite uma frase para verificar se é um palíndromo: ")

if eh_palindromo(frase):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
