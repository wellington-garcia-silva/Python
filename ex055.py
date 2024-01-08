menor = 0
maior = 0
for c in range(0,5):
    peso = float(input('Digite um peso: '))
    if menor > peso:
        menor = peso
    if maior < peso:
        maior = peso
print('O maior peso é {} e o menor peso é {}'.format(maior,menor))
