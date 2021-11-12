pao = 3.69
desconto_pao = 3.69 - ((3.69 * 60) / 100)
valor_pao_velho = pao - desconto_pao
compra = int(input('Informe a quantidade de sacos de pão: '))


def output(c):
    total = c * valor_pao_velho
    print(f'Preço do pão fresco: R${pao:.2f}')
    print(f'Preço do pão envelhecido: R${valor_pao_velho:.2f}')
    print(f'Valor descontado do pão envelhecido: R${desconto_pao:.2f}')
    print(f'Valor total pago: R${total:.2f}')


output(compra)

