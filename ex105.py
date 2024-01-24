dicionario = dict()
def notas(*n,sit):
    dicionario.append(n)
    dicionario.append(len(n))
    maior = menor = 1
    media = 0
    for c in range(0,len(n)):
        if dicionario[c] > maior:
            maior = dicionario[c]
        if dicionario[c] < menor:
            menor = dicionario[c]
        media += dicionario[c]
    dicionario.append(maior)
    dicionario.append(menor)
    media=media/len(n)
    dicionario.append(media)
    if sit != '':
        dicionario.append(sit)
    return dicionario


#Programa Principal
print(notas(1,1,1,1,sit=True))
