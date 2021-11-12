import math

while True:
    try:
        temp_ar = float(input('Informe a temperatura do ar em Celsius: '))
        vel_vento = float(input('Informe a velocidade do vento em Km/h: '))
    except ValueError:
        print('Erro. É nessário informar valores válidos!')
    else:
        break


def calc_sen_termica(t, v):
    s_termica = 13.12 + (0.6215 * t) - (11.37 * math.pow(v, 0.16)) + (0.3965 * (t * math.pow(v, 0.16)))
    return s_termica


print(f'Sensação térmica: {round(calc_sen_termica(temp_ar, vel_vento))} ')




