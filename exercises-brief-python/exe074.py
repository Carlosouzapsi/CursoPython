import math

x = int(input('Informe o valor de x: '))
palpite = ""
update_calculo = 0
valor_absoluto = 0
while True:
    if palpite != 'Bom o suficiente!':
        calculo = x / 2
        update_calculo += calculo
        media_calculo = update_calculo / calculo
        print(media_calculo)
        valor_absoluto = (calculo * calculo) - x
        if valor_absoluto == math.pow(10, -12):
            palpite = 'Bom o suficiente!'
            print(palpite)
    else:
        break
