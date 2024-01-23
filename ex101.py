def voto(n1):
    n2 = 2024 - n1
    if n2 < 18:
        return f'Com {n2} anos o voto não é obrigatório.'
    elif n2 >= 18 and n2 < 65:
        return f'Com {n2} anos o voto é obrigatório.'
    else:
        return f'Com {n2} anos: VOTO OPCIONAL.'


#Programa Principal
print('-----------------------')
n1 = int(input('Em que ano vc nasceu: '))
print(voto(n1))
