velcarro = float(input('Digite a velocidade do carro:'))
velmaxPermitida = 80
valorMulta = (velcarro - velmaxPermitida) * 7
if velcarro > 80:
    print('Você foi multado! O limite de 80km foi excedido.')
    print('O valor da multa aplicada foi de R$ {}'.format(valorMulta))
print('A velocidade do seu carro era de {} km/h e estava dentro do limite estabelecido! Tenha um bom dia!'.format(velcarro))