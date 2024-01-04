preco = input(float('Digite o preço do produto: '))
formaPagamento = input('Qual a forma de pagamento: ')
if formaPagamento == 'dinheiro' or formaPagamento == 'cheque':
    printf('Você tem 10% desconto então irá pagar {}'.format(preco*0.9))
elif formaPagamento == 'cartão':
    printf('Você tem 5% desconto então irá pagar {}'.format(preco*0.95))
elif formaPagamento == '2x cartão':
    print('Preço normap')
elif formaPagamento == '3x cartão':
    printf('Você tem de pagar 20% de juros, então irá pagar: {}'.format(preco*1.2))
