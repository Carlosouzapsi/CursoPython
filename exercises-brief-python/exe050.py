mag = float(input('Informe a magnitude: '))

def verifica_mag(m):
    if m < 2:
        print('MICRO')
    elif m >= 2 and m < 3:
        print('MUITO MENOR')
    elif m >= 3 and m < 4:
        print('MENOR')
    elif m >= 4 and m < 5:
        print('LIGHT')
    elif m >=5 and m < 6:
        print('MODERADO')
    elif m >= 6 and m < 7:
        print('FORTE')
    elif m >= 7 and m < 8:
        print('MAIOR')
    elif m >= 8 and m < 10:
        print('GRANDE')
    elif m >= 10:
        print('METEÓRICO')

verifica_mag(mag)