import math

frequencia = float(input('Informe o valor da frequência: '))
range1 = 3 * math.pow(10, 9)
range2 = 3 * math.pow(10, 12)
range3 = 4.3 * math.pow(10, 14)
range4 = 7.5 * math.pow(10, 14)
range5 = 3 * math.pow(10, 17)
range6 = 3 * math.pow(10, 19)

def verifica_freq(f):
    if f < range1:
        print('Radio Waves')
    elif f >= range1 and f < range2:
        print('Microwaves')
    elif f >= range2 and f < range3:
        print('Infrared Light')
    elif f >= range3 and f < range4:
        print('Visible Light')
    elif f >= range4 and f < range5:
        print('Ultraviolet Light')
    elif f >= range5 and f < range6:
        print('X - rays')
    elif f >= range6:
        print('Gamma Rays')


verifica_freq(frequencia)