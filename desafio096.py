def cab():
    print('-' * 30)
    print('CONTROLE DE TERRENOS')
    print('-' * 30)


def calc_area(l, c):
    area = l * c
    print('A área de um terreno de {} X {} é de {} m2'.format(l, c, area))


### PROGRAMA PRINCIPAL:
cab()
largura = int(input('Informe a largura do terreno: '))
comprimento = int(input('Informe o comprimemnto do terreno: '))
calc_area(largura, comprimento)




