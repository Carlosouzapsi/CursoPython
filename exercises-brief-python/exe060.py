import math

ano = int(input('Informe o ano: '))

dia_semana = (ano + math.floor((ano - 1) / 4) - math.floor((ano - 1) / 100) + math.floor((ano - 1) / 400)) % 7


def verifica_dia_semana(d):
    if d == 0:
        print('DOMINGO')
    elif d == 1:
        print('SEGUNDA')
    elif d == 2:
        print('TERÇA')
    elif d == 3:
        print('QUARTA')
    elif d == 4:
        print('QUINTA')
    elif d == 5:
        print('SEXTA')
    elif d == 6:
        print('SABADO')


verifica_dia_semana(dia_semana)
