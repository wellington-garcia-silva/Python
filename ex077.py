tupla = ['palavras','leite','manteiga','soro','fogo','fonema','piracicaba','lembrete','vassoura','praia']
for c in range(0,10):
    palavra = tupla[c]
    if 'a' in palavra:
        a = 'a'
        impressao = (f'Na palavra {palavra} temos {a} {''}{''}{''}{''}')#'
    if 'e' in palavra:
        e = 'e'
        #print(f'Na palavra {palavra} temos {}')
        impressao = (f'Na palavra {palavra} temos  {''}{e}{''}{''}{''}')
    if 'i' in palavra:
        i = 'i'
        impressao = (f'Na palavra {palavra} temos {''} {''}{i}{''}{''}')
    if 'o' in palavra:
        o = 'o'
        impressao = (f'Na palavra {palavra} temos {''} {''}{''}{o}{''}')
    if 'u' in palavra:
        u = 'u'
        impressao = (f'Na palavra {palavra} temos {''} {''}{''}{''}{u}')
    print(impressao)
