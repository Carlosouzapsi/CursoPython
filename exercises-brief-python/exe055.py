frequencia = float(input('Informe o valor do espectro de luz: '))

def verifica_frequencia(f):

    if f >= 380 and f < 450:
        print('Violeta')
    elif f >= 450 and f < 495:
        print('Azul')
    elif f >= 495 and f < 570:
        print('Verde')
    elif f >= 570 and f < 590:
        print('Amarelo')
    elif f >= 590 and f < 620:
        print('Laranja')
    elif f >= 620 and f <= 750:
        print('Vermelho')
    else:
        print('Faixa não especificada.')

verifica_frequencia(frequencia)


